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
