// Vite 核心功能示例代码

// 1. 静态资源导入
const staticImports = `
// 导入图片，返回 URL
import logoUrl from './assets/logo.png'

const img = document.createElement('img')
img.src = logoUrl

// 导入 SVG 为字符串
import svgContent from './assets/icon.svg?raw'

// 导入为 URL 查询参数
import url from './image.png'
import urlInline from './image.png?inline'
import urlRaw from './image.png?raw'
import urlWorker from './worker.js?worker'
`;

console.log('=== 静态资源导入 ===');
console.log(staticImports);

// 2. public 目录
const publicDir = `
public/
├── favicon.ico          # 直接访问 /favicon.ico
├── robots.txt           # 直接访问 /robots.txt
└── data/
    └── config.json      # 直接访问 /data/config.json

// 使用时直接引用根路径
fetch('/data/config.json')
`;

console.log('\n=== public 目录 ===');
console.log(publicDir);

// 3. 环境变量
const envVariables = `
# .env                # 所有情况加载
# .env.local          # 所有情况加载，git 忽略
# .env.development    # 开发模式加载
# .env.production     # 生产模式加载
# .env.staging        # 自定义模式

VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My App
SECRET_KEY=secret123  # 不会被暴露！

// 在代码中使用
console.log(import.meta.env.VITE_API_URL)
console.log(import.meta.env.VITE_APP_TITLE)

// 内置变量
import.meta.env.MODE           // 'development' 或 'production'
import.meta.env.BASE_URL       // 部署基础路径
import.meta.env.PROD           // 是否生产环境
import.meta.env.DEV            // 是否开发环境
import.meta.env.SSR            // 是否服务端渲染
`;

console.log('\n=== 环境变量 ===');
console.log(envVariables);

// 4. 开发服务器配置
const devServerConfig = `
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    host: true,              // 监听所有地址
    port: 3000,              // 指定端口
    strictPort: true,        // 端口被占用则退出
    open: true,              // 自动打开浏览器
    proxy: {                 // 代理配置
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^/api/, '')
      }
    },
    cors: true,              // 启用 CORS
    headers: {               // 自定义响应头
      'X-Custom-Header': 'value'
    }
  }
})
`;

console.log('\n=== 开发服务器配置 ===');
console.log(devServerConfig);

// 5. HMR 热模块替换
const hmrExample = `
// 手动接受 HMR 更新
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    console.log('模块已更新:', newModule)
  })
  
  // 接受依赖模块的更新
  import.meta.hot.accept('./dep.js', (newDep) => {
    console.log('依赖已更新:', newDep)
  })
  
  // 清理副作用
  import.meta.hot.dispose(() => {
    console.log('模块即将被替换')
  })
}

// React/Vue 等框架已内置 HMR 支持
// 无需手动配置！
`;

console.log('\n=== HMR 热模块替换 ===');
console.log(hmrExample);

// 6. CSS 功能
const cssFeatures = `
/* 直接导入 CSS */
import './style.css'

/* CSS Modules */
import styles from './module.module.css'
<div className={styles.container}></div>

/* CSS 预处理器，安装相应依赖即可 */
// npm install -D sass
import './style.scss'

// npm install -D less
import './style.less'

/* PostCSS，内置支持 */
// autoprefixer 自动添加前缀
`;

console.log('\n=== CSS 功能 ===');
console.log(cssFeatures);

// 7. CSS Modules 示例
const cssModulesExample = `
/* style.module.css */
.container {
  padding: 20px;
}

.title {
  color: blue;
}

// 使用
import styles from './style.module.css'

function App() {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Hello</h1>
    </div>
  )
}

// 生成的类名类似：_container_abc123 _title_def456
`;

console.log('\n=== CSS Modules 示例 ===');
console.log(cssModulesExample);

// 8. 预构建优化
const preoptimization = `
// vite.config.js
export default defineConfig({
  optimizeDeps: {
    include: ['lodash-es', 'axios'],  // 强制预构建
    exclude: ['my-local-dep'],       // 排除预构建
    esbuildOptions: {
      plugins: []                    // esbuild 插件
    }
  }
})

// 预构建的好处：
// 1. CommonJS/UMD 转换为 ESM
// 2. 减少请求数量（合并多个文件）
// 3. 缓存，只有依赖变化时才重新构建
`;

console.log('\n=== 预构建优化 ===');
console.log(preoptimization);

// 9. Glob 导入
const globImport = `
// 导入多个模块
const modules = import.meta.glob('./dir/*.js')

// 动态导入
for (const path in modules) {
  modules[path]().then(mod => {
    console.log(path, mod)
  })
}

// 同步导入
const modulesSync = import.meta.glob('./dir/*.js', { eager: true })

// 只导入默认导出
const modulesDefault = import.meta.glob('./dir/*.js', { import: 'default' })
`;

console.log('\n=== Glob 导入 ===');
console.log(globImport);

// 10. Web Workers
const webWorkers = `
// 普通 Worker
import MyWorker from './worker.js?worker'

const worker = new MyWorker()
worker.postMessage('hello')

// 内联 Worker
import MyInlineWorker from './worker.js?worker&inline'

// SharedWorker
import SharedWorker from './worker.js?sharedworker'
`;

console.log('\n=== Web Workers ===');
console.log(webWorkers);
