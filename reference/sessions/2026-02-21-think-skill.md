# Maintenance Session: /think Skill — Collaborative Design Exploration

**Date:** 2026-02-21
**Status:** Complete

## Intent

Create a skill that fills the gap between "exploring what and why" and "planning how
to implement." The framework supports doing work (/maintain) and planning work (plan
mode), but not the preceding phase where the most important decisions happen. In NLAs,
deep thinking often produces less code but better results — a single sentence can make
a huge difference. The what/why phase must be complete before the how.

## The Self-Referential Design Process

This session used the thinking-it-through process to design the thinking-it-through
skill. The conversation that preceded planning was itself a model for what the skill
should enable. Key observations from the process:

1. **The AI is already good at this when it knows the task.** The thinking conversation
   flowed naturally once the framing was clear. This led to the decision to make the
   skill lightweight — it sets conditions rather than prescribing procedure.

2. **Posture matters more than process.** The initial posture proposal was too
   deferential ("say I don't know and sit with that"). The user corrected: bring
   expertise, own what you know, propose ideas — but be transparent and respect the
   Cardinal Rule. The AI enhances the human; neither is just executing for the other.

3. **The four questions.** The user's practice of ending responses with "Thoughts?
   Concerns? Ideas? Questions?" keeps conversations genuinely collaborative. Named
   explicitly in the skill as a practice worth adopting.

4. **The couching insight.** The user deliberately softens their certainty so the AI
   doesn't treat tentative thoughts as decisions. Good thinking-mode posture reduces
   the need for this workaround — if the AI already treats ideas as exploratory, the
   human doesn't have to artificially soften them.

5. **Thinking is work.** A session where the output is "we decided not to build X
   and here's why" is just as valuable as one that produces files. Session logs
   accommodate this — their Intent and Decisions sections capture conceptual work.

## Decisions Made

- **Skill, not guidance** — A non-invokable skill rather than general context in
  CLAUDE.md or foundations. The skill creates a discrete moment and loads focused
  posture guidance. Evidence from penny post: the AI suggests write-letter at the
  right moment, but quality comes from loading the skill file.

- **Lightweight** — ~90 lines focused on posture, not procedure. The AI doesn't need
  to be taught how to think collaboratively; it needs to know when to do it and a few
  nudges to do it better.

- **No separate thinking log** — Session logs are sufficient. Guidance about
  checkpointing insights to the session log when significant reframings happen,
  rather than creating a parallel artifact.

- **Prior art as capability, not requirement** — The skill mentions checking design
  rationale and session archives when relevant, but doesn't mandate it. Exercise
  judgment about when it's useful.

- **Four-phase flow** — think → plan → implement → debrief. Each phase has its own
  skill/mode. Not every task needs all four. The AI knows when to suggest each one.

- **Debrief is a separate concern** — The friction log has a related entry about a
  post-session reflection skill. Thinking mode looks forward (what/why); debrief
  looks back (how did the process go). Different inputs, different outputs.

## Changes Made

- Created `core/skills/think.md` — the core skill file (~90 lines)
- Created `.claude/skills/think/SKILL.md` — framework wrapper with prior art note
- Added `/think` to `install/skills-intent.md` — reference wrapper for domain projects
- Updated `core/skills/maintain.md` Principle 2 — brief reference to thinking phase
- Added `/think` to `core/skills/README.md`, `CLAUDE.md`, `README.md`
- Added design rationale entry covering the decision, alternatives, self-referential
  process, and relationship to removed `/plan` skill
- Resolved friction log entry "Need a 'thinking it through' mode"

## Blast Radius

- **All domain projects:** New `/think` skill available via thin wrapper (additive).
  Maintain.md Principle 2 updated with thinking phase reference (behavioral — suggests
  thinking before planning for design-judgment work).
- **Project generation:** `install/skills-intent.md` updated (new projects get /think).
- **Framework documentation:** Design rationale, README, CLAUDE.md updated.

## State at Close

The `/think` skill is implemented, documented, and validated. All cross-references
are consistent. The friction log entry is resolved and archived.

**Validated.** Structural check found 2 issues (missing from /create-app Category 1
table, no update note). Both fixed.

**Pending from this session:**
- Three feedback log items for `/update` skill improvements remain (reference-search
  step, README downstream check, strengthen validate-after-update). These are the
  natural next session's work.
- Debrief/retrospective skill friction log entry remains pending — the other bookend
  of the thinking/reflecting pair.
- Voice and values splitting friction log entry remains pending — needs its own
  thinking session.
