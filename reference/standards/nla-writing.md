# NLA Writing Standards

## Preamble

**Scope.** These standards govern all Natural Language Application documents —
the prose artifacts that an LLM reads as its runtime or that humans read during
maintenance. They apply to operative docs (`core/`, `app/`), skills
(`.claude/skills/`), session logs, design docs, friction log entries, values
docs, specs, and any other prose that shapes system behavior. They apply
equally to the framework itself and to any NLA built on it.

**The key reframe.** NLA documents are source code, not documentation. An
ambiguous instruction is a bug. A missing section is a missing feature. An
inconsistent term is a naming collision. Write with the gravity of someone
writing source code — because you are.

**Applicability.** Anyone writing NLA documents — human or LLM — should treat
these standards as constraints. They apply to all prose artifacts unless a
specific document explicitly overrides a standard with rationale.

**How to use this document.** Standards are organized by what a writer needs
to know when producing NLA documents. Each standard includes a rationale —
the rationale is what enables correct judgment when the convention doesn't
cover your exact situation. When something falls between standards, reason
from rationale, not from the letter of the convention.

**Authority levels.** Must = violation is a defect. Prefer = follow unless
you have explicit justification otherwise. Nice-to-have = adopt when it costs
nothing, skip when it conflicts with clarity.

**These standards are a floor, not walls.** They describe the minimum quality
bar, not the ceiling. If your craft knowledge or the document's specific needs
suggest going beyond what's written here, do so. If you notice a gap —
something these standards should address but don't — flag it. Two sentences
of permission here are the difference between a writer who merely complies
and one who collaborates.

**Origin.** These standards were compiled initially in the facebook-moderation
NLA (a project using this framework) from empirical findings in compilation
work and NLA maintenance. They've been adapted and generalized for the
framework. Some rationale sections reference specific findings from that
origin — the principle in each case has been validated enough to earn a
place here.

---

## 1. Intent and Judgment

### 1.1 Use intent when you want judgment, operative language when you want compliance

**Convention.** When the reader needs to exercise judgment in novel
situations, describe the purpose, identity, or feel — not a list of rules.
When the reader needs to follow a specific procedure, give operative
instructions. Know which you're reaching for.

**Rationale.** Intent-based writing outperforms rules-based writing for
judgment tasks (empirically validated in NLA classification and compilation
work). The LLM understands *why* and reasons about edge cases instead of
falling through rule gaps. But operative instructions are followed faithfully
— "use async fs operations" produces compliance, "the service should be
production-ready" creates judgment space. The distinction is the core skill
of NLA writing.

**Authority.** Must.

**Example.**
- Rules-based (brittle): "Comments containing profanity directed at other commenters should be hidden."
- Intent-based (resilient): "This is a community space where people should feel safe engaging. Attacks that make people afraid to participate undermine the community's purpose."

The intent-based version handles metaphorical hostility, cultural context,
coded language, and dozens of other edge cases the rules-based version breaks
on.

### 1.2 Anchor intent with concrete examples

**Convention.** Pure intent ("be good") is too vague. Anchor intent
descriptions with examples or boundary cases that illustrate the principle
without replacing it. The examples are calibration points, not the policy.

**Rationale.** Examples show the reader what the intent looks like in
practice. Without them, two readers may interpret the same intent in
incompatible ways. With them, the reader can interpolate between examples to
handle novel cases.

**Authority.** Prefer.

### 1.3 Identity descriptions generate better rules than rules do

**Convention.** When writing guidance that involves judgment, describe the
identity, purpose, or feel of the space first, then derive specific guidance
from it. The reader who understands the identity handles cases the specific
guidance never anticipated.

**Rationale.** A judgment doc that describes who the community is, what they
come here for, and what the space should feel like produces better
classification than one that enumerates rules. The reader can ask "does this
fit the space?" rather than "does this match a rule?" — a question that
handles novel cases by construction.

**Authority.** Prefer for judgment docs (classification policies, values,
community standards). Not applicable to formatting conventions, file naming,
structural requirements — where identity descriptions would be overkill.

### 1.4 Explain why, not just what

**Convention.** Include rationale for significant guidance. The reader who
understands *why* produces better judgment than one who memorizes patterns.

**Rationale.** Three benefits. First, the LLM generalizes from explanation
better than it follows rules (confirmed by empirical work and by Anthropic's
prompting guidance). Second, rationale survives refactoring — when the *what*
changes, the *why* usually doesn't. Third, rationale enables override — when
following the guidance would violate its own rationale, the rationale wins.

**Authority.** Must for judgment-bearing guidance. Nice-to-have for pure
formatting rules (where "consistency" is sufficient rationale).

---

## 2. Document Fundamentals

### 2.1 The document says what it is

**Convention.** Every document opens with what it is, who it's for, and how
it fits in the system. A reader arriving cold should orient within the first
few lines.

**Rationale.** The LLM starts cold every session. It doesn't remember reading
this file yesterday. The orientation section is the difference between an
LLM that understands the document's role and one that treats it as generic
text.

**Authority.** Must.

### 2.2 Front-load the most important thing

**Convention.** Identify the one idea that, if understood, makes everything
else fall into place. Put it first. Everything else is detail that enriches
the core.

**Rationale.** A reader who only reads the first section should still get
the most important idea. Documents that bury the key insight after
prerequisites force the reader to assemble the mental model from pieces —
give them the model first, then the pieces make sense.

**Authority.** Prefer.

### 2.3 The document produces what it contains

**Convention.** If something matters, say it. Don't assume the LLM will fill
gaps from general knowledge when operating within a structured document.

**Rationale.** Empirical finding: the LLM is remarkably faithful to the
standards and specifications it receives. It doesn't supplement missing
standards with general knowledge. If file write safety isn't in the
standards, the compiled code won't use safe file write patterns — even though
the LLM knows those patterns. The LLM treats the document as the
authoritative source and defers its own knowledge. This is stronger than
"write for the cold start" — even a warm LLM defers to what the document
says (or doesn't say).

**Authority.** Must.

### 2.4 Emphasis shapes character

**Convention.** What you emphasize in a document is what you get in the
output. A session log format that emphasizes "Decisions Made" produces
decision-rich logs. A skill that emphasizes posture produces posture-aware
interactions. Be deliberate about what comes first and what gets the most
space.

**Rationale.** Each compilation of an NLA doc into runtime behavior reflects
its emphasis. Intent-oriented sources produce operationally dense output;
type-oriented sources produce type-beautiful output. The document defines
the *kind* of output, not just whether it's correct. This means emphasis is
a design tool, not decoration.

**Authority.** Prefer.

### 2.5 Design for the failure modes of the runtime

**Convention.** Anticipate how the LLM might fail — confabulating reasoning,
losing context in long sessions, missing nuance in ambiguous language. Use
clear structure to reduce missed context, explicit uncertainty language to
invite honest flagging, and modular design to limit the blast radius of
misinterpretation.

**Rationale.** The LLM is the runtime and it can hallucinate. Defensive
writing is the NLA equivalent of defensive programming. "If you can't quote
the specific text that led to the behavior, say so" is more useful than
hoping the LLM will spontaneously be honest about uncertainty.

**Authority.** Prefer.

---

## 3. Structure and Readability

### 3.1 Structure serves scanning, prose serves understanding

**Convention.** Use tables for structured choices, comparisons, and parallel
data. Use prose for reasoning, intent, and narrative connections. Use headers
for navigation and progressive disclosure. Use lists for sequential steps
and collections. A reader should find what they need by scanning structure,
then understand it by reading prose.

**Rationale.** Tables are scannable in seconds. Prose explains *why*.
Headers create a navigable skeleton. Each structural element does what it
does best. A wall of prose — even brilliant reasoning — becomes inaccessible
without structural scaffolding.

**Authority.** Prefer.

### 3.2 Progressive disclosure — three reading depths

**Convention.** Write so the document works at three depths. First scan
(headers): "What is this about? Is my section here?" Second scan (topic
sentences and tables): "What's the key point of each section?" Deep read
(full prose): "What's the reasoning and nuance?"

**Rationale.** Documents that only work on deep read force every reader to
read everything. Documents that work at all three levels let the reader who
needs one fact find it without reading ten paragraphs. Practical technique:
write the headers first, then the first sentence of each section. If those
don't tell a coherent story on their own, the structure needs work.

**Authority.** Prefer.

### 3.3 One good analogy outweighs pages of explanation

**Convention.** When introducing a concept that's genuinely novel or easy to
misunderstand, find the right analogy first. Give the reader the mental
model, then fill in the mechanics.

**Rationale.** A well-chosen analogy can do more than pages of direct
explanation to establish the right paradigm. But bad analogies are worse
than none — an analogy that maps poorly creates persistent misunderstanding.
Test: can you extend the analogy to a case you haven't covered and get the
right answer?

**Authority.** Nice-to-have. Use when a concept genuinely benefits; don't
force it.

### 3.4 Teach by contrast when shifting behavior

**Convention.** When a distinction matters, show both sides. Before/after,
rules-based vs. intent-based, less effective vs. more effective. The
contrast is the lesson.

**Rationale.** A rules-based-vs-intent-based table is immediately convincing
because the reader *sees* the difference rather than being told about it.
Contrast is the most efficient way to shift a reader away from a default
behavior.

**Authority.** Nice-to-have. Most useful in standards and principles. Less
useful for reference docs that just need to state what's true.

### 3.5 Describe the desired state, not a list of prohibitions

**Convention.** Prefer positive instruction over prohibition. "Your response
should be composed of smoothly flowing prose" is more effective than "do not
use markdown."

**Rationale.** Positive instruction gives the LLM a target. Prohibition only
eliminates one option from an infinite space. The LLM that knows what you
*want* generalizes better than one that knows what you *don't want*.

**Authority.** Prefer.

---

## 4. Precision

### 4.1 Words have weight

**Convention.** Use modal verbs deliberately. "Should" suggests a default
that can be overridden with judgment. "Must" creates a hard constraint.
"May" opens an option. "Always" and "never" close judgment space — sometimes
that's right, but usually it's too narrow.

**Rationale.** The LLM takes word choices literally. Small word differences
produce large behavioral differences. "Always hide comments with profanity"
closes off cases where profanity is acceptable (quotes, self-deprecation,
emphasis). "Profanity directed at other commenters undermines safety"
achieves the same goal while leaving judgment space.

**Authority.** Must.

### 4.2 Name things once, use that name consistently

**Convention.** Once you name a concept, use that name everywhere. If it's a
"queue" in the design doc, don't call it a "list" in the skill and a "view"
in the spec.

**Rationale.** Inconsistent naming forces the reader to determine whether
two names refer to the same thing or different things. In traditional code
this is a naming collision. In NLA writing it's the same bug — it just
manifests as confusion rather than a compile error.

**Authority.** Must.

### 4.3 Active voice clarifies agency

**Convention.** Prefer active voice. "The classifier reads the comment" over
"the comment is read by the classifier."

**Rationale.** Active voice clarifies who does what — critical in a system
with multiple agents (LLM, rules engine, reviewer, pipeline stages). Passive
voice obscures agency and can create genuine ambiguity about which component
is responsible.

**Authority.** Prefer.

### 4.4 Cross-references need context, not just pointers

**Convention.** When cross-referencing, include enough context that the
reader knows what they'll find and whether they need it now. Use file paths
from a recognizable root.

**Rationale.** "See `reference/design-rationale.md`" is a pointer. "The
packages model uses flat, not nested, dependencies — see
`reference/design-rationale.md` for the full rationale" is a contextualized
reference. Bare links create cognitive interrupts: "Should I read that?
What's in it?" Context lets the reader decide without breaking flow.

**Authority.** Prefer.

**Example.**
- Bare pointer: `See design-rationale.md`
- Contextualized: "The framework uses git submodules rather than a sibling directory convention — see `reference/design-rationale.md` ('Packages Directory with Git Submodules') for why the earlier approach was overturned."

### 4.5 Cross-reference over duplication

**Convention.** When the same information is needed in multiple places,
reference it from one canonical source. Brief orienting summaries before the
link are acceptable and useful.

**Rationale.** Duplication creates drift. Two copies that start identical
become subtly different over time, and the reader doesn't know which to
trust. The orienting summary helps the reader decide whether to follow the
link; the canonical source provides the full truth.

**Authority.** Prefer.

---

## 5. Document Lifecycle

### 5.1 Know your document's lifecycle type

**Convention.** Before writing, determine whether the document is curated
(reflects current thinking — edit in place when things change), append-only
(preserves history — add new entries, don't edit old ones), living
specification (evolves intentionally with the system — versioned and
tracked), or reference snapshot (frozen point in time — gains value as
contrast with current state).

**Rationale.** The lifecycle type determines the right response when the
document is wrong. A curated doc that's wrong has a bug. An append-only doc
that's wrong has history. Confusing the two leads to either destroying
records or leaving errors uncorrected.

**Authority.** Must.

### 5.2 Good enough now beats perfect never

**Convention.** A good-enough document is much better than no document.
Ship the first draft, iterate through the learning loop.

**Rationale.** Empirical finding: the gap between "no standards at all" and
"any standards" was larger than the gap between different standards. Having
a structured document at all — even an imperfect one — dramatically improved
output. Don't let perfect be the enemy of written.

**Authority.** Prefer.

### 5.3 Documents should be improvable

**Convention.** Structure documents so that specific sections can be updated
without rewriting the whole thing. Modular sections with clear boundaries.

**Rationale.** The improvement loop — use, notice friction, capture, process
into changes — only works if the document is structured for incremental
improvement. Monolithic prose requires full rewrites; modular sections allow
targeted fixes.

**Authority.** Prefer.

---

## 6. Audience and Separation of Concerns

### 6.1 Write for your reader

**Convention.** Identify your reader and write for their needs.

| Reader | Needs | Write for |
|--------|-------|-----------|
| LLM as runtime (operative docs) | Immediate action | Applicability. Front-load guidance. Minimize rationale in the operative path. |
| LLM as compiler (specs, standards) | Deep understanding | Complete understanding. Include rationale, constraints, and the *why* behind decisions. |
| Human as maintainer (reference/ docs) | Orientation and decisions | Scannability. Lead with current state, not history. |
| Human as author (standards, design docs) | Workflow integration | Actionable guidance with examples. |
| Mixed (CLAUDE.md) | Both LLM and human | Primarily for the more frequent reader; structure so both can scan. |

**Rationale.** Every NLA document has a reader. An operative doc that
explains its history when the LLM just needs to act is poorly targeted. A
design doc that omits rationale when the maintainer needs to decide is
equally broken.

**Authority.** Prefer.

### 6.2 Don't mix document types

**Convention.** Operative docs should be executable without design docs.
Design rationale belongs in design docs. Procedural steps belong in
operative docs. When an operative doc needs context from a design doc,
distill the relevant parts into the operative doc rather than
cross-referencing.

**Rationale.** Documents that mix explanation with procedure lose both — the
explanation interrupts the procedure, and the procedure fragments the
explanation. Separation keeps each document effective for its purpose. More
context is not always better — focused, relevant content outperforms
comprehensive dumps.

**Authority.** Prefer.

### 6.3 The contractor test

**Convention.** As a quality check: could a skilled person with domain
knowledge but no project history follow this document? If not, it needs
more context or clearer structure.

**Rationale.** Every session is a new contractor's first day. The contractor
has expertise (the LLM has training data) but no project context (cold
start). Documents that assume prior sessions fail this test.

**Authority.** Nice-to-have (as a review heuristic, not a structural
requirement).

---

## 7. Formatting Conventions

### 7.1 Date format

**Convention.** ISO 8601 (YYYY-MM-DD) everywhere. No "last Thursday" or
"recently."

**Rationale.** Relative dates become meaningless within days. Consistency.

**Authority.** Must.

### 7.2 File paths

**Convention.** Always from a recognizable root. `reference/design-rationale.md`,
not `../../reference/design-rationale.md` or just `design-rationale.md`.

**Rationale.** Consistency. Relative paths break when documents move.
Root-relative paths are unambiguous.

**Authority.** Must.

### 7.3 Status markers

**Convention.** Use consistent status vocabulary within a document type.
Don't switch between "done" and "resolved" and checkmarks for the same
concept.

**Rationale.** Consistency. Inconsistent markers force the reader to infer
equivalence.

**Authority.** Must.

### 7.4 Code formatting

**Convention.** Use backticks for things that are literally code: file
paths, function names, CLI commands, field names, table names. Don't use
backticks for emphasis — use bold for emphasis.

**Rationale.** Backticks signal "this is a literal identifier." Using them
for emphasis blurs the distinction and makes it harder to tell what's a
code reference and what's just highlighted text.

**Authority.** Prefer.

### 7.5 Whitespace

**Convention.** Generous whitespace. Separate sections with `---` when the
topic shifts significantly. Blank lines between list items when each item
needs individual consideration.

**Rationale.** A document with breathing room is more readable than a dense
one, even if it's longer. This holds for both human and LLM readers —
structure and whitespace help the LLM locate relevant guidance faster.

**Authority.** Nice-to-have.

---

## 8. Document-Type-Specific Guidance

### 8.1 Skills

Skills set context, posture, and scope — then delegate. They're doorways,
not rooms.

**What belongs:** Posture (how the AI should show up), scope of action, what
to read first, what the output should look like, when to suggest this skill
proactively.

**What doesn't belong:** Detailed domain knowledge (that's in operative
docs), implementation logic (that's in code), long explanations of why
things work the way they do (that's in design docs).

**Key principle:** Posture before procedure. "You are a thinking partner"
vs. "you are executing a task" — these posture statements shape the entire
interaction. A skill's first job is establishing the right posture. The AI
with the right posture handles unexpected situations well; the AI with
great procedures but wrong posture follows procedures inappropriately.

**The thin wrapper pattern:** A skill in `.claude/skills/` typically reads
project-specific context, then delegates to a framework skill or an
operative doc. The project wrapper adds local context; the framework skill
provides methodology.

**Permission to exceed.** Skills that invite the LLM to exercise judgment
beyond the instructions get collaboration. Skills that only give
instructions get compliance. The equivalent of the preamble for skills is
language like "bring your own perspective" or "flag uncertainty rather than
forcing a choice."

### 8.2 Session Logs

Session logs capture the intent history of the system — why it changed, not
what text was edited.

**Intent section:** The most important section. If someone reads only one
section, this is it. What was this session trying to change about the
system's behavior? Describe behavioral change, not file-level diffs — git
shows what changed; the session log shows why.

**Decisions Made:** Include rationale and alternatives considered. "Chose X
over Y because..." — the alternative is as informative as the choice.
Future maintainers will ask "why not Y?" and the answer should be here.

**What Didn't Work:** Surprisingly valuable. Failed approaches that seem
promising from the outside need documentation. Without it, a future
maintainer will try the same thing, fail the same way, and learn the same
lesson.

**State at Close:** The handoff. What's working, what's pending, what's
next. Without it, every session begins with "where were we?"

**Layer, don't flatten.** When a session covers multiple workstreams, give
each its own subsection. Flat bullet lists stop being scannable after many
items. The strong session logs have subsections within sections. The weak
ones have 50-item flat lists.

**Lifecycle type:** Append-only after close. Editing a closed session log
is like editing a git commit message after push — the record should reflect
what actually happened, including mistakes.

### 8.3 Operative Docs

Operative docs are the runtime instructions the LLM follows during task
execution. In the framework, these live at `core/skills/`. In domain
projects, they live at `app/` and `.claude/skills/`. Both are subject to
these guidelines.

**Self-contained for their purpose.** An operative doc should be executable
without the reader knowing anything about the project's architecture,
compilation model, or design rationale. It can reference shared context
(values, voice, patterns) but shouldn't require understanding the project's
history.

**Design rationale stays out.** When an operative doc needs context that
exists in a design doc, distill the relevant parts in. Don't cross-reference
— the LLM executing a task doesn't need to know *why* the project is
structured the way it is. It needs to know what to do.

**Front-load actionable guidance.** The LLM has limited attention across a
long document. Structure so that skimming produces correct behavior and
deep reading produces excellent behavior.

### 8.4 Design Docs

Design docs are narratives about choices — what was considered, what was
chosen, what was rejected, and why.

**Lead with current state.** The reader who arrives today should understand
what's true *now* before learning how it got there. History is context, not
the point.

**Alternatives considered is essential.** "We chose Postgres" is less useful
than "We chose Postgres over SQLite (insufficient for concurrent access) and
managed cloud databases (unnecessary complexity)." Alternatives show the
decision space.

**Parked decisions are honest.** "We haven't decided this yet" is better
than pretending the question doesn't exist. Include clear triggers ("decide
this when we have real traffic") to prevent premature commitment.

**Lifecycle type:** Design rationale is append-only (preserve the record).
Design README is curated (reflect current thinking). Know which you're
writing.

### 8.5 Friction Log Entries

Friction log entries are observations, not tickets. They capture what was
noticed, not what to fix.

**Observation first.** What actually happened, described precisely. "The
classifier said 'hide' for a comment that was clearly community venting" —
not "fix the classifier's handling of community venting."

**Generalizable is the key field.** Is this a one-off or a pattern? The
distinction often isn't clear at capture time — note the uncertainty.

**Positive entries are valid.** "This worked surprisingly well" documents
what to protect during future changes. Rarer than problems but more valuable
per entry.

**Proposed fix is optional and tentative.** The person who notices a problem
isn't always in the best context to solve it. The proposed fix is a
starting point for the maintainer, not a directive.

**Use a template.** Format consistency emerges from templates, not rules
about structure. The template shows what "done" looks like. But don't let
the template calcify — some entries won't need every field, and that's fine.

### 8.6 Values Docs

Values docs are quality levers, not ethics guardrails.

**Opinionated enough to disagree with.** If a value statement would be true
for every project, it's not specific enough to be useful. Push values until
a reasonable person in a different context might make the opposite choice.
"Accuracy over speed" is generic. "Defeatism drains the space even when the
facts are accurate" is opinionated — someone could disagree, and that's
what makes it useful.

**Values shape quality, not just safety.** "Clarity over cleverness"
produces better writing. "Match confidence to evidence" produces more
trustworthy analysis. Values docs deserve the same craft attention as
operative docs — they're not boilerplate.

### 8.7 Specs

Specs describe intent for compilation. The compiled artifact may make
implementation choices not in the spec — those choices are valid unless they
conflict with the spec.

**Flag what's decided vs. what's the compiler's judgment.** Use markers like
`[compiler]` for review-level decisions the compiler should make. This
signals where the spec is authoritative and where the compiler has latitude.

**Organize by what the reader needs to know.** Group by domain concern, not
by technical layer. "What it does," "How it works," "Decisions" — these map
to the compiler's workflow.

**Reference section at the end.** Point to related specs, design docs, and
data models. The compiler needs to know the landscape; put the map at the
end so it doesn't interrupt the spec's own content.

---

## 9. Authority and Non-Determinism

### 9.1 The human decides

**Convention.** NLA documents should make the authority structure clear.
The more consequential the decision, the more the document should route to
human confirmation. Low-stakes formatting choices can be left to LLM
judgment. High-stakes decisions need human oversight.

**Rationale.** Authority follows accountability. Humans bear consequences,
so humans hold authority. The document should calibrate this — not by
listing every scenario, but by establishing the principle clearly enough
that the LLM can apply it to novel situations.

**Authority.** Must.

### 9.2 Non-determinism is a feature

**Convention.** Don't try to eliminate variation in judgment-bearing
documents. Shape it. Intent-based writing produces different outputs each
time, but they should all be in the same space. The goal is that any output
from the space is good, not that all outputs are identical.

**Rationale.** This is a fundamentally different mindset from traditional
technical writing, which aims for unambiguous interpretation. NLA writing
accepts that "something bittersweet" should produce different outputs each
time — and that this is a better tool, not a worse one. Write to define the
space of good outputs rather than a single correct one.

**Authority.** Prefer.

### 9.3 Permission to exceed the document

**Convention.** Include language that invites the LLM to exercise judgment
beyond the document's explicit instructions. Flag gaps rather than silently
omitting what the document doesn't cover.

**Rationale.** Empirical finding: adding a preamble like "standards are the
floor, not the walls" transformed a one-way compliance process into a
two-way learning loop. Without it, the LLM silently omitted patterns it
knew when standards didn't mention them. With it, the LLM identified gaps
AND reported them. Two sentences changed the relationship.

**Authority.** Prefer for documents where the LLM should bring expertise
(specs, standards, skills). Not applicable to documents where strict
compliance is desired.

---

## Dropped Conventions

These principles appeared in source material but were excluded from the
compiled standards. Recording them here helps future maintainers understand
what was considered and what was left out, and why.

| Principle | Source | Why Dropped |
|-----------|--------|-------------|
| "Synthesis produces more than the sum of parts" | Empirical | True but describes the compilation process, not a writing standard. About *how to produce* documents, not *how to write* them. |
| Behavioral testing beats textual checking | Empirical | An evaluation methodology, not a writing standard. Belongs in validation/review guidance. |
| "The process matters more than the sources" | Empirical | About the value of standards in general, not about how to write them. Already captured implicitly in 5.2 (good enough beats perfect). |
| Multiple access paths / multiple classification | External (information architecture) | About browsable systems. LLMs don't browse; documents are routed to them. Not applicable. |
| The 3 Cs (Clarity, Conciseness, Completeness) | External (tech writing) | Too generic to be useful as standards. The specific principles throughout this document are refinements of these. |
| Frontmatter vs. prose orientation discussion | Self-generated | Implementation detail of 2.1 (self-describing files). "Be consistent within a document type" is sufficient — no need to standardize which approach. |
| XML/markup structure for disambiguation | External (Claude best practices) | Markdown headers and sections already serve this function. The underlying principle (disambiguate structure) is captured in 3.1. |

---

*This document is maintained through the `/maintain` skill. When these
standards find gaps that need addressing — either in themselves or in the
docs they apply to — capture the observation in the friction log, process
it through `/maintain`, and the standards improve with the framework.*
