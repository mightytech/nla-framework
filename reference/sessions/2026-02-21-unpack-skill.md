# Maintenance Session: /unpack Skill

**Date:** 2026-02-21
**Status:** Complete

## Intent

Create a conversation structure skill — a facilitation technique that helps the AI
lay out bundled threads and work through them sequentially. This is the first of a
potential category of technique-based skills, distinct from phase skills (/think,
/debrief) and action skills (/validate, /export).

## Design Thinking

Ran a /think session exploring three open questions from the friction log:

1. **Naming:** Explored /chunk, /structure, /untangle, /slow-down, /focus, /unpack.
   Chose `/unpack` — captures the action (lay out bundled pieces, work through them)
   and sounds natural ("let's unpack this").

2. **Interaction model:** The skill layers on top of active context (think, maintain,
   domain work) without resetting it. Method: recognize bundled threads → propose the
   set → work through sequentially → track state visibly. Skills are just markdown the
   AI reads — nothing prevents two from being active simultaneously.

3. **Scope:** Anything that benefits from sequential attention — questions, proposals,
   feedback items, competing options. Don't enumerate use cases; trust the AI's judgment
   and the human's agency.

Key insight from the session: this isn't an anomaly — it's potentially the first of a
category of facilitation technique skills (brainstorming, card sorting, naming). The
user has ICA facilitation training. Let the pattern emerge rather than designing the
category upfront.

Additional design decisions:
- **Tracking:** Visible but light, adapts to scale. Few items get names, many get counts.
- **Weight:** Lightweight like /think and /debrief (~100 lines). The AI knows how to
  facilitate — it needs permission and method, not heavy procedure.

## Changes Made

- Created `core/skills/unpack.md` — lightweight facilitation technique (~95 lines)
- Created `.claude/skills/unpack/SKILL.md` — framework wrapper
- Added /unpack to `install/skills-intent.md` (after /debrief)
- Added /unpack to `CLAUDE.md` skills table
- Added unpack/ to `README.md` directory tree
- Added update note to `install/update-notes.md`
- Added design rationale entry (facilitation technique category, composability, naming)
- Resolved and archived friction log entry "Conversation structure skill"

## Blast Radius

- `core/skills/unpack.md`: all domain projects (new skill available via thin wrapper)
- `install/skills-intent.md`: project generation, /install, /update
- `CLAUDE.md`, `README.md`: framework documentation only

## State at Close

/unpack skill is complete and integrated. First facilitation technique skill
established as a pattern — future technique skills (brainstorming, card sorting, etc.)
can follow the same conventions.

**Remaining pending items:**
- Friction log: Voice and values splitting (major, deferred to own session)
