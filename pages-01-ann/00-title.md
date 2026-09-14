---
layout: cover
class: title-cover
---

<div class="cover-motif">
  <svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="var(--ann-ember)" stroke-width="3" opacity="0.55">
      <path d="M40,40 Q100,55 140,100" />
      <path d="M30,100 Q95,100 140,112" />
      <path d="M40,165 Q100,148 140,120" />
    </g>
    <ellipse cx="180" cy="100" rx="42" ry="32" fill="none" stroke="var(--ann-ink-soft)" stroke-width="3" opacity="0.55" />
    <g fill="none" stroke="var(--ann-circuit)" stroke-width="3" opacity="0.6">
      <path d="M222,100 L620,100" />
      <path d="M480,100 L480,40" />
      <path d="M560,100 L560,160" />
    </g>
    <g fill="var(--ann-circuit)" opacity="0.6">
      <circle cx="480" cy="40" r="4" />
      <circle cx="560" cy="160" r="4" />
      <circle cx="620" cy="100" r="4" />
    </g>
  </svg>
</div>

# Artificial Neural Networks

### From rules → to learning from data → to a borrowed idea from biology → to learning by itself

<div class="cover-meta">Introduction · conceptual understanding, not coding</div>

<style>
.cover-motif {
  width: min(30%, 300px);
  margin: 0 0 1.6em;
}
.cover-motif svg {
  width: 100%;
  height: auto;
  display: block;
}
.cover-meta {
  margin-top: 1.2em;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  letter-spacing: 0.04em;
  color: var(--ann-muted);
}
</style>

<!--
Welcome the class. This is a substitute-taught session, so open by anchoring
students back to where the previous lectures left off: they already know
basic Machine Learning (regression, classification, maybe SVMs/trees), and
today is their first formal introduction to Artificial Neural Networks.

Say something like: "Today is conceptual, not coding. My goal is that by the
end of this session you can explain, in plain language, why neural networks
exist, what problem they solve that older ML methods could not, and how a
single artificial neuron works — before we ever touch a framework like
PyTorch or TensorFlow."

Point at the subtitle line and read it as the arc of the whole lecture:
rules → data-driven learning → biological inspiration → self-taught features.
That is the spine every slide today hangs off of.

Transition: "Let's start where AI itself had to start — with the limits of
writing rules by hand."
-->

---
layout: default
---

# Where we're going

<!-- <div class="key-message">Five ideas, in the order your brain needs them — not the order a textbook would give them.</div> -->

<div class="roadmap">
  <div class="roadmap-row">
    <div class="roadmap-num">1</div>
    <div><b>Why Machine Learning?</b><span>Rules break down. Learning from data doesn't.</span></div>
  </div>
  <div class="roadmap-row">
    <div class="roadmap-num">2</div>
    <div><b>Biology → Artificial Neuron</b><span>Borrowing one idea from the brain — not simulating it.</span></div>
  </div>
  <div class="roadmap-row">
    <div class="roadmap-num">3</div>
    <div><b>The Full Neuron</b><span>Weighted sum and why activation functions must exist.</span></div>
  </div>
  <div class="roadmap-row">
    <div class="roadmap-num">4</div>
    <div><b>How the Network Learns</b><span>Forward propagation, loss, backpropagation, training loop.</span></div>
  </div>
  <div class="roadmap-row">
    <div class="roadmap-num">5</div>
    <div><b>Deep Learning &amp; Synthesis</b><span>What "deep" actually means, and why it took off in 2012.</span></div>
  </div>
</div>

<style>
.roadmap { margin-top: 1.2em; display: flex; flex-direction: column; gap: 0.55em; }
.roadmap-row { display: flex; align-items: flex-start; gap: 0.9em; }
.roadmap-num {
  flex-shrink: 0;
  width: 2em; height: 2em;
  border-radius: 999px;
  background: var(--ann-indigo-soft);
  color: var(--ann-indigo);
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  display: flex; align-items: center; justify-content: center;
}
.roadmap-row div > b { display: block; font-family: 'Space Grotesk', sans-serif; font-size: 1.05rem; }
.roadmap-row div > span { color: var(--ann-ink-soft); font-size: 0.9rem; }
</style>

<!--
This is a genuine sequence, not a decorative list — each chapter's opening
problem is created by the previous chapter's ending. Walk through the five
rows quickly (30 seconds total), framing each as a question the previous one
raises:

1 → asks "how do we avoid writing rules by hand?"
2 → answers it by asking "what does the most powerful learner we know
    (the brain) actually do?"
3 → takes that biological sketch and asks "what, precisely, is the math?"
4 → having built one neuron, asks "how does a whole network of these get
    good at anything?"
5 → zooms out and asks "how far can this idea scale, and why did it
    suddenly explode around 2012?"

Don't dwell — this slide exists so students have a map before the terrain,
not as content to memorize. Transition: "Let's go build that map, one
question at a time."
-->

<!-- ---
layout: default
---

# How to read these slides

<div class="key-message">A small color/label convention repeats all lecture — learn it once, use it all day.</div>

<div class="legend-grid">
  <div class="legend-item">
    <span class="eyebrow why">Why / Intuition / Biology</span>
    <span class="legend-desc">Warm <b>ember</b> tags mark the informal, human-intuition side of an idea — motivation, analogy, "why should you care."</span>
  </div>
  <div class="legend-item">
    <span class="eyebrow math">Math / In practice</span>
    <span class="legend-desc">Cool <b>teal</b> tags mark the formal, engineered side — the equation, and what it buys us in practice.</span>
  </div>
  <div class="legend-item">
    <div class="legend-demo">
      <div class="demo-chip demo-bio">Biological term</div>
      <div class="demo-arrow">→</div>
      <div class="demo-chip demo-ann">ANN term</div>
    </div>
    <span class="legend-desc">This bridge shape always means "biology inspired this engineering choice" — never "these are the same thing."</span>
  </div>
  <div class="legend-item">
    <span class="legend-desc"><b>Indigo</b> marks structure: chapter dividers, architecture, one-sentence takeaways.</span>
  </div>
</div>

<style>
.legend-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1em 1.5em; margin-top: 1.3em; }
.legend-item { display: flex; flex-direction: column; gap: 0.4em; }
.legend-desc { font-size: 0.88rem; color: var(--ann-ink-soft); }
.legend-desc b { color: var(--ann-ink); }
.legend-demo { display: flex; align-items: center; gap: 0.5em; }
.demo-chip { padding: 0.3em 0.7em; border-radius: 0.4em; font-size: 0.82rem; font-family: 'Space Grotesk', sans-serif; font-weight: 600; }
.demo-bio { background: var(--ann-ember-soft); color: var(--ann-ember); border-left: 3px solid var(--ann-ember); }
.demo-ann { background: var(--ann-circuit-soft); color: var(--ann-circuit); border-left: 3px solid var(--ann-circuit); }
.demo-arrow { color: var(--ann-muted); }
</style> -->

<!--
Optional slide — show it fast (under a minute) if you're on schedule, or
skip straight to Chapter 1 if you're tight on time; nothing later depends on
students having seen it explicitly, it's a convenience so the visual
language doesn't feel arbitrary the first time it appears.

Mention the misconception boxes too, even though there's no example on this
slide: "Whenever you see a two-tone box with a cross and a checkmark, that's
a misconception I'm pre-empting — students in past cohorts have tripped on
that exact point."

Transition: "With that vocabulary in place — let's go back to the actual
history. Why did we need Machine Learning in the first place?"
-->
