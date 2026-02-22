# Maintenance Session: Voice/Values Design Exploration

**Date:** 2026-02-22
**Status:** In Progress

## Intent
Explore whether and how to split voice-and-values.md into separate concerns, support multiple voices, and treat values-as-transparency as a foundational NLA concept. This is a /think session — exploring what/why before planning how.

## Design Decisions (from /think session)

1. **Foundations:** New principle (values transparency) between Judgment Over Rules and the Cardinal Rule. All priorities are value choices, varying in stakes not category. NLAs make them visible; traditional code hides them. No neutral default. Range from stylistic to legal.
2. **File split:** `voice-and-values.md` → `values.md` + `voice.md`. Both required for new projects. No backward-compatibility fallback — migration via update notes and `/update`.
3. **Loading:** `values.md` at startup (infrastructure, always present — execution and maintenance). `voice.md` stays task-level shared context. Values awareness enables soft contradiction flagging ("are you sure?") across the whole lifecycle.
4. **Multiple voices:** Supported pattern, not engineered feature. One or more voice files in `app/shared/`, self-contained, referenced by task docs.
5. **Naming:** `values.md`.
6. **Create-app:** Light touch — one tradeoffs-oriented question, seeds the file with a sentence or two. Maintenance cycle refines. Validate architecture review gains a values-consistency dimension.

## Changes Made
- Added "Values Are Visible" as Principle #3 in `core/nla-foundations.md`, renumbering existing 3-6 to 4-7
- Updated `core/skills/startup.md` — values.md replaces voice-and-values.md in the startup chain; voice stays task-level
- Updated `core/skills/maintain.md` — split downstream effects table, added values-awareness guidance ("are you sure?" soft flagging)
- Updated `core/skills/validate-architecture.md` — added "Values consistency" analytical category
- Updated `core/skills/validate-structural.md` — updated file reference examples
- Updated `core/skills/preferences.md` — split conflict detection to reference both files, added values-override stakes note
- Updated `core/skills/export.md` — principle count 1-6 → 1-7, file reference updates
- Updated `core/skills/friction-log.md` — example reference update
- Updated `install/structure-intent.md` — split directory entry, added values vs. voice explanation and multiple-voices note
- Updated `install/CLAUDE-intent.md` — added values-are-visible grounding principle, added values protection to "What NOT to Change"
- Updated `install/skills-intent.md` — domain skill prerequisites: voice only (values at startup)
- Updated `.claude/skills/create-app/SKILL.md` — added values/tradeoffs info target, conversation grouping, split Category 3 table, split Domain File Structures, updated generation order and narration
- Added update note to `install/update-notes.md` with migration guidance
- Added "Values and Voice Separation" section to `reference/design-rationale.md`
- Updated two historical examples in design-rationale.md
- Marked friction log entry as resolved
- Updated README.md domain project tree

## Blast Radius
- `core/nla-foundations.md`: all domain projects (new principle, renumbering)
- `core/skills/*`: all domain projects (reference updates, new validate category, values awareness in maintain)
- `install/*`: project generation, `/install`, `/update`
- `.claude/skills/create-app/SKILL.md`: project creation
- `reference/`: framework maintainers only

## State at Close
[pending — implementation complete, awaiting commit]
