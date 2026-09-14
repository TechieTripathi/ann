# Lecture 2 · Backpropagation — Topic Summary

A concise, one-idea-per-topic index. Mirrors the slide order in `lecture-02-backpropagation.md`.

**The spine.** Lecture 1 ended with "backpropagation computes exactly how much *each* weight
contributed to the loss, and nudges it *slightly* in *the direction that reduces it*." Five phrases
in that sentence were never defined. Each becomes a chapter.

## Chapter 1 · Which number?

- **What a loss function has to be** — Three requirements: it collapses to one number, it is smallest when the prediction is right, and it is **differentiable in every weight**. Squared error is the simplest thing meeting all three. Accuracy fails the third — it is a step function with zero gradient almost everywhere, so it can never say which way to go.
- **Classification wants a different ruler** — Cross-entropy asks "how much probability did you put on the truth?" rather than "how far off were you". Being confidently wrong costs unboundedly much. *Why* it is the right choice is a gradient argument, deferred to Chapter 5.

## Chapter 2 · Which direction, and how far?

- **The loss is a landscape over the weights** — The x-axis is a **weight**, not the data; the data is frozen. That is why the derivative we want is ∂E/∂w.
- **The derivative is the slope, its sign is the direction** — Positive gradient means increasing w increases the loss, so move the other way. Both cases reduce to "move opposite the gradient" — which is the minus sign.
- **The update rule** — `w ← w − η ∂E/∂w`. Every training loop ever written is this line, repeated.
- **How big a nudge** — η is the one number nothing computes for you. Too small creeps; too large overshoots and the loss *grows*.

## Chapter 3 · Credit assignment

- **A weight three layers from the loss** — Multiply the local slopes along the chain. Each factor is **local**, which is what makes the method scale.
- **When one thing feeds many** — A variable affecting the loss through several paths gets the **sum** over paths — and the terms can have opposite signs. Downstream neurons genuinely disagree.
- **Backpropagation vs gradient descent** — Backprop *computes* the gradients; gradient descent *uses* them. Two separate algorithms. Nothing "flows backward": the network is inert during the backward pass, and "backward" names an order of evaluation.

## Chapter 4 · Backpropagation by hand

A 2-2-2 network, sigmoid throughout, MSE loss `L = ½Σ(o − t)²`, targets 0.01 / 0.99, η = 0.5.
This is exactly the canonical Matt Mazur worked example, so every **weight** gradient below matches his
published numbers to the digit. One deliberate difference: Mazur holds the biases fixed, we update them —
which changes the loss after one step (0.2910 his, 0.2805 ours) but no weight gradient.
All figures verified against autograd.

- **Forward** — Weighted sum, add bias, squash, twice. Loss E = ½[(0.7414)² + (−0.2171)²] = **0.2984**.
- **Blame: start at the end** — Two factors, and both survive: δ = (o − t) × o(1−o) = 0.7414 × 0.1868 = **0.1385**. The ½ in the loss is what makes the first factor come out as plain (o − t).
- **Four gradients, and a gift** — A weight's gradient is its blame times what it multiplied. A bias multiplies 1, so **∂E/∂b = δ** outright.
- **A hidden neuron is blamed by everyone it feeds** — ∂E/∂out_h1 = (0.1385)(0.40) + (−0.0381)(0.50) = +0.0554 − 0.0190 = **+0.0364**, then × σ′(net_h1) = 0.2413 → δ_h1 = **0.0088**. The two paths disagree; the gradient is the argument's verdict. This recursion is the only new idea in backpropagation.
- **Ten gradients, one step** — Every gradient computed from the *old* weights; all parameters then move simultaneously. The minus sign does not mean "decrease": w₅ falls 0.40 → 0.3589, w₇ **rises** 0.50 → 0.5113. Loss 0.2984 → 0.2805 (only 6%), and 2.4 × 10⁻⁶ after 10,000 steps.

## Chapter 5 · The general case

- **The backward pass in three lines** — δ⁽ᴸ⁾ = (a⁽ᴸ⁾ − y) ⊙ σ′(z⁽ᴸ⁾); δ⁽ˡ⁾ = ((W⁽ˡ⁺¹⁾)ᵀδ⁽ˡ⁺¹⁾) ⊙ σ′(z⁽ˡ⁾); ∂E/∂W = δ(a⁽ˡ⁻¹⁾)ᵀ, ∂E/∂b = δ. The transpose *is* the sum over paths, done for every neuron at once.
- **Why deep networks stopped learning** — σ′ never exceeds 0.25, so each layer back multiplies the blame by less than a quarter — visible in our own numbers, δ_o = 0.1385 → δ_h = 0.0088, 16× in one layer. Ten sigmoid layers costs ~10⁻⁷. The early layers, which learn the most general features, move least.
- **Two fixes, one confession** — ReLU (σ′ = 1) and cross-entropy (σ′ cancels) both work by removing a σ′ from the product. On our own forward pass squared error gave δ_o1 = 0.1385 where cross-entropy would have given 0.7414 — a factor of 5.35 surrendered on the first step. And a network predicting 0.999 when the truth is 0 gets a squared-error gradient of **0.000998** against cross-entropy's **0.999** — 1000×. The rule is not "MSE is bad" but **match the loss to the output activation**.

## Chapter 6 · From one step to training

- **Epoch, batch, iteration, SGD** — Four words answering one question: when do we step? SGD has an identical update rule; only the sample the gradient is estimated from changes.
- **The training loop** — Lecture 1's diagram, with an equation under every box.
