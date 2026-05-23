<template>
  <div class="space-y-6">
    <PageHeader title="系统" description="系统配置与模块管理">
      <template #actions>
        <AppButton variant="secondary" size="sm">
          <RefreshCw :size="14" />
          刷新
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

    <AppCard title="系统模块" description="可用的管理模块">
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

    <AppCard title="运行环境" description="当前运行环境详情">
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
  { label: '后端框架', value: 'Django 5.x', icon: Server, iconBg: 'bg-emerald-50 dark:bg-emerald-500/10', iconColor: 'text-emerald-500' },
  { label: '前端框架', value: 'Vue 3 + Vite', icon: Globe, iconBg: 'bg-blue-50 dark:bg-blue-500/10', iconColor: 'text-blue-500' },
  { label: '数据库', value: 'SQLite / PostgreSQL', icon: Database, iconBg: 'bg-violet-50 dark:bg-violet-500/10', iconColor: 'text-violet-500' },
]

const modules = [
  { label: '用户管理', description: '管理用户、角色与权限', icon: Users, iconBg: 'bg-blue-50 dark:bg-blue-500/10', iconColor: 'text-blue-500', status: '运行中', statusVariant: 'success' },
  { label: '身份认证', description: '基于 JWT Token 的认证系统', icon: Key, iconBg: 'bg-violet-50 dark:bg-violet-500/10', iconColor: 'text-violet-500', status: '运行中', statusVariant: 'success' },
  { label: 'API 网关', description: 'RESTful API 与代理转发', icon: Globe, iconBg: 'bg-emerald-50 dark:bg-emerald-500/10', iconColor: 'text-emerald-500', status: '运行中', statusVariant: 'success' },
  { label: '审计日志', description: '系统事件记录与查询', icon: FileText, iconBg: 'bg-amber-50 dark:bg-amber-500/10', iconColor: 'text-amber-500', status: '规划中', statusVariant: 'neutral' },
  { label: '安全防护', description: 'CORS、限流、CSRF 防护', icon: Shield, iconBg: 'bg-red-50 dark:bg-red-500/10', iconColor: 'text-red-500', status: '运行中', statusVariant: 'success' },
  { label: '数据备份', description: '数据库备份与恢复', icon: HardDrive, iconBg: 'bg-slate-100 dark:bg-slate-800', iconColor: 'text-slate-500', status: '规划中', statusVariant: 'neutral' },
]

const envInfo = [
  { key: 'API 基础地址', value: import.meta.env.VITE_API_BASE_URL || '/api' },
  { key: '应用版本', value: '1.0.0' },
  { key: '构建模式', value: import.meta.env.MODE },
  { key: '技术栈', value: 'Vue 3.4 + Vite 5' },
]
</script>
