# Maintenance Session: /close Skill and Next-Step Suggestions

**Date:** 2026-03-04
**Status:** In Progress

## Intent
Make the implicit session workflow partly visible through use. Two related friction log
entries traced to the same gap: no session close skill, and skills don't suggest what
comes next. Implementing both together lets skills point to `/close` as the natural
terminus, and `/close` becomes the destination that makes the other suggestions useful.

## Changes Made
- Created `/close` core skill — shape-neutral session closer that creates or finalizes
  session logs, checks loose ends (uncommitted changes, doc mirrors, validation),
  summarizes state. Works after any substantive session, not just /maintain.
- Added next-step suggestions to debrief (→ /close), validate (→ /debrief, /close),
  export (→ validation, /close), and maintain (session close steps → /close delegation)
- Registered /close across the framework: wrapper, core/skills/README, skills-intent,
  create-app Category 1, CLAUDE.md, README directory tree
- Added update note in install/update-notes.md for domain projects
- Post-validation fixes: session log title convention in close.md, /debrief suggestion
  in close.md, added missing template sections to framework maintain wrapper

## Blast Radius
- All core skill changes affect all projects (maintain.md, debrief.md, validate.md,
  export.md, close.md)
- All changes are additive — they suggest next steps without changing existing behavior
- install/update-notes.md and install/skills-intent.md affect project generation and
  /update behavior

## Decisions Made
- /close is shape-neutral (works after any session, not just /maintain) — because any
  persistent NLA with session logs benefits from clean close
- /maintain keeps responsibility for creating session logs early (essential for context
  compaction) — /close is the finalizer and backstop, not the only creator
- Combined session close + next-step suggestions in one session because they're
  interdependent: next-step suggestions need /close to exist as a destination

## Friction Log Entries Processed
- "Session close skill" (2026-03-03) — resolved
- "Skills should suggest next steps" (2026-03-03) — resolved

## Debrief

## State at Close
