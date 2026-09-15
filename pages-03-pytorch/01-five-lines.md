---
layout: section
chapter: '1 · The five lines'
---

# Chapter 1

## The five lines

<div v-click class="thesis" style="margin-top:0.8em">A framework is not a cleverer algorithm. It is your arithmetic, with the bookkeeping automated.</div>

<!--
Fifteen seconds. State the thesis and move — the proof is four slides away and
the proof is what convinces, not the assertion.

If you want one extra sentence: "Nothing in this chapter is new mathematics.
Everything in it is new typing."
-->

---
chapter: '1 · The five lines'
clicks: 5
---

# The whole of Chapter 4, retyped

<span class="eyebrow practice">Practice</span>

<div class="key-message" style="margin-top:-0.8em">Two lines of setup you already know. Five lines that do the work.</div>

<div class="setup-note">Setup — the network you spent an hour on, entered as numbers:</div>

```python
x = torch.tensor([0.05, 0.10]);  y = torch.tensor([0.01, 0.99])
net[0].weight = [[0.15, 0.20], [0.25, 0.30]];  net[0].bias = [0.35, 0.35]
net[2].weight = [[0.40, 0.45], [0.50, 0.55]];  net[2].bias = [0.60, 0.60]
```

```python {1|2|3|4|5|all}
net  = nn.Sequential(nn.Linear(2, 2), nn.Sigmoid(), nn.Linear(2, 2), nn.Sigmoid())
out  = net(x)
loss = 0.5 * ((out - y) ** 2).sum()
loss.backward()
print(net[2].weight.grad)
```

<div v-click="5" class="transition-line">Five lines, and four of them you could have written from Chapter 5's equations. <span class="arrow">Only one is new.</span></div>

<style>
.setup-note { font-size: 0.78rem; color: var(--ann-muted); margin: 0.5em 0 -0.2em; }
.slidev-layout .key-message { margin: 0.4em 0 0.6em; }
</style>

<!--
This is the slide the whole lecture was promised on. Type-along pace — let
them read each line before you speak it.

Open by dealing with the setup block honestly, because someone is already
counting: "Three lines above the fold, and I am not counting them. They are
the inputs, the targets and the initial weights — the contents of the table on
slide 16. Loading known numbers is not the algorithm. If you think that is
cheating, hold it; I will give you the honest line count at the end."

Click 1 (nn.Sequential): "This is the architecture picture from slide 15,
written left to right. Linear, sigmoid, Linear, sigmoid. nn.Linear(2, 2) is
'two in, two out' — it holds a 2x2 weight matrix and a bias vector, which is
exactly W and b from Chapter 5." Point out the indices now, they will need
them: net[0] is the first Linear, net[2] is the second, because the sigmoids
are net[1] and net[3].

Click 2 (out = net(x)): "Forward propagation. The entire thing. Slides 16
through 18 — two weighted sums, two biases, two squashes — is one function
call." Worth pausing: "This is the line that makes people think a framework is
magic. It is not. It is a for-loop over the four modules."

Click 3 (the loss): "Our loss, written out. One half, sum of squared errors.
I am writing it by hand rather than calling nn.MSELoss() and I want you to
notice that I did. Four slides from now you will find out why."

Click 4 (loss.backward()): "There it is. That is Chapter 3, Chapter 4 and
Chapter 5. Every delta, every sum over paths, every local slope — one method
call, no arguments." Let it sit. Then: "And it is the only line on this slide
you could not have written yourself from what we have covered."

Click 5 (print + all): the reveal is deliberately anticlimactic. "And then we
look."

Likely student question: "Where is the transpose from Chapter 5?" Answer:
"Inside nn.Linear, and inside backward(). nn.Linear stores its weight as
[outputs, inputs] — which is the layout we drew on slide 23 — and multiplies
by the transpose internally. You will see in a moment that net[2].weight
prints exactly the W2 matrix you wrote down."

Transition: "So. Does it print your numbers?"
-->

---
chapter: '1 · The five lines'
clicks: 5
---

# Line by line

<span class="eyebrow practice">Practice</span>

<div class="key-message" style="margin-top:-0.8em">Four of these you already know by another name. One of them is the new idea.</div>

```python {all|1|2|3|4|5}
net  = nn.Sequential(nn.Linear(2, 2), nn.Sigmoid(), nn.Linear(2, 2), nn.Sigmoid())
out  = net(x)
loss = 0.5 * ((out - y) ** 2).sum()
loss.backward()
print(net[2].weight.grad)
```

<div class="annot">
  <div v-click="[1,2]"><span class="an">1 · architecture</span>Slide 15, written left to right. <b>nn.Linear(2, 2)</b> is two in, two out — a 2×2 weight matrix and a bias vector, which is <b>W</b> and <b>b</b> from Chapter 5. The sigmoids take the odd indices; that is why the gradients come from <b>net[2]</b>.</div>
  <div v-click="[2,3]"><span class="an">2 · forward</span>Slides 16 to 18, in one call. Two weighted sums, two biases, two squashes — a loop over four modules. It also quietly <b>records the graph</b> that line 4 walks back down.</div>
  <div v-click="[3,4]"><span class="an">3 · the loss</span>Ours, <b>½ Σ(o−t)²</b>, written out rather than calling <b>nn.MSELoss()</b> — deliberately, and two slides from now you will see why. The ½ is what makes ∂E/∂o come out as plain (o − t).</div>
  <div v-click="[4,5]"><span class="an">4 · every gradient</span><b>The only line you could not have written from Lectures 1 and 2.</b> Chapters 3, 4 and 5 — every δ, every sum over paths — in one call with no arguments. It moves <b>no weight</b>; it fills in <b>.grad</b>.</div>
  <div v-click="5"><span class="an">5 · look at it</span>The gradients for w₅…w₈. <b>nn.Linear</b> stores its weight as [outputs, inputs] — the same layout as your <b>W₂</b> — so [0,0] is w₅ and [1,0] is w₇. Nothing to re-index.</div>
</div>

<style>
.annot { position: relative; min-height: 5.2em; margin-top: 0.5em; }
.annot > div { position: absolute; inset: 0; font-size: 0.83rem; color: var(--ann-ink-soft); line-height: 1.55; }
.an {
  display: block; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
  text-transform: uppercase; letter-spacing: 0.05em; color: var(--ann-circuit);
  margin-bottom: 0.25em;
}
.slidev-layout .key-message { margin: 0.4em 0 0.6em; }
</style>

<!--
The dissection. The previous slide was the reveal; this one earns it. One click
per line, and the annotation under the code changes rather than piling up — so
the audience is always reading exactly one thing.

Click 1 (architecture): the only click where you should mention indices, and do
mention them, because net[2] looks arbitrary until you have said out loud that
the sigmoids are modules too and occupy net[1] and net[3].

Click 2 (forward): "Slides sixteen to eighteen. An hour of arithmetic. One call."
Then plant the seed you collect on the last slide of the chapter: "and while it
does that, it is writing down what it did. Remember that."

Click 3 (the loss): flag the deliberate choice without explaining it yet — "I
could have called nn.MSELoss() here and I did not. Two slides." Refusing to
resolve it is what makes the later slide land.

Click 4 (backward): the one to slow down on. "Everything you did by hand last
week, for this network, is this line." Then the two negatives, because both are
load-bearing: it does not move a weight, and it does not overwrite .grad. The
first is why the optimiser is a separate object; the second is why zero_grad()
exists, which is the last slide of the chapter.

Click 5 (print): brisk. The layout point is genuinely useful — students expect
to have to transpose something and they do not.

If someone asks "so which line is the framework?": all five, and none of them.
Four are notation for things you derived. The fourth is the automation.

Transition: "So it runs. Does it print your numbers?"
-->

---
chapter: '1 · The five lines'
clicks: 4
---

# It prints your numbers

<span class="eyebrow practice">Practice</span>

<div class="key-message" style="margin-top:-0.8em">Not &ldquo;close to&rdquo;. Not &ldquo;consistent with&rdquo;. The same digits, as far as you care to look.</div>

<pre v-click="1" class="output">&gt;&gt;&gt; print(net[2].weight.grad)
tensor([[ 0.0822,  0.0827],
        [-0.0226, -0.0227]], dtype=torch.float64)</pre>

<div v-click="2" class="calc-strip">
  <div class="calc-chip bwd"><span class="lbl">slide 22 · ∂E/∂w₅</span>0.0822</div>
  <div class="calc-chip bwd"><span class="lbl">slide 22 · ∂E/∂w₆</span>0.0827</div>
  <div class="calc-chip bwd"><span class="lbl">slide 22 · ∂E/∂w₇</span>−0.0226</div>
  <div class="calc-chip bwd"><span class="lbl">slide 22 · ∂E/∂w₈</span>−0.0227</div>
</div>

<pre v-click="3" class="output">&gt;&gt;&gt; torch.set_printoptions(precision=9)
&gt;&gt;&gt; print(net[2].weight.grad)
tensor([[ 0.082167041,  0.082667628],
        [-0.022602540, -0.022740242]], dtype=torch.float64)</pre>

<div v-click="4" class="transition-line">Four decimals is where rounding hides. Nine decimals is where it cannot. <span class="arrow">Your hand arithmetic was exact.</span></div>

<style>
.slidev-layout .key-message { margin: 0.4em 0 0.7em; }
.slidev-layout .calc-strip { margin: 0.5em 0; }
</style>

<!--
SLOW DOWN. This is the emotional centre of the lecture and it is over in four
clicks if you let it be.

Click 1 (the print): read the four numbers aloud, slowly, and then stop
talking. Give them three full seconds to find the same numbers in their own
notes. Someone will say it out loud. Let them.

Click 2 (slide 22 strip): "These are not from the framework. These are the
four numbers you computed with a calculator last week, off slide 22." Put the
two rows side by side on screen and say nothing for a beat.

Click 3 (precision): here is the move that turns a nice coincidence into a
proof. "Four decimal places is exactly where a rounding error would hide.
0.0822 could be 0.08216 or 0.08224 — you cannot tell. So let us ask for more."
Then read the nine-decimal row: "Zero point zero eight two one six seven oh
four one. That is not agreement. That is identity."

MUST SAY, because it is the thing they will remember in five years: "There is
no version of this where the framework was doing something you were not. You
did not approximate what PyTorch does. PyTorch reproduces what you did."

Click 4 (transition): land it and move on before it becomes a victory lap.

Likely student question: "Would it match in float32?" Excellent question and
the answer is instructive: "To about seven significant figures, then it
drifts. I forced float64 precisely so the match would be unambiguous. In real
training nobody uses float64 — the noise is irrelevant next to the noise in
the data. But for an audit like this one, you want the arithmetic exact."

Second likely question: "Why net[2] and not net[1]?" — the sigmoids occupy the
odd indices. Say it, it costs four seconds and saves confusion later.

Transition: "Gradients are half of it. Chapter 2 said gradient descent is a
separate decision. Let's take the step."
-->

---
chapter: '1 · The five lines'
clicks: 4
---

# One step, and w₇ still goes up

<span class="eyebrow practice">Practice</span>

<div class="key-message" style="margin-top:-0.8em">Backprop computed the blame. The optimiser is the separate decision to act on it.</div>

```python {1|2|all}
opt = torch.optim.SGD(net.parameters(), lr=0.5)
opt.step()
```

<div v-click="2" class="calc-strip">
  <div class="calc-chip upd"><span class="lbl">w₅ &nbsp;gradient +0.0822</span>0.40 → <b>0.3589</b> &nbsp;(down)</div>
  <div class="calc-chip upd"><span class="lbl">w₇ &nbsp;gradient −0.0226</span>0.50 → <b>0.5113</b> &nbsp;(<b>up</b>)</div>
  <div class="calc-chip upd"><span class="lbl">loss</span>0.2984 → <b>0.2805</b></div>
</div>

<div v-click="3" class="statement-box">PyTorch lands on <b>0.280471447</b> — <i>our</i> number, not Mazur's 0.291028.</div>

<div v-click="4" class="transition-line">Because <b>nn.Linear</b> gives every neuron a bias and the optimiser updates it — the one place we deliberately left the canonical walkthrough. <span class="arrow">The framework took our side.</span></div>

<style>
.slidev-layout .key-message { margin: 0.4em 0 0.6em; }
.slidev-layout .statement-box { margin-top: 0.6em; font-size: 0.9rem; }
</style>

<!--
Brisk until click 3, then slow right down — click 3 is the best twenty seconds
in the chapter and it is easy to throw away.

Click 1 (SGD): "lr is eta. Half. The same half you used. net.parameters() is
'all ten weights and four biases' — the optimiser does not need to be told
which is which."

Click 2 (the strip): these are the same three figures as slide 22, so move
fast, but do not skip the w7 point — it was the hardest idea on that slide and
it is worth re-landing: "w7's gradient is negative, so the minus sign in the
update rule makes it INCREASE. 'Descend the loss' never meant 'decrease the
weight'."

Click 3 (the statement box): SET THIS UP PROPERLY. "Last week I told you we
were deviating from Matt Mazur in exactly one respect. He freezes the biases.
We update them, because a bias is a parameter like any other. That choice
changed one number: the loss after one step. His is 0.291028. Ours is
0.280471."

Then the payoff, and say it slowly: "PyTorch just printed 0.280471447."

Click 4: "That is not PyTorch agreeing with a textbook. nn.Linear gives every
neuron its own bias and SGD updates all of them, because that is what a real
network does. On the one point where we disagreed with the most-copied
backprop tutorial on the internet, the framework is on our side."

This is worth one extra sentence about why you set it up that way last week:
"I did not pick that deviation to be contrarian. I picked it because it is
what nn.Linear does, and I wanted today to be a clean match."

Likely student question: "So is Mazur wrong?" No — and be fair to him: "His
arithmetic is exact for the network he describes, which holds the biases
fixed. It is a different network by one modelling choice. Both are correct;
only one of them is what a framework will build for you."

Transition: "One thing on slide two I asked you to notice. I wrote the loss
out by hand."
-->

---
chapter: '1 · The five lines'
clicks: 4
---

# The loss that agreed by accident

<span class="eyebrow backward">Backward</span>

<div class="key-message" style="margin-top:-0.8em">Reach for <b>nn.MSELoss()</b> here and it gives the right answer for the wrong reason.</div>

<div v-click="1" class="cmp">
  <div class="cmp-col">
    <div class="cmp-h">two outputs — this network</div>
    <div class="cmp-r"><span class="cl">ours &nbsp;½ Σ(o−t)²</span><span class="num bwd">0.298371108</span></div>
    <div class="cmp-r"><span class="cl">nn.MSELoss()</span><span class="num bwd">0.298371108</span></div>
    <div class="cmp-v ok">identical</div>
  </div>
  <div v-click="2" class="cmp-col">
    <div class="cmp-h">three outputs — any other network</div>
    <div class="cmp-r"><span class="cl">ours &nbsp;½ Σ(o−t)²</span><span class="num bwd">0.303000000</span></div>
    <div class="cmp-r"><span class="cl">nn.MSELoss()</span><span class="num bwd">0.202000000</span></div>
    <div class="cmp-v bad">not even close</div>
  </div>
</div>

<div v-click="3" class="statement-box"><b>MSELoss</b> divides by <i>n</i>. We divide by 2. They agree only when <i>n</i> = 2.</div>

<div v-click="4" class="transition-line">A loss matters only through its derivative — and dividing by the wrong constant scales every gradient in the network. <span class="arrow">Read the reduction, always.</span></div>

<style>
.cmp { display: flex; gap: 1.2em; margin: 0.6em 0; }
.cmp-col { flex: 1; border: 1px solid var(--ann-line); border-radius: 0.5em; padding: 0.6em 0.9em; background: var(--ann-paper-raised); }
.cmp-h { font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--ann-muted); margin-bottom: 0.45em; }
.cmp-r { display: flex; justify-content: space-between; align-items: baseline; font-size: 0.8rem; margin: 0.15em 0; }
.cl { font-family: 'JetBrains Mono', monospace; color: var(--ann-ink-soft); }
.cmp-v { margin-top: 0.5em; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; }
.cmp-v.ok { color: var(--ann-circuit); }
.cmp-v.bad { color: var(--ann-ember); }
.slidev-layout .statement-box { margin-top: 0.3em; font-size: 0.88rem; }
</style>

<!--
This is the footnote promised on the title slide, and it is the one slide in
the chapter where the framework makes you WORSE off if you trust it. Give it
its due.

Open with the confession: "On slide two I wrote the loss out by hand instead
of calling nn.MSELoss(), and I asked you to notice. Here is why."

Click 1 (n=2 column): "If you had called nn.MSELoss() on this network, you
would have got 0.298371108. Our number. Identical to nine decimals. Everything
in this lecture would still have worked."

Click 2 (n=3 column): "Now add one output neuron. Nothing else changes." Read
both numbers. "0.303 against 0.202. That is not a rounding difference. That is
a different function."

Click 3 (the statement): "MSELoss reduces by the MEAN — it divides by the
number of outputs. We divide by two, always, because the two came from
differentiating the square. Those two rules coincide at exactly one network
width: this one."

NAME THE TRAP PLAINLY, because this is the transferable lesson: "So the
framework agreed with us for a reason that had nothing to do with us being
right. It agreed because this network has two outputs. That is the most
dangerous kind of agreement there is — the kind that stops agreeing the moment
you change something unrelated."

Click 4: connect it back to Chapter 5's rule. "And remember why it matters: a
loss only ever reaches the weights through its derivative. Divide by n instead
of 2 and every gradient in the network is scaled by 2/n. With eta fixed, that
is a different step. Your training either crawls or diverges, and nothing in
the error message will mention the loss."

Practical advice, say it: "Every loss function in every framework has a
reduction argument. Look at it. nn.MSELoss(reduction='sum') and a factor of a
half is what we wrote."

Transition: "One line left to explain. The one you could not have written."
-->

---
chapter: '1 · The five lines'
clicks: 5
---

# What backward() actually did

<span class="eyebrow structure">Structure</span>

<div class="key-message" style="margin-top:-0.8em">It did not think. It replayed a recording it made on the way forward.</div>

<pre v-click="1" class="output">&gt;&gt;&gt; print(loss)
tensor(0.298371109, dtype=torch.float64, grad_fn=&lt;MulBackward0&gt;)</pre>

<div v-click="2" class="graph-note">Every tensor produced by an operation remembers <b>which</b> operation made it. That chain of <b>grad_fn</b>s <i>is</i> the chain rule's chain — built during the forward pass, walked backwards on request.</div>

<div v-click="3" class="statement-box">Chapter 5's three matrix lines, executed for you. <b>Nothing is added.</b></div>

<div v-click="4" class="zero-grad"><b>One genuinely new rule:</b> gradients <i>accumulate</i>. Call <code>backward()</code> twice without <code>opt.zero_grad()</code> and you get the sum of two steps' blame. The hand method had nowhere to accumulate into, so this rule has no counterpart in anything you did last week.</div>

<div v-click="5" class="compact-callout">

<Callout>
  <template #misconception>The framework must be doing something cleverer than I did by hand.</template>
  <template #clarification>It runs the <b>same recursion, in the same order</b>, on the same numbers — that is why the digits match to nine places. The only thing it adds is <i>bookkeeping</i>: it records the graph as you build it, so it knows what to differentiate without being told. Automatic differentiation automates the <b>clerical</b> part of Chapter 4, not the <b>mathematical</b> part.</template>
</Callout>

</div>

<style>
.graph-note { font-size: 0.8rem; color: var(--ann-ink-soft); margin: 0.5em 0; line-height: 1.5; }
.zero-grad { font-size: 0.76rem; color: var(--ann-ink-soft); background: var(--ann-ember-soft); border-radius: 0.5em; padding: 0.45em 0.9em; margin: 0.5em 0; line-height: 1.45; }
.slidev-layout .statement-box { margin: 0.35em 0; font-size: 0.85rem; padding: 0.15em 1em; }
.slidev-layout .key-message { margin: 0.35em 0 0.45em; }
.compact-callout :deep(.callout) { font-size: 0.76rem; }
.compact-callout :deep(.callout-row) { padding: 0.4em 0.9em; }
.compact-callout :deep(.callout-label) { font-size: 0.62rem; }
</style>

<!--
The closing slide of the chapter. Its job is to remove the last trace of magic,
so do not rush the first two clicks — the grad_fn is the evidence.

Click 1 (print(loss)): "Look at the end of that line. grad_fn=MulBackward0.
The loss is not just a number. It is a number that remembers it was produced
by a multiplication."

Click 2 (the graph): this is the one genuinely new concept in the chapter, so
give it a sentence of its own. "Every tensor that came out of an operation
carries a pointer back to the operation that made it. Chain those pointers
together and you have a graph of the entire forward computation — built as a
side effect of doing the forward pass. backward() walks that graph in reverse.
That is all 'automatic differentiation' means: the chain rule, over a chain
the program wrote down while it was running."

Say this, because it pre-empts the mysticism: "Nothing flows backward. Same as
last week — the network is inert. 'Backward' is still just an order of
evaluation, and now it is an order over a data structure you could print."

Click 3: "The three matrix lines from slide 23, executed on your behalf. Not
improved. Executed."

Click 4 (zero_grad): FLAG THIS AS A REAL GOTCHA, they will hit it. ".grad is
added to, not overwritten. Forget zero_grad() in a training loop and your
gradients are the running total of every batch you have ever seen, and your
model quietly does not learn. It is the single most common beginner bug in
PyTorch." Worth the aside: "It works that way on purpose — it lets you split
one large batch across several backward passes. But the default costs you a
line in every loop you will ever write."

Click 5 (callout): read both halves.

If time allows, the honest line count from slide two, because you promised it:
"I said five lines. Strictly: five to compute, one to set up the optimiser, one
to step, one to zero the gradients. Eight lines is a training step. I stand by
five for what you were promised — the forward pass, the loss, and every
gradient in the network."

Transition: "Which means we can now do it a few thousand times. And the moment
we do, a question we have avoided for two lectures becomes unavoidable: this
network has seen exactly one example."
-->
