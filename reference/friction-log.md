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

### 2026-02-22 — Package creation relies on pattern-matching against existing packages

**Type:** intent
**Severity:** minor
**Blast radius:** maintainers / package creators
**Status:** pending

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

**Evidence that the pattern works:**
The process helpers package was created in one pass with no structural errors — validate
found zero issues. The penny post template was unambiguous enough to follow. This is
positive evidence that the conventions are sound; the question is discoverability.

**Possible approaches (not yet decided):**
1. **Package structure intent file** — `install/package-intent.md` describing what a
   well-formed package looks like, parallel to structure-intent.md for domain projects.
   Could be read by a future `/create-package` skill.
2. **Documentation** — describe the package pattern in CONTRIBUTING.md or a new doc.
   Lighter touch, sufficient for human readers and AI maintainers.
3. **Wait for more evidence** — two packages is a small sample. A third might reveal
   conventions the first two don't share.

**Notes:**
This is not urgent. Two packages exist and both are well-structured. The risk is that
a third package creator (human or AI) without access to penny post or process helpers
as a reference would struggle with conventions that are currently implicit. The
/think → plan → implement flow that produced process helpers was smooth precisely
because penny post provided a strong template.

---

### 2026-02-22 — Process helpers package creation went smoothly end-to-end

**Type:** process
**Severity:** positive
**Blast radius:** maintainers
**Status:** pending

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
