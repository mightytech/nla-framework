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

### 2026-02-22 — Framework install/update wrappers use wrong path prefix

**Type:** core
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** pending

**Observation:**
The framework's own `.claude/skills/install/SKILL.md` and `.claude/skills/update/SKILL.md`
use `../nla-framework/core/skills/` paths — the domain-project convention. Since the
framework's working directory IS `nla-framework/`, these should use project-relative
paths (`core/skills/install.md`, `core/skills/update.md`), matching the pattern used
by the debrief, export, think, and unpack wrappers.

`core/skills/README.md` explicitly states: "The framework's own skills in `.claude/skills/`
use project-relative paths instead." These two wrappers violate that convention.

**Affected files:**
- `.claude/skills/install/SKILL.md`
- `.claude/skills/update/SKILL.md`

**Proposed fix:**
Change `../nla-framework/core/skills/install.md` → `core/skills/install.md` and same
for update. Mechanical fix.

---

### 2026-02-22 — "Adding a New Skill" checklist missing framework wrapper step

**Type:** documentation
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** pending

**Observation:**
The "Adding a New Skill" checklist in `core/skills/README.md` has 6 steps but doesn't
include creating a `.claude/skills/[name]/SKILL.md` wrapper in the framework itself.
When adding a new framework skill (as was done for think, debrief, unpack, export),
this step is essential — without the wrapper, the skill isn't discoverable by Claude Code.

**Affected files:**
- `core/skills/README.md`

**Proposed fix:**
Add a step: "Create `.claude/skills/[name]/SKILL.md` with framework-adapted wrapper
(project-relative paths, framework-specific context notes if needed)."

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

### 2026-02-22 — Session logs fall behind commits

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Added commit-point log sync guidance to both the framework
maintain wrapper (`.claude/skills/maintain/SKILL.md`) and core maintain skill
(`core/skills/maintain.md`).

**Observation:**
Architecture review findings #11 and #14 were fixed in code but the session log
still listed them as unresolved. The fixes were committed — the session log just
wasn't updated to reflect them. This means the session log's "State at Close"
becomes unreliable as a record of what was actually resolved.

**The pattern:**
Fixes happen, a commit goes out, but the session log entry that tracks the work
doesn't get updated before the commit. The next session reads "State at Close"
and sees stale information about what's pending.

**Proposed fix:**
Add guidance to the maintain skill's session lifecycle: update the session log
before every commit, not just at session close. The session log should reflect
reality at each commit point, not just at the end. This is lightweight — just
a sentence in the commit workflow reminding the maintainer to sync the log.

**Notes:**
The friction is minor per occurrence but compounds — each stale entry costs
a future session time to investigate whether it's actually pending or already
done. The fix is proportional: one line of guidance, not a new mechanism.

---

### 2026-02-21 — Conversation structure skill: "slow your roll, let's chunk this"

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Created `/unpack` skill (`core/skills/unpack.md`) as a
lightweight facilitation technique for structuring complex conversations. Added to
`install/skills-intent.md`, `CLAUDE.md`, and `README.md`. Design rationale entry
covers the facilitation technique category, composability, and naming. See session
log `reference/sessions/2026-02-21-unpack-skill.md`.

**Observation:**
During the /debrief design session, the AI presented four design questions and worked
through them one at a time. The user noted this chunked pattern was highly effective —
"I know exactly what we did without reading the actual markdown" — and asked whether
it should be formalized. The discussion evolved from "formalize the pattern" to "this
is a distinct skill."

**The problem it solves:**
The AI sometimes produces long responses with multiple embedded questions or discussion
points. The human faces an awkward choice: answer everything at once (unwieldy —
answering some parts might inform others) or answer partially and risk losing threads
to context compaction. The chunked pattern makes the AI responsible for managing
conversation structure: propose the question set, agree on scope, work through them
one at a time, track what's open and what's resolved.

**The proposed solution:**
A skill the user can invoke mid-conversation — not a mode switch, but an intervention:
"I see where this is going, let's structure it." The AI would:
1. Identify the distinct questions/points in play
2. Propose them as a set for the user to confirm or modify
3. Work through them sequentially, each answer informing the next
4. Track open vs. resolved questions (survives context compaction)

This is different from /think (which explores what/why before work) and /debrief
(which reflects after work). This structures the conversation *during* work — any work,
maintenance or domain execution.

**Why not nla-foundations.md (a general principle):**
Two problems. First, as context grows, principles in foundations get fuzzed out —
the specific behaviors fade. Skills get re-read when invoked, putting guidance at the
top of the context pile. This is observed behavior, not theoretical. Second, a principle
imposes one collaboration style on every NLA user. The chunked pattern is one user's
preferred way of working. Others might want questions written to a file for inline
annotation, or might prefer the wall of text. A skill keeps it available without
imposing it.

**Why not part of /think:**
The /think skill worked this way in the debrief design session, but that was because
the friction log had already decomposed the problem into clear questions. In more
open-ended thinking sessions (like the plugin export design), the questions aren't
obvious at the start — the first phase is figuring out what the questions are.
Imposing "identify your starter questions" too early could force premature structure.

**Why not a session log enhancement:**
Adding "Open Questions" to session logs captures the record but not the process. The
value isn't in logging questions — it's in the AI managing conversation flow so nothing
gets lost and each answer can inform the next. The session log is a side effect, not
the point. (Though open questions in session logs are still worth having for context
compaction resilience.)

**What needs design work:**
- Naming — it's a mid-conversation intervention, not a mode. "Slow your roll" captures
  the spirit but isn't a skill name.
- Interaction model — how does it work when invoked mid-conversation? The AI is already
  in some context (/think, /maintain, domain execution). The skill structures the
  conversation without changing the context.
- Scope — does it only structure questions, or any multi-part exchange? The debrief
  session used it for design questions, but it could apply to multi-part proposals,
  complex feedback, or any situation where dumping everything at once degrades the
  interaction.

**Notes:**
This is new territory — not a reflection tool, not a design tool, but a conversation
structure tool. Deserves its own /think session with fresh context.

---

---

### 2026-02-20 — Need a way to export NLAs for use in Claude Cowork

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-20 — Created `/export` skill (`core/skills/export.md`) that converts
NLA projects into self-contained plugins for Claude Code and Cowork. Added to
`install/skills-intent.md`, `CLAUDE.md`, and `README.md`. Updated design rationale with
plugin export section and wrapper spectrum patterns. See session log
`reference/sessions/2026-02-20-plugin-export-design.md` for full design discussion.

**Observation:**
There's no path for taking an NLA built with this framework and exporting it for use
in Claude Cowork. The design rationale has a "Cowork as a Target Environment" section
with conceptual thinking (skill mimicry via routing tables, discoverability via startup
banners, self-contained generation), but nothing is implemented. Users who build NLAs
today are locked to Claude Code as the runtime.

**Notes:**
Design rationale already covers: routing tables replacing skill discovery, three layers
of discoverability (startup banner, help keyword, context-aware hints), generation
differences by target, and a proposed `/convert` implementation path. Open questions
remain about Cowork's exact instruction mechanism and session continuity model.

This is the gap between "neat geeky idea" and "idea that resonates with many types of
people" — Cowork reaches non-technical users who work with voice, tone, and content
daily but don't use a terminal.

---

### 2026-02-19 — Voice and values may need splitting; values as transparent ethics

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-22 — Split `voice-and-values.md` into `values.md` (startup
infrastructure) and `voice.md` (task-level shared context). Added "Values Are Visible"
principle (#3) to nla-foundations.md. Updated all core skills, intent files, and
create-app. See session `reference/sessions/2026-02-22-voice-values-design.md`.

**Observation:**
Voice (tone, personality, style) and values (ethics, priorities, non-negotiables) are
conceptually different things bundled into one file (`voice-and-values.md`). Voice might
vary by context — the same NLA could use different tones for different platforms or
audiences (Substack vs. Twitter, creative partner vs. educator). Values should be stable
across all contexts — you don't have different ethics for different platforms.

This suggests three potential changes:

1. **Split voice and values** into separate files. Values are stable and universal;
   voice may be contextual. Different lifecycles, different reasons to edit.

2. **Support multiple voices.** Like output-spec, a single voice file works for simple
   NLAs. NLAs with contextual tone needs could have multiple voice files
   (voice-substack.md, voice-twitter.md) referenced by the relevant task doc.

3. **Values as a foundational NLA concept.** Traditional code has always embedded values
   (what gets prioritized, who gets served, what gets filtered), but they're hidden in
   logic — scoring functions, filter criteria, if/else branches. In an NLA, values are
   written in natural language: readable, debatable, and modifiable by anyone who can
   read. "We never sacrifice accuracy for engagement" is a values statement that
   traditional code expresses through opaque logic nobody can inspect. An NLA just
   says it. This transparency is a fundamental capability worth discussing in
   `nla-foundations.md`.

**Affected files:**
- `core/nla-foundations.md` — values transparency as a foundational concept
- `app/shared/voice-and-values.md` convention — splitting, multiple voices
- `core/skills/startup.md` — loading voice context
- `install/structure-intent.md` — file structure
- `install/CLAUDE-intent.md` — runtime identity
- `.claude/skills/create-app/SKILL.md` — conversation flow and generation

**Notes:**
This is a bigger design than output-spec conditionality. Deserves its own session with
fresh context. Captured here so the insights aren't lost.

---

## Patterns to Watch

*Recurring themes that may need deeper attention:*

1. **Two-hop reading** — The LLM reads a wrapper, then a framework file, then domain files. Watch for confusion or context loss in the chain.

2. **Path resolution** — Domain projects use `../nla-framework/` paths. Watch for breakage when projects are in unexpected locations.

3. **Intent file completeness** — As the framework evolves, intent files must stay in sync. Track gaps between what `/create-app` needs and what intent files provide.

4. **Language breadth** — Domain-specific language leaking into framework-general docs. The framework was built around a transformation NLA; watch for words that assume transformation, deterministic output, or a specific workflow when the context should be shape-neutral.

---

*This log is maintained by the `/friction-log` skill (which creates entries) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
