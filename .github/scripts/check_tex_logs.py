"""Fail a build when a TeX log reports visible layout or font problems."""
import re
import sys
from pathlib import Path

pattern = re.compile(
    r"Overfull \\[hv]box|Missing character:|LaTeX Font Warning:|"
    r"(?:Citation|Reference) .+ undefined|There were undefined (?:references|citations)"
)
problems = []
for filename in sys.argv[1:]:
    path = Path(filename)
    if not path.is_file():
        problems.append(f"Missing compilation log: {path}")
        continue
    for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if pattern.search(line):
            problems.append(f"{path}:{number}: {line}")
if problems:
    print("\n".join(problems))
    raise SystemExit(1)
print(f"Checked {len(sys.argv) - 1} TeX logs: no overflow, missing characters or font warnings.")
