<template>
  <div class="space-y-6">
    <PageHeader title="控制台" description="系统概览与快捷操作" />

    <!-- Hero Welcome Card -->
    <div
      class="relative overflow-hidden rounded-2xl border border-slate-200/60 dark:border-slate-800 bg-white dark:bg-slate-900 p-6 sm:p-8"
    >
      <div
        class="absolute -top-24 -right-24 w-64 h-64 bg-gradient-to-br from-blue-500/15 via-indigo-500/15 to-violet-500/15 rounded-full blur-3xl pointer-events-none"
      />
      <div
        class="absolute -bottom-16 -left-16 w-48 h-48 bg-gradient-to-tr from-violet-500/8 to-blue-500/8 rounded-full blur-3xl pointer-events-none"
      />

      <div class="relative">
        <h2 class="text-xl sm:text-2xl font-bold text-slate-900 dark:text-slate-100">
          欢迎回来
        </h2>
        <p class="mt-2 text-sm text-slate-500 dark:text-slate-400 max-w-lg">
          一个现代化的 Django + Vue 3 开发框架已经准备就绪，开始构建你的下一个项目吧。
        </p>
        <div class="mt-5 flex flex-wrap gap-3">
          <AppButton size="sm">
            <Rocket :size="15" />
            快速开始
          </AppButton>
          <AppButton variant="secondary" size="sm">
            <BookOpen :size="15" />
            查看文档
          </AppButton>
        </div>
      </div>
    </div>

    <!-- Stats Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <AppCard v-for="stat in stats" :key="stat.label">
        <div class="flex items-start justify-between">
          <div>
            <p class="text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">
              {{ stat.label }}
            </p>
            <p class="mt-2 text-2xl font-bold text-slate-900 dark:text-slate-100">
              {{ stat.value }}
            </p>
          </div>
          <div
            class="w-10 h-10 rounded-xl flex items-center justify-center"
            :class="stat.iconBg"
          >
            <component :is="stat.icon" :size="20" :class="stat.iconColor" />
          </div>
        </div>
        <div class="mt-3">
          <AppBadge :variant="stat.badgeVariant" dot>
            {{ stat.badge }}
          </AppBadge>
        </div>
      </AppCard>
    </div>

    <!-- Quick Actions + Recent Activity -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
      <!-- Quick Actions -->
      <AppCard title="快捷操作" description="常用功能入口" class="lg:col-span-1">
        <div class="space-y-2">
          <button
            v-for="action in quickActions"
            :key="action.label"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800/60 transition-colors text-left cursor-pointer"
          >
            <div
              class="w-8 h-8 rounded-lg flex items-center justify-center"
              :class="action.iconBg"
            >
              <component :is="action.icon" :size="16" :class="action.iconColor" />
            </div>
            <span class="font-medium">{{ action.label }}</span>
            <ChevronRight :size="14" class="ml-auto text-slate-300 dark:text-slate-600" />
          </button>
        </div>
      </AppCard>

      <!-- Recent Activity -->
      <AppCard title="最近动态" description="系统最新事件" class="lg:col-span-2">
        <div class="space-y-1">
          <div
            v-for="activity in recentActivity"
            :key="activity.id"
            class="flex items-center gap-3 px-3 py-3 rounded-xl hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors"
          >
            <div
              class="w-9 h-9 rounded-xl flex items-center justify-center shrink-0"
              :class="activity.iconBg"
            >
              <component :is="activity.icon" :size="16" :class="activity.iconColor" />
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-slate-900 dark:text-slate-100 truncate">
                {{ activity.title }}
              </p>
              <p class="text-xs text-slate-400 dark:text-slate-500">
                {{ activity.time }}
              </p>
            </div>
            <AppBadge :variant="activity.badgeVariant">
              {{ activity.badge }}
            </AppBadge>
          </div>
        </div>
      </AppCard>
    </div>
  </div>
</template>

<script setup>
import PageHeader from '../components/ui/PageHeader.vue'
import AppCard from '../components/ui/AppCard.vue'
import AppButton from '../components/ui/AppButton.vue'
import AppBadge from '../components/ui/AppBadge.vue'
import {
  Rocket,
  BookOpen,
  Activity,
  Users,
  Server,
  CheckCircle,
  UserPlus,
  Code,
  Settings,
  FileText,
  ChevronRight,
  Shield,
  Zap,
  RefreshCw,
} from 'lucide-vue-next'

const stats = [
  {
    label: '后端状态',
    value: '运行中',
    icon: Server,
    iconBg: 'bg-emerald-50 dark:bg-emerald-500/10',
    iconColor: 'text-emerald-500',
    badge: '正常',
    badgeVariant: 'success',
  },
  {
    label: 'API 请求数',
    value: '12.8k',
    icon: Activity,
    iconBg: 'bg-blue-50 dark:bg-blue-500/10',
    iconColor: 'text-blue-500',
    badge: '+18%',
    badgeVariant: 'info',
  },
  {
    label: '用户数',
    value: '1,248',
    icon: Users,
    iconBg: 'bg-violet-50 dark:bg-violet-500/10',
    iconColor: 'text-violet-500',
    badge: '今日 +42',
    badgeVariant: 'neutral',
  },
  {
    label: '构建状态',
    value: '已通过',
    icon: CheckCircle,
    iconBg: 'bg-emerald-50 dark:bg-emerald-500/10',
    iconColor: 'text-emerald-500',
    badge: 'v1.0.0',
    badgeVariant: 'success',
  },
]

const quickActions = [
  { label: '新增用户', icon: UserPlus, iconBg: 'bg-blue-50 dark:bg-blue-500/10', iconColor: 'text-blue-500' },
  { label: '查看接口', icon: Code, iconBg: 'bg-violet-50 dark:bg-violet-500/10', iconColor: 'text-violet-500' },
  { label: '系统设置', icon: Settings, iconBg: 'bg-slate-100 dark:bg-slate-800', iconColor: 'text-slate-500' },
  { label: '查看日志', icon: FileText, iconBg: 'bg-amber-50 dark:bg-amber-500/10', iconColor: 'text-amber-500' },
]

const recentActivity = [
  {
    id: 1,
    icon: Shield,
    iconBg: 'bg-blue-50 dark:bg-blue-500/10',
    iconColor: 'text-blue-500',
    title: '系统安全扫描已完成',
    time: '2 分钟前',
    badge: '已通过',
    badgeVariant: 'success',
  },
  {
    id: 2,
    icon: Users,
    iconBg: 'bg-violet-50 dark:bg-violet-500/10',
    iconColor: 'text-violet-500',
    title: '新用户注册：john@example.com',
    time: '15 分钟前',
    badge: '新用户',
    badgeVariant: 'info',
  },
  {
    id: 3,
    icon: Zap,
    iconBg: 'bg-amber-50 dark:bg-amber-500/10',
    iconColor: 'text-amber-500',
    title: 'API 请求频率达到阈值',
    time: '1 小时前',
    badge: '警告',
    badgeVariant: 'warning',
  },
  {
    id: 4,
    icon: RefreshCw,
    iconBg: 'bg-emerald-50 dark:bg-emerald-500/10',
    iconColor: 'text-emerald-500',
    title: '数据库备份已完成',
    time: '3 小时前',
    badge: '完成',
    badgeVariant: 'success',
  },
]
</script>
