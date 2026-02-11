# Framework Design Rationale

This document explains WHY the NLA Framework is built the way it is. It captures the reasoning, trade-offs, and principles that shaped the design.

**Audience:** Framework maintainers (human or AI) who need to understand the decisions before modifying them.

**Purpose:** Prevent well-intentioned "improvements" that break things that work across every domain project.

---

## Foundational Decisions

### Dual-Source Architecture

Domain projects reference the framework as a sibling directory (`../nla-framework/`). The framework is a separate git repo. `git pull` updates the framework independently.

**Why not a package/dependency manager:** NLA "code" is Markdown files. Package managers add complexity that doesn't match the medium. A sibling directory is simple, visible, and the LLM can read both repos naturally.

**Why not git submodules:** Submodules add tooling friction (init, update, sync). A sibling directory with thin wrappers is simpler and matches how LLMs already work — reading files from paths.

### `core/` for Framework Executable Docs

The framework's operative files live in `core/`, not `app/`. Domain projects use `app/` for their application. The different name signals the different role: `core/` is infrastructure read by all projects, `app/` is domain-specific content.

### `reference/` Stays As-Is

Both the framework and domain projects use `reference/` for maintenance records. Familiar to developers. The NLA twist (non-executing channel, operative during maintenance) is worth a sentence in docs, not a rename.

### Thin Wrapper Skills

Claude Code requires skills in `.claude/skills/` within the project. Framework skills use thin wrappers in domain projects that delegate to logic files in the framework's `core/skills/`.

**Why wrappers:** Claude Code discovers skills by scanning `.claude/skills/`. It can't scan a sibling directory. Wrappers give Claude Code what it needs (frontmatter, discoverability) while the actual logic lives in the framework (updatable via `git pull`).

**Eject pattern:** Any wrapper can be replaced with a full skill file for customization. The wrapper is a convenience, not a lock-in.

### /learning-feedback Excluded from Framework

The friction log + maintain cycle is the universal learning loop. `/learning-feedback` (structured correction analysis with before/after examples) is a domain extension for content-transformation NLAs, not universal infrastructure.

**Why not include it:** Not every NLA transforms content. A data-processing NLA, a classification NLA, or a planning NLA might not have "corrections" in the editorial sense. The framework provides the general pipeline; domains extend it.

### Framework Self-Maintenance

The framework has its own CLAUDE.md, `/maintain`, `/friction-log`, and `/plan` skills, plus a `reference/` directory. These are full skills (not thin wrappers) because the framework's working directory IS the framework — `../nla-framework/` paths would be self-referential.

**Why full skills instead of wrappers:** The logic files in `core/skills/` use `../nla-framework/core/` paths, designed for domain projects whose working directory is elsewhere. When the working directory is the framework itself, those paths break. Framework skills use project-relative paths (`core/...`, `reference/...`).

### Scaffold Directory

The framework contains `scaffold/` — a complete working project template with a sample article formatter. It serves two roles: manual fallback (copy and customize by hand) and structural reference for `/create-app`.

**Sample content, not markers:** Scaffold files have working sample content so someone can test immediately. "Replace me" markers would be metadata that influences LLM behavior.

### /create-app: Conversational Project Creation

`/create-app` asks about the user's domain, voice, and tasks, then generates a tailored project. The first interaction with the framework is itself an NLA interaction — flexible interface on top (conversation), structure underneath (generated project).

**Why conversational, not just copy:** The scaffold requires manual customization of 6+ files. That's an implementation burden the LLM can absorb. The user describes what they want; the LLM generates files that fit. This is the structure gradient in action.

**Why read scaffold at generation time:** The skill instructs the LLM to read each scaffold file as a structural reference immediately before generating its counterpart. This keeps generated projects in sync with scaffold updates — when the scaffold improves, `/create-app` picks up the changes without skill edits.

**Why framework-only:** Domain projects don't create other domain projects. `/create-app` lives in `.claude/skills/create-app/` (not in `core/skills/`) because it's framework infrastructure, not a universal skill that domain projects delegate to.

**Scaffold still exists because:** Some users prefer to see exactly what they're getting before customizing. Manual copy is transparent and requires no conversation. `/create-app` is the recommended path; scaffold is the fallback.

### Dual-Mode Framework CLAUDE.md

The framework's CLAUDE.md defaults to project creation (welcoming, directs to `/create-app`). `/maintain` activates maintenance mode. This mirrors the domain project pattern where the default mode is the primary task (content transformation) and `/maintain` switches to system editing.

**Why default to creation:** Most people arriving at the framework want to build something. A maintenance-focused landing page front-loads concepts (blast radius, session lifecycle) that new users don't need yet. Creation mode is welcoming; maintenance mode is available when needed.

**Why this mirrors domain projects:** Domain CLAUDE.md has a default mode (content transformation) and a maintenance mode. The framework CLAUDE.md has the same pattern — default mode (project creation) and maintenance mode. The consistency helps users who've seen one understand the other.

---

## Adding Decisions

When you make architectural changes to the framework, add an entry here documenting:
- What was decided
- Why (including what alternatives were considered)
- Blast radius (core = all projects, scaffold = new projects, reference = maintainers)

---

*This document is updated by the `/maintain` skill when architectural decisions are made.*
