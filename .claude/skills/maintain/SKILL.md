---
name: maintain
description: Edit the NLA Framework itself — core docs, skills, intent files, and configuration. Relevant when the user wants to make changes to the framework. AI: Suggest as an option; invoke only on user assent or `/maintain`.
---

# Framework Maintenance Mode

You are now the **system maintainer** for the NLA Framework. You are editing the shared infrastructure that domain projects depend on. What you change here ripples to every downstream NLA the next time it runs `/update`.

---

## Required Reading

Before making any changes, read these in order:

1. **`reference/design-rationale.md`** — Understand what exists, why it exists, what was tried and rejected.
2. **`core/nla-foundations.md`** — NLA concepts and principles.
3. **`reference/friction-log.md`** — Recent learnings, unresolved issues, patterns to watch.
4. **`reference/feedback-log.md`** — Accepted items from external feedback, waiting for implementation.

The framework doesn't have `app/overview.md` — skip that step from the core skill's required reading.

Then read the specific files relevant to your task.

---

## Core Methodology

Read and follow `core/skills/maintain.md` for the full maintenance methodology — Session Start, Before Starting Work, Maintenance Principles (Understand, Confirm, Name the Blast Radius, One Change at a Time, Record Decisions, Update Friction Log), Pre-flight Review, Session Lifecycle, Writing Standards (author-time and diagnostic use), Shippability at Commit Time, and the universal Common Tasks (Processing Friction/Feedback Log Entries, Adding a New Skill).

Then apply the framework-specific addenda below. The addenda override or supplement the core where explicitly noted.

---

## What You Can Edit (framework context)

This replaces the editable-targets table in `core/skills/maintain.md`:

| Target | Examples |
|--------|----------|
| `core/` hierarchy | `nla-foundations.md`, skill logic files |
| `install/` | Intent files (`CLAUDE-intent.md`, `skills-intent.md`, `structure-intent.md`, `example-catalog.md`, `package-intent.md`, `update-notes.md`) |
| `reference/` | Design rationale, friction log, session archives, standards |
| `CLAUDE.md` | Framework runtime configuration |
| `.claude/skills/` | Framework skill files, including this one |
| `README.md` | Developer-facing documentation |
| `CONTRIBUTING.md` | Contribution guidelines |
| `lib/` | Traditional-code helpers (e.g., `export.py`) |

## What You Should Not Touch (framework context)

| Target | Reason |
|--------|--------|
| `.claude/settings.local.json` | Permission config — operational |
| Submodules under `packages/` | Part of another project — edit in that project's own maintenance context |
| Domain project files outside this repo | Not part of this repo — flow changes through `/update` |

---

## Framework Blast Radius Taxonomy

Core principle #3 (Name the Blast Radius) applies universally. The framework-specific taxonomy:

| If you edit... | It affects... |
|----------------|---------------|
| `core/nla-foundations.md` | Every domain project (loaded at startup) |
| `core/skills/*.md` | Every domain project using that skill |
| `install/` intent files | Project generation and package installation |
| `reference/` files | Framework maintainers only (internal, not shipped) |
| `CLAUDE.md` | Framework maintainers only (framework's own runtime identity, not read by consumers) |
| `README.md` / `CONTRIBUTING.md` | Framework documentation only |
| `.claude/skills/` | Framework maintenance behavior only |

A change to `core/skills/maintain.md` affects every domain project's `/maintain`. A change to `install/skills-intent.md` affects project generation and package installation. Name the specific blast radius when proposing.

**Dual-channel coverage for runtime principles.** When adding or changing a behavioral principle that should fire during *both* consumer NLA sessions *and* framework maintenance sessions (`/create-app`, `/maintain`, `/think` run from the framework itself), check whether the change needs to land in two channels:

- `install/CLAUDE-intent.md` propagates to every domain project's CLAUDE.md via `/create-app` and `/update` — covers consumer NLAs.
- The framework's own `CLAUDE.md` is **hand-written, not synthesized from `install/CLAUDE-intent.md`** — so intent-file changes do *not* propagate to it. Framework sessions need their own update.

If the principle applies to both, edit both. The intent-file channel alone leaves the framework uncovered; the framework's CLAUDE.md alone leaves consumers uncovered. The same pattern may apply to package wrappers when a package has both intent files and its own runtime identity file.

---

## Framework-Specific Common Tasks

These supplement the universal Common Tasks in `core/skills/maintain.md`.

### Updating Core Skill Logic

1. Read the current skill logic in `core/skills/`.
2. Propose changes (blast radius: all domain projects).
3. If the skill's purpose or description changed, update the reference wrapper in `install/skills-intent.md`.

### Updating Intent Files

1. Make changes in `install/` intent files.
2. Check that intent files are internally consistent (skills listed match `core/skills/`, structures are complete).
3. Note: these changes affect `/create-app` generation and `/install` / `/update` behavior.
4. If the change affects domain projects in a non-obvious way, ask the maintainer: "This change affects domain projects. Want to add an update note?" If yes, add an entry to `install/update-notes.md` — see that file for format. Not every change needs a note; only changes where the *so what for your project* isn't obvious from the intent diff alone.

### Updating Core Files

1. Make changes in `core/` files.
2. Propose changes (blast radius: all domain projects — consumed via `packages/nla-framework/`).
3. Core file changes propagate to domain projects when they run `/update` to advance their framework submodule. If the change has implications domain projects should know about (e.g., new concepts they might want to reflect in their overview), consider adding an update note to `install/update-notes.md`.

---

*When in doubt: read the design rationale, propose the change, name the blast radius, and ask.*
