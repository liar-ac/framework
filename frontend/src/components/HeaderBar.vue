<template>
  <header
    class="sticky top-0 z-30 h-16 flex items-center justify-between px-4 sm:px-6 bg-white/80 dark:bg-[#131314]/80 backdrop-blur-xl border-b border-slate-200/60 dark:border-slate-800"
  >
    <!-- Left: mobile menu + page title -->
    <div class="flex items-center gap-3">
      <button
        class="p-2 rounded-xl text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 lg:hidden transition-colors cursor-pointer"
        @click="$emit('toggle-sidebar')"
      >
        <Menu :size="20" />
      </button>
      <div>
        <h2 class="text-sm font-semibold text-slate-900 dark:text-slate-100">
          {{ pageTitle }}
        </h2>
        <p class="text-xs text-slate-400 dark:text-slate-500 hidden sm:block">
          {{ pageDescription }}
        </p>
      </div>
    </div>

    <!-- Right: search, theme, user -->
    <div class="flex items-center gap-2">
      <!-- Search (desktop) -->
      <div class="hidden md:flex items-center">
        <div
          class="flex items-center gap-2 h-9 px-3.5 rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200/60 dark:border-slate-700 text-sm text-slate-400 dark:text-slate-500 cursor-pointer hover:border-slate-300 dark:hover:border-slate-600 transition-colors"
        >
          <Search :size="15" />
          <span class="text-xs">Search...</span>
          <kbd
            class="ml-4 px-1.5 py-0.5 text-[10px] font-medium bg-white dark:bg-slate-700 rounded border border-slate-200 dark:border-slate-600 text-slate-400"
          >
            Ctrl K
          </kbd>
        </div>
      </div>

      <!-- Theme toggle -->
      <button
        class="p-2 rounded-full text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
        :title="themeLabel"
        @click="themeStore.toggleTheme()"
      >
        <Sun v-if="effectiveTheme === 'light'" :size="18" />
        <Moon v-else-if="effectiveTheme === 'dark'" :size="18" />
        <Monitor v-else :size="18" />
      </button>

      <!-- Notification bell -->
      <button
        class="relative p-2 rounded-full text-slate-500 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
      >
        <Bell :size="18" />
        <span class="absolute top-1.5 right-1.5 w-2 h-2 bg-blue-500 rounded-full" />
      </button>

      <!-- User avatar (mobile) -->
      <div
        class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-400 to-violet-400 flex items-center justify-center text-white text-xs font-semibold lg:hidden"
      >
        {{ userInitial }}
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '../stores/user'
import { useThemeStore } from '../stores/theme'
import { Menu, Search, Sun, Moon, Monitor, Bell } from 'lucide-vue-next'

defineEmits(['toggle-sidebar'])

const route = useRoute()
const userStore = useUserStore()
const themeStore = useThemeStore()

const effectiveTheme = computed(() => themeStore.getEffectiveTheme())

const themeLabel = computed(() => {
  const map = { light: 'Light mode', dark: 'Dark mode', system: 'System theme' }
  return map[themeStore.theme]
})

const userInitial = computed(() => {
  const name = userStore.userInfo?.username || 'U'
  return name.charAt(0).toUpperCase()
})

const pageMeta = {
  '/': { title: 'Home', description: 'Your profile and account overview' },
  '/dashboard': { title: 'Dashboard', description: 'System overview and quick actions' },
  '/system': { title: 'System', description: 'System configuration and management' },
  '/settings': { title: 'Settings', description: 'Manage your application preferences' },
}

const pageTitle = computed(() => pageMeta[route.path]?.title || 'Framework')
const pageDescription = computed(() => pageMeta[route.path]?.description || '')
</script>
