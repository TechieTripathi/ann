<template>
  <div class="callout">
    <div class="callout-row wrong">
      <div class="callout-icon"><ph-x-circle-fill /></div>
      <div class="callout-body">
        <div class="callout-label">Common misconception</div>
        <div class="callout-text"><slot name="misconception" /></div>
      </div>
    </div>
    <div class="callout-row right">
      <div class="callout-icon"><ph-check-circle-fill /></div>
      <div class="callout-body">
        <div class="callout-label">Clarification</div>
        <div class="callout-text"><slot name="clarification" /></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.callout {
  border-radius: 0.6rem;
  overflow: hidden;
  border: 1px solid var(--ann-line);
  font-size: 0.92rem;
}

.callout-row {
  display: flex;
  gap: 0.7em;
  padding: 0.7em 1em;
  align-items: flex-start;
}

.callout-row.wrong {
  background: var(--ann-ember-soft);
  border-left: 4px solid var(--ann-ember);
}

.callout-row.right {
  background: var(--ann-circuit-soft);
  border-left: 4px solid var(--ann-circuit);
}

.callout-icon {
  flex-shrink: 0;
  font-size: 1.2em;
  line-height: 1.3;
  margin-top: 0.05em;
}

.callout-row.wrong .callout-icon {
  color: var(--ann-ember);
}

.callout-row.right .callout-icon {
  color: var(--ann-circuit);
}

.callout-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ann-ink-soft);
  margin-bottom: 0.15em;
}

.callout-text :deep(p) {
  margin: 0;
}

.callout-text :deep(strong) {
  color: inherit;
}
</style>
