# Maintenance Session: Session-Bracketing Rhythm + Handoff Template

**Date:** 2026-05-22
**Status:** Complete

## Intent

Execute the warm-context plan at
`reference/plans/session-bracketing-rhythm-and-handoff-template.md`
(drafted 2026-05-19, cold-context reviewed 2026-05-19, marked
ready-for-execution). Land three feedback log items from the 2026-05-18
facebook-moderation triage as one coherent execution unit:

1. The Session-Bracketing Discipline as the framework's eighth Working
   Rhythm
2. Plan/handoff document template at `core/plan-handoff-template.md`
3. Plans-not-runbooks preventive framing (inline in the rhythm)

The three items form one unit because the rhythm names *when* to draft a
plan; the template names *what* a plan contains; the preventive note
keeps framing consistent (the cardinal rule depends on it).

## Changes Made

- **`core/nla-foundations.md`** — added The Session-Bracketing Discipline
  as the eighth Working Rhythm, placed as #5 between Session Structure
  and Structural Change Discipline. Cycle: do-work → plan-while-hot →
  simulate-cold → cold-question-check → adjust → close-and-clear. Three
  paragraphs covering cycle + substep meanings, two-mechanism distinction
  (simulation vs. question gap-classes), and rhythm framing (plans-not-runbooks,
  "someone drives" default, when-it-fires, template reference). Design
  Flow gains a one-sentence tail cross-reference to the new rhythm
  (Option C hybrid framing).

- **`core/plan-handoff-template.md`** (new) — standalone template doc.
  Six sections (Title+Intent, Substance, Procedural-edge cases, Judgment
  defaults, Confidence band, Warm-context next-steps with three sub-parts)
  plus block-end checkpoints. Scaffolds without enforcing; section-dropping
  guidance included. ~70 lines.

- **`core/structure.md`** — added the new file as an entry in the
  `core/` table and the Decision Sources scan view, per the Structural
  Change Discipline (recording-coupled-to-change in the same operation).

- **`reference/design-rationale.md`** — added "Session-Bracketing
  Discipline" entry capturing the framing alternatives (Options 0/A/B/C),
  template location alternatives (Options A/B/C), two-mechanism
  distinction with empirical validation pointer, plans-not-runbooks
  framing, "someone drives" default, placement-in-list reasoning, and
  blast radius.

- **`install/update-notes.md`** — added 2026-05-22 entry for downstream
  NLA consumers, naming the new rhythm, the new template file, and the
  plans-not-runbooks framing. Cross-references prior Inquiry Flow entries
  (2026-05-14 and 2026-05-18). Names that no project-side action is needed.

- **`reference/feedback-log.md` / `feedback-log-archive.md`** — archived
  three resolved feedback log entries (session-bracketing rhythm,
  plan/handoff template, plans-not-runbooks preventive guidance) with
  `**Resolved:** 2026-05-22 — ...` lines. Active log retains the two
  accept-with-/think entries (/close enhancement, memory-mining beat).

- **GitHub follow-up comments** posted on Issues #24 and #25 naming
  what landed and what remains pending.

## Decisions Made

- **Framing: Option C (hybrid)** — standalone eighth rhythm + one-sentence
  cross-reference from Design Flow's debrief beat. The user landed here
  after the AI presented Options 0/A/B/C; Option C preserves substep
  visibility (against Option A's folding) and discoverability (against
  Option B's isolation).
- **Placement: #5 (after Session Structure, before Structural Change
  Discipline)** — chosen for the dual pairing argument (session-lifecycle
  pair #4/#5 within/across; discipline pair #5/#6 both conditional
  propose/record rhythms). The user pushed back on the AI's initial
  "thin margin" framing by observing that the reader is an AI loading the
  full file into context at once — which collapses the
  progressive-disclosure argument for #8 and strengthens the pairing
  argument for #5.
- **Name: "The Session-Bracketing Discipline"** — parallels Structural
  Change Discipline in shape and naming. Alternative "The Bracketing
  Rhythm" considered (shorter, loses the discipline parallel).
- **Template location: Option A (standalone at
  `core/plan-handoff-template.md`)** — chosen over Option B (inside
  `core/skills/close.md`, conflates where-it-lives with where-it's-used)
  and Option C (inside the rhythm, balloons foundations.md). The template
  is referenced from multiple places (rhythm now, eventual /close
  enhancement) and warrants its own file.
- **Design-rationale entry written** — modeled on the "Structure
  Decisions Protocol" entry (the closest precedent for a discipline
  rhythm). Inquiry Flow and Validation Flow apparently don't have
  separate entries, but the bracketing rhythm has substantial alternatives
  considered worth recording.

## What Didn't Work

Nothing substantive. The plan was well-drafted and cold-reviewed, so
execution was largely mechanical translation of plan-side decisions into
prose + structural updates. One small process note: during Step 1, the
AI initially reached for `AskUserQuestion` enum-style tool for the
framing/placement/naming three-question bundle. The user interrupted
before the questions rendered. Reverted to prose-style proposal, which
matched the existing feedback memory "Prose over enum for decisions."

## Friction Log Entries Processed

None directly resolved. The 2026-05-20 friction entries (Accept-with-/think
verdict prominence; two-mechanism empirical validation) are pending and
remain in the active friction log:

- The two-mechanism entry was cited in the design-rationale entry and the
  rhythm prose, exactly as the State at Close for the prior session
  anticipated.
- The Accept-with-/think prominence entry remains pending — it's a small
  fix to `packages/nla-penny-post/app/check-feedback.md` that can ride
  along with any upcoming penny-post work.

## Debrief

(To be captured at session close via `/close`, or as brief observations
here if no explicit debrief happens.)

**Brief observations from execution:**

1. **The plan was load-bearing.** The plan's cold-context review section
   (simulation findings + question findings + patches applied) had already
   resolved most ambiguities. Execution mostly translated plan-side
   decisions into prose. This validates the plan-while-hot →
   simulate-cold → cold-question-check workflow that the rhythm itself
   names — the plan's quality reduced execution-session friction
   substantially.

2. **AskUserQuestion reach was a near-miss.** The AI started to call
   AskUserQuestion for the framing/placement/naming bundle. User
   interrupted; AI reverted to prose. The relevant memory exists
   ("Prose over enum for decisions"); the reach happened anyway in the
   first multi-decision moment of the session. Worth noting for future
   sessions — the memory's pull weakens in flow.

3. **The "reader is an AI" observation reframed the placement question.**
   The user's observation that the reader is an AI loading the file
   wholesale (not a human reading sequentially) collapsed one of the
   competing arguments and crystallized the decision. Worth remembering:
   when applying writing standards developed in human-reader mental
   models, ask "what's the actual reader?"

## State at Close

**What's working:**

- All eight steps of the warm-context plan executed cleanly. Three feedback
  log items resolved and archived. Two GitHub follow-up comments posted.
  One design-rationale entry added. Update-notes entry written. Structure
  record updated in the same operation as the new file creation (per
  Structural Change Discipline).
- The framework now has named vocabulary for cross-session work — the
  rhythm, the template, the plans-not-runbooks framing, the two-mechanism
  distinction. The naming propagates to every NLA at next `/update`.

**What's pending:**

Two accept-with-/think feedback log entries (both 2026-05-18) remain in
the active log:

- /close enhancement: plan-shaped artifact detection + handoff integration
- Memory-mining beat in lifecycle

Both need a /think session before they can be specified for execution.
Either can be picked up independently.

The friction log retains eight pending entries (none touched this
session). The 2026-05-20 "Accept-with-/think" verdict prominence entry
is a small check-feedback skill fix awaiting penny-post work.

**Commits this session (one expected):**

- One commit covering: nla-foundations.md + plan-handoff-template.md +
  structure.md + design-rationale.md + update-notes.md + feedback-log
  archival + this session log + VERSION bump. Per shippability rule,
  consumer-facing content (core/, install/) → tag at push. Tag scope:
  v0.0.11.

**Where to pick up:**

The natural next session is either of the two accept-with-/think items.
Both need a /think session. The /close enhancement is the higher-leverage
one (it touches the most-frequently-run skill and closes the workflow
loop the bracketing rhythm names). The memory-mining beat is the more
exploratory one (lifecycle integration question with several options).
