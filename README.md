# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

TakeMeter sorts posts from the **LetsRun.com message board**, one of the
oldest and loudest running forums online, where runners argue about race
results, doping, shoes and training. Every post goes into one of three labels:
`analysis` (an argument carried by a checkable fact), `hot_take` (a confident
claim with nothing behind it), or `reaction` (the writer's own feeling or
experience). The goal is to separate the posts that actually argue from data
from the much larger pile of confident opinions, which is most of what the
forum is.

---

## Label Taxonomy

### `analysis`

**Definition:** Makes an argument where a specific, checkable fact (a time, a
date, a stat, a quote or a named comparison) carries the argument.

**Example 1:**
> A 2:01:41 has a VDOT of 84.6. That VDOT predicts a 58:04 for the half
> marathon. Age grading factor the half marathon for 44 is 93.27%. That puts him
> at 62:15. There’s uncertainty around the VDOT prediction and age grading, but
> 2:15 is a lot of time to cut off. Super shoes could do it (he set his marathon
> PB pre-super shoes).

**Example 2:**
> It’s because the police depts are using events to fill their coffers. We have
> to pay 4 hrs of time +1 hr travel time for 2 officers in addition to vehicle
> fees. What cost 615 in 2018 is now 1200+. This is for a small 5k

### `hot_take`

**Definition:** A confident general claim about runners, races or the sport,
with no support offered. It might be true, but it isn't argued.

**Example 1:**
> Father Time has defeated talent every time. There will be no exception here.
> But perhaps a 60:xx is possible. I thought Kenenisa had an injury.

**Example 2:**
> Mantz and Talbi will be lucky to be <2:08.

### `reaction`

**Definition:** The writer's own response or experience: a feeling about a
result or news that just happened, or a report of their own running, rather
than an argument about the world.

**Example 1:**
> Colour me impressed, thought the mileage would be too much and he’d be too
> fatigued for anything fast. Hope it converts to the full

**Example 2:**
> I’m actually really shocked by this, but I suppose I shouldn’t be. She’s been
> successful for so long I really thought she was clean. Definitely in the
> conversation for GOAT status and now it’s all ruined.

### The hardest boundary

**Which two labels:** `analysis` vs `hot_take`. LetsRun posts are full of
times and splits, so almost every post has a number in it. The question is
whether the number is doing anything.

**The decision rule I used every time:** Cover up the number and reread the
post. If the conclusion still stands exactly as confidently, the number was
decoration and the post is a `hot_take`. It's `analysis` only if the fact is
the reason given for the conclusion. Second rule, for `reaction` vs
`hot_take`: if the post is about the writer's own running or feelings, it's
`reaction`; if it claims something about runners or the sport in general,
it's `hot_take`.

---

## The Dataset

**Where the posts came from:** Public threads on the LetsRun.com forum
(letsrun.com/forum), collected on 25 October 2026 from 22 running threads. The
threads covered the Valencia Half Marathon results, Yaseen Abdalla's 59:12,
Mark Kiptoo's age-50 marathon record, Peres Jepchirchir's EPO positive, the WSJ
super-shoe injury story, rising race prices, pacing advice for a high school
5k, and a "5k PB vs current fitness" thread. Only each poster's own words were
kept: quoted replies, usernames, links and posts under 6 words were removed.
Results tables pasted from websites and a few posts that were mainly attacks on
whole nationalities were dropped. 222 posts were collected; 22 that fit no
label (plain questions and one-line jokes) were removed, leaving 200. The
source URL for every post is in `data/post_sources.csv`, and the removed posts
are in `data/dropped_posts.csv`.

**How I labelled them:** I labelled the first 20 posts cold, on my own, before
seeing any other labels (note `cold`). The other 180 were pre-labelled by
Claude using my three definitions, and I then read and checked every one,
correcting the labels I disagreed with (note `pre-labelled, checked`).
<!-- ⚠️ Only keep the sentence above once you have actually reviewed all 180.
     Add how many labels you changed, e.g. "I changed 23 of the 180." -->

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `hot_take` | 114 | 57% |
| `reaction` | 48 | 24% |
| `analysis` | 38 | 19% |
| **Total** | 200 | 100% |

<!-- ⚠️ Update these if your review changes any labels. -->

**Three hard cases**

**1.**
> *The post:* "Did you watch NYC 2024? Mantz ran 2:09 on an abbreviated
> buildup after the Olympics when he was there for a payday. He’s a better
> runner today. You might be crazy if you think he won’t run under 2:08."
>
> *Could have been:* `hot_take` or `analysis`
>
> *I chose, because:* `analysis`. The tone is a hot take ("you might be crazy"),
> but cover up the 2:09 and there's no argument left. The 2024 time on a short
> buildup is the whole reason for the prediction, so the fact carries it.

**2.**
> *The post:* "Agreed. Not even her primary distance, and she's in the middle
> of training for CIM—her first Marathon. Venters did well, too; not sure what
> her goal race but I doubt it was this."
>
> *Could have been:* `reaction` or `analysis`
>
> *I chose, because:* `analysis`. It was written within hours of the race, which
> pulls toward `reaction`, but recency doesn't outrank evidence. The post argues
> that the result is better than it looks, and the checkable fact that she's
> mid-way through marathon training is the support.

**3.**
> *The post:* "Back in my 30's my best was 16:52 this weekend in my 60's I ran
> a 23:53 happy to still be racing and running daily."
>
> *Could have been:* `analysis` or `reaction`
>
> *I chose, because:* `reaction`. It has two specific times, but they aren't
> arguing anything. They report the writer's own running and how he feels about
> it. Numbers alone don't make a post `analysis`.

<!-- ⚠️ These are drafts. Swap in posts that really made YOU pause, and make
     sure each "I chose" matches the label in your final labels.csv. -->

---

## The Training Run

**Base model:** `distilbert-base-uncased`

**Settings:** Run 1 used the notebook defaults: 3 epochs, learning rate 2e-5,
batch size 16, max length 128, seed 42. Trained on Apple Silicon (`mps`),
torch 2.14.1.

**Anything I changed from the defaults, and why:** Run 1 collapsed. The model
predicted `hot_take` for all 30 test posts: accuracy 0.567, macro F1 0.241, and
F1 of 0.00 for both `analysis` and `reaction`. That is exactly the score of
always guessing the biggest label (57% of my data). With only 140 training
posts, 3 epochs at batch size 16 is about 27 update steps at a small learning
rate, which wasn't enough for the model to move away from the majority label.
For run 2 I raised **epochs to 10** and **learning rate to 5e-5**, keeping
everything else the same.
<!-- ⚠️ Fill in after you re-run: "Run 2: accuracy ___, macro F1 ___,
     F1 analysis ___ / hot_take ___ / reaction ___." If run 2 also collapses,
     say so plainly. -->

**Split sizes:** 140 train / 30 validation / 30 test (stratified 70/15/15,
seed 42). The test split has 17 `hot_take`, 7 `reaction` and 6 `analysis`.
Both `reaction` and `analysis` have fewer than 8 posts in test, so one post
changes their recall by about 15 points. I expect their F1 to move a lot
between seeds in unit 6.
<!-- Paste the train/val per-label table from notebook section 3 here. -->

**A note on timing:** I wrote `criteria.md` before training, but committed it
in the same commit as my first `results.json`, so my git history can't show
the order. None of the targets were changed after seeing results.

---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
