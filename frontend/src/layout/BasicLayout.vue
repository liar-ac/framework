<template>
  <div class="flex h-screen overflow-hidden">
    <SideMenu :mobile-open="sidebarOpen" @close="sidebarOpen = false" />
    <div class="flex-1 flex flex-col min-w-0 overflow-hidden">
      <HeaderBar @toggle-sidebar="sidebarOpen = !sidebarOpen" />
      <main class="flex-1 overflow-y-auto">
        <div class="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8">
          <router-view />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import HeaderBar from '../components/HeaderBar.vue'
import SideMenu from '../components/SideMenu.vue'

const sidebarOpen = ref(false)
</script>
