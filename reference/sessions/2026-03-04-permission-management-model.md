# Maintenance Session: Permission Management Model

**Date:** 2026-03-04
**Status:** Complete

## Intent
Eliminate the friction of Claude Code's per-directory permission prompts for NLAs
that routinely read from sibling directories (framework, packages, domain data).
Introduce a permission management model where packages declare their needs in
intent files and skills generate/maintain `settings.local.json`.

## Changes Made

### Framework (10 files)
- **install/install.md** — Added Permissions section declaring framework's own needs
  (Read, git, ls, test) and note linking to it from the directory table
- **install/structure-intent.md** — Added `.claude/settings.local.json` to directory
  tree and description of the settings file's purpose
- **install/package-intent.md** — Added Permissions Section convention for packages
  with format, examples, and guidance
- **reference/design-rationale.md** — New "Permission Management Model" section
  covering problem, tiered model, rationale, declaration format, migration path
- **.claude/skills/create-app/SKILL.md** — Settings file generation: added to
  Category 2 table, generation guidance, generation order (early), narration,
  post-creation user-wide tip, and consistency check
- **core/skills/install.md** — New step 3b: Process Permission Declarations (read
  manifest, check settings, propose missing entries, create file if needed)
- **core/skills/update.md** — Permission delta detection in change categorization,
  permission application section in step 4, permissions row in install log format
- **core/skills/validate-structural.md** — New check #8: Permission consistency
  (compare declared required permissions against settings entries)
- **core/skills/startup.md** — Lightweight first-run awareness (one-line note if
  no settings.local.json exists)
- **install/update-notes.md** — Migration guidance entry for existing projects

### Packages
No direct changes. Package maintainers will add Permissions sections to their own
manifests when they pull the framework update and run `/update` — the update notes
explain what to do. This follows the migration design: each layer learns through
`/update` from the layer above.

## Blast Radius
- `install/` changes affect project generation and package installation
- `core/skills/` changes affect all domain projects (via thin wrappers)
- `.claude/skills/create-app/` affects the framework only (new projects)
- `reference/design-rationale.md` affects maintainers only
- Package changes affect their respective consuming projects
- All changes are additive — no existing behavior modified

## Decisions Made
- **Tiered placement** — Framework reads with absolute path (resolved at setup),
  package/domain reads with relative paths, writes manual. Rationale: absolute path
  for framework because it's the one entry that might go user-wide; relative paths
  for everything else because they move with the project.
- **No new skill** — Permission management flows through existing lifecycle:
  /create-app, /install, /update, /validate. A /permissions skill would be invoked
  rarely and only when one of these is already active.
- **settings.local.json by default** — Gitignored automatically, machine-specific
  paths. Checked-in settings.json documented as team option.
- **Intent files declare needs** — Same format (Permissions table with Pattern,
  Purpose, Required) for framework, packages, and standalone NLAs. The installing
  skill reads declarations and proposes entries.
- **Migration through /update** — Framework update teaches packages to declare
  permissions, packages teach domain projects. Each layer learns from the layer
  above via /update.
- **Broad bash patterns** — Pre-approve git:*, ls:*, test:* to eliminate the most
  common prompt noise. Remaining one-off approvals are Claude Code's UX to solve.

## What Didn't Work
- **Plan agent proposed cross-project edits** — Phase 4 directly edited penny-post
  and process-helpers manifests, contradicting the /think design that each layer
  learns through `/update`. Caught by the human, reverted, logged to friction log,
  and pre-flight check updated to catch this pattern going forward.

## Friction Log Entries Processed
- N/A (this addresses a feedback log entry, not friction log)

## Feedback Log Entries Processed
- "Permission model: NLAs need a way to whitelist external directory access" (Issue #7)
  — resolved

## Debrief
Explicit /debrief conversation surfaced five observations:

1. **/think + /unpack was the design MVP.** The permission model had 6+ interdependent
   threads. /unpack structured them sequentially so each decision informed the next.
   This combination is a strong pattern for design work with many moving parts.

2. **Plan agent context gap caused the only error.** The Plan agent received decision
   summaries but not the *why* behind the migration flow. It optimized for
   completeness over design integrity. The fix (pre-flight check for cross-project
   edits) addresses the symptom; the deeper question is how to pass /think reasoning
   to Plan agents more explicitly.

3. **"Seventh thread" emergence.** The migration story for existing projects wasn't in
   the original thread set. The human caught it through "are we done?" probing, then
   refined it through two reframings (packages-learn-through-update, then
   NLAs-declare-their-own-needs-too). The session would have shipped a less complete
   model without those probes.

4. **Human caught the cross-project edit at a values level** — not "wrong files" but
   "the design said changes flow through /update." Confirms the /think conversation
   built genuine shared understanding of the design principles.

5. **Post-implementation validation caught real issues.** Architecture review found 2
   fixes and 3 improvements — all proportional, all things that would have confused
   future maintainers. Continues to earn its keep as a standard post-implementation step.

## State at Close
**What's working:** Permission management model is fully implemented across the
framework. Declarations in install.md, generation in /create-app, proposals in
/install and /update, checking in /validate, awareness in /startup. Design rationale
documented, update notes written, friction log entry for the process issue captured.

**What's pending (friction log — 5 items):**
- Context-aware help/guide skill (needs /think)
- /create-app bare project path (minor, project generation)
- Should friction logs be gitignored? (needs /think)
- Framework maintain thin wrapper pattern (deferred)
- Context window awareness for session log nudges (deferred)

**What's pending (feedback log — 1 item):**
- Export hybrid approach: script for mechanical work, AI for judgment (needs /think)

**What's pending (this session):**
- Resolved feedback log entry (Issue #7) should be archived to feedback-log-archive.md
- Close loop on GitHub Issue #7 with a follow-up comment

**Where to pick up:** The export hybrid approach is the meatiest remaining feedback
item. The help/guide skill and friction-log-gitignore questions are smaller design
explorations. All need /think sessions.
