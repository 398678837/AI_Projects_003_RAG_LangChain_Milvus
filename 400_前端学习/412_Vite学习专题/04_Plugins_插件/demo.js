// Vite 插件示例代码

// 1. Vue 插件
const vuePlugin = `
// 安装
npm install @vitejs/plugin-vue -D

// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag.startsWith('my-')
        }
      }
    })
  ]
})
`;

console.log('=== Vue 插件 ===');
console.log(vuePlugin);

// 2. React 插件
const reactPlugin = `
// 安装
npm install @vitejs/plugin-react -D

// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [
    react({
      babel: {
        plugins: ['babel-plugin-macros']
      }
    })
  ]
})

// 或者使用 react-swc（更快）
npm install @vitejs/plugin-react-swc -D
import react from '@vitejs/plugin-react-swc'
`;

console.log('\n=== React 插件 ===');
console.log(reactPlugin);

// 3. 常用插件列表
const commonPlugins = [
  {
    name: '@vitejs/plugin-vue',
    desc: 'Vue 3 支持',
    install: 'npm install @vitejs/plugin-vue -D'
  },
  {
    name: '@vitejs/plugin-react',
    desc: 'React 支持',
    install: 'npm install @vitejs/plugin-react -D'
  },
  {
    name: 'vite-plugin-compression',
    desc: 'gzip/brotli 压缩',
    install: 'npm install vite-plugin-compression -D'
  },
  {
    name: 'vite-plugin-pwa',
    desc: 'PWA 支持',
    install: 'npm install vite-plugin-pwa -D'
  },
  {
    name: 'vite-plugin-svg-icons',
    desc: 'SVG 图标管理',
    install: 'npm install vite-plugin-svg-icons -D'
  },
  {
    name: 'vite-plugin-md',
    desc: 'Markdown 作为组件',
    install: 'npm install vite-plugin-md -D'
  },
  {
    name: 'vite-plugin-eslint',
    desc: 'ESLint 检查',
    install: 'npm install vite-plugin-eslint -D'
  },
  {
    name: 'vite-plugin-style-import',
    desc: '样式按需导入',
    install: 'npm install vite-plugin-style-import -D'
  },
  {
    name: 'unplugin-auto-import',
    desc: '自动导入 API',
    install: 'npm install unplugin-auto-import -D'
  },
  {
    name: 'unplugin-vue-components',
    desc: 'Vue 组件自动注册',
    install: 'npm install unplugin-vue-components -D'
  }
];

console.log('\n=== 常用插件列表 ===');
commonPlugins.forEach(p => {
  console.log(`\n【${p.name}】`);
  console.log(`  说明: ${p.desc}`);
  console.log(`  安装: ${p.install}`);
});

// 4. Compression 插件
const compressionPlugin = `
import { defineConfig } from 'vite'
import viteCompression from 'vite-plugin-compression'

export default defineConfig({
  plugins: [
    viteCompression({
      verbose: true,
      disable: false,
      threshold: 10240,
      algorithm: 'gzip',
      ext: '.gz',
      
      // 或者使用 brotli
      // algorithm: 'brotliCompress',
      // ext: '.br',
    })
  ]
})
`;

console.log('\n=== Compression 插件 ===');
console.log(compressionPlugin);

// 5. PWA 插件
const pwaPlugin = `
import { defineConfig } from 'vite'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'robots.txt', 'apple-touch-icon.png'],
      manifest: {
        name: 'My App',
        short_name: 'App',
        description: 'My Awesome App',
        theme_color: '#ffffff',
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          }
        ]
      }
    })
  ]
})
`;

console.log('\n=== PWA 插件 ===');
console.log(pwaPlugin);

// 6. 自动导入插件
const autoImportPlugin = `
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'

export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      imports: ['vue', 'vue-router', 'pinia'],
      dts: 'src/auto-imports.d.ts'
    }),
    Components({
      dts: 'src/components.d.ts'
    })
  ]
})

// 使用时无需导入
// 之前: import { ref, onMounted } from 'vue'
// 现在: 直接用 ref, onMounted
`;

console.log('\n=== 自动导入插件 ===');
console.log(autoImportPlugin);

// 7. 编写简单插件
const writePlugin = `
// my-plugin.js
export default function myPlugin() {
  return {
    name: 'my-plugin',
    
    // Vite 特有钩子
    config(config, env) {
      console.log('config hook')
      return {
        define: {
          __MY_PLUGIN__: true
        }
      }
    },
    
    configResolved(config) {
      console.log('configResolved hook')
    },
    
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        console.log('请求:', req.url)
        next()
      })
    },
    
    transformIndexHtml(html) {
      return html.replace(
        '<head>',
        '<head><script>console.log("Injected!")</script>'
      )
    },
    
    // Rollup 钩子
    transform(code, id) {
      if (id.endsWith('.js')) {
        return code.replace('__VERSION__', '"1.0.0"')
      }
    }
  }
}

// 使用
import { defineConfig } from 'vite'
import myPlugin from './my-plugin'

export default defineConfig({
  plugins: [myPlugin()]
})
`;

console.log('\n=== 编写简单插件 ===');
console.log(writePlugin);

// 8. 虚拟模块插件
const virtualModulePlugin = `
// virtual-module-plugin.js
export default function virtualModulePlugin() {
  const virtualModuleId = 'virtual:my-config'
  const resolvedVirtualModuleId = '\\0' + virtualModuleId

  return {
    name: 'virtual-module-plugin',
    
    resolveId(id) {
      if (id === virtualModuleId) {
        return resolvedVirtualModuleId
      }
    },
    
    load(id) {
      if (id === resolvedVirtualModuleId) {
        return \`
          export const config = {
            apiUrl: 'https://api.example.com',
            version: '1.0.0'
          }
        \`
      }
    }
  }
}

// 使用
import { config } from 'virtual:my-config'
console.log(config.apiUrl)
`;

console.log('\n=== 虚拟模块插件 ===');
console.log(virtualModulePlugin);
