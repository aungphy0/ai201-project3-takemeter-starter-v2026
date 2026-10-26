# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy

Overall accuracy on the held-out test split is **at least 0.65 on every one of
the three seeds**.

**Why this target:** `hot_take` is 114 of my 200 posts (57%), so a model that
calls everything a hot take already scores about 0.57. On a 30-post test split,
0.65 means getting roughly 20 right instead of 17, so it has to correctly catch
at least a few `analysis` or `reaction` posts. Anything lower would mean the
fine-tuning added almost nothing over guessing the biggest label.

---

## 2. Macro F1

Macro F1 on the test split is **at least 0.50 on every seed**.

**Why this target:** accuracy hides the minority labels. The "always hot_take"
guesser has a macro F1 of only about 0.24 (0.73 for `hot_take`, 0 for the other
two). Requiring 0.50 means the model has to be doing real work on `analysis`
and `reaction`, not just riding the majority label.

---

## 3. The two small labels

`analysis` and `reaction` each have an **F1 of at least 0.40 on every seed**.

**Why this target:** these are my smallest labels: 38 `analysis` (19%) and 48
`reaction` (24%) posts. With a stratified 15% test split, that's only about 6
`analysis` and 7 `reaction` posts in test, so one wrong post moves recall by
about 15 points. I set this looser than criterion 1 because a score computed on
6 posts will jump between seeds. 0.40 is still clearly above zero, which is
where these labels would sit if the model learned to ignore them.

---

## 4. Agreement with the staff labels

When I label the 30 staff posts under the staff taxonomy, I agree with staff on
**at least 21 of 30 (70%)**.

**Why this target:** my hardest boundary is `analysis` vs `hot_take`: whether a
number in the post actually carries the argument or is just decoration.
LetsRun posts are full of times and splits, so I have to make this call on
almost every post. In my own cold 20, I tended to call advice or questions
`analysis` even when no checkable fact did the work. The staff notes say the
ambiguous set makes the 70s normal, so 70% is a fair bar. Below it, I'd treat my
own 200 labels as inconsistent rather than blame the model.

---

## 5. Confidence means something

On every seed, accuracy on the model's **most confident third** of test posts
is **at least 0.15 higher** than accuracy on its **least confident third**.

**Why this target:** if the model is to be useful for sorting real LetsRun
threads, a confident prediction has to be more trustworthy than an unsure one.
Many of my posts mix a feeling with a number (e.g. reacting to a race result
while quoting the time), so I expect those to be the low-confidence ones. A
0.15 gap is 1–2 more correct posts out of the 10 in each third. If the
gap is zero, the confidence score tells a reader nothing.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
