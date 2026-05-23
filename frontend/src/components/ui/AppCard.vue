<template>
  <div
    class="rounded-2xl border border-slate-200/60 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-[0_1px_3px_rgba(15,23,42,0.04)] dark:shadow-none"
  >
    <div v-if="title || description || $slots.header" class="px-5 pt-5 pb-0">
      <slot name="header">
        <h3 v-if="title" class="text-base font-semibold text-slate-900 dark:text-slate-100">
          {{ title }}
        </h3>
        <p v-if="description" class="mt-1 text-sm text-slate-500 dark:text-slate-400">
          {{ description }}
        </p>
      </slot>
    </div>
    <div :class="['px-5', title || description || $slots.header ? 'pt-3 pb-5' : 'py-5']">
      <slot />
    </div>
    <div v-if="$slots.footer" class="px-5 pb-5 pt-0">
      <slot name="footer" />
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: '' },
  description: { type: String, default: '' },
})
</script>
