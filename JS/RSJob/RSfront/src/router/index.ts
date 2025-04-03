import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'

// createRouter 创建路由实例，===> new VueRouter()
// history 是路由模式，hash模式，history模式
// createWebHistory() 是开启history模块 
// createWebHashHistory() 是开启hash模式   

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: () => import('../views/main.vue')
  },
  {
    path: '/changedetectHome',
    name: 'changedetectHome',
    component: () => import('../views/RSChangeDetect/HomePage/index.vue')
  },
  {
    path: '/changedetectMain',
    name: 'changedetectMain',
    component: () => import('../views/RSChangeDetect/Detect/index.vue')
  },
  {
    path: '/landclassHome',
    name: 'landclassHome',
    component: () => import('../views/RSLandClassific/HomePage/index.vue')
  },
  {
    path: '/landclassMain',
    name: 'landclassMain',
    component: () => import('../views/RSLandClassific/Detect/index.vue')
  },
  {
    path: '/objectdetectHome',
    name: 'objectdetectHome',
    component: () => import('../views/RSObjectDetect/HomePage/index.vue')
  },
  {
    path: '/objectdetectMain',
    name: 'objectdetectMain',
    component: () => import('../views/RSObjectDetect/Detect/index.vue')
  },
  {
    path: '/roadextractHome',
    name: 'roadextractHome',
    component: () => import('../views/RSRoadExtract/HomePage/index.vue')
  },
  {
    path: '/roadextractMain',
    name: 'roadextractMain',
    component: () => import('../views/RSRoadExtract/Detect/index.vue')
  }
] as RouteRecordRaw[]
const router = createRouter({
  history: createWebHistory(),
  routes: routes
})

export default router