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
