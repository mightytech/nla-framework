# Maintenance Session: Writing Standards Phase 2 (+ dual-maintain fix)

**Date:** 2026-04-18
**Status:** In Progress

## Intent

Two pieces of work, sequenced so the first unblocks the second:

1. **Dual-maintain fix** (friction entry 2026-03-03, bumped to pending last
   session). Broaden `core/skills/maintain.md` so the framework can thin-wrap
   it following the `/validate` pattern — core holds universal methodology,
   the framework wrapper carries framework-specific addenda. Clears the sync
   burden (which grew during the 2026-04-17 session when Writing Standards
   was dual-applied) before Pass 1 below starts touching both files.

2. **Writing Standards Phase 2** (feedback item #21). Two-pass review of
   framework docs against the standards at `reference/standards/nla-writing.md`.
   Pass 1: behavioral gaps (standards 2.3, 2.4, 8.3) on ~12 high-risk
   operative docs. Pass 2: craft refinements (4.2, 4.4, 3.5) across core
   skills + intent files. User preference: single-session sweep if energy
   holds; check in after Pass 1.

## Changes Made

- **Dual-maintain fix landed (friction 2026-03-03).** Broadened
  `core/skills/maintain.md` to work in both domain-project and framework/package
  contexts — conditional path phrasing for foundations and project overview,
  project-type-agnostic "What You Can Edit" table, principle #3 renamed
  "Check for Downstream Effects" → "Name the Blast Radius" as a universal
  principle (domain-project specifics — shared-context table and values
  awareness — preserved inside the section), Writing Standards path broadened.
  Shrank `.claude/skills/maintain/SKILL.md` to the `/validate` wrapper pattern:
  framework-specific opening + required reading, delegation to core for
  methodology, framework-specific addenda (editable targets, Framework Blast
  Radius Taxonomy, framework-specific Common Tasks: Updating Core Skill Logic,
  Updating Intent Files, Updating Core Files). Update-notes entry added
  describing the no-op for domain projects and the cosmetic principle rename.
  Friction entry moved to archive with resolution note.

## Blast Radius

- `core/skills/maintain.md` — all domain projects (consumer-facing).
  Behavioral no-op for existing domain projects; principle rename is cosmetic.
- `.claude/skills/maintain/SKILL.md` — framework maintenance only
  (framework-internal).
- `install/update-notes.md` — announces the change to domain-project
  maintainers (consumer-facing).
- `reference/friction-log.md` / `reference/friction-log-archive.md` —
  maintainers only (internal).
- `reference/sessions/2026-04-18-writing-standards-phase-2.md` — maintainers
  only (internal).

## Decisions Made

- **Dual-maintain fix follows the `/validate` wrapper pattern.** Core holds
  universal maintenance methodology (Session Start, Maintenance Principles,
  Session Lifecycle, Writing Standards pointer, Shippability, Processing
  Friction/Feedback logs). Framework wrapper carries framework-specific
  addenda (editable targets, Blast Radius taxonomy, framework-specific
  Common Tasks). Core language broadens where it had hardcoded `app/`
  references so both contexts read cleanly.
- **Blast Radius is a universal principle, not framework-specific.** User
  confirmed. Core gains a "Name the Blast Radius" section framing the
  principle generally; framework wrapper specifies the framework-level
  taxonomy (which projects inherit what).

## What Didn't Work

*(Updated as the session progresses.)*

## Friction Log Entries Processed

- 2026-03-03 — Dual-maintain sync burden: resolved, archived

## Feedback Log Entries Processed

- #21 Phase 2 (writing standards review): in-progress

## Pass 1 Findings (scratch)

*(Populated as the review walks each doc. Format per finding:
File • Standard • Observation • Proposed fix • Severity.)*

## Pass 2 Findings (scratch)

*(Populated in Pass 2 if we proceed there.)*

## Debrief

*(Added at session close.)*

## State at Close

*(Added at session close.)*
