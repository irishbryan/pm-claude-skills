---
name: pm-skills:create-strategy-canvas
description: Create an evidence-backed Blue Ocean Strategy-style strategy canvas with competitor discovery, cited comparator dossiers, 1-5 value-curve scoring, crisp visual charts when supported, plotted ASCII fallback when not, and eliminate-reduce-raise-create actions. Use when a PM, founder, strategist, or team lead wants to compare an offering with competitors, substitutes, or the status quo and shape a differentiated future strategy.
---

# Purpose

Create a paste-ready, visually clear strategy canvas showing the current offering, intended future curve, relevant buyer alternatives, and the actions required to create meaningful strategic divergence.

# Inputs

- Market, category, or strategic arena
- Target buyer or noncustomer segment and the job they need done
- Offering being assessed and the decision the canvas should inform
- Candidate competitors, substitutes, status quo, or internal alternatives
- Competitive factors, usually 6-10
- Evidence, customer signals, assumptions, and research behind relative scores
- Optional local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Workflow

- Use local context only for defaults such as role, team, company, product area, and timezone. Never treat it as market evidence.
- Keep the process conversational unless the user asks to fast-track. Ask one or two questions at a time.
- Use the 1-5 scale consistently: `1` means a very low offering level and `5` means a very high offering level. Do not imply that a high score is inherently desirable.
- Work through these phases:
  1. Clarify the arena, target buyer, buyer job, offering, and decision context.
  2. Build the comparator set from direct competitors, substitutes, status quo, manual work, internal build, services, and low- or high-end alternatives.
  3. Identify the factors on which the current market competes and invests.
  4. Research and analyze comparators before assigning scores.
  5. Rank offerings factor by factor, then derive relative 1-5 scores and confidence.
  6. Define and pressure-test a future curve that creates a coherent value leap.
  7. Translate the intended shift into eliminate-reduce-raise-create moves.
- Push back when the comparator set is too narrow, only contains weak direct competitors, or does not reflect real buyer choices.
- Push back when the future curve raises every factor, copies another curve, ignores cost or complexity, lacks a specific buyer, or has no meaningful create move.

# Competitor research

- Research current public claims when browsing is available. Prefer first-party product, pricing, documentation, and policy pages; use credible independent sources when they add necessary buyer or market context.
- Attribute vendor claims, cite factual competitor claims near the claim, include the research date or source date, and separate observations from inference and strategic hypotheses.
- Compare the same target buyer, use case, geography, plan level, and time period across alternatives. Do not treat absence from public documentation as proof that a capability does not exist.
- If research tools are unavailable, use user-supplied evidence and mark unsupported claims and scores as provisional. Never invent evidence.
- Recommend 2-5 primary comparators for interpretation, but honor the requested set. Document relevant but unplotted alternatives and explain which plotted comparator represents them.
- Give each plotted comparator a compact dossier with buyer relevance, category, inclusion reason, defining strengths and weaknesses, pivotal score rationales, evidence freshness, and confidence.

# Factors and scoring

- Prefer 6-10 buyer-facing factors. Ask the user to reduce a longer list unless retaining it is important to the decision.
- Include price only when it shapes the buying decision. Include substitutes when the goal is to find a value leap rather than win a feature checklist.
- Before scoring, ask which offering is strongest and weakest on each factor and why. Derive scores from the relative ranking.
- Capture score confidence as `High`, `Medium`, or `Low`. Treat provisional rankings, stale sources, and indirect evidence as `Low` confidence.
- Add rationale only for pivotal, surprising, or weakly supported scores. Do not fabricate precision by explaining every cell.
- Require the future curve to include at least one meaningful reduction or elimination and at least one raised or created source of buyer value.

# Visual delivery

- Prefer high-fidelity visual charts whenever they can be created and displayed accurately. Return the score table with a current-market chart and a separate current-versus-future chart.
- Use titled ASCII value-curve panels only when reliable visual output is unavailable. Use one solid curve per panel, stack current-market panels vertically, and place the separately titled current and future panels side by side when width permits.
- For visual charts, use crisp text, a consistent 1-5 scale, restrained gridlines, a colorblind-safe palette, and lines that remain distinguishable without color. Plot no more than four comparators with the current offering in one panel; split larger sets into consistent panels.
- Keep every plotted score and label consistent with the score table. Use image-generation tools only when their output can preserve exact chart text and values; otherwise use deterministic charting or ASCII.
- Do not require a fixed file type, output directory, companion document, or bundle of artifacts unless the user asks for files.
- Do not return both visual and ASCII charts unless the user asks for both or the response is explicitly demonstrating the available formats.
- Do not substitute rating bars, coded marker legends, dotted-line semantics, or an unreadable multi-series ASCII overlay for a plotted value curve.

# Interpretation and action

- Explain 2-4 important curve observations covering strategic divergence, buyer value, cost or complexity tradeoffs, and comparator contrast.
- Use eliminate-reduce-raise-create as the bridge from chart to action:
  - `Eliminate`: remove factors the market invests in without enough buyer value.
  - `Reduce`: offer selected factors below the current standard.
  - `Raise`: offer selected factors above the current standard.
  - `Create`: introduce buyer value the current market does not meaningfully offer.
- Include open questions only when they materially affect factor selection, scoring, evidence quality, or confidence in the strategic direction.

# Output

Return a concise strategy package containing:

1. Title and `tl;dr`
2. Competitive-factor definitions
3. Comparator selection and exclusion notes
4. Compact competitor dossiers with citations and confidence
5. Score table and pivotal score notes
6. Current-market and current-versus-future visuals, or ASCII fallback
7. Curve interpretation
8. ERRC moves
9. Material evidence gaps and open questions

Use [examples/output.md](examples/output.md) as the canonical document structure. Keep the example and language vendor-neutral and suitable for an open-source repository.
