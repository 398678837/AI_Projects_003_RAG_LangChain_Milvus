// Vite + TypeScript 示例代码

// 1. 基础 tsconfig.json
const tsconfig = {
  compilerOptions: {
    target: 'ES2020',
    useDefineForClassFields: true,
    module: 'ESNext',
    lib: ['ES2020', 'DOM', 'DOM.Iterable'],
    skipLibCheck: true,
    moduleResolution: 'bundler',
    allowImportingTsExtensions: true,
    resolveJsonModule: true,
    isolatedModules: true,
    noEmit: true,
    jsx: 'react-jsx',
    strict: true,
    noUnusedLocals: true,
    noUnusedParameters: true,
    noFallthroughCasesInSwitch: true
  },
  include: ['src/**/*.ts', 'src/**/*.tsx', 'src/**/*.vue'],
  references: [{ path: './tsconfig.node.json' }]
};

console.log('=== tsconfig.json ===');
console.log(JSON.stringify(tsconfig, null, 2));

// 2. vite-env.d.ts
const viteEnvDts = `
/// <reference types="vite/client" />

// 声明环境变量类型
interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
  readonly VITE_DEBUG: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

// 声明资源模块
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module '*.svg' {
  const content: string
  export default content
}

declare module '*.png' {
  const content: string
  export default content
}

declare module '*.jpg' {
  const content: string
  export default content
}

declare module '*.css' {
  const classes: { readonly [key: string]: string }
  export default classes
}
`;

console.log('\n=== vite-env.d.ts ===');
console.log(viteEnvDts);

// 3. 路径别名配置
const pathAliasConfig = `
// vite.config.ts
import { defineConfig } from 'vite'
import path from 'path'

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@utils': path.resolve(__dirname, './src/utils')
    }
  }
})

// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"]
    }
  }
}
`;

console.log('\n=== 路径别名配置 ===');
console.log(pathAliasConfig);

// 4. 使用 TypeScript
const usingTypescript = `
// main.ts
import { createApp } from 'vue'
import App from './App.vue'
import './style.css'

const app = createApp(App)
app.mount('#app')

// 使用环境变量
const apiUrl = import.meta.env.VITE_API_URL
console.log('API URL:', apiUrl)

// 类型安全的组件
interface User {
  id: number
  name: string
  email: string
}

function UserCard({ user }: { user: User }) {
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  )
}
`;

console.log('\n=== 使用 TypeScript ===');
console.log(usingTypescript);

// 5. 类型检查
const typeChecking = `
// 安装类型检查工具
npm install vue-tsc -D

// package.json
{
  "scripts": {
    "dev": "vite",
    "build": "vue-tsc && vite build",
    "type-check": "vue-tsc --noEmit"
  }
}

// 运行类型检查
npm run type-check

// 构建时检查
npm run build
`;

console.log('\n=== 类型检查 ===');
console.log(typeChecking);

// 6. 完整的 TypeScript 配置示例
const fullTypescriptConfig = `
// vite.config.ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})

// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "preserve",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.vue"],
  "references": [{ "path": "./tsconfig.node.json" }]
}

// tsconfig.node.json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}

// src/vite-env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
`;

console.log('\n=== 完整的 TypeScript 配置示例 ===');
console.log(fullTypescriptConfig);
