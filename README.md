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

**Settings:** Final run: 10 epochs, learning rate 5e-5, batch size 16, max
length 128, seed 42. (Run 1 used the notebook defaults of 3 epochs and
learning rate 2e-5.) Trained on Apple Silicon (`mps`),
torch 2.14.1.

**Anything I changed from the defaults, and why:** Run 1 collapsed. The model
predicted `hot_take` for all 30 test posts: accuracy 0.567, macro F1 0.241, and
F1 of 0.00 for both `analysis` and `reaction`. That is exactly the score of
always guessing the biggest label (57% of my data). With only 140 training
posts, 3 epochs at batch size 16 is about 27 update steps at a small learning
rate, which wasn't enough for the model to move away from the majority label.
For run 2 I raised **epochs to 10** and **learning rate to 5e-5**, keeping
everything else the same (same seed, so the same 30 test posts).

That fixed the collapse. Run 2 (seed 42, the one in `results.json`):

| Measure | Run 1 (defaults) | Run 2 (10 epochs, lr 5e-5) |
|---|---|---|
| Accuracy | 0.567 | 0.700 |
| Macro F1 | 0.241 | 0.656 |
| F1 `analysis` | 0.00 | 0.67 |
| F1 `hot_take` | 0.72 | 0.76 |
| F1 `reaction` | 0.00 | 0.55 |

The model now predicts all three labels. Its weakest spot is `reaction`: only
3 of the 7 reaction posts in test were found (recall 0.43), and the other 4
were called `hot_take`. That's the reaction vs hot_take boundary, which makes
sense: many of my `reaction` posts are people reporting their own times,
which read a lot like confident claims. `analysis` and `hot_take` were
confused in both directions (2 each way). The confidence score is useful: the
model was right on 9 of its 10 most confident predictions but only 4 of its 10
least confident.

This is one seed on a 30-post test split, so these numbers aren't stable yet.
Unit 6 reruns them on three seeds.

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
| Overall accuracy | 0.200 | 0.700 | +0.500 |
| Macro F1 | 0.111 | 0.656 | +0.545 |
| F1 — `analysis` | 0.333 | 0.667 | +0.333 |
| F1 — `hot_take` | 0.000 | 0.757 | +0.757 |
| F1 — `reaction` | 0.000 | 0.545 | +0.545 |

**What I predicted before I looked:**
I expect the baseline to score about 0.50 accuracy and 0.40 macro F1, well below my trained model (0.70 / 0.656). It has never seen LetsRun posts and only gets one sentence per label. I expect it to do best on reaction, because first-person feelings and race reports are easy to spot, and maybe beat my model’s 0.43 recall there. I expect it to struggle most on analysis vs hot_take, because the difference is whether a fact actually carries the argument, and a definition alone can’t teach that. If the gap turns out smaller than 0.05 accuracy (under 2 posts out of 30), I’ll treat the two models as tied.

**What the gap actually means:**
I expected 'hot_take' to be its best label but it showed 0. The trained model beat the baseline by 0.545 macro F1 (21 vs 6 correct out of 30), far more than the 1–2 posts chance could explain, so fine-tuning on my 140 labelled posts clearly taught the model something my definitions alone could not. But the baseline labelled every single post analysis, likely because my analysis definition (“makes an argument…”) fits almost any opinion post, so this gap partly reflects a weak opponent rather than a strong model. The fairer comparison is the “always guess hot_take” strategy (0.57 accuracy), which my model beats by only about 4 posts: useful, but still modest.



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | >= 0.65 on every seed | 0.70 | 0.57 | 0.63 | MISSED (fails on seeds 7 and 2024) |
| 2. Macro F1 | >= 0.50 on every seed | 0.66 | 0.49 | 0.57 | MISSED (seed 7 just misses) |
| 3. `analysis` / `reaction` F1 | each >= 0.40 on every seed | 0.67 / 0.55 | 0.33 / 0.43 | 0.67 / 0.31 | MISSED (`analysis` fails on seed 7, `reaction` on seed 2024) |
| 4. Staff agreement | >= 21/30 | 15/30 | 15/30 | 15/30 | MISSED (15/30 = 50%; the same for every seed, since no model is involved) |
| 5. Confidence gap (top third minus bottom third) | >= 0.15 on every seed | 0.90 − 0.40 = 0.50 | 0.80 − 0.20 = 0.60 | 0.90 − 0.40 = 0.50 | MET on all three seeds |

**Spread across seeds** (notebook section 6):

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---|---|---|---|
| Overall accuracy | 0.700 | 0.567 | 0.633 | 0.133 |
| Macro F1 | 0.656 | 0.489 | 0.572 | 0.167 |
| F1 — `analysis` | 0.667 | 0.333 | 0.667 | 0.333 |
| F1 — `hot_take` | 0.757 | 0.706 | 0.743 | 0.051 |
| F1 — `reaction` | 0.545 | 0.429 | 0.308 | 0.238 |

Accuracy moved 0.133 across seeds, which is more than the notebook's 10-point
line. On 30 test posts that's 21 vs 17 correct, a 4-post swing. `hot_take`
(17 test posts) holds steady at about 0.71–0.76. The two small labels swing
hard: `analysis` F1 halves on seed 7, and `reaction` drops from 0.55 to 0.31.
With only 6 and 7 test posts, one or two posts decide those scores. So seed 42,
the run I reported in unit 5, was the best of the three, not a typical one.

### Confusion matrix

Seed 42, the one the notebook prints:

| true \ predicted | analysis | hot_take | reaction |
|---|---|---|---|
| analysis | 4 | 2 | 0 |
| hot_take | 2 | 14 | 1 |
| reaction | 0 | 4 | 3 |

Summed over all three seeds (90 test predictions), to check whether the
pattern holds:

| true \ predicted | analysis | hot_take | reaction |
|---|---|---|---|
| analysis | 10 | 6 | 2 |
| hot_take | 5 | 39 | 7 |
| reaction | 3 | 10 | 8 |

**My biggest off-diagonal number, and what it means:**
My biggest off-diagonal number is 4: on seed 42, four real `reaction` posts
were called `hot_take`, while only 1 `hot_take` was called `reaction`. So on
that seed the model leans toward `hot_take` for this pair. I think this
happens because many of my `reaction` posts report the writer's own race time,
which reads like a confident claim. Across all three seeds the same pair is
still the biggest problem (10 `reaction` → `hot_take`, the largest summed
off-diagonal cell), but it isn't one-sided. Seeds 7 and 2024 each called 3
`hot_take` posts `reaction`, so it's 10 one way and 7 the other. The model
finds `reaction` vs `hot_take` hard in both directions, and `reaction` is
right only 8 times out of 21. Errors going both ways usually point to a fuzzy
boundary rather than a model bias, and Milestone 3's agreement check can show
whether that fuzziness is in my own labelling.



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

**Agreement rate:** 15 / 30 = 50%

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

**Where the 15 disagreements fall:**

| Staff said | I said | Count |
|---|---|---|
| `reaction` | `hot_take` | 5 |
| `hot_take` | `reaction` | 4 |
| `analysis` | `hot_take` | 3 |
| `analysis` | `reaction` | 2 |
| `hot_take` | `analysis` | 1 |

**1.**
> *The post:* "The club championship scoring changed in 2019 from top-6 to top-10. Since then our B team has finished above the A team twice. That's not depth improving, it's the scoring rewarding turnout."
>
> *Staff said / I said:* `analysis` / `reaction`
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:* "Everyone blames the hill at 18 miles. I split the field into people who ran the first half under 1:45 and over, and the slowdown after 18 was almost identical for both groups. If the hill were the problem the fast starters would fall apart harder."
>
> *Staff said / I said:* `analysis` / `hot_take`
>
> *My call, and why:*
>
> *Which pile:*

**3.**
> *The post:* "Ran the same loop in 4C and in 24C within a fortnight, same effort by heart rate. 90 seconds slower in the heat over six miles. People keep saying heat costs you 'a bit' and it's more than that."
>
> *Staff said / I said:* `analysis` / `hot_take`
>
> *My call, and why:*
>
> *Which pile:*

**4.**
> *The post:* "The 10K route was remeasured in 2021 and came out 60 metres long. Everyone comparing PBs from before and after that is comparing two different races, which is about 12 seconds at club pace."
>
> *Staff said / I said:* `analysis` / `hot_take`
>
> *My call, and why:*
>
> *Which pile:*

**5.**
> *The post:* "Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people."
>
> *Staff said / I said:* `analysis` / `reaction`
>
> *My call, and why:*
>
> *Which pile:*

**6.**
> *The post:* "Anyone who races more than once a month isn't training, they're just collecting medals."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:*
>
> *Which pile:*

**7.**
> *The post:* "The club needs to stop pretending the Tuesday session is for everyone. It isn't and it never has been."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:*
>
> *Which pile:*

**8.**
> *The post:* "Times are down about 3% since the shoe rules changed, so obviously the shoes are the whole story and the sport has a problem."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:*
>
> *Which pile:*

**9.**
> *The post:* "Road racing peaked in about 2015 and everything since has been marketing."
>
> *Staff said / I said:* `hot_take` / `analysis`
>
> *My call, and why:*
>
> *Which pile:*

**10.**
> *The post:* "Nobody actually enjoys the long run. They enjoy having done it, which is a completely different thing, and the sport would be more honest if it said so."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:*
>
> *Which pile:*

**11.**
> *The post:* "Got up at 5, drove ninety minutes, and it's cancelled. Standing in the car park in the rain reading the email."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:*
>
> *Which pile:*

**12.**
> *The post:* "Watching the last 400 of that and I had to stand up. Still standing up actually."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:*
>
> *Which pile:*

**13.**
> *The post:* "Blew up at 20 with the pace band still in my hand like it was going to help. Rough one."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:*
>
> *Which pile:*

**14.**
> *The post:* "Third DNF this year. I don't really want to talk about it, just wanted to put it somewhere."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:*
>
> *Which pile:*

**15.**
> *The post:* "Just realised the shoes I set every PB in this year are the ones I bought by accident in the wrong size."
>
> *Staff said / I said:* `reaction` / `hot_take`
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
