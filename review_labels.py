#!/usr/bin/env python3
"""
Milestone 5 helper: go through relabel_review.csv one post at a time and fill
in `new_label`. Saves after every answer, so you can quit and resume.

    python review_labels.py          # priority-1 rows only (the 60)
    python review_labels.py --all    # every row

Keys:  r = reaction   h = hot_take   a = analysis
       Enter = keep the CURRENT label     s = skip for now     q = quit
"""
import argparse
import csv
import textwrap

KEYS = {"r": "reaction", "h": "hot_take", "a": "analysis"}
PATH = "relabel_review.csv"

ap = argparse.ArgumentParser()
ap.add_argument("--all", action="store_true", help="review priority-2 rows too")
args = ap.parse_args()

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)


def save():
    with open(PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


todo = [r for r in rows if not r["new_label"].strip() and (args.all or r["priority"] == "1")]
print(f"{len(todo)} rows to review. Rule: the writer's own running/feelings -> reaction; "
      f"a claim about runners or the sport -> hot_take. Ignore tone.\n")

for n, r in enumerate(todo, 1):
    print("=" * 78)
    print(f"[{n}/{len(todo)}]  labels.csv row {r['row']}")
    print(textwrap.fill(r["text"], 78))
    print("-" * 78)
    print(f"  current:   {r['label']}")
    if r.get("suggested"):
        mark = "   <-- CHANGE" if r.get("change") else ""
        print(f"  suggested: {r['suggested']} ({r.get('confidence', '')}){mark}")
        print(f"  reason:    {r.get('reason', '')}")
    while True:
        k = input("  r / h / a, Enter = keep current, s = skip, q = quit > ").strip().lower()
        if k == "":
            r["new_label"] = r["label"]
        elif k in KEYS:
            r["new_label"] = KEYS[k]
        elif k == "s":
            break
        elif k == "q":
            save()
            raise SystemExit("Saved. Run again to continue where you left off.")
        else:
            continue
        save()
        if r["new_label"] != r["label"]:
            print(f"  -> changed to {r['new_label']}")
        break
    print()

done = sum(1 for r in rows if r["new_label"].strip())
print(f"Done. {done} rows have a new_label. Next: python apply_relabels.py")
