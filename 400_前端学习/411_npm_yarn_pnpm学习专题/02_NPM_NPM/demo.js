// NPM 使用示例代码

// 1. npm 常用命令速查
const npmCommands = {
  '初始化项目': [
    'npm init              # 交互式创建 package.json',
    'npm init -y           # 使用默认值快速创建'
  ],
  '安装依赖': [
    'npm install           # 安装 package.json 中的所有依赖',
    'npm i                 # 简写',
    'npm install --production  # 只安装 dependencies'
  ],
  '添加依赖': [
    'npm install <pkg>     # 安装到 dependencies',
    'npm i <pkg>           # 简写',
    'npm install <pkg>@<version>  # 安装指定版本',
    'npm install <pkg>@latest      # 安装最新版本'
  ],
  '添加开发依赖': [
    'npm install -D <pkg>  # 安装到 devDependencies',
    'npm install --save-dev <pkg>'
  ],
  '卸载依赖': [
    'npm uninstall <pkg>',
    'npm remove <pkg>',
    'npm un <pkg>'
  ],
  '更新依赖': [
    'npm update            # 更新所有依赖',
    'npm update <pkg>      # 更新指定包',
    'npm outdated          # 检查过时的包'
  ],
  '运行脚本': [
    'npm run <script>',
    'npm start             # 等同于 npm run start',
    'npm test              # 等同于 npm run test'
  ],
  '查看信息': [
    'npm list              # 查看已安装的包',
    'npm list <pkg>        # 查看指定包',
    'npm info <pkg>        # 查看包的详细信息',
    'npm view <pkg>        # 同上',
    'npm version           # 查看 npm 和 node 版本'
  ],
  '全局操作': [
    'npm install -g <pkg>  # 全局安装',
    'npm uninstall -g <pkg> # 全局卸载',
    'npm list -g --depth=0 # 查看全局安装的包'
  ],
  '其他常用': [
    'npx <pkg>             # 临时运行包',
    'npm cache clean --force # 清除缓存',
    'npm config list       # 查看配置',
    'npm login             # 登录 npm',
    'npm publish           # 发布包'
  ]
};

console.log('=== npm 常用命令 ===');
Object.entries(npmCommands).forEach(([category, commands]) => {
  console.log(`\n【${category}】`);
  commands.forEach(cmd => console.log(`  ${cmd}`));
});

// 2. package.json 完整示例
const completePackageJson = {
  name: 'my-awesome-package',
  version: '1.0.0',
  description: 'A description of my package',
  author: {
    name: 'Your Name',
    email: 'your@email.com',
    url: 'https://yourwebsite.com'
  },
  contributors: [
    { name: 'Contributor 1', email: 'contrib1@email.com' }
  ],
  license: 'MIT',
  homepage: 'https://github.com/user/repo',
  repository: {
    type: 'git',
    url: 'https://github.com/user/repo.git'
  },
  bugs: {
    url: 'https://github.com/user/repo/issues',
    email: 'bugs@email.com'
  },
  keywords: ['node', 'javascript', 'package'],
  main: 'dist/index.js',
  module: 'dist/index.esm.js',
  types: 'dist/index.d.ts',
  files: ['dist', 'README.md'],
  bin: {
    'my-cli': './bin/cli.js'
  },
  man: './man/my-package.1',
  scripts: {
    start: 'node dist/index.js',
    dev: 'nodemon src/index.js',
    build: 'webpack --mode production',
    test: 'jest',
    test:watch: 'jest --watch',
    lint: 'eslint src',
    format: 'prettier --write src',
    precommit: 'npm run lint && npm run test',
    prepublishOnly: 'npm run build'
  },
  dependencies: {
    express: '^4.18.0',
    lodash: '~4.17.21',
    axios: '1.4.0'
  },
  devDependencies: {
    nodemon: '^2.0.20',
    jest: '^29.0.0',
    eslint: '^8.0.0',
    webpack: '^5.0.0'
  },
  peerDependencies: {
    react: '>=17.0.0'
  },
  optionalDependencies: {
    fsevents: '^2.3.0'
  },
  engines: {
    node: '>=16.0.0',
    npm: '>=8.0.0'
  },
  os: ['darwin', 'linux', 'win32'],
  cpu: ['x64', 'arm64'],
  private: false,
  publishConfig: {
    registry: 'https://registry.npmjs.org/'
  },
  workspaces: [
    'packages/*'
  ]
};

console.log('\n=== package.json 完整示例 ===');
console.log(JSON.stringify(completePackageJson, null, 2));

// 3. npm 配置（.npmrc）
const npmrcExample = `
# .npmrc 配置文件

# 注册表源
registry=https://registry.npmmirror.com/

# 缓存目录
cache=~/.npm

# 代理配置
# proxy=http://proxy.example.com:8080
# https-proxy=http://proxy.example.com:8080

# 严格模式
strict-ssl=true

# 保存时自动保存 exact 版本
save-exact=true

# 保存时自动添加 ^ 前缀
save-prefix=^

# 初始化默认值
init-author-name=Your Name
init-author-email=your@email.com
init-license=MIT
init-version=1.0.0
`;

console.log('\n=== .npmrc 配置示例 ===');
console.log(npmrcExample);

// 4. npm config 命令
const npmConfigCommands = [
  'npm config list                   # 查看所有配置',
  'npm config get registry           # 查看 registry 配置',
  'npm config set registry <url>    # 设置 registry',
  'npm config delete registry        # 删除配置',
  'npm config edit                   # 编辑配置文件'
];

console.log('\n=== npm config 命令 ===');
npmConfigCommands.forEach(cmd => console.log(`  ${cmd}`));

// 5. 切换镜像源
const registryMirrors = {
  npm: 'https://registry.npmjs.org/',
  淘宝: 'https://registry.npmmirror.com/',
  腾讯云: 'https://mirrors.cloud.tencent.com/npm/',
  华为云: 'https://mirrors.huaweicloud.com/repository/npm/'
};

console.log('\n=== 常用镜像源 ===');
Object.entries(registryMirrors).forEach(([name, url]) => {
  console.log(`  ${name}: ${url}`);
});
console.log('\n切换命令: npm config set registry <url>');

// 6. npx 使用
const npxExamples = [
  'npx create-react-app my-app       # 创建 React 应用',
  'npx vite@latest init              # 创建 Vite 项目',
  'npx eslint .                       # 运行本地或最新 eslint',
  'npx -p typescript tsc             # 指定包运行',
  'npx node@16 script.js             # 使用特定版本 node',
  'npx --no-install <pkg>            # 不安装，只使用本地'
];

console.log('\n=== npx 使用示例 ===');
npxExamples.forEach(cmd => console.log(`  ${cmd}`));

// 7. npm scripts 生命周期
const npmScriptLifecycle = [
  'prepublish          # 在发布前运行',
  'prepare            # 在打包前运行',
  'prepublishOnly     # 在 publish 前运行',
  'prepack            # 在打包前运行',
  'postpack           # 在打包后运行',
  'publish            # 发布',
  'postpublish        # 发布后运行',
  'preinstall         # 安装前运行',
  'install            # 安装',
  'postinstall        # 安装后运行',
  'preuninstall       # 卸载前运行',
  'uninstall          # 卸载',
  'postuninstall      # 卸载后运行',
  'preversion         # 版本更新前运行',
  'version            # 版本更新',
  'postversion        # 版本更新后运行',
  'pretest            # 测试前运行',
  'test               # 测试',
  'posttest           # 测试后运行',
  'prestop            # 停止前运行',
  'stop               # 停止',
  'poststop           # 停止后运行',
  'prestart           # 启动前运行',
  'start              # 启动',
  'poststart          # 启动后运行'
];

console.log('\n=== npm scripts 生命周期 ===');
npmScriptLifecycle.forEach(script => console.log(`  ${script}`));

// 8. npm workspaces 示例
const workspacesExample = {
  '根目录 package.json': {
    name: 'my-monorepo',
    private: true,
    workspaces: ['packages/*']
  },
  '目录结构': `
my-monorepo/
├── package.json
├── packages/
│   ├── utils/
│   │   └── package.json
│   ├── components/
│   │   └── package.json
│   └── app/
│       └── package.json
`
};

console.log('\n=== npm workspaces 示例 ===');
console.log('目录结构:', workspacesExample['目录结构']);
console.log('根 package.json:', JSON.stringify(workspacesExample['根目录 package.json'], null, 2));

const workspaceCommands = [
  'npm install                          # 安装所有 workspace 依赖',
  'npm run build --workspace=packages/utils',
  'npm run build -w packages/utils     # 简写',
  'npm add <pkg> -w packages/utils     # 给指定 workspace 添加依赖',
  'npm run build --workspaces           # 所有 workspace 运行脚本'
];

console.log('\nworkspaces 命令:');
workspaceCommands.forEach(cmd => console.log(`  ${cmd}`));
