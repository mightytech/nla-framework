# Maintenance Session: Mechanics-Without-Spirit Fix

**Date:** 2026-05-23
**Status:** Complete

## Intent

Implement Issue #26 Item 1 (mechanics-without-spirit failure pattern) per the Accept-with-/think verdict from the 2026-05-22 triage. The letter's diagnosis: AI reliably reproduces structural mechanics while skipping framing/spirit content; failure condition is "documentation correctness is necessary but not sufficient" — framing transfers reliably only when structurally reinforced. The letter recommended the writing standards as the highest-leverage first target.

The /think session resolved the response shape (writing standards section + /close Step 3 retrofit as coupled work, with /maintain posture preamble deferred and pre-emption hazard split off as separate friction-log entry). This session executed the plan.

## Changes Made

- **`reference/standards/nla-writing.md`** — added Section 2.6 "Make framing operational" after Section 2.5. Names the failure mode, gives the three move-types (reify into operational checks; position framing at top; co-locate framing with mechanics), and provides an author-time check. Authority: Must. Section eats its own dogfood — three move-types bolded at top of Convention (top-placement), author-time check immediately after the moves (co-located), Example reifies the moves into a before/after (operational check). Consumer-facing.

- **`core/skills/close.md`** — retrofitted Step 3 (Debrief). Replaced the conditional "if no /debrief happened and the work was substantive, offer..." with framing-first structure: opens with "The debrief offer is a real choice point — don't pre-judge"; unconditional offer with narrow exception (single trivial edit); rephrased template that doesn't telegraph pre-judgment ("Want to run /debrief..., or should I add brief observations directly?"); added closing paragraph addressing the 2026-05-21 pre-emption-induced malformed-offer instance with wording-level mitigation. Consumer-facing.

- **`reference/friction-log.md`** — added 2026-05-23 entry "Multi-step protocols: pre-emption hazard when earlier work overlaps later choice points." Captures the related-but-distinct failure shape from the 2026-05-21 recurrence comment. Names the /close instance and three latent instances (/maintain, /think, /create-app). Two design directions proposed for broader fix; worth /think when a second instance surfaces. Status: pending. Internal (reference/).

- **`reference/design-rationale.md`** — added "Make Framing Operational: The Spirit-Mechanics Reinforcement Convention" entry. Captures: the decision (section 2.6 + Step 3 retrofit), why this shape and not alternatives (with rejection rationale for /validate mode and deferral rationale for /maintain preamble), the Fallingwater connection (same design pattern in different domains), the two deferral triggers (near-term reassessment, long-term external instance), the procedural reassessment check, the separate pre-emption hazard. Internal (reference/).

## Decisions Made

- **Section 2.6 placement in Section 2 (Document Fundamentals).** Section 2 is in the always-load path for any author-time work per the maintain skill's standards-loading table. Section 2.5 is the LLM-failure-modes-in-general section; 2.6 names a specific failure mode and what to do about it. Natural progression.
- **Authority: Must.** Foundational hazard — every NLA document is a candidate. Same level as 2.1 (the document says what it is), 2.3 (the document produces what it contains), 2.5 (design for the failure modes of the runtime).
- **Section name: "Make framing operational."** Names the move, not the failure. Operational verb form. "Mechanics-without-spirit" was considered but it's too casual for a standards section heading; better as a friction-log-entry shorthand.
- **/close Step 3 retrofit coupled to Section 2.6, not sequential.** The retrofit is a test of whether the section is strong enough to write Step 3 cleanly. If the retrofit had felt forced, the section needed more work. It didn't — section worked.
- **/validate mode rejected.** Wrong level of abstraction. Failure condition is "framing through documentation alone is insufficient." A /validate mode scans documentation; it could catch structural *presence* of framing but not whether framing transfers in execution.
- **/maintain posture preamble deferred with two triggers.** Near-term: end-of-session reassessment via procedural check (done — answer below). Long-term: future non-prose-authoring instance shows mechanics-without-spirit failure.
- **Pre-emption hazard split off.** Distinct failure class (protocol pre-emption ≠ mechanics-vs-framing). Bundling would have produced a fix that tried to address both and addressed neither cleanly. Wording-level mitigation for the specific /close case landed in the Step 3 retrofit; class-level fix is separate work.

## Debrief

**Procedural reassessment of /maintain posture preamble (dogfood check):**

Where in maintain.md does framing currently rely on documentation-alone reinforcement?

Read maintain.md applying Section 2.6 check. Principal posture beat ("You are now the system maintainer") is at top — passes. Maintenance Principles, Pre-flight review, and Shippability sections each lead with framing — pass. Two minor gaps: "Before Starting Work" closes with framing ("The point is to have the conversational beat before formalizing a plan or executing") — framing-at-bottom; some Maintenance Principles have behavioral framing in the second paragraph rather than co-located with the principle header.

**Verdict: no preamble.** Gaps are small enough that surgical edits to those specific paragraphs (applying 2.6 move-types) would address them better than a wholesale Fallingwater-shaped preamble. Long-term external trigger remains.

**Brief observations from the session:**

1. **The section-and-retrofit coupling worked as designed.** The /close Step 3 retrofit was a real test — I had to apply Section 2.6's moves to rewrite Step 3. The retrofit landed cleanly without me reaching back to revise the section. This validates the coupled-design loop. If the retrofit had felt forced, the section would have needed revision; it didn't.

2. **The Fallingwater connection sharpened the work.** Recognizing that the letter's move-types and the Fallingwater preamble are the same design pattern in different domains reframed the response from "pick option a/b/c/d/e" to "where does framing need structural reinforcement?" The reframing came up in /think, and it was the most load-bearing move of the session. Without it, the response probably would have been a single isolated standards section without the dogfood loop or the explicit Fallingwater capture in design-rationale.

3. **Session-bracketing observation refined during debrief.** My initial close-time read was "we missed session-bracketing twice in a row." On debrief, the user pushed back: the Session-Bracketing Discipline specifically fires when a session produces *non-trivial future-session work*, and centers human judgment. Today's session didn't produce future-session work (we completed it in-session), so the rhythm didn't require closing between phases. My initial observation was pattern-matching the *shape* ("we continued through what could have been a bracketing point") without checking the *trigger condition* ("does the trigger condition actually obtain?"). That's the failure mode Section 2.6 names — observed in real time, in the same session where we shipped the fix for it. The genuine smaller concern from long flow-sessions is commit hygiene: ~6 uncommitted file changes accumulated across two work phases meant cleanup-if-something-went-wrong would have been trickier than per-phase commits. Modest in magnitude (nothing went wrong, /close handles it) but real — and it's the actual lever for "commit per-phase if possible at close time" rather than "close between phases."

4. **Meta-recursive realization about the /maintain preamble decision.** The procedural reassessment check ran end-of-session and returned "no preamble." But on debrief, I noticed the check itself was incomplete: I tested for *structural presence* of framing in maintain.md ("is framing at the top? in principle headers? co-located?"), which is a documentation-correctness check. Section 2.6 says documentation correctness is necessary but not sufficient. The right check is "does the framing fire in execution?" — which can only be answered by observing whether 2.6 itself fires in future framework authoring. So the no-preamble verdict holds, but a third trigger should be added: if future framework authoring shows "I knew about 2.6 but didn't apply it" instances (i.e., 2.6's own awareness-level capture isn't sufficient to fire reliably), revisit the preamble decision. That third trigger is the recursive form of the long-term external trigger.

## State at Close

**What's working:**

- All four content artifacts landed: Section 2.6 (standards), /close.md Step 3 retrofit, friction-log entry for pre-emption hazard, design-rationale entry capturing the decision + Fallingwater connection + deferred-preamble rationale.
- The dogfood reassessment check ran cleanly — verdict is no /maintain posture preamble (gaps are surgical-retrofit candidates, not wholesale-preamble candidates).
- One feedback log item resolved (Issue #26 Item 1) — needs to be archived next.

**What's pending:**

- **Possible surgical retrofits on maintain.md:** the two minor gaps from the dogfood check (Before Starting Work closing, some Maintenance Principles paragraphs). Worth a small follow-up session — not bundled here because they're not load-bearing.
- **Third trigger added to /maintain preamble deferral** (per debrief observation #4): if future framework authoring shows "I knew about 2.6 but didn't apply it" instances, revisit the preamble decision. Recursive form of the long-term external trigger.
- **`/validate standards` follow-up:** the standards file evolved (Section 2.6 added). The maintain.md guidance says broader retrospective review (`/validate standards` sweeping multiple docs) is appropriate when the standards file evolves. Not run at close because most pre-2.6 framework docs would flag positives by construction — better as separate scoped follow-up session that triages findings and decides retrofit-now vs. retrofit-later per document.
- **Friction-log entry on pre-emption hazard awaits /think** when a second instance surfaces.
- **Feedback log retains 4 pending Accept-with-/think items:** #27 (reliability vs determinism), #26 Item 2 (scan-pattern, bundled with 2026-05-18 memory-mining), 2026-05-18 /close enhancement, 2026-05-18 memory-mining beat.

**Done at close:**

- Archived Issue #26 Item 1's feedback-log entry to `feedback-log-archive.md` with Resolved line.
- Posted implementation follow-up comment on Issue #26.
- Saved feedback memory `feedback_check_trigger_before_applying_rhythm.md` capturing the rhythm-over-application lesson from observation #3.

**Commits this session:** Two consumer-facing files (standards Section 2.6, `/close.md` Step 3) + internal files (friction-log entry, design-rationale entry, feedback-log archival, two new session logs spanning two work phases). Per Shippability: tag at push since consumer-facing content touched. Suggested tag: v0.0.12. Commit shape decision (one combined commit vs. split per work-phase) discussed at close.

**Where to pick up:**

`/close` to wrap up commits, tag, push. Then any of the remaining /think sessions in the feedback log. The mechanics-without-spirit fix shipping clean creates conceptual room for the next high-leverage item (either #27 reliability-vs-determinism or scan-pattern+memory-mining bundle).
