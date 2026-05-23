<template>
  <div class="space-y-6">
    <PageHeader title="设置" description="管理应用偏好与配置参数" />

    <AppCard title="通用设置" description="基础应用配置">
      <div class="space-y-5">
        <AppInput
          v-model="settings.apiBaseUrl"
          label="API 基础地址"
          placeholder="http://127.0.0.1:8000/api"
        />
        <AppInput
          v-model="settings.pageSize"
          label="默认分页大小"
          type="number"
          placeholder="20"
        />
      </div>
    </AppCard>

    <AppCard title="偏好设置" description="界面与通知设置">
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-900 dark:text-slate-100">
              启用通知
            </p>
            <p class="text-xs text-slate-500 dark:text-slate-400">
              接收系统和安全告警通知
            </p>
          </div>
          <AppSwitch v-model="settings.notifications" />
        </div>

        <div class="border-t border-slate-100 dark:border-slate-800" />

        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-900 dark:text-slate-100">
              主题偏好
            </p>
            <p class="text-xs text-slate-500 dark:text-slate-400">
              当前：{{ themeLabel }}
            </p>
          </div>
          <div class="flex gap-1.5">
            <button
              v-for="t in themes"
              :key="t.value"
              :class="[
                'px-3 py-1.5 text-xs font-medium rounded-lg transition-colors cursor-pointer',
                themeStore.theme === t.value
                  ? 'bg-blue-50 text-blue-600 dark:bg-blue-500/10 dark:text-blue-400'
                  : 'text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800',
              ]"
              @click="themeStore.setTheme(t.value)"
            >
              {{ t.label }}
            </button>
          </div>
        </div>
      </div>
    </AppCard>

    <div class="flex justify-end gap-3">
      <AppButton variant="secondary" @click="resetSettings">重置</AppButton>
      <AppButton :loading="saving" @click="saveSettings">
        <Save :size="15" />
        保存设置
      </AppButton>
    </div>

    <Transition name="toast">
      <div
        v-if="showToast"
        class="fixed bottom-6 right-6 flex items-center gap-2 px-4 py-2.5 rounded-xl bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-900 text-sm font-medium shadow-lg"
      >
        <CheckCircle :size="16" />
        设置已保存
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { reactive, ref, computed } from 'vue'
import { useThemeStore } from '../stores/theme'
import PageHeader from '../components/ui/PageHeader.vue'
import AppCard from '../components/ui/AppCard.vue'
import AppInput from '../components/ui/AppInput.vue'
import AppSwitch from '../components/ui/AppSwitch.vue'
import AppButton from '../components/ui/AppButton.vue'
import { Save, CheckCircle } from 'lucide-vue-next'

const themeStore = useThemeStore()

const themes = [
  { value: 'light', label: '浅色' },
  { value: 'dark', label: '深色' },
  { value: 'system', label: '跟随系统' },
]

const themeLabel = computed(() => {
  const map = { light: '浅色模式', dark: '深色模式', system: '跟随系统' }
  return map[themeStore.theme]
})

const settings = reactive({
  apiBaseUrl: localStorage.getItem('settings_apiBaseUrl') || '',
  pageSize: localStorage.getItem('settings_pageSize') || '20',
  notifications: localStorage.getItem('settings_notifications') !== 'false',
})

const saving = ref(false)
const showToast = ref(false)

async function saveSettings() {
  saving.value = true
  await new Promise((r) => setTimeout(r, 500))
  localStorage.setItem('settings_apiBaseUrl', settings.apiBaseUrl)
  localStorage.setItem('settings_pageSize', settings.pageSize)
  localStorage.setItem('settings_notifications', String(settings.notifications))
  saving.value = false
  showToast.value = true
  setTimeout(() => (showToast.value = false), 2500)
}

function resetSettings() {
  settings.apiBaseUrl = ''
  settings.pageSize = '20'
  settings.notifications = true
}
</script>

<style scoped>
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}
.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
