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

### 2026-05-22 — Reliability vs determinism as load-bearing distinction in foundational language

**Source:** [Issue #27](https://github.com/mightytech/nla-framework/issues/27)
**Verdict:** Accept-with-/think
**Status:** pending

**What to do:**

Add the reliability-vs-determinism framing to the framework's foundational language. The letter's argument: "non-determinism is a feature" tells you what to embrace; "optimize for reliability" tells you what to optimize *for* — positive direction rather than negation. The framing provides a decision filter ("does this optimize for outcome quality or output uniformity?"), distinguishes the *routing* question (AI vs code) from the *optimization-within-AI-work* question, and connects to existing principles #4 (Intent over Rules) and #7 (Hybrid Architecture) without redundancy.

**Prerequisite: /think session needed** to design:

- **Channel and placement.** The "Non-determinism is a feature" aphorism currently lives in `install/CLAUDE-intent.md` (line 31) and the framework's own `CLAUDE.md` (line 21), NOT in `core/nla-foundations.md` as the letter assumed. So the question isn't "expand the existing foundations line" — it's deciding which channel(s) the sharper framing belongs in. The framework's dual-channel coverage rule (CLAUDE-intent ≠ framework's CLAUDE.md, both may need updates) applies.
- **Placement within foundations.** Multiple valid options: new principle, rewrite/expand of #7 Hybrid Architecture, expansion of the Hybrid Model intro section, or some combination. Letter explicitly invites maintainer judgment.
- **Cross-references.** Potential connection to writing standards (the "rubric/standards quality compounds, constraint count plateaus" claim aligns with standards' own posture).

**Why it was accepted:**

The framing genuinely sharpens existing material. Evidence is solid (Phase C 6/6, standards-as-biggest-quality-driver across multiple facebook-moderation experiments — not single-data-point territory). The decision filter is operational in a way the current aphorism isn't. Principle committed; design step is the prerequisite for placement and channel decisions.

---

### 2026-05-22 — Scan-pattern technique (bundled with memory-mining beat for shared /think)

**Source:** [Issue #26](https://github.com/mightytech/nla-framework/issues/26) Item 2
**Verdict:** Accept-with-/think — bundled with the 2026-05-18 memory-mining beat entry
**Status:** pending
**Bundled with:** 2026-05-18 — Memory-mining beat in lifecycle (below)

**What to do:**

Capture the cross-corpus pattern-scan technique somewhere in the framework. The letter proposed a `/scan-pattern` skill (hybrid: cold-context subagent for broad recall + warm-context orchestrator for filtering, with four-section output: clean candidates / borderline / counter-evidence / existing-captures). N is now ≥2: the framework's own corpus, scanned via the technique during this triage (2026-05-22), surfaced 4 clean misses where the technique would have helped, 4 counter-evidence cases, and a 7-capture map showing the framework has the precedent-scan idea in multiple awareness-level places that haven't fully closed the gap.

**Prerequisite: shared /think session with the memory-mining beat (2026-05-18 entry below).**

The scan revealed structural adjacency: both items are about "consult the corpus proactively at decision-time." Memory-mining promotes patterns *out of* memory into operative artifacts; scan-pattern surfaces patterns *from* the corpus at decision time. Running two separate /think sessions would risk producing two adjacent features that should have been one. The bundled /think considers:

- **Mechanism shape.** Dedicated `/scan-pattern` skill vs. extending `/think`'s existing Prior Art beat vs. always-loaded record extensions (per the scan's Counter 1 — `core/structure.md` surfacing catches precedent natively where always-loaded records exist) vs. some combination.
- **Relationship to memory-mining.** Does one subsume the other? Are they two faces of the same mechanism? Do they share design language?
- **Cost-of-misdiagnosis.** Per the scan's Counter 4: scan-pattern risks solving the wrong layer when the actual failure is *judgment about loaded material*, not recall. Mitigation needed.
- **Connection to Inquiry Flow.** The Inquiry Flow rhythm uses cold-context AI as one of three verification modes; scan-pattern is structurally similar (cold-context AI for surfacing-stage diagnostics). Worth considering whether scan-pattern is an Inquiry Flow application or a sibling rhythm.

**Why it was accepted:**

Evidence picture shifted from N=1 to N≥2 via the framework-side scan run as part of this triage. The 7-capture map argues that the framework keeps re-noticing this gap and capturing it in progressively larger surfaces (memory → /think Prior Art → CLAUDE.md prose-default) without closing it — suggesting awareness-only captures aren't sufficient. Bundling with memory-mining is the higher-leverage move because it surfaces a connection that wouldn't have been visible without the scan. Principle committed; design step is the prerequisite for mechanism-shape and bundling decisions.

**Scan artifact:** Full scan output captured in `reference/sessions/2026-05-22-feedback-triage-and-scan-pattern-test.md` under "Scan output."

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

### 2026-05-18 — Memory-mining beat in lifecycle

**Source:** [Issue #25](https://github.com/mightytech/nla-framework/issues/25) item 3
**Verdict:** Accept-with-/think
**Status:** pending
**Bundled with:** 2026-05-22 — Scan-pattern technique (above). Structural adjacency surfaced during 2026-05-22 triage scan: both items are about "consult the corpus proactively at decision-time." Shared /think session.

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
