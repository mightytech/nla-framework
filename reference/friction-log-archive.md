# Framework Friction Log Archive

Resolved and closed friction log entries, moved here from `friction-log.md` during `/maintain` sessions. This keeps the active friction log lean while preserving history for pattern analysis.

**How entries get here:** When `/maintain` resolves a friction log entry, it moves the complete entry (including the `**Resolved:**` line) from the active log to this archive.

**Searching:** Use grep to search this archive when looking for historical patterns. The `/friction-log` skill searches here automatically before creating new entries.

---

## Entries

*Archived entries in reverse chronological order.*

### 2026-02-22 — Package creation relies on pattern-matching against existing packages

**Type:** intent
**Severity:** minor
**Blast radius:** maintainers / package creators
**Status:** resolved
**Resolved:** 2026-02-22 — Created `install/package-intent.md` describing package conventions as a diff from domain project intent files. Lightweight approach: start from structure-intent.md and CLAUDE-intent.md, apply documented differences.

**Observation:**
When creating the process helpers package (the second NLA extension), every file was
pattern-matched against penny post's structure — CLAUDE.md, app/overview.md, install
manifest, reference files, skill wrappers. This worked well (the package was created
quickly and cleanly), but the conventions live implicitly in penny post's files, not
explicitly anywhere.

If penny post didn't exist, creating a package would mean guessing at conventions:
what goes in install/, how the CLAUDE.md differs from a domain project's, how skill
wrappers work for package skills vs. framework skills, what reference files to include.
The intent files (CLAUDE-intent.md, skills-intent.md, structure-intent.md) describe
what a *domain project* needs, but there's no equivalent for what a *package* needs.

**Notes:**
Resolved with a "diff from baseline" approach — package-intent.md describes only what
differs from domain project conventions, inheriting the rest from structure-intent.md
and CLAUDE-intent.md. Verified by creating and inspecting a throwaway test package.

---

### 2026-02-22 — Process helpers package creation went smoothly end-to-end

**Type:** process
**Severity:** positive
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Archived as baseline. No action needed; positive observation recording the first complete four-phase flow (think → plan → implement → debrief) for package creation.

**Observation:**
The full workflow for creating the process helpers package — /think (4 exchanges to
reach the key insight), plan mode (mechanical after thinking), implementation (28 files
created in one pass), structural validate (zero issues) — worked cleanly. This is the
first time the four-phase flow (think → plan → implement → debrief) was used for a
complete package creation.

Notable positives:
- /think produced the design insight ("preference, not infrastructure") quickly
- Penny post conventions transferred cleanly to a second package (see related entry)
- The structural validate confirmed the /unpack removal was thorough
- Session pacing was good throughout — no confirmation fatigue

**Notes:**
Worth preserving as a baseline. If future package creation hits friction, this session
provides a comparison point for what smooth looks like.

---

### 2026-02-22 — "Adding a New Skill" checklist missing framework wrapper step

**Type:** documentation
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Added step 2: create `.claude/skills/[name]/SKILL.md` wrapper with project-relative paths

**Observation:**
The "Adding a New Skill" checklist in `core/skills/README.md` has 6 steps but doesn't
include creating a `.claude/skills/[name]/SKILL.md` wrapper in the framework itself.
When adding a new framework skill (as was done for think, debrief, unpack, export),
this step is essential — without the wrapper, the skill isn't discoverable by Claude Code.

**Affected files:**
- `core/skills/README.md`

---

### 2026-02-22 — Framework install/update wrappers use wrong path prefix

**Type:** core
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Changed `../nla-framework/core/skills/` → `core/skills/` in both wrappers

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

**Notes:**
The friction is minor per occurrence but compounds — each stale entry costs
a future session time to investigate whether it's actually pending or already
done. The fix is proportional: one line of guidance, not a new mechanism.

---

### 2026-02-22 — Voice and values may need splitting; values as transparent ethics

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
conceptually different things bundled into one file. Voice might vary by context — the
same NLA could use different tones for different platforms or audiences. Values should
be stable across all contexts. The split makes values infrastructure (loaded at startup)
and voice task-level shared context. A new "Values Are Visible" principle was added to
nla-foundations.md. Values range from stylistic preferences to legal requirements.

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
in Claude Cowork. Users who build NLAs today are locked to Claude Code as the runtime.
Cowork reaches non-technical users who work with voice, tone, and content daily but
don't use a terminal.

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
through them one at a time. The user noted this chunked pattern was highly effective.
The discussion evolved from "formalize the pattern" to "this is a distinct skill" — a
facilitation technique that layers on top of active context rather than replacing it.

---

### 2026-02-21 — "Thoughts? Concerns? Ideas? Questions?" is an AI invitation, not a human prompt

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Rewrote the "Keep the conversation open" bullet in
`core/skills/think.md`. Old language ("End substantive responses with an invitation")
read as "ask the human." New language explicitly says: when the human responds, treat
it as an invitation to share YOUR thoughts, concerns, ideas, and questions.

**Observation:**
During the debrief skill design session, the AI used "Thoughts? Concerns? Ideas?
Questions?" as a conversation closer directed at the human — "your turn to respond."
The intended pattern (established in /think) is the opposite: it's an invitation for
the AI to share ITS own thoughts, concerns, ideas, and questions in response to what
the human just said. The human's response IS the prompt; the AI treats it as if the
human had asked "do you have thoughts, concerns, ideas, or questions about this?"

**Before:** AI ends with "Thoughts? Concerns? Ideas? Questions?" as a volley back to
the human — functionally equivalent to "what do you think?"

**After:** AI receives human input and responds with its own perspective — concerns it
sees, ideas it wants to float, questions it has. The named practice is about the AI's
posture (bring expertise, engage substantively), not turn-taking.

**Affected files:**
- `core/skills/think.md` — the "Keep the conversation open" bullet

---

### 2026-02-21 — Post-session reflection as a skill (debrief / retrospective)

**Type:** process
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Created `/debrief` skill (`core/skills/debrief.md`) as a
lightweight reflection tool. Added to `install/skills-intent.md`, `CLAUDE.md`, and
`README.md`. Design rationale entry covers transition-sensitive triggers, judgment-based
handoff, and two-dimension reflection model.

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

### 2026-02-20 — Need a "thinking it through" mode for design exploration

**Type:** process
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Created `/think` skill (`core/skills/think.md`) as a lightweight
collaborative design exploration mode. Added to install/skills-intent.md, CLAUDE.md, README.md.
Updated maintain.md Principle 2 with thinking phase reference. See session log
`reference/sessions/2026-02-21-think-skill.md` and design rationale entry.

**Observation:**
There's a gap between "exploring what and why" and "planning how to implement." Claude
Code's plan mode is implementation-oriented — it wants to produce steps and exit with an
actionable plan. `/maintain` is execution-oriented — it wants to edit files. The old
`/plan` skill was removed because it overlapped with both. But the *thinking space* —
collaborative exploration of what to build and why — doesn't have a dedicated home.

During the plugin export design session, we needed to:
- Walk through key decisions and their rationale
- Challenge assumptions (e.g., "should dev tools ship in plugins?")
- Explore paradigm-level questions (what does a feedback loop look like when distributed?)
- Capture evolving understanding without committing to implementation

Plan mode kept pushing toward decisions (AskUserQuestion with multiple choice options)
and action (ExitPlanMode). The actual design thinking happened by working around the
mode, not within it.

This isn't just a framework gap — it's a gap in how NLAs are designed. The "what and
why" phase is where the most important decisions happen. It deserves its own support,
separate from implementation planning.

**Notes:**
Related to the /plan removal (2026-02-19). /plan was removed because it overlapped with
maintain + plan mode. But what it offered — and what's now missing — is a space for
design thinking that isn't rushing toward implementation. The fix might not be a new
skill. It might be guidance in maintain or foundations about how to hold a design
conversation. Or it might be something else entirely. Needs its own thinking session.

---

### 2026-02-19 — README directory tree falls out of sync on every file change

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-19 — Added "Check documentation mirrors" step to session close in both core/skills/maintain.md and framework wrapper. Triggers on file creation, moves, or deletions.

**Observation:**
The README's directory tree is a manual mirror of the filesystem. Every time a file is
added, moved, or deleted, the tree may need updating — but because the README isn't in
any functional chain (not read by skills, not loaded at startup, not an intent file),
there's no natural trigger to check it. The maintainer's mental model of "what needs
updating" is driven by functional blast radius, and the README is outside that model.

This keeps showing up in `/validate` structural checks. The system catches it reliably,
but after the fact — creating a recurring low-severity finding in every validation pass
that involves file changes.

**Notes:**
The deeper pattern: documentation artifacts that mirror filesystem state will always
drift unless there's a trigger in the workflow that creates the drift. This applies
to README trees, but could also apply to any manually-maintained index or listing.

---

### 2026-02-19 — Pre-flight design review caught gaps before implementation

**Type:** process
**Severity:** positive
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-19 — Strengthened Principle 2 in maintain skill with a named "Pre-flight review" sub-section. Added specific checklist (gaps, unconsidered alternatives, unintended consequences, cost/benefit, scope, maintenance burden) drawn from what pre-flight has actually caught across sessions. Both core/skills/maintain.md and framework wrapper updated.

**Observation:**
After drafting the update notes design in design-rationale.md, we did a critical re-read
before implementation — checking for gaps, viability, appropriateness to the framework,
and extraneous content. It caught two real gaps (multi-commit sessions, core vs. intent
file distinction in notes) that would have surfaced during implementation at higher cost.

This is a distinct activity from the existing `/validate` modes: those check what exists
(coherence of the document chain, scenario traces, debug). This checks what's proposed
(is a design complete and viable before building it). Worth repeating for future designs.

**Notes:**
Not yet clear where this belongs — could be a `/validate` mode, a `/maintain` best
practice, or a standalone pattern. Watch for recurrence before deciding.

---

### 2026-02-14 — Duet maintenance session: 9 framework-level learnings

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved — 2026-02-19. All 11 items processed in session `reference/sessions/2026-02-19-duet-feedback-and-update-notes.md`. Items 1-7, 9-11 implemented across foundations, startup, validate, maintain, create-app, and intent files. Item 8 addressed with light-touch NLA shape prompt in create-app (may revisit if insufficient). Update notes system designed and implemented for propagating changes to domain projects.

---

### 2026-02-11 — /create-app generates everything upfront; large apps may benefit from skeleton + /maintain

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-18 — Added `/maintain` as development cycle guidance in post-creation steps; added complex project edge case (4+ tasks → generate skeleton + one starter task, defer the rest to `/maintain`).

**Observation:**
`/create-app` currently generates all files with full content — voice, patterns, task docs, output spec, reference files. This works well for small, focused apps (1-2 tasks). For larger apps with many tasks or complex domain logic, generating everything in one pass may produce shallow content that needs immediate rework.

A better pattern for larger apps: `/create-app` generates the skeleton structure (directories, thin wrappers, minimal shared context, one starter task), then instructs the user to run `/maintain` sessions to flesh out the domain content iteratively.

Additionally, even for small apps, users should be told that running `/maintain` is a natural next step after creation — to refine voice, add patterns based on early usage, and iterate on the task doc after seeing real output.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Add guidance for large apps; always mention `/maintain` in post-creation steps

**Proposed fix:**
Two changes: (1) For complex projects (many tasks, unclear domain), `/create-app` should generate a working skeleton with one task and instruct the user to flesh out additional tasks via `/maintain`. (2) Post-creation instructions should always mention that `/maintain` is how the app improves — not just for fixing problems, but for iterating on initial content.

**Notes:**
This connects to the framework's core philosophy: iterate through documentation. `/create-app` gets you started; `/maintain` is the development cycle. Making this explicit in the post-creation message reinforces the right mental model.

---

### 2026-02-12 — AI maintainer executed changes without confirming strategy

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-12 — Added assessment step to friction log processing in both `/maintain` skills (core and framework). Straightforward fixes proceed directly; entries requiring new functionality or design decisions get discussed first, with `/plan` if scope warrants it.

**Observation:**
During friction log processing, the AI maintainer treated entry #1 ("ask where to save project") the same as entry #3 ("remove scaffold path") — jumping straight to execution without discussing the approach. Entry #3 was a straightforward removal; entry #1 involved design decisions (when to ask, how to handle non-sibling paths, how much complexity to add). The result was over-engineered changes that had to be reverted.

The pattern: not all friction log entries are equal. Some are "remove X" (clear action, small blast radius). Others are "add Y" (design decisions, trade-offs, dependencies on other work). The AI should distinguish between these and propose before editing on anything that involves design.

**Proposed fix:**
Add guidance to the `/maintain` skill (or to the AI's own memory) that friction log entries requiring new functionality — as opposed to removing or simplifying existing functionality — should be discussed before implementation. The plan mode pattern worked well for entry #3; it should have been used for entry #1 as well, with more attention to the design questions before exiting the plan.

---

### 2026-02-12 — Framework could generate config files for new NLAs

**Type:** core
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-12 — Implemented NLA configuration system. Created `core/skills/preferences.md` (framework skill logic), scaffold config files (`config-spec.md`, `config.md`, `config/`), thin wrapper, and integrated with `/startup`, scaffold `CLAUDE.md`, `overview.md`, `README.md`, `system-status.md`, and `/create-app`. Design rationale in `reference/design-rationale.md` under "Future Direction: NLA Configuration."

**Observation:**
NLA projects need a way for app users to modify behavior without modifying the application itself. Traditional config (YAML, JSON) is too rigid for an LLM runtime. Natural language config (Markdown) lets users express preferences from structured paths to behavioral directives — the LLM reads and applies them with judgment.

**Notes:**
Design rationale covers: three-actor model (framework devs, app devs, app users), quarterback pattern (light main config routes to sub-configs by context), three-layer git separation, generic `/preferences` framework skill + app-specific `config-spec.md`, conflict/ambiguity detection, integration with `/create-app`.

---

### 2026-02-11 — /create-app should ask where to save the project

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved

**Observation:**
`/create-app` defaults to creating the project in a sibling directory (`../project-name/`). The user is not asked where they want the project saved. The sibling convention is convenient but not technically required — the framework reference paths (`../nla-framework/`) just need to resolve correctly, and CLAUDE.md files in different projects shouldn't interact.

The user should be asked where to save the project. The sibling directory is a sensible default, but users may have different workspace layouts.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Add location question to conversation flow, update path generation logic

**Proposed fix:**
Add a question to the `/create-app` conversation (Phase B or D) asking where to save the project. Default suggestion is `../project-name/`. If the user picks a different location, adjust the framework reference paths in thin wrappers and CLAUDE.md accordingly. Note the two constraints: (1) the framework path must resolve, and (2) CLAUDE.md files from different projects shouldn't be in the same directory tree where Claude Code might pick up both.

**Notes:**
Relates to "Path resolution" in Patterns to Watch. Non-sibling layouts are the main case where `../nla-framework/` breaks. If `/create-app` knows the actual location, it can generate correct paths from the start.

**Deferred 2026-02-12:** Asking about location is simple, but the framework path appears in ~17 places across 8 files in generated projects. Non-sibling support means changing all of them, and there's no single source of truth for the path after creation — moving the project later means manually updating all 17 references. A configuration variable (e.g. `framework_path`) would centralize this. Deferring until the config file design is resolved (see "Framework could generate config files for new NLAs" entry above), then tackling location as part of that.

**Resolved 2026-02-12:** Config system is now implemented. Investigated non-standard locations end-to-end. The config system makes the declaration layer easy (`Framework path:` in config.md), but `core/skills/*.md` files share hardcoded `../nla-framework/` paths across all domain projects. Making these location-agnostic requires either natural language path resolution (adds inference overhead to the common case), template variables (foreign to NLAs), or heavier wrappers. All degrade the default sibling experience to support a rare case. Decision: keep the sibling convention for MVP. Path resolution is a mechanical operation where you want reliability, not LLM flexibility. See `reference/design-rationale.md` "Sibling Directory Convention" for full rationale.

---

### 2026-02-11 — Scaffold path in /create-app conflates example app with side-by-side install

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-12 — Removed scaffold/from-scratch path choice from `/create-app`. Created `/create-sample-app` skill for installing the scaffold as a standalone example project.

**Observation:**
The `/create-app` skill presents a "scaffold path" that installs the sample format-article task alongside the user's custom task. The intent was to help users learn by example, but the scaffold app is better understood as a standalone example application — something you install once to see how a complete NLA works, not something you mix into a real project.

**Before:** `/create-app` offers "scaffold path" (includes sample formatter alongside custom task) vs "from-scratch path" (custom task only). The scaffold path is recommended for first-time users.

**After:** Two cleaner options: (1) A separate skill like `/create-sample-app` that installs the scaffold as a standalone example project, or (2) `/create-app` briefly mentions the scaffold can be installed separately as a reference, without emphasizing it. The scaffold-as-example is probably a one-time thing and shouldn't be a prominent fork in the create flow.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Remove or de-emphasize scaffold path
- Possibly new skill: `.claude/skills/create-sample-app/SKILL.md`
- `scaffold/` — Already works as-is for standalone install

**Proposed fix:**
Remove the scaffold/from-scratch path decision from `/create-app`. Either create a `/create-sample-app` skill that installs the scaffold as a standalone example, or have `/create-app` mention in passing that the scaffold directory can be installed separately. The create flow should focus entirely on the user's custom project.

**Notes:**
The user who surfaced this already had a standalone scaffold project and chose "from scratch" immediately. The scaffold path may never have been the right default — a standalone example app is more useful than a hybrid project.
