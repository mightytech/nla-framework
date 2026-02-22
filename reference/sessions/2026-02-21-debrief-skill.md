# Maintenance Session: /debrief Skill

**Date:** 2026-02-21
**Status:** Complete

## Intent

Formalize the reflection step in the learning loop. Evidence from penny post's
post-update session showed that open-ended reflection produces high-quality,
actionable feedback — but the process was informal. The `/debrief` skill gives
the AI permission and posture to reflect after substantive work, completing the
four-phase flow: think → plan → implement → debrief.

## Design Thinking

Went through four design questions in a /think-style collaborative exploration:

1. **Weight:** Lightweight like /think (~100 lines). The AI already knows how to
   reflect — it needs permission and posture, not instructions. But differently shaped
   than /think: debrief has direction (look back, surface, refine, suggest destinations)
   while think is open-ended exploration.

2. **Capture handoff:** Judgment, not routing logic. The skill focuses on reflection
   and refinement. The AI suggests natural destinations (/friction-log, /write-letter)
   based on what emerged, rather than following a classification mechanism.

3. **When to suggest:** Transition-sensitive. The AI notices context shifts between
   tasks/projects and offers a low-cost prompt. Not wired into other skills' closing
   steps. A batch of related tasks gets one suggestion; separate tasks get separate
   suggestions. The prompt is dismissable — "want to debrief?" is easy to wave away.

4. **Naming:** `/debrief` — collaborative (we did this together), not solitary
   (/reflect) or failure-focused (/post-mortem).

## Incidental Discovery

"Thoughts? Concerns? Ideas? Questions?" (the named practice from /think) was being
misused as a conversation closer directed at the human. The intended pattern is the
opposite: it's an invitation for the AI to share ITS perspective in response to what
the human said. Logged as a separate friction log entry for resolution in /think's
skill text.

## Changes Made

- Created `core/skills/debrief.md` — lightweight reflection skill (~100 lines)
- Created `.claude/skills/debrief/SKILL.md` — framework wrapper with maintenance context
- Added /debrief to `install/skills-intent.md` (after /think, as conceptual bookends)
- Added /debrief to `CLAUDE.md` skills table
- Added debrief/ to `README.md` directory tree
- Added update note to `install/update-notes.md`
- Added design rationale entry (includes TCIQ correction documentation)
- Resolved and archived friction log entry "Post-session reflection as a skill"
- Logged "TCIQ is an AI invitation" as new friction log entry

## Blast Radius

- `core/skills/debrief.md`: all domain projects (new skill available via thin wrapper)
- `install/skills-intent.md`: project generation, /install, /update
- `CLAUDE.md`, `README.md`: framework documentation only

## State at Close

/debrief skill is complete and integrated. Four-phase flow is now fully represented
in the framework.

**Also resolved this session:**
- TCIQ friction log entry — rewrote /think's "Keep the conversation open" bullet
- Logged new friction log entry: conversation structure skill ("slow your roll")

**Remaining pending items:**
- Friction log: Conversation structure skill (new — needs /think session)
- Friction log: Voice and values splitting (major, deferred to own session)
