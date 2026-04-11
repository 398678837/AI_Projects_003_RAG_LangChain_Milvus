// 包管理示例代码

// 1. 包的基本结构
const packageStructure = `
my-awesome-package/
├── package.json          # 包配置文件
├── README.md             # 说明文档
├── LICENSE               # 许可证
├── index.js              # 入口文件
├── src/                  # 源代码
│   └── main.js
├── dist/                 # 构建输出
│   └── index.js
├── __tests__/            # 测试
│   └── main.test.js
├── .gitignore
└── .npmignore            # 发布时忽略的文件
`;

console.log('=== 包的基本结构 ===');
console.log(packageStructure);

// 2. 完整的 package.json（发布用）
const publishPackageJson = {
  name: '@your-scope/my-awesome-package',
  version: '1.0.0',
  description: 'An awesome package description',
  author: {
    name: 'Your Name',
    email: 'your@email.com',
    url: 'https://yourwebsite.com'
  },
  license: 'MIT',
  homepage: 'https://github.com/your-scope/my-awesome-package',
  repository: {
    type: 'git',
    url: 'https://github.com/your-scope/my-awesome-package.git'
  },
  bugs: {
    url: 'https://github.com/your-scope/my-awesome-package/issues'
  },
  keywords: ['awesome', 'package', 'utility'],
  main: 'dist/index.js',
  module: 'dist/index.esm.js',
  types: 'dist/index.d.ts',
  exports: {
    '.': {
      import: './dist/index.esm.js',
      require: './dist/index.js',
      types: './dist/index.d.ts'
    },
    './utils': {
      import: './dist/utils.esm.js',
      require: './dist/utils.js'
    }
  },
  files: ['dist', 'README.md', 'LICENSE'],
  bin: {
    'my-cli': './bin/cli.js'
  },
  scripts: {
    'build': 'rollup -c',
    'dev': 'rollup -c -w',
    'test': 'jest',
    'lint': 'eslint src',
    'prepublishOnly': 'npm run build && npm test',
    'version': 'npm run build && git add -A dist',
    'postversion': 'git push && git push --tags'
  },
  dependencies: {},
  devDependencies: {
    'rollup': '^3.0.0',
    'jest': '^29.0.0',
    'eslint': '^8.0.0',
    'typescript': '^5.0.0'
  },
  peerDependencies: {
    'lodash': '>=4.0.0'
  },
  engines: {
    'node': '>=16.0.0'
  },
  publishConfig: {
    'access': 'public',
    'registry': 'https://registry.npmjs.org/'
  },
  sideEffects: false
};

console.log('\n=== 发布用 package.json ===');
console.log(JSON.stringify(publishPackageJson, null, 2));

// 3. 发布流程
const publishSteps = [
  '1. 注册 npm 账号',
  '   https://www.npmjs.com/signup',
  '',
  '2. 登录 npm',
  '   npm login',
  '',
  '3. 检查包名是否可用',
  '   npm view <package-name>',
  '',
  '4. 初始化 Git（可选但推荐）',
  '   git init',
  '   git add .',
  '   git commit -m "Initial commit"',
  '',
  '5. 更新版本',
  '   npm version patch  # 1.0.0 -> 1.0.1',
  '   npm version minor  # 1.0.0 -> 1.1.0',
  '   npm version major  # 1.0.0 -> 2.0.0',
  '   npm version prerelease --preid=beta  # 1.0.0 -> 1.0.1-beta.0',
  '',
  '6. 发布包',
  '   npm publish',
  '   npm publish --access=public  # scoped package',
  '   npm publish --tag beta  # 发布到 beta 标签',
  '',
  '7. 验证发布',
  '   npm view <package-name>',
  '   npm install <package-name>'
];

console.log('\n=== 发布流程 ===');
publishSteps.forEach(step => console.log(`  ${step}`));

// 4. npm version 命令
const versionCommands = {
  'patch': '1.0.0 → 1.0.1 (bug fixes)',
  'minor': '1.0.0 → 1.1.0 (new features)',
  'major': '1.0.0 → 2.0.0 (breaking changes)',
  'prepatch': '1.0.0 → 1.0.1-0',
  'preminor': '1.0.0 → 1.1.0-0',
  'premajor': '1.0.0 → 2.0.0-0',
  'prerelease': '1.0.0-beta.0 → 1.0.0-beta.1'
};

console.log('\n=== npm version 命令 ===');
Object.entries(versionCommands).forEach(([cmd, desc]) => {
  console.log(`  npm version ${cmd.padEnd(12)} → ${desc}`);
});

// 5. 预发布版本和标签
const prereleaseTags = {
  'alpha': '内部测试版，功能可能不完整',
  'beta': '公开测试版，基本功能可用',
  'rc': 'Release Candidate，发布候选版',
  'next': '下一个主要版本',
  'dev': '开发版本'
};

console.log('\n=== 预发布版本标签 ===');
Object.entries(prereleaseTags).forEach(([tag, desc]) => {
  console.log(`  ${tag.padEnd(8)}: ${desc}`);
});
console.log('\n示例: 1.0.0-beta.1, 2.0.0-rc.0');
console.log('\n发布到标签: npm publish --tag beta');
console.log('安装标签版本: npm install <pkg>@beta');

// 6. .npmignore 文件
const npmignoreExample = `
# .npmignore - 发布时忽略的文件

# 构建工具
.vscode/
.idea/
*.swp
*.swo

# 测试
__tests__/
*.test.js
*.spec.js
coverage/

# 开发配置
.eslintrc
.prettierrc
jest.config.js
rollup.config.js
tsconfig.json

# 源文件（如果只发布 dist）
src/

# Git
.git/
.gitignore
.github/

# 文档（可选，通常保留）
# docs/
`;

console.log('\n=== .npmignore 示例 ===');
console.log(npmignoreExample);

// 7. 包的使用方式
const packageUsage = {
  'CommonJS': 'const pkg = require("my-package");',
  'ES Modules': 'import pkg from "my-package";',
  'TypeScript': 'import pkg from "my-package";',
  'CLI': 'npx my-cli 或 全局安装后 my-cli',
  'CDN': '<script src="https://unpkg.com/my-package"></script>'
};

console.log('\n=== 包的使用方式 ===');
Object.entries(packageUsage).forEach(([type, code]) => {
  console.log(`\n【${type}】`);
  console.log(`  ${code}`);
});

// 8. package.json 字段详解
const packageFields = {
  name: '包名，唯一，小写，可含 scope (@scope/name)',
  version: '版本号，语义化版本',
  description: '简短描述',
  keywords: '关键词数组，便于搜索',
  homepage: '项目主页',
  bugs: '问题反馈地址',
  license: '许可证 (MIT, ISC, Apache-2.0, GPL)',
  author: '作者信息',
  contributors: '贡献者列表',
  repository: '代码仓库',
  main: 'CommonJS 入口',
  module: 'ES Modules 入口',
  types: 'TypeScript 类型声明',
  exports: '条件导出（推荐）',
  bin: 'CLI 命令',
  files: '发布包含的文件',
  scripts: '脚本命令',
  dependencies: '生产依赖',
  devDependencies: '开发依赖',
  peerDependencies: '同伴依赖',
  optionalDependencies: '可选依赖',
  engines: 'Node.js 版本要求',
  os: '支持的操作系统',
  cpu: '支持的 CPU',
  private: '设为 true 防止误发布',
  publishConfig: '发布配置',
  workspaces: 'Monorepo 配置',
  sideEffects: '是否有副作用（Tree Shaking）'
};

console.log('\n=== package.json 字段详解 ===');
Object.entries(packageFields).forEach(([field, desc]) => {
  console.log(`  ${field.padEnd(20)}: ${desc}`);
});
