# Skills Integration Intent

What framework skill wrappers the NLA should have after installing the NLA Framework.

---

## Skills to Create

All framework skills use the **thin wrapper pattern**: a minimal skill file in the
NLA's `.claude/skills/` that delegates to logic in `../nla-framework/core/skills/`.
This means pulling the framework repo updates skill logic without touching the NLA.

### /startup

**Purpose:** Load foundational context at session start, then run app-specific initialization if `app/startup.md` exists.
**Wrapper location:** `.claude/skills/startup/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/startup.md`

**Reference wrapper:**
```yaml
---
name: startup
description: Initialize the NLA runtime. Use at session start or when context feels stale after long work.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/startup.md`.
```

### /maintain

**Purpose:** Edit the NLA system itself — docs, skills, and library code.
**Wrapper location:** `.claude/skills/maintain/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/maintain.md`

**Reference wrapper:**
```yaml
---
name: maintain
description: Edit the NLA system itself — docs, skills, lib code, and configuration. Use when the user wants to improve or modify the system.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/maintain.md`.
```

### /friction-log

**Purpose:** Log observations to the friction log from any context.
**Wrapper location:** `.claude/skills/friction-log/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/friction-log.md`

**Reference wrapper:**
```yaml
---
name: friction-log
description: Log observations, issues, or positive findings to the friction log from any context
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/friction-log.md`.
```

### /validate

**Purpose:** Check system consistency (structural check, architecture review, scenario walkthrough, debug).
**Wrapper location:** `.claude/skills/validate/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/validate.md` (dispatcher that routes to mode files)

**Reference wrapper:**
```yaml
---
name: validate
description: Validate the NLA system — structural checks, architecture review, scenario walkthroughs, or debug unexpected behavior.
disable-model-invocation: true
---

Read and follow `../nla-framework/core/skills/validate.md`.
```

### /preferences

**Purpose:** Create or edit user configuration.
**Wrapper location:** `.claude/skills/preferences/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/preferences.md`

**Reference wrapper:**
```yaml
---
name: preferences
description: Create or edit user preferences for this NLA. Personalizes behavior without modifying the application.
disable-model-invocation: true
---

Read and follow `../nla-framework/core/skills/preferences.md`.
```

### /install

**Purpose:** Install a new NLA package into this project.
**Wrapper location:** `.claude/skills/install/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/install.md`

**Reference wrapper:**
```yaml
---
name: install
description: Install a new NLA package into this project. Reads the package's install manifest and synthesizes its intents into the NLA.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/install.md`.
```

### /update

**Purpose:** Update installed NLA packages to their latest versions.
**Wrapper location:** `.claude/skills/update/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/update.md`

**Reference wrapper:**
```yaml
---
name: update
description: Update installed NLA packages to their latest versions. Diffs current intents against the install log and applies changes.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/update.md`.
```

### /export

**Purpose:** Export this NLA project as a plugin for Claude Code or Cowork.
**Wrapper location:** `.claude/skills/export/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/export.md`

**Reference wrapper:**
```yaml
---
name: export
description: Export this NLA project as a plugin for Claude Code or Cowork. Converts the project into a self-contained plugin directory with all dependencies resolved.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/export.md`.
```

### /think

**Purpose:** Collaborative design exploration — think through what to build and why before planning how.
**Wrapper location:** `.claude/skills/think/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/think.md`

**Reference wrapper:**
```yaml
---
name: think
description: Collaborative design exploration — think through what to build and why before planning how. Use when work involves design judgment, unfamiliar territory, or multiple valid approaches.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/think.md`.
```

### /debrief

**Purpose:** Reflect on completed work — surface observations about process, instructions, and experience while context is fresh.
**Wrapper location:** `.claude/skills/debrief/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/debrief.md`

**Reference wrapper:**
```yaml
---
name: debrief
description: Reflect on completed work — surface observations about process, instructions, and experience while context is fresh. Use at task transitions.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/debrief.md`.
```

### /unpack

**Purpose:** Structure complex conversations — identify bundled threads and work through them sequentially.
**Wrapper location:** `.claude/skills/unpack/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/unpack.md`

**Reference wrapper:**
```yaml
---
name: unpack
description: Structure complex conversations — identify bundled threads and work through them sequentially. Use when a discussion has more threads than it can hold at once.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/unpack.md`.
```

---

## Wrapper Pattern

Each wrapper follows the structure shown in the reference wrappers above: YAML frontmatter
with `name`, `description`, and `disable-model-invocation: true`, followed by a single
delegation line pointing to the framework's core skill logic.

The wrapper is intentionally minimal. The NLA can add project-specific context
(e.g., "When maintaining, also check our deployment checklist") but the core
delegation should remain.

**`disable-model-invocation: true` is intentional on all skills.** It prevents
the AI from spontaneously invoking skills and removes them from the active prompt
that influences behavior. The AI can still follow any skill by reading the file
when the user asks. See the framework's design rationale for the full reasoning.

## Domain Skill Pattern

Domain-specific skills (task skills like `/format-article`) are NOT thin wrappers — they
contain the full skill logic because they're project-specific, not framework-provided.

A domain skill wrapper has this structure:

```yaml
---
name: [task-name]
description: [Brief description of what the task does]
disable-model-invocation: true
---

# [Task Title]

You are [brief role description]. Your job is to [what the task accomplishes].

## Execute

Read and follow the instructions in **`app/[task-name].md`**. That document is your
primary source of truth for this task.

It will direct you to read prerequisite docs (voice, common patterns, and
output spec if one exists) if you haven't already. Follow that prerequisite chain.
Values are loaded at startup and don't need task-level prerequisites.

## Input

If invoked with arguments, `$ARGUMENTS` contains the input.

Otherwise, the user will provide input in conversation.

## Key Guardrails

These apply throughout — they're non-negotiable:

- **The Cardinal Rule:** The human decides. The NLA proposes, explains, and
  challenges — but the human has final say.
- **Flag uncertainty:** When unsure, say so — don't silently make consequential choices.
- **Less is more.** [Domain-appropriate version of "don't overdo it."]

## What NOT to Do

- Don't write code to solve content problems — use editorial judgment
- Don't skip the documentation — read it every time, it may have been updated
- Don't make silent changes — flag uncertainty and restructuring decisions
- [Domain-specific guardrails as needed]
```

The guardrails section and "What NOT to Do" should be adapted to the NLA's domain. The
structure (frontmatter → role → execute → input → guardrails → prohibitions) is consistent
across all domain skills.

## Eject Pattern

Any wrapper can be replaced with a full skill file for complete customization.
This is the "eject" pattern — the NLA takes ownership of the skill logic and
no longer receives framework updates for that skill. This is a deliberate choice,
not an accident.

## Extension Package Skills

Some skills (like `/check-feedback` and `/write-letter` from the penny post package) are
managed by their own package's install manifest, not by this file. If those packages are
installed, they'll appear in `CLAUDE.md`'s skills table alongside framework skills, but
their wrappers are created by the package's own install process. (The framework's own
`CLAUDE.md` lists these skills because the framework itself has penny post installed —
domain projects only get them if they install the package separately.)

---

## What NOT to Change

When updating an existing NLA's skills:

- Don't remove or overwrite domain-specific skills
- Don't modify wrappers that have been ejected (customized beyond thin wrapper)
- Framework skills are additive — they sit alongside domain skills

---

*This describes intent, not literal text. The installing AI should create wrappers
that fit the NLA's existing skill conventions.*
