# Update Notes

What's changed in the framework and what it means for your project. Written for both
human readers scanning a changelog and the AI running `/update` as context for proposals.

Not every framework change gets a note — only changes where the *so what for your
project* isn't obvious from the intent diff alone.

For older notes, check `update-notes-archive.md`.

---

## Entry Format

```markdown
### YYYY-MM-DD — [Brief title]

**Affects:** [which intent files or core files changed]
**Commit:** [optional — a hash for precise anchoring, if convenient]

[Narrative guidance. What changed, why, and what it might mean for different
kinds of projects.]
```

The date and "Affects" field do the real work — `/update` matches notes to changes
using those plus the actual git diff. The commit hash is a convenience anchor: include
it when it's easy (e.g., writing the note after committing), omit it when it's not
(e.g., the note is part of the same commit as the change).

---

## Entries

*Entries are added chronologically, newest first.*

### 2026-05-08 — `/close` reordered; tag cadence refined to per-push

**Affects:** core/skills/close.md, core/skills/maintain.md

Two related changes ship together.

**`/close` step order changed.** The skill now runs in dependency order:

1. Validate (if structural changes warrant it)
2. Check documentation mirrors
3. Debrief
4. Finalize the session log
5. Commit + tag (if pushing) + push

The previous order placed the session log first, but validation, mirror
fixes, and debrief can produce work that needs to land *in* the log — so the
log is finalized later, after that work is in hand. This also lets debrief
reflect everything that happened, including the close-time work itself.

**Tag cadence: per-push, not per-commit.** The Shippability section in
`maintain.md` previously read as per-commit tagging — every commit touching
consumer-facing content got tagged. In practice this inflated version
numbers (a single session shipping three consumer-facing commits jumped
v0.0.4 → v0.0.5 → v0.0.6 → v0.0.7 without any of the intermediate tags
marking a meaningful release point).

The refined rule separates two questions:

- *What counts as consumer-facing* — unchanged. `core/`, consumer-facing
  `install/*.md`, `app/`, `.claude/skills/`, or `CLAUDE.md` (depending on
  project type).
- *When the tag goes on* — now at *push*, not at commit. `/close` reviews
  commits since the last tag and tags HEAD before pushing if any touched
  consumer-facing content. A session that ships three consumer-facing
  commits gets one tag.

If a session ends without a push (work left local for later review), no tag
fires. Tags are for consumers; an unpushed tag is noise. The next push
tags whatever has accumulated.

Update-notes entries continue to land per-commit — they're a running
changelog at commit granularity. The tag is the release marker that batches
them.

**What this means for your project:**

- The next time you run `/close`, expect the new step order. The
  practical difference: the session log captures close-time work, so you
  don't need to remember to update it after committing.
- Tag cadence will visibly change. If your project ships consumer-facing
  changes via `git push`, expect fewer, more meaningful tags — typically
  one per session that touched consumer-facing content. Multi-commit
  sessions no longer produce multi-tag releases.
- If a session ends without a push, it ends without a tag. The next push
  catches up.
- Use annotated tags (`git tag -a vX.Y.Z -m "..."`), not lightweight ones.
  `git push --follow-tags` only pushes annotated tags; lightweight tags
  are skipped silently. `close.md` step 5 spells this out explicitly.

**Resolves friction log entry:** "Shippability convention reads as
per-commit tagging; session-end is better" (2026-04-18). The convention
now separates what-counts-as-tag-worthy from when-the-tag-goes-on.

---

### 2026-05-08 — Validation flow added as a sixth working rhythm

**Affects:** core/nla-foundations.md

A new "Validation Flow" working rhythm has been added to
`core/nla-foundations.md` alongside the existing four (Improvement
Loop, Design Flow, Update Cycle, Session Structure) and the recently-
added Structural Change Discipline.

The rhythm: *hypothesize → design experiment → test in cold context →
measure → iterate or commit.* When prose changes have downstream impact
and reasoning alone leaves uncertainty, validate empirically before
committing — controlled experiments with cold-context agents and binary
signals.

Critically, the rhythm includes an intent-shaped caveat: it isn't
always warranted. *"Many prose changes are obviously routine, and
experiments would be overhead. But when stakes are non-trivial, pause
to ask: would experiments inform this work? Would they be worth doing?
The question itself is cheap, even when the answer is 'no, this is
too small to test.'"*

**Why now:** Five empirical experiments across three NLAs have
demonstrated the methodology generalizes across domains: the
framework's skill-invocation discipline (2026-05-06) and structure
decisions protocol (2026-05-07), plus facebook-moderation's
implementation-standards (2026-04-02), ingest-compile-compare
(2026-04-06), and identity-standards-transmission (2026-04-24). The
pattern is mature enough to document; further evolution stays open
(the rhythm explicitly says the methodology continues to evolve).

**What this means for your project:** The next time you're considering
a prose change with downstream impact — convention shift, doctrine
change, skill template revision, framework-level addition — pausing to
ask whether experiments would inform the work is now part of the
documented rhythm. If yes, see `reference/experiments/` (in the
framework or in sibling NLAs) for working examples of the methodology.
If no, proceed with reasoning alone — the question is the discipline,
not running experiments unconditionally.

**Resolves friction log entry:** "Framework lacks documented
experimentation methodology" (2026-05-06). The entry's MVP scope
(documenting the rhythm in foundations) is complete; deeper work
(standalone cold-context review documentation, skill-level affordances
like `/run-experiment` or folding into `/think`) remains as future
opportunities.

---

### 2026-05-07 — Structure decisions protocol (framework-first adoption)

**Affects:** core/nla-foundations.md, core/structure.md (new),
core/skills/maintain.md, core/skills/install.md
**Commit:** 68c145a, ea09b4a

The framework adopts a propose-review-record protocol for structural
change — new directories, reorganizations, new top-level files. The
discipline pauses before structural changes, proposes the change with
its structure-record entry, gets human approval, then acts (with the
record updated as part of the change, not separate hygiene). Borrowed
shape from facebook-moderation's compile-time `build-guide.md`
(attribution per entry, Judgment notes, Decision Sources table).

**What changed in `core/`:**
- `nla-foundations.md`: a fifth working rhythm, "Structural Change
  Discipline." Phrased location-agnostically — refers to "your project's
  structure record" rather than a specific path. Includes an explicit
  guard: don't create `core/structure.md` in a domain project (that's
  the framework's analog; domain projects extend `app/overview.md`'s
  "Where Things Live" section).
- `core/structure.md` (new): the framework's own as-built structure
  record. Domain projects do not consume this file — it's the
  framework's instance of the protocol, not a propagation target.
- `core/skills/maintain.md`: a "When the change is structural" callout
  in Confirm Before Implementing. Names the discipline and the recording
  requirement.
- `core/skills/install.md`: a new principle bullet for structural
  changes introduced by installed packages.

**What this means for your project:** The discipline is now in your
session context (via `nla-foundations.md` being loaded at startup). When
you're maintaining your project and a structural change comes up, the AI
will follow the protocol — it'll propose, ask for approval, and want to
record the change. Until your project has a structure record (a "Where
Things Live" section in `app/overview.md`), the protocol still works:
the AI proposes creating the record alongside the first structural
change.

**Optional adoption:** You can add a "Where Things Live" section to
your `app/overview.md` proactively — list each top-level directory and
top-level file with purpose and attribution (mostly `[framework
default]` for inherited structure, `[domain decision]` for choices
specific to your project). A Decision Sources table at the bottom
helps with scan affordance. This becomes the consultation target for
future placement decisions. New projects created with `/create-app`
(post-2026-05-07) get this section automatically per the updated
generation guidance.

**What's deferred:** `install/CLAUDE-intent.md` and
`install/structure-intent.md` will be updated in a follow-up session
(the publication arc) to canonically describe the structure record's
content for domain projects. Until then, the foundations.md mention
plus the maintain.md/install.md callouts carry the discipline; the
intent file refinements will provide the canonical structure
specification when they land.

---

### 2026-05-04 — `--recurse-submodules` documented as one-step clone option

**Affects:** README.md, .claude/skills/create-app/SKILL.md (generated README template)
**Commit:** aa29548

Both READMEs now suggest `git clone --recurse-submodules` as the primary
clone form, with the two-step `git submodule update --init` shown as the
fallback for already-cloned repos. Cosmetic improvement — the two-step
form continues to work identically.

**What this means for your project:** Optional. Your existing README's
clone instructions are not broken — `git submodule update --init` is the
correct two-step form. If you want to mirror the framework's updated
guidance, add `git clone --recurse-submodules [url]` as the primary
instruction in your README, keeping the two-step as the already-cloned
fallback. No code or behavioral changes; new contributors to your project
get a slightly shorter onboarding path.

---

### 2026-05-04 — `/maintain` now loads writing standards before drafting operative docs

**Affects:** core/skills/maintain.md, .claude/skills/maintain/SKILL.md (mirror)

The Writing Standards section in `/maintain` was upgraded from a pointer
(consult the standards when needed) to an author-time procedure: when
editing an operative doc, identify the doc type, read section 2 of
`reference/standards/nla-writing.md` plus the matching 8.x subsection,
then draft. The targeted load keeps the standards in the room as
constraints applied during writing, not just consulted afterward — and
keeps the load light by reading only what's relevant to the doc type
being edited.

The doc-type → standards mapping covers skills (Section 2 + 8.1),
session logs (2 + 8.2), operative docs (2 + 8.3), design docs (2 + 8.4),
friction log entries (8.5), values docs (2 + 8.6), and specs (2 + 8.7).
Mechanical edits (typos, broken paths, dead references) skip the load —
the standards apply when you're producing prose that shapes runtime
behavior.

The diagnostic-use guidance is preserved and slightly expanded: standards
2.3 (produces what it contains) and 4.4 (cross-references with context)
are named as the most diagnostically productive standards, with a pointer
to `/validate standards` for broader retrospective review.

**What this means for your project:** Behavioral shift in how `/maintain`
approaches operative-doc edits — your AI will read a focused subset of
the standards before drafting, rather than relying on memory or general
knowledge. Available the next time you advance the framework submodule;
no domain-side wrapper changes needed.

---

### 2026-05-04 — New `/validate standards` mode

**Affects:** core/skills/validate.md, core/skills/validate-standards.md (new), core/skills/README.md, install/skills-intent.md

A new sub-mode of `/validate` reads in-scope docs against the NLA writing
standards (`reference/standards/nla-writing.md` in the framework, or
`packages/nla-framework/reference/standards/nla-writing.md` in a domain
project), citing specific standards when something falls short.

Use it when the standards file evolves (re-check existing docs against
the new bar), when a doc feels off but passes structural and coherence
checks, or as a periodic quality sweep — especially over docs written
before the standards landed.

The mode is scope-configurable. Default scope is operative content
(`core/` in the framework, `app/` and `.claude/skills/` in domain
projects), reviewed against standards 2.3 (produces what it contains)
and 4.4 (cross-references with context) — the standards Phase 2 of the
#21 work found most diagnostically productive. Both scope and standards
subset can be narrowed or broadened per invocation.

Findings land in `reference/sessions/YYYY-MM-DD-standards-review.md`,
matching the architecture-review pattern, and route through `/validate`'s
existing fix-now / defer / wont-fix disposition step.

**What this means for your project:** New affordance, not a behavioral
change to existing modes. Available the next time you advance the
framework submodule. If your domain project's `.claude/skills/validate/`
wrapper has its own mode menu, `/update` will propose adding an entry
for the standards mode; if it's a thin wrapper that delegates to
`core/skills/validate.md`, no change needed.

---

### 2026-04-18 — Foundations principle #2 reframed as "NLA Documents Are Source Code"

**Affects:** core/nla-foundations.md, install/CLAUDE-intent.md

Principle #2 in `nla-foundations.md` was renamed from "The Documentation Is
the Application" to "NLA Documents Are Source Code," with an opening paragraph
that lays out the reframe operationally: an ambiguous instruction is a bug, a
missing section is a missing feature, an inconsistent term is a naming
collision. The existing fix-is-in-docs and diagnose-from-artifacts material
is preserved as supporting points.

`install/CLAUDE-intent.md` was updated to match. The Grounding Principles
bullet "Documentation is the application" and the Execution Principles bullet
"Documentation is source code" were both consolidated to "NLA documents are
source code" so that `/create-app` and `/install` generate downstream NLA
CLAUDE.md files with consistent wording.

The reframe was adopted from the NLA writing standards (Phase 2 of the #21
work), which use the same framing as their load-bearing preamble. The earlier
"Documentation Is the Application" wording is accurate but softer; the
source-code framing invites stronger compliance by naming the specific
failure modes that matter.

**What this means for your project:** `/update` may propose a small wording
update to your CLAUDE.md's grounding principles to match the new phrasing.
The operative behavior is unchanged — the LLM still treats docs as
authoritative, the fix is still usually in the docs, and diagnosis still
starts from artifacts. What changes is the mental model the AI and maintainers
hold: these are source code, so treat them with the gravity that implies.

The foundations change is loaded automatically via
`packages/nla-framework/core/nla-foundations.md` the next time you advance the
framework submodule. The intent-file change only propagates if you apply the
`/update` proposal — you can accept or skip it based on your project's voice
and how closely your CLAUDE.md mirrors the framework's language.

---

### 2026-04-18 — /maintain broadened to work in both domain and framework contexts

**Affects:** core/skills/maintain.md

The core `/maintain` skill was written assuming a domain-project context —
hardcoded `app/overview.md` in required reading, `app/`-focused editable
targets, a "Check for Downstream Effects" principle tied to `app/shared/*`.
The framework and packages maintained a parallel full-custom wrapper to
compensate, which drifted from core over time.

Now core is project-type-agnostic:
- Required reading uses conditional phrasing for paths that vary by context
  (foundations, overview).
- "What You Can Edit" lists editable-target types generally; the skill
  wrapper that delegates here supplies the specific list for each project
  type.
- Principle #3 is renamed **Name the Blast Radius** — a universal principle
  that stating scope makes proposals reviewable. The `app/shared/*` quick
  reference and values awareness are preserved as domain-project specifics
  within the section.

**What this means for your project:** The `/maintain` behavior is unchanged
for domain projects — you still read the same files, apply the same
principles, and get the same downstream-effects guidance. The naming shift
on principle #3 ("Check for Downstream Effects" → "Name the Blast Radius")
is cosmetic for domain projects; if any of your own docs reference the old
name, update them at your convenience. Values awareness and the shared-context
downstream table are now explicitly conditional — if your project doesn't
have a values doc or shared context, the corresponding checks are skipped
rather than pointing at missing files.

---

### 2026-04-17 — NLA writing standards available; /maintain consults them

**Affects:** core/skills/maintain.md, reference/standards/nla-writing.md (new)

The framework now ships NLA writing standards — 33 conventions for writing
prose artifacts (skills, operative docs, session logs, design docs, values
docs, specs). Originally compiled from empirical findings in NLA compilation
work on the facebook-moderation project, adapted and generalized for the
framework.

`/maintain` now includes a "Writing Standards" section pointing at
`packages/nla-framework/reference/standards/nla-writing.md`. Consult the
standards when editing or creating operative documents, especially as a
diagnostic for gaps between doc intent and runtime behavior: *the document
produces what it contains*.

**What this means for your project:** Nothing to do. The maintain skill
change propagates via thin wrappers; the standards file ships with the
framework submodule, accessible at
`packages/nla-framework/reference/standards/nla-writing.md`. Read them when
editing operative docs, or when an operative doc seems to be producing the
wrong runtime behavior.

---

### 2026-04-17 — Documented settings.local.json drift pattern

**Affects:** install/structure-intent.md

Added a note to the `.claude/settings.local.json` description explaining that
Claude Code auto-approves and records new Bash patterns over time when
maintainers run tools that weren't pre-declared. These entries accumulate
silently — not framework behavior, not a bug, just how Claude Code's
approve-and-record loop works.

**What this means for your project:** Nothing to do. When you notice
unexpected entries in your settings file, you now know it's Claude Code's
loop rather than something the framework introduced. Periodic pruning is
fine if the file grows large.

---

### 2026-04-17 — Initial submodule install checks for tagged releases

**Affects:** core/skills/install.md, core/skills/update.md, .claude/skills/create-app/SKILL.md

`/install` (and `/update` when applying an intent that adds a submodule) now
check for tagged releases after `git submodule add` and offer the user a
choice between the tagged release (stable) and HEAD. This mirrors the
behavior `/update`'s advance path has always had for existing submodules —
the principle (tagged release = stable default) now applies to initial-add
paths too.

`/create-app` does the same for the framework submodule (and any extension
packages added during creation), so new projects pin at the framework's
tagged release by default.

**What this means for your project:** No project-side change required. The
next time you run `/install` to add a new package, you'll see the stable/HEAD
prompt if a tagged release exists.

**Why:** Without the check, initial-adds silently pin at whatever the
remote's default branch points to — fine when HEAD matches the latest tag,
misleading when they diverge. Caught during the packages/ migration: a
package whose HEAD was one commit past its latest tag (a non-behavioral
session-log update) ended up pinned at `main` rather than at the tagged
release. Catching this at install time is easier than noticing drift months
later.

**Propagates automatically.** The install and update skill changes reach
domain projects via thin wrappers.

---

### 2026-04-17 — Shippability convention for commits: consumer-facing vs. internal

**Affects:** core/skills/maintain.md, install/package-intent.md

The maintain skill now codifies a distinction at commit time: whether a commit
touches **consumer-facing** content (what another NLA's runtime reads) or only
**internal** content (the project's own reference/, session logs, etc.).

**What this means for your project:**

- At commit time, the maintain skill now asks: does this touch consumer-facing
  content? If yes → tag (if you use tagged releases) and add an
  `install/update-notes.md` entry (if you ship update notes). If no → skip both.
- For domain projects, "consumer-facing" means `app/`, `.claude/skills/`, or
  `CLAUDE.md` — the parts that ship in a plugin export. Changes to `reference/`
  are internal.
- For packages, it also includes `install/*.md` (the intent files consumers
  read via `/install` and `/update`).

**Why:** Without the convention, routine internal commits (session log updates,
design-rationale entries) surface to every downstream `/update` run as "there
are new commits to review" — even though nothing has changed that would affect
those projects. Scales poorly as the ecosystem grows. The convention lets
maintainers tag meaningful releases without noise from internal bookkeeping.

See `reference/design-rationale.md` ("Shippability: Consumer-Facing vs. Internal
Content") for the full principle and `core/skills/maintain.md` ("Shippability
at Commit Time") for the commit-time procedure.

**Propagates automatically.** The maintain skill change reaches domain projects
via thin wrappers. No per-project action required — the next time you run
`/maintain`, the commit-time check is part of the session lifecycle. Package
authors should review `install/package-intent.md` for package-specific guidance.

---

### 2026-04-16 — Export skill revised: view-source plugins + Python script

**Affects:** core/skills/export.md, install/skills-intent.md, new lib/export.py (framework-level)

The `/export` skill's mechanics changed substantially. Plugins now preserve NLA structure (view-source) instead of flattening thin wrappers, and mechanical work moved from AI-driven file operations to a Python script at `packages/nla-framework/lib/export.py`.

**What this means for your project:**

- Your `/export` wrapper at `.claude/skills/export/SKILL.md` needs no changes — it remains a thin wrapper pointing at the core skill, which propagates automatically via `/update`.
- The skill now checks Python 3 availability at invocation and offers install guidance if missing. Point-of-use requirement, not a framework-wide prereq.
- The output plugin shape has changed. Old design: shared context bundled per-skill directory, thin wrappers flattened. New design: structure mirrors the NLA, with paths prefixed `${CLAUDE_PLUGIN_ROOT}/`. To get the new shape, re-export.
- Export now requires a clean working tree (commits only). If you have uncommitted changes, the skill will ask you to commit or explicitly confirm.
- If you have committed-but-not-shippable files (e.g., a `reference/` directory), consider adding a `.gitattributes` entry with `export-ignore` — `git archive` honors it automatically.

**Why:** The packages/submodules migration (2026-04-15) made the old flattening design unnecessary — intra-plugin paths now resolve reliably via `${CLAUDE_PLUGIN_ROOT}`. The new design eliminates per-skill duplication, makes plugins inspectable ("view source"), and splits work between AI judgment and a deterministic Python script. See `reference/design-rationale.md` — "Plugin Export: View-Source Model" for full reasoning.

**Blast radius:** Only projects that run `/export` are affected. Re-export to pick up the new shape.

### 2026-04-15 — Packages directory replaces sibling directory convention

**Affects:** All intent files, all core skills, CLAUDE-intent, structure-intent, skills-intent, install.md, package-intent.md

All dependencies now live inside the project in `packages/` as git submodules. The sibling directory convention (`../nla-framework/`, `../nla-package/`) is retired.

**What this means for your project:**

Every thin wrapper path changes from `../nla-framework/core/skills/[name].md` to `packages/nla-framework/core/skills/[name].md`. Extension package wrappers change similarly (e.g., `../nla-penny-post/` → `packages/nla-penny-post/`).

**Migration steps:**

1. Add the framework as a submodule: `git submodule add --depth 1 https://github.com/mightytech/nla-framework.git packages/nla-framework`
2. If you have extension packages installed, add those too: `git submodule add --depth 1 [URL] packages/[name]`
3. Update all thin wrappers: change `../nla-framework/` to `packages/nla-framework/` in every `.claude/skills/*/SKILL.md`
4. Update CLAUDE.md references to the framework and packages
5. Update `reference/installed-packages.md` Source paths
6. If you have a `.claude/settings.local.json` with `Read(../nla-framework/**)` entries, those can be removed — all reads are now within-project
7. Run `/validate` structural check to catch any missed references

**Why:** Cross-directory reads triggered persistent Claude Code permission prompts. The sibling convention also meant no version pinning (every project ran whatever was on main) and projects weren't self-contained (sharing required knowing to clone siblings). The packages/ model solves all three.

**Convention:** Use `git submodule update --init` (not `--recursive`) when cloning projects. Dependencies are flat — each project lists only its direct dependencies.

### 2026-03-05 — New /guide skill and Working Rhythms in foundations

**Affects:** install/skills-intent.md, core/skills/guide.md (new),
core/nla-foundations.md, core/skills/startup.md, core/skills/maintain.md,
install/structure-intent.md, .claude/skills/create-app/SKILL.md

Two related additions that make NLAs more approachable for new users:

**Working Rhythms** — A new section in `core/nla-foundations.md` documents the four
common workflow patterns: the improvement loop, the design flow, the update cycle, and
session structure. Each explains not just what the rhythm is but why it exists. This
loads automatically via `../nla-framework/`.

**`/guide` skill** — Context-aware help that adapts to the user's familiarity level. It
reads both Working Rhythms (from foundations) and `app/overview.md` (for project-specific
context) to explain how the system works, what skills are available, and what to do next.

**`/startup` and `/maintain`** now mention `/guide` as an option when users seem
unfamiliar. These propagate automatically via thin wrappers.

**`overview.md` pattern** — The generation guidance for `app/overview.md` now includes a
"How users work with this" section describing typical sessions and workflow expectations.
Existing projects can add this section to their overview via `/maintain` — it helps both
users and the AI understand the expected session rhythm.

**What to do in your project:**
- Create `.claude/skills/guide/SKILL.md` — standard thin wrapper (the intent diff shows
  the reference wrapper)
- Add `/guide` to your CLAUDE.md skills table
- Optionally add a "How users work with this" section to `app/overview.md` — this gives
  `/guide` richer project-specific content to draw on

### 2026-03-04 — Permission management model

**Affects:** install/install.md, install/structure-intent.md, install/package-intent.md,
core/skills/install.md, core/skills/update.md, core/skills/validate-structural.md,
core/skills/startup.md, .claude/skills/create-app/SKILL.md

Claude Code prompts for permission every time a skill reads from a sibling directory
(`../nla-framework/`, `../nla-penny-post/`, etc.). For NLAs with many thin wrapper
skills, this creates significant friction — prompts on nearly every skill invocation.

The framework now supports a **permission management model**:

- **Package manifests** (`install.md`) declare what filesystem access they need, using
  a Permissions section with Claude Code permission patterns
- **`/create-app`** generates an initial `.claude/settings.local.json` with framework
  reads and common bash patterns pre-approved
- **`/install` and `/update`** propose permission entries when packages declare needs
- **`/validate`** checks declared needs against actual settings and reports gaps
- **`/startup`** notes when no settings file exists (one-line awareness)

**What to do in your project:**

1. Run `/update` — it will detect the new permissions section in the framework manifest
   and offer to generate `.claude/settings.local.json` for you. This is the easiest path.

2. Alternatively, create `.claude/settings.local.json` manually:
   ```json
   {
     "permissions": {
       "allow": [
         "Read(/absolute/path/to/nla-framework/**)",
         "Bash(git:*)",
         "Bash(ls:*)",
         "Bash(test:*)"
       ]
     }
   }
   ```
   Add `Read(../package-name/**)` entries for each installed package.

3. **If you maintain a package:** Add a Permissions section to your `install/install.md`.
   See the framework's own `install/install.md` or `install/package-intent.md` for the
   format and conventions.

This is entirely optional. Projects work without it — they just see more permission
prompts. The settings file eliminates prompts for routine read operations.

**What propagates automatically via thin wrappers:**
- `/startup`'s awareness of missing settings
- `/validate`'s new permission consistency check
- `/install`'s permission proposal step
- `/update`'s permission delta detection

---

### 2026-03-04 — New /close skill for session wrap-up

**Affects:** install/skills-intent.md, core/skills/close.md (new), core/skills/maintain.md, core/skills/debrief.md, core/skills/validate.md, core/skills/export.md

A new `/close` skill wraps up work sessions — finalizing session logs, checking for
loose ends (uncommitted changes, documentation mirrors, validation), and summarizing
state for next time. It creates a session log if one doesn't already exist, ensuring
every substantive session has a record.

`/maintain`'s session close steps now delegate to `/close` instead of inline
instructions. This propagates automatically via thin wrappers. Several skills now
suggest natural next steps at their completion points: `/debrief` suggests `/close`,
`/validate` suggests `/debrief` then `/close`, `/export` suggests validation then
`/close`.

**What to do in your project:**
- Create `.claude/skills/close/SKILL.md` — standard thin wrapper (the intent diff
  shows the reference wrapper)
- Add `/close` to your CLAUDE.md skills table

The skill is additive — no existing behavior changes beyond the session close
delegation in `/maintain`, which propagates automatically.

---

### 2026-02-23 — Startup now surfaces pending friction log entries

**Affects:** core/skills/startup.md, core/skills/friction-log.md

Two small changes to help non-maintainer users get friction observations to the
right person:

**Startup** now checks `reference/friction-log.md` for pending entries and includes
the count in the startup summary. For non-maintainer users, it notes that entries
can be shared with the project's maintainer. No specific mechanism is prescribed —
if `/write-letter` is available the AI mentions it naturally; otherwise it suggests
sharing the file directly.

**Friction-log skill** now has a "Session Awareness" section: at session boundaries
(work wrapping up, context shifting), the AI briefly surfaces pending entry count
with a reminder about processing or sharing options. This is awareness, not a
workflow step.

No action needed — these propagate automatically via thin wrappers. If you ejected
either skill, review the changes and consider incorporating them.

---

### 2026-02-22 — New /check-updates skill, /update enhanced with remote pull and rollback

**Affects:** install/skills-intent.md, core/skills/update.md, core/skills/startup.md,
core/skills/check-updates.md (new), config-spec.md

Two related changes to the update pipeline:

**New `/check-updates` skill** — read-only scan across the NLA and all installed
packages. Reports three tiers: remote-to-local (has the package author pushed changes
you haven't pulled?), local-to-installed (has the local package changed since your
last update?), and the NLA's own remote status. Recommends specific actions for each.

**`/update` now handles the full update lifecycle.** Before applying intent changes,
`/update` can fetch and fast-forward merge on package repos and the NLA's own remote.
It creates a rollback branch before any operations. Non-fast-forward situations are
refused — they need resolution in the package's own context (see "Context Determines
Competence" in `reference/design-rationale.md`).

**What to do in your project:**
- Create `.claude/skills/check-updates/SKILL.md` — standard thin wrapper (the intent
  diff shows the reference wrapper)
- Add `/check-updates` to your CLAUDE.md skills table
- Update `/update`'s description in your CLAUDE.md skills table to reflect its
  broader scope
- Optionally enable startup update checking via `/preferences` ("Check for package
  updates at session start")
- No changes needed for the /update enhancement itself — the thin wrapper picks up
  the new behavior automatically

---

### 2026-02-22 — /unpack moved to process helpers package

**Affects:** install/skills-intent.md, CLAUDE.md

The `/unpack` skill has moved from the framework's core to the new process helpers
package (`../nla-process-helpers/`). Process helpers are facilitation techniques that
shape how conversations happen — that's a preference, not infrastructure. Phase skills
(/think, /debrief) remain in core because they define work lifecycle stages.

**What to do in your project:**
- If you have `.claude/skills/unpack/SKILL.md` pointing to
  `../nla-framework/core/skills/unpack.md`, you have two options:
  1. **Install the process helpers package:** Clone `nla-process-helpers` as a sibling,
     then update the wrapper to point to `../nla-process-helpers/app/unpack.md`
  2. **Remove /unpack:** Delete `.claude/skills/unpack/` and remove it from your
     CLAUDE.md skills table
- If you don't use /unpack, no action needed.

The process helpers package follows the same extension pattern as penny post — thin
wrappers in your NLA pointing to skill logic in a sibling repo.

---

### 2026-02-22 — voice-and-values.md split into values.md and voice.md

**Affects:** core/nla-foundations.md, core/skills/startup.md, core/skills/maintain.md,
core/skills/validate-architecture.md, core/skills/validate-structural.md,
core/skills/preferences.md, core/skills/export.md, core/skills/friction-log.md,
install/structure-intent.md, install/CLAUDE-intent.md, install/skills-intent.md

The single `app/shared/voice-and-values.md` file is now two files:
- **`app/shared/values.md`** — commitments, priorities, non-negotiables. Loaded at
  startup as infrastructure. Present during both execution and maintenance.
- **`app/shared/voice.md`** — tone, personality, style. Stays as task-level shared
  context, referenced by task doc prerequisites.

A new principle (#3, "Values Are Visible") was added to nla-foundations.md, renumbering
the existing principles 3-6 to 4-7. This loads automatically via the framework.

**What to do in your project:**
1. Split `app/shared/voice-and-values.md` into `app/shared/values.md` and
   `app/shared/voice.md`. Values get the priority/tradeoff/non-negotiable content;
   voice gets tone, personality, style, and editorial standards.
2. Update task doc prerequisites to reference `voice.md` instead of `voice-and-values.md`
   (values are loaded at startup, so they don't need to be in task prerequisites).
3. Update any references in `app/overview.md` and `CLAUDE.md` that mention
   `voice-and-values.md`.
4. Delete the old `voice-and-values.md` after confirming the split is complete.

The multiple-voices pattern is now explicitly supported: an NLA can have multiple voice
files (`voice-newsletter.md`, `voice-social.md`) referenced by different task docs.
Values remain singular — one set of values per NLA.

The validate architecture review now includes a "values consistency" analytical category
that checks whether docs and behaviors align with stated values. The maintain skill
now surfaces tensions between proposals and values ("are you sure?").

---

### 2026-02-21 — New /unpack skill for conversation structure

**Affects:** install/skills-intent.md

A new `/unpack` skill helps structure complex conversations — when multiple threads,
questions, or decision points are bundled together, it lays them out and works through
them sequentially. Think of it as a facilitation technique: the AI identifies what's
on the table, proposes the set for confirmation, works through them one at a time, and
tracks progress visibly.

**What to do in your project:**
- Create `.claude/skills/unpack/SKILL.md` — standard thin wrapper (the intent diff
  shows the reference wrapper)
- Add `/unpack` to your CLAUDE.md skills table

The skill is additive — no existing behavior changes. Unlike phase skills (/think,
/debrief), this is a technique that layers on top of whatever's already active. It
can be invoked mid-conversation during thinking, maintenance, or domain work without
interrupting the active context.

---

### 2026-02-21 — New /debrief skill for post-work reflection

**Affects:** install/skills-intent.md

A new `/debrief` skill formalizes the reflection step after substantive work. It's
the bookend to `/think` — think explores what/why before work, debrief reflects on
process and experience after work. Together they complete the four-phase flow:
think → plan → implement → debrief.

**What to do in your project:**
- Create `.claude/skills/debrief/SKILL.md` — standard thin wrapper (the intent diff
  shows the reference wrapper)
- Add `/debrief` to your CLAUDE.md skills table

The skill is additive — no existing behavior changes. It's lightweight by design:
the AI surfaces 3-5 prioritized observations about process and human experience,
collaborates with the human to refine them, then suggests where they should land
(/friction-log for self-directed, /write-letter for upstream feedback). The AI
suggests debrief at task transitions, not wired into other skills' closing steps.

---

### 2026-02-21 — New /think skill for collaborative design exploration

**Affects:** install/skills-intent.md, core/skills/maintain.md

A new `/think` skill creates space for collaborative design exploration — thinking
through *what* to build and *why* before planning mode handles the *how*. It's a
lightweight skill focused on conversational posture rather than procedure: the AI
is already good at collaborative thinking when it knows that's its job.

**What to do in your project:**
- Create `.claude/skills/think/SKILL.md` — standard thin wrapper (the intent diff
  shows the reference wrapper)
- Add `/think` to your CLAUDE.md skills table

The skill is additive — no existing behavior changes. It fits into a four-phase flow:
think (what/why) → plan (how) → implement → debrief. Not every task needs thinking
mode — mechanical fixes and well-specified features can skip straight to planning.
It's most valuable when the work involves design judgment, unfamiliar territory, or
multiple valid approaches.

`/maintain`'s Principle 2 now references `/think` as the phase before planning mode.
This propagates automatically via the thin wrapper.

---

### 2026-02-20 — New /export skill for plugin distribution

**Affects:** install/skills-intent.md

A new `/export` skill converts your NLA project into a self-contained plugin for Claude
Code or Cowork. Think of it as compiling: the NLA project is your source code, the plugin
is the artifact you ship. The plugin bundles all dependencies (framework skills are
resolved and inlined, shared context is copied per skill, paths are rewritten) so it
works without the framework directory.

**What to do in your project:**
- Create `.claude/skills/export/SKILL.md` — standard thin wrapper (the intent diff shows
  the reference wrapper)
- Add `/export` to your CLAUDE.md skills table

The skill is additive — it doesn't change any existing behavior. You only need it when
you're ready to distribute your NLA as a plugin.

**What the export does:** Inventories your skills, classifies them (domain skills become
auto-invocable, dev tools stay hidden, startup is absorbed into a foundation skill),
resolves all framework references, bundles shared context, and generates a plugin
directory at `../[project-name]-plugin/`.

---

### 2026-02-19 — /plan skill removed, design thinking folded into /maintain

**Affects:** install/skills-intent.md, core/skills/maintain.md

The `/plan` skill has been removed from the framework. Its design thinking concepts
(structure gradient, learning loop design) are now part of `/maintain`'s Principle 2
("Confirm Before Implementing"). Implementation planning is handled by Claude Code's
built-in plan mode, which activates naturally for larger changes.

**What to do in your project:**
- Delete `.claude/skills/plan/` (the wrapper is now orphaned)
- Remove `/plan` from your CLAUDE.md skills table
- Remove `/plan` from your README.md if listed
- Update `reference/system-status.md` if it lists /plan as a skill

This is simplification, not loss of capability. The behavior you got from `/plan` is
now delivered by `/maintain` (NLA-specific design thinking) plus Claude Code plan mode
(implementation mechanics). If you had `/plan` in your config.md directives (e.g.,
"always use /plan before changes"), update those to reference "planning mode" generally.

---

### 2026-02-19 — Maintenance learnings captured in foundations, validate, maintain

**Affects:** core/nla-foundations.md, core/skills/validate-architecture.md, core/skills/maintain.md

Three core files now carry learnings from the first cross-NLA feedback session:

- **Foundations** ("How to Read This System"): A note about language encoding assumptions —
  narrow language causes narrow NLA behavior, and broadening language is usually more effective
  than adding rules. All projects load this automatically.

- **Validate architecture review**: New analytical category "Language breadth" — checking
  whether docs assume a specific NLA shape when they should be shape-neutral.

- **Maintain skill**: Two enrichments folded into existing principles and processing
  guidance — broadening over adding (Principle 1) and proportional resolution
  (feedback/friction processing). Principle 2 already had pre-flight/post-validate
  guidance from the earlier validate dispatcher update.

No action needed — these propagate automatically via `../nla-framework/`. If you ejected
any of these files, review the changes and consider whether to incorporate them.

---

### 2026-02-19 — Output spec is now optional

**Affects:** core/skills/startup.md, core/skills/validate-structural.md, core/skills/maintain.md, install/structure-intent.md, install/skills-intent.md

`app/shared/output-spec.md` is no longer assumed to exist in every NLA. The startup
skill loads it only if present (same pattern as config.md). Validate no longer flags
its absence unless a task doc references it. The maintain skill and intent files treat
it as conditional.

This reflects that not every NLA needs a dedicated output spec file. Classification
NLAs, conversational NLAs, and NLAs with simple output can put format guidance directly
in their task docs. NLAs with complex or shared output format concerns still benefit
from the file — it just isn't mandatory.

Existing projects with output-spec.md: no changes needed. Everything works as before.
Projects without one: you'll no longer see it flagged as missing.

---

### 2026-02-19 — Startup extensibility and scaffold reference cleanup

**Commit:** 0d6b1b2
**Affects:** core/skills/startup.md, install/CLAUDE-intent.md, install/skills-intent.md

The startup skill now supports app-specific initialization via `app/startup.md`. After
loading foundational context, the skill checks if this file exists and follows it. This
is where apps define additional startup steps — scanning for active work, checking
environment, presenting status — without ejecting the thin wrapper.

If your project ejected the startup wrapper to add custom startup behavior, you can
now un-eject: restore the thin wrapper and move your custom logic into `app/startup.md`.
The framework handles universal context loading; your file handles domain-specific steps.
This is optional — ejected startups continue to work fine.

The hardcoded `/format-article` task identification table was replaced with generic
guidance that consults `app/overview.md`. Projects using the thin wrapper get this
automatically; ejected startups are unaffected.

---

### 2026-02-19 — Cardinal Rule broadened, NLA Shapes added, TK references removed

**Commit:** 25e9c00
**Affects:** core/nla-foundations.md, install/CLAUDE-intent.md, install/skills-intent.md

The Cardinal Rule changed from "the human must always be able to compare changes
against the original and easily revert" to "the human decides." The old framing was
transformation-specific — it assumed an original to compare against. The new framing
is universal across stateless, persistent, and creative NLAs.

Projects with custom Cardinal Rule language in their CLAUDE.md: check whether your
framing is already aligned with the broader principle. If so, no change needed.

NLA Shapes (stateless, persistent, tool-using) was added to nla-foundations.md. This
is loaded by all projects automatically via `../nla-framework/`. Consider whether your
overview.md reflects which shape your NLA is.

A new Principle 6 (Configuration Is Natural Language) was added to nla-foundations.md.
Also loaded automatically. No project changes needed, but it may inform how projects
think about their config-spec.

TK note references were removed throughout — "flag uncertainty" replaces "use TK notes."
Projects using TK conventions in their own docs can keep them (they're domain choices),
but framework-generated references now use the general language. The domain skill
pattern in skills-intent.md has updated guardrails.

---

*This file is maintained during `/maintain` sessions and read by `/update` when
proposing changes to domain projects. See `reference/design-rationale.md` for the
full design.*
