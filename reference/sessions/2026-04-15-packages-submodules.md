# Maintenance Session: Packages Directory with Git Submodules

**Date:** 2026-04-15
**Status:** In Progress

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

## State at Close
(Session in progress — moving from /think to planning)
