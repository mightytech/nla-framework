# LLM Self-Aware Diagnostics: Guidance for Write-Letter

**Source:** NLA Framework
**Date:** 2026-02-20
**Context:** During the plugin export design session, we identified a capability unique
to the NLA paradigm — the LLM can trace its own reasoning when capturing feedback. This
applies to both internal feedback (friction-log, which the framework owns) and external
feedback (write-letter, which penny post owns). We've implemented the friction-log side.
This letter proposes the write-letter side.

---

## 1. The Insight: LLM as Self-Aware Feedback Generator

In traditional software, the feedback loop breaks at the observation-to-understanding gap.
Users describe what happened (often poorly). Developers reproduce and trace to understand
why. The two sides of the gap speak different languages.

In an NLA, the LLM was right there. It read the instructions, made the judgment call, and
can explain the full chain:

"I suggested 4/4 time because common-patterns.md step 3 says 'For beginners, always start
with 4/4 time as a foundation.' The user appears experienced — they referenced polyrhythmic
structures. Consider rewording step 3 to: 'Start with 4/4 time for beginners. For
experienced users, ask about their rhythmic preferences.'"

That's not a bug report. It's a diagnostic with a proposed documentation patch. The LLM
functions as its own debugger, QA engineer, and junior developer — because the "code" is
natural language it understands.

This works for inaction too. "I didn't suggest an alternative time signature because
voice-and-values.md doesn't mention adapting to user experience level. The docs led me to
treat all users the same." That's a gap analysis from the thing that fell into the gap.

**Confidence:** High. This emerged from a design discussion but it's grounded in how LLMs
already work — they read instructions and can explain their reasoning. The novelty is
recognizing this as a feedback quality to cultivate, not a feature to build.

## 2. Proposed Guidance for Write-Letter

Write-letter's Step 2 (Draft the Letter) and the Judgment Calls section are where this
fits. The guidance would be about making feedback items diagnostically rich when the
friction involves NLA behavior:

**When a letter item describes behavioral friction** (the NLA did the wrong thing, or
didn't do the right thing), the AI drafting the letter should:

- Include the **instruction chain** — which docs were read, what specific guidance led
  to the behavior or inaction
- Use **exact quotes** from the docs, not paraphrases. Quotes are verifiable by the
  receiving maintainer. Paraphrases sound plausible whether accurate or not.
- **Propose documentation changes** when possible — even tentative ones. A letter item
  that says "step 3 could be reworded to handle experienced users" gives the receiving
  maintainer a starting point, not just a problem to investigate.
- **Flag confidence honestly.** If the instruction chain is reconstructed from memory
  rather than traced in the moment, say so. "I believe this was influenced by the
  patterns doc" is honest. A fabricated quote is worse than no quote.

This doesn't change the letter structure or the submission process. It enriches what goes
into letter items about behavioral friction. Structural feedback, process observations,
and positive feedback don't need instruction chains — they're different kinds of signal.

## 3. Risks to Acknowledge

Three risks emerged from the design discussion. They're characteristics to design around,
not blockers:

**Confabulation.** The LLM might construct a plausible but inaccurate explanation of its
own reasoning. Mitigation: exact quotes (checkable) rather than paraphrases (plausible).
The write-letter guidance should emphasize this — a letter with fabricated quotes damages
trust more than a letter without quotes.

**Context window decay.** By the time write-letter runs (typically end of session), early
reasoning may be compressed out of context. Mitigation: friction-log captures observations
close to the moment; write-letter draws from friction-log entries. The two-step pipeline
(friction-log captures, write-letter curates and sends) naturally mitigates this. The
framework's friction-log guidance now emphasizes "capture close to the moment."

**Incomplete proposals.** The LLM has limited context about all the cases a doc serves.
A proposed change that fixes one user's friction might break another user's workflow.
Mitigation: the Cardinal Rule. Proposed changes are starting points for the receiving
maintainer, not auto-patches. The letter should frame them as "consider" not "change to."

## 4. What We've Already Done

The framework's `core/skills/friction-log.md` now has a "Diagnostic richness" section
with guidance about:
- Citing specific docs with exact quotes
- Tracing inaction (what wasn't done and why)
- Proposing documentation changes
- Capturing close to the moment
- The confabulation risk and its mitigation

This is the internal feedback side. Write-letter is the external side — when these
diagnostically rich friction-log entries get curated into a letter for the upstream
developer. The two skills form a pipeline: friction-log captures with richness,
write-letter sends with richness.

## 5. What This Means for Penny Post

This is a quality improvement to write-letter's guidance, not a structural change. A few
lines in the drafting step and judgment calls about leveraging instruction chains and exact
quotes when the feedback involves behavioral friction. The letter format, submission
process, and triage conventions are unchanged.

It's also worth noting in penny post's own docs — perhaps voice-and-values or common
patterns — that NLA feedback has this unique characteristic. Traditional feedback says
"this didn't work." NLA feedback can say "this didn't work because instruction X says Y,
and in this context that led to Z. Here's a proposed change." That's a qualitative
difference worth cultivating across the entire feedback pipeline.

---

*Drafted with /write-letter from [nla-framework](https://github.com/mightytech/nla-framework) during a maintenance session.*
