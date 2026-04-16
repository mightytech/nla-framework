# Export Service

Converts an NLA project into a view-source plugin for Claude Code and Cowork.

> This spec describes intent. The compiled artifact (a prose skill plus a Python
> script) may contain implementation choices not reflected here. Those choices are
> valid unless they conflict with this spec. Items marked `[compiler]` are
> review-level decisions — the compiler's best judgment, subject to revision.
>
> This spec was drafted retrospectively in 2026-04-16 to capture the design intent
> behind the current export implementation (`core/skills/export.md` +
> `lib/export.py`). It is ready for a future compilation pass once the NLA compiler
> infrastructure is available as an installable package.

## What it does

Produces a self-contained plugin directory that mirrors the source NLA's structure,
with a synthesized identity document and rewritten paths so the plugin can be
installed and run outside the source environment. The plugin ships `HEAD` — the
committed state of the NLA — not the working tree.

## Philosophy

The plugin is a **view-source artifact**, not a compiled binary. It preserves the
NLA's structure so someone installing it can both use its skills and learn from its
patterns. This shapes every transform: structure is preserved unless there's a
specific reason to change it. See `reference/design-rationale.md` — "Plugin Export:
View-Source Model" for the full reasoning.

## How it works

1. Gather inputs. Read the NLA's identity (`CLAUDE.md`), overview, and config-spec
   if present. Inventory skills, submodules, and top-level directories.
2. Verify preconditions. Python 3 must be available on the host. The working tree
   must be clean (unless the user explicitly opts out — see Error handling).
3. Classify skills. Every skill in the project goes into one of three buckets:
   `exclude`, `domain`, or `keep_as_is`. See "Skill classification" below.
4. Synthesize plugin-specific content. Produce a foundation identity skill
   (replacing `CLAUDE.md`), an export metadata file (for traceability), and a
   user-facing README.
5. Transform the source into a plugin. Archive the committed tree, inline submodule
   content, rename `.claude/skills/` to `skills/`, remove plugin-redundant files,
   exclude skills in the `exclude` bucket, rewrite paths, adjust domain skill
   frontmatter, and place the synthesized files.
6. Verify the output. Check structural invariants (required files present,
   forbidden files absent, no unprefixed paths in skill content). Abort on
   verification failure — a leaked path is a bug, not a warning.
7. Move to the destination. Atomic replace of any prior plugin at that path.

## Skill classification

Every skill in `.claude/skills/` falls into one of three buckets:

- **`exclude`** — skills that are meaningless or confusing in a plugin. Directory
  removed entirely. Default: `install`, `update`, `export`, `create-app`,
  `install-app`, `startup` (startup is absorbed into the foundation skill since its
  purpose — loading context — happens automatically when the foundation skill has
  `user-invocable: false`).

- **`domain`** — skills a plugin user invokes to perform primary NLA tasks.
  `disable-model-invocation: true` is stripped from their frontmatter so Claude can
  auto-suggest them to non-technical users who don't know the skill's name. Default
  detection: any skill whose SKILL.md delegates to `app/[task].md` (the
  primary-task pattern).

- **`keep_as_is`** — dev tools, utility skills, extension skills (penny post,
  process helpers). Frontmatter is untouched. Users invoke them by name when
  needed.

Skills not listed in any bucket default to `keep_as_is` with a warning.

## Path rewriting

Intra-plugin references must survive installation. Relative paths in SKILL.md have
unreliable resolution in Claude Code (documented bugs). `${CLAUDE_PLUGIN_ROOT}` is
substituted before the LLM reads the skill, so it resolves reliably.

- Every top-level directory in the archived tree (excluding `skills/`,
  `.claude-plugin/`, `.git/`) gets a rewrite rule that prefixes bare references to
  it with `${CLAUDE_PLUGIN_ROOT}/`.
- Rewrite rules are idempotent — re-running does not double-prefix.
- Word-boundary awareness — `myapp/` is not rewritten as `app/`.
- Rewrites apply to every `.md` file in the tree, including synthesized files
  (foundation, README, export metadata). The AI can write natural paths; the
  script handles the prefixing.

## Submodule handling

Submodules are inlined — their `HEAD` content is archived into the plugin at their
original path, so the plugin has no external dependencies after installation.

- Each submodule is archived separately (`git archive` doesn't recurse into
  submodules natively).
- If a submodule's `HEAD` differs from the superproject's recorded commit pointer,
  emit a warning. The script archives what's on disk; the user decides whether to
  `git submodule update` and re-export.
- Nested submodules (submodules within submodules) are not supported. The NLA
  dependency model is flat; this constraint is inherited.

## File removal

Some files from the source don't belong in the plugin:

- **`CLAUDE.md`** is replaced by the synthesized foundation skill, not shipped
  alongside it. CLAUDE.md isn't auto-loaded in plugins; the foundation skill
  (with `user-invocable: false`) takes its role.
- **`.gitmodules`** is meaningless once submodule content is inlined.
- **`.claude/`** (the entire directory) — `.claude/skills/` is renamed to
  `skills/`; everything else under `.claude/` is development tooling
  (`settings.local.json`, etc.) that doesn't belong in a plugin.

## Gitignore-as-export-filter

Exclusions use the NLA's own declarations rather than a parallel
"don't ship" list in the export tool. This reduces duplicate configuration and
gives NLA authors a single source of truth.

- **`.gitignore`** determines what's committed vs. not. `git archive` only ships
  committed state, so gitignored files don't reach the plugin.
- **`.gitattributes export-ignore`** lets NLAs mark committed-but-not-shippable
  files (e.g., a `reference/` directory that maintainers want in the repo but not
  in the plugin). Honored by `git archive` automatically.

## Verification

After transforms, the script checks structural invariants:

- `.claude-plugin/plugin.json` exists and is valid JSON
- `skills/foundation/SKILL.md` exists
- `skills/` exists; `.claude/skills/` does not
- No skill `.md` file contains an unprefixed reference to any rewrite target
  directory
- Domain skills in the manifest lack `disable-model-invocation: true`

Verification failures abort the export — they indicate bugs in the rewriter or
missing transforms, not operational conditions.

## Error handling

- **Dirty working tree.** The plugin ships `HEAD`, not working state. If there are
  uncommitted changes, the script aborts with a clear message. The user may
  explicitly override (`--force` or `allow_dirty: true` in manifest) — their
  choice, not a default.
- **Missing Python 3.** The orchestrating skill checks availability at
  invocation and offers installation guidance. Python 3 is a point-of-use
  requirement, not a framework-wide prereq.
- **Missing synthesized files.** If the AI's synthesized foundation, README, or
  metadata files don't exist at the manifest-declared paths, the script aborts
  before any destructive operation.
- **Failed git operations.** `git archive` or submodule archiving failures abort
  with the git command's own error. No partial output.
- **Output directory exists.** The script refuses to overwrite unless `--force`.
  The orchestrator should confirm with the user before passing `--force`.

## Decisions

- **View-source, not compiled-artifact** framing. The plugin structurally mirrors
  the NLA. This rules out flattening thin wrappers into self-contained skill
  directories (which was the prior design). See design-rationale "Plugin Export:
  View-Source Model" for the full reasoning.
- **Hybrid AI + script architecture.** The orchestrating skill handles judgment
  (classification, synthesis, verification reporting). A Python 3 script handles
  mechanics (git archive, path rewriting, frontmatter surgery, file placement,
  structural verification). The split is strict: the AI doesn't perform transforms
  directly; the script doesn't make judgment calls.
- **Python 3, standard library only.** No pip, no venv, no requirements.txt. The
  script relies on `subprocess`, `os`, `pathlib`, `shutil`, `re`, `json`, and
  `tarfile`. Frontmatter surgery uses string splitting rather than a YAML parser —
  only one line gets removed from domain skill frontmatter, and the minimal
  approach is sufficient. If future transforms require YAML parsing, revisit the
  stdlib constraint.
- **Commits only.** The plugin ships `HEAD`, enforced by using `git archive HEAD`
  rather than walking the working tree. This ensures exports are reproducible and
  traceable to a specific commit.
- **Manifest JSON as the AI↔script handoff.** The AI writes a manifest file
  specifying plugin metadata, skill classifications, and paths to synthesized
  files. The script reads it. This format is inspectable, re-runnable after fixes,
  and decoupled from the AI's turn-taking.
- **Foundation skill synthesis is a judgment task.** The script cannot produce the
  foundation skill from rules — it requires weaving CLAUDE.md's identity, the
  framework's key principles, the project overview, config-spec, and the skills
  table into one coherent document in the NLA's voice. This stays on the AI side.
- **Top-level directory detection is automatic.** Rather than a hardcoded list of
  directories whose references get rewritten, the script scans the archived tree's
  root and generates rewrite rules for each directory it finds (excluding a small
  set of reserved names). This supports non-standard directories (`voices/`,
  `platforms/`, etc.) without code changes.
- **`[compiler]` Regex approach for path rewriting.** The current implementation
  uses Python `re` with negative lookbehinds for idempotency and word-boundary
  guards. Alternative approaches (AST-aware markdown parsing, explicit tokenizing)
  would be more robust but add complexity. The regex approach is sufficient for
  the markdown-with-backtick-code-spans that SKILL.md files actually contain.
  Revisit if malformed rewrites emerge from real NLA shapes.
- **`[compiler]` Staging directory location.** The AI picks a staging path (e.g.,
  `/tmp/nla-export-[name]-staging/`) and cleans up after success. The script
  doesn't care where staging lives — it reads from the paths the manifest
  declares. No fixed convention is prescribed.
- **Self-test and integration test as verification baseline.** The script includes
  `--self-test` (pure functions on synthetic inputs, ~1 second) and
  `--integration-test` (end-to-end with a real git fixture, ~2-3 seconds). These
  are runnable at any time. They're the minimum bar before the script is trusted;
  real exports remain the ultimate test.

## What it writes to

- **The plugin output directory** (user-specified, default `../[plugin-name]-plugin/`).
  Atomic replace of any prior content.
- **`stdout`** — a JSON status report on success or final failure. Parseable for
  automation.
- **`stderr`** — human-readable progress messages and warnings.
- **Exit code** — 0 for success; 1-7 for specific failure modes (manifest error,
  dirty tree, output exists, archive failure, submodule failure, synthesized file
  missing, verification failure). Exit codes are the machine-readable failure
  channel.

## Environment

- **Python 3**, standard library only. Present on most developer machines; point-of-use
  requirement, not framework-wide.
- **Git**, for `git archive`, `git status`, `git submodule`. Required (the source
  NLA must be a git repository).
- **POSIX-compatible filesystem**. The script uses `tarfile`, `subprocess.Popen`
  piping, and `shutil.move`. Windows support is not currently tested.
- **Claude Code** for the orchestrating skill (`core/skills/export.md`). The skill
  uses the `Bash`, `Read`, `Write`, and `Edit` tools.

## Reference

- Design rationale: `reference/design-rationale.md` — "Plugin Export: View-Source Model"
- Skill (AI orchestration): `core/skills/export.md`
- Script (mechanical implementation): `lib/export.py`
- Superseded design (archived): `reference/designs/export-skill-2026-02-20.md`
- Session log capturing the redesign: `reference/sessions/2026-04-16-export-simplification.md`
- Related design: "The Wrapper Spectrum" in `reference/design-rationale.md` —
  covers the thin-wrapper / annotated / ejected / redirected states export preserves
