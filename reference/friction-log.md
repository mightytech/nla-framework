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

### 2026-02-21 — Post-session reflection as a skill (debrief / retrospective)

**Type:** process
**Severity:** major
**Blast radius:** all projects
**Status:** pending

**Observation:**
After running `/update` on penny post, the user asked the AI to reflect on the process:
"Think about what we just went through. Was there anything that could be improved?" That
open-ended reflection produced an 11-item feedback letter (Issue #5) — 3 items triaged
today, all accepted. The reflection wasn't prompted by a skill or a step in the update
flow. It was an informal question that happened to produce high-quality, actionable
feedback.

This suggests a general-purpose "debrief" skill that runs after major work: updates,
maintenance sessions, app execution (create-app, Duet composition, Copydesk formatting).
The AI reflects on what just happened while context is fresh.

**Two dimensions of reflection:**

1. **Process:** Ambiguities in instructions, inefficiencies in the flow, missing steps,
   places where the AI had to guess or improvise. What worked, what didn't, what could
   be streamlined.

2. **Human experience:** How did the human seem during the process? Content, confused,
   frustrated, excited? Did they hesitate before approving something? Did they shorten
   their responses (possible fatigue or impatience)? Were there too many confirmation
   steps? These are observations the human might not consciously articulate but the AI
   can surface from its position as participant-observer.

**The collaborative refinement step is essential.** The AI surfaces 3-5 prioritized
observations. The human pushes back on some, develops others, adds their own. Together
they produce feedback that feeds into the friction log (self-directed) or a penny post
letter (directed at a package or the framework).

**Evidence:** Issue #5 on this repo — penny post's post-update reflection produced 3
accepted items about downstream reference cleanup and validation strengthening in the
update skill. The process worked; it just isn't formalized.

**Discussion notes (from initial conversation):**

- **The LLM's unique position.** It was present for the entire interaction, read the
  same instructions, made judgment calls, and observed reactions. This connects to the
  "LLM self-aware diagnostics" insight from the export session — the AI can trace its
  own reasoning chain AND reflect on the human's experience.

- **Missing step in the learning loop.** Do work → reflect → capture → act. Steps 3-4
  exist (friction-log, write-letter, maintain). Step 2 is currently informal.

- **Bookend with "thinking it through."** That friction log entry is about reflection
  BEFORE implementation (design thinking). This is about reflection AFTER execution.
  Same meta-concern: the framework supports doing work well but has less support for
  thinking about work.

- **Timing is critical.** Must happen while context is fresh — before conversation
  compression loses the details that make reflection valuable.

- **Naming.** "Post-mortem" implies failure. `/debrief` or `/reflect` fits better — this
  is about learning from the full experience, including what went well.

- **Scope control.** Risk of producing a wall of observations after a long session.
  Prioritize — 3-5 observations ranked by impact, with the human choosing which to
  develop.

- **Dual destination.** Output may be letter-ready (aimed at a package or framework) or
  self-directed (friction-log material about the project's own docs). The skill needs
  to handle both.

**Affected files:**
- New skill in `core/skills/` (blast radius: all domain projects)
- `install/skills-intent.md` — new skill wrapper
- Potentially `core/skills/maintain.md` — session close could prompt for debrief

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
**Status:** pending

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
