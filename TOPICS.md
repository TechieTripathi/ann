# Lecture 1 · Artificial Neural Networks — Topic Summary

A concise, one-idea-per-topic index. Mirrors the slide order in `lecture-01-ann.md`.
Lecture 2's index is in `TOPICS-02.md`.

## Chapter 1 · Why Machine Learning?

- **Traditional programming — and where it breaks down** — A program is just human-written rules applied to data; that works when a human already knows the rule, but perceptual problems (faces, speech, handwriting) have no finite set of IF-statements that covers them.
- **Machine Learning — and what it already solves** — Instead of hand-coding rules, ML *learns* rules from data (Rules→Data, Program→Algorithm→Model). Classical algorithms (regression, trees, SVMs) already solve a lot — but still lean on features a human designed by hand.
- **The hidden step: Feature Engineering** — Someone has to manually decide, and compute, which measurements (features) a classifier is allowed to see.
- **Feature engineering doesn't scale** — Hand-picking features works for a handful of human-nameable measurements; it breaks down for complex data (images, speech, language) with potentially thousands of patterns nobody has words for.
- **Can the computer learn useful features by itself?** — The question that motivates everything that follows.

## Chapter 2 · Biology → Artificial Neuron

- **Why the human brain — and what one neuron does** — Researchers borrowed one property of the brain's best-known learner: receive → combine → decide → send. ANN is *inspired by* biology, not a simulation of it.
- **Anatomy of one decision** — Names the physical parts of a neuron (dendrites, soma, axon) one at a time, previewing their mathematical counterparts.
- **The neuron, end to end** — The full pipeline in one diagram: Inputs → Weighted Sum (`z = wᵀx + b`) → Activation Function → Output.
- **Why does it take so many neurons — and layers?** — One neuron draws one decision boundary. Layers of neurons learn increasingly abstract representations (pixels → edges → shapes → identity) — nobody programs what each layer detects.
- **Who teaches the network what an eye is?** — Nobody. The network only ever sees an input and the correct label; useful features emerge because they reduce prediction error, not by design.
- **The complete map** — Side-by-side recap: Dendrites→Inputs, Synapse→Weights, Soma→Weighted Sum, Threshold→Activation Function, Axon→Output, Network of Neurons→Layers.

## Chapter 3 · The Full Neuron

- **Why bias?** — Bias shifts the decision boundary; it's a baseline offset, not an error term.
- **Why activation functions must exist** — Without a nonlinear activation, stacking any number of layers is mathematically identical to one linear layer. Activation is what buys nonlinearity — and depth.
- **Three activation functions you'll meet constantly** — Sigmoid (0 to 1, probabilities), Tanh (−1 to 1, zero-centered), ReLU (simple, fast, most used today).
- **You've already met this neuron** — One neuron with a sigmoid activation *is* Logistic Regression; an ANN just chains many of these into layers.

## Chapter 4 · How the Network Learns

- **ANN Architecture** — Every neuron repeats the same four steps — receive, sum, activate, pass — wired together into input/hidden/output layers.
- **The Loss Function** — A single number that says how far a prediction was from the truth: large loss = poor prediction, small loss = good prediction.
- **Forward Propagation → Backpropagation** — Forward pass produces a prediction from the network's current weights (even random ones). Backpropagation sends the error backward and computes exactly how much each weight contributed to it — calculus, not awareness.
- **The training loop** — Repeat forward → loss → backward → update, thousands (often millions) of times, until the loss is small enough.

## Chapter 5 · Deep Learning & Synthesis

- **Does an ANN "understand" images?** — No. It starts as, and always remains, arithmetic on numbers — never symbolic understanding.
- **What is Deep Learning, really?** — Deep Learning is an ANN with many hidden layers. Every Deep Learning model is an ANN; not every ANN is Deep Learning.
- **Why Deep Learning succeeded when it did** — The theory is decades old. What changed by ~2012 was enough compute (GPUs), enough labeled data, and a landmark result that made it practical.
- **Putting it all back together** — ANNs learn complex, nonlinear relationships directly from data by automatically adjusting their weights during training — trading manual feature engineering for representation learning through layers.
