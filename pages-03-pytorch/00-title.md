---
layout: cover
class: title-cover
---

<div class="cover-motif">
  <svg viewBox="0 0 720 210" xmlns="http://www.w3.org/2000/svg">
    <!-- the 2-2-2 network of Lecture 2: teal forward, ember dashed backward -->
    <g fill="none" stroke="var(--ann-circuit)" stroke-width="2.5" opacity="0.55">
      <path d="M45,70 L145,70" /><path d="M45,70 L145,130" />
      <path d="M45,130 L145,70" /><path d="M45,130 L145,130" />
      <path d="M145,70 L245,70" /><path d="M145,70 L245,130" />
      <path d="M145,130 L245,70" /><path d="M145,130 L245,130" />
    </g>
    <g fill="none" stroke="var(--ann-ember)" stroke-width="2.5" stroke-dasharray="6 5" opacity="0.9">
      <path d="M245,70 L145,70" /><path d="M245,130 L145,130" />
    </g>
    <g fill="var(--ann-circuit)">
      <circle cx="45" cy="70" r="6" /><circle cx="45" cy="130" r="6" />
      <circle cx="145" cy="70" r="6" /><circle cx="145" cy="130" r="6" />
      <circle cx="245" cy="70" r="6" /><circle cx="245" cy="130" r="6" />
    </g>
    <text x="145" y="190" font-family="JetBrains Mono" style="font-size:15px" fill="var(--ann-muted)" text-anchor="middle">by hand</text>
    <text x="350" y="110" font-family="JetBrains Mono" style="font-size:34px" fill="var(--ann-indigo)" text-anchor="middle">=</text>
    <!-- five lines of code -->
    <g fill="var(--ann-indigo)" opacity="0.85">
      <rect x="450" y="56" width="225" height="8" rx="4" />
      <rect x="450" y="80" width="118" height="8" rx="4" />
      <rect x="450" y="104" width="172" height="8" rx="4" />
      <rect x="450" y="128" width="96" height="8" rx="4" />
      <rect x="450" y="152" width="145" height="8" rx="4" />
    </g>
    <text x="562" y="190" font-family="JetBrains Mono" style="font-size:15px" fill="var(--ann-muted)" text-anchor="middle">five lines</text>
  </svg>
</div>

# From Hand to Framework

### The same arithmetic you did yourself, in five lines of PyTorch — and the gradients to prove it

<div class="cover-meta">Lecture 3 · the framework, demystified</div>

<style>
.cover-motif { width: min(44%, 400px); margin: 0 0 1.2em; }
.cover-motif svg { width: 100%; height: auto; display: block; }
.cover-meta {
  margin-top: 1.2em;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  letter-spacing: 0.04em;
  color: var(--ann-muted);
}
</style>

<!--
Welcome them back. Set the register immediately: this lecture is a payoff, not
a new beginning. They have already done the hard part.

The motif is the whole lecture: the network they computed by hand on the left,
five lines of code on the right, an equals sign between them. Not "similar to".
Equals.

IMPORTANT — say this in the first minute, because it inoculates against the
single most common reaction to a framework: "Some of you have been waiting two
lectures to be allowed to use a library. Today you get to. But I am not going
to teach PyTorch as a new subject. I am going to show you that it is the
arithmetic you already did, with the bookkeeping automated. By the end of the
first chapter you will have watched the framework produce your own numbers."

Transition: "Let me put last week's closing promise back on screen."
-->

---
layout: default
chapter: '0 · The promise'
clicks: 3
---

# The promise we made you

<div class="key-message">Two claims, both testable. We test both before the first break.</div>

<blockquote class="lecture-quote">
"Next time: everything you just did by hand, <span v-mark.underline.teal="1">in five lines of PyTorch</span> — and we check its gradients against <span v-mark.underline.orange="2" style="white-space:nowrap">your numbers</span>."
</blockquote>

<div class="unpack">
  <div v-click="1"><span class="ux">"in five lines"</span><span class="uq">honest, or did I count generously?</span><span class="uc">Ch 1</span></div>
  <div v-click="2"><span class="ux">"your numbers"</span><span class="uq">match exactly, or just close?</span><span class="uc">Ch 1</span></div>
</div>

<div v-click="3" class="transition-line">Neither claim is rhetorical. One of them survives intact; the other needs a footnote. <span class="arrow">Both get settled today.</span></div>

<style>
.lecture-quote {
  border-left: 3px solid var(--ann-line);
  padding-left: 0.9em; margin: 0.9em 0 1.1em;
  color: var(--ann-ink-soft); font-style: italic; font-size: 0.95rem;
}
.unpack { display: flex; flex-direction: column; gap: 0.45em; }
.unpack > div { display: flex; align-items: baseline; gap: 0.7em; font-size: 0.88rem; }
.ux { font-family: 'JetBrains Mono', monospace; color: var(--ann-ember); flex: 0 0 11em; }
.uq { color: var(--ann-ink-soft); flex: 1; }
.uc { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--ann-muted); }
</style>

<!--
Twenty-five seconds of setup, then the two clicks. Do not rush the framing —
this slide is what makes the rest of the chapter feel like a verdict rather
than a tutorial.

Read the quote aloud, verbatim, and say you are holding yourself to it.

Click 1 ("in five lines"): the honest question. "Anyone can make code look
short by hiding the setup. So I will show you the setup separately and let you
count the lines that actually do the work." Promise them they may object at the
end of the next slide.

Click 2 ("your numbers"): the sharper question, and the one that matters.
"There is a difference between 'the framework broadly agrees' and 'the
framework prints 0.082167041 and so did you.' I am claiming the second."

Click 3 (transition): the deliberate tease. Do NOT resolve it here. For your
own reference: the five-lines claim survives; the numbers claim survives
exactly; the footnote belongs to the LOSS — nn.MSELoss() agrees with our loss
only because this network has exactly two outputs. That is the fourth slide of
the chapter and it is worth the wait.

Likely student question already at this point: "Why didn't we just use PyTorch
from the start?" Answer, and mean it: "Because then today would be a slide
about which function to call, and you would have no way of knowing whether it
was right. You now do. That is the entire difference between using a tool and
being able to audit it."

Transition: "Chapter one. Five lines."
-->
