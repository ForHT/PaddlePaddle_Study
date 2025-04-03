<template>
  <header class="navbar">
    <img src="./assets/vue.svg" alt="Logo" class="logo">
    <nav class="nav-center">
      <RouterLink to="/" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">首页</span>
      </RouterLink>
      <RouterLink to="/changedetectHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">变化检测</span>
      </RouterLink>
      <RouterLink to="/objectdetectHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">目标检测</span>
      </RouterLink>
      <RouterLink to="/roadextractHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">道路提取</span>
      </RouterLink>
      <RouterLink to="/landclassHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">地物分类</span>
      </RouterLink>
    </nav>
  </header>
  <main class="main-content">
    <RouterView />
  </main>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f8f9fa;
  padding: 1rem;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.logo {
  height: 90%;
  padding: 0.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.nav-center {
  display: flex;
  align-items: center;
  gap: 1rem; /* 添加间距 */
}

.nav-link {
  text-decoration: none;
  color: #343a40;
  transition: color 0.3s ease;
}

.active { /* 高亮当前激活的路由 */
  color: #007bff;
  font-weight: bold;
}

.nav-link:hover {
  color: #007bff;
}
</style>