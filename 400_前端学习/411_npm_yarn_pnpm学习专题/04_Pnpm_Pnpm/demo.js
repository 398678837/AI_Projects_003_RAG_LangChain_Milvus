// pnpm 使用示例代码

// 1. pnpm 常用命令速查
const pnpmCommands = {
  '初始化项目': [
    'pnpm init              # 交互式创建',
    'pnpm init -y           # 使用默认值'
  ],
  '安装依赖': [
    'pnpm install           # 安装所有依赖',
    'pnpm i                 # 简写',
    'pnpm install --prod    # 只安装生产依赖'
  ],
  '添加依赖': [
    'pnpm add <pkg>         # 添加到 dependencies',
    'pnpm add <pkg>@<version>',
    'pnpm add <pkg> --save-exact # 精确版本',
    'pnpm add <pkg> -w      # 安装到 workspace 根目录'
  ],
  '添加开发依赖': [
    'pnpm add -D <pkg>',
    'pnpm add --save-dev <pkg>'
  ],
  '添加可选依赖': [
    'pnpm add -O <pkg>',
    'pnpm add --save-optional <pkg>'
  ],
  '添加全局依赖': [
    'pnpm add -g <pkg>'
  ],
  '卸载依赖': [
    'pnpm remove <pkg>',
    'pnpm rm <pkg>',
    'pnpm remove <pkg> -w'
  ],
  '更新依赖': [
    'pnpm update            # 更新所有依赖',
    'pnpm up                # 简写',
    'pnpm update <pkg>      # 更新指定包',
    'pnpm outdated          # 检查过时的包'
  ],
  '运行脚本': [
    'pnpm <script>          # 运行脚本',
    'pnpm start',
    'pnpm test',
    'pnpm dev'
  ],
  '查看信息': [
    'pnpm list              # 查看依赖',
    'pnpm list <pkg>',
    'pnpm info <pkg>        # 查看包信息',
    'pnpm why <pkg>         # 查看为什么安装',
    'pnpm store status      # 查看存储状态'
  ],
  '存储管理': [
    'pnpm store path        # 查看存储路径',
    'pnpm store prune       # 清理未使用的包',
    'pnpm store add <pkg>   # 添加包到存储'
  ],
  '全局命令': [
    'pnpm list -g           # 查看全局包',
    'pnpm remove -g <pkg>'
  ],
  '其他': [
    'pnpm dlx <pkg>         # 类似 npx',
    'pnpm exec <cmd>        # 执行命令',
    'pnpm create <pkg>      # 创建项目',
    'pnpm link               # 链接本地包',
    'pnpm publish            # 发布包',
    'pnpm audit              # 安全审计'
  ]
};

console.log('=== pnpm 常用命令 ===');
Object.entries(pnpmCommands).forEach(([category, commands]) => {
  console.log(`\n【${category}】`);
  commands.forEach(cmd => console.log(`  ${cmd}`));
});

// 2. pnpm 的核心优势
const pnpmAdvantages = {
  '节省磁盘空间': {
    原理: '硬链接到全局存储，同一包只存一份',
    效果: '节省 50-90% 磁盘空间'
  },
  '安装速度快': {
    原理: '跳过已存在的包，直接链接',
    效果: '比 npm/yarn 快 2-3 倍'
  },
  '严格的依赖管理': {
    原理: '非扁平 node_modules，避免幽灵依赖',
    效果: '更可靠，更少的意外'
  },
  '内容寻址': {
    原理: '基于内容哈希存储，保证完整性',
    效果: '更安全，可验证'
  }
};

console.log('\n=== pnpm 核心优势 ===');
Object.entries(pnpmAdvantages).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  原理: ${info.原理}`);
  console.log(`  效果: ${info.效果}`);
});

// 3. pnpm 的 node_modules 结构
const nodeModulesStructure = {
  'npm/yarn (扁平)': `
node_modules/
├── pkg-a/
├── pkg-b/
└── pkg-c/  # pkg-a 的依赖，但被提升了
  `,
  'pnpm (严格)': `
node_modules/
├── .pnpm/
│   ├── pkg-a@1.0.0/
│   │   └── node_modules/
│   │       ├── pkg-a -> ../../../../pkg-a
│   │       └── pkg-c -> ../../../../pkg-c
│   └── pkg-c@1.0.0/
├── pkg-a -> .pnpm/pkg-a@1.0.0/node_modules/pkg-a
└── pkg-c -> .pnpm/pkg-c@1.0.0/node_modules/pkg-c
  `
};

console.log('\n=== node_modules 结构对比 ===');
console.log('npm/yarn (扁平):', nodeModulesStructure['npm/yarn (扁平)']);
console.log('pnpm (严格):', nodeModulesStructure['pnpm (严格)']);

// 4. pnpm 配置文件
const npmrcPnpm = `
# .npmrc (pnpm 配置)

# 注册表
registry=https://registry.npmmirror.com/

# 存储目录
store-dir=~/.pnpm-store

# 严格模式（禁止幽灵依赖）
strict-peer-dependencies=true

# 自动安装 peer dependencies
auto-install-peers=true

# 链接方式
node-linker=hoisted  # 可选: isolated, hoisted, pnp

# 允许提升某些包
public-hoist-pattern[]=*eslint*
public-hoist-pattern[]=*prettier*
`;

console.log('\n=== .npmrc (pnpm) 示例 ===');
console.log(npmrcPnpm);

// 5. pnpm Workspace
const pnpmWorkspace = {
  'pnpm-workspace.yaml': `
packages:
  - 'packages/*'
  - 'apps/*'
  `,
  '常用命令': [
    'pnpm -F <name> add <pkg>     # 给指定 package 添加依赖',
    'pnpm -F <name> run <script>  # 运行指定 package 脚本',
    'pnpm -r run build             # 递归运行所有 package',
    'pnpm -r --parallel run dev    # 并行运行',
    'pnpm create <pkg>             # 使用 create-* 包'
  ]
};

console.log('\n=== pnpm Workspace ===');
console.log('pnpm-workspace.yaml:', pnpmWorkspace['pnpm-workspace.yaml']);
console.log('\n常用命令:');
pnpmWorkspace['常用命令'].forEach(cmd => console.log(`  ${cmd}`));

// 6. pnpm vs npm vs Yarn 对比
const pmComparison = {
  特性: ['安装速度', '磁盘占用', '严格依赖', '幽灵依赖', '离线模式', 'Workspaces', 'Zero-Installs'],
  npm: ['⭐⭐', '⭐', '❌', '⚠️', '❌', '⭐⭐', '❌'],
  Yarn: ['⭐⭐⭐', '⭐', '❌', '⚠️', '⭐⭐⭐', '⭐⭐⭐', '⭐⭐⭐'],
  pnpm: ['⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐', '❌', '⭐⭐⭐', '⭐⭐⭐⭐', '❌']
};

console.log('\n=== 三者对比 ===');
console.log('特性'.padEnd(12) + '  npm   Yarn   pnpm');
pmComparison.特性.forEach((feature, i) => {
  console.log(
    feature.padEnd(12) + 
    '  ' + pmComparison.npm[i].padEnd(6) + 
    '  ' + pmComparison.Yarn[i].padEnd(6) + 
    '  ' + pmComparison.pnpm[i]
  );
});

// 7. 常用 pnpm create 命令
const pnpmCreateCommands = [
  'pnpm create vite@latest',
  'pnpm create vue@latest',
  'pnpm create react-app my-app',
  'pnpm create next-app',
  'pnpm create astro@latest',
  'pnpm create svelte@latest'
];

console.log('\n=== pnpm create 命令 ===');
pnpmCreateCommands.forEach(cmd => console.log(`  ${cmd}`));

// 8. pnpm 存储管理
const storeCommands = [
  'pnpm store path           # 查看存储位置',
  'pnpm store status         # 查看存储状态',
  'pnpm store prune          # 清理未使用的包',
  'pnpm store add <pkg>      # 添加包到存储'
];

console.log('\n=== 存储管理 ===');
storeCommands.forEach(cmd => console.log(`  ${cmd}`));

// 9. 为什么选择 pnpm？
const whyChoosePnpm = [
  '大型项目节省大量磁盘空间',
  'Monorepo 支持非常好',
  '安装速度极快',
  '严格依赖管理，避免问题',
  '社区活跃，发展迅速',
  '很多大公司在使用（Vue, Vite 等）'
];

console.log('\n=== 为什么选择 pnpm ===');
whyChoosePnpm.forEach(reason => console.log(`  ${reason}`));
