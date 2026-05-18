# Maintenance Session: Inquiry Flow + Principle #2 Recalibration

**Date:** 2026-05-14
**Status:** In Progress

## Intent

Two coupled changes to `core/nla-foundations.md`:

1. **Recalibrate principle #2's third paragraph** from "AI narrative is noise to discard" to "useful input, must be verified." The original framing read as reflexively skeptical — true for raw diagnosis but it discards the AI's account's productive use as hypothesis. The recalibration preserves "hypothesis, not evidence" and the confabulation warning, but reframes both sides (discarding loses signal; accepting substitutes story).

2. **Add a new Working Rhythm — The Inquiry Flow** — that operationalizes the recalibrated principle. Names a rhythm humans and AI are already doing implicitly (debrief, friction log diagnosis, post-execution reflection in `/think`, the artistry conversation in facebook-moderation's compile experiments) and gives it a verification structure that routes through three modes (human smell test, warm/cold-context AI reading artifacts, empirical experiment) all ending at human decision.

Plus a small ripple: soften the Improvement Loop's "diagnose from the artifacts, not from the AI's narrative" line to match the new principle's both-sides framing.

The user's framing of the rhythm matters: most humans pick one of two priors — AI is unreliable (don't listen) or AI is reliable (just automate). The recalibration plants a third: AI is signal, signal must be verified. Operationalized for AI via the rhythm's cycle structure with embedded confab guards as anchor examples (not exhaustive list, per intent-over-rules).

## Changes Made

- **`core/nla-foundations.md` principle #2 paragraph 3** — recalibrated to "useful input — but hypothesis, not evidence." Preserves the confabulation warning ("not bad faith, just the shape of how LLMs report on themselves") to depathologize without softening. Adds the symmetric second half: discarding loses signal, accepting uncritically substitutes story.
- **`core/nla-foundations.md` Working Rhythms** — added The Inquiry Flow between Structural Change Discipline and The Validation Flow. Cycle shape parallels other rhythms. Two anchor examples for confab-resistance (allow "I don't know"; ask before revealing your read) rather than exhaustive list. Three verification modes all routing to human (Cardinal Rule).
- **`core/nla-foundations.md` Improvement Loop** — softened the "diagnose from artifacts, not from AI narrative" line to match the new principle's framing.
- **`install/update-notes.md`** — entry naming the recalibration and new rhythm for downstream projects.

## Decisions Made

- **Confab guards as anchor examples, not enumerated list** — the framework's intent-over-rules principle (#4) and the user's prior memory on criteria design both argue for intent-shaped guidance with concrete anchors over exhaustive technique lists. The LLM has training-data instincts about what produces confabulation; the intent fires that knowledge. Two anchors keep the rhythm short and avoid pattern-matching to "did I do the checklist."

- **Three verification modes all route to human** — the user explicitly identified this as the right structure. Smell test (human eval), warm-context AI eval, cold-context experiment all end at the human's decision. The three aren't parallel paths; they're tools the human pulls down depending on stakes. Connects the rhythm to the Cardinal Rule (principle #6).

- **Inquiry Flow as Validation Flow's hypothesis-generator** — placed Inquiry right before Validation in the doc. Inquiry generates hypotheses; Validation tests them. Reading order matches the dependency. The two are complementary rhythms, not redundant.

- **Single-channel coverage sufficient** — unlike the prose-default work from the last session, this principle lives in `core/nla-foundations.md` which is read by both framework and domain projects through the packages submodule. No dual-channel issue; single edit covers both.

- **Ripple to Improvement Loop softened, not left as-is** — both options were defensible (the cross-reference still resolved correctly even without the touch), but softening keeps the doc internally coherent on the both-sides framing.

## Friction Log Entries Processed

- None directly. This work was driven by user observation about the foundations document's tone, not a logged friction entry. The pattern of "AI experience as productive input" was visible in the facebook-moderation `ingest-compile-compare` experiment report (Section 6, the artistry conversation; Finding 12, post-evaluation reflection on avoidance) but had not been separately logged in the framework's friction log.

---

## Second workstream: Feedback triage (2026-05-18)

After the Inquiry Flow work landed, the maintainer mentioned a downstream NLA had implemented a workflow extension ("Think → plan → implement → debrief → plan next session if necessary") and pointed at a likely-relevant letter from facebook-moderation. Ran `/check-feedback`.

### Intent (second workstream)

Triage accumulated facebook-moderation feedback (two letters: Issue #24 on handoffs and cold-context execution, Issue #25 on plan-template patterns and memory-mining). Determine what's actionable now, what needs /think, and how items connect to the just-added Inquiry Flow.

### Changes Made (second workstream)

- **`reference/feedback-log.md`** — deposited six accepted entries covering both letters:
  1. Session-bracketing as a new Working Rhythm (Letter #24 items 1, 2, 8 + rec F)
  2. Plan/handoff document template (Letter #24 items 3, 5 + rec B; Letter #25 items 1, 2 bundled in)
  3. /close enhancement: plan-shaped detection + handoff integration (Letter #24 recs A, E — accept-with-/think)
  4. Plans-not-runbooks preventive guidance (Letter #24 item 4 + rec C — adapted: audit already clean)
  5. Agent self-report verification as Inquiry Flow anchor (Letter #24 items 6, 7 + rec D — flagged as in-session quick-win candidate)
  6. Memory-mining beat in lifecycle (Letter #25 item 3 — accept-with-/think)
- **GitHub Issue #24** — triage summary comment posted; issue closed.
- **GitHub Issue #25** — triage summary comment posted; issue closed.

### Decisions Made (second workstream)

- **Accept-with-/think as explicit verdict shape** — the maintainer surfaced the inconsistency in my initial verdicts (Theme 3 "Adapt" vs. Theme 6 "Defer" were structurally the same shape: principle committed, design step prerequisite). Reconciled both to "Accept-with-/think" — the hybrid case the check-feedback skill explicitly allows ("Accept the principle, defer the specific implementation"). Both entries remain pending in the feedback log until the /think session happens; they're not "defer in case it matters later." Worth noting as a triage taxonomy clarification for future use.

- **Bundle Letter #25 items 1 and 2 into the handoff template entry** — Letter #25's warm-context next-steps section is explicitly the structural form that bakes Letter #24's plan-while-hot beat into plan templates. Same pattern at two granularities; one feedback log entry covers both letters' contributions to plan-drafting guidance.

- **Theme 5 (agent self-reports) flagged as in-session quick-win, not yet acted on** — because it's directly continuous with the Inquiry Flow work just landed (anchor example inside the rhythm), the entry notes it's small enough to land in this session if the maintainer wants. Captured in feedback log either way.

- **Plans-not-runbooks audit short-circuited** — context check found no "runbook" framing in framework skills already. Recommendation C's audit ask isn't needed; adapted to "add preventive note so future framework work doesn't drift toward runbook framing."

- **Open framing question on session-bracketing rhythm preserved, not resolved in triage** — the question of "extends Design Flow vs. new working rhythm" is design judgment that belongs at implementation time, not triage time. Captured in the feedback log entry.

### Feedback Items Processed

- **[Issue #24 items 1, 2, 8 + rec F]** — Accepted. Session-bracketing rhythm entry.
- **[Issue #24 items 3, 5 + rec B]** + **[Issue #25 items 1, 2]** — Accepted. Plan/handoff template entry (bundled).
- **[Issue #24 recs A, E]** — Accept-with-/think. /close enhancement entry.
- **[Issue #24 item 4 + rec C]** — Accept (adapted). Plans-not-runbooks preventive guidance entry.
- **[Issue #24 items 6, 7 + rec D]** — Accepted. Agent self-report verification + convergence-as-validation-technique entry.
- **[Issue #25 item 3]** — Accept-with-/think. Memory-mining beat entry.

---

## Third workstream: Inquiry Flow anchor — agent self-report verification (2026-05-18)

Theme 5 from the feedback triage was flagged as an in-session quick-win because it
directly continues the Inquiry Flow work — adding a concrete anchor to the rhythm
just landed, rather than deferring to a separate maintenance session. Maintainer
chose to land it now.

### Intent (third workstream)

Resolve the "Agent self-report verification as Inquiry Flow anchor" feedback log
entry by:

1. Adding a concrete anchor inside The Inquiry Flow naming subagent self-reports as
   a frequent verification target (durations, counts, characterizations).
2. Adding "independent-agent convergence" to The Validation Flow's technique
   vocabulary list.

The Inquiry Flow rhythm was added in workstream 1 with two general anchor examples
(allow "I don't know" as a valid answer; ask before revealing your read). This
workstream adds an operational example on the verification side — what to do when
the AI is the *reporter* and the orchestrator is the *relayer*.

### Changes Made (third workstream)

- **`core/nla-foundations.md` The Inquiry Flow** — added a concrete anchor at the
  end of paragraph 1: subagent self-reports as a frequent verification target;
  orchestrator has task metadata (`duration_ms`) and source artifacts available;
  quoting without checking is a confabulation pass-through.
- **`core/nla-foundations.md` The Validation Flow** — added "independent-agent
  convergence" to the technique vocabulary list.
- **`install/update-notes.md`** — 2026-05-18 entry for downstream propagation.
- **`reference/feedback-log.md`** — Theme 5 entry removed (resolved).
- **`reference/feedback-log-archive.md`** — Theme 5 entry archived with Resolved
  line.

### Decisions Made (third workstream)

- **Anchor woven into paragraph 1, not its own paragraph** — considered making the
  agent-self-report example a standalone paragraph for prominence, but woven-in
  fits the rhythm's existing shape (the two general anchor examples for the asker
  side were also inline). Concrete operational example flows naturally after the
  three verification modes; reads as "and here's a frequent target where this fires."

- **"Confabulation pass-through" as the operational framing** — chose this over
  "be careful with subagent reports." The named failure mode is what's
  diagnostically useful: when the orchestrator quotes a subagent self-report to
  the user without checking, the orchestrator becomes a confabulation conduit. The
  framing turns the rhythm into action by pointing at the specific failure.

- **Validation Flow addition as one-word vocabulary item, not a paragraph** — the
  Validation Flow's vocabulary list is intentionally compact; each item is a
  technique name that gets fleshed out in `reference/experiments/`. Convergence
  fits the same shape. The full description lives in the feedback log entry
  archive and in facebook-moderation's friction log entry 2026-05-03.

### Feedback Items Processed (third workstream)

- **2026-05-18 — Agent self-report verification as Inquiry Flow anchor** — resolved.
  `core/nla-foundations.md` + update-notes + follow-up comment on Issue #24. Archived.

## State at Close

[To fill at /close]
