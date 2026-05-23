<template>
  <header class="header-bar">
    <span class="header-title">Framework</span>
    <div class="header-right">
      <span class="header-user">{{ userStore.userInfo?.username || '' }}</span>
      <button class="btn-logout" @click="handleLogout">退出</button>
    </div>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'

const router = useRouter()
const userStore = useUserStore()

function handleLogout() {
  userStore.logout()
  router.push('/login')
}
</script>
