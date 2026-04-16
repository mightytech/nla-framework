# Maintenance Session: Export Simplification — View Source, Not Compile

**Date:** 2026-04-16
**Status:** In Progress

## Intent

Resolve the 2026-04-16 friction log entry asking whether `/export` still needs to
flatten thin wrappers under the packages/submodules model. The underlying question
turns out to be bigger: what *kind* of artifact is a plugin, now that the original
constraint (external references fail) has been dissolved?

This session also converges with feedback item #9 (Export hybrid approach: script
for mechanical work, AI for judgment), which was pending a /think session before
implementation. The redesign produces a joint resolution: the view-source framing
clarifies *what* the plugin is, and the hybrid script approach clarifies *how*
it's built. Both are addressed together.

Two reframings emerged from the /think session, and both shape the implementation:

### Reframing 1: Compile → View Source

The original export design framed plugins as *compiled artifacts*: "NLA project is
source code, plugin is the binary." That analogy was doing double duty. It meant:
(a) we transform source to distribution artifact (still true), AND (b) the artifact
has no structural resemblance to the source (was a consequence of the sibling-directory
model, not essential to plugins).

Packages/submodules dissolved (b). The better analogy is **view source in a browser**:
the plugin is the NLA in an inspectable, usable form. Structure is preserved enough
to read; tweaks are expected to be ephemeral (like dev tools); heavy customization
happens by editing the NLA in Claude Code and re-exporting.

This clarifies priorities (confirmed with the user):
- **Primary:** non-technical users can use NLAs via plugins
- **Secondary:** technical users can inspect plugin structure to learn patterns, with
  light edit capability as a bonus (like browser dev tools)
- **Explicitly deprioritized:** plugin-side persistent customization (handled by
  re-export from source), self-update, in-plugin feedback submission — nice to have,
  far from required

### Reframing 2: Gitignore as Export Filter

The NLA's own `.gitignore` declares what's private (config.md, config/, settings,
etc.). Using gitignore to drive export exclusions means we're not inventing a second,
parallel "don't ship these" list. Structurally consistent with the paradigm: the
project's own declarations become the source of truth for what ships.

This also means `config.md` naturally doesn't ship (it's the developer's preferences,
not the plugin user's). `config-spec.md` does ship (it's committed — tells the user
what's configurable).

## Decisions Made

- **"View source" replaces "compile"** as the guiding metaphor for plugins.
- **Structure-preserving export.** Plugin mirrors NLA structure with foundation +
  plugin.json added and some transforms, rather than flattening everything into
  self-contained skills.
- **`${CLAUDE_PLUGIN_ROOT}` prefixed paths** for cross-skill file references. This is
  the documented, reliable way to construct intra-plugin paths. Relative paths in
  SKILL.md have known resolution bugs (issues #17741, #11011) and are not safe.
- **Gitignore drives export exclusions.** Anything gitignored doesn't ship.
  `.gitattributes` `export-ignore` can be used for files that belong in the repo
  but not in plugins (e.g., `reference/`).
- **Commits only for export.** `git archive HEAD` (or equivalent) — exports ship
  a specific commit. The export skill checks for uncommitted changes and warns.
- **Foundation skill remains a synthesis.** CLAUDE.md doesn't auto-load in plugins,
  so foundation/SKILL.md with `user-invocable: false` is still needed. The synthesis
  can be lighter under the new framing — it doesn't need to strip all framework
  references, since `packages/` is visible in the plugin.
- **Dev tools still ship.** The "view source" framing makes this *more* coherent, not
  less: the tooling is part of what makes the NLA inspectable. Browser dev tools
  analogy sharpens.
- **Framework-only skills still excluded.** `/install`, `/update`, `/export` are
  meaningless without the framework development context.
- **Submodule content resolved, not pointers.** The plugin's `packages/` contains
  files, not submodule references. (Implementation detail, noted to avoid confusion.)
- **Hybrid AI + script architecture.** Mechanical transforms (tree copy, path
  rewrites, frontmatter adjustments, plugin.json generation) handled by a Python
  script. Judgment work (skill classification, foundation synthesis, README,
  verification) stays with the AI. The AI bookends the script: inventory →
  classify → write manifest → synthesize foundation + README → invoke script →
  verify. Resolves feedback item #9 jointly with this redesign.
- **Python 3, stdlib only.** The script uses only Python 3 stdlib (`subprocess`,
  `os`, `pathlib`, `shutil`, `re`, `json`). No pip, no venv, no requirements.txt.
  Frontmatter is handled via string splitting since we only remove specific lines.
- **Python 3 as point-of-use requirement.** Export checks for Python 3 availability
  at invocation and offers to help install it if missing. Not a framework-wide
  prerequisite — only needed when you run `/export`.
- **Script placement.** `packages/nla-framework/lib/export.py` (exact path is a
  plan-mode detail). Lives in the framework, updates with the framework via
  `/update`. Domain projects never edit it.

## Changes Made

### Phase A — Design rationale (complete)

- Added supersession marker at the top of "Plugin Export: NLA as Source, Plugin as
  Artifact" noting the 2026-04-16 revision; framing preserved, mechanics superseded.
- Added supersession marker below the old structural mapping table pointing to the
  new one.
- Strengthened "Dev tools always ship" with a view-source reinforcement parenthetical.
- Inserted new top-level section "Plugin Export: View-Source Model" before "The
  Wrapper Spectrum" — covers what changed, new model, updated structural mapping,
  why it's better, non-technical primacy, hybrid AI+script mechanism, what's
  lost/gained, open questions.
- Added a view-source paragraph to "Ejection is not forking" noting all four wrapper
  states survive export without special handling.

### Phase B — lib/export.py (complete)

- Created `lib/export.py` (~750 lines with comments/docstrings/self-test; ~500 lines
  of core logic). Stdlib only. Establishes the framework-root `lib/` convention.
- CLI: `--manifest`, `--dry-run`, `--force`, `--verbose`, `--self-test`.
- Flow: load/validate manifest → check working tree and submodule sync → archive
  main tree + submodules into temp via `git archive | tarfile` → rename
  `.claude/skills/` to `skills/` → remove excluded skills → auto-detect top-level
  dirs → rewrite paths → strip domain skill frontmatter → write `plugin.json` →
  place synthesized files (foundation + export-metadata + README) → verify → move
  to final output.
- Self-test exercises pure functions on synthetic inputs: rewrite rule
  idempotency, word-boundary handling, multi-match lines, frontmatter strip with
  various edge cases, top-level dir detection, manifest validation. Passes.
- Integration test (`--integration-test`) builds a minimal fixture NLA with a real
  git submodule, runs the full export end-to-end, asserts structural invariants
  on the output (required files present, excluded skills absent, flag stripped
  from domain skills only, paths rewritten, plugin.json correct, status report
  shape). Passes. ~2-3 seconds.
- Exit codes 0–7 per the plan.
- Status JSON emitted on stdout; progress to stderr.
- Total: 984 lines (core ~500, self-test ~150, integration test ~235, comments/docstrings the rest).

### Phase D — First real export: framework-as-plugin test (complete)

Exported the framework itself as a view-source plugin to stress-test the pipeline
before any domain NLA has migrated. The framework has no `app/` (uses `core/`),
no `overview.md`, no domain skills, and a mix of framework-only and extension
skills — each an edge case.

The test surfaced three bugs and produced three follow-up commits:

1. **`framework_submodule_path` was required** in manifest validation, but the
   framework has no framework submodule (it IS the framework). Made the field
   optional; both domain NLAs (with a framework submodule) and the framework
   itself (with only extension submodules) work cleanly.
2. **Path rewrites ran before synthesized file placement**, so foundation
   SKILL.md and README.md had unprefixed `core/` paths that tripped verification.
   Moved the rewrite pass to the final step (after placement), so synthesized
   content benefits from the same auto-detection. Idempotent via lookbehinds.
3. **CLAUDE.md and `.gitmodules` shipped at plugin root.** CLAUDE.md was supposed
   to be replaced by foundation, not coexist. `.gitmodules` has no meaning once
   submodules are inlined. Added explicit removal; integration test asserts
   their absence.
4. **`reference/` was in REWRITE_SKIP_DIRS**, so skill refs like
   `reference/design-rationale.md` stayed unprefixed (unreliable at runtime per
   Claude Code path bugs). Removed from skip; those refs now prefix correctly.

Final result: framework plugin produced at `../nla-framework-plugin/` — 190
files, 1.4MB, 1107 path substitutions, zero verification warnings. All 16
keep_as_is skills plus foundation present; 5 framework-only skills correctly
excluded. Path rewrites verified via grep (no unprefixed refs in skill files
at plugin root).

Observations:

- `CONTRIBUTING.md`, `config.md`, `config-spec.md`, `config/`, `VERSION`,
  `LICENSE` all shipped because they're committed at framework root. Under
  the view-source framing, this is correct, not a gap: someone inspecting the
  plugin sees the full set of committed files, which is exactly what
  "view-source" means. `CONTRIBUTING.md` is teaching material; `VERSION` is
  diagnostic; `config-spec.md` is design documentation. For domain NLAs,
  `config.md`/`config/` are gitignored per convention so they won't ship at
  all; no action needed. The escape hatches (`.gitignore`, `.gitattributes
  export-ignore`) remain available for cases where a project has specific
  files they want withheld — but that's opt-in, not default.
- Nested `packages/nla-penny-post/.claude/skills/*/SKILL.md` files ship as
  submodule content and retain their original (submodule-relative) paths.
  Correct under view-source framing — they're informational files, not active
  plugin skills (Claude Code scans `skills/` at plugin root).

### Phase C — core/skills/export.md + archival + install/skills-intent.md (complete)

- Archived pre-revision skill to `reference/designs/export-skill-2026-02-20.md`
  (faithful copy; `reference/designs/` already existed with prior archived designs).
- Rewrote `core/skills/export.md` in the five-phase flow: Gather → Classify →
  Synthesize → Execute → Verify. 341 lines (down from 360; reduced net of added
  Python 3 check, manifest schema, error-code guide). Skill now orchestrates the
  script rather than performing transforms directly.
- Preserved: foundation synthesis guidance (five sources), README synthesis,
  runtime validation pattern (`env -u CLAUDECODE claude -p ...`).
- Removed: per-skill transitive dependency resolution, path rewrite rules in prose,
  frontmatter adjustment instructions, supporting-files bundling logic, manual
  verification checklist — all script-owned now.
- Updated `install/skills-intent.md` description from "self-contained plugin with
  all dependencies resolved" (flattening-era language) to "structure-preserving
  plugin with the framework and installed packages bundled."
- Added update note to `install/update-notes.md` describing the behavior change
  for domain projects, what's preserved vs. what's new, and the "re-export to
  pick up the new shape" guidance.

## Blast Radius

- `core/skills/export.md`: major revision (all domain projects using export)
- `reference/design-rationale.md`: "Plugin Export: NLA as Source, Plugin as Artifact"
  section needs revision — the "compile analogy" and "structural mapping" descriptions
  are superseded
- `install/skills-intent.md`: export wrapper reference (if changed)
- Plugin format: anyone who has exported a plugin under the old design would need to
  re-export to get the new structure (not a migration concern — re-export is the
  normal update path)

## Friction Log Entries Processed

- 2026-04-16 "/export may not need to flatten thin wrappers anymore" — addressed by
  this redesign (pending implementation)

## Feedback Log Entries Processed

- 2026-03-03 "Export hybrid approach: script for mechanical work, AI for judgment"
  (Issue #9) — addressed jointly with the view-source redesign (pending
  implementation)

## What Didn't Work

- (Nothing — the /think session proceeded cleanly from empirical question through
  reframing to convergence.)

## Debrief

*(Pending — to be completed at session close.)*

## State at Close

*(Pending — session in progress.)*
