# Friction Log

Running log of learnings from NLA operation and human feedback. Each entry captures something worth remembering — problems, surprises, or things that worked well.

---

## How to Use This Log

**When to add entries:**
- After observing a correction or gap
- When you notice a pattern across multiple outputs
- When something works surprisingly well
- When something fails unexpectedly

**Entry types:**
- `output` — How the NLA formatted content
- `process` — How the workflow functioned
- `documentation` — Clarity or gaps in the docs

**Severity includes positive:** Capture what works, not just what breaks.

---

## Entry Format

```markdown
## [DATE] — [CONTENT or CONTEXT]

**Type:** output | process | documentation
**Severity:** positive | minor | major
**Task:** [which task]
**Status:** pending | resolved | deferred | wont-fix

**Observation:**
[What happened or was noticed]

**Before:** [What the NLA produced]
**After:** [What the human wanted]

**Confirmed reason:**
[The human's explanation — their words, not a summary]

**Generalizable:** [yes | no | partially]
[Under what conditions does this apply?]

**Affected documentation:**
[Which app/ file and section would need to change]

**Proposed fix:**
[Specific enough for /maintain to act on]

**Notes:**
[Additional context, related entries, patterns noticed]
```

Not every entry needs all fields. The essentials are: Observation, Type, Severity, Status. The Before/After, Confirmed reason, and other fields are valuable when you have them — richer entries are more useful to `/maintain`. Include what you have; don't force what you don't.

**When `/maintain` resolves an entry**, it updates the Status field:
```markdown
**Status:** resolved
**Resolved:** [DATE] — [brief description of what was changed and where]
```

---

## Entries

*Entries are added chronologically, newest first.*

---

### Example Entry — First Run Review

**Type:** documentation
**Severity:** positive
**Task:** format-article
**Status:** resolved
**Resolved:** Template setup — initial configuration complete

**Observation:**
First run of the NLA produced reasonable output with the sample voice and patterns. The structure gradient is working: human provided rough text, LLM added formatting and structure, output spec ensured consistent format.

**Action:**
- [x] Confirmed template docs are internally consistent
- [x] Verified learning loop works (this entry is the proof)

**Notes:**
This entry exists to demonstrate the friction log format. Replace it with real entries as you use the system.

---

## Patterns to Watch

*Recurring themes that may need deeper attention:*

1. **Link text quality** — Generic link text ("click here") vs descriptive text. Watch for patterns in what humans change.

2. **Header placement** — When do humans add headers the NLA missed? When do they remove headers the NLA added?

3. **Emphasis selection** — Which quotes do humans un-emphasize? What makes a quote "worthy"?

---

*This log is maintained by the `/friction-log` skill (which creates entries from any context) and the `/maintain` skill (which resolves and archives them). Resolved entries are moved to `friction-log-archive.md`.*
