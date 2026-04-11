// Vite 优化示例代码

// 1. 代码分割配置
const codeSplitting = `
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // 按库分割
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          'react-vendor': ['react', 'react-dom'],
          'ui-vendor': ['ant-design-vue', 'element-plus'],
          'utils-vendor': ['lodash-es', 'axios', 'dayjs'],
          
          // 或使用函数
          manualChunks(id) {
            if (id.includes('node_modules')) {
              return id.toString().split('node_modules/')[1].split('/')[0].toString()
            }
          }
        }
      }
    }
  }
})
`;

console.log('=== 代码分割配置 ===');
console.log(codeSplitting);

// 2. 路由懒加载
const lazyLoading = `
// Vue 路由懒加载
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/about',
    component: () => import('@/views/About.vue')
  },
  {
    path: '/admin',
    component: () => import('@/views/admin/Index.vue'),
    children: [
      {
        path: 'users',
        component: () => import('@/views/admin/Users.vue')
      }
    ]
  }
]

// React 路由懒加载
import { lazy, Suspense } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

const Home = lazy(() => import('./pages/Home'))
const About = lazy(() => import('./pages/About'))

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  )
}
`;

console.log('\n=== 路由懒加载 ===');
console.log(lazyLoading);

// 3. 预加载和预获取
const preloadPrefetch = `
<link rel="preload" href="/style.css" as="style" />
<link rel="preload" href="/script.js" as="script" />
<link rel="preload" href="/font.woff2" as="font" crossorigin />
<link rel="preload" href="/image.jpg" as="image" />

<link rel="prefetch" href="/about-page.js" />
<link rel="dns-prefetch" href="//api.example.com" />

// 在 vite.config.js 中配置
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom']
        }
      }
    }
  }
})
`;

console.log('\n=== 预加载和预获取 ===');
console.log(preloadPrefetch);

// 4. 压缩配置
const compressionConfig = `
import { defineConfig } from 'vite'
import viteCompression from 'vite-plugin-compression'

export default defineConfig({
  plugins: [
    // gzip 压缩
    viteCompression({
      algorithm: 'gzip',
      ext: '.gz',
      threshold: 10240
    }),
    // brotli 压缩（更小，但兼容性稍差）
    viteCompression({
      algorithm: 'brotliCompress',
      ext: '.br',
      threshold: 10240
    })
  ],
  build: {
    minify: 'esbuild',  // 或 'terser'
    target: 'es2015',
    cssMinify: true,
    sourcemap: false
  }
})
`;

console.log('\n=== 压缩配置 ===');
console.log(compressionConfig);

// 5. 图片优化
const imageOptimization = `
// 使用 vite-plugin-imagemin
import { defineConfig } from 'vite'
import viteImagemin from 'vite-plugin-imagemin'

export default defineConfig({
  plugins: [
    viteImagemin({
      gifsicle: {
        optimizationLevel: 7,
        interlaced: false
      },
      optipng: {
        optimizationLevel: 7
      },
      mozjpeg: {
        quality: 80
      },
      pngquant: {
        quality: [0.8, 0.9]
      },
      svgo: {
        plugins: [
          {
            name: 'removeViewBox'
          },
          {
            name: 'removeEmptyAttrs',
            active: false
          }
        ]
      }
    })
  ]
})

// 使用现代图片格式
<picture>
  <source srcset="image.avif" type="image/avif" />
  <source srcset="image.webp" type="image/webp" />
  <img src="image.jpg" alt="Image" />
</picture>
`;

console.log('\n=== 图片优化 ===');
console.log(imageOptimization);

// 6. 分析构建产物
const analyzeBundle = `
import { defineConfig } from 'vite'
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    visualizer({
      open: true,
      filename: 'dist/stats.html'
    })
  ]
})

// 运行构建
npm run build

// 查看分析报告
// 自动打开 dist/stats.html
`;

console.log('\n=== 分析构建产物 ===');
console.log(analyzeBundle);

// 7. 完整优化配置
const fullOptimizationConfig = `
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import viteCompression from 'vite-plugin-compression'
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    vue(),
    viteCompression({
      algorithm: 'gzip',
      threshold: 10240
    }),
    visualizer({
      open: true
    })
  ],
  
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,
    minify: 'esbuild',
    target: 'es2015',
    cssCodeSplit: true,
    
    rollupOptions: {
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          'ui-vendor': ['element-plus'],
          'utils-vendor': ['lodash-es', 'axios', 'dayjs']
        },
        chunkFileNames: 'assets/js/[name]-[hash].js',
        entryFileNames: 'assets/js/[name]-[hash].js',
        assetFileNames: 'assets/[ext]/[name]-[hash].[ext]'
      }
    }
  }
})
`;

console.log('\n=== 完整优化配置 ===');
console.log(fullOptimizationConfig);
