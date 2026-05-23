<template>
  <div class="space-y-6">
    <PageHeader title="System" description="System configuration and management">
      <template #actions>
        <AppButton variant="secondary" size="sm">
          <RefreshCw :size="14" />
          Refresh
        </AppButton>
      </template>
    </PageHeader>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <AppCard v-for="info in systemInfo" :key="info.label">
        <div class="flex items-center gap-3">
          <div
            class="w-10 h-10 rounded-xl flex items-center justify-center"
            :class="info.iconBg"
          >
            <component :is="info.icon" :size="18" :class="info.iconColor" />
          </div>
          <div>
            <p class="text-xs text-slate-500 dark:text-slate-400">{{ info.label }}</p>
            <p class="text-sm font-semibold text-slate-900 dark:text-slate-100">
              {{ info.value }}
            </p>
          </div>
        </div>
      </AppCard>
    </div>

    <AppCard title="System Modules" description="Available management modules">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div
          v-for="mod in modules"
          :key="mod.label"
          class="flex items-center gap-3 p-3 rounded-xl border border-slate-100 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors cursor-pointer"
        >
          <div
            class="w-9 h-9 rounded-lg flex items-center justify-center"
            :class="mod.iconBg"
          >
            <component :is="mod.icon" :size="16" :class="mod.iconColor" />
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-slate-900 dark:text-slate-100">
              {{ mod.label }}
            </p>
            <p class="text-xs text-slate-400 dark:text-slate-500 truncate">
              {{ mod.description }}
            </p>
          </div>
          <AppBadge :variant="mod.statusVariant">{{ mod.status }}</AppBadge>
        </div>
      </div>
    </AppCard>

    <AppCard title="Environment" description="Runtime environment details">
      <div class="space-y-3">
        <div
          v-for="env in envInfo"
          :key="env.key"
          class="flex items-center justify-between py-2 border-b border-slate-100 dark:border-slate-800 last:border-0"
        >
          <span class="text-sm text-slate-500 dark:text-slate-400">{{ env.key }}</span>
          <span class="text-sm font-mono text-slate-900 dark:text-slate-100">{{ env.value }}</span>
        </div>
      </div>
    </AppCard>
  </div>
</template>

<script setup>
import PageHeader from '../components/ui/PageHeader.vue'
import AppCard from '../components/ui/AppCard.vue'
import AppButton from '../components/ui/AppButton.vue'
import AppBadge from '../components/ui/AppBadge.vue'
import {
  RefreshCw,
  Server,
  Database,
  Shield,
  Globe,
  Users,
  Key,
  FileText,
  HardDrive,
} from 'lucide-vue-next'

const systemInfo = [
  { label: 'Backend', value: 'Django 5.x', icon: Server, iconBg: 'bg-emerald-50 dark:bg-emerald-500/10', iconColor: 'text-emerald-500' },
  { label: 'Frontend', value: 'Vue 3 + Vite', icon: Globe, iconBg: 'bg-blue-50 dark:bg-blue-500/10', iconColor: 'text-blue-500' },
  { label: 'Database', value: 'SQLite / PostgreSQL', icon: Database, iconBg: 'bg-violet-50 dark:bg-violet-500/10', iconColor: 'text-violet-500' },
]

const modules = [
  { label: 'User Management', description: 'Manage users, roles, and permissions', icon: Users, iconBg: 'bg-blue-50 dark:bg-blue-500/10', iconColor: 'text-blue-500', status: 'Active', statusVariant: 'success' },
  { label: 'Authentication', description: 'JWT token-based auth system', icon: Key, iconBg: 'bg-violet-50 dark:bg-violet-500/10', iconColor: 'text-violet-500', status: 'Active', statusVariant: 'success' },
  { label: 'API Gateway', description: 'RESTful API with proxy support', icon: Globe, iconBg: 'bg-emerald-50 dark:bg-emerald-500/10', iconColor: 'text-emerald-500', status: 'Active', statusVariant: 'success' },
  { label: 'Audit Logs', description: 'System event logging', icon: FileText, iconBg: 'bg-amber-50 dark:bg-amber-500/10', iconColor: 'text-amber-500', status: 'Planned', statusVariant: 'neutral' },
  { label: 'Security', description: 'CORS, rate limiting, CSRF', icon: Shield, iconBg: 'bg-red-50 dark:bg-red-500/10', iconColor: 'text-red-500', status: 'Active', statusVariant: 'success' },
  { label: 'Backup', description: 'Database backup and restore', icon: HardDrive, iconBg: 'bg-slate-100 dark:bg-slate-800', iconColor: 'text-slate-500', status: 'Planned', statusVariant: 'neutral' },
]

const envInfo = [
  { key: 'API Base URL', value: import.meta.env.VITE_API_BASE_URL || '/api' },
  { key: 'App Version', value: '1.0.0' },
  { key: 'Build Mode', value: import.meta.env.MODE },
  { key: 'Framework', value: 'Vue 3.4 + Vite 5' },
]
</script>
