<template>
  <div class="biomap">
    <div class="biomap-side bio">
      <div class="biomap-eyebrow">Biological neuron</div>
      <div class="biomap-icon" v-if="bioIcon"><component :is="bioIcon" /></div>
      <div class="biomap-label"><slot name="bio">{{ bioLabel }}</slot></div>
      <div v-if="bioSub" class="biomap-sub">{{ bioSub }}</div>
    </div>

    <div class="biomap-arrow">
      <div class="biomap-arrow-line" />
      <div class="biomap-arrow-caption">{{ connector }}</div>
    </div>

    <div class="biomap-side ann">
      <div class="biomap-eyebrow">Artificial neuron</div>
      <div class="biomap-icon" v-if="annIcon"><component :is="annIcon" /></div>
      <div class="biomap-label"><slot name="ann">{{ annLabel }}</slot></div>
      <div v-if="annSub" class="biomap-sub">{{ annSub }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  bioLabel: { type: String, default: '' },
  bioSub: { type: String, default: '' },
  annLabel: { type: String, default: '' },
  annSub: { type: String, default: '' },
  bioIcon: { type: [String, Object], default: null },
  annIcon: { type: [String, Object], default: null },
  connector: { type: String, default: 'inspires' },
})
</script>

<style scoped>
.biomap {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: stretch;
  gap: 0.9em;
  margin: 0.5em 0;
}

.biomap-side {
  border-radius: 0.6rem;
  padding: 0.7em 1em;
  border: 1px solid var(--ann-line);
}

.biomap-side.bio {
  background: var(--ann-ember-soft);
  border-left: 4px solid var(--ann-ember);
}

.biomap-side.ann {
  background: var(--ann-circuit-soft);
  border-left: 4px solid var(--ann-circuit);
}

.biomap-eyebrow {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ann-ink-soft);
  margin-bottom: 0.3em;
}

.biomap-icon {
  font-size: 1.4em;
  margin-bottom: 0.15em;
}

.biomap-side.bio .biomap-icon {
  color: var(--ann-ember);
}

.biomap-side.ann .biomap-icon {
  color: var(--ann-circuit);
}

.biomap-label {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 1.05rem;
  color: var(--ann-ink);
}

.biomap-sub {
  font-size: 0.85rem;
  color: var(--ann-ink-soft);
  margin-top: 0.2em;
}

.biomap-arrow {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-width: 4.5em;
  gap: 0.2em;
}

.biomap-arrow-line {
  width: 100%;
  height: 2px;
  background: var(--ann-muted);
  position: relative;
}

.biomap-arrow-line::after {
  content: '';
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  border-style: solid;
  border-width: 5px 0 5px 7px;
  border-color: transparent transparent transparent var(--ann-muted);
}

.biomap-arrow-caption {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  color: var(--ann-muted);
  letter-spacing: 0.03em;
  white-space: nowrap;
}
</style>
