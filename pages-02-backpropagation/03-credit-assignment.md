---
layout: section
chapter: '3 · Credit assignment'
---

# Chapter 3

## Blame, three layers deep

<div v-click class="thesis" style="margin-top:0.8em">w₁ never touches the loss. It touches a neuron, that touches a neuron, that touches the loss.</div>

<!--
State the thesis and let the problem land before offering any tool.

Say it as a genuine puzzle: "Here is something that should bother you. The
loss is computed at the very end of the network, from the outputs. A weight
in the first layer is nowhere near it. The loss function has never seen w₁.
So in what sense can w₁ be *blamed* for the loss?"

This is the credit assignment problem, and every student should feel it as a
problem for about thirty seconds before you hand them the chain rule.

IMPORTANT framing for the whole chapter — put it in your own words: this is
a Master's audience, they have all seen the chain rule in a calculus course.
Do NOT teach it from scratch; that is condescending and costs six minutes.
Teach it as "two moves you already know, in the one configuration that
matters."

Transition: "The tool is one you already own."
-->

---
chapter: '3 · Credit assignment'
clicks: 4
---

# A weight three layers from the loss

<span class="eyebrow math">Math</span>

<div v-click="1" class="key-message">To get the slope along a chain, multiply the local slopes along the chain.</div>

<div v-click="2" class="gear-row">
  <div class="gear"><b>w</b><span>turn this</span></div>
  <div class="gop">→</div>
  <div class="gear"><b>net</b><span>and this moves 3× as fast</span></div>
  <div class="gop">→</div>
  <div class="gear"><b>out</b><span>and this moves 2× as fast</span></div>
  <div class="gop">→</div>
  <div class="gear res"><b>E</b><span>so this moves 6× as fast</span></div>
</div>

<div v-click="3">

$$\frac{\partial E}{\partial w_5}\;=\;\underbrace{\frac{\partial E}{\partial out_{o1}}}_{\text{how wrong}}\;\cdot\;\underbrace{\frac{\partial out_{o1}}{\partial net_{o1}}}_{\text{how responsive}}\;\cdot\;\underbrace{\frac{\partial net_{o1}}{\partial w_5}}_{\text{what it multiplied}}$$

</div>

<div v-click="4" class="transition-line">Each factor is <b>local</b> — it only involves one step. Nothing here needs to know about the network as a whole. <span class="arrow">That locality is what makes backpropagation possible.</span></div>

<style>
.gear-row { display: flex; align-items: center; gap: 0.5em; margin: 0.9em 0; }
.gear {
  flex: 1; text-align: center; background: var(--ann-paper-raised);
  border: 1px solid var(--ann-line); border-radius: 0.5em; padding: 0.6em 0.5em;
}
.gear.res { background: var(--ann-indigo-soft); border-color: var(--ann-indigo); }
.gear b { display: block; font-family: 'JetBrains Mono', monospace; font-size: 1rem; color: var(--ann-circuit); }
.gear.res b { color: var(--ann-indigo); }
.gear span { font-size: 0.74rem; color: var(--ann-ink-soft); }
.gop { color: var(--ann-muted); font-size: 1.2rem; }
</style>

<!--
Click 1: state the rule in words first, with no notation at all.

Click 2 (the gears): this is the non-network example, deliberately, so the
rule is demonstrated on something with no extra baggage. Turn w; net moves
three times as fast; out moves twice as fast as net; so E moves six times
as fast as w. Multiply the rates. That is the chain rule, and they already
knew it.

Click 3: now the same rule in the network's own variable names, still with
no numbers. Read the three underbraces aloud — "how wrong we were, how
responsive the neuron was, and what the weight was multiplying." Those three
phrases come back verbatim in Chapter 4, so say them exactly this way.

Click 4: land LOCALITY, which is the real insight and the thing students
under-appreciate. Every factor involves one step and its immediate
neighbour. No factor requires a global view of the network. That is why this
scales to a billion parameters.

Name the credit assignment problem formally here, once, because it is the
term in the literature: "This is called the credit assignment problem —
deciding how much of the final outcome each internal component is
responsible for." Then use the word "blame" for the rest of the lecture and
never switch again.

Likely student question: "Isn't multiplying all those derivatives expensive
for a big network?" Answer: "It would be, if you did it separately for every
weight — you'd redo the same sub-products millions of times. Backpropagation
is precisely the trick of computing them once, in the right order, and
reusing them. That ordering is the entire algorithm."

Transition: "One complication, and it is the only genuinely new idea in
backpropagation."
-->

---
chapter: '3 · Credit assignment'
clicks: 5
---

# When one thing feeds many

<span class="eyebrow math">Math</span>

<div v-click="1" class="key-message" style="margin-top:-1em">If a variable affects the loss through several paths, its gradient is the <b>sum</b> over those paths.</div>

<div class="fan" style="margin-top:-2em">
  <svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg">
    <g stroke="var(--ann-ink-soft)" stroke-width="2" opacity="0.4" fill="none">
      <line x1="120" y1="105" x2="330" y2="55" />
      <line x1="120" y1="105" x2="330" y2="155" />
      <line x1="370" y1="55" x2="470" y2="105" />
      <line x1="370" y1="155" x2="470" y2="105" />
    </g>
    <g v-click="2" stroke="var(--ann-ember)" stroke-width="3.5" fill="none">
      <line x1="330" y1="55" x2="125" y2="103" stroke-dasharray="6 4" />
      <text x="215" y="62" class="fl">path A</text>
    </g>
    <g v-click="3" stroke="var(--ann-ember)" stroke-width="3.5" fill="none">
      <line x1="330" y1="155" x2="125" y2="107" stroke-dasharray="6 4" />
      <text x="215" y="168" class="fl">path B</text>
    </g>
    <circle cx="120" cy="105" r="30" fill="var(--ann-circuit-soft)" stroke="var(--ann-circuit)" stroke-width="2.5" />
    <text x="120" y="112" class="fn">h</text>
    <circle cx="350" cy="55" r="26" fill="var(--ann-paper-raised)" stroke="var(--ann-ink-soft)" stroke-width="2" />
    <text x="350" y="62" class="fn sm">o₁</text>
    <circle cx="350" cy="155" r="26" fill="var(--ann-paper-raised)" stroke="var(--ann-ink-soft)" stroke-width="2" />
    <text x="350" y="162" class="fn sm">o₂</text>
    <rect x="446" y="82" width="70" height="46" rx="8" fill="var(--ann-indigo-soft)" stroke="var(--ann-indigo)" stroke-width="2" />
    <text x="481" y="112" class="fn ind">E</text>
  </svg>
</div>

<div v-click="4" style="margin-top:-1em">

$$\frac{\partial E}{\partial h}\;=\;\underbrace{\frac{\partial E}{\partial o_1}\frac{\partial o_1}{\partial h}}_{\text{path A}}\;+\;\underbrace{\frac{\partial E}{\partial o_2}\frac{\partial o_2}{\partial h}}_{\text{path B}}$$

</div>

<div v-click="5" class="transition-line">And the two terms can have <b>opposite signs</b>. <span class="arrow">Two downstream neurons can genuinely disagree about what h should have done.</span></div>

<style>
.fan { margin: 0.4em 0; }
.fan svg { width: 100%; max-height: 24vh; display: block; }
.fn { font-family: 'JetBrains Mono', monospace; font-size: 19px; font-weight: 700; fill: var(--ann-circuit); text-anchor: middle; }
.fn.sm { font-size: 16px; fill: var(--ann-ink); }
.fn.ind { fill: var(--ann-indigo); }
.fl { font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: var(--ann-ember); text-anchor: middle; }
</style>

<!--
This is the load-bearing slide of Chapter 3. Everything in Chapter 4 that is
genuinely hard is a re-enactment of this picture with numbers in it. Spend
time here so that slide 21 becomes recognition rather than discovery.

Click 1: state the rule.

Clicks 2 and 3 (the two paths): trace each one physically with a finger or
pointer. "h influenced o₁, and o₁ influenced the loss. That is one route
from h to E. But h ALSO influenced o₂, and o₂ also influenced the loss. That
is a second, completely independent route."

Click 4: the sum. Emphasise WHY it is a sum and not, say, a maximum or an
average: if you nudge h, BOTH consequences happen, simultaneously. The total
effect on the loss is the total of the effects. Nothing is chosen between.

Click 5 — the sentence that makes slide 21 land, so say it well:
"The two terms can have opposite signs. o₁ might be saying 'h pushed me too
high, turn it down', while o₂ says 'h was too low, turn it up'. They
genuinely disagree. And the gradient is not either neuron's opinion — it is
the argument's verdict."

Likely student question: "Wouldn't the terms just cancel out to nothing?"
Answer: "Sometimes they nearly do, and that is a real phenomenon — a neuron
pulled equally hard in both directions barely moves. But usually one side
wins, and the gradient tells you by how much. You'll see exactly this on
slide 21: one path contributes +0.30, the other −0.11, and the verdict is
+0.19."

Transition: "We now have every mathematical ingredient. Before we use them,
let's be precise about what we've actually built — because two different
things are about to get confused."
-->

---
chapter: '3 · Credit assignment'
clicks: 4
---

# So what *is* backpropagation?

<span class="eyebrow structure">Structure</span>

<div v-click="1" class="key-message">Backpropagation computes the gradients. Gradient descent uses them. They are two different algorithms.</div>

<div class="two-algos">
  <div v-click="2" class="algo bp">
    <div class="ah">Backpropagation</div>
    <div class="aw">answers</div>
    <div class="aq">"What is ∂E/∂w, for every w?"</div>
    <div class="an">A bookkeeping procedure. Evaluates one enormous product of partial derivatives in an order that reuses work.</div>
  </div>
  <div v-click="3" class="algo gd">
    <div class="ah">Gradient descent</div>
    <div class="aw">answers</div>
    <div class="aq">"Given those, what do I do?"</div>
    <div class="an">A policy. Subtract η times each gradient. Swap it for Adam and backpropagation does not change at all.</div>
  </div>
</div>

<div v-click="4">

<Callout>
  <template #misconception>The error "flows backward" through the network, like a signal travelling in reverse.</template>
  <template #clarification>Nothing flows. No signal travels, and no error is transmitted — the network is completely <b>inert</b> during the backward pass. "Backward" describes the <i>order in which we evaluate a product</i>, chosen because it lets us reuse each partial result instead of recomputing it. It is bookkeeping, not transport.</template>
</Callout>

</div>

<style>
.two-algos { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; margin: 0.7em 0; }
.algo { border-radius: 0.6em; padding: 0.7em 1em; border: 1px solid var(--ann-line); }
.algo.bp { background: var(--ann-ember-soft); border-left: 4px solid var(--ann-ember); }
.algo.gd { background: var(--ann-circuit-soft); border-left: 4px solid var(--ann-circuit); }
.ah { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 1rem; }
.algo.bp .ah { color: var(--ann-ember); }
.algo.gd .ah { color: var(--ann-circuit); }
.aw { font-family: 'JetBrains Mono', monospace; font-size: 0.64rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ann-muted); margin-top: 0.3em; }
.aq { font-size: 0.9rem; font-weight: 600; margin-bottom: 0.35em; }
.an { font-size: 0.79rem; color: var(--ann-ink-soft); }
</style>

<!--
This slide exists because separating these two is the single most valuable
correction you can make in this subject. Students routinely use
"backpropagation" to mean the entire training process.

Clicks 2 and 3: the cleanest way to make the distinction land is the swap
test — "If I replace gradient descent with Adam or RMSProp, does
backpropagation change? Not by one line. It still computes exactly the same
gradients. That is how you know they are separate."

Click 4 (callout): read it with real emphasis. "The error flows backward" is
in half the textbooks and it is a metaphor that costs students months. Kill
it: nothing propagates, nothing is transmitted, the network does not do
anything during the backward pass. We are evaluating a product, right to
left, because that order lets us reuse partial results.

BEST QUESTION TO HAVE PRE-BAKED HERE — last lecture I was asked "is
backpropagation how the brain actually learns?" and I answered "almost
certainly not" with no mechanism. Now you can give one, and it is worth the
ninety seconds:

"To compute a hidden neuron's blame, we need the weights on its OUTGOING
connections — the same weights, read backwards. In the general equations
you'll see in Chapter 5 this shows up as a transpose, Wᵀ. Now: a biological
synapse is not bidirectional. A neuron has no way to read the strengths of
the connections leaving its own axon. That is called the weight transport
problem, and it is the main reason neuroscientists doubt the brain runs
literal backpropagation. It is an open research question."

That upgrades a hand-wave from Lecture 1 into an actual explanation, which
is the whole design principle of this pair of lectures.

Transition: "Enough theory. Let's take one network, eight weights, four
biases, and actually do it."
-->
