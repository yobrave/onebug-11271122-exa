# exa deadline-excuse relay - u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141
# round 1127-1122: stages the one-line excuse through a fixed pipeline.
import json, os, pathlib, sys

SLIP_LIMIT = 200
BOUNTY_ID = "u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141"
HOME = pathlib.Path(__file__).resolve().parent


def step_read():
    return (HOME / "entry.txt").read_text(encoding="utf-8").strip()


def step_vet(t):
    if not t:
        return "nothing staged"
    if len(t) > SLIP_LIMIT:
        return "slip too long: %d" % len(t)
    return None


def step_put(t):
    tray = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    tray.mkdir(parents=True, exist_ok=True)
    (tray / "entry.txt").write_text(t + "\n", encoding="utf-8", newline="\n")
    return tray


def relay():
    t = step_read()
    trouble = step_vet(t)
    if trouble:
        print(json.dumps({"ok": False, "trouble": trouble, "limit": SLIP_LIMIT}))
        return 1
    tray = step_put(t)
    print(json.dumps({"ok": True, "slip": len(t), "tray": str(tray),
                      "bounty": BOUNTY_ID, "kind": "deadline excuse",
                      "round": "1127-1122"}))
    return 0


sys.exit(relay())
