# Maintenance Session: Pre-flight Review and Friction Log Cleanup

**Date:** 2026-02-19
**Status:** Complete

## Intent

Strengthen the maintain skill's pre-flight review guidance so the AI reliably
self-reviews designs before proposing them, and clean up accumulated friction log
housekeeping debt.

## Changes Made

- **Pre-flight review sub-section** added to Principle 2 in both `core/skills/maintain.md`
  and `.claude/skills/maintain/SKILL.md`. Includes a specific checklist (gaps, unconsidered
  alternatives, unintended consequences, cost/benefit, scope, maintenance burden) drawn
  from what pre-flight has actually caught across past sessions. Bridge sentence added to
  the top-level Principle 2 text to ensure the sub-section isn't skimmed past.

- **Documentation mirrors reminder** added to session close steps in both maintain files.
  Triggers on file creation, moves, or deletions — checks README tree and other
  manually-maintained listings.

- **Friction log cleanup**: archived 4 resolved entries (pre-flight pattern, Duet session,
  create-app skeleton, README drift). Active log now has one pending entry (voice/values
  splitting).

- **README directory tree** updated to include archive files and feedback directory.

## Blast Radius

- **All domain projects:** maintain skill changes (pre-flight sub-section, documentation
  mirrors step)
- **Maintainers only:** friction log archival, README tree update, session log

## State at Close

The maintain skill now has explicit pre-flight review guidance with a concrete checklist
and a documentation-mirrors check at session close. Both address recurring patterns
observed across multiple sessions.

One friction log entry remains pending: voice/values splitting (major, deferred to its
own session with fresh context).
