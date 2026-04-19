# Maintenance Session: Writing Standards Phase 2 (+ dual-maintain fix)

**Date:** 2026-04-18
**Status:** Complete

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

- **Pass 2 writing-standards review implemented (1 fix).** Pass 2 reviewed
  against craft standards 4.2 (naming consistency), 4.4 (cross-references
  with context), 3.5 (positive instruction) across all Pass 1 scope plus
  five previously-unread core skills and all intent files. The framework is
  consistently well-written against these standards — only one finding
  warranted change:
  1. **`install/CLAUDE-intent.md` grounding principle** — updated the
     "Grounding Principles" bullet from "Documentation is the application"
     to "NLA documents are source code," matching the updated foundations
     principle #2 and the file's own Execution Principles bullet.
     Consolidated both bullets to use the canonical phrase. Existing
     update-notes entry extended to mention the intent-file change
     (previously named only `nla-foundations.md`) and the corresponding
     `/update` implication for domain projects (the proposal to reword
     their own CLAUDE.md grounding principles).

  The 3.5 finding (skills-intent.md domain-skill template leads with
  prohibitions) was considered and skipped as stylistic-only — the current
  form is legible and changing it propagates churn to new domain skills
  without behavioral change.

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
- `install/CLAUDE-intent.md` — all domain projects via `/create-app` and
  `/update` propagation (consumer-facing). Grounding principle rename to
  match the reframe; `/update` will propose the wording change to
  downstream CLAUDE.md files.
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

Docs reviewed: all of Pass 1's scope plus the five previously-unread core
skills (`debrief`, `check-updates`, `friction-log`, `session-checkpoint`,
`guide`) and all intent files (`CLAUDE-intent.md`, `skills-intent.md`,
`structure-intent.md`, `package-intent.md`, `install.md`, plus
`example-catalog.md`, `README.md`). Plus targeted greps for bare
cross-references and prohibition-led phrasing.

**Overall craft quality is high.** The framework is consistently written
against 4.2, 4.4, and 3.5. Findings are modest:

### Medium priority

1. **`install/CLAUDE-intent.md` "Grounding Principles" bullet inconsistent
   with updated foundations.** Line 18 says "Documentation is the
   application" — but the same file's "Execution Principles" (line 71) says
   "Documentation is source code," and `nla-foundations.md` principle #2
   (updated in Pass 1) is now "NLA Documents Are Source Code." The intent
   file drives `/create-app` and `/install` generation of downstream NLAs'
   CLAUDE.md files; an inconsistency here propagates. Standard: 4.2 (name
   things once, use that name consistently). **Proposed fix:** Update the
   Grounding Principles bullet to match the reframe — "NLA documents are
   source code. The prose in `app/` is operative — not documentation about
   an application. When behavior needs to change, the fix is better writing,
   not better code."

### Low priority / subjective

2. **`install/skills-intent.md` domain-skill-pattern "What NOT to Do"
   template leads with prohibitions.** The template (lines 298–303) shows
   bullets in the form "Don't X — do Y instead." Standard 3.5 prefers
   leading with the desired behavior: "Read the documentation every time —
   it may have been updated" rather than "Don't skip the documentation —
   read it every time." The current form is legible and widely used;
   flipping it propagates to every new domain skill's pattern via
   `/create-app`. **Proposed fix:** Rewrite to lead positive, with the
   failure mode implied by the "why." Subjective — the current form is
   acceptable and the flip is stylistic.

### Validated across the breadth (the real work this pass)

- **4.2 (naming consistency):** Across the codebase, canonical names hold:
  "framework" / "NLA Framework" / "packages/nla-framework/" are used
  consistently by context; "thin wrapper" / "thin wrapper pattern"; "NLA"
  vs. "domain project" are distinguished correctly (NLA is broader; domain
  project is specifically non-framework/non-package). Skill names match
  between CLAUDE.md skills tables, skill files, and intent files. One
  exception (finding #1). Validated, localized gap.
- **4.4 (cross-references with context):** Every significant
  cross-reference in core skills includes a topic or section name in
  context. Exemplars: `update.md`'s references to "Context Determines
  Competence" (line 70, 251) and `maintain.md`'s reference to
  "Shippability: Consumer-Facing vs. Internal Content" (line 281). Intent
  files consistently include "Purpose" / "Relationship" prose with file
  pointers. Validated, no current gaps.
- **3.5 (positive instruction):** Prohibitions in core skills fall into
  three categories, all acceptable: (a) scope boundaries in "You don't"
  sections (defining what the skill doesn't do — these are reference
  constraints, not operative instructions); (b) prohibition + positive
  alternative (e.g., update.md "Don't undo user work. If the user has
  changed something…flag it"); (c) defensive "What NOT to Change" sections
  in intent files (protecting existing content from well-intentioned
  overwrites — prohibition is the point here). One subjective finding
  (finding #2). Validated broadly.

### Standards assessment (Pass 2)

- **4.2 (naming):** One real finding. Validated otherwise. Active scope-narrow.
- **4.4 (cross-references):** No findings. Validated. Framework has a
  well-developed habit of providing section-name context with file pointers.
- **3.5 (positive instruction):** One subjective finding. Validated
  otherwise. The framework's prohibition use is measured and appropriate to
  the contexts it appears in.

## Debrief

Observations surfaced through an explicit `/debrief` conversation, refined
with user input.

### Process

- **Pre-flight review caught a real miscalibration.** The friction entry
  estimated the dual-maintain fix at 5–10 minutes (framed as "broaden
  paths"). When I actually read both files, the shape was a refactor to
  the `/validate` wrapper pattern, not path-broadening. Surfacing that
  before starting saved rework. Worth preserving: when estimates rest on
  a framing, re-check the framing before starting, not mid-stream.

- **Batched findings worked well for Pass 1, even better than planned.**
  Walking all 14 docs and presenting a batched findings list let cross-doc
  patterns emerge (e.g., "standard 2.3 did most of the real work"). Fix-
  as-you-go would have missed that. Pattern now twice-validated (last
  session's feedback triage used the same approach).

- **"Start narrow" reflex showed up differently this session — and it's
  the same bug the framework already names.** User's insight:
  `start-narrow = rules-reading-instead-of-intent-engagement`. When I
  read the shippability convention as a rule ("touches consumer-facing
  content → tag"), I pattern-matched to "does this commit match?" and
  missed "what cadence does this rule implicitly assume?" Engaging with
  intent would have surfaced the cadence question. The fix isn't a new
  principle (foundations #4 and writing standard 1.4 already cover it);
  it's a concrete self-check habit when reading rules: *"what's
  implicit here — cadence? threshold? audience?"* Analogous to writing
  standard 8.3's "what doesn't the doc specify?"

- **The load-bearing Pass 1 finding (principle #2 reframe) was already in
  last session's State at Close.** Explicitly flagged as a Phase 2
  consideration. Reading it at session start, carrying it through, and
  implementing it as the session's biggest finding is evidence the
  close → startup → close loop works as designed when specific
  decisions-awaiting-implementation items are named precisely.

### Human experience

- **User caught two calibrations I missed, consistent with a pattern.**
  Tagging cadence + (indirectly) scope. Last session's debrief predicted
  the recurrence; the friction log is accumulating real evidence for the
  calibration issue. Proactive practice forward: before committing to a
  narrow interpretation, explicitly check the broader one.

- **Session pacing felt right.** Explicit check-ins at Pass 1 → Pass 2
  boundary and at wrap-up created decision points where the user could
  have pulled back. Redundant in outcome (they said "continue"); valuable
  in form. Worth preserving — explicit decision points prevent runaway
  momentum.

### Drift worth noting

- **Pass 2 finding #6 (export calibration) drifted from plan to
  implementation.** Findings said "defer until an artifact exists"; I
  then implemented a lightweight inline calibration check. Right call,
  but the change from presented plan to landed implementation wasn't
  surfaced for review. Next time: if the plan changes during
  implementation, name it.

- **Didn't `/session-checkpoint` between Pass 1 and Pass 2.** Standards
  fluency went stale in working memory; Pass 2 reasoned from memory +
  recent greps rather than a fresh standards read. Outcome was fine; the
  practice could be tighter. The checkpoint-timing insight applies here:
  before reasoning from files read long ago, not after producing output
  from recent conversation.

### Self-assessment on effort

Honest read: load-bearing changes worth it, polish marginal, aggregate
modestly worth the time.

- **Real value:** dual-maintain fix (compounding ergonomic win),
  principle #2 reframe (gradient effect), export calibration check and
  think broadening (close real gaps), CLAUDE-intent harmonization
  (keeps downstream generation consistent).
- **Marginal value:** CLAUDE.md maintenance-mode sentence, validate.md
  note cleanup, startup.md "After Loading", validate-architecture.md
  cadence. Each a small sharpening; collectively maybe 5% behavioral
  improvement, optimistically.
- **Unexpected value:** (1) validation that the framework IS
  well-written against its own standards — Phase 3 can proceed with
  confidence that standards integration into `/validate` won't reveal
  widespread gaps. (2) The tagging friction entry — emerged mid-session,
  not from the review work; probably the session's highest per-minute
  ROI.

**If I'd make the call again:** dual-maintain + principle #2 reframe +
CLAUDE-intent harmonization + think broadening + export calibration. Defer
the five minor sharpenings to friction log entries for a future natural
`/maintain` session. That would cut ~45 min for ~80% of the value. Scope
more tightly next time a standards review session runs.

## State at Close

### Context for next time

- **Framework at v0.0.5** after this session's tag + push. Four commits
  above v0.0.4, all from this session: dual-maintain fix, shippability
  tagging friction entry, Pass 1 refinements (7 fixes), Pass 2
  refinement (1 harmonization). Tag at HEAD per the session-end tagging
  cadence established mid-session (no intermediate tags).
- **Writing Standards Phase 2 complete.** Both passes done. Framework
  is consistently well-written against its own standards — Pass 1 found
  seven fixes (one high-priority, six small); Pass 2 found one real
  finding and one subjective one (skipped). No widespread gaps.
- **`/maintain` dual-maintenance burden cleared.** Core skill broadened
  to work in both domain-project and framework contexts; framework
  wrapper shrank to a thin delegate with framework-specific addenda.
  Future universal edits land once.
- **Principle #2 reframe propagated.** `nla-foundations.md` and
  `install/CLAUDE-intent.md` both carry "NLA documents are source code"
  as the canonical phrase. Downstream NLAs may see a small wording
  proposal when they next run `/update` to re-synthesize their
  CLAUDE.md.
- **Shippability tagging cadence pattern captured as pending friction.**
  Rule-vs-intent reading issue (see Debrief). The entry proposes
  separating what-to-tag (consumer-facing content) from when-to-tag
  (session-end / meaningful release moments). Future `/maintain` to
  refine the shippability convention text in `core/skills/maintain.md`
  and `install/package-intent.md`.

### Decisions awaiting implementation

- **Phase 3 of #21: deeper standards integration.** `/validate` mode or
  diagnostic check that applies the standards; richer `/maintain`
  writing guidance. Phase 2's findings suggest 2.3 (produces what it
  contains) and 4.4 (cross-references with context) are the most
  automate-able as diagnostic hooks — 2.3 for behavioral gaps,
  4.4 for discrete pattern-matching. 2.4, 4.2, 3.5 are more holistic and
  harder to automate. 8.3 (operative docs) is already validated across
  both passes. 5.1 (document lifecycle type) wasn't reviewed against and
  is relevant to document-type-specific guidance.
- **Shippability convention refinement (2026-04-18 friction entry).**
  Separate what-to-include (consumer-facing content) from when-to-tag
  (meaningful release moments). Short edit to
  `core/skills/maintain.md` Shippability section + mirror in
  `install/package-intent.md`. Probably pairs naturally with Phase 3
  (both touch `/maintain` territory).
- **2026-04-16 friction entries** (Python implementation standards,
  Fallingwater-style prose preamble, `/maintain` prose-vs-code mode,
  re-compile `export.py` through nla-compiler) — all still pending. Pair
  thematically with Phase 3. Best addressed after Phase 3 produces
  concrete findings, in whatever sequence makes sense then.
- **Other older friction entries** (2026-03-08 /startup flag,
  2026-02-23 /create-app bare project path, 2026-02-23 friction-logs
  gitignored, 2026-02-22 context window awareness) — all still pending
  from before this session. Unchanged.
- **Packages migration propagation** (penny-post, process-helpers, then
  domain projects) — still pending from 2026-04-15. Unchanged.

### Where to pick up

**Immediate candidates:**
- **Shippability convention refinement.** Quick, high-clarity win. Fits
  any future session; doesn't require fresh standards context.
- **Phase 3 planning.** Judgment work — /think session-worth. Best with
  fresh context; this session's Phase 2 findings inform scope.

**Medium-term:**
- The 2026-04-16 entries as a cluster after Phase 3.

**Watch:**
- Whether the start-narrow reflex shows up again in a third session. If
  it does, the pattern earns operative treatment (not just a note in
  debriefs).
