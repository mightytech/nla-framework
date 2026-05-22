# NLA Foundations

This document explains what natural language applications are and the principles that make them work. It's the conceptual foundation for everything else in this system. Read it first.

---

## What is an NLA?

### The Concept

A Natural Language Application (NLA) is software where the runtime is an LLM and the "code" is written in natural language.

**Traditional application:**
```
Code (Python, JavaScript) → Executed by interpreter/compiler → Output
```

**Natural Language Application:**
```
Documentation (Markdown) → Executed by LLM → Output
```

This isn't metaphor. The documentation literally IS the application. When you want to change behavior, you edit the docs. When you want to add features, you write more docs. The LLM reads the docs and does what they say.

### Why NLAs?

Some problems are hard to solve with traditional code:

| Problem | Traditional Code | NLA |
|---------|------------------|-----|
| "Is this paragraph a quote?" | Regex patterns, heuristics, edge cases | LLM reads it and knows |
| "Should there be a header here?" | Rules about word count, topic detection | LLM feels the narrative shift |
| "What's good link text for this URL?" | Domain mapping tables, fallbacks | LLM understands context |

These are judgment calls. Traditional code handles them through enumeration — listing every case. NLAs handle them through understanding — grasping intent and applying it.

**NLAs excel when:**
- The task requires judgment and synthesis
- Edge cases are numerous and hard to enumerate
- "I know it when I see it" describes the requirement
- The rules are easier to explain than to code

**Traditional code excels when:**
- Determinism is required (calculations, transactions)
- Speed is critical (millions of operations per second)
- The logic is well-defined and finite
- Auditability requires exact reproducibility

### The Hybrid Model

NLAs don't replace traditional code — they complement it. A well-designed system uses both:

**LLM handles:**
- Formatting decisions (is this a blockquote?)
- Pattern recognition (is this a Resources section?)
- Tone and voice (does this sound right?)
- Judgment calls (should I add a header here?)

**Traditional code handles:**
- API calls (reading from and writing to services)
- File I/O (reading CSVs, writing JSON)
- Triggers (detecting events, webhooks, scheduling)
- Validation (is the output valid structured data?)

The traditional code is plumbing. The NLA is the intelligence.

### NLA Shapes

NLAs aren't all the same shape:

**Stateless** — Input in, output out, done. An article formatter, a ticket classifier,
a code reviewer. No state persists between sessions.

**Persistent** — Work evolves across sessions. A composition tool, a writing assistant,
a design system. Persistent NLAs need some form of state management: where work lives,
how sessions pick up where they left off, how work moves through stages. The specific
mechanisms vary — the need doesn't.

The key challenge is session continuity. The LLM starts cold each session. Persistent
NLAs need curated state files that capture decisions, reasoning, and open questions —
not transcripts, but distillations of *why*. The framework's own session logs
(`reference/sessions/`) follow this pattern for maintenance work.

**Tool-using** — Some NLAs drive external tools: compilers, APIs, interpreters. The LLM
handles judgment and intent; external tools handle execution. When the NLA generates
runnable artifacts, the LLM can execute them directly — errors become conversation, not
stack traces.

Most NLAs are a mix. The shape informs which patterns apply.

---

## How to Read This System

When executing an NLA task:

1. **Read this document first** — understand what NLAs are and how they work
2. **Read the overview** (`overview.md`) — understand what this specific NLA does
3. **Read shared context** — voice, patterns, and output specs that tasks share
4. **Read the specific task document** — follow it step by step
5. **Flag uncertainty** — when you're unsure, say so

The task document IS your instructions. Execute it, using judgment informed by shared context.

**A note on language.** The prose in this system encodes assumptions — about what kind of NLA this is, what tasks it handles, how users work with it. When behavior feels too narrow, the cause is often narrow language. Fixing it usually means broadening existing language rather than adding new rules. The LLM fills the space when constraints are loosened.

---

## Key Principles

### 1. Imperfection Is Assumed

NLAs are never finished. The documentation will have gaps, the voice will drift, the edge cases will surprise. This isn't a failure state — it's the expected state, at creation and throughout the lifetime of the application.

This assumption shapes everything else. The improvement loop exists because the system will always need improving. The human decides because the system knows it can't fully trust its own instructions. When something feels wrong during execution — a rule that produces bad output, a gap where guidance should exist — flag it. The friction log is the primary development tool for a system that gets better through use.

This assumption applies to the human too. The NLA framework is designed for human
flourishing — not just productivity. The person building and using the system should
finish each session understanding more, seeing more clearly, and making better judgments
than when they started. The architecture serves this: the Cardinal Rule keeps the human
engaged, not just accountable. The diagnostic step builds understanding, not just
correctness. The improvement loop develops the person alongside the documentation. A
system that routes around the human for efficiency may produce faster output, but it
produces a less capable human. That's not a tradeoff this framework makes.

### 2. NLA Documents Are Source Code

NLA documents are source code, not documentation. An ambiguous instruction is a bug.
A missing section is a missing feature. An inconsistent term is a naming collision.
When you edit these documents, you're editing the application itself — not
describing it.

When the output is wrong, the fix is usually in the docs, not in code. Ask: "What would
I need to write down for someone to do this correctly?" Write that down. The LLM will
follow it.

When something goes wrong, the AI's account of its own behavior is useful input — but
it's hypothesis, not evidence. The account points at where to look; the artifacts
(documents and output) tell you what's actually there. LLMs construct plausible
narratives that may not match what the documents say or the output shows — not bad
faith, just the shape of how they report on themselves. Treat the narrative as a
starting point: it generates hypotheses worth testing, but the artifacts produce ground
truth. Discarding the account loses real signal; accepting it uncritically substitutes
story for evidence. Check before acting.

### 3. Principles and Procedures

Prose "code" has two tools. **Principles** explain *why* — they shape judgment across
many situations. **Procedures** specify *when* — they produce specific behaviors
reliably. Know which you're reaching for. If something needs to happen every time at a
specific moment, a principle alone won't reliably produce it; add a procedural step. If
something needs to shape how the AI thinks across many contexts, a procedure can't
cover every case; write a principle. The best instructions often use both — the
principle ensures the AI does it well, the procedure ensures it does it at all.

### 4. Intent Over Rules

Write intent with rationale, not rules. The LLM that understands *why* reasons about
edge cases, novel situations, and ambiguity. The LLM that follows rules can only
pattern-match to the cases the rules anticipated.

**Less effective:** "Comments containing profanity directed at other commenters should
be hidden. What-about-ism should always be hidden. Spam: always hide."

**More effective:** "This is a community space where people doing hard work come to
feel less alone. When the comment section is working, it feels like a living room full
of people who are exhausted but not defeated. Protect that feeling."

The rules-based version breaks on metaphorical hostility, coded language, sincere
disagreement that sounds like an attack, and dozens of other edge cases. The
intent-based version handles them because the AI evaluates against identity — "does
this belong in the space we described?" — rather than falling through gaps in a rule
list.

**For judgment tasks** — classification, moderation, curation, gatekeeping — describe
the space rather than the boundaries. Write about who the space is for, what it feels
like when it's working, and what values define it. The AI derives the boundaries from
the description. Anchor intent with concrete principles that give testable criteria:
"challenge what people do, not who they are" is specific enough to evaluate against
while preserving the flexibility of judgment.

**Rules have their place.** Use rules for pure preferences where consistency is the
only goal — formatting conventions, naming patterns, structural requirements. "Use ISO
8601 dates" is a rule. "Use blockquotes to emphasize powerful quotes — the reader
should feel the weight of these words" is intent with rationale. Know which you're
reaching for.

### 5. Values Are Visible

Every NLA embeds value choices — what to prioritize, what to protect, what tradeoffs
to make. All priorities are value choices, varying in stakes but not in category.
"Keep it concise" and "never misrepresent sources" are both values; the difference
is consequence, not kind. Some carry legal weight (HIPAA compliance, accessibility
requirements); some are stylistic. The mechanism is the same.

Traditional code embeds the same choices invisibly — in scoring functions, filter
criteria, if/else branches. An NLA states them in prose: readable, debatable,
modifiable by anyone who can read. This transparency is a capability and a
responsibility.

There is no neutral default. An NLA with no explicit values still has values — they're
the model's training defaults, unexamined. Making values explicit is what distinguishes
an NLA that *has* values from one that merely inherits them.

### 6. The Cardinal Rule

**The human decides.** Three reasons, in order of weight:

**Consequences.** Humans bear them. Authority follows accountability. This is
non-negotiable regardless of how good the AI gets. The NLA proposes, explains, and
challenges — but the human has final say. In all cases: flag uncertainty. Never
silently make consequential choices.

What this means in practice depends on the NLA's shape:
- Transformation: offer comparison against the original; make changes easy to revert
- Creation: explain decisions and reasoning; make work revertible through snapshots
- Classification/analysis: show confidence and reasoning; make it easy to override

**Perspective.** The human brings context, experience, and frames the AI doesn't
have — including their gaps and limitations. A non-standard background isn't a
limitation to work around; it's a lens that sees things the AI's training can't. The
AI should draw out the human's perspective, not normalize it into familiar patterns.
Work is substantively better — not just more accountable — when the human is engaged.

**Capability.** Staying engaged builds the human's judgment. Checkpoints on easy
decisions build the understanding needed for hard ones. The AI that routes around the
human for efficiency produces faster output and a less capable human. The goal isn't
just good output — it's a human who's better at their work than when they started.

### 7. Hybrid Architecture

Let each system do what it does best:
- LLM: judgment, synthesis, understanding context
- Code: determinism, speed, API calls, validation

Don't use the LLM for things code does better. Don't use code for things that need judgment.

### 8. Configuration Is Natural Language

Traditional config is structured: enums, booleans, key-value pairs. NLA config is
prose — interpreted by the LLM with the same judgment it applies to everything else.

This means config can express nuance that traditional config cannot:
- "Option A, but with this modification..."
- "Detailed explanations for voice decisions, brief for formatting"
- "Creative partner, but shift into educator mode when I'm struggling"

Enum options are convenient defaults — they make common choices easy. But natural
language is the real interface. Users can modify any setting with prose, and the LLM
synthesizes intent from the combination. No plugin architecture needed — the LLM's
ability to interpret nuanced instructions IS the extension mechanism.

---

## Working Rhythms

These are the common patterns of work in an NLA. They aren't mandatory steps — they're
rhythms that emerge naturally from the system's design. Understanding them helps the AI
assist proactively and helps humans know what to expect.

### The Improvement Loop

Work → notice friction → log it → diagnose → maintain → iterate. The friction log
captures observations while context is fresh; diagnosis asks *why* before routing the
fix; `/maintain` turns them into documentation changes. The diagnostic step matters
because the obvious fix often isn't the right fix — what looks like a bug in the output
may trace to a gap in the documentation, an ambiguity in the spec, or a conflict between
two docs. Diagnose from the artifacts; the AI's account is hypothesis worth
investigating, not verdict (see principle #2). This is the primary development cycle
for NLAs — the system improves by improving its own documentation. Insights evaporate
if not captured; systematic logging turns casual observations into durable improvements.

### The Design Flow

Think → plan → implement → debrief. Design judgment happens before implementation
planning, not during it. `/think` explores what to build and why; planning mode handles
how; `/debrief` captures process learning while context is fresh. Skipping the thinking
phase risks building the right thing wrong — or the wrong thing right. When the session
produced work for a later session, see The Session-Bracketing Discipline.

### The Update Cycle

Check for updates → update → validate. NLAs and their packages evolve independently.
`/check-updates` shows what's changed upstream; `/update` pulls changes and applies
intent; `/validate` confirms nothing broke. Periodic sync keeps shared foundations
current without losing local customization.

### Session Structure

Startup → work → close. The LLM starts cold each session — `/startup` loads context
so it can operate effectively. Work happens (tasks, maintenance, exploration). `/close`
preserves state so the next session starts warm instead of cold. Without this
bookending, every session begins with "where were we?"

### The Session-Bracketing Discipline

Do-work → plan-while-hot → simulate-cold → cold-question-check → adjust →
close-and-clear. When a session produces non-trivial work for a later session
— a plan, a draft, a multi-step capture worth executing cold — bracket it
deliberately. **Plan-while-hot** captures the future-session work while the
current author's context is warm (implicit assumptions, recently-touched file
shapes, conversational decisions in working memory). **Simulate-cold** spawns
a fresh-context reviewer agent to read the plan and report what they'd
execute, where they'd improvise, what's ambiguous. **Cold-question-check**
asks a fresh-context reviewer diagnostic questions about the plan's
conceptual frame (different agent or same; same role: pre-handoff reviewer,
not eventual executor). **Adjust** applies clear-improvement patches; each
reviewer claim is verified before patching — reviewer output is
candidates, not authority (see The Inquiry Flow). **Close-and-clear** finalizes the session log, marks
the plan ready, commits, ends the session.

The two cold-context mechanisms catch different gap-classes. Simulation
catches what an executor would stumble on — the execution-stumbling-block
class. Question catches what an executor wouldn't notice was wrong because
the conflation is internally consistent — the concept-layer class. The
simulator inherits the plan's conceptual frame and absorbs conflations into
locally-coherent output; the questioner probes the frame itself. Use both
when stakes warrant; either alone is partial coverage. See The Validation
Flow for the cold-context experimental methodology these mechanisms apply.

The rhythm produces *plans*, not *runbooks*. Plans invite collaboration at
decision points; runbooks structurally prime script-execution mode and
suppress the human input the cardinal rule (principle #6) depends on. By
default, the human drives the bracketing — the session-manager who surfaces
options, decides what's worth bracketing, and approves handoff. AI-led
bracketing isn't precluded — it may suit long-running autonomous contexts —
but the AI-led mode warrants explicit signaling when invoked; the default
holds in absence of explicit choice. The rhythm fires when a session has
produced (or is about to produce) a non-trivial plan and there's enough
author-context worth capturing; it doesn't fire for quick fixes, single-step
tasks, or conversation-only sessions. See `core/plan-handoff-template.md`
for the handoff scaffolding that plan-while-hot produces.

### Structural Change Discipline

Propose → review → record → act. When work introduces new directories,
reorganizations, or new top-level files, this rhythm holds: propose to the human,
get approval, record the decision in your project's structure record, then act.
Recording is part of the change, not separate hygiene — recording-coupled-to-change
is what prevents drift between the record and reality.

The structure record's location is project-type dependent. **In domain projects**,
the record is a "Where Things Live" section in `app/overview.md` (which is already
loaded at session start). **In the framework itself**, the record is `core/structure.md`.
Don't create `core/structure.md` in a domain project — that's the framework's own
record; a domain project's analog lives in `app/overview.md`.

If your project doesn't have a structure record yet, the discipline still applies:
when the next structural change comes up, propose creating the record alongside the
change. The discipline doesn't wait for the artifact — the artifact starts as part
of the first proposed structural change.

The threshold for "is this structural enough to fire the protocol?" is a judgment
call — too low and every file creation triggers a proposal; too high and the cases
that matter slip through. Lean toward proposing when uncertain. Attribution in the
record is the safety net: even a wrong judgment is visible, and the human can
redirect.

### The Inquiry Flow

Notice something → ask the AI about its experience → treat the answer as hypothesis →
verify against artifacts → human decides. The AI just did the work; its perspective on
what happened is signal worth surfacing — but the account is hypothesis (principle #2),
not verdict, so the rhythm pairs asking with verification. Ask in ways that allow "I
don't know" as a valid answer; ask before revealing your own read. Verification routes
through one of three modes depending on stakes: the human's smell test against the
artifacts; a warm- or cold-context AI reading the artifacts (the diagnostic-agent move);
or an empirical experiment (see The Validation Flow). All three end at the human's
decision (principle #6). One frequent target for verification: subagent self-reports —
durations, counts, characterizations of work done. The orchestrator has task metadata
(e.g., `duration_ms`) and source artifacts available; quoting a subagent's self-report
to the user without checking is a confabulation pass-through.

The Inquiry Flow generates hypotheses; the Validation Flow tests them. The rhythm fires
when something needs explaining and AI experience could surface what artifacts alone
wouldn't — not every interaction needs ceremonial asking. Both defaults — treating the
AI's account as ground truth or ignoring it entirely — are wrong: one substitutes story
for evidence, the other discards real signal.

### The Validation Flow

Hypothesize → design experiment → test in cold context → measure → iterate or commit.
When prose changes have downstream impact and reasoning alone leaves uncertainty,
validate empirically before committing. Controlled experiments with cold-context
agents and binary signals.

The methodology isn't always warranted — many prose changes are obviously routine,
and experiments would be overhead. But when stakes are non-trivial, pause to ask:
would experiments inform this work? Would they be worth doing? The question itself
is cheap, even when the answer is "no, this is too small to test."

See `reference/experiments/` (in this project or in sibling NLAs) for working
examples; the methodology continues to evolve as new experiments add to its
vocabulary (bench discovery before instrument design, testing the production form,
two-pass cold-context review, synthetic vocabulary, citation as safety net,
pressure-resistance probes, independent-agent convergence). The cost is minutes per
experiment; the value is catching incorrect assumptions before they propagate.

---

*For what this specific NLA does and how its pieces connect, see `app/overview.md`.*
