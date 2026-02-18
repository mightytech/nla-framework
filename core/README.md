# core/ — Framework Foundations

This directory contains the universal building blocks that every NLA built on the framework shares. Domain projects don't modify these files — they read them.

---

## What's Here

### `nla-foundations.md`

The conceptual foundation for all NLAs. Defines what a Natural Language Application is, the structure gradient (human flexibility → LLM judgment → traditional code determinism), the cardinal rule, and the principles that guide NLA design.

Every domain project reads this at startup via `/startup`. It's the shared mental model that makes an NLA behave like an NLA regardless of domain.

### `skills/`

Skill logic files that domain projects delegate to via thin wrappers. See [skills/README.md](skills/README.md) for details.

---

## Relationship to Domain Projects

Domain projects reference `core/` via `../nla-framework/core/` paths. The thin wrapper pattern in `.claude/skills/` provides Claude Code discoverability while keeping logic here, updatable via `git pull`.

Changes to files in `core/` affect **every domain project** on their next session. This is the highest blast radius in the framework.

---

*This directory is maintained by the framework developer via `/maintain`. Domain projects consume it, never modify it.*
