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

### 2026-05-06 — Reading accumulated artifacts before /think saves rediscovery

**Type:** process
**Severity:** positive
**Blast radius:** maintainers (immediate); all projects (the pattern generalizes to any NLA)
**Status:** resolved
**Resolved:** 2026-05-06 — Pattern surfaced and applied during this session; documented for future use.

**Observation:**
This session ran /think on the skill-invocation doctrine question and
converged on several findings independently — only to discover that
GitHub Issue #24 (a feedback letter from facebook-moderation) had
captured most of those findings and several more. Reading the issue
*after* /think meant the plan needed substantive rework to incorporate
findings that were already documented.

The maintainer was the one who pointed at the issue (knowing it
existed), so the cost was bounded. But the pattern generalizes: when
considering substantive work on a topic where prior thinking might
exist, *read accumulated artifacts first*. /think extends and stress-
tests existing thinking; it shouldn't reinvent it.

**Generalizable:** Yes. Applies to any maintenance work where prior
artifacts (feedback log, friction log, design rationale, related
GitHub issues) might capture relevant thinking. Cost: a few minutes
of reading. Value: variable but can be large (the letter saved us
from a plan missing three sections).

**Operational gap noticed:** The /maintain session-start prompt reads
the *post-triage* feedback log. Open GitHub Issues that haven't been
triaged yet are invisible at session start. Issue #24 was filed
2026-05-05 (one day before this session) and hadn't been triaged —
so it was on GitHub but not in the feedback log. Two possible fixes:
(a) maintainer remembers to run `/check-feedback` discovery
(no triage) at session start when substantive work is on deck; or
(b) /maintain's session-start adds a quick `gh issue list` check
alongside the feedback log read. The second feels procedurally
right but lives outside this entry's scope.

**Affected files:**
- `core/skills/maintain.md` (potentially — Session Start)
- Possibly the Working Rhythms section in `core/nla-foundations.md`

**Proposed fix:**
Two adjacent fixes:
1. Update /maintain's Session Start to scan open GitHub issues, not
   just the feedback log. Lightweight check (`gh issue list --state
   open --limit 20`); maintainer decides whether to triage now or
   defer.
2. Document the broader principle in foundations: before /think on
   substantive work, scan accumulated artifacts for prior thinking.
   Potentially fold into the "improvement loop" working rhythm or
   a new "validation flow" rhythm (see related entry on
   experimentation methodology).

**Notes:**
- Related to "Framework lacks documented experimentation methodology"
  entry below (the meta-question about formalizing methodology).
- Maintainer's framing: "I sent the feedback letter myself, and I
  knew we were missing key parts of the plan, which is why I wanted
  you to read the full letter." So the maintainer was operating as
  an informed session-manager (Issue #24 item 8); the cost would be
  higher in sessions without that human-in-the-loop awareness.

---

### 2026-05-06 — Bulk Edit calls don't parallelize when system reminders fire between each

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** pending

**Observation:**
This session migrated 21 framework wrappers as part of the skill-
invocation convention adoption. The intent was to send batches of
Edit calls in parallel — a single assistant message with multiple
Edit tool uses — to amortize cost across edits. In practice, each
Edit triggered a system reminder showing the updated skill listing,
which ended my turn. Net result: 21 sequential edits, not parallel
batches.

This isn't a framework problem — it's a Claude Code harness behavior.
But it's worth flagging because:
- The framework's `/maintain` discusses parallel tool use generally
  in its principles ("call multiple tools in a single response"); a
  reader might assume bulk edits parallelize when they don't always.
- For bulk edits specifically, a different shape might work better —
  e.g., Write-based file rewrites for files where changes are
  substantial enough that the entire file is being replaced anyway,
  or a single Bash sed/awk pipeline for mechanical pattern
  substitutions.

**Before:** Bulk wrapper edits via Edit tool ran sequentially despite
parallel intent. Took longer than expected for a mechanical change.
**After:** Bulk-edit work uses the right shape per case — Write for
substantial rewrites, Bash for mechanical substitutions, Edit for
surgical changes — and doesn't assume parallelism for cases where
the harness will interrupt.

**Confirmed reason:**
System reminders that fire after tool use end the current assistant
turn. For tools that update state visible to the AI (e.g., the
SKILL.md edits update the Skill listing in the active prompt), the
reminder fires every time. For other tools (e.g., Read, Bash) the
reminder may not fire on every call. The "parallel tool use"
principle is true for non-state-updating tools; it has limits for
state-updating ones.

**Affected files:**
None directly. This is harness behavior. Worth a possible feature
request to Claude Code (consolidate state-update reminders across
batched edits in a single turn).

**Proposed fix:**
1. Note in `core/skills/maintain.md` (or wherever bulk-edit work is
   discussed) that bulk wrapper migrations should use Write or Bash
   shaping rather than expecting parallel Edit calls.
2. File a Claude Code feature request (separate from framework
   maintenance work) about reminder consolidation for batched
   state-updating tools.

**Notes:**
- Surfaced during this session's wrapper migration. The 21 wrappers
  took longer to update than they should have because each Edit
  ended a turn rather than batching.
- Severity is minor because the work completed correctly; only the
  pacing was off. But for larger bulk migrations (e.g., a domain
  project with 30+ wrappers), the pattern would scale poorly.
- Related to but distinct from the experimentation methodology entry
  — that's about empirical validation; this is about mechanical bulk
  edits. Both are about doing maintenance work efficiently but at
  different stages.

---

### 2026-05-06 — Controlled prose experiments validated the skill-invocation doctrine refinement

**Type:** process
**Severity:** positive
**Blast radius:** maintainers (immediate); all projects (methodology generalizes)
**Status:** resolved
**Resolved:** 2026-05-06 — Experiments ran (Layers A-D + T1-T5 + calibration); framework wrappers migrated to new convention; full writeup at `reference/experiments/skill-invocation-discipline/experiment-report.md`. Plan for downstream publication at `reference/plans/skills-doctrine-publication.md`.

**Observation:**
A controlled prose-experiment methodology produced empirical findings
that reasoning alone wouldn't have surfaced. The experiments tested
whether constraint-bearing skill description language disciplines AI
invocation behavior — a question where the framework had a documented
prior decision (`disable-model-invocation: true` on all skills) and
proposed reversing required evidence proportional to the original
concern.

The shape that worked: hypothesize → isolate variable → cold-context
agent → binary signal (filesystem state) → iterate or commit. Each
test cycle was ~30 seconds + analysis. Total experimental cost across
all layers and calibrations: ~30-45 minutes. One finding (Layer C)
disconfirmed an assumption we'd otherwise have shipped.

The methodology pattern is the more durable contribution. Future
prose-as-code work in the framework — doctrine changes, convention
shifts, skill template revisions — could benefit from the same shape.
See report Section 4 ("Cross-Cutting Findings") for the methodology
findings beyond the immediate doctrine question.

**Generalizable:** Yes. The pattern is "controlled experiments on
prose-as-code." Applies whenever a prose change has downstream impact
and reasoning alone leaves uncertainty. The experiments worked in this
domain (skill descriptions); they should generalize to others (CLAUDE.md
prescriptive language, intent file conventions, skill template shapes,
etc.).

**Notes:**
- The cold-context review methodology (two-pass: simulation + frame
  question) is a related but distinct contribution surfaced by this
  work. Issue #24 introduced it; our experiments validated its value
  in a different domain. Worth surfacing in the same writeup but
  conceptually separate from the prose-experiment methodology.
- See companion friction-log entry: "Framework lacks documented
  experimentation methodology" (the meta-question of whether to
  elevate this pattern to framework-level guidance).
- The experiment report itself (~600 lines) is the durable artifact;
  this friction log entry is the pointer.
- Mistakes worth flagging (full list in report Section 6): the initial
  test design conflated visibility and constraint; we almost shipped
  pilot-skill testing instead of production-form testing; a
  rules-vs-intent slip on audit design needed correction. The user-as-
  session-manager pattern (Issue #24 item 8) was load-bearing
  throughout.

---

### 2026-05-06 — Framework lacks documented experimentation methodology

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
The NLA Framework documents four working rhythms in
`core/nla-foundations.md`: the improvement loop, the design flow, the
update cycle, and session structure. None of these cover empirical
validation of prose-as-code claims between hypothesis and commit.

This session's prose experiments
(`reference/experiments/skill-invocation-discipline/experiment-report.md`)
ran ad-hoc. They worked. But the methodology isn't documented and
isn't discoverable for future work. The next time someone considers
a doctrine change, convention shift, or any prose-as-code change with
downstream impact, they'd have to either (a) reinvent the methodology,
(b) find this experiment report and copy the pattern, or (c) skip the
empirical step and rely on reasoning alone.

**Before:** Prose-as-code changes go directly from /think to plan to
commit. Empirical validation between hypothesis and commit is ad-hoc
when it happens at all. Cold-context review (the related but distinct
practice of reviewing artifacts before commit) is similarly undocumented.

**After:** A documented "validation flow" — possibly as a fifth working
rhythm — describes when and how to test prose-as-code claims
empirically. Cold-context review (two-pass: simulation + frame question)
is similarly documented. Both compose with existing rhythms (improvement
loop, design flow) without replacing them.

**Confirmed reason:**
The framework's current rhythms reflect what was true when they were
documented. The prose-experiment pattern is newer (this session is
where it surfaced as a generalizable pattern, though Issue #24 from
facebook-moderation introduced related methodology). The framework
hasn't yet absorbed it.

**Affected files (proposed):**
- `core/nla-foundations.md` Working Rhythms section
- Potentially a new core skill (e.g., `core/skills/run-experiment.md`)
  or fold guidance into existing skills (`/think`, `/maintain`)
- `reference/design-rationale.md` for the rationale entry

**Proposed fix:**
Sized appropriately, probably a /think session followed by maintain
work in a separate session. Specific shape to explore:

1. **Validation flow** as a fifth working rhythm in foundations.
   Tentative wording: "Hypothesize → design experiment → test in cold
   context → measure → iterate or commit. Used when prose changes
   have downstream impact and reasoning alone is uncertain."

2. **Cold-context review pattern** documented separately. Two-pass
   distinction (simulation + frame question) is load-bearing per
   Section 4.2 of the experiment report.

3. **Skill or sub-skill** for facilitating experiments? Could be
   `/run-experiment`, or could be folded into `/think` as a phase. The
   shape depends on how often the pattern fires; this is the design
   judgment to settle in /think.

Don't decide all three at once. The minimum viable change is documenting
the patterns (in foundations + design rationale) so future maintainers
can find them. Skill-level affordances are optional add-ons.

**Notes:**
- This is the meta-version of the previous entry. The previous entry
  documents that the experiments paid off; this entry asks whether to
  elevate the methodology to framework-level guidance.
- Related to Issue #24 (recommendations B and F about handoff template
  and session-bracketing rhythm); consider triaging together.
- Worth checking facebook-moderation's `reference/experiments/` pattern
  for prior art on directory structure and report format. Our first
  experiment report (`reference/experiments/skill-invocation-discipline/`)
  borrows that pattern.
- Tag for cross-reference: the rules-vs-intent slip flagged in the
  experiment report's Section 6 is itself a meta-pattern about
  defaulting to rules where intent is appropriate. Worth watching
  during framework methodology work specifically.

---

### 2026-05-04 — Multi-file maintenance: cross-references demand the referenced file ship first

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** pending

**Observation:**
During the Phase 3 writing-standards session, the original implementation
plan put `core/skills/maintain.md` first and `core/skills/validate-standards.md`
second. Catching the dependency happened just before executing — `maintain.md`
ends with "use `/validate standards`" as its diagnostic-use pointer, so a
commit that landed `maintain.md` first would have shipped a reference to a
file that didn't yet exist. The order was reversed mid-execution; nothing
broke.

But the plan had no surfacing step for it. The /maintain proposal flow
asks for blast radius, scope, and approval — it doesn't ask "do these
files reference each other, and if so, what order do they need to land
in?" When multi-file work cross-references, write the referenced file
*before* the file that refers to it; otherwise an interim commit ships
a broken reference.

**Confirmed reason:**
The implementation order was driven by perceived size ("smaller,
foundational change first"), not by dependency direction. Size and
dependency aren't the same axis. The relevant question is which file
references which, not which file is shorter — but the planning step
didn't ask the right question.

**Affected files:**
- `core/skills/maintain.md` (Confirm Before Implementing or Pre-flight Review section)
- Possibly the planning-mode guidance in the same file

**Proposed fix:**
Add a quick check to the Pre-flight Review (or Confirm Before
Implementing) section: "For multi-file work, identify cross-references
and write referenced files first. Each commit should be internally
consistent — interim commits with broken references are friction even
if the final state is fine." One sentence in a checklist.

**Notes:**
The session caught it organically because the AI was reading both
files' content while drafting. In sessions where one file is "settled"
and another is being authored, this is easier to miss. Worth flagging
because the cost of catching it post-commit (interim broken reference,
order-of-events confusion in git history) is annoying enough that the
sentence-level prevention earns its place.

---

### 2026-05-04 — Resolved-but-unarchived log entries drift across sessions

**Type:** process
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
At the start of the 2026-05-04 session, the active feedback log carried
seven 2026-04-15 entries that had been marked resolved during that
2026-04-15 session but were never archived. They sat in the active log
for ~3 weeks across multiple intervening sessions. None of those
sessions had a reason to archive them — each focused on its own work —
and the drift was silent.

The /maintain Common Tasks section covers archival ("Archive resolved
entries") *as part of processing an entry*. Entries resolved during a
session that doesn't immediately archive them fall through. There's no
session-end prompt that catches the gap.

**Before:** Active feedback log accumulating resolved-but-unarchived
entries silently across sessions; new session start has to notice the
drift to address it.

**After:** Session close (or session start) catches the drift cheaply
without requiring the maintainer to remember.

**Confirmed reason:**
The procedural rule lives at the wrong moment. "Archive when you
resolve" only fires if the resolver is also archiving. A different
person in a future session — or the same person picking up after
hours — has no procedural prompt to do it. The natural moment to catch
this is /close (or the session-start summary in /maintain), where the
maintainer is already looking at log state.

**Affected files:**
- `core/skills/close.md` (Loose Ends section)
- Possibly `core/skills/maintain.md` Session Start (already counts
  resolved-unarchived friction entries — could extend to feedback log)

**Proposed fix:**
Add a Loose Ends item to /close: "Check for resolved-but-unarchived
entries in `reference/friction-log.md` and `reference/feedback-log.md`.
If any exist, offer to archive them now — the procedure step in
`/maintain` only fires during the session that resolves an entry, so
entries resolved without immediate archival drift across sessions."

**Notes:**
Different from the 2026-04-17 `settings.local.json` drift entry but in
the same family — small drift that accumulates silently because no
procedural prompt fires at the right moment. The /maintain Session Start
already mentions resolved-but-unarchived friction entries; extending
that or mirroring it in /close would cover both logs.

---

### 2026-04-18 — Shippability convention reads as per-commit tagging; session-end is better

**Type:** process
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
During the 2026-04-18 writing-standards session, I tagged the first
consumer-facing commit (the `/maintain` broadening work) as v0.0.5 mid-session,
with more consumer-facing work planned for the same session. The user pushed
back: jumping 0.0.4 → 0.0.5 → 0.0.6 → 0.0.7 in a single session inflates
version numbers without making each tag more meaningful. Downstream consumers
would rather see "v0.0.5 = one session of writing-standards-related work"
than three incrementally-numbered tags of the same arc of work.

The `core/skills/maintain.md` Shippability section as currently written —
"If yes → tag the commit (if the project uses tagged releases)" — reads as
per-commit tagging. The operative rule works correctly (consumer-facing
content gets tagged); the *timing* doesn't distinguish "tag each commit" from
"tag a meaningful release." Per-commit tagging was the literal
interpretation; session-end (or "explicit release moment") tagging is what
the downstream consumer actually benefits from.

**Confirmed reason:**
User's framing: "It just seems weird to potentially jump up from 0.0.4 to
0.0.7 in this session alone (if we go to 0.0.6 after pass 1 and 0.0.7 after
pass 2)." The version number should track meaningful release cadence, not
commit cadence. A session is a natural unit: one arc of work, one set of
changes a consumer should review together, one tag.

Related: the 2026-04-17 session's debrief already carried a gentle tension
about tagging choice ("reassess after a few more sessions if the pattern
recurs"). This is the recurrence.

**Affected files:**
- `core/skills/maintain.md` (Shippability at Commit Time section)
- `install/package-intent.md` (package-specific pointer, per 2026-04-17 session)

**Proposed fix:**
Refine the Shippability guidance to separate the *what-to-include-in-tag*
question (consumer-facing content) from the *when-to-tag* question. Rough
direction:
- The commit-time decision stays: "does this commit touch consumer-facing
  content?" determines whether the work belongs in the next release.
- The tagging-time decision is separate: tag at meaningful release moments
  (typically session end, or when a consumer-facing arc of work is
  complete), not per-commit. Update-notes entries can still land per-commit
  — they're a running changelog, not a release marker.
- Update-notes per consumer-facing commit still makes sense (changelog
  granularity); it's the tag that should be release-grained.

Scope for a future `/maintain` to work through — this friction log entry
captures the observation; convention refinement happens when processed.

**Notes:**
- Mid-session local v0.0.5 tag was deleted (it wasn't pushed). The
  2026-04-18 session will tag at end, once, for all its consumer-facing
  work.
- Worth checking how the per-commit vs. release-moment distinction interacts
  with `/update`'s tag-check behavior (install.md "Pin to a Tagged Release"
  and update.md's fast-forward tag offer) — the tag-check pattern assumes
  tags mark stable release points. Batched session-end tagging matches that
  assumption better than per-commit tagging does.

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

### 2026-03-25 — settings.local.json accumulates junk instead of systematic permission entries

**Type:** process
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-04-15 — Architectural change: the packages/ submodule model eliminates cross-directory reads entirely, making Read permission entries and settings.local.json generation for them unnecessary. The symlink investigation is also closed — symlinks are ruled out (test data from Issues #15, #16 confirmed they add friction rather than removing it).

**Observation:**
The permission management model (designed 2026-03-04) envisioned clean, systematic
entries like `Read(../nla-framework/**)` generated by `/create-app`, `/install`, and
`/update`. In practice, the framework's own `settings.local.json` contains a junk
drawer of individually approved commands — entire commit messages, shell loop fragments,
broken entries — accumulated from one-off approvals over time. No systematic Read
permission entries for sibling directories exist.

The user reports "tons of permissions messages" despite having updated their NLAs. The
generation lifecycle (create → install → update → validate) either never ran for
existing projects, or the generated entries don't match what Claude Code actually checks.

**Before:** Permission model designed but not delivering friction relief in practice.
**After:** Clean permission entries that actually eliminate cross-directory prompts.

**Related discovery:**
Symlinks within the project directory bypass Claude Code's permission checks entirely.
A symlink at `dependencies/nla-penny-post` → `../nla-penny-post/` allows reads through
the logical path with no permission prompt. Tested 2026-03-25 from the framework project.
Test letters sent to 5 domain projects to gather broader data.

**Open questions:**
- Is the generation logic in `/create-app` and `/update` actually producing the entries?
- Does Claude Code's permission pattern matching support `Read(../nla-framework/**)`?
- Would symlinks be a more reliable solution than settings-based permissions?
- Why did direct reads to sibling directories also work without prompts from the
  framework project? (Permission mode specific? Accumulated one-off approvals?)

**Affected files:**
- `install/install.md` — permission declarations
- `.claude/skills/create-app/SKILL.md` — settings generation
- `core/skills/install.md`, `core/skills/update.md` — permission proposal logic

**Proposed fix:**
Awaiting test results from domain projects (Issues filed 2026-03-25). Once data is in,
either fix the settings generation pipeline or pivot to a symlink-based architecture.

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

### 2026-03-04 — Plan agent proposed cross-project edits that contradicted /think design

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-03-04 — Reverted package edits, logged pattern.

**Observation:**
During implementation of the permission management model, the Plan agent proposed
directly editing sibling package manifests (penny-post, process-helpers). This
contradicted the design from the /think session, which explicitly established that
packages learn about permission declarations through `/update` from the framework —
not through direct cross-project edits by the framework maintainer.

The changes were implemented before the human caught the contradiction.

**Root cause:**
Two contributing factors:

1. **Plan agent lacked design context.** The Plan agent received a summary of
   decisions but not the reasoning behind the migration flow design. It optimized
   for completeness ("these packages need permissions sections") rather than
   honoring the principle that each project adopts changes through its own update
   channel.

2. **Review gap between /think and plan.** When reviewing the Plan agent's output,
   the AI checked for mechanical correctness (right files, right format) but didn't
   verify each step against the /think design principles. The contradiction was
   between a design-level decision (migration flows through /update) and an
   implementation step (directly edit packages) — a category mismatch that
   mechanical review doesn't catch.

**Generalizable pattern:**
When a /think session establishes *how changes flow between projects*, the
implementation plan must respect those flow decisions. Direct cross-project edits
bypass the update channel that was designed precisely for this purpose. This is
also a "Context Determines Competence" issue — changes to a package's manifests
are judgment operations that should happen in that package's own maintenance
context.

**Proposed fix:**
When writing implementation plans after a /think session, explicitly check each
proposed cross-project edit against the /think design: "Does this change belong
in the current project's context, or should it flow through /update?" Add this
as a pre-flight check item in the maintain skill.

---

### 2026-02-23 — /create-app bare project path: missing guidance and speculative seeds

**Type:** intent
**Severity:** minor
**Blast radius:** project generation
**Status:** pending

**Observation:**
When a user requests a bare project (no tasks, minimal domain input), `/create-app`
has two gaps:

1. **No explicit edge case for zero tasks.** The skill's "Conversation Edge Cases"
   section handles "complex project with many tasks" (defer some, generate a few) but
   doesn't address zero. The skill was adapted on the fly — empty task tables in
   overview, stubs in shared context — and it worked, but the zero-task case isn't
   documented as a valid path.

2. **Speculative seeds despite minimal input.** With only "facebook moderation" and
   "bare" as input, the skill still generated voice ("neutral, not robotic") and values
   ("accuracy over speed") files with substantive content. These are reasonable guesses
   for moderation, but they're guesses. Risk: when the user runs `/maintain` later, these
   seeds may feel authoritative enough to build on rather than question. The alternative —
   truly empty stubs — would force that conversation but give `/maintain` less to work with.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — "Conversation Edge Cases" section

**Proposed fix:**
Add a "Bare project" edge case: when the user explicitly requests no tasks, generate
the full framework structure with minimal shared context stubs. For the speculative
seeds question, consider adding a note in generated voice/values files that's stronger
than "refine with /maintain" — something like "These are starter assumptions based on
the domain name. Review before building on them."

**Notes:**
Surfaced during debrief after creating `facebook-moderation` as a bare project.
The generation succeeded — this is about making the path explicit rather than fixing
a failure.

**Additional observation (2026-02-24, nla-writer creation):**
The task assumption runs deeper than the edge cases section. Phase B's follow-up
groupings, Phase C's summary template, and the file generation tables all thread
tasks through as a core structural element. With zero tasks, the generator adapts
each section independently — empty task tables, skipping domain skill generation,
adjusting the summary format. Works, but requires judgment at every step rather
than following instructions.

Separately: when rich domain context exists (as with nla-writer — extensive
writings, a model project in duet, values from AMG), the "speculative seeds"
concern inverts. The shared context files (values, voice, patterns) are
well-informed, not guesses. The risk shifts from "seeds feel authoritative" to
"seeds are good enough that the user never revisits them." May warrant different
guidance for blank-but-context-rich vs. blank-and-context-sparse projects.

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
