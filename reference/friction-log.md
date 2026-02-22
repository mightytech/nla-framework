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

---

## Patterns to Watch

*Recurring themes that may need deeper attention:*

1. **Two-hop reading** — The LLM reads a wrapper, then a framework file, then domain files. Watch for confusion or context loss in the chain.

2. **Path resolution** — Domain projects use `../nla-framework/` paths. Watch for breakage when projects are in unexpected locations.

3. **Intent file completeness** — As the framework evolves, intent files must stay in sync. Track gaps between what `/create-app` needs and what intent files provide.

4. **Language breadth** — Domain-specific language leaking into framework-general docs. The framework was built around a transformation NLA; watch for words that assume transformation, deterministic output, or a specific workflow when the context should be shape-neutral.

---

*This log is maintained by the `/friction-log` skill (which creates entries) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
