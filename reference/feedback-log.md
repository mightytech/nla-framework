# Framework Feedback Log

Accepted items from external feedback, waiting for implementation. Each entry captures
what was accepted, why, and where to find the full context.

The feedback log is the sibling of the friction log:
- **Friction log** — things *you* noticed while working
- **Feedback log** — things *others* noticed that you agreed with

Both feed into `/maintain`. Both are queues of actionable items.

---

## How to Use This Log

**When items are added:**
- After triaging feedback (via `/check-feedback` or any intake mechanism), accepted
  items are deposited here with their verdict rationale and a reference to the source.

**When items are resolved:**
- During `/maintain` sessions, the maintainer reviews pending items and implements them.
  Resolved entries are moved to `feedback-log-archive.md`.

**At session start:**
- `/maintain` checks this log alongside the friction log to surface what's waiting.

---

## Entry Format

```markdown
### [DATE] — [Brief description of the accepted item]

**Source:** [Link to GitHub Issue or intake item]
**Verdict:** [Accept / Adapt — and the reasoning]
**Status:** pending | in-progress | resolved

**What to do:**
[Concrete description of the change needed]

**Why it was accepted:**
[The rationale from triage — why this matters, what it improves]

**Resolved:** [DATE] — [brief description of what was changed and where]
```

Not every entry needs all fields. The essentials are: Source, What to do, Why it was
accepted, Status.

---

## Entries

*Entries are added chronologically, newest first.*

### 2026-05-18 — Session-bracketing as a new Working Rhythm

**Source:** [Issue #24](https://github.com/mightytech/nla-framework/issues/24) items 1, 2, 8 + recommendation F
**Verdict:** Accept
**Status:** pending

**What to do:**

Add a new Working Rhythm to `core/nla-foundations.md` capturing the session-bracketing
pattern: `do-work → plan-while-hot → simulate-cold → cold-question-check → adjust →
close-and-clear`. Substeps (per letter item 1):

- **Plan-while-hot** — capture future-session work while current-session context is warm
- **Simulate-cold** — spawn fresh-context agent to read plan; catches author-implicit execution gaps
- **Cold-question-check** — diagnostic questions about conceptual frame; catches concept-layer conflations the simulation can't catch (simulating agent inherits the conceptual frame)
- **Adjust** — apply clear-improvement patches with verify-each-claim discipline
- **Close-and-clear** — finalize, commit, end session

Include the two cold-context check mechanisms distinction (item 2 — simulation catches execution gaps, question catches concept gaps) and the "someone drives the bracketing" note (item 8 — default: human as session-manager; AI surfaces options). Rhythm fires when a session creates non-trivial future work.

**Open framing question:** does this extend The Design Flow's "debrief" beat (downstream framing the maintainer already implemented in facebook-moderation as `Think → plan → implement → debrief → plan next session if necessary`) or stand as a separate rhythm (letter's framing — fires when session creates future work, not within Design Flow)? Resolve at implementation.

**Why it was accepted:**

Well-grounded — multiple project-internal cycles in facebook-moderation, multiple distinct failure mode classes, multiple kinds of substantive work. The maintainer has already implemented it downstream. Naming at framework level propagates discipline to all NLAs producing future-session work. Pairs with the plan/handoff document template entry below.

---

### 2026-05-18 — Plan/handoff document template

**Source:** [Issue #24](https://github.com/mightytech/nla-framework/issues/24) items 3, 5 + recommendation B; [Issue #25](https://github.com/mightytech/nla-framework/issues/25) items 1, 2
**Verdict:** Accept
**Status:** pending

**What to do:**

Document plan-drafting guidance covering four sections beyond title and intent (from letter #24 item 3 + rec B):

- **Substance** — what to do (typically well-served already)
- **Procedural-edge cases** — what to do when source deviates from plan (typically thin)
- **Judgment defaults** — where to lean when rule space is open (typically thin)
- **Confidence band** — where to push back at next collaborative step (typically absent)

Plus two structural patterns from letter #25:

- **Warm-context next-steps section** — explicit section near phase-close beat that asks "what work benefits from the warm context this session produced?" (specific candidate categories + generic open-question + calibration: do plan-shaped and capture-shaped work warm; defer execution-shaped work to fresh session)
- **Paired specific+generic checkpoint questions** — at block-end checkpoints, pair specific questions tied to block decisions with at least one generic open-question for unstructured surfacing

Plus item 5 (intent at every layer): per-step intent, pause-and-surface conditions, open questions surfaced rather than pre-decided. Aligns with existing intent-over-rules principle.

Template doesn't need to be enforced — serves as scaffolding the drafter consults. Sections can be dropped when work doesn't warrant them.

**Placement question:** standalone guidance doc that the new session-bracketing rhythm references? Or folded into `core/skills/close.md`? Depends on the /close-integration decision (next entry).

**Caveat:** Letter #25 item 2 (paired specific+generic) has one-application-validated confidence — slightly lower than other items.

**Why it was accepted:**

Concrete, high-leverage. Drafters answering each section from warm context (cheap) prevents the cold executor from improvising (lossy). Structural form (named sections) makes the discipline more reliable than remembered.

---

### 2026-05-18 — /close enhancement: plan-shaped artifact detection + handoff integration

**Source:** [Issue #24](https://github.com/mightytech/nla-framework/issues/24) recommendations A, E
**Verdict:** Accept-with-/think
**Status:** pending

**What to do:**

Two related enhancements to `/close`:

1. **Detect plan-shaped artifacts and offer cold-context simulation.** When a session has produced files in `reference/sessions/`, `reference/experiments/*/handoffs/`, or similar plan-shaped paths, `/close` offers (opt-in) to spawn a cold-context simulation agent. Simulation reads the plan, reports what they'd do, what they'd improvise, what's ambiguous. Orchestrator presents findings to human for triage with verify-each-claim discipline.

2. **Fold handoff-drafting discipline into `/close`** rather than creating a separate `/handoff` skill. Letter's lean: separate skill would fragment session-end workflow; `/close` is the natural locus.

**Prerequisite: /think session needed** to design:

- Detection rule (which paths count as plan-shaped; how to avoid false positives)
- Integration shape with current `/close` steps (Validate → Check Documentation Mirrors → Debrief → Finalize Session Log → Commit/Tag/Push)
- Whether simulation is offered, default-on, or default-off
- How handoff template guidance (separate entry above) gets consulted in this beat

**Why it was accepted:**

Closes the workflow loop named in the session-bracketing rhythm. Concrete operational value. But the integration design is non-trivial — touches the most-frequently-run framework skill (/close runs every session) and adds opt-in machinery that needs to feel lightweight, not ceremonial. Principle committed; design step is the prerequisite.

---

### 2026-05-18 — Plans-not-runbooks preventive guidance

**Source:** [Issue #24](https://github.com/mightytech/nla-framework/issues/24) item 4 + recommendation C
**Verdict:** Accept (adapted: audit already clean; add preventive note)
**Status:** pending

**What to do:**

Audit finding from triage context-check: no "runbook" framing exists in framework skills already. Only "handoff" appears (in `core/skills/maintain.md` and `core/skills/validate-architecture.md`, both benign uses about NLA artifacts). So the corrective audit recommended in letter #24 rec C isn't needed.

What *is* worth adding: short preventive guidance naming the principle, so future framework work doesn't accidentally adopt runbook framing. Runbook framing structurally suppresses human input (primes script-execution mode); contradicts the cardinal rule even if content tries to compensate. The cases where unattended execution makes sense are properly served by traditional code, not natural-language runbooks.

Natural placement: as a note inside the new session-bracketing rhythm (when describing plan-shaped artifacts), or in `core/skills/close.md` where handoff drafting will be discussed. Either covers the surface area.

**Why it was accepted:**

Sound principle, aligns with foundations principle #4 (intent over rules — "plan" carries different semantic intent than "runbook"). Low cost to add preventive guidance; non-zero benefit when future work touches multi-step-workflow surfaces.

---

### 2026-05-18 — Memory-mining beat in lifecycle

**Source:** [Issue #25](https://github.com/mightytech/nla-framework/issues/25) item 3
**Verdict:** Accept-with-/think
**Status:** pending

**What to do:**

Establish a memory-mining beat in the NLA session lifecycle. Memory accumulates patterns; some patterns earn promotion to structural artifacts (operative docs, plan templates, framework-level guidance) where they become *automatic* — applied because they're in the operative loop, not because the AI consulted memory.

Current asymmetry the letter names: AIs tend to consult memory reactively (when answering) rather than proactively (when creating new artifacts and asking "what existing patterns should this invoke?").

**Prerequisite: /think session needed** to design:

- Where the beat lives (letter floats four options: discrete `/promote-memory` skill; folded into `/debrief`; folded into `/maintain`; folded into `/close` — letter's lean). Letter explicitly asks for framework-level lifecycle decision.
- Triage axis: NLA-specific institutionalization (lands in this NLA's operative docs) vs. upstream framework promotion (lands in framework guidance, applies across all NLAs)
- Mining cadence (per-session, periodic, on-demand)
- Three target categories per pattern: quick fix in this NLA, upstream letter, friction-log entry

**Why it was accepted:**

Identifies a real gap — patterns sit in memory rather than reaching the operative loop. The letter's evidence (their own session: items 1 and 2 of letter #25 were patterns memory would have supplied proactively if mining was operating) makes the case concrete. Principle committed; design step is the prerequisite.

---

*This log is populated by `/check-feedback` (or any external feedback tool) and consumed
by `/maintain`. Resolved entries are moved to `feedback-log-archive.md`.*
