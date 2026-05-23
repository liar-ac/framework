<template>
  <div class="auth-page">
    <div class="auth-card">
      <h2 class="auth-title">注册</h2>
      <form @submit.prevent="handleRegister">
        <div class="form-group">
          <label>用户名</label>
          <input v-model="form.username" type="text" placeholder="请输入用户名" required />
        </div>
        <div class="form-group">
          <label>邮箱</label>
          <input v-model="form.email" type="email" placeholder="请输入邮箱（选填）" />
        </div>
        <div class="form-group">
          <label>密码</label>
          <input v-model="form.password" type="password" placeholder="请输入密码（至少6位）" required minlength="6" />
        </div>
        <div class="form-group">
          <label>确认密码</label>
          <input v-model="form.password2" type="password" placeholder="请再次输入密码" required minlength="6" />
        </div>
        <p v-if="errMsg" class="error-msg">{{ errMsg }}</p>
        <button type="submit" class="btn-primary" :disabled="loading">
          {{ loading ? '注册中...' : '注 册' }}
        </button>
      </form>
      <p class="auth-link">已有账号？<router-link to="/login">去登录</router-link></p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'

const router = useRouter()
const userStore = useUserStore()

const form = reactive({ username: '', email: '', password: '', password2: '' })
const loading = ref(false)
const errMsg = ref('')

async function handleRegister() {
  loading.value = true
  errMsg.value = ''
  try {
    await userStore.register(form)
    router.push('/')
  } catch (e) {
    errMsg.value = e.message
  } finally {
    loading.value = false
  }
}
</script>
