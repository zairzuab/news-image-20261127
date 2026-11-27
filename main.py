#!/usr/bin/env python3
"""news-image-20261127 entry (Python 3.13, standard library only).

The front page is the entry.png beside this file. The program copies it
to /output/entry.png, the one image this entry hands in. Nothing else is
read, written or fetched; it runs with no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
try:
    shutil.copyfile(SRC, OUT)
except OSError as exc:
    print(f"could not hand in entry.png: {exc}", file=sys.stderr)
    raise SystemExit(1)
# The grader runs the program twice and both runs must write the same
# bytes, so confirm the copy landed whole before reporting success.
if os.path.getsize(OUT) != os.path.getsize(SRC):
    print("handed-in entry.png is not whole", file=sys.stderr)
    raise SystemExit(1)
print(f"handed in {OUT}")
