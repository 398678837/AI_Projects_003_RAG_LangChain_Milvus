// Vite 配置示例代码

// 1. 基础配置
const basicConfig = `
import { defineConfig } from 'vite'

export default defineConfig({
  // 项目根目录
  root: '.',
  
  // 部署时的基础路径
  base: '/',
  
  // 开发服务器配置
  server: {
    port: 3000,
    open: true
  },
  
  // 构建配置
  build: {
    outDir: 'dist',
    sourcemap: true
  }
})
`;

console.log('=== 基础配置 ===');
console.log(basicConfig);

// 2. 路径别名配置
const aliasConfig = `
import { defineConfig } from 'vite'
import path from 'path'

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@utils': path.resolve(__dirname, './src/utils'),
      '@assets': path.resolve(__dirname, './src/assets'),
      
      // 或者使用对象写法
      '~bootstrap': 'bootstrap/dist/css/bootstrap.css'
    }
  }
})

// tsconfig.json 也需要配置
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    }
  }
}

// 使用
import Button from '@/components/Button'
import { formatDate } from '@utils/date'
`;

console.log('\n=== 路径别名配置 ===');
console.log(aliasConfig);

// 3. 开发服务器完整配置
const devServerConfig = `
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    host: '0.0.0.0',        // 监听所有地址
    port: 3000,              // 端口
    strictPort: false,       // 端口被占用时自动尝试下一个
    https: false,            // 是否启用 HTTPS
    open: true,              // 自动打开浏览器
    cors: true,              // 启用 CORS
    
    // 代理配置
    proxy: {
      // 字符串简写
      '/api': 'http://localhost:8080',
      
      // 完整选项
      '/api2': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^/api2/, ''),
        configure: (proxy, options) => {
          proxy.on('error', (err, req, res) => {
            console.log('proxy error', err)
          })
        }
      },
      
      // WebSocket 代理
      '/socket.io': {
        target: 'ws://localhost:3000',
        ws: true
      }
    },
    
    // 自定义响应头
    headers: {
      'X-Custom-Header': 'Hello Vite'
    }
  }
})
`;

console.log('\n=== 开发服务器完整配置 ===');
console.log(devServerConfig);

// 4. 构建配置
const buildConfig = `
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    // 输出目录
    outDir: 'dist',
    
    // 静态资源目录
    assetsDir: 'assets',
    
    // 资源内联阈值（字节）
    assetsInlineLimit: 4096,
    
    // 源映射
    sourcemap: false,
    
    // 压缩
    minify: 'esbuild',  // 'esbuild' | 'terser' | false
    
    // 目标浏览器
    target: 'modules',
    
    // CSS 代码分割
    cssCodeSplit: true,
    
    // Rollup 选项
    rollupOptions: {
      input: {
        main: './index.html',
        admin: './admin.html'
      },
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          utils: ['lodash-es']
        }
      }
    },
    
    // 库模式
    lib: {
      entry: './src/main.ts',
      name: 'MyLib',
      fileName: (format) => \`my-lib.\${format}.js\`
    },
    
    // 清空输出目录
    emptyOutDir: true
  }
})
`;

console.log('\n=== 构建配置 ===');
console.log(buildConfig);

// 5. 预览服务器配置
const previewConfig = `
import { defineConfig } from 'vite'

export default defineConfig({
  preview: {
    port: 4173,
    strictPort: true,
    host: true,
    open: true,
    proxy: {
      // 同 server.proxy
    }
  }
})
`;

console.log('\n=== 预览服务器配置 ===');
console.log(previewConfig);

// 6. 环境相关配置
const envConfig = `
import { defineConfig, loadEnv } from 'vite'

export default defineConfig(({ command, mode }) => {
  // 加载环境变量
  const env = loadEnv(mode, process.cwd(), '')
  
  return {
    define: {
      __APP_ENV__: JSON.stringify(env.APP_ENV)
    },
    
    server: {
      port: mode === 'development' ? 3000 : 8080
    },
    
    build: {
      sourcemap: mode === 'staging'
    }
  }
})
`;

console.log('\n=== 环境相关配置 ===');
console.log(envConfig);

// 7. CSS 配置
const cssConfig = `
import { defineConfig } from 'vite'

export default defineConfig({
  css: {
    // CSS Modules
    modules: {
      localsConvention: 'camelCase',
      scopeBehaviour: 'local',
      generateScopedName: '[name]__[local]__[hash:base64:5]'
    },
    
    // PostCSS
    postcss: {
      plugins: [
        require('autoprefixer'),
        require('tailwindcss')
      ]
    },
    
    // 预处理器选项
    preprocessorOptions: {
      scss: {
        additionalData: \`$primary-color: #1976d2;\`
      },
      less: {
        math: 'always'
      }
    }
  }
})
`;

console.log('\n=== CSS 配置 ===');
console.log(cssConfig);

// 8. 完整配置示例
const completeConfig = `
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
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
          vue: ['vue', 'vue-router', 'pinia']
        }
      }
    }
  }
})
`;

console.log('\n=== 完整配置示例 ===');
console.log(completeConfig);
