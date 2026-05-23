<template>
  <div class="flex flex-col items-center justify-center py-16 text-center">
    <div class="w-16 h-16 rounded-2xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center mb-4">
      <component :is="icon" v-if="icon" :size="28" class="text-slate-400 dark:text-slate-500" />
      <Inbox v-else :size="28" class="text-slate-400 dark:text-slate-500" />
    </div>
    <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100 mb-1">
      {{ title || '暂无数据' }}
    </h3>
    <p class="text-sm text-slate-500 dark:text-slate-400 max-w-sm mb-6">
      {{ description || '这里暂时没有任何内容。' }}
    </p>
    <slot />
  </div>
</template>

<script setup>
import { Inbox } from 'lucide-vue-next'

defineProps({
  icon: { type: Object, default: null },
  title: { type: String, default: '' },
  description: { type: String, default: '' },
})
</script>
