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

**Commit:** [hash — for sessions with multiple commits, use the final commit]
**Affects:** [which intent files or core files changed]

[Narrative guidance. What changed, why, and what it might mean for different
kinds of projects.]
```

---

## Entries

*Entries are added chronologically, newest first.*

### 2026-02-19 — Startup extensibility and scaffold reference cleanup

**Commit:** 356af0b
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
