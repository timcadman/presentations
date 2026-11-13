<script setup>
defineProps({
  height: {
    type: String,
    default: '16rem',
  },
  // output lines stay hidden until this is true, then appear one by one,
  // each at the time given by its own --t style
  start: {
    type: Boolean,
    default: true,
  },
})
</script>

<template>
  <!-- Content is anchored to the bottom, so as more output is revealed the
       oldest lines scroll off the top, as they would in a real terminal. -->
  <div class="term" :class="{ running: start }" :style="{ height }">
    <div class="term-lines">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.term {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  overflow: hidden;
  padding: 0.6rem 0.9rem;
  border-radius: 8px;
  background: #1E3A5F;
}

.term-lines :deep(pre) {
  margin: 0;
  padding: 0;
  background: transparent;
  font-family: var(--font-subtitle);
  font-size: 10.5px;
  line-height: 1.4;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  color: var(--slidev-theme-text-light);
}

.term-lines :deep(pre.out) {
  max-height: 0;
  opacity: 0;
  overflow: hidden;
}

/* Lines placed directly in the terminal start with the `start` prop. Lines
   wrapped in a `.stage` group start when that group is given the `go` class,
   so one slide can release its output in several steps. */
.term.running .term-lines > :deep(pre.out),
.term-lines :deep(.stage.go pre.out) {
  animation: term-line-in 0.01s linear var(--t, 0s) forwards;
}

/* Characters marked `.typed` appear one at a time within a line that is
   already showing, each at its own --t, to look like typing. They start
   when an enclosing element is given the `type-go` class. */
.term-lines :deep(.typed) {
  opacity: 0;
}

.term-lines :deep(.type-go .typed) {
  animation: term-char-in 0.01s linear var(--t, 0s) forwards;
}

@keyframes term-char-in {
  to {
    opacity: 1;
  }
}

@keyframes term-line-in {
  to {
    max-height: 12em;
    opacity: 1;
  }
}

.term-lines :deep(.cmd) {
  color: var(--slidev-theme-secondary);
  font-weight: 600;
}

.term-lines :deep(.dim) {
  color: #9AA0A6;
}
</style>
