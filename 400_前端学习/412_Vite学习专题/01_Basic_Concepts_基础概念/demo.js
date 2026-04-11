// Vite 基础概念示例代码

// 1. Vite 核心优势
const viteAdvantages = {
  '极速冷启动': {
    原理: '基于原生 ES 模块，无需打包',
    对比: 'Webpack 需要先打包整个应用',
    效果: '秒级启动'
  },
  '即时热更新': {
    原理: '只更新变更的模块',
    对比: 'Webpack 可能需要重新构建依赖链',
    效果: '无论项目多大，HMR 始终快速'
  },
  '原生 ESM': {
    原理: '直接使用浏览器的 ES Modules',
    优势: '利用浏览器原生能力',
    支持: '现代浏览器全部支持'
  },
  '预构建': {
    原理: '使用 esbuild 预构建依赖',
    优势: 'esbuild 比传统工具快 10-100 倍',
    作用: '减少请求数量，转换 CommonJS 为 ESM'
  }
};

console.log('=== Vite 核心优势 ===');
Object.entries(viteAdvantages).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  原理: ${info.原理}`);
  if (info.对比) console.log(`  对比: ${info.对比}`);
  if (info.优势) console.log(`  优势: ${info.优势}`);
  console.log(`  效果: ${info.效果}`);
});

// 2. 创建 Vite 项目
const createViteCommands = [
  '# 使用 npm',
  'npm create vite@latest',
  '',
  '# 使用 yarn',
  'yarn create vite',
  '',
  '# 使用 pnpm',
  'pnpm create vite',
  '',
  '# 直接指定项目名和模板',
  'npm create vite@latest my-vue-app -- --template vue',
  'npm create vite@latest my-react-app -- --template react',
  'npm create vite@latest my-ts-app -- --template vanilla-ts'
];

console.log('\n=== 创建 Vite 项目 ===');
createViteCommands.forEach(cmd => console.log(cmd));

// 3. 可用的模板
const viteTemplates = [
  { name: 'vanilla', desc: '原生 JavaScript' },
  { name: 'vanilla-ts', desc: '原生 TypeScript' },
  { name: 'vue', desc: 'Vue 3' },
  { name: 'vue-ts', desc: 'Vue 3 + TypeScript' },
  { name: 'react', desc: 'React' },
  { name: 'react-ts', desc: 'React + TypeScript' },
  { name: 'preact', desc: 'Preact' },
  { name: 'preact-ts', desc: 'Preact + TypeScript' },
  { name: 'lit', desc: 'Lit' },
  { name: 'lit-ts', desc: 'Lit + TypeScript' },
  { name: 'svelte', desc: 'Svelte' },
  { name: 'svelte-ts', desc: 'Svelte + TypeScript' },
  { name: 'solid', desc: 'SolidJS' },
  { name: 'solid-ts', desc: 'SolidJS + TypeScript' },
  { name: 'qwik', desc: 'Qwik' },
  { name: 'qwik-ts', desc: 'Qwik + TypeScript' }
];

console.log('\n=== Vite 可用模板 ===');
viteTemplates.forEach(t => {
  console.log(`  ${t.name.padEnd(15)}: ${t.desc}`);
});

// 4. 项目结构
const projectStructure = `
my-vite-app/
├── node_modules/
├── public/              # 静态资源，原样复制
│   └── favicon.ico
├── src/
│   ├── assets/          # 资源文件，会被构建处理
│   │   └── logo.svg
│   ├── App.css
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx         # 入口文件
├── .gitignore
├── index.html           # HTML 入口（在根目录！）
├── package.json
├── vite.config.js       # Vite 配置文件
└── README.md
`;

console.log('\n=== Vite 项目结构 ===');
console.log(projectStructure);

// 5. 常用命令
const viteCommands = {
  '开发模式': {
    npm: 'npm run dev',
    yarn: 'yarn dev',
    pnpm: 'pnpm dev',
    说明: '启动开发服务器，支持 HMR'
  },
  '生产构建': {
    npm: 'npm run build',
    yarn: 'yarn build',
    pnpm: 'pnpm build',
    说明: '构建生产版本，输出到 dist 目录'
  },
  '预览构建': {
    npm: 'npm run preview',
    yarn: 'yarn preview',
    pnpm: 'pnpm preview',
    说明: '本地预览构建结果'
  }
};

console.log('\n=== 常用命令 ===');
Object.entries(viteCommands).forEach(([name, cmd]) => {
  console.log(`\n【${name}】`);
  console.log(`  npm: ${cmd.npm}`);
  console.log(`  yarn: ${cmd.yarn}`);
  console.log(`  pnpm: ${cmd.pnpm}`);
  console.log(`  说明: ${cmd.说明}`);
});

// 6. package.json scripts
const packageJsonScripts = {
  name: 'my-vite-app',
  private: true,
  version: '0.0.0',
  type: 'module',
  scripts: {
    dev: 'vite',
    build: 'vite build',
    preview: 'vite preview'
  },
  dependencies: {},
  devDependencies: {
    vite: '^5.0.0'
  }
};

console.log('\n=== package.json ===');
console.log(JSON.stringify(packageJsonScripts, null, 2));

// 7. index.html 入口
const indexHtml = `
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite App</title>
  </head>
  <body>
    <div id="root"></div>
    <!-- 注意：type="module" -->
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
`;

console.log('\n=== index.html 入口 ===');
console.log(indexHtml);

// 8. Vite vs Webpack 对比
const viteVsWebpack = {
  特性: ['启动速度', 'HMR 速度', '配置复杂度', '生产构建', '原生 ESM', '开发体验'],
  Vite: ['⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐', '⭐⭐⭐⭐', '✅', '极佳'],
  Webpack: ['⭐⭐', '⭐⭐⭐', '⭐⭐', '⭐⭐⭐⭐⭐', '需配置', '好']
};

console.log('\n=== Vite vs Webpack ===');
console.log('特性'.padEnd(12) + '  Vite      Webpack');
viteVsWebpack.特性.forEach((feature, i) => {
  console.log(
    feature.padEnd(12) + 
    '  ' + viteVsWebpack.Vite[i].padEnd(10) + 
    '  ' + viteVsWebpack.Webpack[i]
  );
});

// 9. Vite 的工作原理
const howViteWorks = [
  '1. 开发阶段',
  '   - 不打包，直接使用浏览器 ESM',
  '   - 浏览器请求哪个模块就处理哪个模块',
  '   - 使用 esbuild 预构建依赖（node_modules）',
  '',
  '2. 热更新 HMR',
  '   - 只重新编译变更的模块',
  '   - 精确更新，不影响其他模块',
  '   - 速度与项目大小无关',
  '',
  '3. 生产构建',
  '   - 使用 Rollup 打包',
  '   - Tree Shaking 优化',
  '   - 输出优化的静态资源'
];

console.log('\n=== Vite 工作原理 ===');
howViteWorks.forEach(step => console.log(step));

// 10. 为什么 Vite 这么快？
const whyViteIsFast = [
  '🚀 esbuild 预构建依赖（Go 编写，比 JS 工具快 10-100 倍）',
  '🚀 开发时不打包，按需提供模块',
  '🚀 利用浏览器原生 ESM 支持',
  '🚀 HMR 只更新变更的模块',
  '🚀 智能缓存机制'
];

console.log('\n=== 为什么 Vite 这么快？ ===');
whyViteIsFast.forEach(reason => console.log(reason));
