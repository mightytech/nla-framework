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

### 2026-02-22 — "Adding a New Skill" checklist not surfaced during skill creation

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** pending

**Observation:**
When adding `/check-updates` as a new core skill, three of seven steps in the
`core/skills/README.md` "Adding a New Skill" checklist were missed: creating the
framework's own wrapper, updating the What's Here table, and updating the README
directory tree. `/validate` caught all three post-implementation.

The checklist exists and is correct — it just wasn't consulted during implementation.
The maintain skill's "Updating Core Skill Logic" section and the plan file both
focused on the core logic and intent files, not the mechanical registration steps.

**Proposed fix:**
Reference the checklist in `core/skills/maintain.md` or the maintain skill's
"Updating Core Skill Logic" section — something like "When adding a new skill,
follow the checklist in `core/skills/README.md`." This surfaces it at the moment
it's needed rather than relying on the maintainer to remember it exists.

**Affected files:**
- `core/skills/maintain.md` (or `.claude/skills/maintain/SKILL.md`)

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
