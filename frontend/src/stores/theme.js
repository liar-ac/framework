import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useThemeStore = defineStore('theme', () => {
  const theme = ref(localStorage.getItem('theme') || 'system')

  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  function getEffectiveTheme() {
    return theme.value === 'system' ? getSystemTheme() : theme.value
  }

  function applyTheme() {
    const effective = getEffectiveTheme()
    const html = document.documentElement
    html.classList.add('theme-transition')
    if (effective === 'dark') {
      html.classList.add('dark')
    } else {
      html.classList.remove('dark')
    }
    setTimeout(() => html.classList.remove('theme-transition'), 350)
  }

  function setTheme(newTheme) {
    theme.value = newTheme
    localStorage.setItem('theme', newTheme)
    applyTheme()
  }

  function toggleTheme() {
    const order = ['light', 'dark', 'system']
    const idx = order.indexOf(theme.value)
    setTheme(order[(idx + 1) % order.length])
  }

  if (typeof window !== 'undefined') {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
      if (theme.value === 'system') applyTheme()
    })
  }

  applyTheme()

  return { theme, setTheme, toggleTheme, getEffectiveTheme }
})
