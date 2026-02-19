# Skills Integration Intent

What framework skill wrappers the NLA should have after installing the NLA Framework.

---

## Skills to Create

All framework skills use the **thin wrapper pattern**: a minimal skill file in the
NLA's `.claude/skills/` that delegates to logic in `../nla-framework/core/skills/`.
This means pulling the framework repo updates skill logic without touching the NLA.

### /startup

**Purpose:** Load foundational context at session start.
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

### /plan

**Purpose:** Planning mode for new tasks or major changes.
**Wrapper location:** `.claude/skills/plan/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/plan.md`

**Reference wrapper:**
```yaml
---
name: plan
description: Planning mode for building new tasks or making major changes to the NLA system
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/plan.md`.
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

It will direct you to read prerequisite docs (voice/values, common patterns, output spec)
if you haven't already. Follow that prerequisite chain.

## Input

If invoked with arguments, `$ARGUMENTS` contains the input.

Otherwise, the user will provide input in conversation.

## Key Guardrails

These apply throughout — they're non-negotiable:

- **The Cardinal Rule:** The human must always be able to compare your changes against
  the original and easily revert.
- **Flag uncertainty:** Use TK notes (`TK [VERIFY]`, `TK [QUESTION]`, `TK [MISSING]`,
  `TK [SUGGESTION]`) for any judgment call that might need adjustment.
- **Less is more.** [Domain-appropriate version of "don't overdo it."]

## What NOT to Do

- Don't write code to solve content problems — use editorial judgment
- Don't skip the documentation — read it every time, it may have been updated
- Don't make silent changes — flag restructuring with TK notes
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

## What NOT to Change

When updating an existing NLA's skills:

- Don't remove or overwrite domain-specific skills
- Don't modify wrappers that have been ejected (customized beyond thin wrapper)
- Framework skills are additive — they sit alongside domain skills

---

*This describes intent, not literal text. The installing AI should create wrappers
that fit the NLA's existing skill conventions.*
