# Update Notes

What's changed in the framework and what it means for your project. Written for both
human readers scanning a changelog and the AI running `/update` as context for proposals.

Not every framework change gets a note — only changes where the *so what for your
project* isn't obvious from the intent diff alone.

For older notes, check `update-notes-archive.md`.

---

## Entry Format

```markdown
### YYYY-MM-DD — [Brief title]

**Affects:** [which intent files or core files changed]
**Commit:** [optional — a hash for precise anchoring, if convenient]

[Narrative guidance. What changed, why, and what it might mean for different
kinds of projects.]
```

The date and "Affects" field do the real work — `/update` matches notes to changes
using those plus the actual git diff. The commit hash is a convenience anchor: include
it when it's easy (e.g., writing the note after committing), omit it when it's not
(e.g., the note is part of the same commit as the change).

---

## Entries

*Entries are added chronologically, newest first.*

### 2026-02-19 — Maintenance learnings captured in foundations, validate, maintain

**Affects:** core/nla-foundations.md, core/skills/validate-architecture.md, core/skills/maintain.md

Three core files now carry learnings from the first cross-NLA feedback session:

- **Foundations** ("How to Read This System"): A note about language encoding assumptions —
  narrow language causes narrow NLA behavior, and broadening language is usually more effective
  than adding rules. All projects load this automatically.

- **Validate architecture review**: New analytical category "Language breadth" — checking
  whether docs assume a specific NLA shape when they should be shape-neutral.

- **Maintain skill**: Two enrichments folded into existing principles and processing
  guidance — broadening over adding (Principle 1) and proportional resolution
  (feedback/friction processing). Principle 2 already had pre-flight/post-validate
  guidance from the earlier validate dispatcher update.

No action needed — these propagate automatically via `../nla-framework/`. If you ejected
any of these files, review the changes and consider whether to incorporate them.

---

### 2026-02-19 — Output spec is now optional

**Affects:** core/skills/startup.md, core/skills/validate-structural.md, core/skills/maintain.md, install/structure-intent.md, install/skills-intent.md

`app/shared/output-spec.md` is no longer assumed to exist in every NLA. The startup
skill loads it only if present (same pattern as config.md). Validate no longer flags
its absence unless a task doc references it. The maintain skill and intent files treat
it as conditional.

This reflects that not every NLA needs a dedicated output spec file. Classification
NLAs, conversational NLAs, and NLAs with simple output can put format guidance directly
in their task docs. NLAs with complex or shared output format concerns still benefit
from the file — it just isn't mandatory.

Existing projects with output-spec.md: no changes needed. Everything works as before.
Projects without one: you'll no longer see it flagged as missing.

---

### 2026-02-19 — Startup extensibility and scaffold reference cleanup

**Commit:** 0d6b1b2
**Affects:** core/skills/startup.md, install/CLAUDE-intent.md, install/skills-intent.md

The startup skill now supports app-specific initialization via `app/startup.md`. After
loading foundational context, the skill checks if this file exists and follows it. This
is where apps define additional startup steps — scanning for active work, checking
environment, presenting status — without ejecting the thin wrapper.

If your project ejected the startup wrapper to add custom startup behavior, you can
now un-eject: restore the thin wrapper and move your custom logic into `app/startup.md`.
The framework handles universal context loading; your file handles domain-specific steps.
This is optional — ejected startups continue to work fine.

The hardcoded `/format-article` task identification table was replaced with generic
guidance that consults `app/overview.md`. Projects using the thin wrapper get this
automatically; ejected startups are unaffected.

---

### 2026-02-19 — Cardinal Rule broadened, NLA Shapes added, TK references removed

**Commit:** 25e9c00
**Affects:** core/nla-foundations.md, install/CLAUDE-intent.md, install/skills-intent.md

The Cardinal Rule changed from "the human must always be able to compare changes
against the original and easily revert" to "the human decides." The old framing was
transformation-specific — it assumed an original to compare against. The new framing
is universal across stateless, persistent, and creative NLAs.

Projects with custom Cardinal Rule language in their CLAUDE.md: check whether your
framing is already aligned with the broader principle. If so, no change needed.

NLA Shapes (stateless, persistent, tool-using) was added to nla-foundations.md. This
is loaded by all projects automatically via `../nla-framework/`. Consider whether your
overview.md reflects which shape your NLA is.

A new Principle 6 (Configuration Is Natural Language) was added to nla-foundations.md.
Also loaded automatically. No project changes needed, but it may inform how projects
think about their config-spec.

TK note references were removed throughout — "flag uncertainty" replaces "use TK notes."
Projects using TK conventions in their own docs can keep them (they're domain choices),
but framework-generated references now use the general language. The domain skill
pattern in skills-intent.md has updated guardrails.

---

*This file is maintained during `/maintain` sessions and read by `/update` when
proposing changes to domain projects. See `reference/design-rationale.md` for the
full design.*
