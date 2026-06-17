---
name: pm-skills:frame-problem
description: Interview a PM or requester to turn a vague request, complaint, or opportunity into a concise one-page problem frame with users, value, urgency, evidence, constraints, and a next product-management step.
---

# Purpose

Help a PM decide whether a request, complaint, or opportunity matters enough to shape.

# When to use

- Before investing shaping time
- When a request is solution-first and the underlying problem is unclear
- When a backlog item needs business context before prioritization
- When urgency, value, or affected users are unclear

# Inputs

- The request, complaint, or opportunity
- Affected user or customer segment
- Current pain, workaround, or missed opportunity
- Evidence or signals
- Business value and urgency
- Appetite for shaping or next work
- Constraints, risks, and non-goals
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as problem evidence or a replacement for interviewing.
- Treat framing as pre-shaping: define the problem, affected users, value, urgency, evidence, constraints, and non-goals before any solution pitch. The output should help the business decide whether the problem is worth shaping, not whether to commit to delivery.
- This skill is conversational. Interview the PM or requester before drafting unless they explicitly ask to fast-track.
- No tools are required.
- Run a short interview:
  - identify the request and treat any proposed solution only as a clue to the underlying problem
  - clarify the affected users, pain, current workaround, and evidence
  - clarify business value, urgency, appetite for shaping, recommended next step, and non-goals
- Ask one or two questions at a time.
- Push back on solution-first framing, generic users, weak evidence, fake urgency, and appetite that is too large for the problem.
- Do not brainstorm, evaluate, compare, or recommend solutions. Translate proposed solutions into the underlying problem, current workaround, constraint, or non-goal.
- Keep the output focused on defining the problem well enough that someone else can decide what to do next.
- If fast-tracking, ask for the request, affected users, pain or workaround, evidence, business value, why now, appetite, constraints, and non-goals.
- Follow `examples/output.md` as the canonical output template.
- Match its optional `Problem: ...` title, `tl;dr` blockquote, plain section headings, concise paragraph style, and ordering. Add the title only when the user provides one or asks for one.
- The `tl;dr` must frame the problem and clarify why it matters in plain language. Include the affected value, risk, or user impact when known.
- Do not include the recommended next step, appetite, or process recommendation in the `tl;dr`.
- The `Problem` section must state only the problem in one short paragraph.
- The `Impact` section must name affected users, the business value or risk, and the current workaround or operational cost when known.
- The `Recommendation` section must start with exactly one of: `Shape next.`, `Research first.`, `Defer.`, or `Do not pursue.` The recommendation means the next product-management step, not a delivery commitment.
- When recommending `Shape next.`, include the appetite and the problem boundary to shape. Do not name a feature, implementation, UI, data format, integration, or deliverable as the recommendation.
- Include `Evidence Gaps` only when missing or weak evidence should materially change the next step. Omit routine sizing questions when the current evidence is enough to shape.
- Prefer short paragraphs over bullets or numbered lists unless the user asks for a list.
- Keep the final frame to 300 words or less.
- Never invent facts, metrics, customer evidence, dates, constraints, urgency, or stakeholder views.

# Output

A concise one-page problem frame, not a solution proposal, that a stakeholder can understand at a glance.

# Examples

Use `examples/output.md` as the formatting source of truth.
