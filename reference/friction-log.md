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

### 2026-03-03 — Framework maintain skill can't use thin wrapper pattern

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
The framework's own `.claude/skills/maintain/SKILL.md` is a full custom version
rather than a thin wrapper to `core/skills/maintain.md`. The core file assumes domain
project context — hardcoded paths like `app/overview.md`, `app/shared/values.md`,
`reference/system-status.md`. The framework doesn't have these, so it maintains a
parallel version with adjusted targets.

This creates a sync burden: structural changes to the session log format, common tasks,
or session lifecycle steps need to be applied to both files. The framework is an NLA
itself — it should be able to use its own patterns.

**Root cause:** The core maintain skill is written in "code style" (prescriptive paths)
rather than "NLA style" (described intent). "Read `app/overview.md`" could be "read
your project's overview document." The AI resolves the right path in any context.

**Possible approaches:**
- Broaden language in `core/skills/maintain.md` until the framework can thin-wrap it
- Rename/move core files to match the `app/` convention the skill assumes
- Some combination

**Re-prioritized 2026-04-17:** Status bumped from deferred to pending after the
2026-04-17 session added to the dual-maintenance surface (Writing Standards
section dual-applied to both files). The user flagged that the sync burden is
getting more annoying and estimated the broadening fix at 5–10 minutes. Next
session candidate — pairs naturally with #21 Phase 2 work or can be done
independently.

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
