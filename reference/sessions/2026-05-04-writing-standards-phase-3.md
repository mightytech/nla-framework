# Maintenance Session: Writing Standards Phase 3

**Date:** 2026-05-04
**Status:** In Progress

## Intent

Bring the NLA writing standards into active use through two complementary
integrations: author-time use during `/maintain` editing, and on-demand
retrospective review through a new `/validate standards` mode. Phase 1
(2026-04-17) brought the standards file into the framework with a
lightweight pointer in `/maintain`. Phase 2 (2026-04-18) ran two manual
review passes that empirically validated the standards' diagnostic value.
Phase 3 operationalizes that diagnostic value: author-time so docs land
right the first time, retrospective so existing docs (much of which
predate the standards) can be reviewed against them on demand and again
as the standards evolve.

## Approach

The /think exploration converged on a two-piece shape with an explicit
iteration posture:

**Author-time integration in `/maintain`:** Targeted-load — when editing
operative docs, identify the doc type, read section 2 (document
fundamentals) plus the matching 8.x subsection. Doc-type-aware loading
avoids burning context on every edit while keeping the high-leverage
standards in the room. Starting with targeted rather than always-load is
the lighter starting position; if the targeted approach keeps missing,
`/validate standards` catches the gaps and signals when to escalate.

**New `/validate standards` mode:** Retrospective review modeled on
Phase 2's flow. Scope-configurable — user picks docs and standards
subset. Defaults focus on 2.3 (produces what it contains) and 4.4
(cross-references with context), Phase 2's empirically most-diagnostic
standards. Output is a findings file in `reference/sessions/`, matching
`validate-architecture.md`'s pattern, then routed through `/validate`'s
existing disposition step (fix-now / defer to friction log / wont-fix).

## Decisions Made

- **Three modes collapsed to two.** Initial framing distinguished
  prospective (before drafting) / current (during drafting) /
  retrospective (after drafting). Conversation collapsed prospective and
  current to **author-time** — the value is standards in the room while
  writing, not a pre-edit reading ritual. Two modes that matter:
  author-time and retrospective. — Rationale: prospective awareness
  without operational use is hollow; current is what produces the value.

- **`/validate standards` over `/validate writing` or enhancing
  `/validate debug`.** Debug is reactive to a specific observed bug;
  standards review is proactive against the standards. Different
  diagnostic question. "Standards" is more accurate than "writing"
  (which suggests grammar/style). — Rationale: name should match the
  diagnostic question.

- **Targeted-load over always-load for /maintain.** When editing
  operative docs, read section 2 + the matching 8.x subsection rather
  than the full 738-line standards file. — Rationale: targeted is the
  lighter starting position; always-load is the conservative fallback if
  the targeted approach keeps missing. The /validate standards mode
  catches gaps and provides the escalation signal.

- **Default standards subset for /validate standards: 2.3 + 4.4.**
  Phase 2's empirical findings: 2.3 surfaced most behavioral gaps; 4.4
  is the most discrete, gremmable pattern. — Rationale: defaults should
  reflect what produced findings.

- **New mode is a sub-mode of /validate, not a top-level skill.**
  Follows the existing validate-* pattern (architecture, coherence,
  debug, scenario, structural). No separate framework wrapper needed. —
  Rationale: matches established structure; lower surface area.

## What Didn't Work

- **Initial "enhance /validate debug" suggestion.** Was offered as a
  quick side-quest but the user rejected it — debug is reactive to a
  specific observed problem, not standards-conformance review. Right
  pushback; revealed the diagnostic-question distinction.

## Friction Log Entries Processed

None directly. This session is processing the Phase 3 portion of feedback
log entry "2026-04-15 — Bring NLA writing standards into the framework."

## Debrief

(To be added at session close.)

## State at Close

(To be added at session close.)
