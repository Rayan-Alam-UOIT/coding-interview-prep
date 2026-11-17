
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

START = "<!-- STATS_START -->"
END = "<!-- STATS_END -->"

LANGUAGES = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".c": "C",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".cs": "C#",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".rb": "Ruby",
    ".php": "PHP",
    ".sql": "SQL",
}

IGNORE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
}

IGNORE_FILES = {
    "readme.md",
    "license",
    ".gitignore",
}


def solution_files(directory):
    """Find programming-language files recursively."""
    if not directory.exists():
        return []

    files = []

    for path in directory.rglob("*"):
        if not path.is_file():
            continue

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        if path.name.lower() in IGNORE_FILES:
            continue

        if path.suffix.lower() in LANGUAGES:
            files.append(path)

    return sorted(files)


def count_problems(directory):
    """
    Count distinct problem directories containing code.

    A folder with multiple submissions counts once.
    Code directly inside the platform root counts
    by filename.
    """
    files = solution_files(directory)
    problems = set()

    for file in files:
        relative = file.relative_to(directory)

        if len(relative.parts) == 1:
            problems.add(("file", file.stem))
        else:
            problems.add(("folder", str(relative.parent)))

    return len(problems)


def language_stats(files):
    counts = Counter()

    for file in files:
        language = LANGUAGES.get(file.suffix.lower())

        if language:
            counts[language] += 1

    return counts


def generate_dashboard():
    leetcode_dir = ROOT / "LeetCode"
    neetcode_dir = ROOT / "NeetCode"

    lc_files = solution_files(leetcode_dir)
    nc_files = solution_files(neetcode_dir)

    lc_count = count_problems(leetcode_dir)
    nc_count = count_problems(neetcode_dir)

    total = lc_count + nc_count
    total_files = len(lc_files) + len(nc_files)

    languages = language_stats(lc_files + nc_files)

    updated = datetime.now(timezone.utc).strftime(
        "%B %d, %Y at %H:%M UTC"
    )

    lines = [
        "### Solution Overview",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| **Total platform-specific problems** | **{total}** |",
        f"| LeetCode problems | {lc_count} |",
        f"| NeetCode problems | {nc_count} |",
        f"| Solution code files | {total_files} |",
        f"| Programming languages | {len(languages)} |",
        "",
        "### Programming Languages",
        "",
    ]

    if languages:
        lines.extend([
            "| Language | Files | Share |",
            "|---|---:|---:|",
        ])

        for language, count in languages.most_common():
            percentage = (
                count / total_files * 100
                if total_files else 0
            )

            lines.append(
                f"| {language} | {count} | {percentage:.1f}% |"
            )
    else:
        lines.append("_No solutions synchronized yet._")

    lines.extend([
        "",
        f"*Last updated: {updated}*",
        "",
        "> Counts are based on solution folders and "
        "recognized source files. The same problem "
        "solved on both platforms is counted separately.",
    ])

    return "\n".join(lines)


def update_readme():
    if not README.exists():
        raise FileNotFoundError("README.md not found")

    content = README.read_text(encoding="utf-8")

    if START not in content or END not in content:
        raise ValueError(
            "README must contain STATS_START and STATS_END markers"
        )

    dashboard = generate_dashboard()

    pattern = (
        re.escape(START)
        + r".*?"
        + re.escape(END)
    )

    replacement = (
        START
        + "\n"
        + dashboard
        + "\n"
        + END
    )

    updated_content = re.sub(
        pattern,
        lambda match: replacement,
        content,
        count=1,
        flags=re.DOTALL,
    )

    if updated_content != content:
        README.write_text(
            updated_content,
            encoding="utf-8",
        )
        print("README dashboard updated.")
    else:
        print("README dashboard already up to date.")


if __name__ == "__main__":
    update_readme()
