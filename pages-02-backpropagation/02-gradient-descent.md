---
layout: section
chapter: '2 · Which direction, and how far?'
---

# Chapter 2

## Which direction, and how far?

<div v-click class="thesis" style="margin-top:0.8em">You cannot see the landscape. You can only feel the slope under your feet.</div>

<!--
Twenty seconds. The thesis is the entire intuition of gradient descent and
it is worth saying slowly, because everything students get wrong about
optimisation comes from imagining that the algorithm can see the whole
surface. It cannot. It is standing in fog, feeling the ground tilt.

Transition: "First — what surface are we even standing on?"
-->

---
chapter: '2 · Which direction, and how far?'
clicks: 5
---

# The loss is a landscape over the weights

<span class="eyebrow intuition">Intuition</span>

<div class="key-message"  style="margin-top:-1em">Freeze the data. The weights are the only things that vary — and the loss is a surface over them.</div>

<LossLandscape variant="good" :from="1" compact  style="margin-top:-3.5em"/>

<div v-click="5" class="compact-callout">

<Callout>
  <template #misconception>The x-axis is the input data, or the training epoch.</template>
  <template #clarification>The x-axis is <b>a weight</b>. While we draw this picture the training data is completely frozen — it is a constant. The weights are the only free variables in the universe. That is exactly why the derivative we want is <b>∂E/∂w</b>, and never ∂E/∂x.</template>
</Callout>

</div>

<style>
.compact-callout :deep(.callout) { font-size: 0.8rem; }
.compact-callout :deep(.callout-row) { padding: 0.45em 0.9em; }
</style>

<!--
This slide's Callout is the highest-yield correction in the chapter. If
students leave with the wrong axis in their heads, every subsequent slide
is quietly misread. Ask them, before clicking anything: "What is on the
horizontal axis?" You will get "the data" or "time" or "epochs" from
someone. That wrong answer is the reason this slide exists.

Clicks 1-4 walk the ball downhill. For each, narrate only what the algorithm
can actually sense: "It cannot see the valley. It feels the ground sloping
down to the right, so it steps right. Now it feels a gentler slope, so it
takes a smaller step. It is not aiming at the minimum — it has no idea
where the minimum is. It is just walking downhill."

NAME THE LIE IN THE PICTURE, explicitly, at click 4: "This drawing is
one-dimensional because that is what I can draw. The real landscape for the
tiny network we use in Chapter 4 has TWELVE dimensions — eight weights and
four biases. For a real network, billions. Almost every intuition this
picture gives you is wrong: there are no simple valleys, and the surface is
not remotely this smooth. It is right about exactly one thing, which is the
only thing I need from it — the slope tells you which way is down."

Notes only, if asked about local minima: in very high dimensions, true local
minima are rare; saddle points dominate, and in practice they are escapable.
Don't put this on the slide, but have it ready — someone always asks.

Click 5 (callout): read both halves.

Transition: "So how do we feel the slope? We already have the tool."
-->

---
chapter: '2 · Which direction, and how far?'
clicks: 4
---

# The derivative is the slope, and its sign is the direction

<span class="eyebrow math">Math</span>

<div v-click="1" class="key-message">∂E/∂w answers exactly one question: if I increase this weight a little, does the loss go up or down?</div>

<div class="signs">
  <div v-click="2" class="sign-card pos">
    <div class="sig">∂E/∂w &gt; 0</div>
    <div class="mean">Increasing w <b>increases</b> the loss.</div>
    <div class="act">So go the other way — <b>decrease</b> w.</div>
  </div>
  <div v-click="3" class="sign-card neg">
    <div class="sig">∂E/∂w &lt; 0</div>
    <div class="mean">Increasing w <b>decreases</b> the loss.</div>
    <div class="act">So keep going — <b>increase</b> w.</div>
  </div>
</div>

<div v-click="4" class="transition-line">In both cases you move <b>opposite</b> to the sign of the gradient. <span class="arrow">That single observation is the minus sign in the update rule.</span></div>

<style>
.signs { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; margin-top: 0.8em; }
.sign-card { border-radius: 0.6em; padding: 0.8em 1em; border: 1px solid var(--ann-line); }
.sign-card.pos { background: var(--ann-circuit-soft); border-left: 4px solid var(--ann-circuit); }
.sign-card.neg { background: var(--ann-ember-soft); border-left: 4px solid var(--ann-ember); }
.sig { font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 600; margin-bottom: 0.3em; }
.sign-card.pos .sig { color: var(--ann-circuit); }
.sign-card.neg .sig { color: var(--ann-ember); }
.mean { font-size: 0.88rem; color: var(--ann-ink-soft); }
.act { font-size: 0.88rem; margin-top: 0.3em; }
</style>

<!--
This slide is short on purpose. It exists so that the minus sign on the next
slide is inevitable rather than memorised.

Click 1: state the question the derivative answers, in words, before any
symbols. "If I increase this weight a little, does the loss go up or down,
and how fast?" That is all a partial derivative is here.

Clicks 2 and 3: walk both cases out loud, pointing at the ball on the
previous slide if it helps. Make them say the action before you reveal it.

Click 4: land the generalisation. Both cases are the same instruction —
move opposite the gradient.

Likely student question: "Does the gradient point at the minimum?" This is
the number-two misconception in the chapter and it is worth pre-empting even
if nobody asks. Answer: "No. It points along the locally steepest direction,
measured right where you are standing. It is first-order and myopic — it
knows the tilt of the ground under your feet and nothing else. It does not
know where the valley is, how far away it is, or whether there is a wall in
between."

Transition: "Direction, settled. Now the whole algorithm fits on one line."
-->

---
layout: statement
chapter: '2 · Which direction, and how far?'
clicks: 5
---

# $w \;\leftarrow\; w \;-\; \eta \,\dfrac{\partial E}{\partial w}$

<div class="symbols">
  <div v-click="1"><span class="sy">w</span><span class="sd">any single weight — or bias. They are all just numbers.</span></div>
  <div v-click="2"><span class="sy">∂E/∂w</span><span class="sd">the gradient. Which way is uphill, and how steeply.</span></div>
  <div v-click="3"><span class="sy">−</span><span class="sd">go the <b>opposite</b> way. This is the whole of "descent".</span></div>
  <div v-click="4"><span class="sy">η</span><span class="sd">the learning rate. How big a step to take.</span></div>
</div>

<div v-click="5" class="transition-line" style="max-width:34em;margin-left:auto;margin-right:auto;text-align:left">Every line of every training loop you will ever write is this line, repeated. <span class="arrow">Everything remaining in this lecture exists to compute that one derivative.</span></div>

<style>
.symbols { display: flex; flex-direction: column; gap: 0.4em; margin: 1.2em auto 0; max-width: 34em; text-align: left; }
.symbols > div { display: flex; align-items: baseline; gap: 1em; }
.sy {
  font-family: 'JetBrains Mono', monospace; font-size: 1rem; font-weight: 600;
  color: var(--ann-circuit); flex: 0 0 4.5em; text-align: right;
}
.sd { font-size: 0.88rem; color: var(--ann-ink-soft); }
</style>

<!--
Put the equation up and then refuse to move on for a full minute. This is
the most important line in the lecture and probably in the course.

Name every symbol out loud as you click, and read the whole thing as an
English sentence before and after: "The new weight is the old weight, minus
a small multiple of the gradient."

Click 1 (w): stress that bias is included. It is just a number that gets the
same treatment — which is exactly what I claimed last lecture and never
demonstrated. You will see it demonstrated in Chapter 4.

Click 3 (the minus): this is where to spend time. "Descent is not a
complicated idea. It is a minus sign."

Click 5: set up the rest of the lecture explicitly. We now have the entire
algorithm EXCEPT for one thing: how to actually compute ∂E/∂w for a weight
that is nowhere near the loss. That gap is Chapters 3, 4 and 5.

Likely student question: "Is this the same as what an optimiser like Adam
does?" Answer: "Adam is this line plus some memory of previous gradients.
The gradient it uses is computed exactly the same way. Everything today
applies unchanged."

Transition: "One symbol on that line is not computed by anything. Let's
look at it."
-->

---
chapter: '2 · Which direction, and how far?'
clicks: 3
---

# How big a nudge?

<span class="eyebrow practice">In practice</span>

<div class="key-message">η is the one number in this lecture that nothing computes for you.</div>

<div class="lr-grid">
  <div v-click="1"><LossLandscape variant="tiny" :from="1" compact /></div>
  <div v-click="2"><LossLandscape variant="overshoot" :from="1" compact /></div>
</div>

<div v-click="3">

<Callout>
  <template #misconception>A bigger learning rate means faster learning.</template>
  <template #clarification>Up to a point. Past it, each step leaps clean over the minimum and lands somewhere <i>worse</i> than it started — and the loss grows instead of shrinking. There is no gradient to tell you where that point is: η is a <b>hyperparameter</b>, chosen by you and tuned by experiment.</template>
</Callout>

</div>

<style>
.lr-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2em; margin-top: 0.4em; }
</style>

<!--
[CUT IF BEHIND — this slide can be compressed into two extra clicks on the
update-rule slide if you are running long. Nothing later depends on it.]

Click 1 (too small): "It is going the right way. It will get there. It will
get there some time next week." Cost is compute, not correctness.

Click 2 (too large): the interesting failure. Trace the ball: it overshoots,
lands higher up the far side, and the next gradient is bigger, so it
overshoots harder. The loss diverges. Students find it genuinely surprising
that gradient descent can make things worse — make sure they see it.

Click 3 (callout): read both halves, then land the honest bit: nothing in
the mathematics chooses η for you. It is tuned by running experiments.

MUST SAY, and say it here rather than being caught out in Chapter 4:
"In Chapter 4 I am going to use η = 0.5. That is enormous by modern
standards — you would normally see something between 0.001 and 0.1. I have
picked it deliberately so that one single step visibly moves the numbers on
a slide. In real training you take a very small step, millions of times."

If you skip this slide, say that sentence anyway, on the setup slide.

Transition: "We can now do everything — except the one thing we actually
need. Nobody has told us how to get ∂E/∂w for a weight buried in the middle
of the network."
-->
