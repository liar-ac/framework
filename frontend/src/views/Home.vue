<template>
  <div class="space-y-6">
    <PageHeader title="Home" description="Your profile and account overview" />

    <AppCard v-if="userStore.userInfo">
      <div class="flex flex-col sm:flex-row items-start gap-5">
        <div
          class="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-400 to-violet-500 flex items-center justify-center text-white text-xl font-bold shadow-sm"
        >
          {{ userInitial }}
        </div>
        <div class="flex-1 space-y-4">
          <div>
            <h3 class="text-lg font-bold text-slate-900 dark:text-slate-100">
              {{ userStore.userInfo.username }}
            </h3>
            <p class="text-sm text-slate-500 dark:text-slate-400">
              {{ userStore.userInfo.email || 'No email set' }}
            </p>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div class="space-y-1">
              <p class="text-xs font-medium text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                Nickname
              </p>
              <p class="text-sm text-slate-700 dark:text-slate-300">
                {{ userStore.userInfo.nickname || 'Not set' }}
              </p>
            </div>
            <div class="space-y-1">
              <p class="text-xs font-medium text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                Joined
              </p>
              <p class="text-sm text-slate-700 dark:text-slate-300">
                {{ userStore.userInfo.date_joined || 'Unknown' }}
              </p>
            </div>
            <div class="space-y-1">
              <p class="text-xs font-medium text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                Role
              </p>
              <AppBadge variant="info">Member</AppBadge>
            </div>
          </div>
        </div>
      </div>
    </AppCard>

    <AppCard v-else>
      <EmptyState
        :icon="UserCircle"
        title="No user data"
        description="Unable to load user information. Please try logging in again."
      >
        <AppButton variant="secondary" size="sm" @click="retryFetch">
          <RefreshCw :size="14" />
          Retry
        </AppButton>
      </EmptyState>
    </AppCard>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
      <AppCard v-for="stat in accountStats" :key="stat.label">
        <div class="flex items-center gap-3">
          <div
            class="w-10 h-10 rounded-xl flex items-center justify-center"
            :class="stat.iconBg"
          >
            <component :is="stat.icon" :size="18" :class="stat.iconColor" />
          </div>
          <div>
            <p class="text-xs text-slate-500 dark:text-slate-400">{{ stat.label }}</p>
            <p class="text-lg font-bold text-slate-900 dark:text-slate-100">{{ stat.value }}</p>
          </div>
        </div>
      </AppCard>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useUserStore } from '../stores/user'
import PageHeader from '../components/ui/PageHeader.vue'
import AppCard from '../components/ui/AppCard.vue'
import AppBadge from '../components/ui/AppBadge.vue'
import AppButton from '../components/ui/AppButton.vue'
import EmptyState from '../components/ui/EmptyState.vue'
import { UserCircle, Shield, Clock, Activity, RefreshCw } from 'lucide-vue-next'

const userStore = useUserStore()

const userInitial = computed(() => {
  const name = userStore.userInfo?.username || 'U'
  return name.charAt(0).toUpperCase()
})

const accountStats = [
  { label: 'Account Status', value: 'Active', icon: Shield, iconBg: 'bg-emerald-50 dark:bg-emerald-500/10', iconColor: 'text-emerald-500' },
  { label: 'Last Login', value: 'Today', icon: Clock, iconBg: 'bg-blue-50 dark:bg-blue-500/10', iconColor: 'text-blue-500' },
  { label: 'Sessions', value: '1', icon: Activity, iconBg: 'bg-violet-50 dark:bg-violet-500/10', iconColor: 'text-violet-500' },
]

async function retryFetch() {
  try {
    await userStore.fetchUserInfo()
  } catch {
    // handled by interceptor
  }
}

onMounted(async () => {
  if (!userStore.userInfo) {
    try {
      await userStore.fetchUserInfo()
    } catch {
      // handled by interceptor
    }
  }
})
</script>
