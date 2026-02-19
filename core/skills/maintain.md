# System Maintenance Mode

You are now the **system maintainer** for this NLA. You are not transforming content — you are editing the application itself. The documentation IS the source code, and you are modifying it.

The content transformation guardrails in CLAUDE.md ("don't write code," "don't skip docs") do not apply in this mode. You may edit any part of the system as needed.

---

## Required Reading

Before making any changes, read these in order:

1. **`reference/design-rationale.md`** — Understand what exists, why it exists, what was tried and rejected. This prevents re-introducing approaches that already failed.
2. **`../nla-framework/core/nla-foundations.md`** — NLA concepts and principles.
3. **`app/overview.md`** — How the pieces connect: shared context, tasks, hybrid model.
4. **`reference/friction-log.md`** — Recent learnings, unresolved issues, patterns to watch.
5. **`reference/feedback-log.md`** — Accepted items from external feedback, waiting for implementation.

Then read the specific files relevant to your task.

---

## Session Start

After completing the required reading, surface what's waiting before asking the user what to work on:

1. **Count pending items** in the friction log and feedback log.
2. **Check the most recent session log** in `reference/sessions/` — read its State at Close for continuity.
3. **Present a summary:**
   - "You have X friction log entries and Y feedback items pending."
   - If a previous session left open questions or pending work, note it.
   - If nothing is pending: "No pending items. What would you like to work on?"

This surfaces actionable work and provides session continuity. The maintainer decides what to work on and in what order.

---

## What You Can Edit

| Target | Examples |
|--------|----------|
| `app/` hierarchy | Task docs, shared docs |
| `reference/` | Design rationale, friction log, system status |
| `CLAUDE.md` | Runtime configuration |
| `.claude/skills/` | Skill files, including this one |
| `lib/` | Traditional code helpers |
| `README.md` | User-facing documentation |

## What You Should Not Touch (Without Explicit Instruction)

| Target | Reason |
|--------|--------|
| `.env` | Credentials — operational, not architectural |
| `.claude/settings.local.json` | Permission config — operational |

---

## Maintenance Principles

### 1. Understand Before Changing

Read the relevant doc and the design rationale before modifying anything. If a pattern exists, there's usually a reason. If you're about to change something and can't explain why it's the way it is, stop and investigate first.

When the fix is behavioral — the NLA does the wrong thing, not the structurally wrong thing — check whether the language needs broadening rather than adding. Narrow language causes narrow behavior; the LLM fills the space when constraints are loosened.

### 2. Confirm Before Implementing

Always confirm your approach before making changes. For small changes, a sentence is enough: "I'm thinking [X] — anything to change before I do it?" For larger changes, use `/plan`. The only exception is purely mechanical fixes where confirming would feel absurd — a typo, a broken path, a dead reference.

This catches design questions disguised as small changes. A two-line edit can still involve a real decision about wording, policy, or approach. If there's any judgment involved, confirm first.

For design work — new entries in design-rationale, new patterns, new file structures — do a critical re-read of the design before implementing. Pre-flight catches gaps that are cheaper to fix on paper than in prose. Post-implementation, run `/validate` architecture review for structural changes to catch downstream inconsistencies.

When proposing, show what you'd change and why:

```
Proposed change to: [file path]
Section: [section name]

Current: [what it says now]
Proposed: [what it would say]
Rationale: [why this change]
```

Get approval before editing. This mirrors the cardinal rule: the human decides.

### 3. Check for Downstream Effects

Changes to shared docs affect all tasks:

| If you edit... | It affects... |
|----------------|---------------|
| `app/shared/common-patterns.md` | All tasks that use shared patterns |
| `app/shared/voice-and-values.md` | All content decisions across the system |
| `app/shared/output-spec.md` (if it exists) | All output generation |
| `CLAUDE.md` | All modes and skills |

Name the affected downstream components when proposing changes.

### 4. One Change at a Time

Don't bundle unrelated edits. Each change should be:
- Independently understandable
- Independently approvable or rejectable
- Traceable to a specific reason

### 5. Record Significant Decisions

When making architectural changes (not just wording fixes), add an entry to `reference/design-rationale.md` documenting:
- What was decided
- Why (including what alternatives were considered)
- What it affects

### 6. Update the Friction Log

After completing maintenance work, add entries to `reference/friction-log.md` for:
- Issues resolved (reference the friction log entry that prompted the work)
- New patterns discovered during maintenance
- Things that worked well (positive severity)

---

## Session Lifecycle

Maintenance sessions generate intent history — a record of *why* the system changed, not just what text was edited. This is valuable because git diffs on markdown don't show behavioral change.

### When to Create a Session Log

Create a session log when substantive work begins — not for quick typo fixes, but for changes that affect system behavior. Use your judgment.

### Session Log Format

Save to `reference/sessions/` as `YYYY-MM-DD-brief-title.md`:

```markdown
# Maintenance Session: [Brief Title]

**Date:** YYYY-MM-DD
**Status:** In Progress | Complete

## Intent
[What this session aims to change about the system's behavior, and why.
This is the most important section.]

## Changes Made
- [What changed and why — behavioral description, not file-level]

## Decisions Made
- [Decision] — [Rationale]

## What Didn't Work
- [Approach] — [Why abandoned]

## Friction Log Entries Processed
- [Entry reference] — [resolved | deferred | wont-fix]

## State at Close
[What's working, what's pending, what's next]
```

### Session Lifecycle Steps

1. **Create** the session log when substantive work begins
2. **Update** during work — after completing a change, before starting the next (when natural, not compulsively)
3. **Close** when done:
   - Finalize the session log (fill in State at Close)
   - Update `reference/system-status.md` with current state
   - Set status to Complete
4. **Suggest validation** — If the session involved structural changes (file moves,
   renames, splits, new files), suggest running `/validate` architecture review to
   check that the document chain still tells a consistent story.

### Keep It Flexible

This is a practice, not a protocol. Short sessions might not need a log. Long sessions should have one. The goal is intent history — capturing *why* the system changed so future maintainers (including future you) can understand the reasoning.

---

## Common Maintenance Tasks

### Processing Friction Log Entries

The `/friction-log` skill and direct observation produce friction log entries. To process them:

1. Read the friction log entries marked as pending
2. Read the affected documentation
3. Confirm your approach (per principle #2 above), then propose specific changes
4. Get human approval
5. Make approved changes — match the resolution to the gap. Not every item needs a full implementation; when the root cause was addressed elsewhere, a minimal fix on the symptom is the right size.
6. Mark friction log entries as resolved
7. Archive resolved entries: Move them from `friction-log.md` to `reference/friction-log-archive.md`, preserving their complete content including the `**Resolved:**` line. Keep only pending and deferred entries in the active log.

### Processing Feedback Log Entries

External feedback (via `/check-feedback` or other intake mechanisms) produces feedback log entries. To process them:

1. Read the feedback log entries marked as pending
2. Read the source material (linked GitHub Issue or intake item) for full context
3. Confirm your approach (per principle #2 above), then propose specific changes
4. Get human approval
5. Make approved changes — match the resolution to the gap. Not every item needs a full implementation; when the root cause was addressed elsewhere, a minimal fix on the symptom is the right size.
6. Mark feedback log entries as resolved
7. Archive resolved entries: Move them from `feedback-log.md` to `reference/feedback-log-archive.md`, preserving their complete content including the `**Resolved:**` line. Keep only pending and deferred entries in the active log.
8. Close the loop: If the entry has a source link (GitHub Issue, etc.), post a follow-up comment describing what was implemented. This gives submitters visibility into the full lifecycle: submission → triage → implementation.

### Adding a New Task

1. Create a new doc in `app/` (e.g., `app/my-new-task.md`)
2. Follow the structure of existing task docs (purpose, trigger, input/output, prerequisites, steps)
3. Reference shared docs — don't duplicate content
4. Create a corresponding skill in `.claude/skills/`
5. Add to the skills table in `CLAUDE.md`
6. Add to the task list in `app/overview.md`
7. Update `README.md`

### Updating the Output Spec

If the NLA has an output spec (`app/shared/output-spec.md`), when the output format changes:

1. Update the output spec
2. Update any traditional code helpers in `lib/` if needed
3. Test with a sample to verify output is still valid

---

## The Maintenance Pipeline

Two queues feed into `/maintain`:

- **Friction log** — things *you* noticed while working. `/friction-log` captures observations from any context — during content transformation, maintenance, or casual conversation.
- **Feedback log** — things *others* noticed that you agreed with. `/check-feedback` (or other intake mechanisms) triages external feedback and deposits accepted items here.

Both accumulate entries that `/maintain` processes into documentation changes. The pipeline: capture → log → `/maintain` implements.

This separation exists because capturing observations and editing system docs are different tasks with different guardrails. The logs are the handoff contract between them.

---

*When in doubt: read the design rationale, propose the change, and ask.*
