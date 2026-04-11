// Yarn 使用示例代码

// 1. Yarn 常用命令速查
const yarnCommands = {
  '初始化项目': [
    'yarn init              # 交互式创建',
    'yarn init -y           # 使用默认值'
  ],
  '安装依赖': [
    'yarn                   # 安装所有依赖',
    'yarn install           # 完整命令',
    'yarn --production      # 只安装生产依赖'
  ],
  '添加依赖': [
    'yarn add <pkg>         # 添加到 dependencies',
    'yarn add <pkg>@<version>',
    'yarn add <pkg>@^1.2.3',
    'yarn add <pkg> --exact # 精确版本'
  ],
  '添加开发依赖': [
    'yarn add -D <pkg>',
    'yarn add --dev <pkg>'
  ],
  '添加全局依赖': [
    'yarn global add <pkg>'
  ],
  '卸载依赖': [
    'yarn remove <pkg>',
    'yarn remove <pkg> -W   # workspaces'
  ],
  '更新依赖': [
    'yarn upgrade            # 更新所有依赖',
    'yarn upgrade <pkg>     # 更新指定包',
    'yarn upgrade-interactive # 交互式更新',
    'yarn outdated          # 检查过时的包'
  ],
  '运行脚本': [
    'yarn <script>          # 运行脚本',
    'yarn start',
    'yarn test',
    'yarn dev'
  ],
  '查看信息': [
    'yarn list               # 查看依赖树',
    'yarn info <pkg>        # 查看包信息',
    'yarn why <pkg>         # 查看为什么安装',
    'yarn versions          # 查看版本'
  ],
  '缓存和清理': [
    'yarn cache list         # 查看缓存',
    'yarn cache clean        # 清理缓存',
    'yarn autoclean          # 清理 node_modules'
  ],
  '全局命令': [
    'yarn global list        # 查看全局包',
    'yarn global remove <pkg>'
  ],
  '其他': [
    'yarn dlx <pkg>         # 类似 npx',
    'yarn link               # 链接本地包',
    'yarn unlink',
    'yarn publish            # 发布包'
  ]
};

console.log('=== Yarn 常用命令 ===');
Object.entries(yarnCommands).forEach(([category, commands]) => {
  console.log(`\n【${category}】`);
  commands.forEach(cmd => console.log(`  ${cmd}`));
});

// 2. Yarn 1 vs Yarn 2/3 (Berry)
const yarnVersions = {
  'Yarn 1 (Classic)': {
    发布时间: '2016年',
    特点: '稳定，广泛使用',
    node_modules: '使用',
    推荐: '⭐⭐⭐⭐ 稳定项目'
  },
  'Yarn 2/3 (Berry)': {
    发布时间: '2020年',
    特点: '全新架构，PnP',
    node_modules: '可选/Zero-Installs',
    推荐: '⭐⭐⭐⭐⭐ 新项目'
  }
};

console.log('\n=== Yarn 版本对比 ===');
Object.entries(yarnVersions).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  发布时间: ${info.发布时间}`);
  console.log(`  特点: ${info.特点}`);
  console.log(`  node_modules: ${info.node_modules}`);
  console.log(`  推荐: ${info.推荐}`);
});

// 3. Yarn Berry 特性
const berryFeatures = {
  'Plug\'n\'Play (PnP)': {
    说明: '不再需要 node_modules',
    优势: '更快的安装，更少的磁盘占用'
  },
  'Zero-Installs': {
    说明: '将依赖提交到仓库',
    优势: '团队成员无需安装依赖'
  },
  '工作区': {
    说明: '内置强大的 monorepo 支持',
    优势: '轻松管理多个包'
  },
  'Constraints': {
    说明: '强制项目规则',
    优势: '保持一致性'
  }
};

console.log('\n=== Yarn Berry 特性 ===');
Object.entries(berryFeatures).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  说明: ${info.说明}`);
  console.log(`  优势: ${info.优势}`);
});

// 4. 迁移到 Yarn Berry
const migrateToBerry = [
  'yarn set version berry          # 升级到最新版本',
  'yarn install                    # 安装依赖',
  '# 会生成 .yarn 目录和 .pnp.cjs'
];

console.log('\n=== 迁移到 Yarn Berry ===');
migrateToBerry.forEach(cmd => console.log(`  ${cmd}`));

// 5. Yarn 配置文件
const yarnrcExample = `
# .yarnrc.yml

# 注册表
npmRegistryServer: "https://registry.npmmirror.com/"

# PnP 模式
nodeLinker: pnp

# 依赖压缩
compressionLevel: mixed

# 启用 Zero-Installs
enableGlobalCache: false

# 忽略脚本
enableScripts: false

# 插件
plugins:
  - path: .yarn/plugins/@yarnpkg/plugin-typescript.cjs
    spec: "@yarnpkg/plugin-typescript"
`;

console.log('\n=== .yarnrc.yml 示例 ===');
console.log(yarnrcExample);

// 6. Yarn Workspaces
const yarnWorkspacesExample = {
  'package.json': {
    name: 'my-monorepo',
    private: true,
    workspaces: ['packages/*']
  },
  '命令': [
    'yarn workspaces list               # 列出所有 workspace',
    'yarn workspace <name> add <pkg>   # 给指定 workspace 添加依赖',
    'yarn workspace <name> run <script> # 运行指定 workspace 脚本',
    'yarn workspaces foreach run build   # 所有 workspace 运行'
  ]
};

console.log('\n=== Yarn Workspaces ===');
console.log('package.json:', JSON.stringify(yarnWorkspacesExample['package.json'], null, 2));
console.log('\n常用命令:');
yarnWorkspacesExample['命令'].forEach(cmd => console.log(`  ${cmd}`));

// 7. Yarn vs npm 命令对比
const yarnVsNpm = {
  '初始化': { npm: 'npm init', yarn: 'yarn init' },
  '安装所有': { npm: 'npm install', yarn: 'yarn' },
  '添加依赖': { npm: 'npm install <pkg>', yarn: 'yarn add <pkg>' },
  '添加开发': { npm: 'npm install -D <pkg>', yarn: 'yarn add -D <pkg>' },
  '卸载': { npm: 'npm uninstall <pkg>', yarn: 'yarn remove <pkg>' },
  '更新': { npm: 'npm update', yarn: 'yarn upgrade' },
  '运行脚本': { npm: 'npm run <script>', yarn: 'yarn <script>' },
  'npx': { npm: 'npx <pkg>', yarn: 'yarn dlx <pkg>' }
};

console.log('\n=== Yarn vs npm 命令 ===');
console.log('操作            npm                yarn');
Object.entries(yarnVsNpm).forEach(([action, cmds]) => {
  console.log(`${action.padEnd(12)}  ${cmds.npm.padEnd(18)}  ${cmds.yarn}`);
});

// 8. Yarn 为什么快？
const whyYarnIsFast = [
  '并行下载: 同时下载多个包',
  '网络优化: 更好的请求队列',
  '离线缓存: 已下载的包无需重新下载',
  '确定性: yarn.lock 保证一致'
];

console.log('\n=== Yarn 为什么快 ===');
whyYarnIsFast.forEach(reason => console.log(`  ${reason}`));

// 9. 离线模式
const offlineMode = [
  'yarn install --offline          # 强制离线安装',
  'yarn cache dir                   # 查看缓存目录',
  'yarn cache list                  # 查看缓存的包'
];

console.log('\n=== 离线模式 ===');
offlineMode.forEach(cmd => console.log(`  ${cmd}`));
