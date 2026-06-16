from __future__ import annotations

from pathlib import Path
from urllib import request
from difflib import SequenceMatcher
from html import escape
import json
import math
import re


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = ROOT / "assets"
SVG_PATH = ASSETS / "leetcode-difficulty.svg"

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

IGNORE_DIRS = {
    ".git",
    ".github",
    "scripts",
    "assets",
    "__pycache__",
}

DIFFICULTIES = ["Easy", "Medium", "Hard"]

COLORS = {
    "Easy": "#00b8a3",
    "Medium": "#ffc01e",
    "Hard": "#ff375f",
    "Unknown": "#8b949e",
}

SLUG_ALIASES = {
    "three_sum": "3sum",
    "three_sum_closest": "3sum-closest",
    "four_sum": "4sum",
    "two_sum_2_input_array_is_sorted": "two-sum-ii-input-array-is-sorted",
    "two_sum_ii_input_array_is_sorted": "two-sum-ii-input-array-is-sorted",
    "product_except_self": "product-of-array-except-self",
}


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def folder_to_slug(folder_name: str) -> str:
    if folder_name in SLUG_ALIASES:
        return SLUG_ALIASES[folder_name]

    return folder_name.replace("_", "-")


def leetcode_graphql(query: str, variables: dict) -> dict | None:
    payload = json.dumps({
        "query": query,
        "variables": variables,
    }).encode("utf-8")

    req = request.Request(
        LEETCODE_GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Origin": "https://leetcode.com",
            "Referer": "https://leetcode.com/problemset/",
        },
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        print(f"LeetCode request failed: {exc}")
        return None


def fetch_question_by_slug(slug: str) -> dict | None:
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        title
        titleSlug
        difficulty
      }
    }
    """

    data = leetcode_graphql(query, {"titleSlug": slug})
    if not data:
        return None

    return data.get("data", {}).get("question")


def search_question(folder_name: str) -> dict | None:
    search_text = folder_name.replace("_", " ")

    query = """
    query problemsetQuestionList(
      $categorySlug: String,
      $skip: Int,
      $limit: Int,
      $filters: QuestionListFilterInput
    ) {
      problemsetQuestionList(
        categorySlug: $categorySlug,
        skip: $skip,
        limit: $limit,
        filters: $filters
      ) {
        questions {
          title
          titleSlug
          difficulty
        }
      }
    }
    """

    variables = {
        "categorySlug": "",
        "skip": 0,
        "limit": 10,
        "filters": {
            "searchKeywords": search_text,
        },
    }

    data = leetcode_graphql(query, variables)
    if not data:
        return None

    questions = (
        data
        .get("data", {})
        .get("problemsetQuestionList", {})
        .get("questions", [])
    )

    if not questions:
        return None

    target = normalize(search_text)

    def score(question: dict) -> float:
        title = normalize(question.get("title", ""))
        slug = normalize(question.get("titleSlug", "").replace("-", " "))
        return max(
            SequenceMatcher(None, target, title).ratio(),
            SequenceMatcher(None, target, slug).ratio(),
        )

    best_match = max(questions, key=score)

    if score(best_match) < 0.45:
        return None

    return best_match


def fetch_problem(folder_name: str) -> dict | None:
    slug = folder_to_slug(folder_name)

    question = fetch_question_by_slug(slug)
    if question:
        return question

    return search_question(folder_name)


def get_problem_dirs() -> list[Path]:
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and path.name not in IGNORE_DIRS
    )


def polar_to_cartesian(cx: float, cy: float, radius: float, angle: float) -> tuple[float, float]:
    angle_rad = math.radians(angle)
    return (
        cx + radius * math.cos(angle_rad),
        cy + radius * math.sin(angle_rad),
    )


def pie_slice_path(cx: float, cy: float, radius: float, start_angle: float, end_angle: float) -> str:
    start_x, start_y = polar_to_cartesian(cx, cy, radius, start_angle)
    end_x, end_y = polar_to_cartesian(cx, cy, radius, end_angle)

    large_arc = 1 if end_angle - start_angle > 180 else 0

    return (
        f"M {cx} {cy} "
        f"L {start_x:.2f} {start_y:.2f} "
        f"A {radius} {radius} 0 {large_arc} 1 {end_x:.2f} {end_y:.2f} "
        f"Z"
    )


def render_svg(counts: dict[str, int], unknown_count: int) -> None:
    ASSETS.mkdir(exist_ok=True)

    chart_counts = dict(counts)
    if unknown_count > 0:
        chart_counts["Unknown"] = unknown_count

    total = sum(chart_counts.values())

    width = 820
    height = 420

    cx = 210
    cy = 235
    radius = 130
    inner_radius = 62

    title = "LeetCode Difficulty Distribution"

    slices = []

    non_zero_items = [
        (difficulty, count)
        for difficulty, count in chart_counts.items()
        if count > 0
    ]

    if total == 0:
        slices.append(
            f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="#30363d"/>'
        )
    elif len(non_zero_items) == 1:
        difficulty, count = non_zero_items[0]
        slices.append(
            f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{COLORS[difficulty]}">'
            f'<title>{escape(difficulty)}: {count}</title>'
            f'</circle>'
        )
    else:
        current_angle = -90

        for difficulty, count in chart_counts.items():
            if count == 0:
                continue

            angle = 360 * count / total
            path = pie_slice_path(cx, cy, radius, current_angle, current_angle + angle)

            slices.append(
                f'<path d="{path}" fill="{COLORS[difficulty]}">'
                f'<title>{escape(difficulty)}: {count}</title>'
                f'</path>'
            )

            current_angle += angle

    legend_rows = []
    legend_order = ["Easy", "Medium", "Hard"]
    if unknown_count > 0:
        legend_order.append("Unknown")

    y = 145

    for difficulty in legend_order:
        count = chart_counts.get(difficulty, 0)
        percent = 0 if total == 0 else count / total * 100

        legend_rows.append(
            f'<rect x="430" y="{y - 18}" width="24" height="24" rx="4" fill="{COLORS[difficulty]}"/>'
            f'<text x="470" y="{y}" font-size="25" font-weight="700" fill="#f0f6fc">'
            f'{escape(difficulty)}: {count} ({percent:.1f}%)'
            f'</text>'
        )

        y += 52

    svg = f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(title)}">
  <rect width="{width}" height="{height}" rx="28" fill="#0d1117"/>

  <text x="{width / 2}" y="52" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="32" font-weight="800" fill="#f0f6fc">
    {escape(title)}
  </text>

  <g font-family="Arial, Helvetica, sans-serif">
    {''.join(slices)}

    <circle cx="{cx}" cy="{cy}" r="{inner_radius}" fill="#0d1117"/>

    <text x="{cx}" y="{cy - 8}" text-anchor="middle" font-size="36" font-weight="800" fill="#f0f6fc">
      {total}
    </text>
    <text x="{cx}" y="{cy + 34}" text-anchor="middle" font-size="19" font-weight="600" fill="#8b949e">
      solved
    </text>

    {''.join(legend_rows)}
  </g>
</svg>
"""

    SVG_PATH.write_text(svg, encoding="utf-8")


def update_readme(counts: dict[str, int], unknown: list[str]) -> None:
    start = "<!-- LEETCODE_STATS_START -->"
    end = "<!-- LEETCODE_STATS_END -->"

    known_total = sum(counts.values())
    total_solved = known_total + len(unknown)

    unknown_text = ""
    if unknown:
        unknown_text = "\n\n**Problems without difficulty lookup:**\n\n"
        unknown_text += "\n".join(f"- `{name}`" for name in unknown)

    block = f"""{start}
![LeetCode Difficulty Distribution](assets/leetcode-difficulty.svg)

**Total solved:** {total_solved}

| Difficulty | Count |
|---|---:|
| Easy | {counts["Easy"]} |
| Medium | {counts["Medium"]} |
| Hard | {counts["Hard"]} |
{unknown_text}
{end}"""

    if README.exists():
        content = README.read_text(encoding="utf-8")
    else:
        content = "# LeetCode Solutions\n\n"

    if start in content and end in content:
        before = content.split(start)[0]
        after = content.split(end)[1]
        content = before + block + after
    else:
        content = content.rstrip() + "\n\n" + block + "\n"

    README.write_text(content, encoding="utf-8")


def main() -> None:
    counts = {
        "Easy": 0,
        "Medium": 0,
        "Hard": 0,
    }

    unknown = []

    for folder in get_problem_dirs():
        question = fetch_problem(folder.name)

        if question and question.get("difficulty") in counts:
            difficulty = question["difficulty"]
            counts[difficulty] += 1

            title_slug = question.get("titleSlug", "unknown-slug")
            print(f"{folder.name}: {difficulty} ({title_slug})")
        else:
            unknown.append(folder.name)
            print(f"{folder.name}: unknown")

    render_svg(counts, len(unknown))
    update_readme(counts, unknown)


if __name__ == "__main__":
    main()
