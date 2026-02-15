# Framework Feedback: Duet Maintenance Session

**Source:** Duet (collaborative music composition NLA)
**Date:** 2026-02-14
**Context:** Resolved four friction log entries in one session — music directory structure, lifecycle skills, setup/environment, and auto-play. This letter captures patterns that emerged from building on the framework that seem general enough to push upstream.

---

## 1. Artifact Persistence Is a Missing Pattern

**The gap:** The framework scaffold assumes stateless work — transform input, produce output, done. Duet needed multi-session persistence: a work directory, piece folders, context files, iteration history. We built all of this from scratch.

**The general pattern:** Any NLA where work spans sessions needs:
- A directory structure for work-in-progress
- A context file per work item (the "session bridge")
- Conventions for where things go and how they're named

**Recommendation:** The framework should document this pattern and `/create-app` should ask "does your NLA produce artifacts that persist across sessions?" If yes, scaffold the directory structure and context template.

**Suggested framework addition to `nla-foundations.md`:**

```markdown
### Stateless vs. Persistent NLAs

Some NLAs are stateless — they transform input and produce output in a single session.
Others produce artifacts that evolve across sessions: compositions, articles in progress,
codebases, designs. Persistent NLAs need:

- **A work directory** — Where artifacts live, organized by lifecycle state
  (in-progress, shelved, done)
- **Context files** — A curated record per work item capturing intent, decisions,
  rejected alternatives, and open questions. This is the session bridge — it lets
  a cold-start session pick up the collaboration without re-reading conversation history.
- **Lifecycle operations** — Ways to snapshot, shelve, finish, and resume work items

The context file is not a transcript. It's a distillation of *why* — decisions and their
reasoning, things tried and rejected, questions still open. Write it so a future session
(human or AI) can understand the state of the work and continue it.
```

---

## 2. The Session Bridge (context.md) Is General

**What we built:** A `context.md` file per composition capturing concept, decisions (with reasoning), rejected ideas (with reasoning), references, listening notes, unresolved questions, and iteration history. A template provides scaffolding; the AI uses judgment about which sections are relevant.

**Why it's general:** Any multi-session NLA work needs this. An article NLA needs editorial context between sessions. A code-generation NLA needs architectural decision context. The specific sections change; the pattern doesn't.

**Recommendation:** Add a context file pattern to the framework — guidance on designing context files, what makes a good one, and a template-of-templates. Key principles we discovered:
- The template is scaffolding for the AI, not a form for the human
- Human overrides to the template are signal worth learning from
- Distill, don't transcribe — the context file is curated, not comprehensive
- The "Rejected" section is as valuable as "Decisions" — it prevents re-treading

---

## 3. Lifecycle Is a Unified Pattern

**What we built:** `/snapshot`, `/shelve`, `/finish`, `/resume`. These started as four separate concepts but the user recognized they're all the same core operation: capture state + note → put somewhere.

| Skill | Destination | Work item stays active? |
|-------|------------|----------------------|
| /snapshot | iterations/ | Yes |
| /shelve | shelved/ | No |
| /finish | done/ | No |
| /resume | (reverse of shelve) | Yes |

**Why it's general:** Any NLA with multi-session work needs lifecycle management. The specific operations are always variants of: save state, move state, restore state.

**Recommendation:** The framework could provide a lifecycle skill template that apps customize. The template would include the shared structure (prompt for a note, save files, update context, move to destination) with app-specific hooks.

**Key insight:** Every transition prompts for a note. The real value is capturing what the user is thinking at the moment they're most likely to have insight and least likely to write it down voluntarily.

---

## 4. The Startup Skill Needs Extensibility

**What happened:** The framework startup is a flat sequence: load docs 1-6, confirm ready. Duet needed to add piece awareness (scan active work) and environment checking (read environment.md, compare against requirements). We had to completely replace the framework startup rather than extend it.

**Recommendation:** A two-phase startup pattern:
- **Phase 1 (framework):** Load foundational context — nla-foundations, overview, shared docs, config. This is universal.
- **Phase 2 (app-specific):** Check for active work, verify environment, present status. This varies per NLA.

The framework startup should document the extension point: "After loading foundational context, the app may add startup steps. Define these in the app's startup skill."

**Suggested framework startup addition:**

```markdown
## App-Specific Startup

After loading foundational context, check if the app's startup skill defines
additional steps. Common app-specific startup tasks:

- Scanning for active work items (if the NLA is persistent)
- Reading environment state (if the NLA uses external tools)
- Presenting a status summary to the user

These steps live in the app's `.claude/skills/startup/SKILL.md`, not in the
framework. The app startup skill should load framework foundations first,
then add its own steps.
```

---

## 5. Environment Management for External Tools

**What we built:** An `environment.md` file at the work directory root that caches platform detection, installed tools, and extensions. The `/setup` skill detects and writes it; `/startup` reads it.

**Why it's general:** Any NLA that uses external tools (compilers, interpreters, APIs, databases) needs to know what's available. The NLA advantage: cross-platform differences are handled through AI judgment, not coded detection.

**Recommendation:** Add environment management guidance to the framework. Key patterns:
- Detect once, cache in environment.md, read on subsequent startups
- The AI handles platform differences naturally — no coded detection needed
- Always confirm before installing anything
- The `/setup` skill is the writer; everything else is a reader

---

## 6. Tool-Specific Output Specs

**What we did:** Renamed `output-spec.md` to `output-spec-sc.md`. When Duet supports a second engine, it will get its own spec rather than diluting the first.

**Why it matters:** The framework scaffold has one generic `output-spec.md`. But when an NLA might support multiple output tools/formats, separate specs beat premature abstraction. Each tool gets tailored guidance; overlap is extracted only when it demonstrably exists.

**Recommendation:** `/create-app` should ask if the NLA might support multiple output tools. If yes, name the output spec after the tool from the start. The framework docs should note this as a pattern.

---

## 7. The AI Can Execute What It Generates

**What we built:** Auto-play — the AI generates SuperCollider code AND runs it via `sclang`, handling errors conversationally and managing background processes.

**Why it's general:** Any NLA that generates runnable artifacts (code, scripts, configs) can also execute them. This is a major NLA advantage: a traditional app needs a coded integration layer; the NLA just uses its tool access. The framework doesn't discuss this capability at all.

**Recommendation:** Add a section to `nla-foundations.md` on tool execution. Key patterns:
- Config toggle (off by default — the user opts into automatic execution)
- Execution supplements, never replaces, the conversational output
- Errors become conversation, not stack traces
- Background execution so the conversation isn't blocked
- The docs describe desired behavior; the AI handles shell-level mechanics

---

## 8. `/create-app` Could Guide Deeper Decisions

**Current state:** `/create-app` scaffolds structure through a conversation about domain, voice, tasks, and output format.

**What it could also ask:**
- "Does your NLA produce artifacts that persist across sessions?" → scaffold work directory + context template
- "Does your NLA use external tools?" → scaffold environment.md + /setup skill
- "Will your NLA support multiple output tools?" → name output spec after tool
- "Does work span multiple sessions?" → scaffold lifecycle skills

The more `/create-app` asks up front, the less the developer builds from scratch. Each of these is a decision that Duet had to make organically and then retrofit.

---

## 9. The Maintenance Exit Interview Pattern

**This document is itself a proposed pattern.** After a substantive maintenance session, the NLA should have a structured way to send feedback upstream to the framework.

**The pattern:**
1. After completing maintenance work, the NLA asks itself: "What did I build that the framework should have provided? What was harder than it should have been? What patterns emerged that are general?"
2. The NLA writes a feedback letter (like this one) — narrative context with specific recommendations, including suggested markdown when appropriate.
3. The letter is placed in the framework repo at `reference/feedback/[date]-[source]-[topic].md`.
4. The framework's `/maintain` process reviews letters like pull requests — accept, reject, defer, or adapt. Accepted learnings become framework changes; deferred ones stay as reference.

**Why this matters:** The framework improves through the experience of the NLAs built on it. Without a structured feedback channel, learnings stay trapped in individual projects. The friction log captures problems; the exit interview captures patterns and architectural insights.

**Suggested additions to framework:**
- `reference/feedback/` directory for NLA feedback letters
- Guidance in `/maintain` skill on processing feedback letters
- Guidance in NLA `/maintain` skill on writing exit interviews after substantive sessions

---

## 10. Natural Language Config Is a Fundamental NLA Capability

**The insight:** The framework's config-spec scaffold and guidance leans toward structured settings — enums, levels, on/off toggles. These are useful as convenient defaults, but they understate what NLA config can actually do. Because config is prose interpreted by an LLM, users aren't limited to predefined choices. They can write:

- "Adventurousness: exploratory, but stay grounded on rhythm — I want weird harmony over a solid groove"
- "Instruction depth: detailed for harmony, light for rhythm, off for mixing"
- "Voice: creative partner, but lean into teaching when I'm clearly lost"

This is like extensions or plugins — except the NLA doesn't need a plugin architecture. The LLM IS the extension system. Natural language modifiers on any setting are a baked-in feature of NLAs.

**What the framework should do:**
- Discuss this explicitly in `nla-foundations.md` or config guidance. It's a core NLA capability that distinguishes NLA config from traditional config.
- The config-spec scaffold should show the pattern: enum options as defaults, with explicit guidance that users can modify with natural language ("Choose one of these, or describe what you want in your own words").
- `/preferences` skill should encourage this: "You can pick one of these options, or describe something more specific."

**Suggested framework addition to `nla-foundations.md`:**

```markdown
### Configuration in NLAs

Traditional software config is structured: enums, booleans, key-value pairs. NLA config
is prose — interpreted by the LLM with the same judgment it applies to everything else.

This means NLA config can express nuance that traditional config cannot:
- "Option A, but with this modification..."
- "Option C, and also consider..."
- "Something entirely different: [natural language description]"

Enum options are convenient defaults — they give users a starting point and make common
choices easy. But natural language is the real interface. Users can modify any setting
with prose, and the LLM synthesizes the base option with the modification.

This is equivalent to a plugin or extension system — except no architecture is needed
to support it. The LLM's ability to interpret nuanced instructions IS the extension
mechanism. App developers should embrace this: provide enum defaults for discoverability,
but make clear that users can customize beyond the options listed.
```

**Where this came from:** Duet is adding selectable voices (creative partner, music educator, etc.). The user pointed out that voice config doesn't have to be an enum choice between files — it can be "creative partner, but shift into educator mode when I'm struggling." This applies to every config setting, not just voice.

---

## 11. Assumptions to Broaden

The items above are about what's missing. This section is about what's there but reveals the framework's origin as a **stateless transformation NLA** (the article formatter). Nothing here needs to be removed — it needs to be broadened so the framework works equally well for creative, generative, and persistent NLAs.

### The Cardinal Rule Is Transformation-Specific

The Cardinal Rule states: "The human must always be able to compare changes against the original and easily revert." This is perfect for transformation — you have an original, you're modifying it. It's less applicable to creation — there is no original; you're making something new.

The underlying principle (human oversight and control) is universal. The specific framing is not. A broader version might be: "The human must always understand what changed and why, and be able to undo it." This covers both transformation (compare against original) and creation (understand what decisions were made, revert to a previous state via snapshots).

### The Startup Skill Leaks Scaffold References

The framework startup's task-identification table references `/format-article` — a scaffold-specific skill. Any NLA that doesn't eject the startup inherits a reference to a task that doesn't exist in their project. This should either be removed from the framework startup (let apps define their own task identification) or replaced with a placeholder pattern that apps fill in.

### The Scaffold Shapes Expectations

The scaffold is an article formatter. Developers building new NLAs with `/create-app` see transformation patterns as the "default" — stateless input/output, text-oriented shared context, a single task that processes content. This subtly shapes how they think about their NLA.

Not wrong for what it is, but the framework would benefit from acknowledging the range. Options:
- A second example NLA (a simpler creative/generative one) that shows a different shape
- Explicit guidance in `/create-app` or the README: "The scaffold is a transformation NLA. Your NLA might be creative, generative, or persistent — the same patterns apply but the shape differs."
- Notes in the scaffold files themselves: "This is one way to structure shared context. A creative NLA might organize differently."

### The Validate Skill Assumes Deterministic Output

`/validate` has three modes: structural, scenario walkthrough, and debug. Scenario tracing is designed for "given this input, what output should the system produce?" — which works for transformation where there's a roughly correct answer.

For creative NLAs, output is non-deterministic by design. "Given this mood, what music?" doesn't have a correct answer. Validation needs to focus on **process** (did the AI read the right docs? did it follow its voice? did it explain its reasoning?) rather than **output** (is this the right result?).

The validate skill could add guidance for non-deterministic NLAs:

```markdown
### Validating Creative/Generative NLAs

When output is non-deterministic by design, scenario walkthroughs focus on process:
- Did the AI read and follow the relevant task doc?
- Did it apply shared context (voice, patterns)?
- Did it explain its reasoning and flag uncertainty?
- Did it invite human feedback rather than presenting output as final?

The question isn't "did it produce the right output?" but "did it follow the right process
with appropriate judgment?"
```

---

## Related

- **Cowork plugin export:** The NLA framework structure maps nearly 1:1 to Cowork plugin structure. A converter (`/export-plugin`) could give any NLA a distribution channel. Design doc at `reference/designs/cowork-plugin-export.md`.

---

*This letter is from Duet's first major maintenance session (2026-02-14), which resolved all four founding friction log entries in one pass. The patterns above emerged from building a persistent, multi-session, tool-using NLA on a framework designed around stateless transformation. The framework is solid — these observations are about broadening its lens, not fixing what's broken.*
