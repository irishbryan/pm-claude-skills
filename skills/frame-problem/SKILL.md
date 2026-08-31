---
name: pm-skills:frame-problem
description: Interview a PM or requester to turn a vague request, complaint, or opportunity into a concise one-page problem frame with users, impact, evidence, constraints, and non-goals.
---

# Purpose

Help a PM define a request, complaint, or opportunity clearly enough for later solution shaping and prioritization.

# When to use

- Before shaping solutions or prioritizing work
- When a request is solution-first and the underlying problem is unclear
- When a backlog item needs business context before prioritization
- When impact, evidence, or affected users are unclear

# Inputs

- The request, complaint, or opportunity
- Affected user or customer segment
- Triggering situation, current workflow or workaround, and the point where it breaks down
- Evidence or signals
- Business relevance or user impact
- Constraints, risks, and non-goals
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as problem evidence or a replacement for interviewing.
- Treat framing as pre-shaping: define the problem, affected users, impact, evidence, constraints, and non-goals before any solution pitch or prioritization decision.
- This skill is conversational. Interview the PM or requester before drafting unless they explicitly ask to fast-track.
- No tools are required.
- Run a short interview:
  - identify the request and treat any proposed solution only as a clue to the underlying problem
  - clarify the triggering situation, affected users, current workflow or workaround, and the exact point where it breaks down
  - clarify user impact, business relevance, evidence strength, constraints, and non-goals
- Ask one or two questions at a time.
- Push back on solution-first framing, generic users, problem statements that only describe a missing feature, unsupported impact claims, and weak evidence.
- Do not brainstorm, evaluate, compare, or recommend solutions. Translate proposed solutions into the underlying problem, current workaround, constraint, or non-goal.
- Stop at the problem frame. Leave solution shaping, prioritization, appetite, and next-step decisions outside the artifact.
- If fast-tracking, ask for the request, triggering situation, affected users, current workflow or workaround, exact breakdown, evidence, business relevance or user impact, constraints, and non-goals.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` that names the problem, affected users, and impact without recommending what to do next.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with sequential numbered section headings: `Problem`, `Users and Impact`, `Evidence`, and `Constraints and Non-goals`.
- The `Problem` section must describe the triggering situation, current baseline, and exact workflow breakdown in one short paragraph. Frame the breakdown rather than merely naming a missing feature.
- The `Users and Impact` section must name affected users, user impact or operational cost, and known business relevance. If the business connection is not known, say so without manufacturing urgency.
- The `Evidence` section must distinguish known signals from material gaps or uncertainty. Keep evidence gaps within this section rather than creating a separate unnumbered label.
- The `Constraints and Non-goals` section must define boundaries for later shaping without proposing a solution.
- Use hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Use a short paragraph when a section contains one coherent point. When a section needs multiple distinct points, use a numbered list to make the frame easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Keep the final frame to 300 words or less.
- Never invent facts, metrics, customer evidence, dates, constraints, or stakeholder views.

# Output

A concise one-page problem frame that a stakeholder can understand at a glance and use in later solution shaping and prioritization.
