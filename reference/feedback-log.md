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

### 2026-09-09 — Understanding over deliverables: wicked problems and silent taming

**Source:** [Issue #31](https://github.com/mightytech/nla-framework/issues/31)
**Verdict:** Accept-with-/think — bundled with the 2026-05-22 reliability-vs-determinism entry (below)
**Status:** pending
**Bundled with:** 2026-05-22 — Reliability vs determinism (below)

**What to do:**

Add a principle to `core/nla-foundations.md` along the lines the letter drafts: the problems that matter are wicked (Rittel & Webber) — no definitive formulation, no stopping rule, better-or-worse rather than right-or-wrong. A spec, a schema, a test is a wicked problem wearing a tame mask, held in place by judgment filling the gaps, so the real work is defining and redefining what the problem *is* rather than producing the deliverable-shaped object. The guard is process, not restraint — contestable stopping points, the human drawing the consequential lines — because the taming happens inside retrieval, before any deliberation the runtime could inspect.

Two edges the letter insists keep the principle from flattening into a platitude: the runtime's flatness is a **reagent** (a confident, well-formed answer to an under-defined question marks where understanding is still owed), and route by **stakes** in both directions (spend understanding where wickedness compounds; withhold it where a wrong choice is cheap and reversible).

**Prerequisite: shared /think session with the 2026-05-22 reliability-vs-determinism entry.**

Both items propose sharpening foundational language about *what the work optimizes for*, both carry open channel-and-placement questions, and both explicitly invite maintainer judgment on shape. Designing them in separate sessions risks two adjacent principles that should have been one — the same failure the 2026-05-22 scan caught for scan-pattern and memory-mining. The bundled /think considers:

- **One principle or two?** The letter itself flags the possible split (the taming diagnosis vs. the stakes-routing operational half), and #27's decision filter may be the same axis viewed from a different side.
- **Channel and placement.** Framework's dual-channel rule applies: `install/CLAUDE-intent.md` propagates to domain projects, the framework's own `CLAUDE.md` does not inherit from it, and `core/nla-foundations.md` is a third surface. #27's entry already establishes that the "non-determinism is a feature" aphorism lives in the first two, not foundations.
- **How hard to state the contestable claims.** The letter is emphatic that the principle earns foundations only if it keeps its teeth (specs are wicked problems wearing tame masks; a more capable model computes a better average and so deepens the flatness; software as a field denies its own wickedness). Smoothing those into a values-statement tames the principle about taming. Open question for a doc that domain projects across many fields will read.

**Why it was accepted:**

The framing is sound and the letter is a warm-context briefing rather than a closed verdict — it hands over reasoning to continue with, and is explicit that wording, placement, and cardinality are open. The theory it rests on is the maintainer's own. Principle committed; design step is the prerequisite for shape and placement decisions.

**Second payload, routed separately:** #31 also carries post-fix recurrence evidence that is not about the principle — see the gate/verification-cluster entry below, which is where that evidence lands.

---

### 2026-09-09 — "Be-done" bias at review/verify/wrap gates (gate/verification cluster)

**Source:** [Issue #32](https://github.com/mightytech/nla-framework/issues/32), with corroborating evidence from [Issue #31](https://github.com/mightytech/nla-framework/issues/31) and [Issue #28](https://github.com/mightytech/nla-framework/issues/28) Item 3
**Verdict:** Accept-with-/think
**Status:** pending

**What to do:**

Address the recurring AI disposition toward *being done* — wrapping up or advancing to the next stage over doing good work — and the associated misreading of felt-slowness as a stop signal. The discipline the letter names: reason to the stopping *criterion* rather than assert "done," and treat "we're done, proceed" at a review/verify/wrap gate as the weakest kind of confidence.

**Prerequisite: /think session** on the response shape, drawing on the full cluster rather than #32 alone:

- **#32** — the disposition at gates. Three proposed terminuses in one session, each overridden by "one more cheap check," each check paying (two spec gaps, two more, a full-scope review, ultimately a deploy-breaking mechanism error caught only because the compile actually ran).
- **#31's second payload** — post-fix recurrence evidence. `core/skills/close.md:92` carries the mechanics-without-spirit retrofit verbatim ("The offer is a fresh invitation, not an opt-out from work-already-done"), shipped 2026-05-23; #31 documents that exact failure on 2026-07-15. The same letter documents a warm-context handoff drafted as a runbook despite the Session-Bracketing rhythm's plans-not-runbooks note — which design rationale describes as *preventive* because a 2026-05-18 audit found no runbook framing anywhere.
- **#28 Item 3** — third-party corroboration from a different project: "the framework's procedures sometimes describe the load-bearing step in detail and underweight the closing/verification step." nla-office-hours deferred the generalization question to us pending more cases; #31 and #32 are those cases.
- **2026-05-23 friction entry** (multi-step protocols: pre-emption hazard) — its stated trigger was "worth /think when a second instance surfaces." #31 is that second instance. Fold it in rather than running a separate session.
- **The `/maintain` posture-preamble deferral** — 2026-05-23's third trigger ("if future authoring shows *I knew about it but didn't apply it* instances, revisit") has now fired. Note that this third trigger was decided in the 2026-05-23 debrief but never recorded in `reference/design-rationale.md`, which still lists only two; recording it is a prerequisite housekeeping step.
- **Sequencing with the pending #24 `/close` enhancement** — that item modifies `/close`'s step structure and #31's instance is a `/close` Step 3 failure. The two shouldn't be designed blind to each other.

**Constraint on the fix shape, from the letter itself:** when asked to diagnose the bias, the AI's proposed fix — "just price the cheap check into the stop decision" — *was the bias operating*, converting an open truth into a tidy closeable rule so the discussion could end. So "add a rule to the gate skills" is suspect as a response. The counterweight is also real: the efficiency instinct is sometimes right, and the ask is calibration, not suppression.

**Why it was accepted:**

Three independent sources converging on one shape — the verify/close/deliberate step gets underweighted or skipped. #32 self-describes as a single richly-documented instance, but the cross-letter picture is considerably stronger. The decisive evidence is that the framework's two existing mitigations in this exact territory (Section 2.6 plus the `/close` Step 3 retrofit; the plans-not-runbooks note) were both present and both failed to fire. That argues awareness-level captures aren't sufficient here — the same conclusion the 2026-05-22 scan-pattern triage reached about corpus-consultation, arriving now with different content.

---

### 2026-09-09 — Post-bulk-edit verification step missing from /maintain Bulk Edits

**Source:** [Issue #28](https://github.com/mightytech/nla-framework/issues/28) Item 2
**Verdict:** Accept
**Status:** pending

**What to do:**

Append a verification clause to the Bulk Edits section of `core/skills/maintain.md`. The section currently says mechanical pattern substitutions should use a single `Bash` pipeline over the target files — correct for the substitution step, but the procedure stops there. Add guidance to grep-verify across operative content (`app/`, `CLAUDE.md`, `README.md`, and equivalents) before committing, with the reason: sed catches uniform structural prose cleanly, while narrative references embed the old pattern in surrounding text and escape regex matching. The letter drafted usable clause text.

Consumer-facing (`core/`) — update-notes entry at commit, tag at push.

**Why it was accepted:**

Two clean instances in a single session with identical shape: the packages migration sed-swept 16 thin wrappers correctly but missed narrative references in three files, and the examples-catalog pass missed CLAUDE.md's Modes section and Environment table. Both passes "looked clean" after the sweep and weren't; both were caught post-commit. `/validate` structural mode catches this, but only if invoked — folding it into the Bulk Edits flow closes the gap without requiring a separate invocation per sweep. Exact landing spot, drafted text, no design question.

---

### 2026-09-09 — /update Phase 1 reports "up to date" when the project is months behind

**Source:** [Issue #29](https://github.com/mightytech/nla-framework/issues/29) items 2 and 3
**Verdict:** Accept — light shape only; medium and heavier shapes deferred
**Status:** pending

**What to do:**

Add a clarifying sentence to `core/skills/update.md` Phase 1 noting that "up to date with remote" doesn't mean "up to date with installed state," and pointing readers to Phase 2 for the dormancy signal.

**Deferred:** the letter's medium option (reorder — run a `commits-since-install` check before fetching remotes) and heavier option (a dormancy branch triggered past N commits or M months). Revisit if a second dormant-project update reports the same friction.

Consumer-facing (`core/`) — update-notes entry at commit, tag at push.

**Why it was accepted:**

Verified against the artifact. For a dormant project every Phase 1 line reads "0 ahead, 0 behind" while Phase 2 surfaces the real gap — in the reporting session, 121 commits between installed state and current package state. The Phase 1 summary (`update.md:74`) reports only remote-vs-local status, so a maintainer reading it would reasonably conclude no update is needed.

One refinement from verification that shapes the fix: line 76 already gates the early stop on local-vs-installed state, so the protocol wouldn't actually terminate wrongly. The defect is in the *reported signal*, not the control flow — which is why the light fix is likely sufficient and the medium reorder isn't warranted on one data point.

---

### 2026-09-09 — Update-notes backstop: new skills can ship without an entry

**Source:** [Issue #30](https://github.com/mightytech/nla-framework/issues/30)
**Verdict:** Accept — both halves, with the author-time fix landing more precisely than the letter proposed
**Status:** pending

**What to do:**

Three pieces, in order:

1. **Backfill the specific gap.** Add an `install/update-notes.md` entry for `/session-checkpoint`. Confirmed absent: no mention in the notes file, and no `update-notes-archive.md` exists at all (the letter hedged about an archive it couldn't read — there isn't one).
2. **Close the author-time hole.** `core/skills/README.md`'s "Adding a New Skill" checklist has 7 steps and none of them is "add an update-notes entry." That is the precise hole. Add the step. The letter proposed an author-time convention in general terms; the checklist is where such a convention actually lives for skill additions.
3. **Skill-time backstop, sequenced second.** Have `core/skills/update.md` Phase 2 cross-reference `install/skills-intent.md` against the consuming NLA's wrappers, flagging missing wrappers regardless of update-notes coverage. More machinery than pieces 1 and 2, so it follows them.

Pieces 2 and 3 are consumer-facing; piece 1 is an update-notes entry in its own right.

**Why it was accepted:**

The gap is verified and the risk scales badly: `/update` consults update-notes to decide what to propose, so a skill that ships without an entry is invisible to dormant projects unless their maintainer independently lists the canonical skill set and compares — which is what the reporting maintainer happened to do.

The backstop half earns its keep for a reason the letter couldn't see from outside: a general rule *already exists* — `maintain.md`'s Shippability protocol says commits touching consumer-facing content get an update-notes entry, and `core/skills/` is consumer-facing. That rule didn't fire. Author-time convention alone has now demonstrably failed once, which is the argument for pairing it with a defensive check rather than treating them as alternatives.

---

### 2026-09-09 — End-user update affordance (materializing submodule pins)

**Source:** [Issue #28](https://github.com/mightytech/nla-framework/issues/28) Item 1
**Verdict:** Adapt — gap accepted, proposed shape corrected and reconsidered
**Status:** pending

**What to do:**

Give end users a path to bring a cloned NLA up to date. `/update` is maintainer machinery — it advances submodule pins *and* integrates intent migrations — and an end user who runs it triggers a workflow they didn't want. Without the second command, `packages/` sits at the old pinned state and the user hits wrong content silently.

**Two adaptations to the letter's proposal:**

1. **Drop `--recursive`.** The letter proposes wrapping `git pull --ff-only && git submodule update --init --recursive`. That contradicts documented framework convention — `install/update-notes.md:755` states: "Use `git submodule update --init` (not `--recursive`). Dependencies are flat — each project lists only its direct dependencies." Recursing would descend into packages' own `packages/` directories, which the packages-migration design rationale names as wasteful nesting.
2. **Reconsider whether a script is the right shape.** The real gap is *awareness* — the AI recognizing that "bring this application up to date" means these two commands and the split between them — not the absence of a two-line wrapper. Documentation plus AI awareness is cheaper, ships no new code artifact, and avoids depending on the pending "no implementation standards for Python scripts in `lib/`" entry. Recommended shape: document the split (`/update` integrates intent changes, maintainer-only; plain git materializes pins, everyone) and make the AI aware of the phrasing that should trigger it, with a `lib/` script as an optional convenience if it still seems warranted afterward.

**Why it was accepted:**

The gap is real and high-confidence — verified that no such affordance exists (`lib/` holds only `export.py`, and README documents the clone but not the update). It surfaced organically from a genuine question about whether `/update` should learn about a new `examples/` directory; the right answer there was no, and that conversation made the missing affordance visible.

**Related:** shares the update-pipeline surface with the #29 and #30 entries above. Worth considering whether all three are one session's work.

---

### 2026-05-22 — Reliability vs determinism as load-bearing distinction in foundational language

**Source:** [Issue #27](https://github.com/mightytech/nla-framework/issues/27)
**Verdict:** Accept-with-/think
**Status:** pending
**Bundled with:** 2026-09-09 — Understanding over deliverables (above). Both sharpen foundational language about what the work optimizes for; both carry open channel-and-placement questions. Shared /think session.

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
