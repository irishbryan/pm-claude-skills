# Visual Output

Use this guide to choose and format the clearest chart the agent can reliably deliver.

## Choose one delivery path

- **Visual charts:** When the agent can create and display accurate, readable charts, return the score table with a current-market chart and a separate current-versus-future chart.
- **ASCII charts:** When the agent cannot create or display visual charts reliably, return the score table with the titled ASCII panels below.

Use one path in a real response unless the user asks for both. The canonical example shows both only to teach the two capability variants. Do not require a fixed file format, output directory, companion Markdown file, or artifact bundle.

## Optional deterministic renderer

When Python 3 and a writable workspace are available, `scripts/render_strategy_canvas.py` can create exact SVG charts from structured data:

```text
python3 <skill-directory>/scripts/render_strategy_canvas.py \
  --input <canvas-data.json> \
  --output-dir <output-directory> \
  --basename strategy-canvas \
  --png auto
```

Add `--ascii` when using the renderer for the fallback. The renderer is optional; use any supported method that can preserve the score table's exact labels and values.

## JSON schema

```json
{
  "title": "Strategy Canvas for a Generic Offering",
  "subtitle": "Optional target buyer or decision context",
  "hypothesis_note": "Scores are strategic hypotheses; sources are documented in the report.",
  "factors": [
    {"id": "F1", "label": "Full factor name", "short_label": "Chart label"}
  ],
  "series": [
    {"id": "current", "label": "Current offering", "role": "current", "scores": [3]},
    {"id": "future", "label": "Future offering", "role": "future", "scores": [5]},
    {"id": "alternative", "label": "Alternative", "role": "comparator", "scores": [2]}
  ]
}
```

Require at least two factors, exactly one `current` series, exactly one `future` series, unique IDs, nonempty labels, and one integer score from 1-5 per factor. Keep `short_label` concise enough to wrap into at most three short lines.

## Visual specification

- Prefer vector or other high-resolution output so chart text stays crisp when scaled.
- Use a clear landscape chart with a title, optional subtitle, legend above the plot, restrained horizontal gridlines, factor labels below the plot, and a hypothesis footer.
- Use a neutral, colorblind-safe palette. Distinguish series with line patterns and marker shapes as well as color.
- Use common system fonts. Do not bundle or assume a company font.
- Plot the current offering and no more than four comparators in one market panel. Repeat the current offering when additional comparator panels are required.
- Create the current-versus-future chart separately. Add a vertical arrow and `from → to` label where a factor changes.
- Include descriptive alt text or equivalent accessible labeling when the output format supports it.
- Do not place citations, paragraphs, logos, decorative images, or company branding inside a chart.
- Use image-generation tools only when exact chart text, scores, and curve positions can be preserved. Otherwise use deterministic charting or ASCII.

## Quality bar

- Every point must match the score table.
- Titles, legends, labels, ticks, and annotations must be readable and unclipped.
- Curves must remain distinguishable without relying on color alone.
- If the visual path cannot meet this bar, use the ASCII path.

## Markdown structure

Use this order:

1. Title and `tl;dr`
2. Competitive-factor table
3. Comparator selection table and supporting alternatives
4. Compact comparator dossiers
5. Score table and pivotal notes
6. Current-market visual chart or titled ASCII panels
7. Current-versus-future visual chart or titled ASCII panels
8. `What The Curves Show`
9. ERRC table
10. Evidence gaps and material open questions

Use descriptive alt text and relative image paths. Keep the score table even when images are present so the result stays accessible, auditable, and pasteable.

## ASCII fallback

Use the same chart logic in text form when images cannot be displayed:

- Draw a real 1-5 vertical axis, connected curve, and factor-ID x-axis.
- Put exactly one solid curve in each panel and identify it with a plain title above the chart.
- Stack the current offering and comparator panels vertically under `CURRENT MARKET VALUE CURVES` so crossings never obscure identity.
- Under `CURRENT VS. FUTURE STRATEGY`, place separately titled current and future panels side by side when the available width is at least 100 monospace columns; otherwise stack them.
- Use `o` for score points and `-`, `/`, and `\` for the solid curve. The title, not a marker code or line texture, identifies the series.
- Include a factor key after the panels.
- Never substitute horizontal rating bars, overlay several curves, or label a curve through conventions such as `[x, dotted]`.

Follow the complete fallback in [../examples/output.md](../examples/output.md) exactly. Use the optional renderer with `--ascii` when helpful, or reproduce the same titled-panel structure manually.

```text
CURRENT OFFERING
5 |      o
  |    // \
4 |o--o     \
3 |          o
2 |
1 |
  +-------------------
   F1    F2    F3    F4
```
