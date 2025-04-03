import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  css: {
  },
  server: {
    proxy: {
      '/api': {
        // '/api'是代理标识，用于告诉node，url前面是/api的就是使用代理的
        ws: true,
        target: 'http://127.0.0.1:8000', //这里填入你要请求的接口的前缀
        changeOrigin: true,   //是否跨域
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
