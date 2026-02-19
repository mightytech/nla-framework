# Maintenance Session: Validate Split + Architecture Review Mode

**Date:** 2026-02-18
**Status:** Complete

## Intent

Add architecture review capability to `/validate` and split the monolithic skill into a dispatcher + mode files. Originated from Copydesk's Issue #4 proposing a `/code-review` skill for checking document chain coherence after restructuring.

The core behavioral change: domain projects can now run `/validate` and choose "Do my docs tell a consistent story?" to get a thorough architecture review that walks their full document chain checking for coherence issues. Previously, `/validate` could only check mechanical consistency (file references, skill tables) or trace individual scenarios.

## Changes Made

- **Split `/validate` into dispatcher + mode files** — the monolithic `core/skills/validate.md` (124 lines) became a dispatcher (~55 lines) routing to four mode files. Each mode is self-contained and focused.

- **Added architecture review mode** — new Mode 4 with nine analytical categories (path resolution, cross-reference integrity, layer boundaries, consistency, conditional completeness, generic/specific alignment, prerequisite sufficiency, contradiction, orphaned content). Writes findings incrementally to `reference/sessions/`.

- **Refactored framework validate** — `.claude/skills/validate/SKILL.md` (140 lines of duplicated content) refactored to delegate to core mode files with framework-specific addenda. Eliminates dual maintenance.

- **Added session-close reminder** — `/maintain` now suggests running `/validate` architecture review after sessions involving structural changes.

- **Updated supporting files** — README table for core/skills/, skills-intent.md description, CLAUDE.md skills table, design rationale entry.

## Blast Radius

- **All domain projects:** core dispatcher rewrite, new mode files (domain wrappers point to `core/skills/validate.md` which now routes to mode files)
- **All domain projects:** maintain session-close reminder (additive)
- **Project generation:** skills-intent.md description update
- **Framework only:** framework validate refactoring
- **Maintainers only:** design rationale, README, session log

## Decisions Made

- **Mode 4 of /validate, not standalone /code-review** — conceptual unity (all modes answer "is my NLA correct?"), shared setup, wrapper simplicity
- **Dispatcher + mode files, not four separate skills** — one wrapper per project, shared required reading and scope
- **Hybrid menu** — maps user concerns ("are my files wired up correctly?") to system approaches (structural check), skipped when intent is clear
- **Nine categories, not six** — added prerequisite sufficiency, contradiction, and orphaned content beyond Copydesk's original six
- **Framework validate delegates to core** — eliminates dual maintenance of mode logic

## Feedback Log Entries Processed

- [Issue #4](https://github.com/mightytech/nla-framework/issues/4) — resolved (adapted: Mode 4 of /validate, not standalone /code-review). Issue closed with triage comment.

## State at Close

All changes implemented and verified. The validate skill is now a dispatcher routing to four mode files. The framework's own validate delegates to core with addenda. No pending work from this session.

Next steps (not blocking):
- Domain projects will pick up the new dispatcher and mode files on next `git pull`
- Architecture review mode should be exercised on a real project to validate the analytical categories
- Consider writing a penny post letter to Copydesk notifying them of the implementation
