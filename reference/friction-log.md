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

### 2026-02-14 — Duet maintenance session: 9 framework-level learnings

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** pending

**Observation:**
Duet's first major maintenance session (resolving all founding friction log entries) surfaced nine patterns that appear framework-general, not app-specific. The full analysis with suggested markdown additions is at `reference/feedback/2026-02-14-duet-maintenance-learnings.md`.

Summary of gaps (items 1–9), NLA config insight (item 10), and assumptions to broaden (item 11):
1. No guidance on artifact persistence (multi-session work)
2. No session bridge / context file pattern
3. No lifecycle skill template (snapshot/shelve/finish/resume)
4. Startup skill not extensible (had to fully replace it)
5. No environment management pattern for external tools
6. Output spec should be tool-specific, not generic
7. No discussion of AI executing its own output (auto-play pattern)
8. `/create-app` doesn't ask about persistence, tools, or lifecycle
9. No structured NLA → framework feedback channel (the letter itself is the prototype)
10. Natural language config is a fundamental NLA capability — enums are defaults, prose is the real interface. Users can modify any setting with "option X, but..." The LLM IS the extension system.
11. Framework assumptions reveal transformation-NLA origin:
    - Cardinal Rule framing is transformation-specific
    - Startup skill leaks scaffold references (`/format-article`)
    - Scaffold shapes expectations toward stateless transformation
    - Validate skill assumes deterministic output

**Affected files:**
- `core/nla-foundations.md` — Stateless vs. persistent NLAs, tool execution, NLA config capabilities, broaden Cardinal Rule
- `core/skills/startup.md` — Two-phase extensibility, remove scaffold-specific references
- `core/skills/validate.md` — Add guidance for non-deterministic NLAs
- `core/skills/maintain.md` — Processing feedback letters
- `.claude/skills/create-app/SKILL.md` — Deeper scaffolding questions
- `scaffold/` — Templates for context files, lifecycle skills, environment.md; notes acknowledging this is one shape of NLA

**Proposed fix:**
Process the feedback letter item by item via `/maintain`. Each learning can be accepted, adapted, or deferred independently. The letter includes specific suggested markdown for several items.

**Notes:**
This is the first "maintenance exit interview" — the pattern itself (item #9) is proposed as a framework feature. If adopted, `reference/feedback/` becomes the inbox for NLA → framework learnings.

---

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
