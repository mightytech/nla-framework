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

### /maintain

**Purpose:** Edit the NLA system itself — docs, skills, and library code.
**Wrapper location:** `.claude/skills/maintain/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/maintain.md`

### /friction-log

**Purpose:** Log observations to the friction log from any context.
**Wrapper location:** `.claude/skills/friction-log/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/friction-log.md`

### /validate

**Purpose:** Check system consistency, trace scenarios, debug behavior.
**Wrapper location:** `.claude/skills/validate/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/validate.md`

### /plan

**Purpose:** Planning mode for new tasks or major changes.
**Wrapper location:** `.claude/skills/plan/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/plan.md`

### /preferences

**Purpose:** Create or edit user configuration.
**Wrapper location:** `.claude/skills/preferences/SKILL.md`
**Delegates to:** `../nla-framework/core/skills/preferences.md`

## Wrapper Pattern

Each wrapper follows this structure:

```yaml
---
name: [skill-name]
description: [Brief description of what the skill does]
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/[skill-name].md`.
```

The wrapper is intentionally minimal. The NLA can add project-specific context
(e.g., "When maintaining, also check our deployment checklist") but the core
delegation should remain.

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
