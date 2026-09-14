<!--
  LossLandscape.vue — Lecture 2, Chapter 2.

  A 1-D loss curve with a ball taking gradient-descent steps, one step per
  click. Three variants show the three learning-rate regimes.

  CLICK CONTRACT
  Reveals are absolute v-click indices starting at `from` (default 1).
  NOTE this deliberately differs from NeuronDiagram.vue, which starts at
  v-click="2" and so wastes the first key press. Because these v-click
  directives live inside a child component, Slidev cannot auto-count them:
  every slide using this component MUST declare `clicks: N` in frontmatter,
  where N = from + steps - 1.
-->
<template>
  <div class="landscape">
    <svg :viewBox="`0 0 620 ${H}`" xmlns="http://www.w3.org/2000/svg">
      <!-- axes -->
      <line x1="50" :y1="BASE" x2="595" :y2="BASE" stroke="var(--ann-line)" stroke-width="1" />
      <line x1="50" y1="30" x2="50" :y2="BASE" stroke="var(--ann-line)" stroke-width="1" />
      <text x="592" :y="BASE + 20" class="ax" text-anchor="end">a single weight, w</text>
      <text x="44" y="38" class="ax" text-anchor="end">loss</text>

      <!-- the curve -->
      <path :d="curve" fill="none" stroke="var(--ann-ink-soft)" stroke-width="2.5" style="opacity:0.55" />

      <!-- the minimum we cannot see from inside the problem -->
      <g style="opacity:0.5">
        <line :x1="sx(MIN)" :y1="sy(loss(MIN))" :x2="sx(MIN)" :y2="BASE"
              stroke="var(--ann-indigo)" stroke-width="1.5" stroke-dasharray="4 4" />
        <text :x="sx(MIN)" :y="BASE + 20" class="ax mid" text-anchor="middle">minimum</text>
      </g>

      <!-- one group per descent step -->
      <g v-for="(p, i) in steps" :key="i" v-click="from + i">
        <!-- tangent: the only thing the algorithm can actually sense -->
        <line :x1="sx(p.w) - 46" :y1="sy(p.L) + 46 * slopeScreen(p.w)"
              :x2="sx(p.w) + 46" :y2="sy(p.L) - 46 * slopeScreen(p.w)"
              stroke="var(--ann-ember)" stroke-width="2.5" style="opacity:0.85" />
        <!-- the step taken -->
        <line v-if="i > 0"
              :x1="sx(steps[i - 1].w)" :y1="sy(steps[i - 1].L)"
              :x2="sx(p.w)" :y2="sy(p.L)"
              stroke="var(--ann-indigo)" stroke-width="2" stroke-dasharray="5 3" style="opacity:0.75" />
        <circle :cx="sx(p.w)" :cy="sy(p.L)" r="9"
                fill="var(--ann-circuit)" stroke="var(--ann-paper)" stroke-width="2.5" />
        <text :x="sx(p.w)" :y="sy(p.L) - 20" class="stepnum" text-anchor="middle">{{ i }}</text>
      </g>

      <!-- verdict caption, after the last step -->
      <text v-click="from + steps.length - 1"
            x="322" :y="H - 8" class="verdict" :class="variant" text-anchor="middle">
        {{ caption }}
      </text>
    </svg>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  // 'good'      — converges smoothly
  // 'tiny'      — learning rate far too small, creeps
  // 'overshoot' — learning rate far too large, diverges
  variant: { type: String, default: 'good' },
  from: { type: Number, default: 1 },
  compact: { type: Boolean, default: false },
})

const H = computed(() => (props.compact ? 230 : 300))
const BASE = computed(() => H.value - 40)
const MIN = 5

// L(w) = 0.06 (w - 5)^2 + 0.4   ->   L'(w) = 0.12 (w - 5)
const loss = (w) => 0.06 * (w - MIN) ** 2 + 0.4
const grad = (w) => 0.12 * (w - MIN)

const sx = (w) => 50 + (w / 10) * 545
const sy = (L) => BASE.value - ((L - 0.4) / 1.5) * (BASE.value - 50)
// slope converted to screen space, for drawing the tangent
const slopeScreen = (w) => grad(w) * ((BASE.value - 50) / 1.5) / 54.5

const CONFIG = {
  good:      { w0: 0.6, eta: 2.5,  n: 5 },
  tiny:      { w0: 0.6, eta: 0.6,  n: 5 },
  overshoot: { w0: 1.0, eta: 15.8, n: 5 },
}

const steps = computed(() => {
  const { w0, eta, n } = CONFIG[props.variant] ?? CONFIG.good
  const out = []
  let w = w0
  for (let i = 0; i < n; i++) {
    out.push({ w, L: loss(w) })
    w = w - eta * grad(w)
    w = Math.max(-0.2, Math.min(10.2, w))   // keep it on canvas
  }
  return out
})

const caption = computed(() => ({
  good: 'Just right — each step lands closer, and the steps get smaller on their own.',
  tiny: 'Too small — it is heading the right way, and will take forever to arrive.',
  overshoot: 'Too large — it leaps past the minimum every time, and the loss grows.',
}[props.variant]))

const curve = computed(() => {
  const pts = []
  for (let w = 0; w <= 10.001; w += 0.25) pts.push(`${sx(w).toFixed(1)},${sy(loss(w)).toFixed(1)}`)
  return 'M' + pts.join(' L')
})
</script>

<style scoped>
.landscape { width: 100%; }
.landscape svg { width: 100%; height: auto; display: block; max-height: 29vh; }

.ax {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 12px;
  fill: var(--ann-muted);
}
.ax.mid { fill: var(--ann-indigo); }

.stepnum {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 13px;
  font-weight: 600;
  fill: var(--ann-circuit);
}

.verdict {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 14px;
  font-weight: 600;
  fill: var(--ann-ink-soft);
}
.verdict.overshoot { fill: var(--ann-ember); }
.verdict.good { fill: var(--ann-circuit); }
</style>
