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

### 2026-02-19 — README directory tree falls out of sync on every file change

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** pending

**Observation:**
The README's directory tree is a manual mirror of the filesystem. Every time a file is
added, moved, or deleted, the tree may need updating — but because the README isn't in
any functional chain (not read by skills, not loaded at startup, not an intent file),
there's no natural trigger to check it. The maintainer's mental model of "what needs
updating" is driven by functional blast radius, and the README is outside that model.

This keeps showing up in `/validate` structural checks. The system catches it reliably,
but after the fact — creating a recurring low-severity finding in every validation pass
that involves file changes.

**Proposed fix:**
Add a brief reminder to the maintain skill's file-creation workflow: "If you created,
moved, or deleted files, check that README.md's directory tree is current." Small
friction cost, prevents the recurring validate finding. Alternatively, accept that
validate catches it and don't add prevention — the cost of a stale README line is low.

**Notes:**
The deeper pattern: documentation artifacts that mirror filesystem state will always
drift unless there's a trigger in the workflow that creates the drift. This applies
to README trees, but could also apply to any manually-maintained index or listing.

---

### 2026-02-19 — Pre-flight design review caught gaps before implementation

**Type:** process
**Severity:** positive
**Blast radius:** maintainers
**Status:** pending

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

## Patterns to Watch

*Recurring themes that may need deeper attention:*

1. **Two-hop reading** — The LLM reads a wrapper, then a framework file, then domain files. Watch for confusion or context loss in the chain.

2. **Path resolution** — Domain projects use `../nla-framework/` paths. Watch for breakage when projects are in unexpected locations.

3. **Intent file completeness** — As the framework evolves, intent files must stay in sync. Track gaps between what `/create-app` needs and what intent files provide.

4. **Language breadth** — Domain-specific language leaking into framework-general docs. The framework was built around a transformation NLA; watch for words that assume transformation, deterministic output, or a specific workflow when the context should be shape-neutral.

---

*This log is maintained by the `/friction-log` skill (which creates entries) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
