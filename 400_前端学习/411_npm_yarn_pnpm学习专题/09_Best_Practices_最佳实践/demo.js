// 包管理器最佳实践示例代码

// 1. 包管理器选择指南
const choosePM = {
  '小型项目/学习': {
    推荐: 'npm',
    理由: '无需额外安装，生态最成熟'
  },
  '中型项目': {
    推荐: 'pnpm',
    理由: '节省磁盘空间，速度快'
  },
  '大型项目/Monorepo': {
    推荐: 'pnpm',
    理由: 'workspaces 支持好，严格依赖管理'
  },
  'React生态': {
    推荐: 'pnpm 或 Yarn',
    理由: '与 React 生态配合良好'
  },
  '追求稳定性': {
    推荐: 'npm',
    理由: '最稳定，问题少'
  }
};

console.log('=== 包管理器选择指南 ===');
Object.entries(choosePM).forEach(([scenario, info]) => {
  console.log(`\n【${scenario}】`);
  console.log(`  推荐: ${info.推荐}`);
  console.log(`  理由: ${info.理由}`);
});

// 2. 依赖管理最佳实践
const depBestPractices = [
  {
    实践: '提交 lock 文件',
    说明: 'package-lock.json / yarn.lock / pnpm-lock.yaml 必须提交到 Git',
    原因: '确保团队成员和 CI/CD 安装完全相同的依赖'
  },
  {
    实践: '定期更新依赖',
    说明: '使用 npm outdated / yarn outdated / pnpm outdated 检查',
    原因: '获取 bug 修复、安全更新、新功能'
  },
  {
    实践: '安全审计',
    说明: '定期运行 npm audit',
    原因: '及时发现和修复安全漏洞'
  },
  {
    实践: '区分 dependencies 和 devDependencies',
    说明: '生产依赖放 dependencies，开发工具放 devDependencies',
    原因: '减小生产构建体积'
  },
  {
    实践: '使用确切版本或合理范围',
    说明: '^ 适合大多数，~ 适合保守，精确版本适合关键依赖',
    原因: '平衡稳定性和更新便利性'
  },
  {
    实践: '删除未使用的依赖',
    说明: '定期检查并删除不用的包',
    原因: '减小 node_modules 体积，降低安全风险'
  }
];

console.log('\n=== 依赖管理最佳实践 ===');
depBestPractices.forEach((item, i) => {
  console.log(`\n${i + 1}. ${item.实践}`);
  console.log(`   ${item.说明}`);
  console.log(`   原因: ${item.原因}`);
});

// 3. 脚本最佳实践
const scriptBestPractices = [
  '✅ 使用清晰的命名',
  '   build, dev, test, lint 而非 random-script',
  '',
  '✅ 将复杂脚本拆分为小脚本',
  '   然后组合使用 pre/post 或 npm-run-all',
  '',
  '✅ 使用 cross-env 跨平台',
  '   避免 Windows/Unix 兼容性问题',
  '',
  '✅ 使用 rimraf 替代 rm -rf',
  '   跨平台删除文件',
  '',
  '✅ 文档化复杂脚本',
  '   在 README 或注释中说明用途',
  '',
  '✅ 避免在脚本中写死路径',
  '   使用 npm_package_* 变量'
];

console.log('\n=== 脚本最佳实践 ===');
scriptBestPractices.forEach(p => console.log(`  ${p}`));

// 4. 安全最佳实践
const securityBestPractices = [
  {
    实践: '定期运行 npm audit',
    频率: '每周或每次添加新依赖后'
  },
  {
    实践: '使用 Dependabot',
    说明: '自动创建 PR 更新依赖',
    平台: 'GitHub, GitLab'
  },
  {
    实践: '限制 npm scripts 权限',
    说明: '使用 --ignore-scripts 安装不受信任的包',
    命令: 'npm install --ignore-scripts'
  },
  {
    实践: '使用 npm ci 而非 npm install',
    说明: 'CI/CD 中使用，确保安装 lock 文件中的精确版本',
    优势: '更快，更可预测'
  },
  {
    实践: '验证包的完整性',
    说明: '使用 package-lock.json 验证',
    工具: 'npm ci, snyk, socket.dev'
  }
];

console.log('\n=== 安全最佳实践 ===');
securityBestPractices.forEach((item, i) => {
  console.log(`\n${i + 1}. ${item.实践}`);
  if (item.说明) console.log(`   说明: ${item.说明}`);
  if (item.频率) console.log(`   频率: ${item.频率}`);
  if (item.命令) console.log(`   命令: ${item.命令}`);
});

// 5. 性能优化
const performanceTips = [
  {
    优化: '使用 pnpm',
    效果: '节省 50-90% 磁盘空间，安装更快'
  },
  {
    优化: '配置缓存',
    说明: 'npm/yarn/pnpm 都有缓存，利用好'
  },
  {
    优化: '使用 npm ci',
    场景: 'CI/CD 环境',
    优势: '比 npm install 快'
  },
  {
    优化: '使用国内镜像',
    说明: '淘宝镜像、腾讯云镜像等',
    命令: 'npm config set registry https://registry.npmmirror.com/'
  },
  {
    优化: '定期清理缓存',
    命令: 'npm cache clean --force, pnpm store prune'
  }
];

console.log('\n=== 性能优化 ===');
performanceTips.forEach((item, i) => {
  console.log(`\n${i + 1}. ${item.优化}`);
  if (item.效果) console.log(`   效果: ${item.效果}`);
  if (item.说明) console.log(`   说明: ${item.说明}`);
  if (item.命令) console.log(`   命令: ${item.命令}`);
});

// 6. 不要做的事情
const dontDoList = [
  '❌ 不要提交 node_modules 到 Git',
  '❌ 不要忽略 lock 文件',
  '❌ 不要使用 * 作为版本范围',
  '❌ 不要在 dependencies 放开发工具',
  '❌ 不要忽略 npm audit 警告',
  '❌ 不要随意使用 --force 或 --legacy-peer-deps',
  '❌ 不要运行不信任的包的 scripts',
  '❌ 不要在 package.json 中提交机密信息'
];

console.log('\n=== 不要做的事情 ===');
dontDoList.forEach(item => console.log(`  ${item}`));

// 7. Monorepo 最佳实践
const monorepoBestPractices = [
  {
    工具: 'pnpm workspaces',
    优势: '性能好，严格依赖管理'
  },
  {
    工具: 'Yarn workspaces',
    优势: '成熟稳定'
  },
  {
    工具: 'npm workspaces',
    优势: '无需额外安装'
  },
  {
    实践: '使用 Turborepo / Nx',
    说明: '智能缓存，并行任务'
  }
];

console.log('\n=== Monorepo 最佳实践 ===');
monorepoBestPractices.forEach((item, i) => {
  console.log(`\n${i + 1}. ${item.工具}`);
  if (item.优势) console.log(`   优势: ${item.优势}`);
  if (item.说明) console.log(`   说明: ${item.说明}`);
});

// 8. 推荐的工具
const recommendedTools = {
  '依赖管理': [
    'pnpm - 节省空间，速度快',
    'npm-check-updates - 更新 package.json 版本',
    'depcheck - 检查未使用的依赖'
  ],
  '脚本工具': [
    'npm-run-all - 并行/串行运行脚本',
    'concurrently - 同时运行多个命令',
    'cross-env - 跨平台环境变量',
    'rimraf - 跨平台删除'
  ],
  '安全工具': [
    'npm audit - 内置审计',
    'snyk - 安全扫描',
    'socket.dev - 供应链安全'
  ],
  'Monorepo': [
    'pnpm workspaces',
    'Turborepo',
    'Nx'
  ]
};

console.log('\n=== 推荐工具 ===');
Object.entries(recommendedTools).forEach(([category, tools]) => {
  console.log(`\n【${category}】`);
  tools.forEach(tool => console.log(`  - ${tool}`));
});

// 9. 日常工作流
const dailyWorkflow = [
  '1. 开始新功能',
  '   git pull',
  '   pnpm install (如果 lock 文件有变化)',
  '',
  '2. 添加新依赖',
  '   pnpm add <package>',
  '   检查是否有安全警告',
  '   提交 lock 文件',
  '',
  '3. 每周维护',
  '   pnpm outdated',
  '   pnpm audit',
  '   更新依赖',
  '',
  '4. 发布前',
  '   运行所有测试',
  '   再次检查依赖',
  '   清理 node_modules 重新安装验证'
];

console.log('\n=== 日常工作流 ===');
dailyWorkflow.forEach(step => console.log(`  ${step}`));
