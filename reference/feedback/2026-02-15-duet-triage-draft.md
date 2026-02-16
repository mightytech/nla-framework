# Draft Triage: Duet Feedback Letter

**Date:** 2026-02-15
**Source letter:** `2026-02-14-duet-maintenance-learnings.md`
**Context:** Informal triage during the feedback channel design session, before the penny post existed. Revised after reading three whitepapers (Collaborative AI Writing Platform, Medical Intake System, Policy Platform) that validated several patterns as general.

**Purpose:** Baseline for comparison with the formal penny post triage. This triage was ad-hoc — done in conversation without the structured process the penny post defines. Comparing the two will help evaluate whether the penny post's process produces different or better results.

---

## Verdicts

### 1. Artifact Persistence
**Verdict: Accept**
**Where:** `nla-foundations.md`
**Rationale:** Stateless vs. persistent is a fundamental axis. All three whitepapers are persistent. The framework should name the axis at the foundations level.

### 2. Session Bridge / Context File Pattern
**Verdict: Accept (concept + principles, not template)**
**Where:** Within the persistence section of `nla-foundations.md`
**Rationale:** The principles (distill don't transcribe, rejected section is valuable) are genuinely general. Accept as guidance within the persistence section, not as a standalone template.

### 3. Lifecycle Skill Template
**Verdict: Accept (concept, no template)** — changed from Defer after whitepapers
**Where:** Within the persistence section of `nla-foundations.md`
**Rationale:** Initially deferred as one data point. Writing Platform has timeline/versions/rollback, Policy Platform has iterative refinement with sandboxing. The pattern is clearly general. Still no template, but a stronger discussion than a mere mention.

### 4. Startup Skill Extensibility
**Verdict: Accept**
**Where:** `core/skills/startup.md` + guidance
**Rationale:** The startup wrapper is the one wrapper that's expected to be "thick." The framework startup provides the universal sequence; the domain wrapper adds to it rather than just delegating. Bless this pattern explicitly.

### 5. Environment Management for External Tools
**Verdict: Accept (concept)** — changed from Defer after whitepapers
**Where:** `nla-foundations.md`
**Rationale:** Initially deferred as one data point. Medical Intake integrates with records systems, Policy Platform needs data feeds. The concept is broader than Duet's CLI-tool framing — it's "external system integration." Worth naming as a pattern.

### 6. Tool-Specific Output Specs
**Verdict: Accept**
**Where:** `/create-app`
**Rationale:** Low cost addition: just ask "might your NLA support multiple output tools?" and name output specs accordingly. Reinforced by all three whitepapers producing multiple output types.

### 7. AI Executing Its Own Output (Auto-Play)
**Verdict: Accept**
**Where:** `nla-foundations.md`
**Rationale:** A distinctive NLA capability — the runtime that generates the artifact can also execute it. Worth naming. Safety framing matters: user consent, config toggle, execution supplements conversation.

### 8. /create-app Deeper Questions
**Verdict: Accept (follows from 1, 5, 6, 7)**
**Where:** `/create-app`
**Rationale:** Once persistence, external systems, output specs, and auto-play are accepted into the framework, /create-app should ask about them during project setup.

### 9. Structured NLA-to-Framework Feedback Channel
**Verdict: Accept**
**Where:** `/maintain` skills (both framework and domain)
**Rationale:** The penny post design session itself is the implementation of this item.

### 10. Natural Language Config
**Verdict: Adapt (brief addition)**
**Where:** `nla-foundations.md`
**Rationale:** The insight ("enums are defaults, prose is the real interface, the LLM IS the extension system") is good but already implicit in the design rationale. Add a brief mention to foundations (config-as-prose as a principle) without duplicating what's in the rationale.

### 11a. Cardinal Rule Broadening
**Verdict: Accept**
**Where:** `nla-foundations.md`
**Rationale:** "The human must always understand what changed and why, and be able to undo it" covers both transformation and creation. The current framing is a special case of this broader principle.

### 11b. Startup Leak
**Verdict: Accept (fix)**
**Where:** `core/skills/startup.md`
**Rationale:** `/format-article` reference in the framework startup is just a bug. Mechanical fix.

### 11c. Scaffold Shapes Expectations
**Verdict: Defer (with increased urgency)** — urgency raised after whitepapers
**Where:** Future project
**Rationale:** None of the three whitepapers look anything like an article formatter. The gap between scaffold and reality is wider than first thought. But the fix (second scaffold or explicit guidance) is a project, not a line item.

### 11d. Validate Assumes Deterministic
**Verdict: Accept**
**Where:** `core/skills/validate.md`
**Rationale:** Process-focused validation guidance for non-deterministic NLAs fills a real gap.

---

## Summary

| Verdict | Count | Items |
|---------|-------|-------|
| Accept | 10 | 1, 2, 4, 6, 7, 8, 9, 11a, 11b, 11d |
| Accept (changed from Defer) | 2 | 3, 5 |
| Adapt | 1 | 10 |
| Defer | 1 | 11c |

The whitepapers shifted items 3 (lifecycle) and 5 (environment) from defer to accept, and raised urgency on 11c (scaffold shapes expectations).

---

*This is a pre-penny-post triage — done informally in conversation. It serves as a comparison baseline for the formal triage through the penny post's process.*
