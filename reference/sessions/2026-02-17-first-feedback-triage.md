# Maintenance Session: First Feedback Triage and Implementation

**Date:** 2026-02-17
**Status:** In Progress

## Intent

Process the first three GitHub Issues filed against the framework (all from penny post
maintenance sessions). Establish the feedback triage workflow by simulating penny post's
`/check-feedback` conventions, then implement accepted items.

This session is also the framework's first use of its own feedback pipeline — the
feedback log was created during this session and immediately used to track the work.

## Changes Made

### Issue #1 — `install/` directory (Accept)
Created `install/` directory with four intent files formalizing what `/create-app` does
implicitly. This is the framework's counterpart to penny post's `install/` directory —
the standard mechanism for NLA packages to describe their integration points.

Files created:
- `install/install.md` — orchestrator
- `install/CLAUDE-intent.md` — runtime identity intent
- `install/skills-intent.md` — skill wrapper intent
- `install/structure-intent.md` — directory structure intent (includes feedback log)

Blast radius: framework only (new directory, no existing behavior changed)

### Issue #2 — Feedback log as framework concept (Accept)
Added the feedback log as a sibling to the friction log — internal observations vs.
external feedback, both feeding into `/maintain`.

- `core/skills/maintain.md` — added to Required Reading, added Processing Feedback Log
  Entries section, renamed "Friction Log Pipeline" to "Maintenance Pipeline"
- `.claude/skills/maintain/SKILL.md` — same additions for the framework itself
- `scaffold/reference/` — added `feedback-log.md` and `feedback-log-archive.md`
- `.claude/skills/create-app/SKILL.md` — added feedback log files to both file tables
- `reference/feedback-log.md` and `reference/feedback-log-archive.md` — created for
  the framework itself

Blast radius: all projects (core skill change), new projects (scaffold), framework

### Issue #3 — Session-start checklist (Accept items 1+3, decline 2/5/6, defer 4)
Added a Session Start section to `/maintain` that surfaces pending friction log and
feedback log counts, reads the most recent session log for continuity, and presents
a summary before asking what to work on.

- `core/skills/maintain.md` — added Session Start section after Required Reading
- `.claude/skills/maintain/SKILL.md` — same addition

Blast radius: all projects (core skill change), framework

## Decisions Made

- **Reordered implementation: #1 before #2** — Originally planned to implement the
  feedback log (#2) first. Realized that without `install/structure-intent.md`, there's
  no standard way for existing projects to learn they should have a feedback log. The
  install/ directory provides the propagation mechanism.

- **Issue #1 verdict changed from Defer to Accept** — Initially assessed as premature
  (only one extension exists). User correctly pointed out that penny post's install/
  directory exists now and NLAs need a way to use it now. Deferring would mean ad hoc
  workarounds costing as much as the real thing.

- **Issue #3, Item 2 declined (session log template)** — Investigation showed penny
  post's thin wrapper correctly delegates to `core/skills/maintain.md`, which already
  has the template. Penny post's actual session log uses and extends it. The item was
  filed from a mistaken premise.

- **Simulated penny post triage conventions** — Framework doesn't have `/check-feedback`
  installed yet, so we followed penny post's `app/check-feedback.md` manually: read
  issues, assess against project goals, propose verdicts, record in feedback log, comment
  on issues, close them.

## Blast Radius

- `core/skills/maintain.md` changes affect **all domain projects** (feedback log in
  Required Reading, Processing Feedback Log Entries section, Maintenance Pipeline section,
  Session Start section)
- `scaffold/` changes affect **new projects only**
- `install/` is **framework only** (new directory)
- Framework's own `/maintain` skill is **framework only**

## State at Close

[To be filled at session end]
