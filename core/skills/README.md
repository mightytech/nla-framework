# core/skills/ — Skill Logic Files

This directory contains the full logic for framework-provided skills. Domain projects access these through thin wrappers in their `.claude/skills/` directories.

---

## The Thin Wrapper Pattern

Claude Code discovers skills by scanning `.claude/skills/` in the project directory. It can't scan a sibling directory. So domain projects have thin wrappers:

**Domain project** (`.claude/skills/maintain/SKILL.md`):
```yaml
---
name: maintain
description: Edit the NLA system itself.
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/maintain.md`.
```

**This directory** (`core/skills/maintain.md`):
Contains the full skill logic — what to read, what to check, how to propose changes. Updated when the framework is `git pull`'d.

The wrapper gives Claude Code what it needs (YAML frontmatter, discoverability). The logic lives here (updatable, shared across all projects).

---

## What's Here

| File | Skill | Purpose |
|------|-------|---------|
| `startup.md` | `/startup` | Load foundational context at session start |
| `maintain.md` | `/maintain` | System maintenance mode — edit docs, skills, config |
| `friction-log.md` | `/friction-log` | Capture observations to the learning journal |
| `validate.md` | `/validate` | Dispatcher — routes to mode files below |
| `validate-structural.md` | `/validate` | Structural check — file references, skill tables, hierarchy |
| `validate-architecture.md` | `/validate` | Architecture review — document chain coherence |
| `validate-scenario.md` | `/validate` | Scenario walkthrough — trace docs for a hypothetical |
| `validate-debug.md` | `/validate` | Debug — explain divergence between expected and actual |
| `plan.md` | `/plan` | Planning mode for new tasks or major changes |
| `preferences.md` | `/preferences` | Create or edit user configuration |
| `install.md` | `/install` | Install a new NLA package |
| `update.md` | `/update` | Update installed packages |

### Multi-file skills

Some skills use a dispatcher + mode file pattern. The dispatcher (`validate.md`) presents a mode selection menu and routes to the appropriate mode file (`validate-*.md`). This keeps each mode focused while sharing common setup (required reading, scope constraints) in the dispatcher. Domain project wrappers still point to the dispatcher — they don't need to know about mode files.

---

## The Eject Pattern

Any thin wrapper can be replaced with a full skill file — the NLA takes ownership of that skill's logic. This is useful when a project needs behavior that differs from the framework default.

To eject a skill:
1. Read the logic file here (e.g., `maintain.md`)
2. Copy its content into the domain project's `.claude/skills/maintain/SKILL.md`
3. Add YAML frontmatter at the top
4. Customize as needed

The ejected skill no longer receives framework updates for that skill. The project can always re-wrap later by replacing the full file with a thin wrapper.

---

## Adding a New Skill

When the framework adds a new skill:

1. Create the logic file here (`core/skills/new-skill.md`)
2. Add a reference wrapper to `install/skills-intent.md`
3. Add the skill to `CLAUDE.md`'s skills table
4. Update the framework's `/validate` to check for the new skill

Existing domain projects pick up the new logic file on `git pull`, but they need to create a thin wrapper manually (or via `/update`).

---

*These files use `../nla-framework/core/` paths designed for domain projects. The framework's own skills in `.claude/skills/` use project-relative paths instead.*
