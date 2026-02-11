---
name: maintain
description: Edit the NLA Framework itself — core docs, skills, scaffold, and configuration. Use when making changes to the framework.
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

Then read the specific files relevant to your task.

---

## What You Can Edit

| Target | Examples |
|--------|----------|
| `core/` hierarchy | nla-foundations.md, skill logic files |
| `scaffold/` | All scaffold files (CLAUDE.md, app/, reference/, skills/) |
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
| `scaffold/` files | New projects only (existing projects unaffected) |
| `reference/` files | Framework maintainers only |
| `README.md` / `CONTRIBUTING.md` | Framework documentation only |

**Always name the blast radius when proposing changes.** A change to `core/skills/maintain.md` affects every domain project's `/maintain` behavior. A change to `scaffold/app/overview.md` only affects new projects.

---

## Maintenance Principles

### 1. Understand Before Changing

Read the relevant doc and the design rationale before modifying anything. If a pattern exists, there's usually a reason.

### 2. Propose Before Editing

Show the human what you'd change and why before making the edit. Format proposals as:

```
Proposed change to: [file path]
Section: [section name]
Blast radius: [core = all projects | scaffold = new projects | reference = maintainers]

Current: [what it says now]
Proposed: [what it would say]
Rationale: [why this change]
```

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

---

## Common Tasks

### Processing Friction Log Entries

1. Read pending entries in `reference/friction-log.md`
2. Read affected files
3. Propose changes (noting blast radius)
4. Get approval, implement, mark resolved
5. Archive resolved entries to `reference/friction-log-archive.md`

### Updating Core Skill Logic

1. Read the current skill logic in `core/skills/`
2. Read the corresponding scaffold wrapper in `scaffold/.claude/skills/`
3. Propose changes (blast radius: all domain projects)
4. Test with the sample formatter
5. Update scaffold wrapper description if the skill's purpose changed

### Updating the Scaffold

1. Make changes in `scaffold/`
2. Check that scaffold is internally consistent (skills tables match, paths resolve)
3. Note: these changes only affect new projects

---

*When in doubt: read the design rationale, propose the change, name the blast radius, and ask.*
