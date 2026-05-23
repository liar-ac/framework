<template>
  <div class="layout">
    <SideMenu />
    <div class="layout-main">
      <HeaderBar />
      <div class="layout-content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import HeaderBar from '../components/HeaderBar.vue'
import SideMenu from '../components/SideMenu.vue'
</script>
