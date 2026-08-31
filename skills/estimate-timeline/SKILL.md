---
name: pm-skills:estimate-timeline
description: Create a launch timeline estimate for project planning, fixed dates, milestones, rollout checkpoints, scope cuts, or date tradeoffs.
---

# Purpose

Help a PM run a short estimation workshop that results in a credible launch-oriented timeline with dated milestones, explicit scope tradeoffs, and a clear MMDD shorthand for the project.

# When to use

- Kicking off a new project
- Turning rough scope into a launch estimate
- Aligning a team on milestones, launch date, and tradeoffs
- Preparing a Linear project or similar planning brief

# Inputs

- Project name and goal
- Rough scope
- Known constraints, dependencies, or deadlines
- Optional launch target
- Optional rollout expectations
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as scope, dependency, or date evidence.
- This skill is conversational. Do not jump straight to the final estimate unless the user explicitly asks to fast-track.
- No tools are required.
- Start by asking whether the team is working backward from a fixed launch date or forward toward choosing one.
- Run a short interview in four phases:
  - clarify the project goal and launch mode
  - separate `Must`, `Should`, and `Could` scope
  - identify milestones, dependencies, and rollout checkpoints
  - pressure-test the plan and confirm the launch date
- Ask one or two questions at a time.
- Treat every estimate as imperfect. Speak in terms of the best current estimate, the main risks, and the likeliest scope cuts.
- Use fixed time, variable scope. Protect the chosen launch date by moving work out of `Must` scope before moving the date.
- Every project needs an MMDD shorthand tied to the launch date. Include it as `Project MMDD: {MMDD} ({Month Day})` in the output, but do not append it to the project title unless the user asks.
- Pair MMDD dates with a human-readable month and day in parentheses in the final output to avoid regional date ambiguity.
- If the team starts from a fixed launch date, work backward to the milestones.
- If the team starts without a fixed launch date, sequence the milestones first, propose a launch date, and ask the user to confirm it before finalizing the output.
- If the user wants to fast-track, ask for the project name, goal, launch mode, rough scope, must-have scope, constraints, dependencies, target date, and rollout expectations.
- Push back on fuzzy scope, missing dependencies, unrealistic sequencing, missing rollout checkpoints, scope cuts that are too vague to act on, and milestones that do not support the launch.
- Distinguish proposed launch dates from committed launch dates. If a date is proposed rather than committed, label it clearly as an estimate and ask for confirmation before final output.
- Prefer concrete milestones the team can aim at, especially dependency deadlines and rollout checkpoints when relevant.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` with the launch estimate, main scope condition, and primary risk.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with sequential numbered section headings: `Estimate Summary`, `Milestones`, and `Risks and Scope Tradeoffs`.
- Use hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Keep confidence language lightweight in the `tl;dr` and risks. Do not add a separate confidence field.
- Use a short paragraph when a section contains one coherent point. When a section needs multiple distinct points, use a numbered list to make the estimate easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Keep the full output to 400 words or less.
- Do not present the estimate as certain.

# Output

A concise estimate summary that includes a launch date, the project MMDD, dated milestones, and the main scope tradeoffs in a format that can be pasted into Linear or a planning doc.
