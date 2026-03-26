# Maintenance Session: Permission Symlink Investigation

**Date:** 2026-03-25
**Status:** In Progress (awaiting domain project test results)

## Intent
Investigate why the permission management model (designed 2026-03-04) isn't eliminating
cross-directory permission friction in practice. Explore whether symlinks within the
project directory could be an alternative or complementary approach.

## Changes Made
- **Friction log entry added** — documents the settings.local.json junk drawer problem
  and the symlink discovery
- **Test letters sent** to 5 domain projects (office-hours, penny-post, process-helpers,
  claude-code, duet) requesting permission behavior data for both direct and symlink reads

## Blast Radius
- Friction log entry: maintainers only (for now)
- If symlink architecture is adopted: all projects (structural change to how dependencies
  are referenced)

## Decisions Made
- **Test before designing** — rather than choosing between fixing settings.local.json
  generation and adopting symlinks, gather data from domain projects first. The framework
  project's own test was inconclusive because direct reads also worked without prompts.
- **Penny post as coordination mechanism** — used /write-letter to send identical test
  protocols to all domain projects. Each project will test and report back via penny post
  letter to the framework.

## What We Learned So Far

### Symlinks bypass permission checks
Created `dependencies/nla-penny-post` → `../nla-penny-post/`. Reads through the symlink
path (`dependencies/nla-penny-post/app/overview.md`) triggered zero permission prompts.
Confirmed on both shallow and deep paths.

### Direct reads also worked (unexpectedly)
From the framework project, direct reads to `../nla-penny-post/app/overview.md` and
`../nla-process-helpers/app/overview.md` also triggered no permission prompts — despite
no `Read` entries for those paths in settings.local.json. This may be permission-mode
specific or due to accumulated one-off approvals. Inconclusive.

### settings.local.json is a junk drawer
The framework's settings file contains individually approved commands accumulated over
time — including literal commit messages, shell loop fragments, and broken entries.
The systematic entries the permission model was designed to generate (`Read(../nla-framework/**)`)
are absent.

### The /think session surfaced key design questions
If symlinks work reliably across projects:
- **Dependency visibility** — `dependencies/` makes what a project uses structurally
  visible, not just declared in config
- **Path migration** — thin wrappers would change from `../nla-framework/` to
  `dependencies/nla-framework/` (big migration, but both paths would work during transition)
- **Git handling** — symlinks could be committed (relative targets) or gitignored (setup step)
- **CLAUDE.md isolation preserved** — Claude Code doesn't load CLAUDE.md from subdirectories,
  so dependency CLAUDE.md files wouldn't activate
- **Maintenance mode unaffected** — maintaining the framework or packages still happens in
  their actual directories

## What Didn't Work
- **Couldn't reproduce the permission friction from the framework project.** Both direct
  and symlink reads worked. The friction likely manifests differently in domain projects,
  which is why we sent the test letters.

## Friction Log Entries Processed
- New entry added: "settings.local.json accumulates junk instead of systematic permission
  entries" (pending — awaiting test data)

## State at Close
**What's working:** Test protocol distributed to 5 projects. Friction log updated.

**What's pending:**
- Test results from domain projects (Issues: nla-office-hours#1, nla-penny-post#11,
  nla-process-helpers#1, nla-claude-code#1, duet#2)
- Design decision: fix settings pipeline vs. adopt symlinks vs. both
- If symlinks: full /think session on the architecture (path conventions, git handling,
  migration strategy, intent file changes)

**Where to pick up:** Check for responses to the test issues. Once data is in from at
least 2-3 projects, reconvene the /think session to make the design decision.
