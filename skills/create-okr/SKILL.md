---
name: pm-skills:create-okr
description: Interview a PM, team lead, founder, manager, or individual to create, improve, grade, and target-set OKRs with clear objectives, measurable key results, baselines, committed vs aspirational expectations, and paste-ready output.
---

# Purpose

Help a person turn fuzzy goals, draft OKRs, or broad initiatives into a clear Objective and 3-5 concrete Key Results.

# When to use

- Creating a new OKR for a team, product area, project, company, or individual
- Improving a draft OKR that feels vague, too broad, too activity-based, or hard to measure
- Grading the quality of a proposed OKR before publishing it
- Setting credible targets when baselines, ambition, or measurement details are unclear

# Inputs

- The intended OKR scope, owner, audience, and cycle
- Strategic priority, customer or business outcome, and why this matters now
- Draft Objective and Key Results, if any
- Candidate metrics, baselines, current run rate, constraints, and desired stretch
- Whether the OKR is committed, aspirational, or mixed
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as OKR evidence, strategy, or metric context.
- This skill is conversational. Do not jump straight to a finished OKR unless the user explicitly asks to fast-track.
- No tools are required.
- Run a short interview in five phases:
  - clarify the scope, cycle, owner, audience, strategic priority, and whether the OKR is committed or aspirational
  - shape the Objective into one concrete, meaningful, outcome-oriented sentence
  - draft 3-5 Key Results as concise measurable outcomes, not project tasks
  - ask for baselines, current run rate, constraints, and desired stretch only when needed to set credible targets
  - grade the OKR draft and propose revisions before finalizing
- Ask one or two questions at a time.
- Push back on vague Objectives, generic improvement language, business-as-usual goals, multi-objective OKRs, output-only Key Results, missing baselines, sandbagging, impossible targets, and Key Results that can all succeed without achieving the Objective.
- Prefer one measurable outcome per Key Result. If a draft has grouped themes with multiple sub-metrics, help collapse them into a few crisp Key Results or split them into separate OKRs.
- Key Results should usually include the metric, direction, threshold, and timing inside the sentence.
- Prefer natural metric phrasing such as `increase from 42% to 60% by end of Q3`, `reduce median time below 10 minutes`, `maintain weekly publication for 4 consecutive weeks`, or `at least 80% within 24 hours`.
- Format each Key Result as one copy-pasteable line: `KR1: {single measurable outcome statement}`.
- Do not split a Key Result into a label line and a separate measurement line. Avoid standalone labels like `KR1: Activation`.
- Do not format the final OKR as a metric-tracking table unless the user asks.
- Do not use separate baseline, target, type, owner, or similar metadata fields in the final OKR unless the user explicitly asks for that format.
- If a baseline is missing, ask for it. If the user still wants a draft, write the Key Result with a clear placeholder inside the sentence, such as `from the baseline confirmed before the cycle starts`.
- Distinguish OKR type when it affects targets:
  - committed OKRs should be realistic enough that full achievement is expected
  - aspirational OKRs should be meaningfully stretching, and 70% progress can still be strong
  - mixed OKRs should make clear which Key Results are committed and which are aspirational
- When grading, grade draft quality separately from end-of-cycle progress. Use either a letter grade or 0.0-1.0 score and explain the largest constraint on the grade.
- If the user asks to grade end-of-cycle progress, ask for actual results and score progress separately from draft quality.
- If the user wants to fast-track, ask for the draft Objective, draft Key Results, OKR cycle, scope, owner, strategic priority, candidate metrics, known baselines, target dates, constraints, and committed or aspirational status.
- Follow `examples/output.md` as the canonical output template.
- Match its title format, Objective line, one-line `KR1: ...` pattern, grade line, revision list, open question list, and compact paste-ready style.
- Keep the final OKR concise enough to paste into a planning doc without cleanup.
- Include `Revisions` only when there are concrete changes, caveats, or target-setting notes the user should handle before publishing.
- Include `Open questions` only when unanswered questions materially affect the OKR quality or target credibility.
- Never invent metrics, baselines, targets, dates, owners, evidence, business value, customer impact, or stakeholder views.

# Output

A paste-ready OKR with one Objective, 3-5 Key Results, a brief quality grade, and only the revisions or open questions needed before publishing.

# Examples

Use `examples/output.md` as the formatting source of truth.
