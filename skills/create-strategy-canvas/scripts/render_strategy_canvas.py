#!/usr/bin/env python3
"""Render deterministic strategy-canvas SVGs, optional PNGs, and ASCII charts."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from html import escape
from pathlib import Path
from typing import Any, Iterable


WIDTH = 1600
HEIGHT = 900
COMPARATORS_PER_PANEL = 4
ROLE_STYLES = {
    "current": {"color": "#5B6472", "dash": "10 7", "marker": "circle"},
    "future": {"color": "#0F766E", "dash": "", "marker": "diamond"},
}
COMPARATOR_STYLES = [
    {"color": "#0072B2", "dash": "", "marker": "square"},
    {"color": "#D55E00", "dash": "3 7", "marker": "diamond"},
    {"color": "#7A5195", "dash": "13 6 3 6", "marker": "triangle"},
    {"color": "#B07D00", "dash": "7 5", "marker": "circle"},
    {"color": "#008A7A", "dash": "3 5", "marker": "square"},
    {"color": "#9C3D54", "dash": "12 5", "marker": "triangle"},
]
DEFAULT_NOTE = "Scores are strategic hypotheses; sources are documented in the report."


class CanvasError(ValueError):
    """Raised when input data cannot produce a trustworthy chart."""


def require_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CanvasError(f"{field} must be a nonempty string")
    return value.strip()


def validate_canvas(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise CanvasError("input must be a JSON object")

    title = require_text(raw.get("title"), "title")
    subtitle = raw.get("subtitle", "")
    if subtitle is None:
        subtitle = ""
    if not isinstance(subtitle, str):
        raise CanvasError("subtitle must be a string")

    note = raw.get("hypothesis_note", DEFAULT_NOTE)
    note = require_text(note, "hypothesis_note")

    raw_factors = raw.get("factors")
    if not isinstance(raw_factors, list) or len(raw_factors) < 2:
        raise CanvasError("factors must contain at least two items")

    factors: list[dict[str, str]] = []
    factor_ids: set[str] = set()
    for index, item in enumerate(raw_factors):
        if not isinstance(item, dict):
            raise CanvasError(f"factors[{index}] must be an object")
        factor_id = require_text(item.get("id"), f"factors[{index}].id")
        if factor_id in factor_ids:
            raise CanvasError(f"duplicate factor id: {factor_id}")
        factor_ids.add(factor_id)
        label = require_text(item.get("label"), f"factors[{index}].label")
        short_label = require_text(
            item.get("short_label"), f"factors[{index}].short_label"
        )
        if len(short_label) > 54:
            raise CanvasError(
                f"factors[{index}].short_label must be 54 characters or fewer"
            )
        factors.append({"id": factor_id, "label": label, "short_label": short_label})

    raw_series = raw.get("series")
    if not isinstance(raw_series, list) or len(raw_series) < 2:
        raise CanvasError("series must contain current and future offerings")

    series: list[dict[str, Any]] = []
    series_ids: set[str] = set()
    role_counts = {"current": 0, "future": 0, "comparator": 0}
    for index, item in enumerate(raw_series):
        if not isinstance(item, dict):
            raise CanvasError(f"series[{index}] must be an object")
        series_id = require_text(item.get("id"), f"series[{index}].id")
        if series_id in series_ids:
            raise CanvasError(f"duplicate series id: {series_id}")
        series_ids.add(series_id)
        label = require_text(item.get("label"), f"series[{index}].label")
        role = require_text(item.get("role"), f"series[{index}].role")
        if role not in role_counts:
            raise CanvasError(
                f"series[{index}].role must be current, future, or comparator"
            )
        role_counts[role] += 1
        scores = item.get("scores")
        if not isinstance(scores, list) or len(scores) != len(factors):
            raise CanvasError(
                f"series[{index}].scores must contain {len(factors)} values"
            )
        normalized_scores: list[int] = []
        for score_index, score in enumerate(scores):
            if isinstance(score, bool) or not isinstance(score, int) or not 1 <= score <= 5:
                raise CanvasError(
                    f"series[{index}].scores[{score_index}] must be an integer from 1 to 5"
                )
            normalized_scores.append(score)
        series.append(
            {
                "id": series_id,
                "label": label,
                "role": role,
                "scores": normalized_scores,
            }
        )

    if role_counts["current"] != 1:
        raise CanvasError("series must contain exactly one current role")
    if role_counts["future"] != 1:
        raise CanvasError("series must contain exactly one future role")

    return {
        "title": title,
        "subtitle": subtitle.strip(),
        "hypothesis_note": note,
        "factors": factors,
        "series": series,
    }


def load_canvas(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            raw = json.load(handle)
    except FileNotFoundError as exc:
        raise CanvasError(f"input file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CanvasError(f"invalid JSON in {path}: {exc}") from exc
    return validate_canvas(raw)


def wrap_label(label: str, max_chars: int = 18, max_lines: int = 3) -> list[str]:
    words = label.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) <= max_chars:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    if len(lines) <= max_lines:
        return lines
    visible = lines[: max_lines - 1]
    remainder = " ".join(lines[max_lines - 1 :])
    if len(remainder) > max_chars:
        remainder = remainder[: max_chars - 1].rstrip() + "…"
    visible.append(remainder)
    return visible


def render_ascii_panel(
    factors: list[dict[str, str]], series: dict[str, Any]
) -> list[str]:
    """Render one titled value curve without relying on a symbol legend."""
    gap = 6
    score_step = 2
    x_positions = [index * gap for index in range(len(factors))]
    width = x_positions[-1] + 1
    height = 4 * score_step + 1
    grid = [[" "] * width for _ in range(height)]

    def y_position(score: int) -> int:
        return (5 - score) * score_step

    for index in range(len(series["scores"]) - 1):
        x_start = x_positions[index]
        x_end = x_positions[index + 1]
        y_start = y_position(series["scores"][index])
        y_end = y_position(series["scores"][index + 1])
        for x in range(x_start + 1, x_end):
            progress = (x - x_start) / (x_end - x_start)
            y = round(y_start + (y_end - y_start) * progress)
            if y_start == y_end:
                char = "-"
            else:
                char = "\\" if y_end > y_start else "/"
            grid[y][x] = char

    for x, score in zip(x_positions, series["scores"]):
        grid[y_position(score)][x] = "o"

    lines = [series["label"].upper()]
    for row_index, row in enumerate(grid):
        score_label = str(5 - row_index // score_step) if row_index % score_step == 0 else " "
        lines.append(f"{score_label} |{''.join(row)}".rstrip())
    lines.append("  +" + "-" * width)
    factor_axis = [" "] * width
    for x, factor in zip(x_positions, factors):
        factor_id = factor["id"]
        factor_axis[x : x + len(factor_id)] = factor_id
    lines.append("   " + "".join(factor_axis))
    return lines


def render_ascii(data: dict[str, Any]) -> str:
    """Render readable small multiples for environments without image display."""
    current = next(item for item in data["series"] if item["role"] == "current")
    future = next(item for item in data["series"] if item["role"] == "future")
    comparators = [item for item in data["series"] if item["role"] == "comparator"]
    factors = data["factors"]

    lines = ["CURRENT MARKET VALUE CURVES", ""]
    for item in [current, *comparators]:
        lines.extend(render_ascii_panel(factors, item))
        lines.append("")

    lines.extend(["CURRENT VS. FUTURE STRATEGY", ""])
    current_panel = render_ascii_panel(factors, current)
    future_panel = render_ascii_panel(factors, future)
    left_width = max(len(line) for line in current_panel)
    for left, right in zip(current_panel, future_panel):
        lines.append(f"{left:<{left_width}}   {right}")

    lines.extend(["", "FACTOR KEY"])
    for factor in factors:
        lines.append(f"{factor['id']} {factor['label']}")
    return "\n".join(lines).rstrip() + "\n"


def text_element(
    x: float,
    y: float,
    value: str,
    *,
    css_class: str = "",
    anchor: str = "start",
    extra: str = "",
) -> str:
    class_attr = f' class="{css_class}"' if css_class else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}"'
        f'{class_attr}{extra}>{escape(value)}</text>'
    )


def marker_element(shape: str, x: float, y: float, color: str, size: float = 8.0) -> str:
    common = f'fill="#FFFFFF" stroke="{color}" stroke-width="3"'
    if shape == "square":
        return (
            f'<rect x="{x - size:.1f}" y="{y - size:.1f}" width="{2 * size:.1f}" '
            f'height="{2 * size:.1f}" rx="1.5" {common}/>'
        )
    if shape == "diamond":
        points = f"{x:.1f},{y - size - 1:.1f} {x + size + 1:.1f},{y:.1f} "
        points += f"{x:.1f},{y + size + 1:.1f} {x - size - 1:.1f},{y:.1f}"
        return f'<polygon points="{points}" {common}/>'
    if shape == "triangle":
        points = f"{x:.1f},{y - size - 2:.1f} {x + size + 1:.1f},{y + size:.1f} "
        points += f"{x - size - 1:.1f},{y + size:.1f}"
        return f'<polygon points="{points}" {common}/>'
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" {common}/>'


def comparator_style(index: int) -> dict[str, str]:
    return COMPARATOR_STYLES[index % len(COMPARATOR_STYLES)]


def style_for(series: dict[str, Any], comparator_indices: dict[str, int]) -> dict[str, str]:
    role = series["role"]
    if role in ROLE_STYLES:
        return ROLE_STYLES[role]
    return comparator_style(comparator_indices[series["id"]])


def legend_layout(series: Iterable[dict[str, Any]]) -> tuple[list[tuple[dict[str, Any], float, float]], int]:
    positions: list[tuple[dict[str, Any], float, float]] = []
    x = 90.0
    y = 150.0
    rows = 1
    for item in series:
        width = min(360.0, max(190.0, 92.0 + len(item["label"]) * 9.0))
        if x + width > 1510.0:
            x = 90.0
            y += 36.0
            rows += 1
        positions.append((item, x, y))
        x += width
    return positions, rows


def chart_description(data: dict[str, Any], series: list[dict[str, Any]], kind: str) -> str:
    names = ", ".join(item["label"] for item in series)
    factor_names = ", ".join(factor["label"] for factor in data["factors"])
    if kind == "future":
        prefix = "Current-versus-future value curves"
    else:
        prefix = "Current-market value curves"
    return f"{prefix} for {names}, scored from 1 to 5 across {factor_names}."


def render_svg(
    data: dict[str, Any],
    displayed_series: list[dict[str, Any]],
    comparator_indices: dict[str, int],
    *,
    kind: str,
    panel_number: int = 1,
    panel_count: int = 1,
) -> str:
    factors = data["factors"]
    legend_positions, legend_rows = legend_layout(displayed_series)
    plot_left = 155.0
    plot_right = 1530.0
    plot_top = 210.0 + (legend_rows - 1) * 36.0
    plot_bottom = 650.0
    plot_width = plot_right - plot_left
    plot_height = plot_bottom - plot_top
    x_positions = [
        plot_left + index * plot_width / (len(factors) - 1)
        for index in range(len(factors))
    ]

    def y_position(score: int) -> float:
        return plot_bottom - ((score - 1) / 4.0) * plot_height

    if kind == "market":
        heading = "Current Market Value Curves"
        if panel_count > 1:
            heading += f" ({panel_number} of {panel_count})"
        title_id = f"market-title-{panel_number}"
        desc_id = f"market-desc-{panel_number}"
    else:
        heading = "Current Offering vs. Future Strategy"
        title_id = "future-title"
        desc_id = "future-desc"

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
            f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="{title_id} {desc_id}">'
        ),
        f'<title id="{title_id}">{escape(heading)}</title>',
        f'<desc id="{desc_id}">{escape(chart_description(data, displayed_series, kind))}</desc>',
        "<defs>",
        (
            '<marker id="delta-arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" '
            'orient="auto" markerUnits="strokeWidth"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0F766E"/></marker>'
        ),
        "</defs>",
        '<rect width="1600" height="900" fill="#FFFFFF"/>',
        "<style>",
        "text{font-family:-apple-system,BlinkMacSystemFont,\"Segoe UI\",Arial,Helvetica,sans-serif;fill:#18212F}",
        ".chart-title{font-size:30px;font-weight:700}",
        ".subtitle{font-size:18px;fill:#5B6472}",
        ".legend{font-size:17px;font-weight:600}",
        ".tick{font-size:16px;fill:#5B6472}",
        ".axis-title{font-size:16px;font-weight:600;fill:#5B6472}",
        ".factor-id{font-size:16px;font-weight:700;fill:#5B6472}",
        ".factor-label{font-size:17px;font-weight:600}",
        ".delta{font-size:16px;font-weight:700;fill:#0F766E}",
        ".footer{font-size:14px;fill:#6B7280}",
        "</style>",
        text_element(70, 62, heading, css_class="chart-title"),
    ]
    context_line = data["title"]
    if data["subtitle"]:
        context_line += f" — {data['subtitle']}"
    lines.append(text_element(70, 101, context_line, css_class="subtitle"))

    for item, x, y in legend_positions:
        style = style_for(item, comparator_indices)
        dash_attr = f' stroke-dasharray="{style["dash"]}"' if style["dash"] else ""
        lines.append(
            f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x + 44:.1f}" y2="{y:.1f}" '
            f'stroke="{style["color"]}" stroke-width="4"{dash_attr}/>'
        )
        lines.append(marker_element(style["marker"], x + 22, y, style["color"], 6.0))
        lines.append(text_element(x + 56, y + 6, item["label"], css_class="legend"))

    for score in range(1, 6):
        y = y_position(score)
        color = "#C8CDD4" if score in (1, 5) else "#E5E7EB"
        width = "1.5" if score in (1, 5) else "1"
        lines.append(
            f'<line x1="{plot_left:.1f}" y1="{y:.1f}" x2="{plot_right:.1f}" y2="{y:.1f}" '
            f'stroke="{color}" stroke-width="{width}"/>'
        )
        lines.append(text_element(plot_left - 24, y + 6, str(score), css_class="tick", anchor="end"))

    axis_y = (plot_top + plot_bottom) / 2
    lines.append(
        text_element(
            42,
            axis_y,
            "Offering level",
            css_class="axis-title",
            anchor="middle",
            extra=f' transform="rotate(-90 42 {axis_y:.1f})"',
        )
    )
    lines.append(
        text_element(
            plot_right,
            plot_top - 18,
            "Offering level: 1 = very low, 5 = very high",
            css_class="tick",
            anchor="end",
        )
    )

    for item in displayed_series:
        style = style_for(item, comparator_indices)
        points = " ".join(
            f"{x_positions[index]:.1f},{y_position(score):.1f}"
            for index, score in enumerate(item["scores"])
        )
        dash_attr = f' stroke-dasharray="{style["dash"]}"' if style["dash"] else ""
        lines.append(
            f'<polyline points="{points}" fill="none" stroke="{style["color"]}" '
            f'stroke-width="4" stroke-linejoin="round" stroke-linecap="round"{dash_attr}/>'
        )
        for index, score in enumerate(item["scores"]):
            lines.append(
                (
                    f'<g data-series="{escape(item["id"])}" '
                    f'data-factor="{escape(factors[index]["id"])}" data-score="{score}">'
                    + marker_element(
                        style["marker"],
                        x_positions[index],
                        y_position(score),
                        style["color"],
                    )
                    + "</g>"
                )
            )

    if kind == "future":
        current = next(item for item in displayed_series if item["role"] == "current")
        future = next(item for item in displayed_series if item["role"] == "future")
        for index, (before, after) in enumerate(zip(current["scores"], future["scores"])):
            if before == after:
                continue
            x = x_positions[index] + 14.0
            start_y = y_position(before)
            end_y = y_position(after)
            direction = 1.0 if end_y > start_y else -1.0
            start_y += direction * 15.0
            end_y -= direction * 18.0
            lines.append(
                f'<line x1="{x:.1f}" y1="{start_y:.1f}" x2="{x:.1f}" y2="{end_y:.1f}" '
                'stroke="#0F766E" stroke-width="2.5" marker-end="url(#delta-arrow)"/>'
            )
            label_x = x + 13.0 if index % 2 == 0 else x - 13.0
            anchor = "start" if index % 2 == 0 else "end"
            lines.append(
                text_element(
                    label_x,
                    (start_y + end_y) / 2 - 7,
                    f"{before} → {after}",
                    css_class="delta",
                    anchor=anchor,
                )
            )

    for index, factor in enumerate(factors):
        x = x_positions[index]
        lines.append(
            text_element(x, plot_bottom + 40, factor["id"], css_class="factor-id", anchor="middle")
        )
        wrapped = wrap_label(factor["short_label"])
        label = (
            f'<text x="{x:.1f}" y="{plot_bottom + 70:.1f}" text-anchor="middle" '
            'class="factor-label">'
        )
        for line_index, value in enumerate(wrapped):
            dy = "0" if line_index == 0 else "23"
            label += f'<tspan x="{x:.1f}" dy="{dy}">{escape(value)}</tspan>'
        label += "</text>"
        lines.append(label)

    lines.append(
        text_element(
            1530,
            858,
            data["hypothesis_note"],
            css_class="footer",
            anchor="end",
        )
    )
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def render_artifacts(data: dict[str, Any], output_dir: Path, basename: str) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    current = next(item for item in data["series"] if item["role"] == "current")
    future = next(item for item in data["series"] if item["role"] == "future")
    comparators = [item for item in data["series"] if item["role"] == "comparator"]
    comparator_indices = {item["id"]: index for index, item in enumerate(comparators)}
    panels = [
        comparators[index : index + COMPARATORS_PER_PANEL]
        for index in range(0, len(comparators), COMPARATORS_PER_PANEL)
    ] or [[]]

    svg_paths: list[Path] = []
    for panel_index, panel in enumerate(panels, start=1):
        suffix = "-market" if panel_index == 1 else f"-market-{panel_index}"
        path = output_dir / f"{basename}{suffix}.svg"
        path.write_text(
            render_svg(
                data,
                [current, *panel],
                comparator_indices,
                kind="market",
                panel_number=panel_index,
                panel_count=len(panels),
            ),
            encoding="utf-8",
        )
        svg_paths.append(path)

    future_path = output_dir / f"{basename}-future.svg"
    future_path.write_text(
        render_svg(
            data,
            [current, future],
            comparator_indices,
            kind="future",
        ),
        encoding="utf-8",
    )
    svg_paths.append(future_path)

    data_path = output_dir / f"{basename}-data.json"
    data_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return svg_paths


def converter_commands(svg_path: Path, png_path: Path) -> list[list[str]]:
    commands: list[list[str]] = []
    if shutil.which("rsvg-convert"):
        commands.append(["rsvg-convert", "-o", str(png_path), str(svg_path)])
    if shutil.which("inkscape"):
        commands.append(
            [
                "inkscape",
                str(svg_path),
                "--export-type=png",
                f"--export-filename={png_path}",
            ]
        )
    if shutil.which("magick"):
        commands.append(["magick", str(svg_path), str(png_path)])
    if shutil.which("convert"):
        commands.append(["convert", str(svg_path), str(png_path)])
    if shutil.which("sips"):
        commands.append(["sips", "-s", "format", "png", str(svg_path), "--out", str(png_path)])
    return commands


def convert_svg_to_png(svg_path: Path) -> tuple[bool, str]:
    png_path = svg_path.with_suffix(".png")
    try:
        import cairosvg  # type: ignore

        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=WIDTH)
        if png_path.exists() and png_path.stat().st_size > 0:
            return True, "cairosvg"
    except (ImportError, OSError, ValueError):
        pass

    errors: list[str] = []
    for command in converter_commands(svg_path, png_path):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=False)
        except OSError as exc:
            errors.append(f"{command[0]}: {exc}")
            continue
        if result.returncode == 0 and png_path.exists() and png_path.stat().st_size > 0:
            return True, command[0]
        detail = result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}"
        errors.append(f"{command[0]}: {detail}")
        png_path.unlink(missing_ok=True)
    if errors:
        return False, "; ".join(errors)
    return False, "no supported local SVG-to-PNG converter was found"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render strategy-canvas SVGs, optional PNGs, and ASCII charts from JSON data."
    )
    parser.add_argument("--input", required=True, type=Path, help="Path to canvas JSON")
    parser.add_argument("--output-dir", required=True, type=Path, help="Artifact directory")
    parser.add_argument("--basename", default="strategy-canvas", help="Output filename prefix")
    parser.add_argument(
        "--png",
        choices=("auto", "always", "never"),
        default="auto",
        help="PNG conversion behavior",
    )
    parser.add_argument(
        "--ascii",
        action="store_true",
        help="Also write a titled small-multiple ASCII chart",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", args.basename):
        print(
            "error: --basename must contain only letters, numbers, dots, underscores, and hyphens",
            file=sys.stderr,
        )
        return 2
    try:
        data = load_canvas(args.input)
        svg_paths = render_artifacts(data, args.output_dir, args.basename)
        ascii_path = None
        if args.ascii:
            ascii_path = args.output_dir / f"{args.basename}-ascii.txt"
            ascii_path.write_text(render_ascii(data), encoding="utf-8")
    except (CanvasError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    png_failures: list[str] = []
    if args.png != "never":
        for svg_path in svg_paths:
            converted, detail = convert_svg_to_png(svg_path)
            if converted:
                print(f"Wrote {svg_path.with_suffix('.png')} using {detail}")
            else:
                png_failures.append(f"{svg_path.name}: {detail}")
        if png_failures and args.png == "always":
            print("error: PNG conversion failed", file=sys.stderr)
            for failure in png_failures:
                print(f"  {failure}", file=sys.stderr)
            return 2
        for failure in png_failures:
            print(f"warning: PNG skipped for {failure}", file=sys.stderr)

    for svg_path in svg_paths:
        print(f"Wrote {svg_path}")
    if ascii_path is not None:
        print(f"Wrote {ascii_path}")
    print(f"Wrote {args.output_dir / f'{args.basename}-data.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
