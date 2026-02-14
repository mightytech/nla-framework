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
- `scaffold` — Gaps or improvements in the project scaffold
- `process` — How framework maintenance workflows function
- `documentation` — Clarity or gaps in framework docs (README, CONTRIBUTING)

**Severity includes positive:** Capture what works, not just what breaks.

---

## Entry Format

```markdown
### YYYY-MM-DD — [Brief descriptive title]

**Type:** core | scaffold | process | documentation
**Severity:** positive | minor | major
**Blast radius:** all projects | new projects | maintainers
**Status:** pending | resolved | deferred | wont-fix

**Observation:**
[What happened or was noticed]

**Before:** [What the framework produced or did]
**After:** [What was expected or desired]

**Confirmed reason:**
[The human's explanation — their words, not a summary]

**Affected files:**
[Which core/ or scaffold/ files would need to change]

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

### 2026-02-11 — /create-app generates everything upfront; large apps may benefit from skeleton + /maintain

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** pending

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

3. **Scaffold drift** — As the framework evolves, scaffold may fall behind. Track gaps between scaffold content and current best practices.

---

*This log is maintained by the `/friction-log` skill (which creates entries) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
