/**
 * 用户相关 API
 */
import request from './request'

// 用户注册
export function register(data) {
  return request({ url: '/users/register/', method: 'post', data })
}

// 用户登录
export function login(data) {
  return request({ url: '/users/login/', method: 'post', data })
}

// 刷新 token
export function refreshToken(refresh) {
  return request({ url: '/users/token/refresh/', method: 'post', data: { refresh } })
}

// 获取当前用户信息
export function getUserInfo() {
  return request({ url: '/users/me/', method: 'get' })
}

// 健康检查
export function healthCheck() {
  return request({ url: '/health/', method: 'get' })
}
