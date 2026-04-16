#!/usr/bin/env python3
"""
NLA Plugin Exporter — Mechanical Phase

Given a manifest JSON describing an NLA's skill classification, synthesized content
paths, and export metadata, produce a view-source plugin directory suitable for
Claude Code and Cowork.

The AI (via core/skills/export.md) does the judgment work: inventory, classify
skills, synthesize the foundation skill / README / export-metadata, write the
manifest. This script does the mechanical work:

  1. Verify the source project's working tree is clean (unless --force)
  2. Archive the committed tree (`git archive HEAD`) into a temp dir
  3. Archive each submodule listed in the manifest into the same temp dir
  4. Rename `.claude/skills/` -> `skills/`
  5. Remove framework-only skills listed in manifest
  6. Auto-detect top-level directories and rewrite references to them:
       packages/... -> ${CLAUDE_PLUGIN_ROOT}/packages/...
       app/...      -> ${CLAUDE_PLUGIN_ROOT}/app/...
       (and any other top-level dir other than .git, skills, .claude-plugin, reference)
  7. Strip `disable-model-invocation: true` from domain skills' frontmatter
  8. Write .claude-plugin/plugin.json
  9. Place the AI's synthesized files (foundation SKILL.md, export-metadata.md, README)
 10. Verify: no unprefixed references leaked through, required files exist
 11. Move the temp tree to the final output directory

Exit codes:
  0  success
  1  manifest error (missing field, invalid JSON, etc.)
  2  working tree dirty and --force not set
  3  output directory exists and --force not set
  4  git archive failure
  5  submodule resolution failure
  6  synthesized file referenced in manifest not found on disk
  7  post-export verification failure

Usage:
  python3 lib/export.py --manifest <path> [--dry-run] [--force] [--verbose]
  python3 lib/export.py --self-test

Stdout: a single JSON status object on success (or on final failure).
Stderr: human-readable progress and warnings.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_MANIFEST_FIELDS = [
    "plugin_name",
    "plugin_description",
    "plugin_version",
    "source_project_path",
    "output_dir",
    "skills",
    "synthesized",
    "export_metadata",
]

# framework_submodule_path is optional — domain NLAs have one, but the framework
# itself (when exported as a view-source artifact) doesn't. Both cases are valid.

REQUIRED_SKILLS_FIELDS = ["exclude", "domain", "keep_as_is"]
REQUIRED_SYNTHESIZED_FIELDS = ["foundation_skill_md", "foundation_export_metadata", "readme"]

# Directories at the extracted tree's root that should NOT get a ${CLAUDE_PLUGIN_ROOT}/
# prefix rule generated for them. `reference/` is deliberately NOT in this set:
# skills reference `reference/design-rationale.md` etc., and those refs need
# prefixing to resolve reliably at runtime.
REWRITE_SKIP_DIRS = {".git", "skills", ".claude-plugin"}

# Files at the plugin root that should be removed after archive extraction.
# CLAUDE.md is replaced by the synthesized foundation skill.
# .gitmodules has no meaning once submodules are inlined.
PLUGIN_ROOT_FILES_TO_REMOVE = ["CLAUDE.md", ".gitmodules"]


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def log(msg: str, *, verbose: bool = True) -> None:
    """Progress/warnings go to stderr so stdout can carry a clean JSON status."""
    if verbose:
        print(msg, file=sys.stderr)


def run_git(cwd: Path, *args: str, capture: bool = True) -> str:
    """Run a git subcommand and return its stdout. Raises on non-zero exit."""
    result = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        check=True,
        capture_output=capture,
        text=True,
    )
    return result.stdout


def iter_markdown_files(root: Path) -> Iterable[Path]:
    """Yield every .md file under `root`."""
    for path in root.rglob("*.md"):
        if path.is_file():
            yield path


def emit_status(status: dict) -> None:
    """Write the machine-readable status to stdout."""
    print(json.dumps(status, indent=2))


# ---------------------------------------------------------------------------
# Manifest loading and validation
# ---------------------------------------------------------------------------

def load_manifest(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Manifest not found: {path}")
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Manifest is not valid JSON: {exc}")


def validate_manifest(manifest: dict) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")

    if "skills" in manifest:
        for sub in REQUIRED_SKILLS_FIELDS:
            if sub not in manifest["skills"]:
                errors.append(f"Missing required field: skills.{sub}")

    if "synthesized" in manifest:
        for sub in REQUIRED_SYNTHESIZED_FIELDS:
            if sub not in manifest["synthesized"]:
                errors.append(f"Missing required field: synthesized.{sub}")

    return errors


def check_synthesized_files_exist(manifest: dict) -> list[str]:
    """Return a list of missing synthesized files (empty if all present)."""
    missing = []
    for key, path_str in manifest.get("synthesized", {}).items():
        if not Path(path_str).exists():
            missing.append(f"synthesized.{key}: {path_str}")
    return missing


# ---------------------------------------------------------------------------
# Working-tree and output-dir checks
# ---------------------------------------------------------------------------

def check_working_tree(source: Path, allow_dirty: bool) -> list[str]:
    """
    Return a list of warnings about the working tree. If not allow_dirty and there
    are uncommitted changes, the caller should abort.
    """
    try:
        porcelain = run_git(source, "status", "--porcelain")
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"git status failed (not a git repo?): {exc}")

    warnings = []
    if porcelain.strip():
        warnings.append(
            "Working tree has uncommitted changes. The plugin ships HEAD, not working state."
        )

    return warnings


def prepare_output_dir(output: Path, force: bool) -> None:
    """Ensure the output parent exists. Refuse to overwrite unless --force."""
    if output.exists():
        if not force:
            raise SystemExit(
                f"Output directory already exists: {output}\n"
                f"Pass --force to overwrite."
            )
        log(f"Removing existing output directory: {output}")
        shutil.rmtree(output)
    output.parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Archiving: main tree + submodules
# ---------------------------------------------------------------------------

def archive_tree_into(source: Path, ref: str, dest: Path, strip_prefix: str = "") -> None:
    """
    Run `git archive <ref>` in `source` and extract the tar stream into `dest`.
    If `strip_prefix` is non-empty, entries are placed at `dest/<strip_prefix>/...`.
    """
    dest.mkdir(parents=True, exist_ok=True)

    # Stream: subprocess.Popen -> tarfile.open(fileobj=..., mode='r|')
    proc = subprocess.Popen(
        ["git", "archive", "--format=tar", ref],
        cwd=str(source),
        stdout=subprocess.PIPE,
    )
    assert proc.stdout is not None
    try:
        # mode='r|' is "open a non-seekable tar stream"
        with tarfile.open(fileobj=proc.stdout, mode="r|") as tar:
            extract_root = dest / strip_prefix if strip_prefix else dest
            extract_root.mkdir(parents=True, exist_ok=True)
            # filter='data' is the most restrictive; appropriate for git-archive
            # output (no special files or suspicious metadata expected).
            tar.extractall(path=str(extract_root), filter="data")
    finally:
        rc = proc.wait()
        if rc != 0:
            raise SystemExit(
                f"git archive failed (exit {rc}) in {source} for ref {ref}"
            )


def archive_submodule(source: Path, submodule_path: str, dest: Path) -> None:
    """
    Archive one submodule's HEAD into dest/<submodule_path>/.
    The submodule must be initialized in the source.
    """
    sub = source / submodule_path
    if not (sub / ".git").exists() and not (sub.is_dir() and any(sub.iterdir())):
        raise SystemExit(
            f"Submodule not initialized or empty: {sub}\n"
            f"Run `git submodule update --init` in {source} first."
        )

    log(f"  Archiving submodule: {submodule_path}")
    archive_tree_into(sub, "HEAD", dest, strip_prefix=submodule_path)


def check_submodule_sync(source: Path) -> list[str]:
    """
    Run `git submodule status` and return warnings for any submodules whose HEAD
    differs from the superproject's recorded commit. Leading '+' indicates drift.
    """
    warnings: list[str] = []
    try:
        output = run_git(source, "submodule", "status")
    except subprocess.CalledProcessError:
        return warnings  # no submodules configured
    for line in output.splitlines():
        if line.startswith("+"):
            warnings.append(
                f"Submodule HEAD differs from superproject pointer: {line.strip()}"
            )
    return warnings


# ---------------------------------------------------------------------------
# Transforms within the extracted tree
# ---------------------------------------------------------------------------

def rename_skills_dir(root: Path) -> None:
    src = root / ".claude" / "skills"
    dst = root / "skills"
    if not src.exists():
        raise SystemExit(
            f"Expected .claude/skills/ in archived tree but found nothing at {src}"
        )
    if dst.exists():
        raise SystemExit(
            f"Unexpected pre-existing `skills/` in archived tree at {dst}"
        )
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    # After moving skills out, .claude/ may still exist with settings files etc.
    # Remove the whole .claude dir — nothing inside it ships to plugins.
    claude_dir = root / ".claude"
    if claude_dir.exists():
        shutil.rmtree(claude_dir)


def remove_excluded_skills(root: Path, excluded: list[str]) -> list[str]:
    """Remove `skills/<name>/` for every `<name>` in `excluded`. Return names actually removed."""
    removed: list[str] = []
    for name in excluded:
        target = root / "skills" / name
        if target.exists() and target.is_dir():
            shutil.rmtree(target)
            removed.append(name)
    return removed


def detect_rewrite_dirs(root: Path) -> list[str]:
    """
    Return the list of top-level directory names that should receive a
    ${CLAUDE_PLUGIN_ROOT}/ prefix rule. Excludes well-known dirs that shouldn't
    be referenced from skill content in this way.
    """
    return sorted(
        p.name
        for p in root.iterdir()
        if p.is_dir() and p.name not in REWRITE_SKIP_DIRS and not p.name.startswith(".")
    )


def build_rewrite_rules(dirs: list[str]) -> list[tuple[re.Pattern[str], str]]:
    """
    For each directory name, build a regex that prefixes bare references with
    ${CLAUDE_PLUGIN_ROOT}/, guarding against already-prefixed paths and against
    matches inside longer words (e.g., don't rewrite 'myapp/' when matching 'app/').
    """
    rules: list[tuple[re.Pattern[str], str]] = []
    for d in dirs:
        # Negative lookbehinds: not already prefixed; not preceded by a word char.
        # We do NOT skip backticks — those are where paths typically live in skill
        # files, and we DO want to rewrite them.
        pattern = re.compile(
            r"(?<!\$\{CLAUDE_PLUGIN_ROOT\}/)(?<!\w)(" + re.escape(d) + r"/)"
        )
        replacement = r"${CLAUDE_PLUGIN_ROOT}/\1"
        rules.append((pattern, replacement))
    return rules


def rewrite_file(path: Path, rules: list[tuple[re.Pattern[str], str]]) -> int:
    """Apply all rules to file in place. Return total substitution count."""
    text = path.read_text()
    total = 0
    for pattern, repl in rules:
        text, count = pattern.subn(repl, text)
        total += count
    if total:
        path.write_text(text)
    return total


def rewrite_paths_in_tree(root: Path, rules: list[tuple[re.Pattern[str], str]], verbose: bool) -> int:
    """Rewrite paths in every .md file under root. Return total substitution count."""
    total = 0
    for md in iter_markdown_files(root):
        count = rewrite_file(md, rules)
        if count and verbose:
            log(f"  rewrites in {md.relative_to(root)}: {count}")
        total += count
    return total


# Matches a frontmatter line `disable-model-invocation: true` (optional whitespace).
_DISABLE_FLAG_RE = re.compile(r"^disable-model-invocation:\s*true\s*\n", re.MULTILINE)


def strip_disable_flag(skill_md_path: Path) -> bool:
    """
    Remove the `disable-model-invocation: true` line from the frontmatter block
    only. Returns True if the file was modified.
    """
    text = skill_md_path.read_text()
    if not text.startswith("---\n"):
        return False
    # Find the closing `---` on its own line after the opening one.
    end = text.find("\n---\n", 4)
    if end < 0:
        return False
    header = text[: end + 5]  # includes "\n---\n"
    body = text[end + 5 :]
    new_header, n = _DISABLE_FLAG_RE.subn("", header)
    if n == 0:
        return False
    skill_md_path.write_text(new_header + body)
    return True


def strip_domain_skill_frontmatter(root: Path, domain_skills: list[str]) -> list[str]:
    """Strip the flag from each domain skill. Return names where the strip happened."""
    touched: list[str] = []
    for name in domain_skills:
        skill_md = root / "skills" / name / "SKILL.md"
        if skill_md.exists() and strip_disable_flag(skill_md):
            touched.append(name)
    return touched


# ---------------------------------------------------------------------------
# Plugin.json and synthesized files
# ---------------------------------------------------------------------------

def write_plugin_json(root: Path, manifest: dict) -> None:
    plugin_json = {
        "name": manifest["plugin_name"],
        "description": manifest["plugin_description"],
        "version": manifest["plugin_version"],
    }
    out_dir = root / ".claude-plugin"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "plugin.json").write_text(json.dumps(plugin_json, indent=2) + "\n")


def place_synthesized_files(root: Path, synthesized: dict) -> None:
    """
    Copy AI-synthesized content into the plugin at the expected paths:
      foundation_skill_md        -> skills/foundation/SKILL.md
      foundation_export_metadata -> skills/foundation/export-metadata.md
      readme                     -> README.md
    """
    foundation_dir = root / "skills" / "foundation"
    foundation_dir.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(synthesized["foundation_skill_md"], foundation_dir / "SKILL.md")
    shutil.copyfile(synthesized["foundation_export_metadata"], foundation_dir / "export-metadata.md")
    shutil.copyfile(synthesized["readme"], root / "README.md")


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

# An unprefixed reference to one of the known top-level dirs in a skill file.
# Used only for post-export verification (flags rewriter misses).
_LEAK_PATTERNS: list[re.Pattern[str]] = []


def build_leak_patterns(rewrite_dirs: list[str]) -> list[re.Pattern[str]]:
    return [
        re.compile(
            r"(?<!\$\{CLAUDE_PLUGIN_ROOT\}/)(?<!\w)" + re.escape(d) + r"/"
        )
        for d in rewrite_dirs
    ]


def verify_output(root: Path, rewrite_dirs: list[str]) -> tuple[list[str], list[str]]:
    """Return (warnings, errors) lists."""
    warnings: list[str] = []
    errors: list[str] = []

    # Required files present.
    must_exist = [
        root / ".claude-plugin" / "plugin.json",
        root / "skills" / "foundation" / "SKILL.md",
        root / "README.md",
    ]
    for p in must_exist:
        if not p.exists():
            errors.append(f"Required file missing after export: {p.relative_to(root)}")

    # plugin.json parses.
    pj_path = root / ".claude-plugin" / "plugin.json"
    if pj_path.exists():
        try:
            pj = json.loads(pj_path.read_text())
            if "name" not in pj:
                errors.append("plugin.json missing 'name' field")
        except json.JSONDecodeError as e:
            errors.append(f"plugin.json is not valid JSON: {e}")

    # Skills directory exists; .claude/skills does not.
    if not (root / "skills").exists():
        errors.append("skills/ directory missing")
    if (root / ".claude" / "skills").exists():
        errors.append(".claude/skills/ still present (rename did not happen)")

    # Scan skill markdown for unprefixed references.
    leak_patterns = build_leak_patterns(rewrite_dirs)
    for md in iter_markdown_files(root / "skills"):
        text = md.read_text()
        for pat in leak_patterns:
            if pat.search(text):
                errors.append(
                    f"Unprefixed reference in {md.relative_to(root)} "
                    f"(pattern {pat.pattern}) — rewriter missed it"
                )
                break

    return warnings, errors


# ---------------------------------------------------------------------------
# Main flow
# ---------------------------------------------------------------------------

def do_export(manifest: dict, args: argparse.Namespace) -> dict:
    source = Path(manifest["source_project_path"]).resolve()
    output = Path(manifest["output_dir"]).resolve()

    all_warnings: list[str] = []

    # 1. Pre-flight.
    log("Checking working tree...")
    tree_warnings = check_working_tree(source, manifest.get("allow_dirty", False))
    if tree_warnings and not args.force and not manifest.get("allow_dirty", False):
        raise SystemExit(
            "\n".join(tree_warnings)
            + "\nCommit first, or pass --force / set manifest.allow_dirty = true."
        )
    all_warnings.extend(tree_warnings)
    all_warnings.extend(check_submodule_sync(source))

    # 2. Synthesized files present.
    missing = check_synthesized_files_exist(manifest)
    if missing:
        raise SystemExit("Synthesized files missing:\n  " + "\n  ".join(missing))

    # 3. Prepare output.
    prepare_output_dir(output, args.force)

    # 4. Archive into temp.
    with tempfile.TemporaryDirectory(prefix="nla-export-") as tmp:
        temp_root = Path(tmp) / "tree"
        log(f"Archiving HEAD from {source}...")
        archive_tree_into(source, "HEAD", temp_root)

        submodules: list[str] = []
        if "framework_submodule_path" in manifest:
            submodules.append(manifest["framework_submodule_path"])
        submodules.extend(manifest.get("additional_submodule_paths", []))
        log(f"Archiving {len(submodules)} submodule(s)...")
        for sub in submodules:
            try:
                archive_submodule(source, sub, temp_root)
            except SystemExit:
                raise
            except Exception as exc:
                raise SystemExit(f"Submodule archive failed for {sub}: {exc}")

        # 5. Rename .claude/skills -> skills (and drop rest of .claude/).
        log("Renaming .claude/skills/ -> skills/...")
        rename_skills_dir(temp_root)

        # 5a. Remove plugin-redundant files at root (CLAUDE.md replaced by foundation,
        #     .gitmodules meaningless once submodules are inlined).
        root_removed: list[str] = []
        for rel in PLUGIN_ROOT_FILES_TO_REMOVE:
            target = temp_root / rel
            if target.exists():
                target.unlink()
                root_removed.append(rel)
        if root_removed:
            log(f"Removed plugin-redundant root files: {root_removed}")

        # 6. Remove excluded skills.
        excluded = manifest["skills"]["exclude"]
        removed = remove_excluded_skills(temp_root, excluded)
        log(f"Excluded skills removed: {removed}")

        # 7. Auto-detect top-level dirs for path rewrites; build rules.
        rewrite_dirs = detect_rewrite_dirs(temp_root)
        log(f"Path rewrite targets: {rewrite_dirs}")
        rules = build_rewrite_rules(rewrite_dirs)

        # 8. Strip disable-model-invocation from domain skill frontmatter.
        touched = strip_domain_skill_frontmatter(temp_root, manifest["skills"]["domain"])
        log(f"Domain skills (flag stripped): {touched}")

        # 9. Write plugin.json.
        write_plugin_json(temp_root, manifest)

        # 10. Place synthesized files.
        place_synthesized_files(temp_root, manifest["synthesized"])

        # 11. Rewrite paths across everything (including synthesized content, which
        #     is why this runs AFTER placement). Idempotent via the lookbehind guards.
        log("Rewriting paths...")
        total = rewrite_paths_in_tree(temp_root, rules, verbose=args.verbose)
        log(f"Total path substitutions: {total}")

        # 12. Verify.
        v_warnings, v_errors = verify_output(temp_root, rewrite_dirs)
        all_warnings.extend(v_warnings)
        if v_errors:
            raise SystemExit("Verification failed:\n  " + "\n  ".join(v_errors))

        # 13. Move to final.
        if args.dry_run:
            log("(dry-run) Skipping move to final output.")
        else:
            shutil.move(str(temp_root), str(output))

    return {
        "status": "ok",
        "plugin_name": manifest["plugin_name"],
        "output": str(output),
        "excluded_skills": removed,
        "domain_skills_touched": touched,
        "path_substitutions": total,
        "warnings": all_warnings,
    }


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def run_self_test() -> int:
    """
    Exercise the pure functions on synthetic inputs. No git operations.
    Returns 0 on pass, nonzero on failure.
    """
    failures: list[str] = []

    # Rewrite rule idempotency and scope.
    rules = build_rewrite_rules(["app", "packages"])
    cases = [
        # (input, expected)
        ("Read `app/overview.md`.", "Read `${CLAUDE_PLUGIN_ROOT}/app/overview.md`."),
        ("See packages/nla-framework/core/skills/startup.md",
         "See ${CLAUDE_PLUGIN_ROOT}/packages/nla-framework/core/skills/startup.md"),
        # Idempotent: already-prefixed should not double-prefix.
        ("${CLAUDE_PLUGIN_ROOT}/app/shared/voice.md",
         "${CLAUDE_PLUGIN_ROOT}/app/shared/voice.md"),
        # Word-boundary: don't match 'myapp/' as 'app/'.
        ("myapp/foo", "myapp/foo"),
        # Word-boundary: don't match 'somepackages/' as 'packages/'.
        ("somepackages/foo", "somepackages/foo"),
        # Multiple matches on one line.
        ("app/ and packages/ on one line",
         "${CLAUDE_PLUGIN_ROOT}/app/ and ${CLAUDE_PLUGIN_ROOT}/packages/ on one line"),
    ]
    for src, expected in cases:
        actual = src
        for pat, repl in rules:
            actual = pat.sub(repl, actual)
        if actual != expected:
            failures.append(f"rewrite:\n  input:    {src!r}\n  expected: {expected!r}\n  actual:   {actual!r}")

    # Frontmatter strip.
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)

        # Case 1: domain skill with the flag — should be stripped.
        f1 = tmp / "domain.md"
        f1.write_text(
            "---\n"
            "name: compose\n"
            "description: Write something\n"
            "disable-model-invocation: true\n"
            "---\n"
            "# Compose\n"
            "disable-model-invocation: true is safe in body.\n"
        )
        if not strip_disable_flag(f1):
            failures.append("strip_disable_flag returned False for a file that has the flag")
        text = f1.read_text()
        # Header should lack the flag.
        _, _, after_open = text.partition("---\n")
        header, _, body = after_open.partition("\n---\n")
        if "disable-model-invocation" in header:
            failures.append("flag not removed from frontmatter")
        if "disable-model-invocation: true is safe in body" not in body:
            failures.append("body content was accidentally modified")

        # Case 2: file without frontmatter — no-op.
        f2 = tmp / "no-frontmatter.md"
        f2.write_text("# Just content\n")
        if strip_disable_flag(f2):
            failures.append("strip_disable_flag returned True for a file without frontmatter")

        # Case 3: frontmatter but no flag — no-op.
        f3 = tmp / "no-flag.md"
        original = "---\nname: x\n---\n# body\n"
        f3.write_text(original)
        if strip_disable_flag(f3):
            failures.append("strip_disable_flag returned True for a file without the flag")
        if f3.read_text() != original:
            failures.append("file modified despite no flag to remove")

    # Top-level dir detection.
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for d in ("app", "packages", "lib", ".claude-plugin", "reference", "skills", ".git"):
            (tmp / d).mkdir()
        detected = detect_rewrite_dirs(tmp)
        # reference/ IS a rewrite target — skills reference it and the refs need
        # prefixing. Only .git, skills, .claude-plugin are skipped.
        expected = ["app", "lib", "packages", "reference"]
        if detected != expected:
            failures.append(f"detect_rewrite_dirs:\n  expected: {expected}\n  actual:   {detected}")

    # Manifest validation.
    errors = validate_manifest({})
    if not errors:
        failures.append("validate_manifest: empty manifest should yield errors")

    good = {
        "plugin_name": "x",
        "plugin_description": "x",
        "plugin_version": "1.0.0",
        "source_project_path": "/tmp/x",
        "output_dir": "/tmp/y",
        "framework_submodule_path": "packages/nla-framework",
        "skills": {"exclude": [], "domain": [], "keep_as_is": []},
        "synthesized": {
            "foundation_skill_md": "/tmp/a",
            "foundation_export_metadata": "/tmp/b",
            "readme": "/tmp/c",
        },
        "export_metadata": {},
    }
    errors = validate_manifest(good)
    if errors:
        failures.append(f"validate_manifest: good manifest rejected: {errors}")

    if failures:
        print("SELF-TEST FAILED:", file=sys.stderr)
        for f in failures:
            print("  - " + f, file=sys.stderr)
        return 1
    print("SELF-TEST PASSED", file=sys.stderr)
    return 0


# ---------------------------------------------------------------------------
# Integration test — exercises the git-integrated path end-to-end.
# ---------------------------------------------------------------------------

def _git_commit(repo: Path, msg: str) -> None:
    """Commit with test identity inline (no rely on global git config)."""
    run_git(
        repo,
        "-c", "user.email=test@example.com",
        "-c", "user.name=test",
        "commit", "-q", "-m", msg,
    )


def run_integration_test() -> int:
    """
    Build a minimal fixture NLA (with a real git submodule), run the full export
    flow end-to-end, and assert structural invariants on the output.
    Returns 0 on pass, nonzero on failure. ~2-3 seconds.
    """
    failures: list[str] = []

    with tempfile.TemporaryDirectory(prefix="nla-export-itest-") as td:
        workspace = Path(td)
        fixture = workspace / "fixture-nla"
        submodule = workspace / "fixture-sub"
        staging = workspace / "staging"
        output = workspace / "plugin"
        staging.mkdir()

        # -- 1. Build the submodule repo -----------------------------------
        submodule.mkdir()
        run_git(submodule, "init", "-q", "-b", "main")
        (submodule / "core").mkdir()
        (submodule / "core" / "skills").mkdir()
        (submodule / "core" / "nla-foundations.md").write_text("# NLA Foundations (fixture)\n")
        (submodule / "core" / "skills" / "maintain.md").write_text("# Maintain (fixture)\n")
        (submodule / "core" / "skills" / "startup.md").write_text("# Startup (fixture)\n")
        run_git(submodule, "add", "-A")
        _git_commit(submodule, "initial")

        # -- 2. Build the main NLA repo -----------------------------------
        fixture.mkdir()
        run_git(fixture, "init", "-q", "-b", "main")

        (fixture / "CLAUDE.md").write_text("# Test NLA\nRead `app/overview.md`.\n")

        (fixture / "app").mkdir()
        (fixture / "app" / "overview.md").write_text(
            "# Overview\nSee `app/compose.md` and `packages/nla-framework/core/skills/startup.md`.\n"
        )
        (fixture / "app" / "compose.md").write_text(
            "# Compose\nRead `packages/nla-framework/core/skills/startup.md`.\n"
        )

        skills = fixture / ".claude" / "skills"
        skills.mkdir(parents=True)

        # Domain skill — should have flag stripped.
        (skills / "compose").mkdir()
        (skills / "compose" / "SKILL.md").write_text(
            "---\n"
            "name: compose\n"
            "description: Start a composition\n"
            "disable-model-invocation: true\n"
            "---\n"
            "Read and follow `app/compose.md`.\n"
        )
        # Dev tool — should keep flag.
        (skills / "maintain").mkdir()
        (skills / "maintain" / "SKILL.md").write_text(
            "---\n"
            "name: maintain\n"
            "description: Maintain the NLA\n"
            "disable-model-invocation: true\n"
            "---\n"
            "Read and follow `packages/nla-framework/core/skills/maintain.md`.\n"
        )
        # Framework-only — should be excluded.
        (skills / "export").mkdir()
        (skills / "export" / "SKILL.md").write_text(
            "---\n"
            "name: export\n"
            "disable-model-invocation: true\n"
            "---\n"
            "Read and follow `packages/nla-framework/core/skills/export.md`.\n"
        )

        # -- 3. Add the submodule + commit everything ---------------------
        # protocol.file.allow=always is needed for file:// submodules on modern git
        # (CVE-2022-39253 mitigation disabled file protocol for submodules by default).
        run_git(
            fixture,
            "-c", "protocol.file.allow=always",
            "submodule", "add", "-q", str(submodule), "packages/nla-framework",
        )
        run_git(fixture, "add", "-A")
        _git_commit(fixture, "initial NLA")

        # -- 4. Synthesized files ------------------------------------------
        foundation_md = staging / "foundation-SKILL.md"
        foundation_md.write_text(
            "---\n"
            "name: foundation\n"
            "description: Test NLA identity\n"
            "user-invocable: false\n"
            "---\n"
            "# Test NLA\nFoundation body.\n"
        )
        foundation_metadata = staging / "export-metadata.md"
        foundation_metadata.write_text("# Export Metadata\n- source: fixture\n")
        readme = staging / "README.md"
        readme.write_text("# Test Plugin\n")

        # -- 5. Manifest ---------------------------------------------------
        manifest = {
            "plugin_name": "test-plugin",
            "plugin_description": "Integration test plugin",
            "plugin_version": "1.0.0",
            "source_project_path": str(fixture),
            "output_dir": str(output),
            "framework_submodule_path": "packages/nla-framework",
            "skills": {
                "exclude": ["export"],
                "domain": ["compose"],
                "keep_as_is": ["maintain"],
            },
            "synthesized": {
                "foundation_skill_md": str(foundation_md),
                "foundation_export_metadata": str(foundation_metadata),
                "readme": str(readme),
            },
            "export_metadata": {
                "framework_commit": "fixture",
                "export_date": "2026-04-16",
            },
        }

        # -- 6. Run the full export ---------------------------------------
        args = argparse.Namespace(dry_run=False, force=False, verbose=False)
        try:
            result = do_export(manifest, args)
        except SystemExit as exc:
            failures.append(f"do_export raised SystemExit: {exc.code!r}")
            print("INTEGRATION TEST FAILED:", file=sys.stderr)
            for f in failures:
                print("  - " + f, file=sys.stderr)
            return 1

        # -- 7. Assertions on output structure ----------------------------

        def missing(rel: str) -> bool:
            return not (output / rel).exists()

        # Required files.
        for rel in [".claude-plugin/plugin.json",
                    "skills/foundation/SKILL.md",
                    "skills/foundation/export-metadata.md",
                    "README.md",
                    "skills/compose/SKILL.md",
                    "skills/maintain/SKILL.md",
                    "app/overview.md",
                    "app/compose.md",
                    "packages/nla-framework/core/nla-foundations.md",
                    "packages/nla-framework/core/skills/startup.md"]:
            if missing(rel):
                failures.append(f"required file missing: {rel}")

        # Things that should NOT exist.
        if (output / ".claude").exists():
            failures.append(".claude/ still present in output")
        if (output / "skills" / "export").exists():
            failures.append("excluded skill `export` still present")
        if (output / "CLAUDE.md").exists():
            failures.append("CLAUDE.md still at plugin root (should be replaced by foundation)")
        if (output / ".gitmodules").exists():
            failures.append(".gitmodules still at plugin root (submodules are inlined)")

        # plugin.json correctness.
        pj_path = output / ".claude-plugin" / "plugin.json"
        if pj_path.exists():
            pj = json.loads(pj_path.read_text())
            if pj.get("name") != "test-plugin":
                failures.append(f"plugin.json name wrong: {pj.get('name')!r}")
            if pj.get("version") != "1.0.0":
                failures.append(f"plugin.json version wrong: {pj.get('version')!r}")

        # Domain skill: flag stripped, paths rewritten.
        cs_path = output / "skills" / "compose" / "SKILL.md"
        if cs_path.exists():
            cs_text = cs_path.read_text()
            if "disable-model-invocation: true" in cs_text:
                failures.append("compose still has disable-model-invocation flag")
            if "${CLAUDE_PLUGIN_ROOT}/app/compose.md" not in cs_text:
                failures.append("compose path not rewritten to CLAUDE_PLUGIN_ROOT")

        # Dev tool: flag retained, paths rewritten.
        mt_path = output / "skills" / "maintain" / "SKILL.md"
        if mt_path.exists():
            mt_text = mt_path.read_text()
            if "disable-model-invocation: true" not in mt_text:
                failures.append("maintain lost its disable-model-invocation flag (should have kept)")
            if "${CLAUDE_PLUGIN_ROOT}/packages/nla-framework/core/skills/maintain.md" not in mt_text:
                failures.append("maintain path not rewritten")

        # Non-skill markdown also rewritten (app/compose.md).
        ac_path = output / "app" / "compose.md"
        if ac_path.exists():
            ac_text = ac_path.read_text()
            if "${CLAUDE_PLUGIN_ROOT}/packages/nla-framework" not in ac_text:
                failures.append("app/compose.md path not rewritten")

        # Status report shape.
        if result.get("status") != "ok":
            failures.append(f"do_export status not ok: {result.get('status')!r}")
        if "export" not in result.get("excluded_skills", []):
            failures.append(f"excluded_skills report missing 'export': {result.get('excluded_skills')!r}")
        if "compose" not in result.get("domain_skills_touched", []):
            failures.append(f"domain_skills_touched missing 'compose': {result.get('domain_skills_touched')!r}")

    if failures:
        print("INTEGRATION TEST FAILED:", file=sys.stderr)
        for f in failures:
            print("  - " + f, file=sys.stderr)
        return 1
    print("INTEGRATION TEST PASSED", file=sys.stderr)
    return 0


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="NLA plugin exporter (mechanical phase)",
    )
    p.add_argument("--manifest", type=Path, help="Path to manifest JSON")
    p.add_argument("--dry-run", action="store_true", help="Do everything except the final move")
    p.add_argument("--force", action="store_true", help="Allow dirty tree / overwrite output")
    p.add_argument("--verbose", action="store_true", help="Log every rewrite")
    p.add_argument("--self-test", action="store_true", help="Run unit tests and exit")
    p.add_argument(
        "--integration-test",
        action="store_true",
        help="Run end-to-end test with a git fixture and exit (~2-3 seconds)",
    )
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if args.self_test:
        return run_self_test()

    if args.integration_test:
        return run_integration_test()

    if not args.manifest:
        raise SystemExit("Either --manifest <path>, --self-test, or --integration-test is required.")

    manifest = load_manifest(args.manifest)
    errors = validate_manifest(manifest)
    if errors:
        raise SystemExit("Manifest validation failed:\n  " + "\n  ".join(errors))

    result = do_export(manifest, args)
    emit_status(result)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except SystemExit as exc:
        # Re-raise clean exits; map string exits to stderr+exit 1.
        if isinstance(exc.code, int):
            sys.exit(exc.code)
        else:
            print(exc.code, file=sys.stderr)
            sys.exit(1)
