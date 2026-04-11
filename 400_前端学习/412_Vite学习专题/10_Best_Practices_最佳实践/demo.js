// Vite 最佳实践示例代码

// 1. 推荐的项目结构
const projectStructureBest = `
src/
├── assets/              # 静态资源
│   ├── images/
│   ├── fonts/
│   └── styles/
├── components/          # 通用组件
│   ├── Button/
│   ├── Input/
│   └── Modal/
├── composables/         # Vue组合式函数 / React Hooks
│   ├── useAuth.ts
│   └── useFetch.ts
├── layouts/             # 布局组件
│   ├── DefaultLayout.vue
│   └── AdminLayout.vue
├── pages/               # 页面
│   ├── Home/
│   ├── About/
│   └── Admin/
├── router/              # 路由
│   └── index.ts
├── stores/              # 状态管理
│   └── user.ts
├── utils/               # 工具函数
│   ├── request.ts
│   └── format.ts
├── types/               # TypeScript 类型
│   └── index.ts
├── App.vue
└── main.ts
`;

console.log('=== 推荐的项目结构 ===');
console.log(projectStructureBest);

// 2. 完整的 vite.config.ts 配置
const fullConfigBest = `
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import viteCompression from 'vite-plugin-compression'
import { visualizer } from 'rollup-plugin-visualizer'
import path from 'path'

export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  
  return {
    plugins: [
      vue(),
      AutoImport({
        imports: ['vue', 'vue-router', 'pinia'],
        dts: 'src/types/auto-imports.d.ts'
      }),
      Components({
        dts: 'src/types/components.d.ts'
      }),
      viteCompression({
        algorithm: 'gzip',
        threshold: 10240
      }),
      mode === 'analyze' && visualizer({ open: true })
    ],
    
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
          target: env.VITE_API_URL,
          changeOrigin: true
        }
      }
    },
    
    build: {
      outDir: 'dist',
      sourcemap: mode === 'development',
      minify: 'esbuild',
      target: 'es2015',
      
      rollupOptions: {
        output: {
          manualChunks: {
            'vue-vendor': ['vue', 'vue-router', 'pinia'],
            'ui-vendor': ['element-plus'],
            'utils-vendor': ['lodash-es', 'axios']
          },
          chunkFileNames: 'assets/js/[name]-[hash].js',
          assetFileNames: 'assets/[ext]/[name]-[hash].[ext]'
        }
      }
    }
  }
})
`;

console.log('\n=== 完整的 vite.config.ts 配置 ===');
console.log(fullConfigBest);

// 3. package.json scripts
const packageJsonScriptsBest = {
  name: 'my-vite-app',
  private: true,
  version: '0.0.0',
  type: 'module',
  scripts: {
    dev: 'vite',
    build: 'vue-tsc && vite build',
    build:staging: 'vue-tsc && vite build --mode staging',
    preview: 'vite preview',
    lint: 'eslint src --ext .vue,.js,.ts,.tsx --fix',
    format: 'prettier --write src',
    type-check: 'vue-tsc --noEmit',
    analyze: 'vite build --mode analyze'
  }
};

console.log('\n=== package.json scripts ===');
console.log(JSON.stringify(packageJsonScriptsBest, null, 2));

// 4. 开发工具配置
const devToolsConfig = `
// .eslintrc.js
module.exports = {
  root: true,
  env: { browser: true, es2021: true },
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
    'plugin:@typescript-eslint/recommended'
  ],
  parser: 'vue-eslint-parser',
  parserOptions: {
    parser: '@typescript-eslint/parser',
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  rules: {
    'vue/multi-word-component-names': 'off'
  }
}

// .prettierrc
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "none",
  "printWidth": 100
}

// .editorconfig
root = true
[*]
charset = utf-8
indent_style = space
indent_size = 2
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
`;

console.log('\n=== 开发工具配置 ===');
console.log(devToolsConfig);

// 5. 环境变量管理
const envManagement = `
# .env                # 所有环境
# .env.local          # 本地覆盖（git 忽略）
# .env.development    # 开发环境
# .env.staging        # 预发布环境
# .env.production     # 生产环境

# .env
VITE_APP_TITLE=My App
VITE_API_TIMEOUT=30000

# .env.development
VITE_API_URL=http://localhost:8080/api
VITE_DEBUG=true

# .env.staging
VITE_API_URL=https://staging.example.com/api
VITE_DEBUG=true

# .env.production
VITE_API_URL=https://api.example.com
VITE_DEBUG=false

# 使用
const apiUrl = import.meta.env.VITE_API_URL
const isDebug = import.meta.env.VITE_DEBUG === 'true'
`;

console.log('\n=== 环境变量管理 ===');
console.log(envManagement);

// 6. 性能优化最佳实践
const perfBestPractices = [
  '✅ 使用路由懒加载',
  '✅ 合理的代码分割',
  '✅ 图片压缩和格式优化',
  '✅ 使用 CDN 加载常用库',
  '✅ 启用 gzip/brotli 压缩',
  '✅ 配置浏览器缓存',
  '✅ Tree Shaking 优化',
  '✅ 移除未使用的依赖',
  '✅ 使用生产构建',
  '✅ 分析构建产物'
];

console.log('\n=== 性能优化最佳实践 ===');
perfBestPractices.forEach(p => console.log(p));

// 7. 安全最佳实践
const securityBestPractices = [
  '✅ 不要在前端代码中提交密钥',
  '✅ 使用环境变量存储敏感信息',
  '✅ 启用 CSP（内容安全策略）',
  '✅ 验证用户输入',
  '✅ 使用 HTTPS',
  '✅ 配置安全的响应头',
  '✅ 定期更新依赖',
  '✅ 运行 npm audit'
];

console.log('\n=== 安全最佳实践 ===');
securityBestPractices.forEach(p => console.log(p));

// 8. 常见问题排查
const troubleshooting = [
  {
    问题: '热更新不生效',
    解决: [
      '检查文件命名是否正确',
      '检查 vite.config.js 配置',
      '重启开发服务器'
    ]
  },
  {
    问题: '路径别名不生效',
    解决: [
      '检查 vite.config.js 的 alias 配置',
      '检查 tsconfig.json 的 paths 配置',
      '重启 IDE'
    ]
  },
  {
    问题: '构建后白屏',
    解决: [
      '检查 base 路径配置',
      '检查路由配置',
      '检查控制台错误'
    ]
  }
];

console.log('\n=== 常见问题排查 ===');
troubleshooting.forEach(item => {
  console.log(`\n【问题】${item.问题}`);
  console.log('【解决】');
  item.解决.forEach(s => console.log(`  - ${s}`));
});

console.log('\n🎉 Vite 学习专题完成！');
console.log('💡 记住：使用 Vite 享受极速开发体验！');
