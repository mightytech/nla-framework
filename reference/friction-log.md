# Framework Friction Log

Running log of learnings from framework development, domain project feedback, and maintenance observations. Each entry captures something worth remembering about the framework itself.

---

## How to Use This Log

**When to add entries:**
- When a domain project encounters friction with framework behavior
- When you notice a pattern across multiple projects
- When something works surprisingly well
- When something fails unexpectedly during framework maintenance

**Entry types:**
- `core` — Issues with framework foundations or skill logic
- `intent` — Gaps or improvements in the install/intent files
- `process` — How framework maintenance workflows function
- `documentation` — Clarity or gaps in framework docs (README, CONTRIBUTING)

**Severity includes positive:** Capture what works, not just what breaks.

---

## Entry Format

```markdown
### YYYY-MM-DD — [Brief descriptive title]

**Type:** core | intent | process | documentation
**Severity:** positive | minor | major
**Blast radius:** all projects | project generation | maintainers
**Status:** pending | resolved | deferred | wont-fix

**Observation:**
[What happened or was noticed]

**Before:** [What the framework produced or did]
**After:** [What was expected or desired]

**Confirmed reason:**
[The human's explanation — their words, not a summary. This field matters as much as the
fix itself. Diagnose from the artifacts (docs and output), not from the AI's narrative.
Record the root cause — was it a doc gap, an ambiguity, a conflict between docs, or an
actual processing error? The diagnosis determines the right fix and prevents recurrence.]

**Affected files:**
[Which core/ or install/ files would need to change]

**Proposed fix:**
[Specific enough for /maintain to act on]

**Notes:**
[Additional context, related entries, patterns noticed]
```

Not every entry needs all fields. The essentials are: Observation, Type, Severity, Blast radius, Status. Include what you have; don't force what you don't.

**When `/maintain` resolves an entry**, it updates the Status field:
```markdown
**Status:** resolved
**Resolved:** [DATE] — [brief description of what was changed and where]
```

---

## Entries

*Entries are added chronologically, newest first.*

### 2026-05-24 — Scaffold-first generation as the unified /create-app mechanism

**Type:** core
**Severity:** minor
**Blast radius:** all projects (project generation)
**Status:** pending

**Observation:**
Surfaced during the 2026-05-24 bare-scaffold maintenance session as an architectural reframe of how `/create-app` works. Currently the AI handles both conversation (judgment) and file generation (largely mechanical) within a single skill — reading intent files and writing 30+ template files inline. For Category 1 files this is pure template reproduction; for Category 2 the conversation customization is often shallow (project name substitution, skill-table filling); for Category 3 the conversation synthesis is the genuine LLM work. Bare mode makes the soft spot more visible — almost everything collapses to template substitution and the LLM's value-add reduces to conversation + edge-case handling.

The architectural reframe: `/create-app` could split into two phases.

1. **Scaffold generation** — a `lib/` script (Python or similar) generates the bare scaffold deterministically from minimal inputs (project name, package list). Produces the same shape as bare-mode generation today: directory structure, git/submodule setup, Category 1 files verbatim, Category 2 files in template-with-empty-task-sections form, Category 3 files as stubs.

2. **AI-applied conversation edits** — the AI has the conversation, then applies the results as Edit operations on top of the scaffold. Categories 2 and 3 get filled with conversation-shaped content via Edit rather than written from scratch. Bare mode is "scaffold-only, no edits." Other modes are "scaffold + N edits."

**Why this matters:**

- Per `core/nla-foundations.md` principle #7 (Hybrid Architecture): mechanics belong in code, judgment belongs in the LLM. The current model has the LLM doing mechanical reproduction.
- Speed and consistency: scaffold generation is fast and identical every time.
- Edits are diffable and reviewable in a way that "AI wrote 30 files from scratch" isn't.
- Bare mode collapses cleanly to "scaffold-only," unifying it with all other modes as the same machinery with different edit counts.
- Mirrors how human developers create projects (`cargo new`, `npm init`, then customize).

**Open questions / to think through:**

- Category 2 files where current behavior is "conversation-shaped from scratch" (e.g., `design-rationale.md`'s "starter rationale with creation decisions for this domain") need spec'ing under scaffold+edit. Scaffold generates a template form; AI fills via Edit. None look blocking, just needs design work.
- Generation Order currently matters because later files reference earlier ones. A pre-generated scaffold might paint into corners — needs verification that the scaffold's known-shape doesn't preclude legitimate variation.
- How do package additions flow? Scaffold generated *before* conversation means we'd either need to ask package questions up-front or run scaffold generation again after submodule adds.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — major refactor
- `lib/create_scaffold.py` (or similar) — new
- Likely `install/structure-intent.md` — scaffold script reads it as the structural source

**Proposed fix:**
`/think` session on the two-phase architecture, then implementation when (a) Python implementation standards exist in the framework (currently a separate pending entry), or (b) the nla-compiler package becomes installable (per the 2026-04-16 cluster). Pairs with existing entries.

**Links:**
- 2026-04-16 — Python implementation standards for `lib/` scripts (pending; blocks this)
- 2026-04-16 — `/maintain` doesn't distinguish prose-code from traditional-code authoring (pending; same cluster)
- 2026-04-16 — Natural experiment: re-compile `lib/export.py` through nla-compiler when available (deferred; same cluster)
- 2026-02-23 — `/create-app` bare project path (resolved 2026-05-24; this entry is the architectural follow-up the bare-mode fix's design-rationale notes as deferred)

**Notes:**
The bare-mode fix shipped 2026-05-24 ran consciously through the existing AI-as-typist mechanism. The design-rationale entry "Bare Scaffold Path in /create-app" includes a paragraph naming this observation and cross-referencing this entry.

---

### 2026-05-23 — Multi-step protocols: pre-emption hazard when earlier work overlaps later choice points

**Type:** process
**Severity:** minor
**Blast radius:** all projects (any multi-step protocol is at risk)
**Status:** pending

**Observation:**
Surfaced via 2026-05-21 recurrence comment on Issue #26. The `/close` protocol assumes sequential execution (Step 1 Validate → Step 2 Mirrors → Step 3 Debrief → Step 4 Finalize log → Step 5 Commit). When work characteristic of Step 4 (adding observations during warm-context next-steps work) happens before Step 3 fires, the Step 3 choice point arrives with state already set. The AI evaluates "is this a fresh choice point?" against the existing state and produces a malformed offer that telegraphs pre-judgment ("if you want substantive reflection beyond what I captured, /debrief is available. Otherwise the captured observations stand").

The pattern generalizes beyond `/close`. Any multi-step skill where one step naturally produces work that overlaps another step's choice point is at risk:
- `/maintain`'s Pre-flight Review may preempt the "Before Starting Work" conversation
- `/think`'s convergence work may preempt the explicit transition checkpoint
- `/create-app`'s later phases may preempt earlier-phase questions

**Confirmed reason:**
Procedural docs assume the AI evaluates each step against a clean slate. When earlier work happens to produce step-relevant state, the AI's "is this a fresh choice point?" evaluation gets state-influenced rather than design-influenced. The protocol design didn't anticipate inter-step state-leakage.

**Affected files:**
- `core/skills/close.md` (the named instance — wording-level mitigation landed 2026-05-23)
- Potentially `core/skills/maintain.md`, `core/skills/think.md`, `core/skills/create-app.md` (latent instances)

**Proposed fix:**
Two design directions worth considering (worth `/think` on which generalizes better):
(a) Each step adds an explicit pre-emption check: "if this step's work has been partially done elsewhere, handle that explicitly — re-offer the choice as additive, not as opt-out."
(b) Protocols designed so steps don't naturally produce overlapping work.

Within the immediate 2026-05-23 mechanics-without-spirit fix, `/close` Step 3 got a narrow pre-emption-awareness paragraph addressing this specific case. The broader fix (does the pattern need a framework-level treatment?) is separate work.

**Notes:**
Distinct from mechanics-without-spirit (parent Issue #26), though the 2026-05-21 instance combined both shapes. Worth `/think` when a second instance surfaces.

---

### 2026-05-20 — "Accept-with-/think" verdict shape needs more prominence in check-feedback

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** pending

**Observation:**
During a multi-letter triage of feedback from facebook-moderation (Issues #24, #25, 2026-05-18), I labeled two structurally-identical items different verdicts: one "Adapt," one "Defer." Both items were the same shape — principle committed; design step (a `/think` session) needed before implementation could be specified. The maintainer caught the inconsistency and named the right shape: "accept-with-/think."

The check-feedback skill (`packages/nla-penny-post/app/check-feedback.md` Step 4) does allow this verdict shape, explicitly: "These are convenient defaults, not an enum. 'Accept the principle, defer the specific implementation' is a valid verdict." But this guidance is a parenthetical after the four primary verdicts (Accept, Adapt, Defer, Decline). The parenthetical's prominence was insufficient to prevent my drift.

**Before:** Two structurally-identical items got different verdicts (Adapt vs. Defer) because the AI pattern-matched to the four primary verdicts rather than recognizing the hybrid case.

**After:** The hybrid case should be visible at decision time, not require post-triage reconciliation.

**Confirmed reason:**
The four primary verdicts (Accept, Adapt, Defer, Decline) are the prominent pattern-matching surface. The hybrid case requires conscious application of guidance that's currently subordinated to the primary verdicts. When triaging multiple items in flow, the AI defaults to the prominent four.

**Affected files:**
- `packages/nla-penny-post/app/check-feedback.md` — Step 4 "Propose Verdicts"

**Proposed fix:**
Give "Accept with prerequisite" more visible placement — possibly as a fifth named verdict ("Accept-with-/think" or "Accept-with-prerequisite"), or as a sub-pattern under Accept ("Accept (immediate)" vs. "Accept (with prerequisite)"). The prerequisite might be `/think`, more evidence, or a dependent change.

When applied, this surfaces the hybrid shape during triage rather than requiring post-triage reconciliation.

**Notes:**
Surfaced during 2026-05-18 triage of Issues #24 and #25. Two items affected:
- `/close` enhancement (Issue #24 recs A, E)
- Memory-mining beat (Issue #25 item 3)
Both were reconciled to "Accept-with-/think" after the maintainer caught the inconsistency.

---

### 2026-04-16 — No implementation standards for Python scripts in the framework

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
The framework now has `lib/export.py` as its first traditional-code artifact (all
prior framework content is prose/markdown). It was written without implementation
standards — hand-rolled error handling, ad hoc exit codes, reactive regex tuning.
The code works but lacks the recognizable character standards produce.

Facebook-moderation's implementation-standards experiments (see
`../facebook-moderation/reference/experiments/implementation-standards/experiment-report.md`)
demonstrated empirically that standards are a bigger lever for code quality than
model capability — Haiku with standards outperformed Opus without standards. The
framework's `lib/export.py` is currently "Opus without standards."

If future `lib/` scripts get added (plugin generators, permission managers, domain
tooling), they'll each be hand-rolled similarly unless a standards document
accumulates. The inconsistency compounds.

**Proposed fix:**
Start with a lightweight Python implementation standards document (~150 lines):
error handling classification, logging conventions, CLI structure, testing
approach. Can grow via the learning-loop pattern facebook-moderation validated.
Best timing: after the NLA writing standards work lands (already in friction log
as short-term task), since the pattern for bringing standards into the framework
will be established.

**Links:** Related to the "Fallingwater preamble" and "re-compile export.py"
entries below. Likely coincides timing-wise with the nla-compiler package install.

---

### 2026-04-16 — /maintain doesn't distinguish prose-code authoring from traditional-code authoring

**Type:** process
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
The current `/maintain` mode handles editing SKILL.md files, design rationale, and
Python scripts with the same posture — read required docs, propose changes, edit.
But prose-code (the documentation that IS the application) and traditional-code
(Python scripts, shell utilities) have different craft disciplines.

Facebook-moderation's `/compile` skill distinguishes sharply: compilation agents
get a specific preamble (Fallingwater), specific required reading (standards,
spec, reference), and specific verification discipline (mandatory execution of
build/typecheck/test). Their model for traditional-code authoring is different
from prose-editing, and deliberately so.

The NLA framework's `/maintain` could develop a parallel distinction: when
authoring traditional code (editing `lib/*.py`, adding new scripts), a different
context should load — implementation standards, a code-authoring preamble,
mandatory verification steps.

**Proposed fix:**
Potentially a sub-mode within /maintain, or a new /compile-like skill once the
nla-compiler package is installable. Not urgent until more traditional code lands
in the framework. Worth revisiting when (a) Python standards exist, (b) the
nla-compiler package is installable, or (c) a second traditional-code file gets
added (pressure from accumulation).

**Links:** Related to "Python implementation standards" above. Best addressed
together once the compiler package is available.

---

### 2026-04-16 — Natural experiment: re-compile lib/export.py through nla-compiler when available

**Type:** process
**Severity:** positive
**Blast radius:** framework
**Status:** deferred

**Observation:**
When facebook-moderation's compiler becomes an installable package (per the
long-term roadmap), `lib/export.py` is a strong candidate for the framework's
first compilation pass.

The artifact exists. The spec exists (`reference/specs/export-service.md`,
drafted 2026-04-16). The author's experience is captured in this session's log —
the script was written as "Opus without standards," and the resulting code is
functional but lacks the character standards produce.

A clean-context compilation through the nla-compiler with Python standards +
Fallingwater preamble + the drafted spec would produce a second artifact.
Diffing the two would be empirical evidence for whether facebook-moderation's
cross-model portability claims extend to Python, and whether the framework
benefits from using its own compilation infrastructure. This is analogous to the
experiment reports' cross-model comparisons, but with the NLA framework as the
consumer rather than a standalone test case.

**Proposed fix:**
Run this experiment when the nla-compiler package lands in the framework.
Doesn't need a specific decision now — it's a noted opportunity.

**Links:** Depends on nla-compiler package availability. Pairs with the Python
implementation standards entry above.

---

### 2026-04-16 — Fallingwater-style preamble for framework's own prose authoring

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
Facebook-moderation's compile preamble (the "Fallingwater" passage at
`../facebook-moderation/app/compile.md` lines 115-148) is the most operationally
specific description of code craft as prose I've encountered. It translates
"vibes about code quality" into instructions an LLM can follow, turning
aspiration into behavioral gradient.

The NLA framework has aspirational language in `core/nla-foundations.md` (e.g.,
"human flourishing" in principle #1) but nothing equivalently strong for *how
the AI should be while authoring framework prose*. When maintaining the
framework, the AI's posture is set by `/maintain`'s procedural instructions, not
by a preamble that shapes craft.

Three options worth thinking through:
1. **Reference:** once the nla-compiler package is installed, have framework
   prose-authoring work load the compile preamble (adapted for prose rather than
   code).
2. **Adapt:** write a framework-specific preamble that adapts the Fallingwater
   framing to prose authoring — "the documentation you write is the application;
   treat it with the care the architect gave Fallingwater."
3. **Originate:** decide that framework's prose authoring has different
   aspirational language than what code compilation needs, and write new
   material from scratch.

**Proposed fix:**
/think session on what aspirational language the framework's maintenance posture
should carry. Probably pairs with the NLA writing standards work (already in
friction log as short-term task) — that work may already touch this territory.

**Links:** Related to NLA writing standards (pending, short-term). Potentially
references or adapts facebook-moderation's compile preamble.

---

### 2026-03-08 — Should /startup disable-model-invocation be false?

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
All skills use `disable-model-invocation: true` to prevent spontaneous invocation.
But `/startup` is arguably the one exception where auto-invocation is desirable — it's
initialization, not a task or mode. You want it to run automatically at session start
without the user remembering to invoke it.

With `disable-model-invocation: false`, the skill description ("Initialize the NLA
runtime. Use at session start") would stay in the active prompt, providing exactly the
nudge needed. This would also reduce redundancy — individual skills currently load
foundations in their own prerequisites because they can't rely on `/startup` having run.

**Open questions:**
- Does Claude Code reliably auto-invoke skills at session start, or would it fire
  unpredictably mid-session?
- Would `/maintain` need to suppress `/startup` to avoid redundant reading, or is
  loading foundations twice harmless?
- The framework itself doesn't need `/startup` (its paths are explicit invocations
  that load their own context). This is a domain project concern only.

**Proposed fix:**
Design session (`/think`) to work through auto-invocation behavior, interaction with
`/maintain`, and whether this is the right exception or whether the blanket rule is
simpler even if imperfect.

---

### 2026-02-23 — Should friction logs be gitignored?

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
The friction log (`reference/friction-log.md`) is committed to git. This works
when user = maintainer, but breaks down when they're different people. A user
who logs friction and pushes creates entries in the project's commit history
that look like development records but are really feedback. Two users logging
friction creates a shared inbox nobody owns. Tentative observations become
permanent history.

The friction log may be better modeled as a personal working buffer (like
`config.md` — gitignored, local). Entries are either processed locally
(`/maintain`) or sent upstream (`/write-letter` or manual sharing). The
resolved *changes* go through git; the log itself is ephemeral.

**Open questions:**
- Working friction logs outside git, archives committed with conflict-safe naming?
- Loss of observation → resolution traceability if the log isn't committed?
  Session logs may be sufficient.
- The framework's own friction log works fine committed (single-maintainer
  context). Is this a domain-project-only concern?

**Proposed fix:**
Design session (`/think`) to work through the implications. Not a quick fix.

**Notes:**
Emerged during design of friction log communication path (startup awareness +
write-letter integration). The communication path works regardless of git
storage, so it was implemented separately.

---

### 2026-02-22 — Context window awareness for session log nudges

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** deferred

**Observation:**
When context grows large, the session log should be updated before auto-compaction
loses detail. A nudge like "your context window is getting large; want to update
the session log?" would catch this naturally. Claude Code's plan mode appears to
have context percentage awareness — unclear whether this is available in normal mode.

**Why we can't fix it yet:**
This depends on Claude Code runtime capabilities, not NLA framework docs. The
framework can't instrument its own runtime. Commit-point syncing (added today)
is the practical substitute — commits happen frequently enough to keep logs current
without needing context awareness.

**Next step:**
Check whether Claude Code exposes context window info that could be used for this.
If not, consider filing a Claude Code feature request.

---

## Patterns to Watch

*Recurring themes that may need deeper attention:*

1. **Two-hop reading** — The LLM reads a wrapper, then a framework file, then domain files. Watch for confusion or context loss in the chain.

2. **Path resolution** — Domain projects use `packages/nla-framework/` paths via submodules. Watch for confusion in the two-hop reading chain when files reference other files within the framework directory.

3. **Intent file completeness** — As the framework evolves, intent files must stay in sync. Track gaps between what `/create-app` needs and what intent files provide.

4. **Language breadth** — Domain-specific language leaking into framework-general docs. The framework was built around a transformation NLA; watch for words that assume transformation, deterministic output, or a specific workflow when the context should be shape-neutral.

---

*This log is maintained by the `/friction-log` skill (which creates entries) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
