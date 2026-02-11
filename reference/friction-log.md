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

---

## Patterns to Watch

*Recurring themes that may need deeper attention:*

1. **Two-hop reading** — The LLM reads a wrapper, then a framework file, then domain files. Watch for confusion or context loss in the chain.

2. **Path resolution** — Domain projects use `../nla-framework/` paths. Watch for breakage when projects are in unexpected locations.

3. **Scaffold drift** — As the framework evolves, scaffold may fall behind. Track gaps between scaffold content and current best practices.

---

*This log is maintained by the `/friction-log` skill (which creates entries) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
