# Maintenance Session: Plugin Export Design

**Date:** 2026-02-20
**Status:** Complete

## Intent

Design the `/export` skill that converts NLA projects into Claude Code/Cowork plugins.
This is the bridge from development environment (NLA framework) to distribution format
(plugin). The session focuses on design thinking — what to build and why — before
implementation.

## Reframing: Paradigm Evangelism, Not Product Shipping

The user reframed the project's purpose early in the session. Key insight: the NLA
framework is not trying to ship polished products to millions of users. It's demonstrating
a new software paradigm — LLMs as runtime, markdown as code, hybrid development. The
NLAs and plugins are illustrations that the ideas work. The goal is to get other people
thinking about this paradigm, possibly building better frameworks, possibly influencing
how Anthropic/OpenAI/Google develop their tools.

This reframing changed several design decisions:

**"I hope this project dies quickly — but makes a big splash before it goes."**

## Research Phase

Conducted parallel research on Cowork's technical capabilities and the plugin system:

### Key Findings

1. **Plugins work in both Claude Code AND Cowork.** Same format, same structure. The
   feature is "export as plugin" not "export for Cowork." The Cowork angle is about
   reaching non-technical users, but the plugin itself is platform-agnostic.

2. **The plugin system is structurally almost identical to NLA projects.** Skills are
   markdown files with YAML frontmatter. Supporting files live in skill directories.
   The mapping is nearly 1:1 — the main transformation is dependency resolution
   (flattening the two-hop thin wrapper pattern).

3. **`user-invocable: false` is a real frontmatter field.** Skills with this flag are
   auto-loaded as background knowledge. This validates the "foundation skill" approach
   for replacing CLAUDE.md's role in the plugin.

4. **Plugin skills are namespaced** (`/plugin-name:skill-name`). No collision with
   other plugins or project-level skills.

5. **No cross-directory references after installation.** `../` paths fail. Every
   dependency must be bundled inside the plugin directory.

6. **Cowork has no cross-session memory** (yet). Knowledge Bases are forthcoming but
   not shipped. The NLA project's own files (in the user's working folder) serve as
   the persistence layer.

### Existing Design Document

`reference/designs/cowork-plugin-export.md` (2026-02-14) had substantial thinking that
held up well against the research. The plugin system was more mature than that doc
assumed, but the core mapping (flatten two-hop, foundation skill, bundle per skill)
was validated.

## Design Decisions

### 1. Plugin as Distribution Format

**Decided:** Export NLA projects as plugins (works in both Claude Code and Cowork).

**Rationale:** The earlier design thinking imagined Cowork-specific conversions (routing
tables, startup banners). The plugin system makes this moot — one format works everywhere.
The framing shifts from "export for Cowork" to "compile for distribution." NLA project
is source code; plugin is the binary.

**Rejected:** Dual-target `/create-app` (generate Claude Code or Cowork project from
same conversation). Conflates development tools with distribution artifacts.

### 2. Foundation Skill Replaces CLAUDE.md

**Decided:** `skills/foundation/SKILL.md` with `user-invocable: false` carries NLA
identity, behavioral principles, overview, config spec, and available skills table.

**Rationale:** Plugins can't auto-load CLAUDE.md. Skills with `user-invocable: false`
are auto-loaded as background knowledge — functionally equivalent.

**Key detail:** The foundation skill is a *synthesis* of five sources, not a
concatenation. It should read as one coherent identity document. Only behavioral
principles from nla-foundations.md (Key Principles 1-6), not the explainer content.

### 3. Bundle Shared Context Per Skill (Option A)

**Decided:** Each domain skill gets copies of voice-and-values.md, common-patterns.md,
etc. as supporting files.

**Rationale:** Self-containment over deduplication. If a shared context skill fails to
load, every domain skill breaks. With bundling, each skill is independently functional.
Markdown files are small; duplication cost is trivial.

**Rejected:** Shared context skill with `user-invocable: false` (Option B). Cleaner
but introduces load-order dependency.

### 4. Dev Tools Always Ship (Revised Decision)

**Originally decided:** Exclude all dev tools (maintain, friction-log, validate, etc.).

**Revised after discussion:** Dev tools always ship. This was the most significant
design discussion of the session. Arguments:

**The paradigm evangelism argument:** The goal is getting people to understand NLAs.
Showing the dev tools — the maintenance cycle, the feedback loop, the validation
system — is part of the paradigm demonstration. Like View Source in browsers: it
turns users into developers.

**The browser dev tools argument:** Chrome ships developer tools to everyone. They
don't clutter the experience for non-technical users (they're hidden until you open
them). Same with `disable-model-invocation: true` — the skills are inert files until
someone intentionally invokes them. Zero context cost, huge educational and debugging
value.

**The early-stage argument:** NLAs are a new paradigm. Things won't always work right.
The ability to debug, validate, and trace in the production environment (the plugin)
is essential. Removing dev tools is like only putting black boxes on test aircraft.

**The trivial cost argument:** With `disable-model-invocation: true`, dev tool skills
aren't loaded into context. They're just files in the plugin directory. No runtime
cost at all.

### 5. Remove `disable-model-invocation` from Domain Skills

**Decided:** Domain skills in plugins lose the flag. Utility and dev skills keep it.
Foundation skill uses `user-invocable: false`.

**Rationale:** Non-technical users say "help me format this" not
`/pluginname:format-article`. Claude needs to auto-match intent to skills. Removing
the flag enables this.

### 6. The LLM as Self-Aware Feedback Generator (Design Insight)

This emerged from discussion about how feedback should work in plugins. Key insight:

In traditional software, the feedback loop is broken at the observation-to-understanding
gap. Users can describe what happened (poorly). Developers must reproduce and trace to
understand why. In an NLA, the LLM was right there — it read the instructions, made the
judgment call, and can explain the full chain:

"I suggested 4/4 time because common-patterns.md step 3 says [exact quote]. The user
appears experienced. Consider rewording to: [proposed documentation change]."

This is not a bug report. It's a diagnostic with a proposed documentation patch. The
LLM functions as its own debugger, QA engineer, and junior developer.

**This is genuinely novel to the paradigm.** Traditional software can't do this because
code doesn't understand itself. NLA "code" is natural language that the LLM understands.
The same intelligence that executed the instructions can reflect on them and propose
improvements.

**Risks flagged:**
- **Confabulation:** The LLM might construct plausible but inaccurate explanations.
  Mitigation: include exact quotes from docs, not paraphrases. Checkable, not just
  plausible.
- **Context window decay:** By the time feedback is triggered, early decisions may be
  compressed out of context. Mitigation: capture close to the moment ("log it before
  you forget"), not session-end retrospectives.
- **Proposed fixes may be incomplete:** The LLM has limited context about all cases a
  doc serves. Proposed changes are starting points, not auto-patches. The Cardinal Rule
  applies: the human decides.

These are characteristics to acknowledge and design around, not blockers.

### 7. Feedback in Plugins: Simpler Than Expected

**Evolution of thinking:** Started with "move write-letter into the framework as a base
class with extension points." Ended at "the export just bundles what's in the NLA."

**Key insight:** External feedback (write-letter) is not a core NLA feature. Internal
feedback (friction-log) is. The framework handles observation capture. Delivery of
observations to someone else is an extension concern (penny post or otherwise).

**What the export does:** Walk the NLA project's `.claude/skills/` directory. Whatever
is there, ships. If the NLA has penny post installed, write-letter ships. If not, it
doesn't. The export has no opinion about feedback delivery.

**Two learning loops in the plugin:**
1. **Local loop:** User tweaks their plugin (maintain), observes what works (friction-log),
   tweaks again. The NLA learning loop running locally.
2. **Upstream loop:** User sends feedback to the NLA developer (write-letter, if installed).
   Only exists if a delivery extension is present.

**The LLM self-aware diagnostic** is a quality improvement to existing skills, not a new
skill. Guidance for friction-log and write-letter about leveraging LLM self-awareness
(include instruction chain, use exact quotes, propose doc changes) belongs in those
skills' own docs.

**Rejected:** Moving write-letter into the framework as a base class. External feedback
is situational (private NLAs don't need it, team NLAs might use Slack, public plugins
want GitHub Issues). Keeping it in penny post respects this variation.

### 8. Export Is NLA-Scoped, Not Framework-Scoped

The export reads the NLA project's `.claude/skills/` directory. That's the complete
manifest. The framework's own skills (including any extensions installed for framework
maintenance) are invisible to the export.

When a thin wrapper references a framework file (`../nla-framework/core/skills/X.md`),
the export resolves and inlines that file. But the framework doesn't independently
contribute skills to the plugin. It's infrastructure — support for the NLA, not part of
the NLA in the plugin context.

**This simplifies the export algorithm:** Walk `.claude/skills/`, classify each skill,
resolve dependencies, bundle everything. No need to inspect installed-packages.md or
check for specific extensions.

### 9. The Wrapper Spectrum: Ejection Isn't Forking

**Original framing (wrong):** "Eject = replace wrapper with custom skill. You've forked;
no more framework updates."

**Corrected framing:** In an NLA, `/update` communicates *intent*, not diffs. When the
framework changes a skill's intent, the LLM can propose how that intent applies to a
customized implementation — not just a thin wrapper.

"Your startup already loads voice context and checks for SuperCollider. The framework
now recommends also loading extension context. Here's where that would fit in your
custom implementation, and here's why."

This is the judgment layer doing something deterministic systems cannot: understanding
both sides of a customization boundary and proposing a merge that respects both.

**Four states of a wrapper:**

1. **Thin wrapper** — full delegation to framework. Updates flow automatically.
2. **Annotated wrapper** — delegates to framework but adds project-specific notes.
   Updates flow for the delegated part; annotations persist.
3. **Ejected (customized) skill** — full custom implementation. Updates arrive as
   intent proposals, merged by the LLM with human approval.
4. **Redirected wrapper** — points at a different implementation (e.g., penny post
   replaces write-letter). Updates from the alternative source apply.

**Risks of intent-based updates to ejected skills:**
- LLM might misunderstand the customization, weakening a subtle guardrail
- LLM might misinterpret framework intent, applying it too broadly
- Compounding: multiple intent-merges over time create a skill nobody fully understands
- Cardinal Rule applies: human reviews every merge proposal

**This is powerful and novel.** Traditional package managers can't reconcile "your custom
version" with "the framework's new intent" because they operate on text. The LLM operates
on meaning. The eject decision goes from "permanent fork" to "customization that still
receives intent-level updates."

Worth documenting as a recognized pattern in design-rationale.md.

### 10. Which Dev Tools Ship

**Final classification:**

| Skill | Ships? | Why |
|-------|--------|-----|
| maintain | Yes | Local plugin tweaking |
| friction-log | Yes | Core learning loop |
| validate | Yes | Structural checks + debugging |
| preferences | Yes | User configuration |
| startup | No (absorbed) | Foundation skill replaces it |
| install | No | Framework package management, meaningless in plugin |
| update | No | Framework update mechanism, meaningless in plugin |
| write-letter | If installed | Extension concern (penny post) |
| check-feedback | If installed | Extension concern (penny post) |

All dev tools ship with `disable-model-invocation: true`. Domain skills lose the flag.
Foundation skill uses `user-invocable: false`.

## Design Insights (Framework-Level)

These emerged from the export discussion but apply beyond it:

### The Override Pattern

Any framework skill can be overridden by pointing the thin wrapper at a different
implementation. This is the NLA equivalent of dependency injection — same interface,
different implementation, decided at install time. No new machinery needed; the thin
wrapper pattern already supports it.

### Intent-Based Updates Across Customization Boundaries

`/update` communicates intent, not diffs. This means ejected (customized) skills can
still receive framework improvements — the LLM proposes how new intent applies to the
custom implementation. This changes ejection from "permanent fork" to "customization
with intent-level update channel."

### NLA as Source, Plugin as Artifact

The compile analogy: NLA project is source code (rich dev tooling, learning loops,
maintenance cycle). Plugin is the compiled artifact (self-contained, installable,
distributable). Develop with the framework, ship as a plugin. To improve the plugin,
improve the NLA and re-export.

### LLM Self-Aware Diagnostics

NLA feedback can include the instruction chain that led to behavior, with exact quotes
from docs and proposed documentation changes. This is possible because the "code" is
natural language the LLM understands. A capability unique to the paradigm.

## Process Observations

### Design-by-Conversation

This session's most important decisions all came from the user pushing back on initial
proposals in open-ended conversation. Dev tools always ship, ejection ≠ forking, export
is NLA-scoped, write-letter stays in penny post — each was a correction of the AI's
initial framing, made through unstructured back-and-forth discussion.

This is evidence about how NLA design works: the collaborative conversation IS the design
process, and it produces better results than structured decision-making (multiple-choice
options, plan-mode exit prompts). The AI proposes based on patterns; the human corrects
based on purpose. Neither alone reaches the right answer.

Related to the "thinking it through" friction log entry — the tooling gap isn't just about
having a mode, it's about protecting space for this kind of conversation.

### Broadening Over Adding (Pattern Recurrence)

The "broadening over adding" pattern from the Duet feedback session (2026-02-19) recurred
here. The dev tools decision was "remove a restriction" (don't exclude them). The domain
skill frontmatter decision was "remove a restriction" (drop the flag). Both improved the
design by loosening constraints, not adding features. This is the third time the pattern
has appeared — it's becoming a reliable design heuristic for NLAs.

### Context Compaction as a Design Session Risk

The architecture review findings were lost when conversation context was compacted. Long
design sessions that explore deeply push against context limits. This is a practical
constraint on the "thinking it through" mode: design conversations need context space,
and current tooling doesn't protect detailed findings from being compressed away.

## Friction Log Entries Added

- "Need a 'thinking it through' mode for design exploration" (process, major, pending)
- "Need a way to export NLAs for use in Claude Cowork" (core, major, resolved)

## Changes Made

- **Created `core/skills/export.md`** — The export skill. Natural language instructions
  for converting an NLA project into a self-contained plugin. Covers inventory,
  foundation skill generation, dependency resolution, path rewriting, verification.
- **Created `.claude/skills/export/SKILL.md`** — Framework's own wrapper.
- **Updated `install/skills-intent.md`** — Added /export thin wrapper reference.
- **Updated `CLAUDE.md`** — Added /export to skills table.
- **Updated `reference/design-rationale.md`** — Replaced stale "Cowork as a Target
  Environment" section with "Plugin Export: NLA as Source, Plugin as Artifact" and added
  "The Wrapper Spectrum" section documenting four wrapper states and intent-based updates.
- **Updated `README.md`** — Added /export to directory tree and new "Distributing as a
  Plugin" section.
- **Updated `reference/friction-log.md`** — Added "thinking it through" entry, marked
  export entry as resolved.
- **Ran `/validate`** — Structural check: all clear. Architecture review: 0 fix-level, 7 improve-level, 4 note-level findings, all terminological consistency and cross-reference clarity.
- **Fixed "four sources" → "five sources"** in `core/skills/export.md` (listed five sources but said four).
- **Fixed README "Ejecting a Skill"** — updated to align with the Wrapper Spectrum insight (ejection ≠ forking, intent-based updates still flow).
- **Added annotated wrapper handling** to `core/skills/export.md` edge cases section.
- **Re-ran architecture review** after context compaction (original findings lost). Found
  2 fix, 3 improve, 4 note. The fix items were documentation drift missed during
  implementation.
- **Fixed `/create-app` Category 1 table** — added `/export` wrapper to generation list.
- **Fixed `core/skills/README.md`** — added export.md to "What's Here" table, updated
  Eject Pattern section to align with Wrapper Spectrum (ejection ≠ forking).
- **Fixed export classification table** — added `/export` itself as Framework-only.
- **Fixed design-rationale.md** — updated stale "Cowork target" reference to "plugin
  export model" in Config open questions.
- **Added guard note to framework export wrapper** — notes that `/export` is designed
  for domain projects, not the framework directory.
- **Fixed README Key Concepts** — "The Structure Gradient" → "The Hybrid Model" to match
  actual terminology in nla-foundations.md.
- **Added update note** for `/export` in `install/update-notes.md` — context for domain
  projects running `/update`.

## Blast Radius

- **All domain projects:** New `/export` skill available via thin wrapper (additive —
  no existing behavior changes)
- **Project generation:** `install/skills-intent.md` updated (new projects get /export)
- **Framework documentation:** Design rationale updated with two new sections, README
  updated with distribution section

## State at Close

The `/export` skill is implemented and documented. Design rationale captures the full
reasoning including dev-tools-always-ship, the wrapper spectrum, and intent-based updates
across customization boundaries.

**Validated twice.** First architecture review (pre-compaction): 0 fix, 7 improve, 4 note.
Second review (post-compaction, after initial fixes): 2 fix, 3 improve, 4 note. The two
fix items were documentation drift — `/create-app` and `core/skills/README.md` missing
the new export entry. All findings resolved except pre-existing items (Structure Gradient
terminology predates this session) and informational notes.

**Not yet tested:** The skill needs real-world testing with Duet or Copydesk. The
foundation skill generation (step 3 of the processing flow) is the most complex part
and most likely to need refinement after testing.

**Pending from this session:**
- "Thinking it through" mode friction log entry remains pending — needs its own design
  session
- The LLM self-aware diagnostic quality improvement for friction-log and write-letter
  is identified but not implemented — it's guidance for those skills' docs, not a
  structural change
- Testing the export with a real project is the natural next step
