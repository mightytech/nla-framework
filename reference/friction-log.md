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

### 2026-11-12 — core/structure.md is internal content inside a consumer-facing path

**Type:** process
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** pending

**Observation:**
Surfaced while committing two small fixes in the 2026-11-12 session. One removed
a phantom `lib/.gitkeep` row from `core/structure.md`. Deciding whether that
commit needed an update-notes entry exposed a seam in the shippability rule.

The rule in `core/skills/maintain.md` § "What counts as consumer-facing" is
path-shaped:

> - **For the framework:** `core/` or consumer-facing `install/*.md`.

`core/structure.md` is in `core/`, so the letter of the rule says
consumer-facing → update-notes entry. But the file records the *framework's own*
as-built directory layout. Domain projects keep their equivalent record in
`app/overview.md` § "Where Things Live"; they never read the framework's. An
update note reading "removed a phantom `lib/.gitkeep` row from the framework's
structure record" is precisely what the same section calls noise:

> If only internal — the project's own `reference/` … — skip the note.
> Consumers see the submodule pointer advance but have nothing to review.

So the file's *location* says ship it and the file's *content* says don't.

**Resolution taken this session:** treated as internal — no update-notes entry,
no tag. The maintainer confirmed. Recording it because the next maintainer
touching `core/structure.md` will hit the same fork, and the rule as written
points the wrong way.

**Confirmed reason:**
The path-shaped rule was a deliberate simplification — paths are checkable and
intent is arguable, which is what makes the rule usable at commit time without a
judgment call per file. `core/structure.md` is the one file in `core/` whose
audience is the framework itself rather than its consumers, so it's the single
case where path and audience diverge. The rule isn't wrong; it has exactly one
documented exception and doesn't say so.

Worth noting the framework's own `CLAUDE.md` is already carved out this way —
the rule explicitly names "for framework and packages, their own `CLAUDE.md`" as
internal despite sitting at the repo root. `core/structure.md` is the same kind
of file and didn't get the same carve-out, most likely because it postdates the
rule (added 2026-05-07 via the Structure Decisions Protocol).

**Affected files:**
- `core/skills/maintain.md` — § "What counts as consumer-facing"

**Proposed fix:**
Add `core/structure.md` to the internal list alongside the own-`CLAUDE.md`
carve-out. One clause: "…or, for framework and packages, their own `CLAUDE.md`
and `core/structure.md` (an as-built record of the project's own directories,
not content consumers read)."

Consider also whether the general principle is worth one sentence: a file's
audience governs, and path is a proxy that holds everywhere except for a
project's own records about itself. That phrasing would cover future files of
this kind without another amendment.

**Notes:**
Found by applying the rule rather than by reading it — the ambiguity is
invisible until a commit actually lands in that path. Same shape as this
session's two `/validate` entries: a seam between two correct sections that
reads as complete until something falls through it.

### 2026-11-12 — /validate recommends "fix now" but cannot execute it

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
Surfaced in the 2026-11-12 debrief after a framework structural check produced
six findings. `core/skills/validate.md` § "After Presenting Findings" instructs:

> **Fix now** — low effort, context advantage (we just touched this file), or
> batches naturally with other fixes

Its Scope section forbids exactly that:

> **You don't:**
> - Edit any files (that is `/maintain`)

So the skill proposes a disposition it is not permitted to carry out, and says
nothing about the handoff. The same section names the cost of the gap:

> Findings that live only in session logs drift — they get noted, carried
> forward, and rediscovered without being acted on.

**The drift it warns about happened in this session.** Two findings from the
structural check — a phantom `lib/.gitkeep` row at `core/structure.md:177`, and
six spurious `validate-*` mode files that Structural Addenda #3 flags on every
run — were approved as fix-now by the maintainer and then existed nowhere but
the conversation. Neither was logged, because logging them would have been the
wrong disposition; neither was fixed, because `/validate` can't. The framework's
anti-drift mechanism manufactured a drift case.

**Before:** "Fix now" is offered, approved, and then silently stranded at the
end of the validation session.
**After:** Either the handoff is explicit, or the option names its own
precondition.

**Confirmed reason:**
The disposition vocabulary (fix now / defer / ignore) was written from the
maintainer's point of view — those are the three things a *human* can decide to
do with a finding. The Scope section was written from the skill's point of view.
Both are correct in isolation; nothing reconciles them. The omission is a seam
between two sections of one file, which is the kind of gap that reads as
complete until something falls through it.

**Affected files:**
- `core/skills/validate.md` — § "After Presenting Findings" and § Scope

**Proposed fix:**
Smallest version: extend the fix-now bullet to name its precondition — "fix now
(requires `/maintain` — offer to switch before the session ends)". Add one line
to the end of the section: any fix-now finding not acted on before the session
closes gets logged instead, so nothing exits validation unrecorded.

Larger version worth considering: `/validate`'s closing suggestion currently
reads "If the session is wrapping up after validation, suggest `/debrief` to
reflect on the work, then `/close`." That sequence has no `/maintain` step, so
fix-now findings have no natural moment to land. Adding one would close the loop
structurally rather than by reminder.

**Notes:**
Found by debriefing a validation session rather than by validating — the gap is
invisible from inside `/validate`, since the skill reports findings and stops.
Related: the 2026-10-21 entry "/validate's structural check can't see
`/create-app` or package intents" is about coverage; this is about what happens
to findings after coverage succeeds. Both concern `/validate`; neither overlaps
the other's fix.

### 2026-11-12 — Running /validate as a known-answer test is undocumented and effective

**Type:** core
**Severity:** positive
**Blast radius:** all projects
**Status:** pending

**Observation:**
During the 2026-11-12 session, the framework structural check was run with a
specific purpose: two real defects had been found by hand two months earlier and
logged (the 2026-09-11 entries on package sibling paths and `/session-checkpoint`).
The check was invoked to see whether it would catch them.

It caught neither — and that miss became the session's highest-value finding,
outranking both originals, because it explained why they reached a generated
project in the first place. See the 2026-10-21 coherence entry for the gap
itself.

The technique: when a real defect has been found by hand, feed it to the
validator as a known-positive case. If the check passes, the finding is about
the checker, not the system — and that finding is usually more valuable than the
defect that prompted it, because it covers a class rather than an instance.

Nothing in `/validate` describes this use. Every mode description frames the
system as the object of inspection — "Are the framework's files wired up
correctly?", "Do the framework's docs tell a consistent story?" — and the file
closes:

> *Validation is read-only inspection. Find problems, explain them, point to
> fixes — then hand off to `/maintain` or `/friction-log`.*

Correct as far as it goes, but it frames validation as finding problems in the
system. Testing the check set against known answers is a different operation
with a different output: a coverage measurement.

**Confirmed reason:**
Not a defect — a missing capability description. The skill supports this use
fine; it just doesn't suggest it, so it depends on whoever runs validation
thinking of it. In this session it was prompted deliberately by the maintainer's
framing ("which options should we do?") plus two fresh known defects sitting in
the log. Absent that coincidence it would not have happened.

**Affected files:**
- `core/skills/validate-structural.md` — the natural home; the technique is most
  mechanical there
- `core/skills/validate.md` — possibly one line in Mode Selection, if the
  technique deserves surfacing at choice time

**Proposed fix:**
Add a short note to `validate-structural.md`: when known defects are in hand —
from the friction log, a recent manual discovery, a bug report — run the check
against them first. A check that passes on a known defect is itself the finding,
and it generalizes to the whole class. Worth stating that the resulting entry
belongs against the *checker*, not the system.

This would have caught both 2026-09-11 defects on the next run after either was
logged, without anyone thinking of it.

**Notes:**
Generalizes beyond the framework — any NLA whose `/validate` wrapper has domain
addenda can be tested this way the next time its maintainer finds something by
hand. The friction log is the natural source of known-answer cases, which makes
this a use for the log that the log doesn't currently advertise: pending entries
are test inputs, not just a work queue.

Relates to the 2026-04-17 pattern recorded in framework memory — "friction log
as design-signal, not just backlog." Same reframe, different use: there the log
was evidence for scoping decisions, here it's a corpus of test cases.

### 2026-10-21 — /validate's structural check can't see /create-app or package intents

**Type:** core
**Severity:** major
**Blast radius:** all projects (project generation)
**Status:** pending

**Observation:**
Surfaced by running the framework structural check specifically to test whether
it would catch the two findings logged 2026-09-11. It caught neither. The gap is
structural, not incidental.

The framework wrapper's Structural Addenda chain `core/skills/` →
`install/skills-intent.md` (#3) → core skill files (#4). Nothing continues the
chain to `/create-app`, which is the file that consumes those intents to generate
every new project. `grep -rn 'create-app' core/skills/validate*.md
.claude/skills/validate/SKILL.md` returns two hits, both in scenario-mode prose
describing what a trace *could* cover: "Trace scenarios where someone uses the
framework itself — running `/create-app`, `/maintain`, etc." `/create-app` is
never a check target.

Second gap, same shape: nothing reads `packages/*/install/skills-intent.md`.
Core check 3 verifies wrapper targets *after* generation — it passed cleanly here
— and checks 7 and 8 test package↔skill and package↔submodule *presence*. None
of the three reads intent content, so six reference implementations specifying
`../nla-penny-post/…` and `../nla-process-helpers/…` sit unvalidated until a
downstream project generates broken wrappers from them.

**Before:** All seven addenda pass. Two known-real bugs, one of them major,
surface nowhere in the report.
**After:** Addenda that compare `install/skills-intent.md` against
`/create-app`'s generation tables, and that verify path validity inside package
intent files.

**Confirmed reason:**
The addenda were written to validate the framework's *own* wiring — skills
tables, intent completeness, config routing. Project generation is a different
surface: it's the framework's output rather than its structure, and nothing in
the check set treats output as something to inspect. The widest-blast-radius
file in the repo is the one file the structural check never reads.

This is also why the two 2026-09-11 findings reached a generated project at all.
Both were caught by a human-directed read during `/create-app`, not by the safety
net. Twice is the argument for the mechanical check.

**Affected files:**
- `.claude/skills/validate/SKILL.md` — Structural Addenda, for the `/create-app`
  comparison (framework-only surface; `/create-app` has no domain analog)
- `core/skills/validate-structural.md` — core checks 3, 7, 8, for package intent
  path validity (domain projects install packages too, so this belongs in core)

**Proposed fix:**
1. Add an addendum: for every skill documented in `install/skills-intent.md`,
   verify it appears in `/create-app`'s Category 1 table *and* its bare-scaffold
   inline list. This directly catches the `/session-checkpoint` class.
2. Add to core check 3 (or a new check): for each package in `packages/`, read
   its `install/skills-intent.md` and verify every path in a reference
   implementation resolves from the installing project's root. Catches the
   sibling-path class, and future convention drift in packages not yet written.
3. Consider whether the framework's single hardcoded list of skills should live
   in `install/skills-intent.md` alone, with `/create-app` deriving from it —
   which would make check (1) unnecessary rather than necessary. See the
   2026-09-11 `/session-checkpoint` entry, proposed fix item 2.

**Notes:**
Third of three entries from the tax-onomy creation arc. The other two —
"Package intent files still specify pre-submodule sibling paths" and
"/session-checkpoint missing from /create-app's file tables," both 2026-09-11 —
are the instances; this is the reason they weren't caught. Resolve this one and
the class closes; resolve only those two and the next convention drift repeats
the pattern.

Relates to **Patterns to Watch #3 (Intent file completeness)**, which reads
"Track gaps between what `/create-app` needs and what intent files provide."
Both 2026-09-11 entries and this one run the *other* direction — the intent file
provides and `/create-app` fails to consume. The pattern's wording should cover
both directions.

### 2026-10-21 — Framework has no /startup wrapper; intent file says it should

**Type:** core
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** pending — needs a maintainer ruling, not a fix

**Observation:**
Found during the 2026-10-21 structural check. `core/skills/startup.md` exists and
`install/skills-intent.md:13` documents `### /startup` with its wrapper location,
but the framework has no `.claude/skills/startup/` directory and `CLAUDE.md`'s
skills table has no `/startup` row. The tables are self-consistent — 21 skills,
21 rows, exact match — so nothing is user-visibly broken.

`/startup` is the only skill in `install/skills-intent.md` without a framework
wrapper. `core/skills/README.md`'s "Adding a New Skill" checklist step 2 says to
create one (added 2026-02-22 precisely because the step was being missed).

**Confirmed reason:**
Not yet diagnosed — this needs the maintainer's intent, which is why it's logged
rather than fixed. The plausible reading is that it's deliberate: the framework
has no `app/` to initialize, and `CLAUDE.md` instead directs reading
`core/structure.md` at session start. If so, the absence is correct and the
record is what's wrong.

**Proposed fix:**
Either outcome is one small edit:
- *If deliberate:* note the exception in `core/structure.md` and/or
  `core/skills/README.md`, so the next structural check doesn't re-flag it.
- *If an oversight:* add the wrapper with a project-relative path
  (`core/skills/startup.md`, matching the other framework wrappers) and a
  `CLAUDE.md` row.

**Notes:**
Same class as the resolved 2026-02-22 entry "Framework install/update wrappers
use wrong path prefix" — the framework's own skill surface drifting from the
convention it publishes.

### 2026-10-21 — installed-packages.md uses display names, not directory names

**Type:** documentation
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** pending

**Observation:**
Found during the 2026-10-21 structural check. `reference/installed-packages.md`
heads its sections `## penny post` and `## process helpers`; the submodules are
`packages/nla-penny-post` and `packages/nla-process-helpers`.

Core check 8 says "verify each logged package appears" in `git submodule
status`. As written, that comparison needs a human to map display name to
directory name. Both packages are in fact present and clean — this is a
legibility defect, not a missing submodule.

For contrast, tax-onomy's generated `installed-packages.md` uses directory names
as headings (`## nla-penny-post`), which makes the check mechanical.

**Proposed fix:**
Rename the two headings to directory names, keeping display names in the prose
if they read better there. Alternatively, have check 8 state the mapping rule
explicitly. The first is smaller and makes the check work as written.

**Notes:**
Cosmetic on its own; logged because check 8 depends on it and because the
generated-project convention already diverges from the framework's own file.

### 2026-09-11 — Package intent files still specify pre-submodule sibling paths

**Type:** intent
**Severity:** major
**Blast radius:** all projects installing penny post or process helpers
**Status:** pending

**Observation:**
Surfaced during the 2026-09-09 `/create-app` session that generated `tax-onomy`
with both extension packages. Both packages' `install/skills-intent.md` files
still specify the pre-submodule sibling-directory convention in their reference
implementations:

- `packages/nla-penny-post/install/skills-intent.md:22` — "Read and follow
  `../nla-penny-post/app/check-feedback.md`." (also line 40 for `/write-letter`)
- `packages/nla-process-helpers/install/skills-intent.md:27, 51, 71, 91` — "Read
  and follow `../nla-process-helpers/app/[skill].md`." for all four techniques

Both `install.md` prerequisites also still read "**This repo cloned as a
sibling** — `../nla-penny-post/` relative to the NLA."

Under the packages/ submodule model (2026-04-15), these paths resolve to nothing.
An installing AI that follows the reference implementations literally generates
six wrappers that silently point at nonexistent files.

**Before:** Following package intent literally produces
`Read and follow ../nla-penny-post/app/check-feedback.md` — a path with no file
behind it.
**After:** `Read and follow packages/nla-penny-post/app/check-feedback.md`.

**Confirmed reason:**
Known-pending propagation, not a new regression. The packages/ migration
(2026-04-15) updated the framework's own intent files; penny post and process
helpers were queued to follow and haven't yet. What this session adds is
evidence that the lag is not merely stale documentation — it is a live trap that
produces broken output on every install.

The failure is silent. A wrapper pointing at a missing file raises nothing at
install time; it fails only when someone invokes the skill, possibly weeks later,
at which point the cause is several steps removed from the symptom.

I caught it because I read both packages' intent files and then verified every
generated wrapper's delegation target resolved on disk. Had I trusted the
reference implementations, six of tax-onomy's twenty wrappers would have shipped
broken and consistency checks 1–4 would still have passed — the skills tables
would have matched the filesystem perfectly, because the wrapper files existed.
Only target resolution catches this.

**Affected files:**
- `core/skills/install.md` — the framework-side fix (see below)
- `.claude/skills/create-app/SKILL.md` — same verification gap
- Package-side: `install/skills-intent.md` and `install/install.md` in both
  packages — but see Proposed fix on who changes those

**Proposed fix:**
Two parts, and the split matters.

*Framework side (actionable here):* add target verification to `/install` and
`/create-app`. After generating wrappers, check that every delegation path
resolves to an existing file; report any that don't. This is mechanical, cheap,
and catches the entire class rather than this instance — including future
convention drift in packages not yet written. It is what caught the bug in this
session, run by hand.

*Package side (not actionable here):* the 2026-03-04 archive entry
("Plan agent proposed directly editing sibling package manifests") established
that packages adopt changes through their own `/update` channel, not through
direct cross-project edits by the framework maintainer. So the framework should
not edit these two files. Each package needs its own maintenance session to
adopt the packages/ convention. Consider a penny post letter to each as the
notification mechanism.

**Notes:**
Relates to **Patterns to Watch #2 (Path resolution)** — and sharpens it. That
pattern currently reads as a caution about *confusion* in the two-hop reading
chain; this is a case where the path is not confusing but simply wrong, and
nothing in the generation path notices.

Same class as the resolved 2026-02-22 entry "Framework install/update wrappers
use wrong path prefix," where the framework's own wrappers used the
domain-project convention. That one was found by inspection too. Two instances
of the same class, both caught by a human or AI happening to look, is an argument
for the mechanical check.

Workaround applied in tax-onomy: used `packages/` paths, verified all six targets
resolve, and recorded the deviation in that project's
`reference/installed-packages.md` so a future `/update` can reconcile.

### 2026-09-11 — /session-checkpoint missing from /create-app's file tables

**Type:** intent
**Severity:** minor
**Blast radius:** project generation
**Status:** pending

**Observation:**
`install/skills-intent.md` documents 14 framework skills, including
`### /session-checkpoint` at line 191 with its wrapper location and reference
implementation. `/create-app` omits it in two places:

- `.claude/skills/create-app/SKILL.md:156–168` — the Category 1 file table lists
  13 wrappers, no session-checkpoint row
- `.claude/skills/create-app/SKILL.md:285` — the bare-scaffold paragraph
  enumerates the framework-default skills inline: "(startup, maintain,
  friction-log, preferences, validate, install, update, export, check-updates,
  think, debrief, close, guide)" — same 13, same omission

The two files disagree about what a new project gets. Every project generated
from the Category 1 table ships without `/session-checkpoint`, despite the intent
file specifying it.

**Confirmed reason:**
Almost certainly an incomplete update when `/session-checkpoint` was added —
`install/skills-intent.md` got the new section, `/create-app`'s two hardcoded
enumerations didn't. The archive shows the framework has hit this shape before:
several entries record adding a skill to "install/skills-intent.md, CLAUDE.md,
and README.md," and `core/skills/README.md`'s "Adding a New Skill" checklist
exists precisely because the propagation surface is wide and easy to
under-cover. `/create-app`'s inline lists appear to be a surface the checklist
doesn't name.

**Resolution direction:** `skills-intent.md` is right and `/create-app` is
wrong — intent files are the framework's declared source of truth, and the
framework carries `/session-checkpoint` in its own skills table. So the fix is
additive to `/create-app`, not a removal from the intent file.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — both locations above
- `core/skills/README.md` — "Adding a New Skill" checklist, if the propagation
  surface is under-specified

**Proposed fix:**
1. Add the `/session-checkpoint` row to the Category 1 table and the skill name
   to the bare-scaffold inline list.
2. Consider whether `/create-app` should enumerate framework skills at all, or
   derive them from `install/skills-intent.md`'s section headings. Two hardcoded
   copies of a list that lives authoritatively elsewhere is the actual defect;
   this instance is a symptom. A single sentence — "generate a wrapper for every
   skill documented in `install/skills-intent.md`" — would make the class
   impossible.
3. If (2) isn't taken, add `/create-app`'s two lists to the "Adding a New Skill"
   checklist in `core/skills/README.md`.

**Notes:**
Relates to **Patterns to Watch #3 (Intent file completeness)**, and inverts it.
That pattern reads "Track gaps between what `/create-app` needs and what intent
files provide" — this is the opposite direction: the intent file provides, and
`/create-app` fails to consume. Worth widening the pattern's wording to cover
divergence in both directions.

Resolved in tax-onomy by following the intent file — 14 wrappers generated, with
the deviation recorded in that project's `reference/installed-packages.md`.

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
