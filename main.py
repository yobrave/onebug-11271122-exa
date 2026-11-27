# exa excuse pipeline r45 — function decomposition style
import json
import os
import time
from pathlib import Path


def locate():
    return Path(__file__).resolve().parent / "entry.txt"


def publish(folder: Path, payload: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    slot = folder / "entry.txt"
    slot.write_text(payload, encoding="utf-8")
    return slot


if __name__ == "__main__":
    text = locate().read_text(encoding="utf-8")
    where = publish(Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"), text)
    print(json.dumps({"stamp": f"exa-r2-{int(time.time())}", "wrote": str(where), "size": len(text)}))
