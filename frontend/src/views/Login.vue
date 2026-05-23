<template>
  <div
    class="min-h-screen flex items-center justify-center p-4 bg-slate-50 dark:bg-[#131314] relative overflow-hidden"
  >
    <div
      class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-gradient-to-br from-blue-500/8 via-indigo-500/8 to-violet-500/8 rounded-full blur-3xl pointer-events-none"
    />

    <div class="relative w-full max-w-[400px]">
      <div class="flex flex-col items-center mb-8">
        <div
          class="w-12 h-12 rounded-2xl bg-gradient-to-br from-blue-500 via-indigo-500 to-violet-500 flex items-center justify-center shadow-sm mb-4"
        >
          <Layers :size="22" class="text-white" />
        </div>
        <h1 class="text-xl font-bold text-slate-900 dark:text-slate-100">
          Welcome back
        </h1>
        <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">
          Sign in to your account
        </p>
      </div>

      <div
        class="rounded-2xl border border-slate-200/60 dark:border-slate-800 bg-white dark:bg-slate-900 p-6 shadow-[0_1px_3px_rgba(15,23,42,0.04)]"
      >
        <form @submit.prevent="handleLogin" class="space-y-4">
          <AppInput
            v-model="form.username"
            label="Username"
            placeholder="Enter your username"
          />
          <AppInput
            v-model="form.password"
            label="Password"
            type="password"
            placeholder="Enter your password"
          />

          <div
            v-if="errMsg"
            class="flex items-center gap-2 px-3 py-2.5 rounded-xl bg-red-50 dark:bg-red-500/10 border border-red-200 dark:border-red-500/20"
          >
            <AlertCircle :size="16" class="text-red-500 shrink-0" />
            <p class="text-sm text-red-600 dark:text-red-400">{{ errMsg }}</p>
          </div>

          <AppButton type="submit" :loading="loading" class="w-full">
            Sign in
          </AppButton>
        </form>

        <p class="mt-5 text-center text-sm text-slate-500 dark:text-slate-400">
          Don't have an account?
          <router-link
            to="/register"
            class="font-medium text-blue-600 dark:text-blue-400 hover:underline"
          >
            Sign up
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'
import AppInput from '../components/ui/AppInput.vue'
import AppButton from '../components/ui/AppButton.vue'
import { Layers, AlertCircle } from 'lucide-vue-next'

const router = useRouter()
const userStore = useUserStore()

const form = reactive({ username: '', password: '' })
const loading = ref(false)
const errMsg = ref('')

async function handleLogin() {
  loading.value = true
  errMsg.value = ''
  try {
    await userStore.login(form)
    router.push('/')
  } catch (e) {
    errMsg.value = e.message
  } finally {
    loading.value = false
  }
}
</script>
