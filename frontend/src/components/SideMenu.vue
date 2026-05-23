<template>
  <!-- Mobile overlay -->
  <Transition name="fade">
    <div
      v-if="mobileOpen"
      class="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm lg:hidden"
      @click="$emit('close')"
    />
  </Transition>

  <!-- Sidebar -->
  <aside
    :class="[
      'fixed lg:static inset-y-0 left-0 z-50 w-[260px] flex flex-col bg-white dark:bg-[#0f1115] border-r border-slate-200/60 dark:border-slate-800 transition-transform duration-300 ease-in-out',
      mobileOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0',
    ]"
  >
    <!-- Logo -->
    <div class="flex items-center gap-3 px-5 h-16 shrink-0">
      <div
        class="w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 via-indigo-500 to-violet-500 flex items-center justify-center shadow-sm"
      >
        <Layers :size="18" class="text-white" />
      </div>
      <div>
        <div class="text-sm font-bold text-slate-900 dark:text-slate-100 tracking-tight">
          Framework
        </div>
        <div class="text-[11px] text-slate-400 dark:text-slate-500 -mt-0.5">
          Django + Vue Starter
        </div>
      </div>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 px-3 py-4 space-y-1 overflow-y-auto">
      <router-link
        v-for="item in navItems"
        :key="item.to"
        :to="item.to"
        :class="[
          'flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all duration-200',
          isActive(item.to)
            ? 'bg-blue-50 text-blue-600 dark:bg-blue-500/10 dark:text-blue-400'
            : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800/60 hover:text-slate-900 dark:hover:text-slate-200',
        ]"
        @click="$emit('close')"
      >
        <component :is="item.icon" :size="18" :stroke-width="isActive(item.to) ? 2.2 : 1.8" />
        <span>{{ item.label }}</span>
      </router-link>
    </nav>

    <!-- User section -->
    <div class="border-t border-slate-200/60 dark:border-slate-800 p-3">
      <div
        class="flex items-center gap-3 px-3 py-2.5 rounded-xl hover:bg-slate-50 dark:hover:bg-slate-800/60 transition-colors cursor-pointer"
      >
        <div
          class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-400 to-violet-400 flex items-center justify-center text-white text-xs font-semibold"
        >
          {{ userInitial }}
        </div>
        <div class="flex-1 min-w-0">
          <div class="text-sm font-medium text-slate-900 dark:text-slate-100 truncate">
            {{ userStore.userInfo?.username || 'User' }}
          </div>
          <div class="text-[11px] text-slate-400 dark:text-slate-500 truncate">
            {{ userStore.userInfo?.email || 'user@framework.dev' }}
          </div>
        </div>
        <button
          class="p-1.5 rounded-lg text-slate-400 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-500/10 transition-colors cursor-pointer"
          title="Logout"
          @click="handleLogout"
        >
          <LogOut :size="16" />
        </button>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'
import {
  Layers,
  LayoutDashboard,
  Home,
  Settings,
  SlidersHorizontal,
  LogOut,
} from 'lucide-vue-next'

defineProps({
  mobileOpen: { type: Boolean, default: false },
})

defineEmits(['close'])

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const navItems = [
  { to: '/', label: 'Home', icon: Home },
  { to: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { to: '/system', label: 'System', icon: Settings },
  { to: '/settings', label: 'Settings', icon: SlidersHorizontal },
]

const userInitial = computed(() => {
  const name = userStore.userInfo?.username || 'U'
  return name.charAt(0).toUpperCase()
})

function isActive(path) {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}

function handleLogout() {
  userStore.logout()
  router.push('/login')
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
