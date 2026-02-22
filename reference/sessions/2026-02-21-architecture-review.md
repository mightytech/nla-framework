# Architecture Review: NLA Framework

**Date:** 2026-02-21
**Trigger:** Post-/unpack skill addition. Focused on /unpack registration consistency and general document chain coherence.

## Document Chain

### Entry Point
`CLAUDE.md` is the root. It references:
- `core/nla-foundations.md` (for explanation)
- `config-spec.md` and `config.md` (for configuration)
- Skills table (14 skills)
- Key files table (8 entries)

### Framework Skill Wrappers (`.claude/skills/`)
16 directories: check-feedback, create-app, debrief, export, friction-log, install, install-app, maintain, preferences, think, unpack, update, validate, write-letter.

Each SKILL.md either:
- Delegates to `core/skills/[name].md` (most framework skills)
- Delegates to `../nla-penny-post/app/[name].md` (check-feedback, write-letter)
- Is self-contained (create-app, install-app, friction-log, maintain, preferences, validate)

### Core Skill Logic (`core/skills/`)
18 files: debrief, export, friction-log, install, maintain, preferences, README, startup, think, unpack, update, validate, validate-architecture, validate-debug, validate-scenario, validate-structural.

### Intent Files (`install/`)
7 files: CLAUDE-intent, example-catalog, install, README, skills-intent, structure-intent, update-notes.

### Chain Summary
```
CLAUDE.md
├── core/nla-foundations.md (explanation, loaded by domain projects at startup)
├── config-spec.md (configuration governance)
├── config.md (user preferences, optional)
├── .claude/skills/*/SKILL.md → core/skills/*.md (skill delegation)
├── install/*.md (project generation, install, update)
└── reference/ (maintenance records, design rationale)
```

---

## Findings

### Fix

1. **`core/skills/README.md` "What's Here" table**: Missing entries for `debrief.md` and `unpack.md`. The table lists 13 skills but the directory contains 15 logic files (excluding README). Both files exist in the directory but are not listed. An AI consulting this table to understand what's available would not know these skills exist. — **Cross-reference integrity** / Blast radius: all domain projects

2. **`.claude/skills/create-app/SKILL.md` Category 1 table**: Missing `.claude/skills/debrief/SKILL.md` and `.claude/skills/unpack/SKILL.md` in the mechanical files list. The table lists 9 skill wrappers to generate but `install/skills-intent.md` defines 11 (including debrief and unpack). New projects created by `/create-app` will be missing these two skill wrappers. — **Cross-reference integrity** / Blast radius: project generation

3. **`reference/design-rationale.md` /think section**: Line 1051 says `4. **Debrief** (future skill) — reflect on the process`. The debrief skill now exists (added same day, `core/skills/debrief.md`). The "(future skill)" annotation is stale. Anyone reading the /think design rationale would incorrectly believe /debrief has not been implemented. — **Consistency** / Blast radius: framework maintainers only

### Improve

4. **`core/skills/README.md` "Adding a New Skill" checklist**: Step 4 says "Update the framework's `/validate` to check for the new skill." This is vague — `/validate`'s structural check dynamically compares `.claude/skills/` against `CLAUDE.md`, so there is nothing to update in validate for a new skill. The step that IS needed and missing: "Update `core/skills/README.md`'s What's Here table." The checklist is the right place to prevent finding #1, but it points to the wrong file. — **Prerequisite sufficiency** / Blast radius: framework maintainers

5. **`core/nla-foundations.md` closing reference**: Line 174 says `see [overview.md](overview.md)`. This file is loaded by domain projects from `../nla-framework/core/nla-foundations.md`. The relative link `overview.md` does not resolve from the framework's `core/` directory. The LLM reads this as a directive, not a clickable link, so it interprets it correctly in domain project context (it finds `app/overview.md`). But the Markdown link itself would be broken if rendered. In framework context (when the framework is the working directory), there is no `overview.md` at all. — **Path resolution** / Blast radius: all domain projects (cosmetic; LLM interpretation is correct)

6. **`install/skills-intent.md` Extension Package Skills section**: Mentions `/check-feedback` and `/write-letter` are managed by their own package, "not by this file." However, CLAUDE.md's skills table includes both of these skills. Anyone reading `skills-intent.md` might incorrectly assume that `/create-app` should not generate these wrappers — which is correct (it should not), but there is no explicit note clarifying that these skills appear in the framework's CLAUDE.md because they are installed in the framework as a consumer of penny post, not because the framework generates them for domain projects. — **Conditional completeness** / Blast radius: project generation (edge case)

7. **`install/update-notes.md` /debrief entry "Affects" field**: Lists only `install/skills-intent.md` but the `/debrief` design rationale notes blast radius includes `core/skills/debrief.md` (a new core file). While technically correct (skills-intent is the only changed intent file), the update note does not mention the new core file that domain projects would access through the thin wrapper. The /think and /unpack entries have the same pattern — this is consistent across all three but slightly incomplete. — **Consistency** / Blast radius: `/update` behavior (minor — `/update` reads intent diffs, and the core file propagates automatically)

8. **`core/skills/maintain.md` (domain version)**: Line 91 references `app/shared/output-spec.md` with "(if it exists)" in the downstream effects table, which is correct. However, line 212-218 has a full section "Updating the Output Spec" that begins with "If the NLA has an output spec" — good conditional. But the phrasing "When the output format changes" assumes the NLA has an output format change workflow. For NLAs without an output spec, this section is harmless but slightly misleading as a common maintenance task. — **Language breadth** / Blast radius: all domain projects (minor)

### Note

9. **Framework CLAUDE.md vs. system-reminder context**: The CLAUDE.md loaded into the system-reminder at the top of this conversation is identical to the file on disk, confirming no drift between the two. Worth noting as a health check.

10. **Penny post skill wrappers delegate to `../nla-penny-post/`**: The `check-feedback` and `write-letter` skill wrappers reference `../nla-penny-post/app/check-feedback.md` and `../nla-penny-post/app/write-letter.md`. If penny post is not cloned as a sibling, these skills will fail with a missing file error. This is documented in `install/skills-intent.md` ("managed by their own package") and handled gracefully by the LLM (it would report the file doesn't exist). — **Conditional completeness** / Blast radius: framework operation

11. **`reference/design-rationale.md` update-notes section**: Header says "Not yet implemented" on line 696, but `install/update-notes.md` exists and has been in active use since 2026-02-19. The design rationale entry describes the design but its header annotation is stale. — **Consistency** / Blast radius: framework maintainers only

12. **Skill count alignment across surfaces**: CLAUDE.md lists 14 skills. `.claude/skills/` has 16 directories. The delta is `check-feedback` and `write-letter` — which ARE in CLAUDE.md's table (14 total). Recounting: create-app, install-app, maintain, friction-log, preferences, validate, check-feedback, write-letter, install, update, think, export, debrief, unpack = 14 in CLAUDE.md. 16 directories in `.claude/skills/`. Wait — 16 directories matches 14 skills + 2? Let me recount: check-feedback, create-app, debrief, export, friction-log, install, install-app, maintain, preferences, think, unpack, update, validate, write-letter = 14 directories. This is consistent. All 14 skills in CLAUDE.md have corresponding directories. No mismatches. — **Cross-reference integrity** (verified clean)

13. **`install/example-catalog.md`**: Lists Penny Post as an "Advanced" example NLA. Penny Post is an extension package, not a domain NLA in the traditional sense. Users might expect a domain NLA example and be confused when they clone what is actually a package with install manifests. However, the description ("Feedback conventions and skills package for NLA projects") is clear about what it is. — **Language breadth** / Blast radius: project generation (cosmetic)

14. **`export.md` excludes `/export` from plugins**: The export skill lists `install, update, export` as "Framework-only" tools not shipped to plugins. But the actual classification table on line 54 only lists `install, update` as "Framework-only" — it does not mention `export` in the table. The text at line 77 in the inventory template does say "Framework-only: install, update" without export. If export is meant to be excluded, it should be in the table. If it's meant to ship as a dev tool, the table is correct but other references are inconsistent. — **Consistency** / Blast radius: all domain projects (export behavior)

---

## Resolution

**Resolved:** Findings 1-6, 11, 14 fixed. Findings 7-8 deliberately left as-is.

### Fixed
- **#1, #2:** Added debrief and unpack to `core/skills/README.md` table and create-app Category 1 table.
- **#3:** Changed "(future skill)" to "(`/debrief`)" in design rationale.
- **#4:** Rewrote "Adding a New Skill" checklist with correct steps (update this table, update create-app, update CLAUDE.md/README, run validate to verify). Removed incorrect "update validate" step.
- **#5:** Fixed broken relative link in foundations — `[overview.md](overview.md)` → `` `app/overview.md` ``.
- **#6:** Added clarifying parenthetical to skills-intent.md explaining why penny post skills appear in the framework's CLAUDE.md.
- **#11:** Stale "Not yet implemented" annotation on update-notes design rationale section — already removed.
- **#14:** `/export` missing from Framework-only classification table in export.md — already added.

### Deliberately not fixed
- **#7 (update-notes Affects fields):** The "Affects" field tracks *changed* files, not *new* files. The core skill files are new additions, not changed intent files. Adding them would blur the distinction between what `/update` acts on (intent file changes) and what simply exists in the framework (new core files that propagate via `git pull`). The narrative in each entry already mentions the new skill. The pattern is consistent across /think, /debrief, and /unpack entries — changing it would require changing all three, and the current convention is technically correct.
- **#8 (maintain output-spec section):** The section already has correct conditional phrasing ("If the NLA has an output spec"). Its presence as a named maintenance task is part of the broader "output spec is optional" design that was already implemented and reviewed. Reducing its prominence would be a judgment call about how much weight to give it, not a coherence fix. The conditional is there and accurate.

---

## Summary

14 findings total: 3 fix, 5 improve, 6 note. 8 resolved, 2 deliberately left, 4 noted.

**The /unpack skill is now consistently registered across all surfaces.**

**The document chain is coherent.** The issues found were registration gaps from adding new skills — caused by a checklist that pointed to the wrong target. The checklist is now corrected, which should prevent these gaps for future skills.

**Overall assessment:** The framework's document chain tells a consistent story. No contradictions, no broken delegation paths, no layer boundary violations.
