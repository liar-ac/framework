<template>
  <div class="space-y-6">
    <PageHeader title="Settings" description="Manage your application preferences" />

    <AppCard title="General" description="Basic application settings">
      <div class="space-y-5">
        <AppInput
          v-model="settings.apiBaseUrl"
          label="API Base URL"
          placeholder="http://127.0.0.1:8000/api"
        />
        <AppInput
          v-model="settings.pageSize"
          label="Default Page Size"
          type="number"
          placeholder="20"
        />
      </div>
    </AppCard>

    <AppCard title="Preferences" description="Interface and notification settings">
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-900 dark:text-slate-100">
              Enable Notifications
            </p>
            <p class="text-xs text-slate-500 dark:text-slate-400">
              Receive system and security alerts
            </p>
          </div>
          <AppSwitch v-model="settings.notifications" />
        </div>

        <div class="border-t border-slate-100 dark:border-slate-800" />

        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-slate-900 dark:text-slate-100">
              Theme Preference
            </p>
            <p class="text-xs text-slate-500 dark:text-slate-400">
              Current: {{ themeStore.theme }}
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
      <AppButton variant="secondary" @click="resetSettings">Reset</AppButton>
      <AppButton :loading="saving" @click="saveSettings">
        <Save :size="15" />
        Save Changes
      </AppButton>
    </div>

    <Transition name="toast">
      <div
        v-if="showToast"
        class="fixed bottom-6 right-6 flex items-center gap-2 px-4 py-2.5 rounded-xl bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-900 text-sm font-medium shadow-lg"
      >
        <CheckCircle :size="16" />
        Settings saved locally
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useThemeStore } from '../stores/theme'
import PageHeader from '../components/ui/PageHeader.vue'
import AppCard from '../components/ui/AppCard.vue'
import AppInput from '../components/ui/AppInput.vue'
import AppSwitch from '../components/ui/AppSwitch.vue'
import AppButton from '../components/ui/AppButton.vue'
import { Save, CheckCircle } from 'lucide-vue-next'

const themeStore = useThemeStore()

const themes = [
  { value: 'light', label: 'Light' },
  { value: 'dark', label: 'Dark' },
  { value: 'system', label: 'System' },
]

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
