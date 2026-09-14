# Concept, Theme, Examples & Artifacts

A reader's guide to this repository: *why* the lectures are sequenced the way they are,
*what* visual language encodes that sequence, *which* concrete examples carry it, and
*what* files actually exist.

For the slide-by-slide index see [TOPICS.md](../TOPICS.md) (Lecture 1) and
[TOPICS-02.md](../TOPICS-02.md) (Lecture 2). For how to run and deploy, see [README.md](../README.md).

---

## 1 · Concept flow

### 1.1 The spine

The two decks are one argument delivered in two sittings. The whole series is driven by a
single question and its consequences:

> Can a computer learn *useful features* by itself, instead of being handed features a
> human designed?

Lecture 1 answers **yes, in principle**, and shows the machinery. Lecture 2 answers
**here is exactly how**, on real digits.

```
Rules break down
  → learn rules from data                 (but a human still picks the features)
  → borrow one principle from biology     (receive · combine · decide · send)
  → formalize it: z = wᵀx + b, then σ(z)  (bias, nonlinearity, depth)
  → a network learns by reducing a loss   (forward → loss → backward → update)
  → depth is the point; 2012 made it pay  ───── LECTURE 1 ENDS
  → "which number, which direction, how far, for which weight?"
  → loss functions · gradient descent · chain rule
  → one 2-2-2 network worked entirely by hand
  → the same thing in matrix form, for any network
  → vanishing gradients, and the two fixes
  → epoch / batch / iteration / SGD       ───── LECTURE 2 ENDS
```

### 1.2 The hand-off between the decks

Lecture 1 closes Chapter 4 with a deliberately under-defined sentence, delivered as a
misconception callout:

> *"It's calculus, not awareness. Backpropagation computes exactly how much **each**
> weight contributed to the loss, and nudges it **slightly** in **the direction that
> reduces it**."*

Lecture 2 opens by quoting that sentence back and pointing out that **five phrases in it
were never defined**. Each undefined phrase becomes a chapter. That is the entire
structural logic of Lecture 2 — it is not a topic list, it is a debt being paid:

| Undefined phrase in Lecture 1 | Paid off in Lecture 2 |
|---|---|
| "contributed to **the loss**" | Ch. 1 · Which number? |
| "the **direction** that reduces it" | Ch. 2 · Which direction |
| "**slightly**" | Ch. 2 · How far (η) |
| "**each** weight" — including buried ones | Ch. 3 · Credit assignment |
| "**computes**" | Ch. 4 (by hand) + Ch. 5 (general form) |

### 1.3 Lecture 1 — chapter logic

Each chapter's opening problem is *created by* the previous chapter's ending. This is
stated explicitly on the "Where we're going" roadmap slide.

1. **Why Machine Learning?** — A program is human-written rules applied to data. That
   works only when a human *already knows the rule*. Perceptual problems have no finite
   IF-statement set. ML flips it: Rules→Data, Program→Algorithm→Model. But classical ML
   still leans on hand-designed **features**, and feature engineering does not scale.
   Chapter ends on the hinge question: *can the computer learn features by itself?*
2. **Biology → Artificial Neuron** — To answer it, researchers looked at the best
   feature-learner they had access to. One neuron: receive → combine → decide → send.
   Maps to Inputs → Weighted Sum → Activation → Output. Layers give increasingly abstract
   representations (pixels → edges → shapes → identity), and **nobody programs what each
   layer detects**.
3. **The Full Neuron** — Now formalize the sketch. Why bias exists (a baseline, not an
   error term). Why an activation function *must* exist (without nonlinearity, any stack
   of layers collapses to one linear layer — depth buys nothing). Sigmoid / tanh / ReLU.
   Punchline: one sigmoid neuron *is* logistic regression.
4. **How the Network Learns** — Architecture, loss, forward propagation, backpropagation,
   the training loop. Backprop is named and motivated here but deliberately *not* derived.
5. **Deep Learning & Synthesis** — An ANN never "understands"; it is arithmetic
   throughout. Deep Learning = an ANN with many hidden layers. The theory was old; compute
   (GPUs), data (ImageNet) and AlexNet (2012) made it practical.

### 1.4 Lecture 2 — chapter logic

1. **Which number?** — A loss must (a) collapse to one number, (b) be minimal when right,
   and (c) be **differentiable in every weight**. Accuracy fails (c) — a step function with
   zero gradient almost everywhere. Cross-entropy is introduced but its *justification* is
   deliberately deferred to Ch. 5, because the argument is a gradient argument.
2. **Which direction, and how far?** — The loss is a landscape over the **weights** (the
   data is frozen — this is the slide's whole misconception). The derivative's sign gives
   the direction; the minus sign is what "move opposite the gradient" means. The update
   rule `w ← w − η ∂E/∂w`. η is the one number nothing computes for you.
3. **Credit assignment** — Chain rule: multiply local slopes along the chain. When one
   variable feeds many, **sum over paths** — and the terms can disagree in sign.
   Backpropagation *computes* gradients; gradient descent *uses* them. Two algorithms.
4. **Backpropagation by hand** — The payoff. A full 2-2-2 network, every digit computed
   on screen (see §3.2).
5. **The general case** — The same thing in three matrix lines; the transpose *is* the
   sum over paths. Then vanishing gradients: σ′ ≤ 0.25, visible in the deck's own numbers
   (δ_o = 0.1385 → δ_h = 0.0088, a 16× drop in one layer). ReLU and cross-entropy both
   work by removing a σ′ from the product. The rule is not "MSE is bad" — it is
   **match the loss to the output activation**.
6. **From one step to training** — Epoch / batch / iteration / SGD are four words
   answering one question: *when do we step?* Closes by re-showing Lecture 1's training
   loop with an equation under every box.

### 1.5 Recurring pedagogical devices

- **Misconception → clarification.** Every chapter pre-empts the specific wrong idea
  students actually form, in a `<Callout>`. Not decoration: each one is the hinge of its
  slide (§3.3 lists all of them).
- **Deferred payoff.** Ideas are introduced where they are *motivated* and derived where
  they are *needed* — cross-entropy (Ch. 1 → Ch. 5), backprop (L1 Ch. 4 → L2 entirely).
- **Presenter notes as the real script.** Most slides carry longer HTML comments than
  visible content: verbatim phrasing, click-by-click timing, the likely student question,
  and the transition line into the next slide.
- **Verifiability over trust.** Lecture 2 cites its source out loud (Matt Mazur) and tells
  students to check it that night; every number is machine-generated.

---

## 2 · Theme

### 2.1 The colour grammar

Defined and justified at the top of [styles/index.css](../styles/index.css). The duotone is
*not* decorative — it encodes the same split the lecture teaches, so students learn to read
colour as meaning.

| Token | Colour | Means |
|---|---|---|
| `--ann-ember` | warm orange `#e1592c` | biological / intuitive side of an analogy |
| `--ann-circuit` | cool teal `#0e7c86` | artificial / engineered / formal side |
| `--ann-indigo` | `#363b6e` | structure — architecture, chapters, depth, takeaways |
| `--ann-paper` / `--ann-ink` | `#f7f4ee` / `#1b1d23` | warm paper ground, not white |
| `--ann-muted`, `--ann-line` | | footers, rules, captions |

Lecture 2 **extends** the same grammar rather than replacing it — announced once on the
worked-example setup slide, then relied on silently:

- **teal = forward** (what the network computes)
- **ember = backward** (what the loss demands)
- **indigo = the update** (where the two meet)

A full dark palette is redefined under `:root.dark`, and mirrored independently in
[landing/index.html](../landing/index.html) under `prefers-color-scheme: dark`.

### 2.2 Typography

Loaded from Google Fonts via the deck frontmatter (`Inter`, `Space Grotesk`,
`JetBrains Mono`, weights 400–700).

- **Inter** — body text.
- **Space Grotesk** — headings, key messages, chips, thesis lines.
- **JetBrains Mono** — eyebrows, footers, numbers, code. Every number the audience must
  read is `font-variant-numeric: tabular-nums`, so a value changing on a click
  (0.15 → 0.1498) never shifts the layout.

### 2.3 Shared typographic components

Utility classes in `styles/index.css`, used across both decks:

| Class | Role |
|---|---|
| `.eyebrow` | small mono tag above a heading; colour-coded `.why` / `.intuition` / `.biology` (ember), `.math` / `.practice` (teal), `.structure` (indigo), `.forward` / `.backward` (L2) |
| `.key-message` | the one sentence of the slide, indigo, left-ruled |
| `.thesis` | large statement on chapter-opening slides |
| `.transition-line` | dashed-top line carrying the hand-off into the next slide |
| `.example-box`, `.statement-box`, `.step-chip` | concrete example / boxed claim / inline pipeline chip |
| `.num` + `.fwd` `.bwd` `.upd` | a single coloured figure in the worked example |
| `.calc-strip` / `.calc-chip` | horizontal arithmetic strip *under* a diagram — the diagram shows state, the strip shows the multiplication that produced it, keeping digits out of the picture |

Slide-local `<style>` blocks add one-off pieces (`.task-grid`, `.algo-grid`,
`.rule-attempt`, `.roadmap`, `.bias-figure`, `.cover-motif`).

### 2.4 Layout & interaction conventions

- **16:9, `canvasWidth: 980`, `colorSchema: light`, `transition: fade`** on both decks.
- **Layouts used:** `cover` (+ `class: title-cover`), `section` for chapter dividers,
  `statement` for hinge questions, `quote` for the closing one-sentence synthesis,
  `two-cols-header`, `end`.
- **Chapter frontmatter.** Every content slide carries `chapter: '<n> · <name>'`.
  [global-bottom.vue](../global-bottom.vue) reads it off the active route and renders the
  footer; `chapter: ''` suppresses the footer, as do the cover/section/end/statement/quote
  layouts. (Note in that file: `$frontmatter` does *not* resolve per-slide inside a global
  component — it must be read from `nav.currentSlideRoute`.)
- **Click contract.** Content is revealed one idea per click, with the presenter note
  scripting each click. Because `v-click` directives inside a *child component* cannot be
  auto-counted by Slidev, **any slide using `NeuronDiagram`, `LossLandscape` or
  `BackpropTrace` must declare `clicks: N` explicitly in its frontmatter.**
  `NeuronDiagram` starts at `v-click="2"`; `LossLandscape` and `BackpropTrace` start at a
  `from` prop (default 1) — the two conventions deliberately differ and are documented in
  each component header.
- **Mermaid diagrams** are themed inline with the palette hexes on every diagram
  (`primaryColor` teal, `secondaryColor` ember, `tertiaryColor`/indigo borders) plus a
  global override so edge labels sit on `--ann-paper` instead of Mermaid's opaque default.

### 2.5 One design system, two decks

`styles/index.css`, `components/` and `global-bottom.vue` are picked up by Slidev for *any*
entry file in the repo root, because `userRoot` is the entry file's folder. **Both entry
files must stay at the root** — moving a deck into a subfolder would force a duplicated
copy of the design system.

---

## 3 · Examples

### 3.1 Lecture 1 — the teaching examples

| Example | Where | What it is doing |
|---|---|---|
| `IF Marks > 40 → Pass ELSE Fail` | Ch. 1 | The simplest possible hand-written rule — trivial *because* the human already knows the rule with certainty |
| Face / speech / handwriting / translation / diagnosis | Ch. 1 | Five tasks a human performs effortlessly but cannot *state the rule* for |
| `IF eye_size > x → Person A` | Ch. 1 | Half-serious strawman; broken by lighting, pose, expression, camera angle, occlusion |
| Cat vs. dog: ear shape, fur texture, tail length, colour | Ch. 1 | Feature engineering made concrete, built one Mermaid node per click. The ceiling on performance is set by the human's feature choice, not the classifier |
| House price from square footage + rooms | Ch. 1 (notes) | The "simple data" column of the scaling table |
| Edge detectors / SIFT / HOG | Ch. 1 (notes) | The expected student objection, and its answer |
| Dendrites / soma / axon | Ch. 2 | Anatomy revealed in 5 clicks, each part previewing its mathematical counterpart |
| pixels → edges → shapes → identity | Ch. 2 | Why depth; nobody programs what a layer detects |
| Spam filter with zero suspicious keywords | Ch. 3 (notes) | Why an all-zero input may still deserve a nonzero baseline — i.e. why bias exists |
| Two sigmoid curves, same weights, different *b* | Ch. 3 | Bias slides the curve; it does not change its shape |
| Sigmoid / tanh / ReLU | Ch. 3 | Ranges 0–1, −1–1, and "simple, fast, most used today" |
| One sigmoid neuron = logistic regression | Ch. 3 | Connects the new object to something already known |
| AlexNet, 2012, GPUs + ImageNet | Ch. 5 | Same neuron, same backprop — what changed was scale, not theory |

### 3.2 Lecture 2 — the worked example

The centrepiece. **One 2-2-2 network, sigmoid everywhere, computed by hand across eight
slides**, with the `BackpropTrace` component holding the picture and `.calc-strip`
carrying the arithmetic.

```
inputs   i1 = 0.05   i2 = 0.10          targets  t1 = 0.01   t2 = 0.99
weights  w1..w4 = 0.15 0.20 0.25 0.30   (input → hidden)
         w5..w8 = 0.40 0.45 0.50 0.55   (hidden → output)
biases   0.35, 0.35 (hidden)  ·  0.60, 0.60 (output)   — four, not two
loss     L = ½ Σ (o − t)²                learning rate  η = 0.5
```

The narrative beats:

1. **Forward** → `E = ½[(0.7414)² + (−0.2171)²] = 0.2984`.
2. **Blame at the output** → `δ = (o − t) · o(1−o) = 0.7414 × 0.1868 = 0.1385`.
   The ½ in the loss is exactly what makes the first factor come out as plain `(o − t)`.
3. **Gradients, and a gift** → a weight's gradient is its blame times what it multiplied;
   a bias multiplies 1, so `∂E/∂b = δ` outright.
4. **A hidden neuron is blamed by everyone it feeds** →
   `∂E/∂out_h1 = (0.1385)(0.40) + (−0.0381)(0.50) = +0.0554 − 0.0190 = +0.0364`,
   then `× σ′(net_h1) = 0.2413 → δ_h1 = 0.0088`. **The two paths disagree in sign** — the
   gradient is the argument's verdict. This recursion is the only genuinely new idea.
5. **Ten gradients, one step** → all gradients computed from the *old* weights, all
   parameters moved simultaneously. The minus sign does not mean "decrease":
   w₅ falls 0.40 → 0.3589 while **w₇ rises** 0.50 → 0.5113. Loss 0.2984 → 0.2805 (just
   6%), and 2.4 × 10⁻⁶ after 10,000 steps.

Two decisions worth knowing before you teach it:

- **Provenance.** These are the weights and inputs of the canonical Matt Mazur worked
  example — the most-copied backprop walkthrough on the internet — precisely so students
  can check the lecture against an independent source. Every **weight** gradient matches
  his published figures to the digit.
- **One deliberate divergence.** Mazur holds the biases fixed; this deck updates them,
  because a bias is a parameter like any other (and `nn.Linear` gives every neuron its
  own). No weight gradient changes; the loss after one step does — **0.2910** his,
  **0.2805** ours. Both are printed by the verification script.

Also in Lecture 2: the **1-D loss landscape with a rolling ball** (`LossLandscape`, three
learning-rate regimes, one gradient-descent step per click), and the closing numeric
comparison — a network predicting 0.999 when the truth is 0 gets a squared-error gradient
of **0.000998** against cross-entropy's **0.999**, a factor of 1000.

### 3.3 The misconception catalogue

Every `<Callout>` in the series, in order. These are the points past cohorts actually
tripped on:

| Misconception | Clarification | Slide |
|---|---|---|
| A human can eventually hand-craft the right features for *any* problem | Many useful patterns in raw perceptual data have no human name at all | L1 Ch. 1 |
| Engineers program each layer ("layer 2 = edges") | The network *discovers* representations, because they reduce prediction error | L1 Ch. 2 |
| Bias is a fudge factor / error term | Bias is a learned parameter; it shifts *where* the boundary sits, never measures error | L1 Ch. 3 |
| The network "notices" its mistake and corrects itself | Calculus, not awareness | L1 Ch. 4 |
| After training, the network "understands" the image | Certain neurons become statistically *sensitive* to correlated patterns. That is optimization | L1 Ch. 5 |
| We could just use accuracy as the loss | Accuracy is a step function — zero derivative almost everywhere, so it can never say which way to go | L2 Ch. 1 |
| The loss curve's x-axis is the data, or the epoch | It is **a weight**. The data is frozen — that is why the derivative we want is ∂E/∂w | L2 Ch. 2 |
| A bigger learning rate means faster learning | Past a point each step leaps over the minimum and the loss *grows* | L2 Ch. 2 |
| The error "flows backward" like a reversed signal | Nothing flows. The network is **inert**; "backward" names an order of evaluation | L2 Ch. 3 |
| MSE and cross-entropy are interchangeable | A loss matters *only through its derivative* | L2 Ch. 5 |
| SGD is a different algorithm from gradient descent | Identical update rule; only the sample the gradient is estimated from changes | L2 Ch. 6 |

---

## 4 · Artifacts

### 4.1 Source artifacts

```
lecture-01-ann.md                 entry: frontmatter (theme, fonts, 16:9) + 6 src includes
lecture-02-backpropagation.md     entry: same design frontmatter, 7 src includes
pages-01-ann/                     00-title · 01-why-ml · 02-biology · 03-neuron-math
                                  04-learning · 05-deep-learning
pages-02-backpropagation/         00-title · 01-loss-functions · 02-gradient-descent
                                  03-credit-assignment · 04-by-hand · 05-general-case
                                  06-synthesis
styles/index.css                  the design system — palette, utilities, Mermaid/KaTeX fixes
global-bottom.vue                 chapter + page-number footer, on every non-divider slide
public/images/                    ann-architecture-wikimedia.svg
landing/index.html                standalone course index (own copy of the palette)
docs/CONCEPT.md                   this file
```

Each `pages-*/*.md` file is one chapter and contains its own chapter-divider slide plus
its content slides; the entry file is a table of contents, nothing more.

### 4.2 Vue components

| Component | Deck | What it renders |
|---|---|---|
| [components/NeuronDiagram.vue](../components/NeuronDiagram.vue) | L1 Ch. 2 | Schematic (not anatomical) biological neuron, 5 reveals: bare shape → dendrites → soma → axon → ANN mapping. Requires `clicks: 5` |
| [components/BioMap.vue](../components/BioMap.vue) | L1 Ch. 2 | The bridge shape: biological term (ember, left) — *inspires* — artificial term (teal, right). Always means "biology inspired this choice", never "these are the same thing" |
| [components/Callout.vue](../components/Callout.vue) | both | Two-row misconception / clarification box (ember ✕ over teal ✓) |
| [components/LossLandscape.vue](../components/LossLandscape.vue) | L2 Ch. 2 | 1-D loss curve with a ball; one gradient-descent step per click, tangent drawn because the slope is the *only* thing the algorithm can sense. Three learning-rate variants |
| [components/BackpropTrace.vue](../components/BackpropTrace.vue) | L2 Ch. 4 | The 2-2-2 network across seven `stage`s. Squares = data, circles = computation; above a neuron = net, inside = out, below = δ, right = bias. All numbers come from a frozen table generated by the verification script |

### 4.3 Verification artifact

[scripts/verify-numbers.py](../scripts/verify-numbers.py) (`npm run verify`, add `--torch` to
cross-check against PyTorch autograd in float64) is the **authoritative source for every
number in Lecture 2**. It re-derives the forward pass, the backward pass, all ten
gradients, the updated parameters, and the loss after 1 and 10,000 steps.

> **If a slide disagrees with that script, the slide is wrong.** The same rule is stated in
> the script's docstring, in `BackpropTrace.vue`'s header, and in the README.

### 4.4 Documentation artifacts

| File | Purpose |
|---|---|
| [README.md](../README.md) | How to run, why the shared design system requires both entries at the root, why the build uses hash routing |
| [TOPICS.md](../TOPICS.md) | One-idea-per-topic index for Lecture 1, mirroring slide order |
| [TOPICS-02.md](../TOPICS-02.md) | Same for Lecture 2, opening with "the spine" — the five undefined phrases |
| `docs/CONCEPT.md` | This file — concept flow, theme, examples, artifacts |

Presenter notes are themselves an artifact: the HTML comment at the bottom of nearly every
slide carries suggested verbatim phrasing, per-click timing, the likely student question
with its answer, and the transition into the next slide.

### 4.5 Build artifacts

`npm run dev` / `dev:02` serve a deck locally; `build` / `build:02` and `export` /
`export:02` produce a static site and a PDF respectively.

[.github/workflows/deploy.yml](../.github/workflows/deploy.yml) builds both decks plus the
landing page into a single GitHub Pages artifact on every push to `main`:

```
/                   landing/index.html   course index
/lecture-01/        Lecture 1
/lecture-02/        Lecture 2
```

Both decks are built with `--router-mode hash`, because GitHub Pages serves only a **root**
`404.html` — a per-deck SPA fallback in a subdirectory is never used, so history-mode deep
links would 404.
