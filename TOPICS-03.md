# Lecture 3 · From Hand to Framework — Topic Summary

A concise, one-idea-per-topic index. Mirrors the slide order in `lecture-03-pytorch.md`.

Lecture 1's index is in `TOPICS.md`; Lecture 2's is in `TOPICS-02.md`.

**The spine.** Lecture 2 ended with a promise rather than a debt: "everything you just did by
hand, in five lines of PyTorch — and we check its gradients against *your* numbers." That is two
testable claims, and Chapter 1 is the audit. Chapters 2–6 are then driven by the thing the whole
series has so far avoided: every number in Lectures 1 and 2 came from a network that has seen
**exactly one training example**.

> **Status: in progress.** Chapter 1 is written. Chapters 2–6 are planned and outlined below,
> but not yet built.

## Chapter 0 · The promise

- **The promise we made you** — Lecture 2's closing sentence, back on screen. Two claims: that it
  takes five lines, and that the gradients match by hand. One survives intact, the other needs a
  footnote. Both are settled before the first break.

## Chapter 1 · The five lines

The payoff. The same 2-2-2 network, the same weights, the same η = 0.5 — now typed into PyTorch.
Every figure on these slides is asserted by `npm run verify -- --nn`.

- **The whole of Chapter 4, retyped** — Three lines of setup (inputs, targets, initial weights)
  shown separately so the count stays honest, then five that do the work: `nn.Sequential`, the
  forward call, the loss, `backward()`, the print. Four of the five follow directly from Chapter
  5's equations; only `backward()` is new.
- **Line by line** — The same five lines dissected one click at a time, the annotation under the
  code replacing itself rather than piling up. Four of the five are notation for things already
  derived; `backward()` is the only genuinely new instruction.
- **It prints your numbers** — `print(net[2].weight.grad)` gives `0.0822, 0.0827, −0.0226,
  −0.0227` — the four numbers from slide 22, at the precision slide 22 showed them. Then
  `torch.set_printoptions(precision=9)`, because **four decimals is exactly where a rounding
  error would hide**: 0.082167041. Not agreement, identity.
- **One step, and w₇ still goes up** — `SGD(lr=0.5)` and `opt.step()`. w₅ falls 0.40 → 0.3589,
  w₇ **rises** 0.50 → 0.5113, loss 0.2984 → 0.2805. PyTorch lands on **0.280471447** — *our*
  number, not Mazur's 0.291028 — because `nn.Linear` gives every neuron a bias and the optimiser
  updates it. On the one point where this course departs from the canonical walkthrough, the
  framework takes our side.
- **The loss that agreed by accident** — `nn.MSELoss()` returns exactly our `½Σ(o−t)²` on this
  network, and only on this network: it reduces by the **mean**, so the two rules coincide at
  precisely two outputs. Add a third and it is 0.303 against 0.202. The transferable lesson is to
  read the `reduction` argument, because a loss reaches the weights only through its derivative.
- **What backward() actually did** — `print(loss)` ends in `grad_fn=<MulBackward0>`: every tensor
  remembers the operation that made it, and that chain of `grad_fn`s *is* the chain rule's chain,
  built during the forward pass. Nothing flows backward; the graph is a data structure you could
  print. One genuinely new rule — gradients **accumulate**, hence `zero_grad()`, which has no
  counterpart in the hand method because there was nowhere to accumulate into.

## Chapter 2 · From one example to a dataset — *planned*

Epoch, batch and iteration were defined in Lecture 2 Chapter 6 and never exercised: everything so
far trained on a single (x, y) pair. MNIST, a fixed seed, and a `DataLoader` give those words a
referent for the first time.

## Chapter 3 · The loop you already know — *planned*

`zero_grad / forward / loss / backward / step` — one line per box of Lecture 1's training-loop
diagram.

## Chapter 4 · What nothing computes for you — *planned*

η revisited, then momentum and Adam. Pays off Lecture 2's "η is the one number nothing computes
for you."

## Chapter 5 · It fits. Does it generalize? — *planned*

Train/test split and overfitting: the first point in the series where "the loss went down" stops
being the goal.
