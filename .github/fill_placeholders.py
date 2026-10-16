"""Copies the given pages into the output folder and fills in their {{PLACEHOLDERS}}.

    python3 .github/fill_placeholders.py OUTPUT FILE...

Each placeholder takes the value of the environment variable with the same name. The workflow sets
them from the repository's Actions variables. A missing value stops the build, so a page is never
published with a gap.
"""
import html
import os
import re
import sys
from pathlib import Path

PLACEHOLDER = re.compile(r"\{\{([A-Z_]+)\}\}")


def main(output, names):
    output.mkdir(parents=True, exist_ok=True)
    for name in names:
        text = Path(name).read_text(encoding="utf-8")
        missing = sorted({key for key in PLACEHOLDER.findall(text) if not os.environ.get(key, "").strip()})
        if missing:
            sys.exit(f"{name}: set the repository variable {', '.join(missing)} first.")
        filled = PLACEHOLDER.sub(lambda match: html.escape(os.environ[match.group(1)].strip()), text)
        (output / name).write_text(filled, encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]), sys.argv[2:])
