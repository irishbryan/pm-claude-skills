---
name: pm-skills:create-strategy-canvas
description: Create a Blue Ocean Strategy-style strategy canvas with competitive factors, competitor discovery, factor-by-factor competitor analysis, 1-5 value-curve scoring, readable ASCII charts, and eliminate-reduce-raise-create actions. Use when a PM, founder, strategist, or team lead wants to identify relevant competitors or substitutes, rank them against an offering, and shape a differentiated future strategy.
---

# Purpose

Help a PM, founder, strategist, or team lead create a paste-ready strategy canvas that shows where the offering is now, where it should go next, how selected competitors or alternatives compare, and what actions create a clearer strategic shift.

# When to use

- Comparing an offering against competitors, substitutes, or the current market norm
- Identifying the competitors or alternatives that should be plotted before scoring
- Evaluating multiple competitors or alternatives against the same buyer value factors
- Looking for a differentiated strategy instead of incremental feature competition
- Turning competitive analysis into a visual value curve
- Identifying what to eliminate, reduce, raise, or create in a product, service, or business model
- Preparing strategy workshop notes, planning docs, product pitches, or leadership discussion material

# Inputs

- Market, category, or strategic arena
- Target buyer, user, customer, or noncustomer segment
- Offering being assessed
- Competitors, substitutes, alternatives, or current market norms to compare
- Why each competitor or alternative is relevant to the target buyer
- Competitive factors buyers care about, usually 6-10 factors
- Relative scores from 1-5 for current offering, desired future offering, and each selected competitor or alternative
- Evidence, assumptions, customer signals, or research behind scores
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as market evidence or strategy.
- This skill is conversational. Do not jump straight to a finished canvas unless the user explicitly asks to fast-track.
- No tools are required.
- Treat the strategy canvas as a diagnostic and action framework: competitive factors define the basis of comparison, relative scores show each offering's value curve, and the output should make strategic contrast easy to see.
- Use a 1-5 score scale where `1` means very low buyer offering level and `5` means very high buyer offering level. A high score is not automatically good if the factor adds cost without meaningful buyer value.
- Run a short interview in seven phases:
  - clarify the market, target buyer, buyer job, offering, and decision context
  - identify the competitor set, including direct competitors, substitutes, status quo, internal build or manual process, service-led alternatives, and low-end or high-end alternatives when relevant
  - identify the factors the current market competes on and invests in
  - analyze competitors factor-by-factor before plotting scores
  - collect or draft relative 1-5 scores for current offering, future offering, and each selected competitor or alternative
  - define the intended future curve and pressure-test whether it meaningfully diverges
  - translate the curve shift into eliminate-reduce-raise-create moves
- Ask one or two questions at a time.
- Ask which competitors, substitutes, alternatives, or market norms to include. If the user gives many, recommend 2-5 for readability, but honor the user's chosen number.
- If the user does not know which competitors to include, help build the set by asking:
  - what buyers use today instead
  - what they would do manually if no product existed
  - which tools, services, spreadsheets, internal systems, or agencies absorb the budget or attention
  - which premium, low-cost, and good-enough alternatives shape expectations
- For each proposed competitor or alternative, ask why it belongs in the comparison and whether it reflects a real buyer choice.
- If the user is missing factors, propose a draft factor list and ask them to confirm or edit it.
- Before assigning scores, ask which offering is strongest and weakest on each factor and why. Use that ranking to derive 1-5 scores.
- When scores are missing and the user wants momentum, create provisional scores clearly labeled as assumptions.
- Capture score confidence as `High`, `Medium`, or `Low` when the user provides enough signal. Use `Low` for provisional rankings or weak evidence.
- Push back when competitor choices are too narrow, omit substitutes, only include weak competitors, or do not match the target buyer's real alternatives.
- Push back when the future curve only raises every factor, imitates a competitor, lacks a buyer segment, ignores cost structure, or has no create move.
- Prefer 6-10 factors. Fewer than 5 usually hides the strategy; more than 10 usually makes the canvas too noisy for a working doc.
- Include price as a factor when price is central to the market, but do not force it into every canvas.
- Include substitutes or alternatives, not only direct competitors, when the user is trying to find a blue ocean move.
- The future curve should usually show at least one meaningful reduction or elimination and at least one raised or created factor.
- Use eliminate-reduce-raise-create as the action bridge:
  - `Eliminate`: factors the industry competes on that should be removed
  - `Reduce`: factors to offer below the current standard
  - `Raise`: factors to offer above the current standard
  - `Create`: new factors the industry has not meaningfully offered
- Follow `examples/output.md` as the canonical output template.
- Match its title format, `tl;dr` blockquote, factor table, competitor analysis table, score table, separate monospaced ASCII charts, ERRC table, and compact open questions.
- Include `## Competitor Analysis` before the score table. Use columns for comparator, buyer alternative, why included, and score confidence.
- The score table must appear before the ASCII charts and must include factor IDs, factor names, current offering score, future offering score, and one column for each selected competitor or alternative.
- Add short score notes only when they explain important rankings, weak evidence, or surprising differences. Do not explain every cell.
- Do not default to an overlaid multi-series ASCII chart. Separate charts are easier to read and paste into docs.
- Include one ASCII chart for `Where We Are Now`, one for `Where We Want To Be`, and one chart for each selected competitor or alternative.
- Each ASCII chart must be inside a fenced code block and use horizontal score bars with this pattern: `F1 Short label  3/5 |###..|`.
- Use `#` for filled score units and `.` for empty units. Each bar must be exactly five characters long.
- Keep chart labels short. Use factor IDs plus shortened factor names in charts, and rely on the factor table for full descriptions.
- If there are more than five competitors or alternatives, keep every requested competitor chart but make the interpretation concise.
- Include `## What The Curves Show` with 2-4 numbered observations about strategic divergence, cost or complexity tradeoffs, and buyer value.
- Include at least one observation about competitor contrast when competitors are provided.
- Include `## ERRC Moves` with a Markdown table using exactly these columns: `Eliminate`, `Reduce`, `Raise`, `Create`.
- Include `## Open Questions` only when unanswered questions materially affect factor selection, scoring, evidence quality, or strategic confidence.
- Keep the final output concise enough to paste into a working strategy doc.
- Never invent evidence, customer behavior, competitor facts, financial impact, market data, dates, stakeholder views, or research confidence.

# Output

A paste-ready strategy canvas with competitive factors, selected competitor evaluation, score table, separate readable ASCII charts, interpretation, ERRC moves, and only the open questions needed to improve confidence.

# Examples

Use `examples/output.md` as the formatting source of truth.
