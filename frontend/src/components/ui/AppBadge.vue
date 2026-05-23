<template>
  <span
    :class="[
      'inline-flex items-center gap-1 px-2 py-0.5 text-xs font-medium rounded-full',
      variantClasses[variant] || variantClasses.neutral,
    ]"
  >
    <span v-if="dot" :class="['w-1.5 h-1.5 rounded-full', dotClasses[variant] || dotClasses.neutral]" />
    <slot />
  </span>
</template>

<script setup>
defineProps({
  variant: { type: String, default: 'neutral' },
  dot: { type: Boolean, default: false },
})

const variantClasses = {
  success: 'bg-emerald-50 text-emerald-700 dark:bg-emerald-500/10 dark:text-emerald-400',
  warning: 'bg-amber-50 text-amber-700 dark:bg-amber-500/10 dark:text-amber-400',
  danger: 'bg-red-50 text-red-700 dark:bg-red-500/10 dark:text-red-400',
  info: 'bg-blue-50 text-blue-700 dark:bg-blue-500/10 dark:text-blue-400',
  neutral: 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400',
}

const dotClasses = {
  success: 'bg-emerald-500',
  warning: 'bg-amber-500',
  danger: 'bg-red-500',
  info: 'bg-blue-500',
  neutral: 'bg-slate-400',
}
</script>
