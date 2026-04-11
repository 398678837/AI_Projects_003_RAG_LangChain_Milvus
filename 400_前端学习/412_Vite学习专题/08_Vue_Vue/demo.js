// Vite + Vue 示例代码

// 1. 创建项目
const createVueProject = `
# JavaScript 版本
npm create vite@latest my-vue-app -- --template vue
cd my-vue-app
npm install
npm run dev

# TypeScript 版本
npm create vite@latest my-vue-app -- --template vue-ts
cd my-vue-app
npm install
npm run dev

# 使用 pnpm
pnpm create vite my-vue-app --template vue-ts
`;

console.log('=== 创建 Vue 项目 ===');
console.log(createVueProject);

// 2. vite.config.js 配置
const viteConfigVue = `
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag.startsWith('my-')
        }
      },
      reactivityTransform: true
    })
  ],
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  
  server: {
    port: 3000,
    open: true
  }
})
`;

console.log('\n=== vite.config.js 配置 ===');
console.log(viteConfigVue);

// 3. 项目结构
const vueProjectStructure = `
my-vue-app/
├── public/
│   └── favicon.ico
├── src/
│   ├── assets/
│   │   └── logo.svg
│   ├── components/
│   │   └── HelloWorld.vue
│   ├── App.vue
│   ├── main.js
│   └── style.css
├── .gitignore
├── index.html
├── package.json
├── vite.config.js
└── README.md
`;

console.log('\n=== 项目结构 ===');
console.log(vueProjectStructure);

// 4. main.js
const mainJs = `
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App).mount('#app')
`;

console.log('\n=== main.js ===');
console.log(mainJs);

// 5. App.vue
const appVue = `
<script setup>
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'

const count = ref(0)
</script>

<template>
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" />
  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
`;

console.log('\n=== App.vue ===');
console.log(appVue);

// 6. HelloWorld.vue
const helloWorldVue = `
<script setup>
defineProps({
  msg: String
})
</script>

<template>
  <h1>{{ msg }}</h1>
  <div class="read-the-docs">
    Click on the Vite and Vue logos to learn more
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
`;

console.log('\n=== HelloWorld.vue ===');
console.log(helloWorldVue);

// 7. 使用环境变量
const envUsageVue = `
// .env
VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My Vue App

// 在组件中使用
<script setup>
const apiUrl = import.meta.env.VITE_API_URL
const title = import.meta.env.VITE_APP_TITLE

console.log('API URL:', apiUrl)
</script>

<template>
  <div>
    <h1>{{ title }}</h1>
  </div>
</template>

// 检查环境
if (import.meta.env.DEV) {
  console.log('开发环境')
}
if (import.meta.env.PROD) {
  console.log('生产环境')
}
`;

console.log('\n=== 使用环境变量 ===');
console.log(envUsageVue);

// 8. 路由配置
const vueRouter = `
// 安装
npm install vue-router@4

// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
`;

console.log('\n=== 路由配置 ===');
console.log(vueRouter);

// 9. 完整的 vite.config.ts (TypeScript)
const fullViteConfigVueTs = `
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag.startsWith('my-')
        }
      }
    })
  ],
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@views': path.resolve(__dirname, './src/views'),
      '@composables': path.resolve(__dirname, './src/composables'),
      '@utils': path.resolve(__dirname, './src/utils'),
      '@assets': path.resolve(__dirname, './src/assets')
    }
  },
  
  server: {
    port: 3000,
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  },
  
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia']
        }
      }
    }
  }
})
`;

console.log('\n=== 完整的 vite.config.ts ===');
console.log(fullViteConfigVueTs);
