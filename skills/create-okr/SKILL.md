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
  - assess the OKR draft, revise it toward high quality, and identify any remaining blocker before finalizing
- Ask one or two questions at a time.
- Push back on vague Objectives, generic improvement language, business-as-usual goals, multi-objective OKRs, output-only Key Results, missing baselines, sandbagging, impossible targets, and Key Results that can all succeed without achieving the Objective.
- Prefer one measurable outcome per Key Result. If a draft has grouped themes with multiple sub-metrics, help collapse them into a few crisp Key Results or split them into separate OKRs.
- Key Results should usually include the metric, direction, threshold, and timing inside the sentence.
- Prefer natural metric phrasing such as `increase from 42% to 60% by end of Q3`, `reduce median time below 10 minutes`, `maintain weekly publication for 4 consecutive weeks`, or `at least 80% within 24 hours`.
- Format each Key Result as one copy-pasteable numbered item in the form `1. KR1: {single measurable outcome sentence}.`. Keep the Markdown list number and `KR` number aligned sequentially.
- Do not split a Key Result into a label line and a separate measurement line.
- Do not format the final OKR as a metric-tracking table unless the user asks.
- Do not use separate baseline, target, type, owner, or similar metadata fields in the final OKR unless the user explicitly asks for that format.
- If a baseline is missing, ask for it. If the user still wants a draft, write the Key Result with a clear placeholder inside the sentence, such as `from the baseline confirmed before the cycle starts`.
- Distinguish OKR type when it affects targets:
  - committed OKRs should be realistic enough that full achievement is expected
  - aspirational OKRs should be meaningfully stretching, and 70% progress can still be strong
  - mixed OKRs should make clear which Key Results are committed and which are aspirational
- Assess draft quality separately from end-of-cycle progress. Before finalizing, revise the OKR toward an `A` or equivalently high-quality standard: one focused outcome, measurable Key Results, credible targets, clear timing, and meaningful collective coverage of the Objective.
- Never inflate the grade or invent missing inputs. If unresolved inputs prevent a high-quality result, report the lower grade and main gap honestly in chat, prefix the artifact title with `[DRAFT]`, and use a clear placeholder where needed.
- Before the paste-ready artifact, tell the user the final draft-quality grade in one short conversational sentence and name the main remaining constraint only when one exists. The artifact begins with its title and contains no grade, grading rationale, quality assessment, test verdict, or critique.
- If the user asks to grade end-of-cycle progress, ask for actual results and score progress separately from draft quality.
- If the user wants to fast-track, ask for the draft Objective, draft Key Results, OKR cycle, scope, owner, strategic priority, candidate metrics, known baselines, target dates, constraints, and committed or aspirational status.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` that states the intended outcome and the most consequential measurable change.
- Immediately after the `tl;dr`, write the Objective as one inline sentence in the form `**Objective:** ...`. Do not use separate `Objective` or `Key Results` section headings.
- Place the numbered Key Results directly after the Objective sentence.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Prefix the title with `[DRAFT]` only when unresolved inputs materially prevent a publish-ready OKR.
- Keep the final OKR concise enough to paste into a planning doc without cleanup.
- Never invent metrics, baselines, targets, dates, owners, evidence, business value, customer impact, or stakeholder views.

# Output

A paste-ready OKR containing only a title, concrete `tl;dr`, one inline Objective sentence, and 3-5 numbered, concise, measurable Key Results.
