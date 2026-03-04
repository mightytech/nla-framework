# Maintenance Session: /close Skill and Next-Step Suggestions

**Date:** 2026-03-04
**Status:** Complete

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
- Debrief-driven improvements to /maintain workflow (both core and framework wrapper):
  - "Discuss your approach" as explicit workflow step after user picks work, with /think escalation
  - Dependency/connection analysis added to session start summary
  - Plan mode expectations: conversational-first, AskUserQuestion for discrete selections only, preserve context

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
Full `/debrief` with `/unpack` to work through 4 threads:

1. **The /think skip.** The AI jumped to plan mode without the conversational exploration
   that produced the session's best design insight (/close as guarantor, not just finalizer).
   The guidance existed in Principle 2 but didn't override execution momentum. Fix: added
   "discuss your approach" as an explicit workflow step, not a buried principle.

2. **AskUserQuestion as anti-pattern for design decisions.** The structured question UI
   converts rich design spaces into multiple-choice tests. The user's reframing of /close
   couldn't have emerged from a menu. Agreed it has a place for genuinely discrete selections,
   but design decisions belong in conversation. Fix: plan mode expectations added to
   Principle 2.

3. **Dependency analysis primes better recommendations.** The user's "are these connected?"
   question shaped the entire session — what to combine, what to defer, where to start.
   Without that mapping, recommendations would have been less coherent. Fix: light addition
   to session start summary.

4. **Validation two-mode pattern.** Structural + architecture together caught different
   things. Resolved without changes — already covered by judgment and existing next-step
   language.

Also noted: metaphors are genuinely helpful for communicating calibration to the AI.
"Glancing at the side mirror before switching lanes" encoded the right weight for the
conversational beat more precisely than specification would have.

## State at Close
**Working:** /close skill fully registered and operational. Next-step suggestions in
debrief, validate, export, maintain. Conversational-first workflow practices in /maintain.
Validation confirmed structural and architectural coherence.

**Pending friction log (5 items):**
- Context-aware help/guide skill (needs /think)
- /create-app bare project path (pre-existing)
- Should friction logs be gitignored? (needs /think)
- Framework maintain thin wrapper pattern (deferred)
- Context window awareness for session log nudges (deferred)

**Pending feedback log (3 items):**
- Export hybrid approach (needs /think)
- Permission model (needs /think)
- Export runtime validation step (implementable, most self-contained)

**Recommended next session:** Export runtime validation is the most self-contained
implementable item. The /think-dependent items (permission model, export hybrid,
help/guide skill, friction log gitignore) are the bigger design work waiting.
