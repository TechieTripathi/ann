---
layout: section
chapter: '1 · Which number?'
---

# Chapter 1

## Which number?

<div v-click class="thesis" style="margin-top:0.8em">You cannot descend a hill you have not agreed to measure.</div>

<!--
Twenty seconds. State the thesis and move.

Frame it as debt collection, because it is: "Last lecture I put a slide up
called 'The Loss Function: measuring how wrong', and I said — I can quote
myself — 'the exact formula is a detail for a later, more technical
lecture.' Welcome to the later, more technical lecture."

Transition: "So let's not start with a formula. Let's start with the
requirements a formula has to satisfy, and see what falls out."
-->

---
chapter: '1 · Which number?'
clicks: 5
---

# What a loss function has to be

<span class="eyebrow math">Math</span>

<div class="key-message" style="margin-top:-0.8em">Three requirements. Squared error is the simplest thing that meets all three.</div>

<div class="reqs">
  <div v-click="1"><span class="rn">1</span><div><b>One number</b><span>You cannot descend in two directions at once. However many outputs the network has, the loss collapses them to a single scalar.</span></div></div>
  <div v-click="2"><span class="rn">2</span><div><b>Smallest when right</b><span>Minimising it has to mean improving. If a perfect prediction doesn't sit at the minimum, you are optimising the wrong thing.</span></div></div>
  <div v-click="3"><span class="rn">3</span><div><b>Differentiable in every weight</b><span>Nudge any weight by a hair, and the loss must move by a measurable amount — otherwise it cannot tell you <i>which way to go</i>.</span></div></div>
</div>

<div v-click="4" class="statement-box" style="margin-top:0.0em">

$$E = \tfrac{1}{2}\sum_{k}(t_k - o_k)^2$$

</div>

<div v-click="5" class="compact-callout">

<Callout>
  <template #misconception>We could just use accuracy — the percentage the network got right — as the loss.</template>
  <template #clarification>Accuracy is a <b>step</b> function of the weights. Nudge a weight by 0.0001 and accuracy does not move <i>at all</i> — until it suddenly jumps. Its derivative is zero almost everywhere and undefined at the jumps, so it can never tell you which way to go. Accuracy is a <b>metric</b>, for reporting to humans. Loss is what you <b>optimise</b>.</template>
</Callout>

</div>

<style>
.reqs { display: flex; flex-direction: column; gap: 0.3em; margin: 0.4em 0; }
.reqs > div { display: flex; align-items: flex-start; gap: 0.8em; }
.rn {
  flex-shrink: 0; width: 1.7em; height: 1.7em; border-radius: 999px;
  background: var(--ann-circuit-soft); color: var(--ann-circuit);
  font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 0.85rem;
  display: flex; align-items: center; justify-content: center;
}
.reqs b { font-family: 'Space Grotesk', sans-serif; font-size: 0.9rem; display: block; line-height: 1.3; }
.reqs span:last-child { font-size: 0.78rem; color: var(--ann-ink-soft); line-height: 1.35; }
.slidev-layout .statement-box { padding: 0.15em 1em; }
.statement-box :deep(.katex-display) { margin: 0.3em 0; font-size: 0.95em; }
.slidev-layout .key-message { margin: 0.4em 0 0.45em; }
.compact-callout :deep(.callout) { font-size: 0.78rem; }
.compact-callout :deep(.callout-row) { padding: 0.45em 0.9em; }
</style>

<!--
Derive, don't enumerate. This slide exists so that the formula arrives as a
consequence rather than as an announcement.

Click 1 (one number): "Suppose I gave you two loss numbers, one per output.
Which do you minimise? You'd have to combine them anyway — so combine them
up front." Note this also answers why we SUM over outputs.

Click 2 (smallest when right): sounds trivially obvious; it is not. Point
out that plenty of plausible-sounding formulas fail it.

Click 3 (differentiable) — SLOW DOWN. This is the one they have never been
told, and it is the load-bearing requirement for the entire lecture. Last
lecture I described loss as "a finer-grained, differentiable number" and
never explained the word. Explain it now: the whole method depends on
asking "if I wiggle this weight, what happens to the loss?" If the answer
is "nothing, nothing, nothing, then suddenly everything", you have no
signal to follow.

Click 4 (the formula): now it lands as the obvious candidate. Square the
gap: always positive (so errors can't cancel), smooth everywhere, and big
misses hurt superlinearly. The one-half is not a fudge — it is there so the
2 from differentiating the square cancels, leaving ∂E/∂o = o − t exactly.
Say that now, cheaply: you will use that derivative on slide 19, and the
half is the only reason it comes out clean.

Flag it as the loss of record: "This is the loss we will actually use for the
worked example in Chapter 4. Write it down."

Click 5 (callout): read both halves. Ask first: "Why not just use accuracy?"
Let someone try to answer before revealing. Students find the step-function
argument genuinely satisfying.

Likely student question: "Why not the absolute value |t - o| instead of the
square?" Answer: "Good instinct, and it's used — it's called L1 loss. But
it isn't differentiable at exactly zero, which is precisely where you end
up when the model gets good. The square is smooth everywhere."

Transition: "That's regression. Classification wants a different ruler."
-->

---
chapter: '1 · Which number?'
clicks: 4
---

# Classification wants a different ruler

<span class="eyebrow math">Math</span>

<div v-click="1" class="key-message">Cross-entropy doesn't ask "how far off were you." It asks "how much probability did you put on the truth?"</div>

<div v-click="2">

$$E = -\sum_k \Big[\, t_k \log o_k \;+\; (1-t_k)\log(1-o_k) \,\Big]$$

</div>

<div v-click="3" class="ce-read">
  <div><span class="lbl">when the truth is 1</span><span class="frm">−log(o)</span><span class="txt">predict 0.99 → tiny loss. Predict 0.01 → <b>enormous</b> loss.</span></div>
  <div><span class="lbl">when the truth is 0</span><span class="frm">−log(1−o)</span><span class="txt">symmetric: confident and wrong is punished without limit.</span></div>
</div>

<div v-click="4" class="transition-line">Why this is the right choice for classification is a <b>gradient</b> argument — and you cannot read a gradient yet. <span class="arrow">Chapter 5, with these exact numbers. I'll come back for this.</span></div>

<style>
.ce-read { display: flex; flex-direction: column; gap: 0.4em; margin-top: 0.5em; }
.ce-read > div { display: flex; align-items: baseline; gap: 0.8em; font-size: 0.85rem; }
.lbl { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--ann-muted); flex: 0 0 11em; }
.frm { font-family: 'JetBrains Mono', monospace; color: var(--ann-circuit); flex: 0 0 6em; }
.txt { color: var(--ann-ink-soft); }
</style>

<!--
Do not derive cross-entropy from information theory today. It costs ten
minutes and buys nothing they can use this hour. Teach it as a reading
exercise.

Click 1: the conceptual difference. Squared error treats the output as a
*quantity* and measures distance. Cross-entropy treats it as a *probability*
and measures surprise. Same network, different question.

Click 2 (the formula): it looks worse than it is. Point out that for any
single output, one of the two terms is always zero, because t is either 0
or 1. So really it is just "-log of the probability you assigned to the
right answer."

Click 3: read the two rows. The key property to land: as your confidence in
the wrong answer approaches certainty, the loss goes to INFINITY. Squared
error caps out at 1. Cross-entropy does not. "Being confidently wrong is
unboundedly bad" is exactly the attitude you want in a classifier.

Click 4 — MAKE THE PROMISE LOUDLY, and make it specific. Not "we'll see
later" but "Chapter 5, with these exact numbers." Then actually pay it on
slide 26.

Be clear about which loss we are about to use, so nobody is confused in
Chapter 4: "We are going to do the worked example with squared error, not
cross-entropy — it is the loss you have just derived, and its gradient shows
you more of the machinery. Chapter 5 comes back and shows you exactly what
that choice cost us." The students should notice you doing this; the whole deck is
built on cashing promises, and doing it inside a single lecture teaches
them to trust the pattern.

Likely student question: "Can I use cross-entropy for regression?" Answer:
"No — it expects outputs in (0,1) that behave like probabilities. Use
squared error for regression, cross-entropy for classification. The real
rule, which we'll sharpen in Chapter 5, is: match the loss to the output
activation."

Transition: "We have a number. Now — which direction?"
-->
