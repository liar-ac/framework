<template>
  <div
    class="min-h-screen flex items-center justify-center p-4 bg-slate-50 dark:bg-[#131314]"
  >
    <div class="text-center">
      <div
        class="w-20 h-20 rounded-3xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center mx-auto mb-6"
      >
        <FileQuestion :size="36" class="text-slate-400 dark:text-slate-500" />
      </div>
      <h1 class="text-5xl font-bold text-slate-900 dark:text-slate-100 mb-2">404</h1>
      <p class="text-slate-500 dark:text-slate-400 mb-6">
        The page you're looking for doesn't exist.
      </p>
      <AppButton @click="$router.push('/')">
        <Home :size="16" />
        Back to Home
      </AppButton>
    </div>
  </div>
</template>

<script setup>
import AppButton from '../components/ui/AppButton.vue'
import { FileQuestion, Home } from 'lucide-vue-next'
</script>
