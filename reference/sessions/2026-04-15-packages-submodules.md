# Maintenance Session: Packages Directory with Git Submodules

**Date:** 2026-04-15
**Status:** Complete (framework migrated; domain project propagation pending)

## Intent
Replace the sibling directory convention (`../nla-framework/`, `../nla-package/`) with a
`packages/` directory using git submodules within each NLA project. This solves the
cross-directory permission friction, adds version pinning, makes projects self-contained,
and simplifies the new user experience.

## /think Session Summary

### Origin
During /check-feedback triage of permission test results (#15, #16), a lateral idea
emerged: rather than fixing the permission pattern matching (relative vs. absolute paths),
eliminate cross-directory reads entirely by putting dependencies inside the project.

### Threads Explored (via /unpack)

1. **Permission resolution** — Solved. All reads within-project, no prompts.
2. **CLAUDE.md isolation** — Safe. Subdirectory CLAUDE.md files don't auto-load.
3. **Development workflow** — Non-issue. Develop in source repos, consume via submodules.
   Enforces Context Determines Competence.
4. **Framework's own packages** — Self-consistent. Framework eats its own dog food.
   Circular dependencies work (no build step, no resolution needed).
5. **Update model** — Strictly better. Ambient → explicit. Version pinning, atomic
   commits, trivial rollback. `/update` owns all submodule commands.
6. **New user experience** — Improved. Self-contained projects.
   `git submodule update --init` gives a complete working copy.
7. **Path migration** — Mechanical. `../nla-framework/` → `packages/nla-framework/`
   everywhere. Framework migrates first. Required (no transition period — single user).
8. **Permission model obsolescence** — Retire cross-directory permission machinery.
   Keep design rationale with supersession note.

### Key Insights

**Circular dependencies work in NLAs.** The framework depends on penny post; penny post
depends on the framework. In traditional software, this is a build-order problem. In NLAs,
there's no build step — the LLM reads files from paths. Each project pins its own version
of the other. No resolver needed. (Fits the "absurd things that work" pattern.)

**Flat, not nested dependencies.** `git submodule update --init` (without `--recursive`)
clones only direct dependencies. No transitive dependency resolution. If package A needs
package B, the consuming NLA lists both as direct dependencies — they're siblings in
`packages/`.

**The ambient update model was a hidden danger.** `git pull` on a shared sibling changed
behavior in every project simultaneously. Version pinning means each project runs exactly
what it was tested with. The apparent convenience was actually a liability.

## Decisions Made

- **Directory name:** `packages/`
- **Mechanism:** git submodules
- **Clone depth:** shallow (dependencies don't need full history)
- **URL format:** HTTPS in `.gitmodules` (portable)
- **Init convention:** `git submodule update --init` (not `--recursive`)
- **Migration:** required, no transition period
- **Framework migrates first** as test case
- **Permission management model** for cross-directory reads: retired
- **External data directories** (e.g., Duet's `../duet-music/`): project-specific, not a framework decision
- **Tag-aware updates:** `/check-updates` reports available tagged releases; `/update` offers advancing to a tag vs. HEAD
- **Tagged as v0.0.1** — first packages/submodules release

## Changes Made
- **Git submodules added** — `packages/nla-penny-post/` and `packages/nla-process-helpers/` as shallow submodules
- **Framework skill wrappers** — all 6 package-delegating wrappers updated to `packages/` paths
- **CLAUDE.md** — Key Files table updated
- **Core skills** — all `../nla-framework/` paths updated to `packages/nla-framework/`; permission machinery retired from startup, validate-structural, install, update, check-updates
- **Intent files** — all 5 intent files updated (skills-intent, CLAUDE-intent, structure-intent, install.md, package-intent); permission declarations simplified to Bash patterns only
- **Create-app skill** — generation flow now includes git init + submodule add; settings simplified; narration updated
- **Install-app skill** — added submodule init step
- **Design rationale** — supersession notes on 3 existing entries; new "Packages Directory with Git Submodules" entry
- **README.md** — getting started, thin wrappers, directory trees, upgrading all updated
- **Update notes** — new entry with migration steps for domain projects
- **Friction log** — "settings.local.json accumulates junk" resolved
- **Installed-packages.md** — all package paths updated
- **Tag-aware updates** — check-updates reports tagged releases; update offers tag vs. HEAD choice
- **Tagged v0.0.1** and pushed to remote

## Blast Radius
- `install/` intent files: project generation convention changes
- `core/skills/`: path references in update, check-updates, install, startup
- `.claude/skills/`: framework wrapper paths, create-app generation logic
- `CLAUDE.md`: Key Files table
- `reference/design-rationale.md`: new entry, supersession of sibling convention and permission model
- All domain projects: migration via `/update`

## What Didn't Work
- (Nothing — the /think session proceeded cleanly from premise checks through implications)

## Friction Log Entries Processed
- "settings.local.json accumulates junk" — resolved by architectural change (no more
  cross-directory reads), not by fixing the generation pipeline

## Debrief
- The /think → /unpack combination worked well for this — 8 threads, resolved sequentially, clear go/no-go gating on premise checks before investing in downstream threads.
- The "lateral idea during triage" pattern: checking feedback surfaced data (permission test results) that prompted a design question bigger than the feedback itself. The framework correctly paused triage to explore the design question.
- The circular dependency insight is worth capturing beyond the design rationale — it's an "absurd thing that works" that demonstrates the NLA paradigm.
- Plan agent was effective for this scope — the implementation was largely mechanical once the design was settled. No cross-project edit issues this time (lesson learned from 2026-03-04).

## State at Close
**What's done:** Framework fully migrated. Committed, tagged v0.0.1, pushed.

**What's pending:**
- Migrate penny-post and process-helpers (in their own sessions, then push)
- Migrate domain projects (office-hours, claude-code, duet, facebook-moderation, nla-writer) after packages are pushed
- Finish /check-feedback triage — 10 open issues, only permission test results (#15, #16) were triaged before the /think session. Mechanical fixes (#12, #13) and facebook-moderation batch (#14, #17-21) still pending.
- Close permission test issues (#15, #16, plus 3 unanswered: process-helpers#1, claude-code#1, duet#2) with note about architectural resolution

**Where to pick up:** Finishing /check-feedback triage (mid-stream, unpacking item by item). Then propagate migrations to packages and domain projects in separate sessions.

## Checkpoint: Mid-Triage (feedback queue)

**Completed triage:**
- #12 (git -C) — Accept, already implemented. Closed.
- #13 (validate wrapper) — Accept, fixed. Closed.
- #14 (Describe the Space) — Accept, extend principle #4
- #15, #16 (permission tests) — Accept as data, resolved by architecture. Closed.
- #17.1 (intent > rules) — Adapt, fold into #14 as stronger rewrite of principle #4
- #17.2 (session splitting) — Accept, replaced with session-checkpoint promotion from facebook-moderation
- skills-intent.md also has a pending fix (coherence review in validate wrapper description)

**Currently discussing:** #17.3 (AI posture beyond /think) — proposed defer

**Still to triage:** #17.3, #17.4, #18 (6 items), #19, #20, #21

**Key decisions so far:**
- Principle #4 gets a significant rewrite: lead with intent over rules, incorporate identity-description pattern, add "rules are for consistency-only" boundary
- Session-checkpoint promoted from facebook-moderation to framework core skill
- Accepted items will be deposited in feedback log after all triage is complete
