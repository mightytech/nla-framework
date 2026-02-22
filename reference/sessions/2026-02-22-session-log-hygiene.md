# Maintenance Session: Session Log Hygiene

**Date:** 2026-02-22
**Status:** In Progress

## Intent
Clean up stale architecture review findings and improve session log practices so logs stay accurate at every commit point.

## Changes Made
- Updated architecture review session log (`2026-02-21-architecture-review.md`) to reflect that findings #11 and #14 were already fixed — adjusted resolved counts (6→8 resolved, 6→4 noted)
- Added commit-point log sync guidance to framework maintain wrapper (`.claude/skills/maintain/SKILL.md`) — "Keeping the Log Current" subsection
- Tightened step 2 of session lifecycle in core maintain skill (`core/skills/maintain.md`) — anchored updates to commit points instead of "when natural"
- Logged and resolved friction entry: "Session logs fall behind commits"
- Logged deferred friction entry: "Context window awareness for session log nudges"

## Blast Radius
- `core/skills/maintain.md`: all domain projects (session lifecycle step 2 reworded)
- `.claude/skills/maintain/SKILL.md`: framework maintainers only
- `reference/`: framework maintainers only

## State at Close
[pending — session still in progress]
