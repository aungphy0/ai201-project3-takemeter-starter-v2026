#!/usr/bin/env python3
"""
Notebook section 6, run outside Jupyter: one seed per fresh Python process.

Why: on an 8 GB Mac the notebook kernel runs out of memory, because every
trained model stays loaded in the same kernel and the kernel dies partway
through the three seeds. Here each seed runs in its own process, which frees
all its memory when it exits.

The code is NOT re-implemented. The imports, settings (LABELS, EPOCHS,
LEARNING_RATE, ...) and functions (split_dataset, train_model, evaluate, ...)
are read straight out of takemeter.ipynb, so the results match the notebook.

    python run_seeds.py --label after
"""
import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path

SEEDS = [42, 7, 2024]
SETTING_CELLS_HINT = ("def pick_device", "LABELS = [")  # cells whose plain assignments we keep


def notebook_definitions(path="takemeter.ipynb"):
    """Imports, function defs and the settings assignments from the notebook,
    without the top-level calls that would train a model."""
    nb = json.loads(Path(path).read_text())
    keep = []
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        src = "".join(cell["source"])
        tree = ast.parse(src)
        settings_cell = any(h in src for h in SETTING_CELLS_HINT)
        for node in tree.body:
            if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
                keep.append(node)
            elif settings_cell and isinstance(node, ast.Assign):
                keep.append(node)
    return compile(ast.Module(body=keep, type_ignores=[]), path, "exec")


def run_one(seed, out):
    ns = {}
    exec(notebook_definitions(), ns)
    import pandas as pd
    df = pd.read_csv("labels.csv")
    print(f"seed {seed}: {len(df)} rows  {df['label'].value_counts().to_dict()}", flush=True)
    tr, va, te = ns["split_dataset"](df, seed)
    t, tok = ns["train_model"](tr, va, ns["LABELS"], seed, ns["EPOCHS"], ns["LEARNING_RATE"],
                               ns["BATCH_SIZE"], ns["BASE_MODEL"], quiet=True)
    r = ns["evaluate"](t, tok, te, ns["LABELS"], seed=seed)
    r["device"] = ns["DEVICE"]
    r["device_name"] = ns["DEVICE_NAME"]
    r["torch_version"] = __import__("torch").__version__
    r["max_length"] = ns["MAX_LENGTH"]
    Path(out).write_text(json.dumps(r, indent=2))
    print(f"seed {seed}: accuracy {r['accuracy']:.3f}  macro F1 {r['f1_macro']:.3f}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True, help='"after" for Milestone 5')
    ap.add_argument("--one", type=int, help=argparse.SUPPRESS)
    ap.add_argument("--out", help=argparse.SUPPRESS)
    args = ap.parse_args()

    if args.one is not None:
        run_one(args.one, args.out)
        return

    final = Path(f"results_three_seeds_{args.label}.json")
    if args.label == "before" and final.exists():
        sys.exit("results_three_seeds_before.json already exists; refusing to overwrite it.")

    parts = []
    for i, seed in enumerate(SEEDS, 1):
        part = Path(f".seed_{args.label}_{seed}.json")
        if part.exists():
            print(f"seed {seed}: already done, reusing {part}", flush=True)
        else:
            print(f"\n=== Seed {seed} ({i} of {len(SEEDS)}) ===", flush=True)
            subprocess.run([sys.executable, __file__, "--label", args.label,
                            "--one", str(seed), "--out", str(part)], check=True)
        parts.append(json.loads(part.read_text()))

    final.write_text(json.dumps(parts, indent=2))
    for s in SEEDS:
        Path(f".seed_{args.label}_{s}.json").unlink()
    print(f"\nWrote {final}. Commit it.")


if __name__ == "__main__":
    main()
