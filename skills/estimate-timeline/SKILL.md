---
name: pm-skills:estimate-timeline
description: Help a team create a timeline estimate with a launch date, dated milestones, and variable scope.
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
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context only.
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
- Follow `examples/output.md` as the canonical output template.
- Match its title format, `tl;dr` blockquote, section headings, bullet style, milestone pattern, and bold-first-sentence item pattern.
- Preserve these output sections:
  - `Estimate Summary`
  - `Milestones`
  - `Risks and Scope Tradeoffs`
- Keep confidence language lightweight in the `tl;dr` and risks. Do not add a separate confidence field.
- Start each bullet with a bold, concrete first sentence on the same line as the supporting detail.
- Keep the full output to 400 words or less.
- Do not present the estimate as certain.

# Output

A concise estimate summary that includes a launch date, the project MMDD, dated milestones, and the main scope tradeoffs in a format that can be pasted into Linear or a planning doc.

# Examples

Use `examples/output.md` as the formatting source of truth.
