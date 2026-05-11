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

### 2026-05-11 — /create-app's structured Q&A misses the collaborative-refinement mode

**Type:** core
**Severity:** minor
**Blast radius:** all projects (project generation)
**Status:** pending

**Observation:**
During /create-app for nla-archetypes (2026-05-10), the most consequential design
decision in the generated project did not emerge from any structured Phase A/B
question. The decision was the third value — "true like fiction, not like a
transcript," the Guernica anchor that resolves the productive tension with
the grounding value. It emerged because the user explicitly invited
collaboration twice:

1. At the project description (Phase A response): "I'm also interested in
   your thoughts, ideas, concerns or questions."
2. Mid-design, after I proposed two values: "Another candidate: true to life
   as in the way good fiction feels true... I'm not sure how to express that
   as a value exactly. Maybe you can help?"

The Phase B grouping suggestions ("voice + audience," "values/tradeoffs as a
single lightweight question," etc.) frame the AI's job as *extracting* domain
requirements via structured Q&A. That framing fits a user providing
requirements from scratch. It underperforms when the user arrives with rich
conceptual work — a working prompt, a developed framing, half-formed
intuitions — and the AI's job is *translation into NLA structure* rather
than extraction.

In the translation case, the high-value mode is collaborative refinement:
the AI proposes shape, names the gaps, asks for pushback, helps articulate
what the user can feel but hasn't named. That's what happened on the
Guernica value. It wouldn't have happened if I'd followed Phase B
mechanically through its question groupings.

**Confirmed reason:**
Phase A is genuinely open-ended ("What are you building? Accept anything from
a one-liner to a full paragraph.") and accepted the user's rich prompt
cleanly. But Phase B's structure assumes the next move is to fill remaining
fields via targeted Q&A, not to enter a collaborative-refinement mode. The
existing "user provides everything upfront → skip to Phase C" edge case
covers the *requirements-already-given* case, but not the
*conceptual-work-rich-but-design-choices-unresolved* case. In that
intermediate state, neither Q&A nor skip-to-summary is right; collaborative
refinement is.

**Affected files:**
- `core/skills/create-app.md` — Phase A → Phase B transition; the
  Conversation Edge Cases section ("User provides everything upfront") could
  grow a sibling entry for "User arrives with rich conceptual work."
- Possibly `install/CLAUDE-intent.md` or `core/nla-foundations.md` — the
  collaborative-vs-extractive mode-recognition is a general AI posture that
  applies beyond create-app. /maintain has analogous moments
  (refining-a-doc vs. extracting-new-doc-requirements).

**Proposed fix:**
Two complementary moves:

1. In `core/skills/create-app.md`, after Phase A and before Phase B, add a
   mode-recognition step:

   > Before targeted follow-ups, recognize what mode the user is inviting.
   > If their Phase A response is mostly *requirements* (what tasks, what
   > audience, what voice), proceed to Phase B as written — extraction is
   > the right mode. If their response carries rich conceptual work
   > (a working prompt, a developed framing, half-formed intuitions) and
   > invites your perspective explicitly or implicitly, shift to
   > collaborative refinement: propose shape, name gaps, invite pushback,
   > help articulate what the user can feel but hasn't named. Phase B's
   > structured questions still apply for genuinely missing fields, but
   > the conversation should lead with refinement, not extraction.

2. Add a Conversation Edge Cases entry — "User arrives with rich conceptual
   work" — describing the pattern and pointing to the mode-recognition
   guidance.

**Notes:**
- Related to archived entry 2026-02-21 "Reflection after execution produces
  high-quality feedback" (resolved by creating /debrief). Same shape — open
  invitation to reflection/collaboration produces high-value output that
  structured Q&A doesn't — but at a different moment. That entry was about
  reflection *after* execution; this one is about collaboration *during*
  design. /debrief carved out the post-execution slot; this would carve out
  the mid-design slot inside /create-app.
- Distinct from the 2026-05-10 AskUserQuestion entry — that's about
  tool-choice (enum vs. prose) at any conversational moment. This is about
  whole-mode-recognition: when to enter collaborative refinement vs.
  structured extraction. Both pull in the same direction but address
  different layers of the problem.
- The framework addenda apply: this is a `core/skills/` change with reach
  to every domain project's generation, since /create-app is the entry
  point for every new NLA.
- Possible test of the fix: re-read the nla-archetypes transcript and
  check whether the mode-recognition step would have fired correctly on
  the Phase A response (a working extraction prompt + explicit invitation
  to AI thoughts). Should be a clean yes.

---

### 2026-05-10 — AskUserQuestion overreach despite user-private memory note

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
During `/create-app` for nla-archetypes (this session), I invoked Claude Code's
`AskUserQuestion` tool twice for design questions that were "yes-but"/"yes-and"
shaped — questions where the user's likely response was a layered refinement
("yes, but with this addition"), not a discrete pick among mutually exclusive
options. Both invocations were rejected by the user, who reminded me that
prose would be the right format. The user flagged the pattern explicitly:
"You're an AI not a python interpreter so you can (and should) handle more
nuance than can be given by an enum."

Specifically:
- First invocation: three questions (output voice, source format, output
  destination) — each was "could be either" or "depends" shaped.
- Second invocation: similar three-question pattern after the user had
  already clarified the Guernica value and AI-optimized voice direction.

I had a memory note (`feedback_prose_over_enum_for_decisions.md`) from prior
sessions saying exactly this pattern was wrong. The note did not prevent
the lapse — the structured affordance of AskUserQuestion appears strong
enough that user-private memory isn't sufficient mitigation.

**Confirmed reason:**
[Per user] AskUserQuestion fits genuinely discrete clarifications but is
wrong for "yes, but"/"yes, and" shaped decisions. When a question is
layered (refinement, addition, partial agreement), prose lets the user
respond in the shape of the actual decision; enum forces them into a
shape that pre-judges it. Memory notes alone don't prevent the lapse —
the tool's affordance is attractive, and the memory note isn't loaded
into the system prompt the way framework CLAUDE.md or core skill
guidance would be.

**Affected files:**
- `install/CLAUDE-intent.md` — could add framework-level guidance about
  defaulting to prose for design questions; this propagates to every NLA's
  CLAUDE.md via /create-app and /update.
- `core/skills/create-app.md` — Phase B and Phase C currently assume prose
  conversation but don't say so explicitly enough to overcome
  AskUserQuestion's pull. Adding an explicit "default to prose for
  follow-ups; AskUserQuestion only for genuinely discrete clarifications"
  in those sections would fire at the lapse-prone moment.
- Possibly `core/skills/maintain.md`, `core/skills/think.md` — anywhere a
  skill invites multi-turn design conversation could carry the same default.

**Proposed fix:**
Add framework-level guidance, probably in `install/CLAUDE-intent.md`
("Execution Principles" or similar), along these lines:

> When asking the user a follow-up question, default to prose. Tools that
> force enum-style choices (Claude Code's `AskUserQuestion`, similar
> affordances) are appropriate only for genuinely discrete clarifications
> with mutually exclusive answers — never for layered design decisions
> where the user's likely answer is "yes, but" or "yes, and."

Complementary: `core/skills/create-app.md` (and conversation-heavy skills
generally) could state the default explicitly in their Conversation Flow
sections — the lapse-prone moments are where the guidance needs to fire.

**Notes:**
- Related-but-distinct from archived entry 2026-02-21 "Plan mode kept
  pushing toward decisions (AskUserQuestion with multiple choice options),"
  resolved by creating `/think`. That entry addressed plan-mode/design-
  exploration specifically. This one is broader: AskUserQuestion overreach
  across general conversational skills, not just plan mode. The /think
  refuge alone doesn't address the default-tool-choice problem in skills
  like /create-app and /maintain.
- The lapse happened despite the user's existing memory note — evidence
  that memory-only mitigation is insufficient for tool-default behaviors.
  This argues for moving the guidance into framework docs that every
  session loads.
- Affects all projects because the AskUserQuestion pull is a property of
  Claude Code itself, present in every NLA's runtime. Per the framework
  addenda: this is a `core/` (and `install/`) change with all-domain-
  project reach.
- This also relates to the active "Patterns to Watch" item #4 — language
  breadth, when defaults assume one shape (here: enum-shaped questions)
  when the situation needs another.

---

### 2026-05-07 — Borrowing patterns from sibling NLAs requires reading the actual artifact

**Type:** process
**Severity:** positive
**Blast radius:** maintainers
**Status:** pending

**Observation:**
The Structure Decisions Protocol borrowed shape from
facebook-moderation's compile-time `build-guide.md` (attribution per
entry, Judgment notes, Decision Sources table). The borrowing was
high-leverage — but only after the actual artifact was read. Earlier
in the session, hearing "facebook-moderation has a build-guide" wasn't
the same as reading it. The texture (the specific table shape, the
wording of Judgment notes, the integration with the compile workflow)
only became real after I read the file directly.

This connects to the now-archived 2026-05-06 entry "Reading accumulated
artifacts before /think" but extends it to a different scale. That
entry was about prior thinking *within* the project (feedback log,
friction log, design rationale, related GitHub issues). This is about
*sibling-project artifacts* when borrowing patterns. Same lesson at
a different scope.

**Generalizable:** Yes. When considering pattern-borrowing from another
NLA, read the actual artifact (not just descriptions of it) before
designing the borrow. Cost: minutes. Value: the texture of the
borrowed shape, which descriptions don't carry.

**Affected files:**
- `core/skills/think.md` (Prior Art section) — could extend the existing
  "check design rationale, session archives, friction log" guidance to
  include "and read sibling-project artifacts when borrowing patterns."

**Proposed fix:**
Small extension to /think's Prior Art section. One sentence about
reading sibling-project artifacts, not just descriptions.

**Notes:**
- In this session, the maintainer pointed at the file ("read this
  build-guide before /think"). Without that prompt, the pattern-
  borrowing might have proceeded with description alone — losing
  the texture.
- Connects to maintainer-as-session-manager pattern (Issue #24 item 8).
- Could also be captured as a memory entry; the friction log captures
  the observation, processing decides where it lives durably.

---

### 2026-05-07 — Plan agent conservatism is a calibratable input, not a verdict

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** pending

**Observation:**
During this session's plan-mode review, the Plan agent recommended
cutting Steps 5–7 to a follow-up session. The rationale was
fresh-eyes risk-aversion (calibration risk if experiments surface
wording issues; cross-reference ordering complexity; ceremony). The
maintainer pushed back, asked for concrete pros/cons, and we landed
on full scope with conditional Step 7 (abort criteria explicit). The
full scope worked — all four hypotheses validated cleanly and Step 7
shipped.

The Plan agent's advice was useful for surfacing concerns and gaps
but conservatively calibrated on scope. It reflected the agent's own
uncertainty under cold context, not an expert read on whether the
plan could succeed in one session. The right move was to treat the
Plan agent's recommendations as *one input* — to be weighed against
explicit pros/cons and possible mitigations — rather than as a verdict
to follow.

**Generalizable:** Yes. Plan agent reviews are valuable for surfacing
concerns and gaps. They're less reliable for scope-cut recommendations
because they default to risk-aversion under uncertainty. When a Plan
agent recommends cutting scope, the maintainer should: (a) extract the
specific concern (e.g., "calibration risk if experiments fail"),
(b) design an explicit mitigation (e.g., abort criterion), (c) decide
based on the mitigation, not the original cut recommendation.

**Affected files:**
- `core/skills/maintain.md` (Pre-flight Review section, where Plan
  agent reviews are discussed)
- Or a memory entry about plan-mode interaction patterns.

**Proposed fix:**
Light-weight: one sentence in maintain.md's Pre-flight Review section
or planning-mode guidance: "Plan agent scope-cut recommendations
default to risk-aversion under cold context; treat them as input,
design explicit mitigations for the underlying concerns, and decide
based on the mitigations."

**Notes:**
- This session's full-scope choice with Step 7 abort criterion validated
  the calibration insight. Real outcome data, not just hypothesis.
- The Plan agent was *right* about the underlying concerns (calibration
  risk, cross-reference ordering). It was wrong about the recommendation
  to cut. The concerns deserved mitigations, not avoidance.

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

**Update 2026-05-07 (alternative resolution pattern surfaced):** The
2026-05-07 Structure Decisions Protocol session sidestepped this issue
by landing all cross-referenced files in a *single coherent commit*
(commit 68c145a — `core/structure.md`, the design-rationale entry it
cites, the CLAUDE.md section that references it, and the foundations.md
mention all in one). Single-commit atomicity is often easier than
ordering discipline for cross-references — if all referenced and
referrer files can land together, the interim-broken-reference problem
doesn't arise. Worth incorporating into the eventual fix: the proposed
checklist could offer "land cross-referenced files in one commit" as
the simpler path, with "if they must split, write referenced files
first" as the fallback. Status remains pending — the proposed checklist
itself hasn't been added; this note captures a complementary pattern.

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
