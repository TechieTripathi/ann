<!--
  Schematic (not anatomical) biological neuron, revealed in 5 steps:
  1 = bare shape, 2 = dendrites, 3 = soma, 4 = axon, 5 = ANN-mapping overlay.
  Because these v-click directives live inside a child component, Slidev's
  compiler cannot auto-count them from the markdown — any slide using this
  component must set `clicks: 5` explicitly in its frontmatter.
-->
<template>
  <svg viewBox="0 0 720 320" class="neuron-diagram" xmlns="http://www.w3.org/2000/svg">
    <!-- STEP 1: bare shape -->
    <g class="ink" fill="none" stroke="var(--ann-ink-soft)" stroke-width="2.5">
      <path d="M40,80 Q100,90 130,140" />
      <path d="M35,140 Q95,140 130,155" />
      <path d="M40,205 Q100,190 130,165" />
      <path d="M55,240 Q105,215 132,175" />
      <ellipse cx="175" cy="160" rx="55" ry="42" />
      <path d="M230,160 L470,160" />
      <path d="M470,160 Q500,140 545,120" />
      <path d="M470,160 Q505,160 550,160" />
      <path d="M470,160 Q500,180 545,205" />
    </g>
    <g fill="var(--ann-ink-soft)">
      <circle cx="545" cy="120" r="5" />
      <circle cx="550" cy="160" r="5" />
      <circle cx="545" cy="205" r="5" />
    </g>

    <!-- STEP 2: dendrites -->
    <g v-click="2" class="highlight-in">
      <g fill="none" stroke="var(--ann-ember)" stroke-width="4">
        <path d="M40,80 Q100,90 130,140" />
        <path d="M35,140 Q95,140 130,155" />
        <path d="M40,205 Q100,190 130,165" />
        <path d="M55,240 Q105,215 132,175" />
      </g>
      <text x="20" y="55" class="label bio">Dendrites</text>
      <text x="20" y="72" class="caption">receive signals</text>
    </g>

    <!-- STEP 3: soma -->
    <g v-click="3" class="highlight-in">
      <ellipse cx="175" cy="160" rx="55" ry="42" fill="var(--ann-ember-soft)" stroke="var(--ann-ember)" stroke-width="4" />
      <text x="175" y="158" text-anchor="middle" class="label bio on-fill">Soma</text>
      <text x="175" y="175" text-anchor="middle" class="caption on-fill">combine + check threshold</text>
    </g>

    <!-- STEP 4: axon -->
    <g v-click="4" class="highlight-in">
      <g fill="none" stroke="var(--ann-ember)" stroke-width="4">
        <path d="M230,160 L470,160" />
        <path d="M470,160 Q500,140 545,120" />
        <path d="M470,160 Q505,160 550,160" />
        <path d="M470,160 Q500,180 545,205" />
      </g>
      <g fill="var(--ann-ember)">
        <circle cx="545" cy="120" r="5" />
        <circle cx="550" cy="160" r="5" />
        <circle cx="545" cy="205" r="5" />
      </g>
      <text x="350" y="140" text-anchor="middle" class="label bio">Axon</text>
      <text x="350" y="200" text-anchor="middle" class="caption">fire &#8594; send signal onward</text>
    </g>

    <!-- STEP 5: ANN mapping overlay -->
    <g v-click="5" class="highlight-in">
      <rect x="10" y="15" width="690" height="290" rx="16" fill="none" stroke="var(--ann-circuit)" stroke-width="2" stroke-dasharray="6 6" />
      <text x="30" y="285" class="label ann">x&#8321;, x&#8322;, x&#8323; &#8202;(inputs)</text>
      <text x="175" y="230" text-anchor="middle" class="label ann">z = w&#7511;x + b</text>
      <text x="600" y="90" text-anchor="middle" class="label ann">output</text>
      <text x="360" y="35" text-anchor="middle" class="caption ann-title">One artificial neuron</text>
    </g>
  </svg>
</template>

<style scoped>
.neuron-diagram {
  width: 100%;
  max-height: 44vh;
}

.label {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 19px;
}

.label.bio {
  fill: var(--ann-ember);
}

.label.ann {
  fill: var(--ann-circuit);
}

.label.on-fill {
  fill: var(--ann-ink);
}

.caption {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  fill: var(--ann-ink-soft);
}

.caption.on-fill {
  fill: var(--ann-ink-soft);
}

.caption.ann-title {
  fill: var(--ann-circuit);
  font-size: 13px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
</style>
