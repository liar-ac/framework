<template>
  <div class="page">
    <h1>首页</h1>
    <div class="card" v-if="userStore.userInfo">
      <p><strong>用户名：</strong>{{ userStore.userInfo.username }}</p>
      <p><strong>邮箱：</strong>{{ userStore.userInfo.email || '未设置' }}</p>
      <p><strong>昵称：</strong>{{ userStore.userInfo.nickname || '未设置' }}</p>
      <p><strong>注册时间：</strong>{{ userStore.userInfo.date_joined }}</p>
    </div>
    <div class="card" v-else>
      <p>加载用户信息中...</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '../stores/user'

const userStore = useUserStore()

onMounted(async () => {
  if (!userStore.userInfo) {
    try {
      await userStore.fetchUserInfo()
    } catch {
      // 请求失败会被拦截器处理
    }
  }
})
</script>
