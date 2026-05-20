# Maintenance Session: Inquiry Flow + Principle #2 Recalibration

**Date:** 2026-05-14 (spanned to 2026-05-20)
**Status:** Complete

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

---

## Fourth workstream: Warm-context plan for session-bracketing rhythm + handoff template (2026-05-19)

After the third workstream completed, the maintainer asked the AI to honestly assess context state and recommend whether to (a) implement the next pending items now or (b) draft a warm-context plan. Honest read: context heavily loaded; the headline pending item (session-bracketing rhythm) carries an unresolved framing question that benefits from fresh eyes in cold context. Chose option (b) — dogfood the very pattern we just triaged.

### Intent (fourth workstream)

Apply the session-bracketing pattern to the work we just triaged. Draft a plan-shaped artifact for the rhythm + template + preventive-note implementation, using:

- The four-section template from Letter #24 (substance, procedural-edge, judgment defaults, confidence band)
- The two structural patterns from Letter #25 (warm-context next-steps section, paired specific+generic checkpoint questions)
- Intent at every layer (Letter #24 item 5)

The plan demonstrates the patterns before they're documented — establishing that they work in practice in this exact use case, while capturing the warm-context judgment for a fresh-context execution session.

### Changes Made (fourth workstream)

- **`reference/plans/session-bracketing-rhythm-and-handoff-template.md`** — new plan file. Topic-based filename matching the existing `skills-doctrine-publication.md` convention. Covers: what this is, what it adds, why it exists, pre-requisites, goals/non-goals, 8 substantive steps, block-end checkpoints, procedural edge-cases, judgment defaults, confidence band, warm-context next-steps, to-do at session close.

### Decisions Made (fourth workstream)

- **Plan as separate file, not embedded in session log** — cold-context review benefits from a focused artifact; embedding would dilute the cold agent's prompt with retrospective narrative they don't need. The four-section template's self-containment discipline depends on the plan standing on its own.

- **No new directory needed** — `reference/plans/` already exists (added 2026-05-06 via the skill-invocation discipline publication plan; documented in `core/structure.md` lines 54, 155, 250). The structural change discipline check surfaced this in time to avoid unnecessary structure-record overhead.

- **Filename topic-based, not date-based** — matches the existing plan's convention. Date captured in the "Drafted" field at the top of the file.

- **Three-item bundle scope** — session-bracketing rhythm + plan/handoff template + plans-not-runbooks preventive note as one execution unit. /close enhancement and memory-mining beat both excluded as out-of-scope (both need /think sessions before they can be specified at plan level).

- **Open framing question explicitly preserved, not pre-decided** — Step 1 names Options A (extend Design Flow), B (standalone rhythm), and C (hybrid) with author's lean (C, hybrid) but invites fresh-context AI to argue otherwise. This is the precise move The Inquiry Flow describes: warm-context judgment as input, fresh eyes as verification.

- **Confidence band populated honestly with percentages** — for each contestable decision, the band names how confident the warm-context author actually is (60% on framing, 55% on template location, etc.). Aligns with Letter #24 item 3c's framing: "where the cold executor should expect to push back."

- **No cold-context review run yet** — the plan prescribes simulation + question review as session-close steps. To be run separately (either in this session before commit, or at next /close).

### Feedback Items Processed (fourth workstream)

- None resolved. The three relevant pending entries (session-bracketing rhythm; plan/handoff document template; plans-not-runbooks preventive guidance) remain pending in the active feedback log. The plan captures *how* to resolve them; the actual resolution happens in the execution session.

---

## Fifth workstream: Cold-context review of the warm-context plan (2026-05-19)

Honored the plan's prescription — ran both cold-context check mechanisms (Letter #24 item 2) on the plan drafted in workstream 4. Dogfooded the patterns end-to-end while warm context was still available for patching.

### Intent (fifth workstream)

Complete the close-and-clear substep of the session-bracketing rhythm on the plan we just drafted. Specifically: spawn fresh-context reviewer agents (separate simulation and question), triage their findings against the plan, apply clear-improvement patches under Adjust's verify-each-claim discipline. Demonstrate the cycle that the plan documents as a workflow.

### Changes Made (fifth workstream)

- **Cold-context simulation review** — fresh `general-purpose` subagent (~46s, ~30k tokens). Found self-containment positive (didn't need to open referenced files for executability); surfaced ambiguities at Pre-req #3 reading twice with To-do #1-2; Step 4 redundancy with Step 2's content list; Step 1 framing-question current-state confusion.

- **Cold-context question review** — separate fresh `general-purpose` subagent (~59s, ~29k tokens). Surfaced conflations (Plan vs. Handoff treated as one; "cold-context" used for two distinct roles), pre-judged framings (new-rhythm existence; "someone drives" defaulting to human), unsupported leans (standalone-template-doc rationale relies on speculative future referents; placement-justification circular), implicit context dependencies (letter content referenced by number).

- **Patches applied** to `reference/plans/session-bracketing-rhythm-and-handoff-template.md`:
  - **A.** Plan vs. Handoff distinction clarified in Step 3 (template is handoff-shaped; plans that don't cross agent boundaries may carry a subset)
  - **B.** "Cold-context" role disambiguation — Step 2 substeps now distinguish reviewer (pre-execution diagnostic) from executor (post-handoff implementer)
  - **C.** Option 0 added to Step 1 (amend existing rhythms; no new rhythm) as a real fourth option
  - **D.** Letter content inlining clarified — note at top of Substance section
  - **E.** Pre-req / To-do reconciliation paragraph
  - **F.** Step 4 retitled and reframed as explicit verification beat
  - **H.** "Someone drives" framing acknowledged as open question, not settled default
  - **Plus:** Status field updated to "Cold-context review complete; ready for execution"; "Cold-context review" section appended with findings + patches applied + patches not applied + rationale

### Decisions Made (fifth workstream)

- **Two parallel reviewers, not one combined** — Letter #24 item 2 framed the mechanisms as catching different gap-classes; running them as separate fresh agents preserved independence (one didn't influence the other's frame). Output partly overlapped (Step 1 framing state, "cold-context" usage) and partly diverged (simulation found Pre-req #3 / Step 4 / framing-state confusion; question found conflations and pre-judgments). Different findings, both real — independent-agent-convergence-as-validation (Letter #24 item 7) at work.

- **Apply-not-discuss the pre-approved patch set** — the maintainer reviewed and approved A+C+D+E+F+B+H plus review-summary section before patching. Execution was mechanical from there; no per-patch re-litigation. This was right: the verify-each-claim discipline happened during proposal, not during application.

- **Some findings deliberately not patched** — I (template-doc rationale honesty) is already acknowledged in Confidence band at 55%; J (length) is covered by an existing edge case; G (status field semantics) is answerable at execution time; K (shippability rule pointer) lives in maintain.md where the cold executor finds it. The placement-circularity finding is acknowledged in the review summary but not patched in-line because it's a small honest acknowledgment, not a pre-execution gap.

- **Plan vs. Handoff distinction surfaced but not fully resolved** — Patch A clarified the template is handoff-shaped, but the deeper question (whether the rhythm itself should be called "Handoff" rather than "Plan" or "Session-Bracketing") remained open. Surfaced in the Step 3 naming clarification rather than pre-decided. The execution session resolves at template-doc-naming time.

- **Confab-resistance worked in real time** — reviewer findings were treated as hypotheses, each verified against the actual plan content before patching. Two findings (the question agent's claim that letter content wasn't inlined; the simulation agent's worry about "letter references") turned out to be partly inaccurate on verification — the content IS inlined; the references are attribution-laden but not execution-blocking. Adjusted Patch D accordingly (kept attributions; added clarifying note about traceability vs. prerequisite).

### Feedback Items Processed (fifth workstream)

- None. The plan was already drafted in workstream 4; the cold-context review completes the close-and-clear substep. Resolution of the three pending feedback-log entries (rhythm, template, runbook-preventive) still belongs to the execution session.

---

## Debrief

Refined observations from this session's explicit `/debrief`:

- **"Ask the AI about its experience" reframe grew the right way.** The session started with a small note about principle #2's tone reading too negatively about AI narrative. It grew into the recalibration *and* The Inquiry Flow rhythm *and* the feedback triage that surfaced the warm-context plan we dogfooded. The maintainer's willingness to let scope grow appropriately — rather than force-fitting into the original principle-tweak framing — was load-bearing. This methodological openness is worth recognizing as a positive pattern, distinct from "scope creep" because the growth was always followed by re-confirmation of direction before proceeding.

- **Confab-resistance worked in real time.** Two reviewer findings (one from the question agent claiming letter content wasn't sufficiently inlined; one from the simulation agent flagging "letter references" as execution dependency) turned out to be partly inaccurate when verified against the actual plan. The Inquiry Flow's "candidates, not authority" discipline caught them — concrete in-session evidence that the rhythm operates as intended. Positive observation worth recording as a session-log debrief note for future reference; no separate friction entry needed since the rhythm itself is the artifact.

- **Two-mechanism cold-context check empirically validated.** Letter #24 item 2's framing (simulation catches execution gaps; question catches conceptual-frame gaps; the two reach different gap-classes) played out exactly. The question reviewer surfaced the Plan vs. Handoff conflation and the "cold-context" two-roles issue that the simulation reviewer didn't see. Captured as friction log positive observation (2026-05-20) for use during the execution session's rhythm-drafting.

- **Accept-with-/think verdict shape needs more prominence in check-feedback.** Initially labeled two structurally-identical items "Adapt" and "Defer." The maintainer caught it; reconciled. Captured as friction log entry (2026-05-20) for check-feedback skill enhancement. The skill's current treatment of the hybrid case is a parenthetical; it needs to be visible at decision time.

- **Asking sharpens AI thinking, not just user input.** The maintainer's observation: "just because I'm asked doesn't mean I'm confident I'll come up with a better answer than you. But one thing I do suspect: your asking can help *you* arrive at better answers too." Captured as feedback memory. The asking is dual-purpose — surfaces options for the user AND clarifies the AI's own reasoning even before the response arrives. The two purposes reinforce each other; neither is the primary.

- **Autonomy calibration was right.** Tooling decisions (commit shape, hunking trade-offs) delegated; design decisions (verdict taxonomy, prose-default placement, plan-vs-handoff distinction) held by maintainer. Explicit confirmation: "Yes [autonomy felt right]. You asked, which was exactly right. I want to be asked." The asking-as-default operationalizes the Cardinal Rule at the level of surface area, not just authority — the human decides not because they always have a better answer but because they bear the consequences and benefit from staying engaged.

- **Session log's layer-don't-flatten pattern carried five workstreams cleanly.** No restructuring needed; each workstream added as a section. The pattern from 2026-05-11 validated further. Positive observation, doesn't need to land anywhere durable beyond this log.

## State at Close

**What's working:**

- `core/nla-foundations.md` principle #2 recalibrated (2026-05-14); The Inquiry Flow rhythm added and refined with the agent self-report anchor (2026-05-14 and 2026-05-18); The Validation Flow vocabulary extended with "independent-agent convergence" (2026-05-18). Two update-notes entries written for downstream propagation.
- Two GitHub Issues triaged and closed (#24 and #25); #24 carries an implementation follow-up comment.
- One feedback log entry resolved and archived (agent self-report verification as Inquiry Flow anchor); five pending entries from the 2026-05-18 triage.
- Two new friction log entries (2026-05-20): the "accept-with-/think" verdict shape (pending check-feedback skill enhancement); the two-mechanism cold-context check empirical validation (positive observation for use during rhythm execution).
- One new feedback memory: "Asking sharpens AI thinking."
- Warm-context plan drafted (`reference/plans/session-bracketing-rhythm-and-handoff-template.md`) with cold-context review complete; status "ready for execution."

**What's pending:**

Five feedback log entries from the 2026-05-18 triage, plus the new friction log entries:

- Session-bracketing as a new Working Rhythm (Issue #24 items 1, 2, 8 + rec F) — covered by the warm-context plan
- Plan/handoff document template (Issue #24 items 3, 5 + rec B; Issue #25 items 1, 2) — covered by the warm-context plan
- Plans-not-runbooks preventive guidance (Issue #24 item 4 + rec C) — covered by the warm-context plan
- /close enhancement: plan-shaped detection + handoff integration (Issue #24 recs A, E) — accept-with-/think
- Memory-mining beat in lifecycle (Issue #25 item 3) — accept-with-/think
- Accept-with-/think verdict shape prominence (2026-05-20 friction entry) — small check-feedback skill enhancement
- Two-mechanism empirical validation (2026-05-20 friction entry) — positive observation; informs rhythm prose at execution time

**Where to pick up:**

The natural next session executes the warm-context plan at `reference/plans/session-bracketing-rhythm-and-handoff-template.md`. The plan is self-contained and cold-context-reviewed; a fresh-context AI can run it after re-reading the existing Working Rhythms section in `core/nla-foundations.md`.

Alternative natural next steps:

- The two accept-with-/think entries (`/close` enhancement, memory-mining beat) each need a dedicated `/think` session before they can be specified for execution. Either can be picked up independently of the rhythm work.
- The accept-with-/think check-feedback skill enhancement (small fix) could ride along with any upcoming penny-post work.
- The 2026-05-20 two-mechanism positive observation should be referenced when the execution session drafts the rhythm's "two cold-context check mechanisms" beat.

**Commits this session (three):**

- `a57d225` — foundations: principle #2 recalibration + Inquiry Flow rhythm (consumer-facing; tag at push)
- `9461931` — feedback triage: facebook-moderation letters #24 + #25 (internal)
- `360eada` — plan + cold-context review: session-bracketing rhythm and handoff template (internal)

Plus the close-time commit covering the friction log entries, the feedback memory, and this session log's Debrief + State at Close + Status update.
