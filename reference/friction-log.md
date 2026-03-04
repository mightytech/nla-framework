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
[The human's explanation — their words, not a summary]

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

### 2026-03-03 — Framework maintain skill can't use thin wrapper pattern

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** deferred

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

**Why deferred:**
Works fine today, sync burden is manageable. Worth remembering for when the maintain
skill next gets a significant refactor.

---

### 2026-03-03 — Context-aware help/guide skill

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
The framework workflow (startup → maintain → think/plan → validate → debrief → close)
is implicit. Individual skills know what they do but not where they sit in the larger
flow. A new user finishes `/create-app` and has no guidance on what to do next.

A context-aware help/guide skill could: understand where the user is in the workflow,
explain the system as they encounter it, serve as a tour guide for recent framework
changes after `/update`, and adapt to the user's interest level. This is interactive
onboarding, not static documentation.

**Open questions:**
- Does it read session state? Know what skills you've used?
- Is it a mode or a skill you invoke?
- How does it relate to `/startup`?
- Does it replace documentation or complement it?
- The "tour guide for recent changes" angle connects to `/update` — walk through
  what changed and why it matters for your project.

**Proposed fix:**
Design session (`/think`) to work through the concept. This is a new feature, not a
tweak to existing skills.

**Notes:**
Surfaced during debrief. The user has internalized the workflow rhythm but recognized
other users won't. The AI's ability to gauge interest and respond to questions makes
this a natural fit for an NLA skill rather than a static doc.

---

### 2026-03-03 — Session close skill

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
There's no `/close` or `/end` skill to wrap up a session. The maintain skill has
session-close *steps* (finalize log, check README, suggest validation) but they're
buried in the skill doc rather than being an invocable action. From a UX perspective,
an explicit session-close skill signals "we're done" and handles the checklist:
commit, finalize session log (including debrief section), "here's where to pick up
next time."

**Affected files:**
- New: `core/skills/close.md` (or `session-close.md`)
- Update: `core/skills/maintain.md` (session lifecycle section would reference the skill)
- Update: `install/skills-intent.md` (new skill wrapper)

**Proposed fix:**
Create a session-close skill that wraps the existing checklist into an invocable
action. Extract from maintain.md's session lifecycle steps. Include the debrief
section population (brief observations if no explicit /debrief happened, conclusions
from /debrief if it did).

---

### 2026-03-03 — Skills should suggest next steps

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** pending

**Observation:**
Skills have natural successors that aren't surfaced: `/validate` → `/debrief` or fix
findings, `/debrief` → session close, `/install` → `/validate`, `/maintain` (after
resolving items) → `/validate`. Users who know the workflow follow it naturally; new
users don't know what comes next.

**Affected files:**
- `core/skills/validate.md` and mode files
- `core/skills/debrief.md`
- `core/skills/install.md`
- `core/skills/maintain.md`
- Possibly others

**Proposed fix:**
Add brief "next step" guidance to skills at their natural completion points. Light
touch — a sentence, not a workflow engine. E.g., validate's output section could end
with "If you're wrapping up, consider `/debrief`. If findings need fixing, `/maintain`
can address them."

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

2. **Path resolution** — Domain projects use `../nla-framework/` paths. Watch for breakage when projects are in unexpected locations.

3. **Intent file completeness** — As the framework evolves, intent files must stay in sync. Track gaps between what `/create-app` needs and what intent files provide.

4. **Language breadth** — Domain-specific language leaking into framework-general docs. The framework was built around a transformation NLA; watch for words that assume transformation, deterministic output, or a specific workflow when the context should be shape-neutral.

---

*This log is maintained by the `/friction-log` skill (which creates entries) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
