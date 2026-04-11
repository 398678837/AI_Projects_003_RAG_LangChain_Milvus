// Vite + React 示例代码

// 1. 创建项目
const createReactProject = `
# JavaScript 版本
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev

# TypeScript 版本
npm create vite@latest my-react-app -- --template react-ts
cd my-react-app
npm install
npm run dev

# 使用 pnpm
pnpm create vite my-react-app --template react-ts
`;

console.log('=== 创建 React 项目 ===');
console.log(createReactProject);

// 2. vite.config.js 配置
const viteConfigReact = `
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [
    react({
      babel: {
        plugins: [
          ['babel-plugin-styled-components', { ssr: false }]
        ]
      },
      jsxImportSource: '@emotion/react',
      fastRefresh: true
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

// 或使用 SWC（更快）
import react from '@vitejs/plugin-react-swc'
`;

console.log('\n=== vite.config.js 配置 ===');
console.log(viteConfigReact);

// 3. 项目结构
const reactProjectStructure = `
my-react-app/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   │   └── react.svg
│   ├── App.css
│   ├── App.jsx
│   ├── App.test.jsx
│   ├── index.css
│   ├── main.jsx
│   └── setupTests.js
├── .gitignore
├── index.html
├── package.json
├── vite.config.js
└── README.md
`;

console.log('\n=== 项目结构 ===');
console.log(reactProjectStructure);

// 4. main.jsx
const mainJsx = `
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
`;

console.log('\n=== main.jsx ===');
console.log(mainJsx);

// 5. App.jsx
const appJsx = `
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
    </div>
  )
}

export default App
`;

console.log('\n=== App.jsx ===');
console.log(appJsx);

// 6. 使用环境变量
const envUsageReact = `
// .env
VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My React App

// 在组件中使用
function App() {
  const apiUrl = import.meta.env.VITE_API_URL
  const title = import.meta.env.VITE_APP_TITLE
  
  console.log('API URL:', apiUrl)
  
  return (
    <div>
      <h1>{title}</h1>
    </div>
  )
}

// 检查环境
if (import.meta.env.DEV) {
  console.log('开发环境')
}
if (import.meta.env.PROD) {
  console.log('生产环境')
}
`;

console.log('\n=== 使用环境变量 ===');
console.log(envUsageReact);

// 7. 路由配置
const reactRouter = `
// 安装
npm install react-router-dom

// main.jsx
import { BrowserRouter } from 'react-router-dom'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
)

// App.jsx
import { Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'

function App() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  )
}
`;

console.log('\n=== 路由配置 ===');
console.log(reactRouter);

// 8. 完整的 vite.config.ts (TypeScript)
const fullViteConfigReactTs = `
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@pages': path.resolve(__dirname, './src/pages'),
      '@hooks': path.resolve(__dirname, './src/hooks'),
      '@utils': path.resolve(__dirname, './src/utils')
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
          'react-vendor': ['react', 'react-dom'],
          'router-vendor': ['react-router-dom']
        }
      }
    }
  }
})
`;

console.log('\n=== 完整的 vite.config.ts ===');
console.log(fullViteConfigReactTs);
