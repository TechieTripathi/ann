---
layout: cover
class: title-cover
---

<div class="cover-motif">
  <svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="var(--ann-circuit)" stroke-width="3" opacity="0.5">
      <path d="M60,100 L240,60" />
      <path d="M60,100 L240,140" />
      <path d="M240,60 L420,100" />
      <path d="M240,140 L420,100" />
    </g>
    <g fill="none" stroke="var(--ann-ember)" stroke-width="3.5">
      <path d="M420,100 L240,60" stroke-dasharray="7 5" />
      <path d="M420,100 L240,140" stroke-dasharray="7 5" />
      <path d="M240,60 L60,100" stroke-dasharray="7 5" opacity="0.6" />
    </g>
    <g fill="var(--ann-circuit)">
      <circle cx="60" cy="100" r="7" />
      <circle cx="240" cy="60" r="7" />
      <circle cx="240" cy="140" r="7" />
      <circle cx="420" cy="100" r="7" />
    </g>
    <path d="M470,100 L600,100" stroke="var(--ann-ember)" stroke-width="3" />
    <path d="M600,100 L586,92 M600,100 L586,108" stroke="var(--ann-ember)" stroke-width="3" fill="none" />
    <text x="470" y="86" font-family="JetBrains Mono" style="font-size:15px" fill="var(--ann-ember)">blame</text>
  </svg>
</div>

# Backpropagation

### The number, the direction, and the nudge — worked by hand, then written once for any network

<div class="cover-meta">Lecture 2 · the actual mathematics</div>

<style>
.cover-motif { width: min(38%, 340px); margin: 0 0 1.4em; }
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
Welcome them back. This lecture is the opposite of last one in texture: last
time was deliberately conceptual with almost no mathematics, today is
mathematics for ninety minutes. Say that plainly so nobody is ambushed —
but immediately reassure them that it is *one* piece of mathematics, the
chain rule, applied over and over.

Read the subtitle as the shape of the day: a number (the loss), a direction
(the gradient), a nudge (the learning rate), then the hard part — how you
get that direction for a weight buried deep inside the network.

The motif on this slide is the whole lecture in one picture: teal edges
going forward, ember dashed edges coming back. That colour split is used
consistently all day — teal is what the network computes, ember is what the
loss demands.

Transition: "Let's start with a sentence I put on screen last week."
-->

---
layout: default
chapter: '0 · Where we left off'
clicks: 6
---

# The sentence we left you with

<div class="key-message">Five phrases in one sentence were never defined. Each one is a chapter.</div>

<blockquote class="lecture-quote">
"It's calculus, not awareness. Backpropagation <span v-mark.circle.orange="5">computes exactly</span> how much <span v-mark.underline.orange="4">each weight contributed</span> to <span v-mark.underline.teal="1">the loss</span>, and nudges it <span v-mark.underline.teal="3">slightly</span> in <span v-mark.underline.teal="2">the direction that reduces it</span>."
</blockquote>

<div class="unpack">
  <div v-click="1"><span class="ux">"the loss"</span><span class="uq">which number, exactly?</span><span class="uc">Ch 1</span></div>
  <div v-click="2"><span class="ux">"the direction that reduces it"</span><span class="uq">which direction?</span><span class="uc">Ch 2</span></div>
  <div v-click="3"><span class="ux">"slightly"</span><span class="uq">how far?</span><span class="uc">Ch 2</span></div>
  <div v-click="4"><span class="ux">"each weight contributed"</span><span class="uq">how do you know what a buried weight contributed?</span><span class="uc">Ch 3</span></div>
  <div v-click="5"><span class="ux">"computes exactly"</span><span class="uq">by what algorithm, on what numbers?</span><span class="uc">Ch 4-5</span></div>
</div>

<div v-click="6" class="transition-line">Answer all five and there is nothing left of backpropagation to explain. <span class="arrow">That is the whole lecture.</span></div>

<style>
.lecture-quote {
  border-left: 3px solid var(--ann-line);
  padding-left: 0.9em; margin: 0.7em 0 0.9em;
  color: var(--ann-ink-soft); font-style: italic; font-size: 0.95rem;
}
.unpack { display: flex; flex-direction: column; gap: 0.3em; }
.unpack > div { display: flex; align-items: baseline; gap: 0.7em; font-size: 0.86rem; }
.ux { font-family: 'JetBrains Mono', monospace; color: var(--ann-ember); flex: 0 0 16em; }
.uq { color: var(--ann-ink-soft); flex: 1; }
.uc {
  font-family: 'JetBrains Mono', monospace; font-size: 0.72rem;
  color: var(--ann-indigo); background: var(--ann-indigo-soft);
  padding: 0.15em 0.5em; border-radius: 0.3em;
}
</style>

<!--
Open by putting this exact sentence back on screen and telling them the
truth: "This was on a slide last week, in a box, and every one of you nodded
at it. I want to show you that you nodded at five things you could not
define."

Read the quote aloud once, at normal speed, the way they heard it the first
time. Then read it again slowly, stopping at each highlighted phrase.

Click 1 ("the loss") — "I told you it was a single number measuring how
wrong we were. I explicitly said the formula was a detail for a later,
more technical lecture. This is that lecture."
Click 2 ("the direction that reduces it") — "A direction in what space?
There are twelve numbers in the tiny network we'll use today. Which way is
downhill in twelve dimensions?"
Click 3 ("slightly") — "How slightly? This word is doing an enormous amount
of unexamined work, and it has a name: the learning rate."
Click 4 ("each weight contributed") — "This is the hard one. The loss is
computed at the very end. A weight in the first layer never touches it. How
can a number that never met the loss be blamed for it?"
Click 5 ("computes exactly") — "Not approximates. Exactly. There is a
procedure, it is deterministic, and today you will run it by hand."

IMPORTANT — say this here, in the first ninety seconds. Last lecture's final
slide said "Next time: the actual mathematics of backpropagation, AND our
first framework." You are only delivering the first half today. Own it:
"I promised you two things today and you are getting one of them,
completely. Here is why I moved the other: the framework lecture is about
twenty minutes of API and seventy minutes of you not really knowing what
loss.backward() is doing underneath. Today you learn exactly what it does.
Next time, it will take twenty minutes total, and you will read the code
like a native speaker."

That is a genuine argument, not an excuse, and making it costs nothing.
Letting the broken promise pass silently costs trust.

Transition: "Question one. Which number?"
-->
