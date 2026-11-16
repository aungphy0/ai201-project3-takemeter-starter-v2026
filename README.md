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
| 1 | Overall accuracy | >= 0.65 on every seed | MISSED | 0.70 / 0.57 / 0.63. Only seed 42 clears it; seeds 7 and 2024 fall short. |
| 2 | Macro F1 | >= 0.50 on every seed | MISSED | 0.66 / 0.49 / 0.57. Seed 7 misses by 0.01, but the target says every seed. |
| 3 | `analysis` and `reaction` F1 | each >= 0.40 on every seed | MISSED | `analysis` is 0.33 on seed 7 and `reaction` is 0.31 on seed 2024. A different label fails each time, and no seed has both below. |
| 4 | Staff agreement | >= 21/30 | MISSED | 15/30 (50%), 6 posts short. No model involved, so it's the same on every seed. |
| 5 | Confidence gap | top third >= bottom third + 0.15, every seed | MET | Gaps of 0.50 / 0.60 / 0.50, all well above 0.15. |

**Diagnoses**


**Criterion 4 (agreement 15/30): a labelling-consistency problem, which
feeds the other misses.**
9 of my 15 disagreements with staff are on `reaction` vs `hot_take`, and they
go both ways: 5 posts staff called `reaction` I called `hot_take`, and 4 the
other way round. The posts I called `hot_take` were short first-person reports
with no general claim ("Third DNF this year…", "Got up at 5, drove ninety
minutes, and it's cancelled…"). The posts I called `reaction` were general
claims said with feeling ("Nobody actually enjoys the long run…"). Staff rule 2
covers exactly this, and 8 of these 9 are pile (a) in my adjudication: I knew
the rule and applied it loosely. 5 of the other 6 are posts staff called `analysis` and I
didn't. In most of them (the heat loop, the hill split, three runners in
different shoes) the fact was the writer's own measurement, and I treated
"personal" as "not evidence". Only once did it go the other way: I called
"Road racing peaked in about 2015…" `analysis` because it has a year in it,
which is exactly the decoration rule 1 warns about.

**Criteria 1, 2 and 3: two causes, and the agreement report separates them.**

*Cause 1: a boundary I applied inconsistently (`reaction` vs `hot_take`).*
Across the three seeds, the model's biggest confusion is the same pair I
disagreed with staff on: 10 real `reaction` posts called `hot_take` and 7
`hot_take` posts called `reaction` (summed confusion matrix). It's confused
both ways, not lopsided, and that matches my own labelling: I made the same
mistake in both directions on the staff set. If I can't keep the line straight
on 30 posts with written rules in front of me, my 200 training labels almost
certainly blur it too, so the model is learning from contradictory examples.
`labels.csv` backs this up: all 180 pre-labelled rows still carry the note
"pre-labelled by Claude - CHECK", 27 `reaction` rows were tagged "(was
personal)", and 23 rows are marked "(unsure)". The `reaction` label ended up
meaning "personal" rather than "a feeling about something that just happened".
This is the main reason `reaction` F1 drops to 0.31 on seed 2024.

*Cause 2: too few examples for the small labels.*
`analysis` has 38 posts and `reaction` 48, so about 27 and 34 land in
training and only 6 and 7 in each test split. `hot_take` (17 test posts)
barely moves across seeds (F1 0.71–0.76). `analysis` swings from 0.67 to 0.33
and back, and `reaction` from 0.55 to 0.31. On seed 7, `analysis` got 2 of 6
right, and that one label is what pulls macro F1 down to 0.49 (criterion 2)
and accuracy to 0.57 (criterion 1). Accuracy moved 0.133 across seeds, more
than the notebook's 10-point line, so a target like 0.65 can't hold reliably
on a 30-post test set. This part is a data-size problem, not a labelling one.
`analysis` vs `hot_take` is a smaller confusion in the model (6 and 5 summed),
and my staff disagreements there point the same way as Cause 1: I'm stricter
about calling something `analysis` than staff are. That makes the small
`analysis` label even smaller and noisier.

**Not the model:** the confidence gap (criterion 5) is met on every seed
(0.50–0.60). When the model is sure, it's right 80–90% of the time, so it
*is* learning a real signal. The misses cluster where my labels are
inconsistent or thin, not across the board.

**What this points to for Milestone 5:** relabel the `reaction`/`hot_take`
posts in `labels.csv` strictly by rule 2 (general claim → `hot_take`; the
writer's own just-happened experience → `reaction`), starting with the
"(unsure)" and "(was personal)" rows, then re-run the three seeds with
`RUN_LABEL = "after"`.

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
> *My call, and why:* Staff is right. Rule 3: recency doesn't outrank evidence, and this post isn't even recent. A named date (2019), a named rule change (top-6 to top-10) and a named result (B team above A twice) are the whole argument for "it's the scoring rewarding turnout". Nothing in it is a feeling, so `reaction` doesn't fit at all.
>
> *Which pile:* (a). Rule 1 covered it and the fact is clearly load-bearing. I applied it loosely.

**2.**
> *The post:* "Everyone blames the hill at 18 miles. I split the field into people who ran the first half under 1:45 and over, and the slowdown after 18 was almost identical for both groups. If the hill were the problem the fast starters would fall apart harder."
>
> *Staff said / I said:* `analysis` / `hot_take`
>
> *My call, and why:* Staff is right. It opens like a hot take ("Everyone blames the hill"), but rule 1 asks whether the fact carries the argument, and here it does: the writer splits the field at 1:45, reports that the slowdown was the same for both groups, and draws the inference from that. Take the test out and there's no conclusion left.
>
> *Which pile:* (a). I let the confident opening outweigh the evidence that followed.

**3.**
> *The post:* "Ran the same loop in 4C and in 24C within a fortnight, same effort by heart rate. 90 seconds slower in the heat over six miles. People keep saying heat costs you 'a bit' and it's more than that."
>
> *Staff said / I said:* `analysis` / `hot_take`
>
> *My call, and why:* Staff is right. 4C vs 24C, the same heart-rate effort, and 90 seconds over six miles is the reason given for "more than a bit". It's one runner and not a real experiment, but the staff definition only asks for a checkable fact doing work, not good science. Rule 4 agrees: most of the words go to the measurement, not the claim.
>
> *Which pile:* (a). I treated the writer's own measurement as "just personal", which the rules don't support.

**4.**
> *The post:* "The 10K route was remeasured in 2021 and came out 60 metres long. Everyone comparing PBs from before and after that is comparing two different races, which is about 12 seconds at club pace."
>
> *Staff said / I said:* `analysis` / `hot_take`
>
> *My call, and why:* Staff is right. A date (2021), a measurement (60 metres long) and the arithmetic consequence (about 12 seconds) are the argument that before-and-after PBs aren't comparable. That's rule 1's `analysis` example almost exactly.
>
> *Which pile:* (a). Rule 1 covers it directly.

**5.**
> *The post:* "Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people."
>
> *Staff said / I said:* `analysis` / `reaction`
>
> *My call, and why:* Staff is right, even though they marked it HARD. `reaction` is the hardest label to defend here: there's no feeling and nothing that just happened to the writer. The hedged conclusion ("smaller than the noise") rests entirely on a checkable observation (three runners, 10 seconds, 5 miles). The hard call is `analysis` vs `hot_take`, and the fact carries it.
>
> *Which pile:* (a). The rule covered it. I reached for `reaction` because the data was personal.

**6.**
> *The post:* "Anyone who races more than once a month isn't training, they're just collecting medals."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:* Staff is right. Rule 2: "Anyone who races more than once a month…" is a general claim about a group of runners, not a report of what happened to the writer. It's unsupported and confident, which is a `hot_take`.
>
> *Which pile:* (a). Rule 2 covers it directly.

**7.**
> *The post:* "The club needs to stop pretending the Tuesday session is for everyone. It isn't and it never has been."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:* Staff is right. Rule 2 says a post "can be heated and still be `hot_take` if it is making a general claim", and "it isn't and it never has been" is a claim about the club, not the writer's own experience. I labelled it by its frustrated tone.
>
> *Which pile:* (a). The rule names this exact case and I missed it.

**8.**
> *The post:* "Times are down about 3% since the shoe rules changed, so obviously the shoes are the whole story and the sport has a problem."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:* Staff is right. This is the rule 1 example almost word for word: the 3% is decoration and "so obviously" does the work. I called it `reaction`, which isn't even one of the two labels the post is torn between. I think I reacted to "the sport has a problem" sounding like a complaint.
>
> *Which pile:* (a). This is the clearest consistency miss of the 15, since the rule shows this exact post.

**9.**
> *The post:* "Road racing peaked in about 2015 and everything since has been marketing."
>
> *Staff said / I said:* `hot_take` / `analysis`
>
> *My call, and why:* Staff is right. Rule 1: "about 2015" is part of the assertion, not evidence for it. Nothing checkable is offered to show racing peaked, so the year is decoration. I gave the year more weight than it deserved.
>
> *Which pile:* (a). The rule covers it. It's the mirror image of my misses on posts 2–5: here a number I should have ignored, there numbers I should have counted.

**10.**
> *The post:* "Nobody actually enjoys the long run. They enjoy having done it, which is a completely different thing, and the sport would be more honest if it said so."
>
> *Staff said / I said:* `hot_take` / `reaction`
>
> *My call, and why:* Staff is right, even though they marked it HARD. It reads reflective, but rule 2 asks whether the post is about the writer or about the world, and "Nobody actually enjoys the long run" is about everyone. Nothing just happened, so the `reaction` definition ("an immediate response to something that just happened") doesn't fit either.
>
> *Which pile:* (a). I labelled it by its personal, thoughtful tone rather than by what it claims.

**11.**
> *The post:* "Got up at 5, drove ninety minutes, and it's cancelled. Standing in the car park in the rain reading the email."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:* Staff is right. Rule 2: this is entirely what just happened to the writer (5am, ninety-minute drive, standing in the rain reading the email). There's no claim about racing or the world in it, so there's nothing for a `hot_take` to be.
>
> *Which pile:* (a). A plain `reaction` that I mislabelled.

**12.**
> *The post:* "Watching the last 400 of that and I had to stand up. Still standing up actually."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:* Staff is right. The writer reports their own response to something happening now ("I had to stand up. Still standing up actually"). No general claim is made, so rule 2 puts it in `reaction`.
>
> *Which pile:* (a). The rule covers it.

**13.**
> *The post:* "Blew up at 20 with the pace band still in my hand like it was going to help. Rough one."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:* Staff is right. "Blew up at 20… Rough one" is the writer's own race, just finished. The jab at the pace band is about their own band, not a claim that pace bands are useless.
>
> *Which pile:* (a). I may have read the sarcasm as a general claim, but rule 2 asks what the post asserts, and it asserts nothing general.

**14.**
> *The post:* "Third DNF this year. I don't really want to talk about it, just wanted to put it somewhere."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:* Staff is right, even though they marked it HARD. Staff's worry was `analysis` ("third this year" is countable). I said `hot_take`, which is harder to defend: the post makes no claim at all. It's the writer reporting their own state ("just wanted to put it somewhere").
>
> *Which pile:* (a). Rule 2 covers it. Nothing general is asserted.

**15.**
> *The post:* "Just realised the shoes I set every PB in this year are the ones I bought by accident in the wrong size."
>
> *Staff said / I said:* `reaction` / `hot_take`
>
> *My call, and why:* This is the one I'd still argue. Staff call it `reaction` under rule 2, and their own note says it "could be read as a wry hot take about shoe discourse". I read it that way: the point of posting it on a forum that argues endlessly about shoes is the implied claim that the shoe doesn't matter much. On balance I'd concede, because rule 2 asks what the post *says*, and every word is about the writer's own realisation. The claim is only implied, and rule 4 (most words) also points to `reaction`.
>
> *Which pile:* (c). The rule is ambiguous about implied claims, and staff flagged the same reading. My reading is defensible, though I think staff's is slightly better.

**What the pattern in my disagreements tells me:**


14 of my 15 disagreements are pile (a): the staff rule covered the post and I
applied it loosely. Only one (the wrong-size shoes) is a genuine (c). So 50%
mostly measures inconsistency on my part, not ambiguity in the staff set. The
misses follow two habits. First, on `reaction` vs `hot_take` (9 of 15), I
labelled by **tone instead of by subject**: short, blunt first-person posts
became `hot_take`, and frustrated or reflective general claims became
`reaction`. That's the reverse of rule 2, which only asks whether the post is
about the writer or about the world. Second, on `analysis` (6 of 15), I
**discounted personal measurements**: a writer's own split test, heat
comparison or three-runner comparison is still a checkable fact doing the
work, but I didn't count it, while I did count a year that was only
decoration. My own taxonomy draws `reaction` vs `hot_take` with the same rule
(writer vs world), so if I applied it this inconsistently on 30 posts, the
same blur is very likely in my 200 training labels. It's also exactly the
pair my model confuses in both directions.

---

## The Improvement

**What I changed:**
I relabelled `reaction` vs `hot_take` in `labels.csv`, applying one rule
strictly: is the post about the writer's own running or feelings (`reaction`),
or does it claim something about runners or the sport (`hot_take`)? Ignore
tone. I reviewed the 60 rows most likely to be wrong: the 27 tagged "(was
personal)", the 10 tagged "(unsure)", 21 `hot_take` posts written heavily in
the first person, and 2 `reaction` posts full of general words. I changed 7,
all `hot_take` → `reaction` (rows 8, 19, 87, 96, 117, 157, 196). Counts went
from 114 / 48 / 38 to **107 `hot_take` (54%) / 55 `reaction` (28%) / 38
`analysis` (19%)**. Claude suggested a label and a rule-2 reason for each of
the 60 rows (`relabel_review.csv`). I made the final call on every row and
overruled the suggestion twice (rows 6 and 196). Nothing else changed: same
model, same settings, same three seeds.

*How it was run:* the notebook kernel ran out of memory partway through
section 6 (8 GB Mac, every seed's model stays loaded). The after-run used
`run_seeds.py`, which runs section 6 one seed per process using the
notebook's own functions and settings, read straight from `takemeter.ipynb`.

**Which diagnosis pointed at it:**
The criterion 4 diagnosis. 9 of my 15 staff disagreements were `reaction` vs
`hot_take`, 8 of them pile (a), and they went in both directions. The model's
biggest confusion across the three seeds was the same pair, also in both
directions (10 / 7 summed). That pointed at inconsistent labels on this
boundary rather than at the model, so I fixed the labels and left the model
alone.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | >= 0.65 on every seed | 0.73 | 0.63 | 0.80 | MISSED (seed 7 short by 0.02; was 0.57) |
| 2. Macro F1 | >= 0.50 on every seed | 0.73 | 0.58 | 0.77 | MET (was MISSED) |
| 3. `analysis` / `reaction` F1 | each >= 0.40 on every seed | 0.57 / 0.88 | 0.40 / 0.67 | 0.73 / 0.71 | MET, just (seed 7 `analysis` is exactly 0.40; was MISSED) |
| 4. Staff agreement | >= 21/30 | 15/30 | 15/30 | 15/30 | MISSED (unchanged; this fix didn't touch the staff set) |
| 5. Confidence gap | >= 0.15 on every seed | 1.00 − 0.50 = 0.50 | 0.70 − 0.70 = 0.00 | 0.90 − 0.60 = 0.30 | MISSED (seed 7 has no gap; was MET) |

| Measure | Before (42 / 7 / 2024) | After (42 / 7 / 2024) |
|---|---|---|
| Accuracy | 0.70 / 0.57 / 0.63 | 0.73 / 0.63 / 0.80 |
| Macro F1 | 0.66 / 0.49 / 0.57 | 0.73 / 0.58 / 0.77 |
| F1 `analysis` | 0.67 / 0.33 / 0.67 | 0.57 / 0.40 / 0.73 |
| F1 `hot_take` | 0.76 / 0.71 / 0.74 | 0.73 / 0.69 / 0.88 |
| F1 `reaction` | 0.55 / 0.43 / 0.31 | 0.88 / 0.67 / 0.71 |

Confusion matrix summed over the three seeds (90 test predictions each):

| true \ predicted | Before: analysis | hot_take | reaction | After: analysis | hot_take | reaction |
|---|---|---|---|---|---|---|
| analysis | 10 | 6 | 2 | 10 | 7 | 1 |
| hot_take | 5 | 39 | 7 | 6 | 37 | 5 |
| reaction | 3 | 10 | 8 | 1 | 5 | 18 |

**Did it help, and how do I know:**


Yes, on the boundary I targeted, and clearly enough that it isn't seed noise.
`reaction` F1 went up on **every** seed (0.55→0.88, 0.43→0.67, 0.31→0.71).
Summed over the three seeds, `reaction`↔`hot_take` errors fell from 17 to 10,
and `reaction` posts correctly found went from 8 of 21 to 18 of 24. Macro F1
rose on every seed, so criteria 2 and 3 went from MISSED to MET. The
`analysis` row barely moved (10 right both times; `analysis`↔`hot_take`
errors 11 → 13), which is what I'd expect from a fix that didn't touch
`analysis`. That makes it more believable that the gain comes from the
relabelling, not luck.

Two caveats keep me from claiming more:
1. **The test sets aren't the same posts as before.** Changing labels changes
   the stratified split. Each test set now has 8 `reaction` and 16 `hot_take`
   instead of 7 and 17. And 2 of the 7 relabelled posts landed in the test
   split on seeds 7 and 2024 (0 on seed 42). So part of the gain is that the
   test labels themselves are now more consistent, which is partly the point,
   but it's not a pure same-posts comparison. Seed 42 had no relabelled test
   posts and still saw `reaction` F1 rise from 0.55 to 0.88, which suggests
   the training-side fix did real work.
2. **Seed 7 is still the weak split.** Accuracy 0.63 misses criterion 1 by
   one post. On that seed the confidence gap disappeared (0.70 vs 0.70), so
   criterion 5 went from MET to MISSED. With 10 posts per third, one or two
   posts decide that gap. Accuracy still moves 0.17 across seeds, so the
   small-test-set problem from my diagnosis hasn't gone away. Relabelling
   wasn't meant to fix it.

---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->


Three criteria are still missed after the fix. Criteria 1 and 5 fail only on
seed 7, and criterion 4 hasn't moved.

**Criterion 1: accuracy (seed 7 is 0.63, target 0.65).**
Seed 7 got 19 of 30 right; it needed 20. Most of its errors are `analysis`:
it found only 2 of its 6 `analysis` posts and called 4 of them `hot_take`.
*What I'd do:* collect and label about 40 more `analysis` posts, so the label
has around 55 training examples instead of 27, and around 12 in each test
split instead of 6. I'd also report accuracy over 5-fold cross-validation, so
one unlucky split of 30 posts can't decide the verdict.
*Why I stopped:* the milestone asks for one fix, and I spent it on the
`reaction` vs `hot_take` boundary my diagnosis pointed at most strongly. New
`analysis` posts need collecting from LetsRun threads and labelling under rule
1, which is the boundary I'm least consistent on. Rushing that would add
noisy labels, not better ones.

**Criterion 4: staff agreement (15/30, target 21/30).**
This one can't be fixed by re-doing the same 30 posts. I've now seen the
staff answers, so a second attempt would measure memory, not consistency.
*What I'd do:* turn my Milestone 3 findings into a written checklist (rule 2:
ask "writer or world?", ignore tone; rule 1: count a personal measurement as
a fact if it carries the argument), then label a fresh batch of about 30
posts I've never seen and have a classmate label the same batch blind. Our
agreement on that batch would show whether the checklist fixed the habit.
*Why I stopped:* there's no second staff set to test against, and finding an
independent second labeller was out of scope for this unit.

**Criterion 5: confidence gap (seed 7 is 0.00, target 0.15).**
On seed 7 the most and least confident thirds both scored 0.70, and the
model's average confidence was the same whether it was right or wrong (0.868
vs 0.868). So on that split, its confidence told you nothing. Seeds 42 and
2024 still have clear gaps (0.50 and 0.30), and before the fix all three
seeds passed.
*What I'd do:* look at seed 7's confidently-wrong posts. I expect them to be
`analysis` posts called `hot_take` with high confidence, which would make
this the same `analysis` problem as criterion 1. I'd also measure the gap on
a larger test set, because with 10 posts per third, two posts swinging the
other way erases a 0.20 gap.
*Why I stopped:* I can't tell a real loss of calibration from noise on 10
posts per third, and the fix that would settle it (more data, cross-
validation) is the same as for criterion 1.

**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->

I meant `analysis` to mean "a checkable fact carries the argument", but the
model never learned that: summed over the three after-seeds it got only 10 of
18 `analysis` posts right and called 7 of them `hot_take`, no better than
before relabelling, while `reaction`, once I sharpened it to "about the
writer, not the world", jumped from 8 of 21 to 18 of 24. On LetsRun almost
every post contains a time or a split, so "has a number" can't separate
`analysis` from `hot_take`, and 27 training examples aren't enough for the
model to learn whether the number is doing the work.

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [x] criteria.md has five numbered criteria, each naming a NUMBER
       [x] Each has a reason underneath tied to your data or taxonomy
       [x] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [x] No label above 70%
       [x] All five unit 5 sections have real content
       [x] Label Taxonomy includes the decision rule for your hardest boundary
       [x] The Dataset includes three hard cases
       [x] results.json and test_split.csv committed (the notebook does this)
       [x] At least four new commits
       [x] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [x] Baseline vs. Trained table, with your prediction written beforehand
       [x] Run Log — Before, five criteria across three seeds
       [x] Confusion matrix TYPED AS A MARKDOWN TABLE
       [x] A verdict on every criterion
       [x] A diagnosis for every miss, using the agreement report as evidence
       [x] Agreement Report with every disagreement adjudicated
       [x] One improvement, with Run Log — After
       [x] What's Still Broken
       [x] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [x] At least four new commits
       [x] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
