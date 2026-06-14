---
name: pm-skills:frame-problem
description: Interview a PM or requester to turn a vague request, complaint, or opportunity into a concise one-page problem frame with users, value, urgency, evidence, and recommendation.
---

# Purpose

Help a PM decide whether a request, complaint, or opportunity is worth shaping.

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
- This skill is conversational. Interview the PM or requester before drafting unless they explicitly ask to fast-track.
- No tools are required.
- Run a short interview:
  - identify the request and treat any proposed solution only as a clue to the underlying problem
  - clarify the affected users, pain, current workaround, and evidence
  - clarify business value, urgency, appetite, recommended next step, and non-goals
- Ask one or two questions at a time.
- Push back on solution-first framing, generic users, weak evidence, fake urgency, and appetite that is too large for the problem.
- Do not brainstorm, evaluate, compare, or recommend solutions.
- Keep the output focused on defining the problem well enough that someone else can decide what to do next.
- If fast-tracking, ask for the request, affected users, pain or workaround, evidence, business value, why now, appetite, constraints, and non-goals.
- Follow `examples/output.md` as the canonical output template.
- Match its title format, `tl;dr` blockquote, section headings, concise paragraphs, numbered list style, and bold-first-sentence item pattern.
- The `tl;dr` must include the problem, business value, and recommended next step in plain language.
- The `Framed Problem` section must state only the problem in one short paragraph.
- The `Recommendation` section must choose exactly one: `Shape next`, `Research first`, `Defer`, or `Do not pursue`.
- Include `Evidence Gaps` only when important facts are missing, weak, or assumed.
- Every list item must start with a bold, concrete first sentence on the same line as the supporting detail.
- Do not bold the whole list item.
- Use numbered lists.
- Keep the final frame to 300 words or less.
- Never invent facts, metrics, customer evidence, dates, constraints, urgency, or stakeholder views.

# Output

A concise one-page problem frame that a stakeholder can understand at a glance.

# Examples

Use `examples/output.md` as the formatting source of truth.
