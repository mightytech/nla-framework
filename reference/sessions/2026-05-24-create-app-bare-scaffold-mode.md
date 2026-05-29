# Maintenance Session: Bare Scaffold Mode in /create-app

**Date:** 2026-05-24
**Status:** Complete

## Intent

Resolve the 2026-02-23 friction-log entry "/create-app bare project path: missing guidance and speculative seeds" by giving `/create-app` an explicit handling for users who want a scaffolded NLA they'll author in `/maintain`. Two behavioral shifts:

1. The skill stops grinding through Phase B's content extraction (voice, values, tasks) when the user has signaled they want to defer authoring. The AI recognizes the bare signal during/after Phase A, confirms in prose, and proceeds to mechanical generation.
2. Shared-context files stop carrying invented content from a domain name alone. They're generated as minimal stubs with explicit "unauthored" framing, and a preloaded umbrella friction-log entry surfaces the authoring work in the user's first `/maintain` session — leveraging the existing maintenance queue rather than inventing a new signaling mechanism.

The 2026-02-24 nla-writer follow-up observation (rich-context-but-blank case: good seeds become invisible because they're not bad enough to revisit) is *adjacent* friction and explicitly out of scope here. Recording the boundary in design-rationale prevents future drift back into a single combined fix.

## Changes Made

- **`.claude/skills/create-app/SKILL.md`** — multiple coupled additions:
  - "Between Phase A and Phase B: Recognize the mode" extended to three shapes (Extraction / Collaborative-refinement / Bare scaffold). Bare-scaffold definition leads with posture ("AI's job is not to extract or refine — it's to set up scaffolding and get out of the way"); confirmation prose included; bare-scaffold signals enumerated as a parallel list to collaborative-refinement signals.
  - "Phase B: Targeted Follow-ups" gets a top paragraph: if bare scaffold was recognized, Phase B collapses; confirm name only.
  - "Phase C: Summary and Confirmation" gets a bare-scaffold summary template variant.
  - "Conversation Edge Cases" gets a "User wants a bare scaffold" entry pointing at the recognition beat and the Bare Scaffold Mode subsection.
  - New "Bare Scaffold Mode" subsection in File Generation, between Domain File Structures and Generation Order. Specifies per-category behavior, stub file shapes including the exact unauthored-stub header, the preloaded friction-log entry template (with creation-date placeholder), and the "why two surfaces" framing for the stub+friction-log pairing.
  - "Generation Order" gets a one-line pointer noting which steps differ for bare-scaffold.
  - "Narration" table gets a bare-scaffold row.
  - "Post-Creation" gets a bare-scaffold next-steps variant (step 5 is `/maintain`, not running a task).
  - "Internal Consistency Check" gets bare-mode items 11-17 (no task docs, no domain skills, stubs verified, output-spec absent, preloaded friction entry exists, overview reflects bare state, skills tables clean).
  - "What You Don't Do" gets a "Don't invent content when bare scaffold was confirmed" bullet.
- **`reference/design-rationale.md`** — added "Bare Scaffold Path in /create-app" section before "Adding Decisions." Captures: what was decided, why this shape (reuse existing recognition pattern, two-surface epistemic signal, leverage existing maintenance queue), rejected alternatives (universal Phase B/C broadening; CLI flag), adjacent case explicitly out of scope (2026-02-24 nla-writer rich-context-but-blank inversion), architectural observation (deferred — bare-mode generation is a strong candidate for `lib/` extraction once Python standards exist; cross-references the new 2026-05-24 friction-log entry), blast radius.
- **`reference/friction-log.md`** — added new 2026-05-24 entry "Scaffold-first generation as the unified /create-app mechanism." Captures the architectural reframe surfaced during this session: split `/create-app` into deterministic scaffold generation + AI-applied conversation edits. Pairs with the existing 2026-04-16 cluster (Python standards, prose-vs-code distinction, nla-compiler experiment). Status: pending. Waits on Python standards / nla-compiler availability.
- **`reference/friction-log.md`** — removed the 2026-02-23 entry (moved to archive).
- **`reference/friction-log-archive.md`** — added the 2026-02-23 entry at the top (most recent resolution), with `Status: resolved` and a `Resolved:` line referencing the design-rationale section and naming the explicit out-of-scope boundary.
- **`reference/sessions/2026-05-24-create-app-bare-scaffold-mode.md`** — this session log (internal).

## Decisions Made

- **Extend the existing mode-recognition beat (third value) rather than create a new recognition.** The 2026-05-11 mode-recognition pattern (extraction vs. collaborative-refinement) is fundamentally "what conversation is the user inviting?" — bare is a third answer on the same axis, not a parallel axis. Reuses existing pattern; no new machinery.
- **Two-surface epistemic signaling: stub header *and* preloaded friction-log entry.** Stub headers catch the gap at task-execution time (LLM reads voice.md and sees "unauthored"). Friction-log entry catches it at `/maintain` session start (the maintainer sees authoring work in the queue). Different surfaces for the same signal — covering both is light belt-and-suspenders, not redundancy.
- **Prose recognition with confirmation, not CLI flag.** Per CLAUDE.md's prose-default principle. User talks to an AI, not a Python program. AI confirms: "Sounds like you want a bare scaffold named X — empty stubs you'll author in /maintain. Right?"
- **Phase B collapses to project-name-only in bare mode.** Skip voice/values/tasks/output/audience. The framework needs a name and a place to put things; everything else is deferred.
- **Reject "broaden Phase B/C universally."** Considered making tasks structurally optional throughout the skill (the route the 2026-02-24 addendum hints at). Rejected: bare is a specific user-requested shape, not a general restructuring. Broadening universally would require the AI to improvise at every step rather than having a clear starting signal. The recognition beat *is* the structural signal.
- **2026-02-24 nla-writer case explicitly out of scope.** Different friction shape (rich-context-but-blank vs. thin-context-but-blank). Same generated content, opposite failure modes depending on input richness. Treating both in one fix would conflate them. Recorded as adjacent in design-rationale.

## What Didn't Work

- **Initial /think framing pulled in the 2026-02-24 nla-writer addendum as if it were core scope.** I read the addendum carefully alongside the main entry and let its depth color my mental model — coming into /think with a frame that bundled seed-authority signaling and the rich-context-blank case with the bare-scaffold work. The maintainer's "Maybe I'm misremembering" reframe caught it cleanly. Cost was small (one round-trip), but the underlying mistake was treating the addendum as additional requirements rather than as context that may or may not be in scope.

## Friction Log Entries Processed

- **2026-02-23 — /create-app bare project path: missing guidance and speculative seeds** — resolved this session via bare-scaffold mode addition to `.claude/skills/create-app/SKILL.md` + design-rationale entry. Archived.

## Friction Log Entries Created

- **2026-05-24 — Scaffold-first generation as the unified /create-app mechanism** — new pending entry capturing the architectural reframe surfaced when the maintainer asked "what are the actual mechanisms?" Pairs with the 2026-04-16 cluster (Python standards, prose-vs-code distinction, nla-compiler experiment). Waits on Python standards / nla-compiler availability.

## Debrief

Refined observations from this session's explicit `/debrief`:

1. **Addendum over-shaped initial scope.** The 2026-02-24 nla-writer addendum is *adjacent context* to the 2026-02-23 entry, not additional requirements. Reading both before forming a frame meant the addendum's depth set my initial mental model. Diagnostic: when a friction entry has a richly-detailed addendum, read the entry as written first and treat the addendum as context whose scope-inclusion is a separate question. The reset was inexpensive in this session but the pattern generalizes.

2. **Architectural soft spot came from the maintainer's question, not my proactive surfacing.** The maintainer's "what are the actual mechanisms?" question landed at commit time, but it was a design-time question — the bare path is so mechanical that "is the LLM the right tool for this?" was worth raising during /think, not after validation. I designed bare-mode entirely within the existing AI-as-typist paradigm without flagging the hybrid-architecture observation. Diagnostic: for any /create-app or file-generation work, explicitly ask "what's mechanical here and is the LLM the right tool?" as a routine /think beat. (The reframe still landed productively, captured as a new friction-log entry, but it would have been part of the original design rather than emergent.)

3. **Section 2.6 nearly bit on validation findings.** When naming the two soft findings from /validate, I labeled them "not blockers" and asked whether to apply — phrasing that reads as *almost* pre-judging toward skip. The same failure mode that Section 2.6 and the /close Step 3 retrofit just shipped to address. The maintainer's "apply both" suggests the framing wasn't catastrophic, but the offer language carried a default pull. The just-shipped guidance applies to validation findings too, not only to skill choice points. Worth keeping in awareness.

4. **Consumer-facing self-catch worked, but the underlying lapse is noteworthy.** I wrote "Consumer-facing: yes... Tag at push" in the design-rationale entry, then caught it during commit prep by checking the 2026-05-11 session log's note that create-app changes don't contribute to tag decisions. The catch was good, but the original write was wrong — I'd written what felt plausible rather than checking the Shippability rule. Diagnostic: before filling Shippability or blast-radius fields, read the relevant rule explicitly. The framework's own definition is short; the check is cheap.

5. **Positive: the /think reset was cheap.** The maintainer's single-sentence reframe ("Maybe I'm misremembering...") was enough to land us on the right scope. I acknowledged the drift, didn't defend the larger frame, and we converged in a few exchanges. The design flow worked as intended. Preserving this — flagging it as something the framework's posture already supports.

The maintainer noted observations #1 and #2 as most generalizable — candidates for promotion to memory or friction-log if they recur. Not filing now; awaiting recurrence to confirm pattern.

## State at Close

**Context for next time:**

- Bare-scaffold mode shipped 2026-05-24, committed in e7a6e0d. Framework-internal change; no tag, no update-notes entry. Pushed/unpushed status depends on Step 5 below.
- Friction log delta: one resolved (2026-02-23 bare-project), one created (2026-05-24 scaffold-first generation). Net: 8 pending → 8 pending (count unchanged; composition shifted).
- Feedback log unchanged: 4 pending Accept-with-/think items (#27 reliability-vs-determinism, #26 scan-pattern + #25 memory-mining bundle, #24 /close enhancement).
- Multi-day session: work done 2026-05-24; close completed 2026-05-29.

**Decisions awaiting implementation:**

- None. All decisions made this session were implemented in-session.

**Where to pick up:**

- **Bare-scaffold fresh-context test.** The maintainer has a real bare app to create and elected the fresh-context path over same-context (per Validation Flow rhythm + writing standards Section 2.6 — documentation correctness is necessary but not sufficient; framing transfers reliably only when verified in execution). The fresh-context run will produce real signal about whether the bare-mode recognition beat fires cleanly on real user input and whether the generation rules produce the intended stub-plus-preloaded-entry shape. If anything feels off, capture via /friction-log in the new project or surface here for the next /maintain session.
- **Remaining pending work** (unchanged from prior session): four Accept-with-/think feedback items; the 2026-04-16 traditional-code cluster (Python standards, /maintain prose-vs-code distinction, Fallingwater-style preamble, deferred re-compile of lib/export.py); the 2026-05-20 accept-with-/think verdict prominence in check-feedback (penny-post submodule, not editable from framework); the 2026-05-23 multi-step protocols pre-emption hazard (awaits second instance for /think); the 2026-03-08 /startup disable-model-invocation question; the 2026-02-23 friction-log gitignored question.
- **Architectural follow-up entry (2026-05-24 scaffold-first generation)** waits on Python implementation standards / nla-compiler availability. Best addressed together when those land.
