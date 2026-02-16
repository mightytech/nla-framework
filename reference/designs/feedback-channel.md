# Design: NLA → Framework Feedback Channel

**Status:** In design
**Date started:** 2026-02-15
**Context:** Processing Duet's first feedback letter surfaced the need to design the feedback process itself — before processing the content.

---

## What This Document Is

A working design for how domain NLAs send learnings back to the framework. We're iterating on this — sections marked with decisions, leanings, or open questions. Decisions on one section may reopen others.

---

## The Problem

The framework improves through the experience of NLAs built on it. Currently there's no defined channel for this. Duet's feedback letter (`../nla-penny-post/boxes/framework/2026-02-14-duet-maintenance-learnings.md`) was the first attempt — it surfaced valuable patterns but also exposed questions about the process itself.

### What exists today

- **Friction log** — The framework's self-observations. "I noticed X while working on the framework."
- **Maintenance sessions** — Human-directed work on the framework.
- **Nothing** for domain NLA → framework feedback.

### Why feedback letters are different

Friction log entries are self-observations. Feedback letters are field reports from a different vantage point — what the framework looks like from the outside, from an NLA that was built on it. Different source, different signal, different processing needs.

### The deeper pattern: inter-agent communication

Feedback is an instance of a broader pattern: two human-driven AI agents communicating through shared artifacts. The domain NLA (AI + human) authors a letter. The framework (AI + human) reads, annotates, and responds. Both agents read and write to the same documents. The conversation is the document — not a linear email chain, but a collaborative artifact that evolves as both parties contribute.

This pattern is bigger than just feedback. Framework-to-domain guidance, domain-to-domain knowledge sharing, and framework internal design discussions (like this document) are all instances of the same thing: agents communicating through shared, editable artifacts.

---

## Foundational Decisions

### Scale and audience (Question 6)

**Decision:** Design for a handful of NLA developers who don't know each other. The framework is intended to be shared widely (light adoption expected, but strangers will participate). Two-part principle:

- **Artifact quality for strangers** — Letters, formats, triage records should be self-explanatory. A stranger should be able to write a good letter without talking to the maintainer, and a maintainer should be able to triage a letter from a stranger. No assumed shared context.
- **Process weight stays light** — The actual workflow stays light. Documentable in a page or two. No bureaucratic overhead that discourages participation.

The test: a stranger can participate effectively (artifact quality), but doesn't feel like they're filing a TPS report to do it (process weight).

### The medium: a shared mailbox repo (Question 1)

**Decision:** Feedback lives in a separate git repo — a mailbox that any NLA can write to and the framework can read from.

**Why a separate repo:**
- The framework repo stays clean — it's the application, not a communication channel
- The mailbox can be messy and that's fine. Real mailboxes get junk mail. You throw it out. The good mail you bring into your house and process.
- Both parties have read/write access to the same artifact
- Strangers can participate (PRs, forks) without access to the framework repo's internals
- Git gives you history, attribution, diffs for free
- GitHub's PR model provides conversation semantics (submit, review, comment, merge) with zero custom infrastructure

**Why not the framework repo:** Unprocessed letters look endorsed. Messy mail clutters the application. Separation of concerns — the framework is software, the mailbox is communication.

**What the mailbox contains:** Markdown files. Letters, annotations, conversations. No schema, no tooling, no deployment. Maintenance cost is effectively zero beyond reading the mail.

**Multiple return addresses:** The mailbox isn't only for domain NLA → framework. Framework → domain NLA, framework → framework (internal design conversations), even domain → domain — same mailbox, same conventions. The direction of communication is metadata, not infrastructure.

**Forks and the shared mailbox:** Because the mailbox is decoupled from any particular framework instance, forks of the framework see the same feedback. Each fork makes independent decisions about what to incorporate. A fork could accept feedback the main framework declined. The mailbox becomes a shared community resource — a marketplace of ideas where feedback is proposed once and evaluated independently by different maintainers.

### The apartment building: multi-box architecture

The mailbox NLA isn't one mailbox — it's an apartment building. Multiple boxes in one repo, one per project:

```
nla-penny-post/
├── CLAUDE.md
├── app/                     # How the mailbox NLA works
│   ├── overview.md
│   └── shared/
├── reference/               # Mailbox NLA's own maintenance artifacts
│   ├── friction-log.md
│   └── design-rationale.md
├── boxes/
│   ├── framework/           # Community mail about the NLA framework
│   ├── mailbox/             # Community mail about the mailbox NLA itself
│   └── ...                  # More boxes as needed
└── .claude/skills/
```

**The canonical repo** (published by the framework maintainer) ships with community boxes — `boxes/framework/` and `boxes/mailbox/`. These are the common spaces in the building.

**When a developer forks it**, they add boxes for their own projects:

```
boxes/
├── framework/               # Community box (from upstream)
├── mailbox/                 # Community box (from upstream)
├── duet/                    # This developer's project box
└── my-other-nla/            # Another of their projects
```

**The git flow:**
- `git pull` from upstream brings new community letters into `boxes/framework/` and `boxes/mailbox/` without disturbing private boxes
- PRs to the canonical repo submit letters to community boxes
- Private boxes stay local to the fork
- Adding a new box is just creating a directory

**What this solves:**
- One repo per developer, no matter how many NLAs they maintain
- The mailbox NLA's own feedback has a natural home — just another box, no special-casing
- Framework feedback from the community flows to everyone on pull
- No confusion about which mailbox goes with which project

**Privacy note:** Community boxes in the canonical repo are public. A developer's fork is also public by default on GitHub, which means their project-specific boxes are visible too. If someone wants private feedback, they either make their fork private or keep that feedback in their domain project's own `reference/`. The mailbox is for sharing — private feedback stays home.

### The mailbox as an NLA

The mailbox isn't just a collection of files — it's a Natural Language Application. It already has the defining properties: documentation that IS the application (the README defines how feedback works), an LLM as runtime (AIs read, triage, split, synthesize), natural language as interface (letters, annotations, config), judgment over rules (the AI decides how to process each letter).

**Decision:** Build the mailbox as an explicit NLA on the framework. It gets its own CLAUDE.md, app docs, skills, config, friction log — the full structure, kept lightweight. This means:

- **Self-improving.** If the mailbox bends at scale, the fix is better documentation — refine triage guidance, add synthesis patterns, update splitting approaches. The same iterate-through-documentation cycle that works for every NLA.
- **Dogfooding.** The framework's own feedback channel is built on the framework. "Here's an NLA that manages communication between NLAs."
- **A living counterexample.** The scaffold is a content transformation NLA (stateless, single-task). Duet is a creative NLA (persistent, tool-using). The mailbox is a communication/knowledge management NLA (multi-participant, stateful, non-transformation). Three shapes, one framework — a much stronger argument for "NLAs are general" than prose alone.

The NLA structure cleanly separates the mailbox's own maintenance (`reference/`) from the mail it manages (`boxes/`). The friction log in `reference/` is about the mailbox's behavior ("the triage patterns aren't working well"). The content in `boxes/` is feedback about other projects. Same separation any NLA has between system and content.

### The mailbox as a forkable pattern

The mailbox NLA is designed so others can fork it for their own purposes:

- **A domain NLA's feedback channel.** Duet gets users; those users want to send feedback. Fork the mailbox, customize the governance norms, point it at Duet's community.
- **Team collaboration.** A team building an NLA uses a forked mailbox as their coordination space. Letters become proposals, sub-letters become working groups.
- **Inter-NLA coordination.** Two NLAs that need to talk (content creation + content publishing) use a shared mailbox fork.
- **General knowledge management.** Strip the "feedback" framing and you have an NLA for managing collections of natural language documents with AI-assisted triage, splitting, synthesis, and search.

**What forkability requires:** Clean separation between domain-specific content (framework feedback norms, triage criteria for framework changes) and general patterns (letter format, annotation conventions, splitting, synthesis, mail checking). This falls out naturally from good NLA design — it's not extra work, it's the same principle that makes the scaffold forkable.

**The nested pattern:** The NLA framework helps you build NLAs. One of those NLAs is the mailbox. The mailbox can be forked into other communication NLAs. Three levels, all using "documentation is the application." Each level demonstrates the principle it's built on.

### The penny post as a feedback framework

The penny post isn't just an NLA — it's a framework. The same way the NLA framework provides development infrastructure via thin wrappers, the penny post provides feedback infrastructure via thin wrappers.

| | NLA Framework | Penny Post |
|---|---|---|
| **Provides** | NLA development infrastructure | Feedback processing infrastructure |
| **Installs via** | Thin wrappers in `.claude/skills/` | Thin wrappers in `.claude/skills/` |
| **Convention** | `../nla-framework/` | `../nla-penny-post/` |
| **Logic lives in** | `core/skills/` | `core/skills/` |

**Decision:** The penny post installs thin wrapper skills in participating NLAs, just like the framework does. Triage and mail-checking happen *inside the target project's context* (during `/maintain`), not in the penny post standalone. This means the AI has full access to the target project's files when assessing feedback.

**What this requires:**
- The penny post needs a `core/skills/` directory with external-facing logic — skill files designed to work from any NLA's context, referencing `../nla-penny-post/` paths explicitly. These are separate from the `app/` task docs (which are the penny post's own internal logic).
- Participating NLAs install thin wrappers (e.g., `.claude/skills/check-mail/SKILL.md` → `../nla-penny-post/core/skills/check-mail.md`).
- Each box gets a `BOX.md` config file identifying the target project and key files to read before triaging.

**How triage works in practice:**
1. Developer runs `/maintain` on their NLA (e.g., the framework)
2. `/maintain` offers to check the penny post (triggered by config directive or explicit request)
3. The check-mail skill scans `../nla-penny-post/boxes/framework/` for new letters
4. The triage skill processes items with full access to the framework's own files
5. Annotations are written back to the letter in the penny post

**The /maintain integration:** Rather than modifying `core/skills/maintain.md` directly, this is config-driven. A user adds "at the start of maintenance sessions, check the penny post for new mail" to their config. The AI reads this, sees the check-mail skill exists, and offers it. Pure NLA — config as behavior modification, no skill modification needed.

**Why this matters:** The letter carries the author's context (what the domain NLA experienced). But assessing whether feedback is valid requires the *target's* context (the project receiving feedback). Triage happens where the context is. The penny post provides the conventions and the mailbox; the target project provides the domain knowledge.

### Letter format (Question 2)

**Decision:** The format is a suggestion with published reasoning, not a mandate. Deviations are welcome when they serve the communication better — the reader is an LLM that applies judgment, not a parser.

**Suggested structure:**
- **Summary/abstract** at the top — what the letter is about, what kind of NLA, roughly how many items. Helps a triager decide whether and when to read the full letter.
- **Source** — NLA name, context (e.g., "after first major maintenance session"), repo URL (nice-to-have). Enough for a stranger to understand where this is coming from.
- **Items** with natural language confidence — each item describes an observation and how confident the author is that it's framework-general. Confidence is prose, not an enum: "high" and "high for multi-session NLAs, less sure about stateless ones" are both valid.
- **Everything else is freeform** — narrative context, suggested text, grouping by theme, priority, impact assessments. Include what you have; don't force what you don't.

**Annotation convention:** When the framework (or anyone) responds to a letter, annotations are blockquoted with attribution:

```markdown
> **[Framework, 2026-02-16]** Does this apply beyond tool-using NLAs?

> **[Duet, 2026-02-17]** Probably not in this exact form, but the broader
> principle feels general.
```

Annotations go wherever they make most sense — inline on a specific item, at the end as overall observations, or as new sections. Non-linear conversation, not email chains.

**What we deliberately excluded from required fields:**
- "What kind of change" (concept? tooling? scaffold?) — the triager is better positioned to determine where a change lands than the author.
- Rigid enum values for any field — natural language is the real interface. Enums are convenient defaults, not constraints.

**Why this format:** The mailbox README explains the reasoning so authors can make informed deviations. Key priorities for the framework: enough context to triage without talking to the author, confidence levels so the triager can calibrate, and freeform prose because the letter is an NLA artifact — flexibility is the point.

**Privacy note:** Domain NLAs may handle proprietary content. The exit interview skill should generalize — talk about patterns, not domain-specific content. Authors can also use NLA config to scrub specific information ("don't include details about X when submitting feedback"). Traditional software would need a privacy filter in code; the NLA just reads a config directive and applies judgment.

---

## Resolved Design Questions

### Triage process (Question 3)

**Decision:** Scan the full letter to get the lay of the land before implementing anything. Items may be interconnected — the verdict on one can affect another.

**What triage produces per item:**
- Verdict: accept / adapt / defer / decline (natural language — these are defaults, not an enum)
- Rationale (especially for decline and defer)
- Where accepted items land (which files, what blast radius)

**Who triages:** The framework maintainer (human + AI in /maintain mode). The AI can propose verdicts ("I'd accept items 1 and 3, defer 5, here's why") but the human decides. Same principle as the exit interview — no autonomous action on either side.

**Triage can span sessions.** A complex letter might need research, discussion, or time to think. The letter in the mailbox tracks triage state through annotations.

**Implementation doesn't have to wait for full triage.** Clearly independent items (a typo fix, a mechanical cleanup) can proceed while complex items are still being considered. The constraint: don't implement something whose verdict might change based on another item's outcome. The AI judges what's independent.

### What happens to triaged items (Question 4)

**Decision:** The letter is the tracker. No separate tracking infrastructure.

- **Accepted items** get brought "into the house" — implemented in the framework repo via /maintain. The letter is annotated with what was done and where.
- **Deferred items** stay in the letter with rationale and what would trigger revisiting. "Deferred pending more data points" vs. "deferred, low priority" — the rationale matters.
- **Declined items** stay in the letter with rationale preserved. Same principle as rejected alternatives in the design rationale — if someone proposes the same thing later, they should find the reasoning.
- **Need-more-info items** — the framework AI appends questions to the letter. The domain NLA reads them on its next check and appends answers. Asynchronous, artifact-based, non-linear.

### Communication (Question 5)

**Decision:** The mailbox is the communication channel. No separate mechanism prescribed.

The letter is the conversation. Both AIs can read and write to it, guided by their humans. Questions, answers, and triage decisions are all annotations on the shared document.

When the document isn't enough — when humans need to talk directly — they use whatever channel they prefer. The framework prescribes artifacts and conventions, not human communication channels. Ideally outcomes get captured back in the letter.

**GitHub layer:** If the mailbox is on GitHub, PRs and issues provide structured conversation (threading, notifications, status) on top of the document artifacts. Strangers get a natural interaction model for free.

### Feedback as anti-fork mechanism (Question 7)

**Decision:** The channel's value depends on responsiveness. If processing a letter takes weeks or the process feels heavy, domain projects stop sending letters and just build what they need locally.

The light process weight (question 6) and the mailbox model (question 1) address this. A letter that's easy to write and gets a prompt, visible response is better than a perfectly formatted letter that sits in a queue.

The shared mailbox strengthens this further: even if a fork diverges from the main framework, it still benefits from the community's feedback pool.

### Closing the loop (Question 8)

**Decision:** Closing the loop happens naturally through the mailbox. The framework annotates the letter with triage decisions. The domain NLA reads the annotations on its next check. No separate notification mechanism.

For GitHub-based mailboxes: PR comments and status changes provide notifications automatically.

---

## Checking Mail

The mailbox is passive — it doesn't push notifications. Both submitters and maintainers need a way to know something is there for them.

### Two layers of notification

**Activity-based (GitHub).** If the mailbox is on GitHub and letters are submitted as PRs, GitHub handles the basics: new PR = new letter, PR comment = response, merge/close = resolution. Both parties get GitHub notifications. Zero infrastructure.

**Content-based (NLA behavior).** This is where the NLA advantage shows. Any participant can define custom notification patterns in their config:

- A maintainer: "When checking the mailbox, highlight letters that mention persistence or lifecycle patterns."
- A submitter: "When checking the mailbox, look for responses to my previous letters."
- Anyone: "Flag high-confidence items from NLAs I haven't seen before."

The AI reads the config, reads the mailbox, filters accordingly. Semantic notification based on content, not just activity. No subscription system, no webhooks. Just prose in config.

### When to check

Checking mail is a behavior woven into existing skills, not a separate feature:

- **For maintainers:** The `/maintain` skill includes "check the mailbox for new or updated feedback" as an early step. The AI scans, summarizes what's new, the human decides what to engage with.
- **For submitters:** The exit interview skill checks for responses to previous letters before drafting a new one. Or the domain NLA's startup could include a mailbox check.
- **Custom patterns:** Anyone can add mailbox checking to any skill or config. "At the start of every maintenance session, check the mailbox" is a config directive, not a feature.

### Access

The AI needs to be able to read the mailbox repo. Options:
- `gh` CLI commands (no local clone needed, reads via GitHub API)
- Clone/pull the repo locally
- The auto-install pattern — the NLA sets up mailbox access when the dependency is first needed, with user permission

The mailbox repo URL is discoverable through the framework's documentation. Domain NLAs that want to participate store it in their config.

---

## The Exit Interview Skill

The primary way letters get written. A framework skill (in `core/skills/`, thin wrappers in domain projects) that runs after maintenance sessions.

### How it works

Human-initiated. The AI might suggest "some of this might be worth sending upstream" after a substantive maintenance session, but the human decides whether to run the skill. No phoning home. No monitoring.

The skill prompts reflection: what did you build that the framework should have provided? What was harder than it should have been? What patterns emerged? The AI drafts the letter based on the session's work; the human reviews, edits, and approves before submission.

### Flexibility

- One-item sessions might produce a quick note. Twenty-two-item sessions might produce a full letter. The AI judges what's worth saying based on the substance of the work.
- The skill uses the suggested format by default but doesn't enforce it. Users or AIs can improve upon or deviate from the format for specific reasons.
- Privacy directives from config are respected. The skill generalizes — patterns, not domain-specific content.

### Dependency management

The skill needs access to the mailbox repo. This is an installable dependency — the NLA sets up mailbox access (clone or configure `gh`) when the skill is first used, with user permission. This fits a larger NLA pattern: NLAs managing their own dependencies (the framework itself via tagged versions, external tools like SuperCollider, communication channels like the mailbox).

---

## Broader Patterns Surfaced

Concepts that emerged during this design that are bigger than the feedback channel:

### Inter-agent communication

Two human-driven AI agents communicating through shared, editable artifacts. The feedback channel is one instance. The pattern may deserve discussion in `nla-foundations.md` independent of this design.

### NLA dependency management

NLAs that install and manage their own operational dependencies — frameworks (tagged versions), tools (SuperCollider, plugins), communication channels (the mailbox). The NLA knows what it needs and can get it, with human permission. Connects to Duet's items on environment management and AI executing output.

### The NLA advantage demonstrated

This entire system demonstrates NLA principles:
- Natural language as the interface (letter format is prose, not schema)
- Judgment over rules (triage is judgment-based, format is suggested not mandated)
- Flexible on top, structured underneath (freeform letters, consistent annotation conventions)
- The LLM as runtime (reading letters, performing triage, synthesizing patterns, filtering by content)
- Documentation as application (the README IS the process)
- Config as prose (privacy scrubbing, notification patterns, checking behavior — all config directives, not code)

Traditional software would need: a ticketing system, a schema, a workflow engine, API endpoints, notification services, a database. The NLA version: markdown files in a git repo, conventions described in prose, interpreted by LLMs.

### Reusable NLA patterns

The mailbox NLA isn't just useful — it's forkable. This surfaces a framework-level question: can you build reusable NLA patterns that others customize? The scaffold demonstrates this for content transformation (fork and customize the article formatter). The mailbox demonstrates it for communication/knowledge management (fork and customize the feedback channel). If both work, the framework has two very different reusable patterns — evidence that NLA reusability is general, not limited to one domain.

---

## Design Principle: Flexible Units of Work

A letter arrives as one artifact but doesn't have to be processed as one artifact. The AI can split a letter into sub-letters — smaller, focused documents that reference the original — whenever it makes sense. "Makes sense" is a judgment call, not a rule:

- **Quick wins.** Pull out the trivial items and process them immediately while complex items get deeper triage.
- **Thematic grouping.** Group the persistence items together, the tooling items together, even across letters from different sources.
- **Cross-letter connections.** Item 3 from Duet's letter and item 2 from a future NLA's letter both address the same gap — combine them into a focused sub-letter.
- **Practical reasons.** The maintainer wants to tackle one item in this session and defer the rest.

Sub-letters reference the original ("From Duet letter 2026-02-14, items 1-3"). The original letter gets a note indicating it's been split ("Items from this letter have been split into: [list]"). The original stays intact as the primary source.

This is deeply NLA-native. A traditional ticketing system needs explicit "split issue" functionality, parent-child schemas, relationship tracking. The NLA version: the AI creates new markdown files with prose references. The relationships are sentences, not foreign keys.

**Sub-letters as triage output.** Instead of annotating the original letter with 16 inline verdicts, triage can produce sub-letters: a "quick wins" batch, a "needs discussion" group, a "declined with rationale" set. The original letter stays clean. Each sub-letter has its own focused conversation.

**The beginning of synthesis.** A sub-letter that combines "persistence" items from two different NLAs IS a synthesis artifact. The flexible unit of work is how the institutional memory layer emerges naturally — not as a deliberate knowledge management project, but as a byproduct of working with the mail.

---

## Design Principle: The Public Mailbox

The mailbox repo is public. Anyone can read, submit, and comment. This is a deliberate choice with significant implications.

### What transparency enables

- **Visible decision-making.** Anyone can see what feedback the framework has received, what was accepted, what was declined, and why. The framework's evolution is a public conversation, not a closed-door process.
- **Community signal amplification.** A stranger sees a letter about persistence and adds "we experienced the same thing" — one NLA's observation becomes a corroborated pattern.
- **Cross-pollination.** NLA developers learn from each other's letters without anyone curating the exchange.
- **AI-assisted community moderation.** The framework AI can summarize community sentiment across annotations, highlight constructive input, and filter noise. Traditional issue trackers need human moderators; the NLA has a built-in one that reads everything and applies judgment.

### Risks to watch

- **Noise and bikeshedding.** Open comments can drift from substance. The sub-letter pattern helps — focused conversations in focused artifacts.
- **Authority dilution.** Public pressure can complicate difficult decisions. Declining a popular request is harder with an audience. Popular isn't the same as right — the framework has a philosophy, and community input should inform it, not override it.
- **Scope creep via democracy.** Democratic input can push toward "what's popular" rather than "what's principled."
- **Toxic behavior.** The standard open source risk. Trolls, aggressive comments, unconstructive criticism.
- **Privacy beyond content.** Even with scrubbing, a public letter reveals "someone is building an NLA for X." The existence of certain NLAs or the problems they solve could itself be sensitive.
- **Maintainer burnout.** Active community engagement competes with framework development. The classic open source maintainer trap.

### Governance (light)

The mailbox README establishes norms — a few paragraphs, not a formal governance framework:
- The mailbox is open. Anyone can read, submit, and comment.
- The framework maintainer makes final decisions. Community input informs but doesn't override.
- Constructive feedback, respect for others' work, assume good intent.
- The mailbox is public. Write accordingly.

This is consistent with "process weight for A/B" — enough structure to set expectations, not enough to feel bureaucratic.

---

## Design Principle: The Mailbox as Institutional Memory

The mailbox isn't just an inbox — over time it becomes a knowledge base. Three layers of information accumulate:

1. **Raw letters** — Primary sources. Messy, detailed, specific to one NLA's experience.
2. **Triage records** — Verdicts and rationale per letter. Per-letter, attached to the source.
3. **Synthesized knowledge** — Cross-letter patterns. "Three NLAs have flagged persistence. Here's the pattern." Emerges across letters.

Layers 1 and 2 are per-letter. Layer 3 is the distillation — the institutional memory. A new maintenance session reads the synthesis instead of the archive. This is the same quarterback pattern as `config.md`: a light document that captures essentials and points to detail when needed.

**Where synthesis lives:** Unsettled. The mailbox is close to the source material. The framework repo is where synthesis informs decisions. Possibly both — the mailbox has the living synthesis, and crystallized conclusions migrate to the framework's design rationale.

**When to start:** Not yet. One letter has nothing to synthesize across. But the principle is established: the mailbox accumulates institutional memory, not just mail. When there's enough material to distill, the synthesis layer should exist.

---

## Parking Lot

Things worth noting that aren't ready to be questions yet:

- **Conflicting feedback.** Two NLAs might disagree. How does the framework resolve contradictions? (Not urgent until there are two NLAs sending feedback.)
- **Volume.** If many NLAs send letters, triage becomes a maintenance burden. Cadence? Priority fields? (Not urgent at current scale.)
- **Multi-agent/persona patterns.** All three whitepapers use multiple AI personas. The framework doesn't discuss this. Not part of the feedback channel design, but surfaced during this analysis.
- **Dual output streams.** Also surfaced from whitepapers, also not part of this design.
- **~~Mailbox repo name.~~** Decided: `nla-penny-post`. Named after the 1840 British postal reform that democratized communication — fitting for a project about democratizing software development beyond coders.
- **When to create the mailbox repo.** Now? When the framework goes public? Can it exist with a README that says "this is in design"?
- **Testing with the Duet letter.** Retroactively format the Duet letter as a test case. Move it into `boxes/framework/` in the mailbox repo. A draft triage exists at `reference/feedback/2026-02-15-duet-triage-draft.md` for comparison with the formal penny post triage.
- **Box naming conventions.** Should box names match repo names? NLA names? Or is it freeform? Probably freeform with guidance.
- **BOX.md format.** Each box needs a config file pointing to the target project. What fields? Just a path and key files, or more?

---

## Next Steps

1. ~~Create the penny post NLA~~ — Done (2026-02-15). Basic project at `../nla-penny-post/`.
2. Refine the penny post via `/maintain` — use the Duet letter as a test case. Move the letter from `reference/feedback/` to `boxes/framework/`. Add `core/skills/` for external-facing logic. Add `BOX.md` config files.
3. Add feedback skills to the framework — install penny post thin wrappers in the framework (check-mail, triage). Build the exit interview skill in `core/skills/`. Add config guidance for mail-checking during `/maintain`.
4. Formal triage of the Duet letter through the penny post — compare with draft triage at `reference/feedback/2026-02-15-duet-triage-draft.md`.
5. Implement accepted items in the framework — use triage results to update `nla-foundations.md`, `core/skills/startup.md`, `core/skills/validate.md`, `/create-app`, etc.
6. Close the loop — annotate the Duet letter with what was implemented. Resolve the framework friction log entry.

---

*This document is updated during the feedback channel design process. It will eventually become either a section of design-rationale.md (if the design is simple) or remain as a standalone design doc (if it's substantial).*
