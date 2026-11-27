"""r44 exa entry mover: one excuse line for a missed deadline, 200 cap."""

import json
import os
from pathlib import Path

BOUNTY = "u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141"
TOP = 200

read_line = lambda p: p.read_text(encoding="utf-8").strip()

def move():
    line = read_line(Path(__file__).resolve().parent / "entry.txt")
    good = bool(line) and len(line) <= TOP
    if good:
        where = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        where.mkdir(parents=True, exist_ok=True)
        (where / "entry.txt").write_text(line + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"good": good, "where": where.name if good else None, "n": len(line)}))
    if not good:
        raise SystemExit(2)

move()

STAMP = "r44-exa"
print(json.dumps({"stamp": STAMP, "final": True}))
