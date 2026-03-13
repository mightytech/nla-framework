# Contributing

This project works differently from most open source. Understanding why will make
your contributions more effective — and might change how you think about contributing
to software generally.

---

## Why This Project Doesn't Accept Pull Requests

In a traditional codebase, a pull request shows the maintainer a proposed change.
The reviewer reads the diff, evaluates whether the code works, and merges or declines.
The change speaks for itself — in theory.

In an NLA, the prose *is* the application. A prose change isn't a code fix — it's a
change to how the application thinks, reasons, and behaves. Evaluating that change
requires understanding not just *what* you changed but *why* — what you observed,
what you were trying to do, what friction you encountered, and what you think should
be different. A diff can't carry that. Your reasoning can.

If you do open a pull request, we'll read it — but we'll ask you to resubmit as an
issue with the reasoning behind your change. The diff tells us what you'd change; we
need to understand what you observed and why.

This project needs your thinking more than your edits. What you noticed is more
valuable than what you'd change. The observation and the reasoning behind it give
the project information that a proposed edit never could.

---

## How to Contribute

### What makes a good contribution

You observe something. A friction point, a missing capability, an idea, a
disagreement with a design choice, a place where the instructions led you somewhere
unexpected.

The easiest path: just talk to the AI about it. The `/friction-log` and
`/write-letter` skills do the heavy lifting. You describe what happened,
the AI asks clarifying questions, and the skill produces structured feedback with
your observations, reasoning, and recommendations in plain English. Your job is to
notice something and have a conversation about it. The skill handles the rest.

You can also write feedback by hand — as a GitHub issue, a letter, or any format
that captures what you noticed and why it matters. The structured templates are
helpful but not required. What matters is the thinking, not the format.

**More useful:** "I was building a scheduling tool and the update skill's rollback
instructions confused me — I expected it to preserve my custom config but it
overwrote it. Here's what I was trying to do and what happened instead."

**Less useful:** "The update skill should be rewritten to handle custom configs
better."

The first gives the project something to work with. The second might be right, but
without the observation behind it, there's no way to evaluate whether the proposed
solution matches the actual problem.

Context about yourself helps too — your domain, your use case, your level of
experience. What looks like a bug to a newcomer might be working as intended for a
different audience. What looks obvious to an expert might be a genuine gap. Either
way, the context helps the project evaluate the feedback accurately.

Framework changes have blast radius. A change to `core/` affects every NLA built on
this framework. A change to `install/` affects how new projects are generated. When
you share what you noticed, the context of which layer it affects helps the maintainer
evaluate it accurately.

### Where to send it

**GitHub Issues** are the simplest path. Whether you used the friction log skill,
the write-letter skill, or wrote feedback by hand — open an issue with your
observations. This works well for focused feedback on a specific skill, behavior,
or design choice.

**Structured letters** (via `/write-letter`) are the richer path, especially for
substantial feedback that spans multiple observations. A letter submitted as a
GitHub Issue gets triaged by the project's AI — each item evaluated against the
project's values, goals, and design philosophy, with a proposed verdict (accept,
adapt, defer, or decline) and reasoning for each. The maintainer reviews the
verdicts and decides.

### Simulating the evaluation first

This is optional but encouraged, especially for substantial contributions.

Fork this project. Submit your feedback as an issue on your fork. The fork's AI will
evaluate your feedback against the project's full context — values, design rationale,
existing skill files, everything — and show you how it would triage each item.

This lets you see the project's perspective before you contact the maintainer. You
might discover your recommendation conflicts with a design decision you weren't aware
of. You might find a stronger way to frame your observation. You might realize the
project already handles what you're describing and the real issue is discoverability,
not functionality.

**A note on the simulation:** The simulated evaluation is informative, not
authoritative. Different model versions may reason differently. The same model may
reason differently on a second pass — non-determinism is a property of the medium,
not a flaw. And the human maintainer brings judgment, context, and priorities that no
simulation fully captures. A simulated "accept" doesn't guarantee acceptance. A
simulated "decline" doesn't mean your idea lacks merit. The simulation helps you
understand the project's perspective. The maintainer makes the final call.

### If you disagree with an evaluation

Good. Reasoned pushback is welcome — it's one of the most valuable forms of
contribution.

If your letter was evaluated and you think the verdict was wrong, you're encouraged
to appeal. Include your original letter, the triage results (whether from your
fork simulation or the maintainer's evaluation), and your reasoning for why the
evaluation should come out differently.

Maybe the AI missed context. Maybe the project's values should be reconsidered for
this case. Maybe the design rationale doesn't account for your use case. All of
these are legitimate grounds for appeal — and all of them, if you're right, improve
the project's governance, not just its content.

The appeal itself becomes useful data. If the evaluation process is consistently
missing something, that's friction worth capturing. Your pushback might improve how
the project evaluates all future contributions.

---

## What Happens After You Contribute

Your feedback is evaluated transparently — you can see the reasoning at every step.

If accepted: the maintainer and AI implement the change together, in the project's
voice, consistent with its architecture and values. The implementation may differ
from what you proposed, because the maintainer has context about how the change
interacts with everything else in the project. The reasoning for any differences is
preserved in the project's development history.

Your contribution may be credited more deeply than you're used to in open source.
This project maintains detailed development history — feedback logs, session logs,
friction logs, and sometimes design rationale. If your observation led to a change,
that reasoning chain is preserved. Six months later, when someone asks why a skill
works the way it does, the answer may trace back through your observation. You're
part of that reasoning chain. Since contributions come through public GitHub Issues,
this development history is visible at the same level as the contributions themselves.

If declined: the reasoning is visible. You'll understand why, and you'll learn
something about the project's design philosophy that might inform your next
contribution — or your own projects.

If deferred: the idea has merit but the timing, priority, or dependencies aren't
right yet. It stays in the project's awareness for when conditions change.

---

## For Developers Coming from Traditional Open Source

This process might feel unusual. You're used to showing your work as code. Here,
showing your work means showing your thinking.

The shift from "here's my fix" to "here's what I noticed and why I think it matters"
might feel less concrete. It's actually more useful. It gives the project information
a diff can't carry — the context of what you were doing, what you expected, and why
the gap between expectation and reality matters.

If you're curious about why this project works this way, the
[probe report](https://github.com/mightytech/nla-office-hours/blob/main/content/the-documentation-is-the-application.md) explains the paradigm.
The short version: when documentation is the application, contributions need to carry
intent, not just changes.

---

## For Non-Developers

You don't need technical knowledge to contribute valuably. Some of the most useful
contributions come from people with domain expertise and fresh perspectives.

If you're a teacher who tried using this for curriculum development and found the
instructions confusing — that's a contribution. If you're a policy analyst who
noticed the values document doesn't account for something important — that's a
contribution. If you're a first-time user who couldn't figure out where to start —
that's a contribution.

Your experience of the system, described honestly and specifically, is exactly the
kind of feedback that makes NLAs better. You don't need to know how to fix what you
found. You just need to describe what happened and what you expected instead.

---

## Language

Contributions in any language are welcome. This project's AI can read and evaluate
feedback in any major language. If you think more clearly in Spanish, Portuguese,
Japanese, Arabic, or any other language — write in that language. Your best thinking
matters more than writing in English.

---

## Values

This project's contribution process reflects its values:

- **Transparency.** The evaluation criteria are readable. The reasoning is visible.
  The process is inspectable at every step.
- **The human decides.** AI evaluates and proposes. Humans — both the maintainer and
  the contributor — exercise judgment. The AI serves the conversation. It doesn't
  govern it.
- **Authority follows accountability.** The maintainer bears responsibility for the
  project's coherence and direction. Contributors bear responsibility for the quality
  of their observations and reasoning. Each has authority where they have
  accountability.
- **Observations from diverse contexts are the most valuable input.** Different
  domains, different experience levels, different languages, different ways of
  thinking — each reveals something about the project that the maintainer can't see
  alone.

---

*The best contributions aren't the ones that propose the cleverest changes — they're
the ones that share what the project couldn't see from where it was standing.*
