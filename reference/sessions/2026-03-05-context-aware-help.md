# Maintenance Session: Context-Aware Help/Guide Skill

**Date:** 2026-03-05
**Status:** In Progress

## Intent
Design and implement context-aware help for NLA projects. New users finish `/create-app`
and have no guidance on what to do next. The framework workflow is implicit — individual
skills don't know where they sit in the larger flow. Make NLAs self-explanatory.

## Changes Made

### Working Rhythms in foundations (blast radius: all projects)
- Added `## Working Rhythms` section to `core/nla-foundations.md` documenting four
  universal workflow patterns with intent: the improvement loop, the design flow, the
  update cycle, and session structure. Each explains why the rhythm exists, not just
  what it is. This is the content foundation that makes both on-demand help and
  `/guide` mode actually good.

### `/guide` skill — mode-as-skill (blast radius: all projects via thin wrappers)
- Created `core/skills/guide.md` — core skill logic following the `/think` pattern.
  Defines posture (meet users where they are, adapt verbosity, include the why),
  what to cover, scope, and transition behavior.
- Created `.claude/skills/guide/SKILL.md` — framework wrapper with adjusted context
  (framework has no `app/overview.md`).
- Registered in: `install/skills-intent.md`, `core/skills/README.md`, `CLAUDE.md`,
  `README.md`, `.claude/skills/create-app/SKILL.md` Category 1 table.

### Broadened overview.md pattern (blast radius: project generation)
- Updated `install/structure-intent.md` — overview.md comment now includes "how users
  work with the system."
- Updated `.claude/skills/create-app/SKILL.md` — overview.md domain structure now
  includes "How users work with this" section with guidance on typical sessions,
  workflow expectations, and domain-specific workflows. Added narration row.
  Added post-creation tip about `/guide`.

### Nudges (blast radius: all projects via thin wrappers)
- `core/skills/startup.md` — added `/guide` as a recognized user action alongside
  existing options.
- `core/skills/maintain.md` — added mention of `/guide` for unfamiliar users.

### Housekeeping
- `install/update-notes.md` — changelog entry for domain projects.

## Blast Radius
- `core/nla-foundations.md` — all projects (loaded at startup)
- `core/skills/guide.md`, `startup.md`, `maintain.md` — all projects (via thin wrappers)
- `install/` changes — project generation and `/install`/`/update`
- Framework `.claude/skills/`, `CLAUDE.md`, `README.md` — framework only

## Decisions Made
- **Content over mechanism** — The Working Rhythms section is the load-bearing piece.
  Without it, the AI improvises from skill descriptions. With it, the AI has real
  understanding of how the pieces connect. The `/guide` skill activates a mode; the
  content makes that mode useful.
- **Mode-as-skill pattern** — `/guide` follows the `/think` precedent: a mode surfaced
  as a skill for discoverability, with `disable-model-invocation: true` to avoid
  context cost when unused.
- **Broaden overview, not new file** — User workflow guidance goes in `app/overview.md`
  rather than a separate `app/guide.md`. Keeps one source of truth and may improve
  AI behavior generally (not just during `/guide`).
- **Include intent with mechanics** — Both the Working Rhythms section and the guide
  skill explain *why* each workflow exists. Consistent with "Judgment over rules"
  principle. Purpose enables edge-case handling.
- **Nudges as the "you can ask" bridge** — New users may not know asking the AI is a
  valid move. One-sentence nudges in startup, maintain, and create-app bridge this
  mental model gap without being heavy-handed.

## What Didn't Work
- (nothing notable — design was well-explored in /think before implementation)

## Friction Log Entries Processed
- "Context-aware help/guide skill" (2026-03-03) — resolved

## Debrief
1. **/think was the most valuable phase.** The user's reframe — "context-aware help is
   free, but we can structure it" — prevented over-engineering. We wrote better content
   and gave the AI a mode to deliver it, rather than building a complex help system.
   Implementation was nearly mechanical after the design conversation.

2. **"Broadening overview makes the AI run better" has legs.** The hypothesis that
   user-workflow content in overview.md improves general AI behavior (not just /guide)
   is now testable across domain projects. If confirmed, it's a broader principle:
   the AI performs better when it understands the expected user journey, not just
   system architecture.

3. **"Include the why" threaded through every piece.** One design decision shaped
   Working Rhythms (intent per rhythm), guide.md (posture: explain why), and
   overview.md broadening (domain-specific why). The framework practicing its own
   "Judgment over rules" principle at the meta level.

4. **Architecture review: valuable but needs judgment filter.** Caught a real
   description inconsistency. Also flagged arguable concerns (skill names in
   foundations, existing projects lacking new sections). The review agent is thorough
   but the human's judgment about which findings matter is the real filter.

5. **Thorough /think → clean implementation.** Previous session noted plan agents
   lack design context. This time, thorough /think produced clear shared understanding
   so the plan was mostly sequencing. Supports the pattern.

## State at Close
(pending)
