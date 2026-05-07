# Maintenance Session: Structure Decisions Protocol

**Date:** 2026-05-07
**Status:** In Progress

## Intent

Design a propose-review-record protocol for structural change in NLAs — new
directories, file placements, reorganizations — backed by an attributed
structure-with-reasoning artifact and a consultation pattern. The pattern
borrows facebook-moderation's compile-time build-guide discipline (every entry
attributed to a source or `[judgment]`, non-obvious tradeoffs surfaced as
**Judgment note** callouts, Decision Sources table for scan) and applies it
to NLAs' structural decisions.

The behavioral change: AI pauses and proposes before materially changing
structure (new directory, reorganization, new top-level file), recording the
approved decision in the artifact as part of the change. Future AI sessions
consult the artifact when placing or finding things. Today, those decisions
slip in silently and ad-hoc; future sessions either re-derive or guess.

The framework adopts first as proof and as meta-application of its own
discipline; downstream propagation follows after experimental validation
(per the prior session's "implement on framework, see how it looks/works
with experiments, then push out broadly" methodology).

## Changes Made

*(In progress — to be filled as work lands.)*

## Decisions Made

- **Three-layer shape:** behavioral rule + recording artifact + consultation
  pattern. All three required. Recording is coupled to the change itself
  (single operation, not two) — drift can only enter when structure changes
  happen *outside* the protocol, which becomes a named failure mode rather
  than a general worry.
- **Threshold as intent over rules.** Describe the tension between
  over-gating and under-gating; name attribution as the safety net; let the
  AI judge. Applies framework principle #4 to the protocol's own design.
  Even when the AI judges wrong, the human can see what happened (because
  attribution records what was decided and why).
- **Centralized over distributed.** Single short artifact loaded at startup.
  Distributed per-directory READMEs would require lazy-load discovery the
  AI can't easily do without an index.
- **Operative-channel placement.** Artifact lives where the AI sees it
  during normal work, not just maintenance. Reference channel is invisible
  at runtime. For domain projects: extension to `app/overview.md`. For the
  framework: a new top-level operative file (likely `core/structure.md`),
  since the framework lacks `app/overview.md` by design.
- **Framework-first adoption with experimental validation.** Don't
  wait-and-see; the framework changes too slowly to test in real use before
  propagation. Run controlled experiments (cold-context `claude -p` agents,
  binary filesystem signals, test the production form) before propagating
  to domain projects. Methodology inherited from
  `reference/experiments/skill-invocation-discipline/experiment-report.md`.
- **Two-pass cold-context plan review** before commit, per Section 4.2 of
  the prior experiment report.

## What Didn't Work

*(Empty — too early.)*

## Friction Log Entries Processed

- **New entry added this session:** "Ad-hoc structural decisions lack
  process and record" (2026-05-07). The observation that prompted this
  work didn't yet have a friction log entry; added so the genealogy is
  preserved.

## Debrief

*(At session close.)*

## State at Close

*(At session close.)*
