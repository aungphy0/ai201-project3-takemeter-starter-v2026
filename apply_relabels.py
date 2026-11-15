#!/usr/bin/env python3
"""
Milestone 5 helper: copy the `new_label` column of relabel_review.csv back
into labels.csv.

Only rows where you typed a new_label that differs from the current label are
changed. Each changed row gets "relabelled in unit 6 (rule 2)" added to its
note, so the change is visible in the file and in git.

    python apply_relabels.py            # show what would change
    python apply_relabels.py --write    # actually change labels.csv
"""
import argparse
import collections
import csv

LABELS = {"analysis", "hot_take", "reaction"}

ap = argparse.ArgumentParser()
ap.add_argument("--write", action="store_true", help="write labels.csv")
args = ap.parse_args()

with open("labels.csv", newline="") as f:
    rows = list(csv.DictReader(f))
with open("relabel_review.csv", newline="") as f:
    review = list(csv.DictReader(f))

changes = []
for r in review:
    new = r["new_label"].strip()
    if not new:
        continue
    if new not in LABELS:
        raise SystemExit(f"Row {r['row']}: '{new}' is not one of {sorted(LABELS)}")
    i = int(r["row"]) - 2
    if rows[i]["text"] != r["text"]:
        raise SystemExit(f"Row {r['row']}: text doesn't match labels.csv — did the file change?")
    if new != rows[i]["label"]:
        changes.append((r["row"], rows[i]["label"], new, rows[i]["text"][:70]))
        if args.write:
            rows[i]["label"] = new
            rows[i]["note"] = (rows[i]["note"] + "; relabelled in unit 6 (rule 2)").lstrip("; ")

reviewed = sum(1 for r in review if r["new_label"].strip())
print(f"Reviewed {reviewed} rows, {len(changes)} label changes:\n")
for row, old, new, text in changes:
    print(f"  row {row}: {old} -> {new}   {text}…")
print("\nBy direction:", dict(collections.Counter((o, n) for _, o, n, _ in changes)))

counts = collections.Counter(r["label"] if not args.write else r["label"] for r in rows)
if not args.write:
    counts = collections.Counter(r["label"] for r in rows)
    for _, old, new, _ in changes:
        counts[old] -= 1
        counts[new] += 1
print("\nLabel counts after:", {k: f"{v} ({v/len(rows):.0%})" for k, v in sorted(counts.items())})
if max(counts.values()) / len(rows) > 0.70:
    print("WARNING: a label is above 70% of the data.")

if args.write and not changes:
    print("\nNothing to change — fill in new_label in relabel_review.csv and save it as CSV.")
elif args.write:
    with open("labels.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_ALL,
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("\nWrote labels.csv. Re-run notebook section 2 so it reads the new labels.")
else:
    print("\nDry run. Add --write to change labels.csv.")
