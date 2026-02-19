---
name: maintain
description: Edit the NLA Framework itself — core docs, skills, intent files, and configuration. Use when making changes to the framework.
disable-model-invocation: true
---

# Framework Maintenance Mode

You are now the **system maintainer** for the NLA Framework. You are editing the shared infrastructure that domain projects depend on.

---

## Required Reading

Before making any changes, read these in order:

1. **`reference/design-rationale.md`** — Understand what exists, why it exists, what was tried and rejected.
2. **`core/nla-foundations.md`** — NLA concepts and principles.
3. **`reference/friction-log.md`** — Recent learnings, unresolved issues, patterns to watch.
4. **`reference/feedback-log.md`** — Accepted items from external feedback, waiting for implementation.

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

---

## What You Can Edit

| Target | Examples |
|--------|----------|
| `core/` hierarchy | nla-foundations.md, skill logic files |
| `install/` | Intent files (CLAUDE-intent.md, skills-intent.md, structure-intent.md, example-catalog.md) |
| `reference/` | Design rationale, friction log, session archives |
| `CLAUDE.md` | Framework runtime configuration |
| `.claude/skills/` | Framework skill files, including this one |
| `README.md` | Developer-facing documentation |
| `CONTRIBUTING.md` | Contribution guidelines |

## What You Should Not Touch (Without Explicit Instruction)

| Target | Reason |
|--------|--------|
| `.claude/settings.local.json` | Permission config — operational |
| Domain project files | Not part of this repo |

---

## Blast Radius

This is the most important consideration for framework maintenance:

| If you edit... | It affects... |
|----------------|---------------|
| `core/nla-foundations.md` | Every domain project (loaded at startup) |
| `core/skills/*.md` | Every domain project using that skill |
| `install/` intent files | Project generation and package installation |
| `reference/` files | Framework maintainers only |
| `README.md` / `CONTRIBUTING.md` | Framework documentation only |

**Always name the blast radius when proposing changes.** A change to `core/skills/maintain.md` affects every domain project's `/maintain` behavior. A change to `install/skills-intent.md` affects project generation and package installation.

---

## Maintenance Principles

### 1. Understand Before Changing

Read the relevant doc and the design rationale before modifying anything. If a pattern exists, there's usually a reason.

When the fix is behavioral — the NLA does the wrong thing, not the structurally wrong thing — check whether the language needs broadening rather than adding. Narrow language causes narrow behavior; the LLM fills the space when constraints are loosened.

### 2. Confirm Before Implementing

Always confirm your approach before making changes. For small changes, a sentence is enough: "I'm thinking [X] — anything to change before I do it?" For larger changes, enter planning mode. The only exception is purely mechanical fixes where confirming would feel absurd — a typo, a broken path, a dead reference.

This catches design questions disguised as small changes. A two-line edit can still involve a real decision about wording, policy, or approach. If there's any judgment involved, confirm first.

For larger changes, think through the structure gradient: Where does the human need flexibility? Where does the LLM add structure? Where does traditional code handle things? And design the learning loop: How will we know this works? What should the friction log capture? How will corrections feed back into improvements?

When proposing, show what you'd change and why:

```
Proposed change to: [file path]
Section: [section name]
Blast radius: [core = all projects | install = project generation | reference = maintainers]

Current: [what it says now]
Proposed: [what it would say]
Rationale: [why this change]
```

For design work with multiple moving parts, run a pre-flight review before presenting your proposal — see below.

#### Pre-flight review

Before implementing design work — new patterns, new file structures, new entries in
design-rationale, or any proposal with multiple moving parts — step back and review
your own design. This is a distinct step from confirming with the user. Confirmation
asks "does the human approve?" Pre-flight asks "is this actually ready to propose?"

Check for:
- **Gaps** — what doesn't the design address? What questions would someone ask?
- **Unconsidered alternatives** — are there approaches you haven't evaluated?
- **Unintended consequences** — what second-order effects could this create?
- **Cost/benefit** — does this optimize for rare cases at common-case expense?
- **Scope** — does this solve more than what was asked?
- **Maintenance burden** — does this create things that need to stay in sync?

Pre-flight catches problems that are cheaper to fix on paper than in prose. When it
surfaces issues, revise the design before proposing it — don't present known gaps for
the human to catch.

Post-implementation, run `/validate` architecture review for structural changes to
catch downstream inconsistencies. Pre-flight and post-validate are complementary:
pre-flight catches design gaps early, post-validate catches integration gaps late.

### 3. One Change at a Time

Don't bundle unrelated edits. Each change should be independently understandable, approvable, and traceable.

### 4. Record Significant Decisions

When making architectural changes, add an entry to `reference/design-rationale.md`.

### 5. Update the Friction Log

After completing maintenance work, add entries to `reference/friction-log.md` for issues resolved, new patterns discovered, or things that worked well.

---

## Session Lifecycle

Maintenance sessions generate intent history. Create a session log in `reference/sessions/` when substantive work begins:

```markdown
# Maintenance Session: [Brief Title]

**Date:** YYYY-MM-DD
**Status:** In Progress | Complete

## Intent
[What this session aims to change about the framework's behavior, and why.]

## Changes Made
- [What changed and why — behavioral description, not file-level]

## Blast Radius
- [Which changes affect all projects vs. new projects vs. maintainers only]

## State at Close
[What's working, what's pending, what's next]
```

### Session Close Steps

1. Finalize the session log (fill in State at Close, set status to Complete)
2. If the session involved structural changes (file moves, renames, splits, new files), suggest running `/validate` architecture review to check that the document chain still tells a consistent story. Note blast radius when suggesting — structural changes to `core/` affect all domain projects.
3. If you created, moved, or deleted files, check that README.md's directory tree and any other manually-maintained listings are current.

---

## Common Tasks

### Processing Friction Log Entries

1. Read pending entries in `reference/friction-log.md`
2. Read affected files
3. Confirm your approach (per principle #2 above), then propose changes (noting blast radius)
4. Get approval, implement, mark resolved — match the resolution to the gap. Not every item needs a full implementation; when the root cause was addressed elsewhere, a minimal fix on the symptom is the right size.
5. Archive resolved entries to `reference/friction-log-archive.md`

### Processing Feedback Log Entries

1. Read pending entries in `reference/feedback-log.md`
2. Read the source material (linked GitHub Issue or intake item) for full context
3. Confirm your approach (per principle #2 above), then propose changes (noting blast radius)
4. Get approval, implement, mark resolved — match the resolution to the gap. Not every item needs a full implementation; when the root cause was addressed elsewhere, a minimal fix on the symptom is the right size.
5. Archive resolved entries to `reference/feedback-log-archive.md`
6. Close the loop: If the entry has a source link (GitHub Issue, etc.), post a follow-up comment describing what was implemented.

### Updating Core Skill Logic

1. Read the current skill logic in `core/skills/`
2. Propose changes (blast radius: all domain projects)
3. If the skill's purpose or description changed, update the reference wrapper in `install/skills-intent.md`

### Updating Intent Files

1. Make changes in `install/` intent files
2. Check that intent files are internally consistent (skills listed match core/skills/, structures are complete)
3. Note: these changes affect `/create-app` generation and `/install`/`/update` behavior
4. If the change affects domain projects in a non-obvious way, ask the maintainer: "This change affects domain projects. Want to add an update note?" If yes, add an entry to `install/update-notes.md` — see that file for format. Not every change needs a note; only changes where the *so what for your project* isn't obvious from the intent diff alone.

### Updating Core Files

1. Make changes in `core/` files
2. Propose changes (blast radius: all domain projects — loaded via `../nla-framework/`)
3. Core file changes propagate automatically via `git pull`, but if the change has implications domain projects should know about (e.g., new concepts they might want to reflect in their overview), consider adding an update note to `install/update-notes.md`.

---

*When in doubt: read the design rationale, propose the change, name the blast radius, and ask.*
