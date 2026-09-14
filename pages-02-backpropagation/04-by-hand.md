---
layout: section
chapter: '4 · Backpropagation by hand'
---

# Chapter 4

## Backpropagation by hand

<div v-click class="thesis" style="margin-top:0.8em">Eight weights, four biases, one example. By hand, once — so you never have to wonder again.</div>

<!--
Set expectations honestly: this is the longest chapter, it is arithmetic,
and it is the reason the lecture exists. Tell them what the payoff is:
"After this chapter, there is nothing left in backpropagation that is hidden
from you. Next lecture, when a framework does this in one line, you will
know precisely what that line did — because you will have done it yourself."

Tell them not to copy the digits. The numbers are on the slides and in the
repository; what they should watch is the PATTERN, which repeats.

Transition: "Here is the network. Every number we need is on one slide."
-->

---
chapter: '4 · Backpropagation by hand'
clicks: 4
---

# The setup

<span class="eyebrow structure">Structure</span>

<div class="key-message">Two inputs, two hidden, two outputs, sigmoid everywhere. MSE loss, η = 0.5.</div>

<BackpropTrace stage="setup" :from="1" style="margin-top:-2.5em"/>

<!--
This slide teaches the reading conventions that carry the next seven slides.
Spend a full minute here; it buys the rest of the chapter.

Click 1 (inputs and targets): note the shapes — inputs and targets are
SQUARES because they are data. Circles are computation. Nobody has to ask
whether an input "has an activation."

Click 2 (weights): eight of them, on the edges, in teal.

Click 3 (biases): four of them, drawn as DASHED HOLLOW chips so they never
read as weights. Say the important part explicitly, because it is the most
common question this slide gets:

"Every neuron has its OWN bias. There are four here, not two. b for h1 and b
for h2 are separate parameters that happen to START at the same value, 0.35 —
and likewise 0.60 for the two output neurons. They are not one shared number
printed twice."

Pre-empt the obvious follow-up — 'if they're identical, why not just use one?'
Answer: "Because they will not stay identical. Watch them on slide 20. The two
output biases get gradients of +0.7514 and −0.2271 — opposite signs. After a
single update, [0.60, 0.60] becomes [0.5308, 0.6190]. One falls, one rises.
They were never the same parameter; they just started in the same place."

Worth naming the lineage here too: the classic textbook version of this example
really does share a single scalar bias per layer. We do not, because that is
not what a real network does — in PyTorch, nn.Linear gives every neuron its own
bias, and so does every framework you will meet.

Click 4 (the legend) — TEACH THIS EXPLICITLY, then never mention it again:
  teal   = forward, what the network computes
  ember  = backward, what the loss demands
  indigo = the update, where the two meet
And the fixed positions: above a neuron is net (the weighted sum), inside is
out (the activation), below is delta (the blame), to the right is the bias.
Tell them directly: "If you lose the thread at any point in the next twenty
minutes, you can decode any number on screen from its position and its
colour alone."

CITE THE SOURCE, because they will Google it: "The weights and inputs here
are from Matt Mazur's step-by-step backpropagation example, which is the
most-copied worked example on the internet — you can and should look it up
tonight. One difference: he uses squared error with soft targets of 0.01 and
0.99, and so are we. Every WEIGHT gradient on the next six slides matches
his published numbers to the digit — tell them that, and tell them to go and
check it tonight. Being able to verify a lecture against an independent
source is worth more than taking it on trust.

ONE deliberate difference, and you must state it or a checker will think you
are wrong: Mazur holds the biases FIXED. We update them, because they are
parameters like any other. That changes nothing about the weight gradients,
but it does change the loss after one step —
    Mazur (weights only)      0.2910
    ours  (weights + biases)  0.2805

Name the loss out loud, because the whole backward pass depends on it:
'We are using mean squared error — L equals one half the sum of (output minus
target) squared. The one half is there so that the 2 from differentiating the
square cancels, which makes dL/do exactly (o minus t). Chapter 1 derived this
loss; now we use it.'"

MUST SAY if you skipped the learning-rate slide: η = 0.5 is enormous by
modern standards (you'd normally see 0.001 to 0.1). It is chosen so that one
step visibly moves the numbers on a slide.

Transition: "Forward pass. Hidden layer first."
-->

---
chapter: '4 · Backpropagation by hand'
clicks: 5
---

# Forward: the hidden layer

<span class="eyebrow forward">Forward</span>

<div class="key-message" style="margin-top:-1em">Weighted sum, add the bias, squash. Twice. That is the whole hidden layer.</div>

<BackpropTrace stage="forward-hidden" :from="1" compact style="margin-top:-2em"/>

<div class="calc-strip">
  <div v-click="2" class="calc-chip fwd"><span class="lbl">net h1</span>0.15(0.05) + 0.20(0.10) + 0.35 = 0.3775</div>
  <div v-click="3" class="calc-chip fwd"><span class="lbl">out h1 = σ(net)</span>1 / (1 + e<sup>−0.3775</sup>) = 0.5933</div>
</div>

<!--
Click 1: h1's two incoming edges light up; the output layer dims. One neuron
at a time.

Click 2 (net_h1): read the arithmetic off the strip below the diagram, not
out of the picture. Each input times its weight, plus the bias. This is
exactly the z = wᵀx + b from last lecture — same formula, now with numbers
in it.

Click 3 (out_h1): apply the sigmoid. 0.3775 goes in, 0.5933 comes out. Note
it barely moved: sigmoid is roughly linear near zero, and 0.3775 is near
zero. Worth flagging — it foreshadows the saturation discussion in Ch 5.

Click 4 (h2, both numbers at once) — DELIBERATELY ONE CLICK. Say so:
"h2 is the same calculation with different weights. I'm not going to walk
it; if you can do h1 you can do h2." The collapse itself signals "this is a
repeat, don't re-derive it in your head." Doing otherwise wastes two minutes
and teaches nothing.

Click 5: un-dim. Both hidden activations are now on screen and they stay
there — we will need them as multiplicands in the backward pass.

Likely student question: "Why sigmoid and not ReLU?" Answer: "Two reasons.
Sigmoid's derivative is clean to compute by hand, and it makes Chapter 5's
point about vanishing gradients visible with real numbers. In a modern
network these hidden layers would almost certainly be ReLU — and slide 26
explains exactly why."

Transition: "Same operation again, one layer along."
-->

---
chapter: '4 · Backpropagation by hand'
clicks: 5
---

# Forward: the output layer, and the number we minimise

<span class="eyebrow forward">Forward</span>

<div class="key-message" style="margin-top:-1.8em">Identical arithmetic — and then one number that judges the whole network.</div>

<BackpropTrace stage="forward-output" :from="1" compact style="margin-top:-2em" />

<div class="calc-strip" style="display:flex; justify-content:center">
  <div v-click="4" class="calc-chip"><span class="lbl">targets</span>t₁ = 0 &nbsp; t₂ = 1</div>
  <div v-click="5" class="calc-chip upd"><span class="lbl">MSE, summed over outputs</span>E = 0.2984</div>
</div>

<style>
.calc-chip.upd { background: var(--ann-indigo-soft); border-color: var(--ann-indigo); }
</style>

<!--
Clicks 1-3: exactly the same narration as the hidden layer, deliberately
faster. The point to make out loud: "Notice I am not teaching you anything
new. Every neuron in every layer does the identical thing. That is what we
meant last lecture when we said a network is one neuron, repeated."

Click 4 (targets): the true labels appear. Emphasise these are available
during TRAINING — that is what makes this supervised learning.

Click 5 (the loss): E = 0.2984. Write it out once, out loud:
E = ½[(0.7514 − 0.01)² + (0.7729 − 0.99)²] = ½[0.5496 + 0.0471] = 0.2984.
Pause here. "This single number is the entire target of everything that
follows. Every one of the next three slides exists to make it smaller."

Worth a footnote if anyone is checking along: compute this from the FULL
precision outputs, not the four decimals on screen. The rounded values give
0.29840, which is close enough to look right and wrong enough to be annoying
if a student diffs it against the script."

Ask the class to eyeball it before moving on: o₁ = 0.7514 but should be 0.
o₂ = 0.7729 but should be 1. Which output is more wrong? o₁, badly — it is
confidently wrong in the wrong direction. Watch what the gradients do about
that; it shows up immediately on the next slide.

Likely student question: "Is 0.2984 good or bad?" Answer: "Meaningless in
isolation — loss values are only interpretable as a trajectory. What matters
is that it goes down. By the end of this chapter it will be 0.2805 after a
single step, and near zero after a few thousand."

Transition: "Now the backward pass. And we start at the end, because the end
is the only place we actually know anything."
-->

---
chapter: '4 · Backpropagation by hand'
clicks: 6
---

# Blame: start at the end

<span class="eyebrow backward">Backward</span>

<BackpropTrace stage="delta-output" :from="1" compact style="margin-top:-1em"/>

<div class="calc-strip">
  <div v-click="2" class="calc-chip bwd"><span class="lbl">how wrong &nbsp;∂E/∂out</span>o − t = 0.7514 − 0.01 = <b>0.7414</b></div>
  <div v-click="3" class="calc-chip bwd"><span class="lbl">how responsive &nbsp;∂out/∂net</span>o(1−o) = <b>0.1868</b></div>
</div>

<div v-click="4" class="delta-box">

$$\delta_{o1}\;=\;\frac{\partial E}{\partial out}\cdot\frac{\partial out}{\partial net}\;=\;(o-t)\;\times\;o(1-o)\;=\;0.7414 \times 0.1868\;=\;\mathbf{0.1385}$$

</div>

<div v-click="6" class="key-message" style="margin-top:0.25em; font-size:0.98rem">Blame at the output is <b>how wrong</b> × <b>how responsive</b>. Both factors survive.</div>

<style>
.delta-box {
  background: var(--ann-ember-soft); border-left: 4px solid var(--ann-ember);
  border-radius: 0.5em; padding: 0 1em; margin-top: 0.4em;
}
.delta-box :deep(.katex-display) { margin: 0.3em 0; font-size: 0.86em; }
/* this slide carries a diagram, a calc strip, an equation AND a takeaway,
   so the trace gets less room than on its sibling slides.
   :deep() is required - .bptrace lives inside a scoped child component. */
.bptrace :deep(svg) { max-height: 27vh !important; }
</style>

<!--
This slide is the chain rule from Chapter 3, with numbers in it — exactly two
factors, and you should name them with the same words you used there.

Click 1: the forward numbers fade to 35% — still true, no longer the point —
and an ember arrow appears coming back from the target. Say: "We are turning
around. Everything from here is ember."

Click 2 (how wrong): ∂E/∂out. Because the loss is ½(o − t)², the 2 comes down
and cancels the ½, leaving simply o − t = 0.7514 − 0.01 = 0.7414. Say that explicitly — it is
the entire reason the ½ was put there in Chapter 1.

Click 3 (how responsive): the sigmoid derivative, out(1 − out) = 0.1868. This
is the "how responsive is this neuron" factor from slide 12.

Click 4 (THE PRODUCT): multiply them. 0.7414 × 0.1868 = 0.1385. Stress that
BOTH factors survive: "The neuron was badly wrong — 0.74 out. But it is also
fairly insensitive right now; nudging its weighted sum barely moves its
output. So the blame that actually reaches the weights is much smaller than
the error: 0.14, not 0.74."

That second factor is the one to dwell on, because it comes back to bite us
in Chapter 5. Plant it now: "Notice we just multiplied by a number less than
a quarter. Remember that."

Click 5: δ_o2 = (0.7729 − 0.99) × 0.1755 = −0.0381. One click, it's a repeat.
NOTE THE SIGN and flag it now: "It is negative, and that matters later."

Click 6: the key message.

TERMINOLOGY — disown the bad name here: "You will see δ called the 'error
term'. It is not an error. It is a sensitivity — ∂E/∂net, how much the total
loss responds to this neuron's weighted sum. A hidden neuron has no target,
so it cannot possibly have an error. The name is a historical accident. I'm
going to call it BLAME all lecture."

Likely student question: "Could that σ′ factor ever disappear?" Answer:
"Yes — and this is worth remembering. Pair a sigmoid output with cross-entropy
instead of squared error and the o(1−o) cancels algebraically, leaving δ = o − t
with no second factor at all. That is not a trick; it is why that pairing is
standard for classification. Slide 26 shows exactly what it buys you."

Second likely question: "Is δ the same as the error?" No — see the terminology
note below. The error here is 0.7414; the blame is 0.1385. They are different
numbers and conflating them will cost you later."

Transition: "One neuron's blame gives us four weight gradients immediately."
-->

---
chapter: '4 · Backpropagation by hand'
clicks: 5
---

# Four gradients, and a gift

<span class="eyebrow backward" >Backward</span>

<BackpropTrace stage="grad-output" :from="1" compact style="margin-top:-3em"/>

<div v-click="3" class="calc-strip">
  <div class="calc-chip bwd"><span class="lbl">the pattern</span>∂E/∂w &nbsp;=&nbsp; δ<sub>target</sub> &nbsp;×&nbsp; out<sub>source</sub></div>
  <div class="calc-op">→</div>
  <div class="calc-chip bwd"><span class="lbl">∂E/∂w₅</span>0.1385 × 0.5933 = <b>0.0822</b></div>
</div>

<div v-click="5" class="key-message" style="margin-top:0.4em">A weight's gradient is its own blame times what it was multiplying. A bias multiplies <b>1</b> — so a bias gradient <i>is</i> the blame.</div>

<!--
Click 1 (w5): the gradient appears on the target side of the w5 edge.
Derive it out loud from the chain rule slide: ∂E/∂w5 = δ_o1 × ∂net_o1/∂w5,
and ∂net_o1/∂w5 is just out_h1, because in the weighted sum w5 multiplies
out_h1 and nothing else. So: blame times what it multiplied —
0.1385 × 0.5933 = 0.0822.

Click 2: the other three at once. Repeat, no re-derivation.

Click 3 (the pattern): state the general shape. This one line covers every
weight in the network, in every layer. Nothing new will be needed.

Click 4 (THE GIFT — the biases): this is the payoff. What does a bias
multiply? Nothing — it is added unconditionally, so ∂net/∂b = 1. Therefore
∂E/∂b = δ × 1 = δ. The bias gradient IS the blame, already sitting there.
Point at the connectors drawn from each δ label to its bias chip: same
number, twice.

THE PER-NEURON POINT, PROVED. This is the moment to settle any lingering
doubt from slide 16 that the biases are really separate parameters: "These two
output biases started at exactly the same value, 0.60 and 0.60. Look at their
gradients: +0.1385 and −0.0381. Not just different — opposite in sign. Apply
the update rule and 0.60 goes to 0.5308 while the other 0.60 goes to 0.6190.
One neuron wants to fire less, the other wants to fire more. A single shared
bias could not express that."

CASH THE LECTURE 1 DEBT HERE, out loud: "Last lecture someone asked whether
bias is learned the same way as weights, and I said 'yes, identically, it's
just one more number adjusted by backpropagation.' There it is. Identical
treatment, and in fact easier — the bias gradient needs no multiplication at
all."

(Note: the bias slide in Lecture 1 was cut for time, so for most of the room
this arrives as new information rather than as a promise being kept. Either
way it lands.)

Click 5: the key message.

Likely student question: "So why have a bias at all, if it's so trivial?"
Answer: "Because without it every neuron is forced to output σ(0) = 0.5 when
its inputs are all zero. The bias is what lets a neuron have a baseline
other than dead-centre. It shifts the decision boundary."

Transition: "That was the easy layer — we knew the target. Now the hard one,
where there is no target at all."
-->

---
chapter: '4 · Backpropagation by hand'
clicks: 7
---

# A hidden neuron is blamed by everyone it feeds

<span class="eyebrow backward">Backward</span>

<BackpropTrace stage="delta-hidden" :from="1" compact style="margin-top:-2em"/>

<div class="calc-strip">
  <div v-click="2" class="calc-chip bwd"><span class="lbl">via o₁</span>0.1385 × 0.40 = <b>+0.0554</b></div>
  <div v-click="3" class="calc-chip bwd"><span class="lbl">via o₂ &nbsp;— opposite sign</span>−0.0381 × 0.50 = <b>−0.0190</b></div>
  <div v-click="4" class="calc-op">=</div>
  <div v-click="4" class="calc-chip bwd"><span class="lbl">∂E/∂out h1</span><b>+0.0364</b></div>
</div>

<div v-click="7" class="key-message" style="margin-top:0.25em; font-size:0.98rem">δ<sub>h</sub> = ( Σ<sub>downstream</sub> δ·w ) × σ′(net) — <b>the only new idea in backpropagation.</b></div>

<!--
THE CROWN JEWEL. Slow right down. Everything in Chapter 3 was built so that
this slide is recognition rather than discovery.

Click 1: everything dims except h1 and its two OUTGOING edges. Say: "h1 has
no target. Nobody ever told us what h1 should have output. So where can its
blame possibly come from?" Let that sit. Answer: "From the neurons it fed."

Click 2 (path via o₁): o₁'s blame, times the weight connecting them. +0.0554.
"o₁ is saying: you pushed me too high. Turn down."

Click 3 (path via o₂) — POINT AT THE SIGN: −0.0190. "o₂ is saying the
opposite. Turn UP. These two neurons genuinely disagree about what h1 should
have done."

Click 4 (the sum): +0.0554 + (−0.0190) = +0.0364. "The gradient is not
either neuron's opinion. It is the argument's verdict. o₁ won — but by less
than it wanted."

This is exactly the fan-out picture from slide 13, now with numbers. Say so.

Click 5: multiply by h1's own responsiveness, σ′(net_h1) = 0.2413, to get
δ_h1 = 0.0088. Same "how responsive" factor as the output layer — nothing
new, and note it is the SECOND time we have multiplied by a σ′ on the way
back. That is the whole of Chapter 5 in one observation.

Click 6: δ_h2 = 0.0100, one click, repeat.

Click 7 (the recursion): state it, and state its significance. "Look at the
shape of that formula. To get a hidden layer's blame, you need the blame of
the layer AFTER it. Which needs the blame of the layer after THAT. So you
compute them back to front — output layer first, then one layer at a time
towards the input. That ordering is the entire algorithm. That is why it is
called BACKpropagation."

Point out the gradients now shrink: δ_o ≈ 0.138, δ_h ≈ 0.0088. Roughly 16×
smaller one layer back. Don't explain it yet — just plant it: "Notice the
blame got much smaller going back one layer. Hold that thought for twenty
minutes."

Note: this slide deliberately has no Callout. The sum-over-paths idea is the
key message, not an aside; boxing it would demote it.

Transition: "Every gradient is now available. Let's take the step."
-->

---
chapter: '4 · Backpropagation by hand'
clicks: 6
---

# Ten gradients, one step

<span class="eyebrow structure">The update</span>

<BackpropTrace stage="update" :from="1" compact style="margin-top:-4em"/>

<div v-click="5" class="calc-strip">
  <div class="calc-chip upd"><span class="lbl">w₅ &nbsp;gradient +0.0822</span>0.40 → <b>0.3589</b> &nbsp;(down)</div>
  <div class="calc-chip upd"><span class="lbl">w₇ &nbsp;gradient −0.0226</span>0.50 → <b>0.5113</b> &nbsp;(<b>up</b>)</div>
  <div class="calc-chip"><span class="lbl">every other parameter</span>moves in the same instant</div>
</div>

<div v-click="6" class="ladder">
  <div class="lh">Loss, if we keep going</div>
  <table class="lt">
    <tr><th>steps</th><td>0</td><td>1</td><td>2</td><td>10</td><td>100</td><td>1 000</td><td>10 000</td></tr>
    <tr><th>E</th><td>0.2984</td><td class="hi">0.2805</td><td>0.2619</td><td>0.1255</td><td>0.0061</td><td>0.0003</td><td>2.4e-6</td></tr>
  </table>
</div>

<style>
.ladder { margin-top: 0.4em; }
.calc-chip.upd { background: var(--ann-indigo-soft); border-color: var(--ann-indigo); }
.lh { font-family: 'JetBrains Mono', monospace; font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ann-muted); margin-bottom: 0.2em; }
.lt { width: 100%; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; font-variant-numeric: tabular-nums; }
.lt th { font-size: 0.66rem; color: var(--ann-muted); text-align: left; border-bottom: 1px solid var(--ann-line); padding: 0.15em 0.4em; text-transform: none; letter-spacing: 0; }
.lt td { padding: 0.15em 0.4em; border-bottom: 1px solid var(--ann-line); }
.lt td.hi { color: var(--ann-indigo); font-weight: 700; }
</style>

<!--
Clicks 1-3: the input-layer weight gradients and the hidden biases. Make the
point that NO NEW RULE was needed: ∂E/∂w1 = δ_h1 × i1 = 0.0088 × 0.05 =
0.000439, shown on the diagram as 4.39e-4. Blame times what it multiplied.
Same as w5. The pattern has not changed once in the whole chapter.

These numbers are tiny — four ten-thousandths. Say why, because it is the
point of Chapter 5: two sigmoid derivatives and a small input have been
multiplied together on the way here.

Click 4 (all ten at full opacity): the deliberate climax, and the only
moment all day with this many numbers lit at once. Say: "Every gradient in
the network. This is what one backward pass produces."

Click 5 (the simultaneous update): every weight flips to its new indigo
value at once.

MUST SAY — THE SIGN POINT. Half the slide contradicts you if you skip it:
"Look at w5: gradient positive, so it goes DOWN, 0.40 to 0.3589. Now look at
w7: gradient NEGATIVE, so it goes UP, 0.50 to 0.5113. The minus sign in the
update rule does not mean 'decrease'. It means 'go the opposite way from the
gradient'. When the gradient is negative, that is an increase."

ALSO MUST SAY — simultaneity: "Every one of these gradients was computed
from the SAME old weights. Notice ∂E/∂w1 used w5 = 0.40 — the value BEFORE
the update — even though we had 'already' computed w5's new value. Nothing
moves until all ten are known. Then everything moves at once."

This is exactly what I claimed last lecture — "all weights update together,
once per pass" — and here it is, visible.

Click 6 (the ladder): the honest close. One step took the loss from 0.2984
to 0.2805 — a 6% drop. Look at where it has to go: ten thousand steps to
reach 2.4 × 10⁻⁶. "One step barely helps. The whole game is doing this a very
large number of times."

That 6% is worth a comment, because it is slower than it looks like it should
be. The network is badly wrong on o₁ and yet barely moving. Chapter 5 names
the culprit — every step back multiplied the blame by a σ′ smaller than a
quarter. Plant it here, pay it there."

Likely student question: "Why did the loss barely move?" Answer: "Two
reasons. Every gradient here has been damped by sigmoid derivatives — that is
Chapter 5. And this is one example, one step, with twelve parameters. Real
training runs this loop millions of times."

Transition: "You have now done it. Let's write it once, for any network."
-->
