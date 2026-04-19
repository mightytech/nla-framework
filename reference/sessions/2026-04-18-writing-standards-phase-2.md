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

- **Shippability tagging cadence captured as friction entry.** User observed
  mid-session that per-commit tagging (literal reading of the current
  shippability rule) inflates version numbers across a session and that
  session-end (or "meaningful release moment") tagging serves downstream
  consumers better. Local v0.0.5 tag on the dual-maintain commit was deleted
  (not pushed); session will tag at end if any tag is warranted. Full entry
  in friction-log.md awaiting future `/maintain` to process.

- **Pass 1 writing-standards review implemented (7 fixes).** All findings
  from the Pass 1 review landed:
  1. **`core/nla-foundations.md` principle #2 reframe** — renamed "The
     Documentation Is the Application" → "NLA Documents Are Source Code";
     new opening paragraph names the operational consequences (ambiguous
     instruction = bug, missing section = missing feature, inconsistent
     term = naming collision). Existing fix-is-in-docs and
     diagnose-from-artifacts material preserved. Update-notes entry added.
  2. **`CLAUDE.md` Maintenance Mode section** — added one sentence
     specifying when to suggest `/maintain` (editing framework files, core
     skill logic, intent files, or the framework's own configuration).
  3. **`core/skills/validate.md`** — removed redundant domain-project
     assumption note (same pattern as the one cleaned up in `maintain.md`).
  4. **`core/skills/startup.md` "After Loading"** — clarified as a
     user-facing startup summary (replacing ambiguous "Confirm you've
     read…").
  5. **`core/skills/validate-architecture.md`** — spelled out the
     after-each-file append cadence for writing findings incrementally.
  6. **`core/skills/export.md`** — added a calibration check for the
     foundation-skill synthesis (read it end-to-end as a cold reader; does
     it introduce the NLA without requiring prior context?).
  7. **`core/skills/think.md`** — broadened "Capturing Insights" to handle
     the case where no session log exists (surface to friction log, note to
     user, or prompt to start a session log).

## Blast Radius

- `core/skills/maintain.md` — all domain projects (consumer-facing).
  Behavioral no-op for existing domain projects; principle rename is cosmetic.
- `.claude/skills/maintain/SKILL.md` — framework maintenance only
  (framework-internal).
- `core/nla-foundations.md` — all domain projects (consumer-facing, loaded
  at startup). Principle rename and new opening paragraph; behavioral no-op.
- `CLAUDE.md` — framework maintenance only (framework-internal).
- `core/skills/{startup,validate,validate-architecture,export,think}.md` —
  all domain projects (consumer-facing). Minor refinements per Pass 1.
- `install/update-notes.md` — announces the changes to domain-project
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
- **Shippability tagging pattern: session-end over per-commit.** User
  pushed back on mid-session tag (v0.0.5 on the dual-maintain commit) as
  version inflation when more consumer-facing work was planned for the
  same session. Local tag deleted; session-end tagging is the better
  default. Captured in friction log for future `/maintain` to work into
  the shippability convention. Separates the *what-to-tag* question
  (consumer-facing content) from the *when-to-tag* question (meaningful
  release moments, not every commit).
- **Foundations principle #2 reframed.** Adopted the writing-standards'
  "NLA documents are source code, not documentation" framing in place of
  "The Documentation Is the Application" — sharper, more operationally
  specific, more compliant-invoking. Flagged as a Phase 2 consideration in
  the 2026-04-17 close; this session was the natural place to implement.

## What Didn't Work

*(Updated as the session progresses.)*

## Friction Log Entries Processed

- 2026-03-03 — Dual-maintain sync burden: resolved, archived

## Feedback Log Entries Processed

- #21 Phase 2 (writing standards review): in-progress

## Pass 1 Findings (scratch)

Docs reviewed (14): `core/nla-foundations.md`, `CLAUDE.md`,
`core/skills/{maintain, startup, validate, validate-structural,
validate-architecture, validate-scenario, validate-debug, validate-coherence,
think, update, install, close, export}.md`, `.claude/skills/create-app/SKILL.md`.

**Overall quality is high.** Most docs are well-written against the three
standards. Findings below are mostly modest refinements; only one is a
behavioral-risk item.

### High priority (behavioral)

1. **`core/nla-foundations.md` — principle #2 reframe.** Title and opening
   line frame as "The Documentation Is the Application" with the fix-is-in-docs
   narrative. The writing standards' framing ("NLA documents are source code,
   not documentation") is sharper and more operationally specific — an
   ambiguous instruction is a bug, a missing section is a missing feature. The
   current framing is narrower; the stronger framing invites stronger
   compliance. Standards: 2.3 + 2.4. Previously flagged in last session's
   close as a Phase 2 consideration. **Proposed fix:** Rename to "NLA
   Documents Are Source Code" and rewrite the opening paragraph to lead with
   the source-code framing; keep the docs-are-authoritative and
   diagnose-from-artifacts material as supporting points.

### Medium priority

2. **`CLAUDE.md` (framework) — Maintenance Mode section is too thin.** Lines
   37–39 say only "Different rules apply; the skill provides them." The LLM
   that reads CLAUDE.md knows `/maintain` exists (from the skills table) but
   the CLAUDE.md itself doesn't state *when* to suggest it. Standard: 2.3 —
   the doc produces what it contains. **Proposed fix:** Add one sentence
   specifying the trigger: "When the user wants to edit framework files, core
   skill logic, or intent files, suggest `/maintain`." Keep the section
   short — the skill's own wrapper handles the rest.

3. **`core/skills/validate.md` — domain-project assumption note is now
   out-of-step with the current wrapper shape.** Line 16–17 mirrors the note
   we just cleaned up in `maintain.md`. The framework's `/validate` wrapper
   is already a proper thin delegate with its own required reading; the note
   is informational noise rather than useful guidance. Standard: 2.3 — notes
   should specify behavior, not gesture at it. **Proposed fix:** Remove the
   note. The framework wrapper's own Required Reading section already
   supplies what's needed; the domain-project path reads naturally as-is.

### Low priority (nice-to-have)

4. **`core/skills/startup.md` — "After Loading" confirmation is ambiguous.**
   "Confirm you've read the foundational documents" — user-facing summary?
   Internal check? The follow-up text ("If config was loaded, note it") implies
   a brief user-facing message, but the opening is ambiguous. Standard: 2.3.
   **Proposed fix:** Lead with "Present a brief startup summary to the user:"
   then the current content as the content of that summary.

5. **`core/skills/validate-architecture.md` — "Write findings incrementally"
   could be more explicit.** For a review surfacing many findings, "after
   each file's review, append findings to the report" is clearer than
   "incrementally." Standard: 2.3. **Proposed fix:** Expand the one-liner to
   a two-liner spelling out the append-after-each-file cadence.

6. **`core/skills/export.md` — foundation-skill synthesis lacks a
   calibration example.** "One coherent identity document in the NLA's
   voice" is abstract guidance for a judgment-heavy task. Standard: 2.3
   (anchor intent with examples). **Proposed fix:** Add a line pointing at a
   representative foundation SKILL (e.g., from an example NLA's plugin) as a
   shape reference, if one exists; otherwise leave as-is until such an
   artifact exists.

7. **`core/skills/think.md` — "Capture it in the session log" presumes one
   exists.** `/think` can run outside maintenance sessions. Standard: 2.3.
   **Proposed fix:** Broaden to "If a session log exists, capture it there;
   otherwise, make sure the insight surfaces somewhere durable — a friction
   log entry, a note to the user, or a prompt to start a session log if the
   work is becoming substantial."

### Validated, no current gaps (10 docs)

`core/skills/maintain.md` (just edited), `core/skills/install.md`,
`core/skills/update.md`, `core/skills/close.md`,
`core/skills/validate-structural.md`, `core/skills/validate-scenario.md`,
`core/skills/validate-debug.md`, `core/skills/validate-coherence.md`,
`core/skills/think.md` (one minor finding only, otherwise strong),
`.claude/skills/create-app/SKILL.md`.

### Standards assessment (Pass 1)

- **2.3 (produces what it contains):** The most productive standard — most
  findings above trace to this. Where the doc relies on implication, the
  behavior softens. Active.
- **2.4 (emphasis shapes character):** Only finding #1 leans heavily on this
  standard. Most docs have well-calibrated emphasis already. Active for
  foundations edits, validated elsewhere.
- **8.3 (operative docs):** No findings explicitly traced to 8.3. The docs
  are uniformly self-contained; design rationale stays out with good
  distillation where it appears (e.g., update.md's "Why Fast-Forward Only").
  Validated, no current gaps.

## Pass 2 Findings (scratch)

*(Populated in Pass 2 if we proceed there.)*

## Debrief

*(Added at session close.)*

## State at Close

*(Added at session close.)*
