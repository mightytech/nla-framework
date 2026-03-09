# Coherence Review

Re-read the NLA's foundational documents — the files loaded at startup — checking whether each one works as a unit. This catches problems that structural checks and architecture review miss: redundancy within a document, sections that don't earn their place, flow that breaks after edits.

### When to Run

- After adding, removing, or reordering sections in foundational docs
- After a maintenance session that touched multiple parts of one document
- Periodically, as documents accumulate edits across sessions
- When a document "feels off" but passes structural checks

---

## Process

### 1. Identify Startup Files

Determine which files are loaded at startup — typically CLAUDE.md, nla-foundations.md
(via the framework), the project overview, and shared context files (values, voice,
patterns). These are the documents that shape every interaction. If `/startup` exists,
trace its reading list.

### 2. Read Each File as a Unit

Read each startup file fully, start to finish. You are reading it as a reader, not
searching for a specific issue. The question is: does this document hold together?

### 3. Check For

**Redundancy** — The same idea stated in multiple places within one document. Some
reinforcement is fine (a principle restated in a different context). But when two
sections say the same thing at the same altitude, one should probably be removed or
the two should be consolidated.

**Flow** — Does the document build naturally? Does each section follow from the
previous one? After edits, sections can end up in an order that made sense
historically but doesn't read well sequentially.

**Weight distribution** — Are sections proportional to their importance? A minor
point with three paragraphs next to a major point with one sentence suggests the
document has drifted from its priorities.

**Orphaned content** — Sections or paragraphs that no longer connect to what's around
them. After removing or rewriting neighboring content, a section can lose its context
and feel stranded.

**Tone consistency** — Does the document maintain a consistent voice throughout?
Sections added at different times or by different sessions can shift register in ways
that feel uneven.

**Earned placement** — Does every section justify its presence in a file that's loaded
every session? Foundational docs have a cost — they consume context window and
attention. Content that's rarely relevant or only matters during maintenance may
belong elsewhere.

### 4. Report Findings

For each document reviewed, note:
- Whether it reads well as a whole (many will — that's a valid finding)
- Specific coherence issues with location and suggested resolution
- Whether the issues are worth fixing now or noting for future maintenance

---

## Output

Present findings conversationally — this isn't a formal report. For each document:

- **Reads well** — Say so briefly. No need to elaborate on documents that work.
- **Issues found** — Describe the coherence problem, where it is, and what would fix it. Classify as fix (worth changing now) or note (worth knowing, not urgent).

If issues are found, suggest whether to fix them now (if in a `/maintain` session) or
log them to the friction log for later.

---

*Coherence review complements architecture review: architecture checks consistency
between documents; coherence checks consistency within them.*
