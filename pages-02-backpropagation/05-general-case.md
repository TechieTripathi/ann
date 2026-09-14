---
layout: section
chapter: '5 · The general case'
---

# Chapter 5

## The general case

<div v-click class="thesis" style="margin-top:0.8em">Everything you just did by hand — with the digits replaced by symbols.</div>

<!--
Reassure before you start, because matrix notation is where students brace
for impact: "There is nothing new in this chapter. Not one new idea. We are
going to take the arithmetic you just did and write it down once, in a form
that works for any network of any size. If a symbol here confuses you, the
fix is to point at the slide in Chapter 4 where you computed that exact
number by hand."

Transition: "Two lines forward, three lines back."
-->

---
chapter: '5 · The general case'
clicks: 4
---

# The backward pass, in three lines

<span class="eyebrow math">Math</span>

<div class="key-message">You already computed every one of these. Here they are with names and shapes.</div>

<div class="eqs">

<div v-click="1" class="eq">

$$\delta^{(L)} \;=\; \big(a^{(L)} - y\big)\;\odot\;\sigma'\big(z^{(L)}\big)$$

<div class="en"><b>blame at the output.</b> Slide 19: ([0.7514, 0.7729] − [0.01, 0.99]) ⊙ [0.1868, 0.1755] = [0.1385, −0.0381]. <span class="sh">δ is 2×1</span></div>

</div>

<div v-click="2" class="eq">

$$\delta^{(l)} \;=\; \big( (W^{(l+1)})^{\top}\,\delta^{(l+1)} \big)\;\odot\;\sigma'(z^{(l)})$$

<div class="en"><b>blame, one layer back.</b> Slide 21 — the transpose <i>is</i> the sum over paths. <span class="sh">(2×2)ᵀ · 2×1 ⊙ 2×1 → 2×1</span></div>

</div>

<div v-click="3" class="eq">

$$\frac{\partial E}{\partial W^{(l)}} = \delta^{(l)} \big(a^{(l-1)}\big)^{\top} \qquad \frac{\partial E}{\partial b^{(l)}} = \delta^{(l)}$$

<div class="en"><b>blame × what it multiplied</b>, and <b>the gift</b>. Slides 20 and 22. <span class="sh">2×1 · 1×2 → 2×2</span></div>

</div>

</div>

<div v-click="4" class="transition-line">A hundred layers, a billion weights — the same three lines. <span class="arrow">Only the shapes change.</span></div>

<style>
.eqs { display: flex; flex-direction: column; gap: 0.3em; margin-top: 0.3em; }
.eq { background: var(--ann-paper-raised); border: 1px solid var(--ann-line); border-left: 4px solid var(--ann-ember); border-radius: 0.5em; padding: 0 0.9em 0.3em; }
.eq :deep(.katex-display) { margin: 0.22em 0 0.1em; font-size: 0.88em; }
.en { font-size: 0.76rem; color: var(--ann-ink-soft); line-height: 1.35; }
.slidev-layout .key-message { margin: 0.45em 0 0.4em; }
.slidev-layout .transition-line { margin-top: 0.7em; padding-top: 0.5em; }
.sh { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: var(--ann-circuit); margin-left: 0.4em; }
</style>

<!--
[If you are on time, this is a five-minute slide. If you are behind, it is a
two-minute slide — read the three lines, point at the slide references, move
on. Do not skip it entirely; it is the generalisation the whole chapter
promised.]

RULES FOR TEACHING THIS SLIDE:
- Never show the indexed scalar version. Not once. δ⁽ˡ⁾_j = Σ_k w_kj δ_k σ′(z_j)
  is where math lectures lose the room, and it reads visually as code.
- Read every symbol back to a slide where they computed it by hand. That is
  what the grey captions are for. Point at them.
- State the shapes out loud. Shape-checking is the most transferable habit
  you can give them and it costs three words per line.

Click 1: δ at the output. This is the cancellation from slide 19, in vector
form. Prediction minus truth.

Click 2: the recursion. Spend time on the transpose, because it is the one
piece of notation that genuinely confuses people. Say: "Wᵀ looks like the
network running in reverse. It is not. The transpose appears because when
you differentiate W·a with respect to a, you get Wᵀ. It is linear algebra,
not a reverse gear." Then connect it to slide 21: taking the transpose and
multiplying is EXACTLY the operation 'for each hidden neuron, sum δ×w over
everything it feeds'. The matrix notation is just doing both neurons at once.
The ⊙ is elementwise multiplication — the 'how responsive' factor, applied
per neuron.

Click 3: the gradients themselves, and the bias gift, restated.

Click 4: land the scale claim. These three lines are complete. GPT-scale
models use these three lines.

Likely student question: "Why write it in matrices at all?" Answer: "Two
reasons. It is shorter to reason about — and, much more practically, a GPU
multiplies matrices thousands of times faster than it runs loops. This
notation is not decoration; it is the reason deep learning is feasible."

Transition: "Now look again at that middle line, and at one number in it."
-->

---
chapter: '5 · The general case'
clicks: 5
---

# Why deep networks stopped learning

<span class="eyebrow why">Why</span>

<div v-click="1" class="key-message">σ′ never exceeds 0.25. Every layer you go back multiplies the blame by something smaller than a quarter.</div>

<div v-click="2" class="own-numbers">Your own numbers, from slide 21: &nbsp; δ<sub>o</sub> = <b>0.1385</b> &nbsp;→&nbsp; δ<sub>h</sub> = <b>0.0088</b> &nbsp;&nbsp;— one layer back, <b>16× smaller</b>.</div>

<div v-click="3" class="decay">
  <div><span class="dl">2 layers</span><span class="dv">0.25² = 6.3 × 10⁻²</span></div>
  <div><span class="dl">5 layers</span><span class="dv">0.25⁵ = 9.8 × 10⁻⁴</span></div>
  <div><span class="dl">10 layers</span><span class="dv">0.25¹⁰ = 9.5 × 10⁻⁷</span></div>
  <div><span class="dl">20 layers</span><span class="dv">0.25²⁰ = 9.1 × 10⁻¹³</span></div>
</div>

<div v-click="4" class="statement-box">The early layers — the ones that learn the most general features — get the smallest gradients of all. They barely move.</div>

<div v-click="5" class="transition-line">This is the <b>vanishing gradient problem</b>, and for twenty years it was the reason deep networks did not work. <span class="arrow">Two fixes, and they are the same fix.</span></div>

<style>
.own-numbers { background: var(--ann-ember-soft); border-left: 4px solid var(--ann-ember); border-radius: 0.5em; padding: 0.5em 1em; font-size: 0.9rem; margin-bottom: 0.5em; }
.decay { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5em; margin-bottom: 0.5em; }
.decay > div { background: var(--ann-paper-raised); border: 1px solid var(--ann-line); border-radius: 0.4em; padding: 0.45em 0.6em; text-align: center; }
.dl { display: block; font-family: 'JetBrains Mono', monospace; font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--ann-muted); }
.dv { display: block; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: var(--ann-ember); font-variant-numeric: tabular-nums; }
</style>

<!--
This slide is devastating precisely because it uses numbers the students
produced themselves twenty minutes ago. Lead with that.

Click 1: where 0.25 comes from — σ′(z) = σ(z)(1 − σ(z)), which is maximised
at z = 0 where σ = 0.5, giving 0.5 × 0.5 = 0.25. And that is the BEST case.
Away from zero it is much smaller.

Click 2: their own numbers. δ went from 0.75 to 0.045 in one layer. Ask:
"What happens after ten of those?"

Click 3: the decay table. 0.25 to the tenth is about one in ten million.

Click 4: the cruel part, and the bit worth dwelling on — it is the EARLY
layers that suffer most, and those are the layers learning the most general,
reusable features. The network's foundations are the slowest to train.

Click 5: name the problem and cash the Lecture 1 promise explicitly: "Last
lecture I told you sigmoid 'saturates, so gradients shrink' and that this
previewed why ReLU became popular — and I explicitly said I wasn't going to
do the calculus. That was the calculus."

CLOSE LECTURE 1'S BIGGEST LOOP HERE. It is the best connection in the pair
of lectures, so make it deliberately: "Last lecture, the entire argument for
why activation functions must exist was that without a non-linearity,
stacking ten layers collapses to one. We needed σ to buy depth. And now the
derivative of that very same σ is the thing taxing our gradient and taking
depth away. Non-linearity and trainability are in direct tension. The whole
history of activation function research is people trying to get the first
without paying for the second."

Likely student question: "Can gradients explode too?" Answer: "Yes — if the
weights are large, the Wᵀ multiplications can grow the blame instead of
shrinking it. That is the exploding gradient problem, and it is usually
handled by clipping. Same mechanism, opposite direction."

Transition: "So how did anyone fix this?"
-->

---
chapter: '5 · The general case'
clicks: 5
---

# Two fixes, and one confession

<span class="eyebrow practice">In practice</span>

<div class="fixes">
  <div v-click="1" class="fix">
    <div class="fh">Fix 1 · ReLU in the hidden layers</div>
    <div class="fb"><span class="mono">f(z) = max(0, z)</span>, so <span class="mono">f′(z) = 1</span> for every positive z.</div>
    <div class="fr">Multiply by 1 as many times as you like: <b>1ⁿ = 1</b>. The tax disappears.</div>
  </div>
  <div v-click="2" class="fix">
    <div class="fh">Fix 2 · Cross-entropy at the output</div>
    <div class="fb">Swap squared error for cross-entropy and the output σ′ <b>cancels algebraically</b>: δ = o − t.</div>
    <div class="fr">The blame that starts the whole backward pass is undamped.</div>
  </div>
</div>

<div v-click="3" class="statement-box">Both fixes do the same thing: they <b>remove a σ′ from the product.</b></div>

<div v-click="4" class="confession">
  <div class="ch">The confession — what our own loss cost us. I promised you this on slide 5</div>
  <table class="ct">
    <thead>
      <tr><th></th><th>squared error &nbsp;<i>(what we used)</i></th><th>cross-entropy</th></tr>
    </thead>
    <tbody>
      <tr><td>blame at output, δ</td><td>(o−t)·σ′</td><td>(o−t)</td></tr>
      <tr><td>on <i>our</i> forward pass, δ<sub>o1</sub></td><td class="bad">0.1385</td><td class="good">0.7414</td></tr>
      <tr><td>network says 0.999, truth is 0</td><td class="bad">0.000998</td><td class="good">0.999</td></tr>
    </tbody>
  </table>
</div>

<div v-click="5">

<Callout>
  <template #misconception>MSE and cross-entropy are interchangeable — they're both just ways of scoring how wrong you were.</template>
  <template #clarification>A loss matters <b>only through its derivative.</b> Every gradient in Chapter 4 was damped by a σ′ — which is why one step moved the loss just 6%. And a <i>maximally, confidently wrong</i> network gets a squared-error gradient of 0.000998: it has no idea it is in trouble. The rule is not "MSE is bad" — squared error is right for regression. It is <b>match the loss to the output activation.</b></template>
</Callout>

</div>

<style>
.fixes { display: grid; grid-template-columns: 1fr 1fr; gap: 0.7em; margin-bottom: 0.35em; }
.fix { background: var(--ann-circuit-soft); border-left: 4px solid var(--ann-circuit); border-radius: 0.5em; padding: 0.45em 0.8em; }
.fh { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 0.9rem; color: var(--ann-circuit); }
.fb { font-size: 0.78rem; margin: 0.15em 0; }
.fb .mono { font-family: 'JetBrains Mono', monospace; color: var(--ann-circuit); }
.fr { font-size: 0.76rem; color: var(--ann-ink-soft); }
.confession { margin-top: 0.35em; }
.slidev-layout .statement-box { padding: 0.3em 0.9em; font-size: 0.88rem; }
.slidev-layout .callout { font-size: 0.76rem; }
.slidev-layout .callout-row { padding: 0.4em 0.9em; }
.slidev-layout .key-message { margin: 0.35em 0 0.35em; }
.ch { font-family: 'JetBrains Mono', monospace; font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ann-ember); margin-bottom: 0.2em; }
.ct { width: 100%; font-size: 0.8rem; font-variant-numeric: tabular-nums; }
.ct th { font-size: 0.68rem; }
.ct td { font-family: 'JetBrains Mono', monospace; padding: 0.06em 0.5em; }
.ct th { padding: 0.06em 0.5em; }
.ct { font-size: 0.76rem; }
.ct td.bad { color: var(--ann-ember); font-weight: 700; }
.ct td.good { color: var(--ann-circuit); font-weight: 700; }
</style>

<!--
This is the sharpest three minutes in the deck. It cashes the slide-6
promise, explains ReLU properly, and turns the deck's one apparent
inconsistency into its best lesson.

Click 1 (ReLU): the derivative is 1 on the positive side. Not 0.25 — one.
So the multiplicative tax is exactly 1 per layer, forever. Say plainly:
"ReLU did not replace sigmoid because it is more accurate. It replaced it
because its derivative is 1. It is a gradient-flow fix, not an
expressiveness fix."

Click 2 (cross-entropy): this is the alternative we did NOT take. Show the
one-line algebra if they want it: ∂E/∂o for cross-entropy is (o−t)/[o(1−o)],
and multiplying by ∂o/∂z = o(1−o) cancels the denominator exactly, leaving
δ = o − t with no damping factor at all.

Click 3: the unifying point. Both fixes remove a σ′ from a product of σ′s.
Same disease, same cure, two different places in the network.

Click 4 (THE CONFESSION) — deliver this as a promise being kept, and name it
as such: "On slide 5 I said the reason cross-entropy is right for
classification is a gradient argument you could not read yet. Here it is."

Then make it personal, because it is: "We used squared error all through
Chapter 4. Look at the middle row — that is OUR forward pass. The error at o₁
was 0.7414, but the blame that actually reached the weights was 0.1385,
because we multiplied by a σ′ of 0.1868. Cross-entropy would have handed the
weights the full 0.7414. We paid a factor of five, on the very first step,
for our choice of loss."

Then the 0.000998 row, which is the one to really land: a network as wrong as
it is possible to be gets essentially zero gradient under squared error. It
is confidently, catastrophically wrong, and the loss function is whispering.

Click 5 (callout): read both halves, and be careful with the honest caveat —
do NOT let them leave thinking "MSE bad". Squared error is the right choice
for regression. The cancellation is specific to the sigmoid/softmax +
cross-entropy pairing. The rule is: match the loss to the output activation.

ALSO CASH THIS ONE: last lecture, describing AlexNet, I said it used "the
same core ingredients — activations, ReLU specifically, backpropagation."
Now you can say WHY ReLU mattered to AlexNet: it is what made a network that
deep trainable at all.

Likely student question: "What about ReLU's derivative at exactly zero?"
Answer: "Undefined. Frameworks pick 0 by convention. It is a measure-zero
event and in floating point it essentially never happens — it does not
matter in practice."

Transition: "One step, understood completely. Now — how do we get from one
step to a trained network?"
-->
