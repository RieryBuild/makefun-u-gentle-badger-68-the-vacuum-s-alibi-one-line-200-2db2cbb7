"""Write the vacuum's one-line alibi to entry.txt (deterministic, stdlib only)."""
import os

LINE = "My sensors flagged that patch as load-bearing dust, and my warranty forbids removing anything load-bearing."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
