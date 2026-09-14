<template>
  <div v-if="showFooter" class="ann-footer">
    <span class="ann-footer-chapter">{{ chapter }}</span>
    <span class="ann-footer-page">{{ nav.currentPage.value }} / {{ nav.total.value }}</span>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const nav = useNav()
const hiddenLayouts = ['cover', 'section', 'end', 'statement', 'quote']

// NOTE: $frontmatter does NOT resolve per-slide inside a global component -
// it always yielded the fallback, so this footer silently showed the deck
// name on every slide. Read the active slide's frontmatter off the route.
const frontmatter = computed(
  () => nav.currentSlideRoute.value?.meta?.slide?.frontmatter ?? {},
)
const chapter = computed(
  () => frontmatter.value.chapter || 'Artificial Neural Networks',
)
const showFooter = computed(
  () => !hiddenLayouts.includes(nav.currentLayout.value)
        && frontmatter.value.chapter !== '',
)
</script>

<style scoped>
.ann-footer {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: space-between;
  padding: 0.4rem 1.75rem;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.04em;
  color: var(--ann-muted);
  border-top: 1px solid var(--ann-line);
  z-index: 5;
  pointer-events: none;
}
</style>
