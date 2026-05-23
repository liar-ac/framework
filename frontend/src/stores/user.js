/**
 * 用户状态管理（Pinia）
 */
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { login as loginApi, register as registerApi, getUserInfo as getUserInfoApi } from '../api/user'
import { setToken, setRefreshToken, clearTokens } from '../utils/auth'

export const useUserStore = defineStore('user', () => {
  const userInfo = ref(null)

  // 登录
  async function login(form) {
    const res = await loginApi(form)
    setToken(res.data.access)
    setRefreshToken(res.data.refresh)
    userInfo.value = res.data.user
    return res
  }

  // 注册
  async function register(form) {
    const res = await registerApi(form)
    setToken(res.data.access)
    setRefreshToken(res.data.refresh)
    userInfo.value = res.data.user
    return res
  }

  // 获取当前用户信息
  async function fetchUserInfo() {
    const res = await getUserInfoApi()
    userInfo.value = res.data
    return res
  }

  // 退出登录
  function logout() {
    userInfo.value = null
    clearTokens()
  }

  return { userInfo, login, register, fetchUserInfo, logout }
})
