# Maintenance Session: Process Helpers Package and /unpack Move

**Date:** 2026-02-22
**Status:** Complete

## Intent
Explore whether process helper skills (facilitation techniques like /unpack) belong in
core or in an optional package, then create the package and move /unpack there.

## Thinking Phase (/think)

Started with /think to explore the core vs. package question. Key insights:

1. **Phase vs. process distinction.** Phase skills (/think, /debrief) define *when* in
   the work lifecycle — universal. Process helpers define *how* within conversations —
   preference. The penny post analogy was misleading: penny post adds capabilities some
   NLAs need. Process helpers shape conversations every NLA has, but differently.

2. **The reframing.** The human noted: "unpack is useful across sessions — but it's also
   the way *I* like to work. I can imagine other people preferring different ways." This
   shifted /unpack from "universally useful tool" to "one preferred working style."

3. **Different developers, different sets.** A music NLA might want listening session
   facilitation. A writing workshop NLA might want critique circles. These are domain
   facilitation techniques that share the same shape as /unpack — the package model
   enables curated sets rather than one-size-fits-all.

4. **Selective installation (future direction).** When the package has multiple techniques,
   users should choose which to install. Trivial to implement but not needed with one skill.
   Noted in README and design rationale, not implemented.

## Changes Made

### Part 1: Created `nla-process-helpers/` package
- Full NLA structure: CLAUDE.md, README.md, app/ (overview, unpack, config-spec,
  shared/values), install/ manifest (install.md, CLAUDE-intent.md, skills-intent.md),
  reference/ (design-rationale, friction-log, feedback-log, installed-packages,
  system-status), .claude/skills/ (10 framework wrappers + 1 domain skill)
- app/unpack.md is the full skill logic (moved from core/skills/unpack.md)
- Design rationale captures the phase/process distinction and selective installation
  as future direction
- README includes future directions section noting selective installation

### Part 2: Removed /unpack from framework core
- Deleted `core/skills/unpack.md` and `.claude/skills/unpack/`
- Removed /unpack from `install/skills-intent.md`
- Removed /unpack from `CLAUDE.md` skills table
- Added `../nla-process-helpers/` to `CLAUDE.md` Key Files table
- Removed unpack from `README.md` directory tree
- Removed unpack from `core/skills/README.md` table
- Removed unpack from `.claude/skills/create-app/SKILL.md` Category 1 table
- Added design rationale entry: "Moving Process Helpers to a Package"
- Added update note explaining the move and migration options
- Added process helpers to `install/example-catalog.md`

## Blast Radius

- **Framework core** (all domain projects): `core/skills/unpack.md` deleted. Existing
  wrappers pointing to it will break — update notes guide migration.
- **Install/intent** (project generation): /unpack no longer generated for new projects.
  Available via `/install` from the process helpers package.
- **Example catalog** (project discovery): Process helpers listed alongside other examples.

## State at Close

Process helpers package is created, committed, and functional as a standalone NLA.
Framework is cleaned up — no stale references to unpack in operative files. Historical
references in session logs and friction log archive are preserved as-is (they're records,
not operative).

Three domain projects (copydesk, duet, penny post) may have /unpack wrappers that now
point to a deleted file. The update note in `install/update-notes.md` explains the
migration options. They'll encounter this on their next `/update` run.
