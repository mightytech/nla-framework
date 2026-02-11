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

Then read the specific files relevant to your task.

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

### 2. Propose Before Editing

Show the human what you'd change and why before making the edit. Format proposals as:

```
Proposed change to: [file path]
Section: [section name]

Current: [what it says now]
Proposed: [what it would say]
Rationale: [why this change]
```

Get approval before editing. This mirrors the cardinal rule: humans must be able to see and approve changes.

### 3. Check for Downstream Effects

Changes to shared docs affect all tasks:

| If you edit... | It affects... |
|----------------|---------------|
| `app/shared/common-patterns.md` | All tasks that use shared patterns |
| `app/shared/voice-and-values.md` | All content decisions across the system |
| `app/shared/output-spec.md` | All output generation |
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

### Keep It Flexible

This is a practice, not a protocol. Short sessions might not need a log. Long sessions should have one. The goal is intent history — capturing *why* the system changed so future maintainers (including future you) can understand the reasoning.

---

## Common Maintenance Tasks

### Processing Friction Log Entries

The `/friction-log` skill and direct observation produce friction log entries. To process them:

1. Read the friction log entries marked as pending
2. Read the affected documentation
3. Propose specific changes that address the confirmed issues
4. Get human approval
5. Make approved changes
6. Mark friction log entries as resolved
7. Archive resolved entries: Move them from `friction-log.md` to `reference/friction-log-archive.md`, preserving their complete content including the `**Resolved:**` line. Keep only pending and deferred entries in the active log.

### Adding a New Task

1. Create a new doc in `app/` (e.g., `app/my-new-task.md`)
2. Follow the structure of existing task docs (purpose, trigger, input/output, prerequisites, steps)
3. Reference shared docs — don't duplicate content
4. Create a corresponding skill in `.claude/skills/`
5. Add to the skills table in `CLAUDE.md`
6. Add to the task list in `app/overview.md`
7. Update `README.md`

### Updating the Output Spec

When the output format changes:

1. Update `app/shared/output-spec.md`
2. Update any traditional code helpers in `lib/` if needed
3. Test with a sample to verify output is still valid

---

## The Friction Log Pipeline

`/friction-log` captures observations from any context — during content formatting, maintenance, or casual conversation. Entries accumulate in the friction log, where patterns emerge over time. `/maintain` processes them into documentation changes.

The pipeline: `/friction-log` captures → friction log stores → `/maintain` implements.

This separation exists because capturing observations and editing system docs are different tasks with different guardrails. The friction log is the handoff contract between them.

---

*When in doubt: read the design rationale, propose the change, and ask.*
