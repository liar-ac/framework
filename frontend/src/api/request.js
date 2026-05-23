/**
 * Axios 请求封装
 * - 统一 baseURL
 * - 请求拦截器自动携带 token
 * - 响应拦截器统一错误处理
 */
import axios from 'axios'
import { getToken, getRefreshToken, setToken, clearTokens } from '../utils/auth'
import router from '../router'

const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 15000,
})

// 请求拦截器：自动携带 token
service.interceptors.request.use(
  (config) => {
    const token = getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// 响应拦截器：统一错误处理
service.interceptors.response.use(
  (response) => {
    const res = response.data
    // 后端统一返回 { code, message, data }
    if (res.code >= 200 && res.code < 300) {
      return res
    }
    // 业务错误
    const err = new Error(res.message || '请求失败')
    err.code = res.code
    return Promise.reject(err)
  },
  async (error) => {
    const originalRequest = error.config

    // 401 且未重试过，尝试用 refresh_token 刷新
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      const refreshToken = getRefreshToken()
      if (refreshToken) {
        try {
          const res = await axios.post(
            `${import.meta.env.VITE_API_BASE_URL}/users/token/refresh/`,
            { refresh: refreshToken }
          )
          const newToken = res.data.access
          setToken(newToken)
          originalRequest.headers.Authorization = `Bearer ${newToken}`
          return service(originalRequest)
        } catch {
          clearTokens()
          router.push('/login')
          return Promise.reject(error)
        }
      }
    }

    if (error.response?.status === 401) {
      clearTokens()
      router.push('/login')
    }

    const message = error.response?.data?.message || error.message || '网络错误'
    return Promise.reject(new Error(message))
  }
)

export default service
