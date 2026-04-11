// npm/yarn/pnpm 学习专题总结

// 1. 包管理器速查表
const cheatSheet = {
  操作: {
    '初始化项目': {
      npm: 'npm init',
      yarn: 'yarn init',
      pnpm: 'pnpm init'
    },
    '安装所有依赖': {
      npm: 'npm install',
      yarn: 'yarn',
      pnpm: 'pnpm install'
    },
    '添加依赖': {
      npm: 'npm install <pkg>',
      yarn: 'yarn add <pkg>',
      pnpm: 'pnpm add <pkg>'
    },
    '添加开发依赖': {
      npm: 'npm install -D <pkg>',
      yarn: 'yarn add -D <pkg>',
      pnpm: 'pnpm add -D <pkg>'
    },
    '卸载依赖': {
      npm: 'npm uninstall <pkg>',
      yarn: 'yarn remove <pkg>',
      pnpm: 'pnpm remove <pkg>'
    },
    '更新依赖': {
      npm: 'npm update',
      yarn: 'yarn upgrade',
      pnpm: 'pnpm update'
    },
    '运行脚本': {
      npm: 'npm run <script>',
      yarn: 'yarn <script>',
      pnpm: 'pnpm <script>'
    },
    'npx/dlx': {
      npm: 'npx <pkg>',
      yarn: 'yarn dlx <pkg>',
      pnpm: 'pnpm dlx <pkg>'
    },
    '安全审计': {
      npm: 'npm audit',
      yarn: 'yarn audit',
      pnpm: 'pnpm audit'
    },
    '发布包': {
      npm: 'npm publish',
      yarn: 'yarn publish',
      pnpm: 'pnpm publish'
    }
  }
};

console.log('=== 命令速查表 ===');
console.log('操作'.padEnd(18) + '  npm'.padEnd(20) + '  yarn'.padEnd(20) + '  pnpm');
Object.entries(cheatSheet.操作).forEach(([action, cmds]) => {
  console.log(
    action.padEnd(18) + 
    '  ' + cmds.npm.padEnd(20) + 
    '  ' + cmds.yarn.padEnd(20) + 
    '  ' + cmds.pnpm
  );
});

// 2. 三者对比总结
const comparisonSummary = {
  npm: {
    发布时间: '2010',
    安装速度: '⭐⭐',
    磁盘占用: '⭐',
    严格依赖: '❌',
    离线模式: '❌',
    Workspaces: '⭐⭐',
    ZeroInstalls: '❌',
    生态: '⭐⭐⭐⭐⭐',
    推荐场景: '小型项目/学习/追求稳定'
  },
  Yarn: {
    发布时间: '2016',
    安装速度: '⭐⭐⭐',
    磁盘占用: '⭐',
    严格依赖: '❌',
    离线模式: '⭐⭐⭐',
    Workspaces: '⭐⭐⭐',
    ZeroInstalls: '⭐⭐⭐',
    生态: '⭐⭐⭐⭐',
    推荐场景: 'React生态/需要离线模式'
  },
  pnpm: {
    发布时间: '2017',
    安装速度: '⭐⭐⭐⭐⭐',
    磁盘占用: '⭐⭐⭐⭐⭐',
    严格依赖: '⭐⭐⭐⭐⭐',
    离线模式: '⭐⭐⭐',
    Workspaces: '⭐⭐⭐⭐',
    ZeroInstalls: '❌',
    生态: '⭐⭐⭐⭐',
    推荐场景: '中大型项目/Monorepo/节省空间'
  }
};

console.log('\n=== 三者对比总结 ===');
console.log('特性'.padEnd(15) + '  npm    Yarn   pnpm');
console.log('安装速度'.padEnd(15) + '  ⭐⭐    ⭐⭐⭐  ⭐⭐⭐⭐⭐');
console.log('磁盘占用'.padEnd(15) + '  ⭐     ⭐     ⭐⭐⭐⭐⭐');
console.log('严格依赖'.padEnd(15) + '  ❌     ❌     ⭐⭐⭐⭐⭐');
console.log('生态'.padEnd(15) + '  ⭐⭐⭐⭐⭐ ⭐⭐⭐⭐  ⭐⭐⭐⭐');

// 3. 选择决策树
function choosePackageManager(project) {
  if (project.size === 'small' || project.experience === 'beginner') {
    return 'npm - 最简单，无需额外安装';
  }
  if (project.monorepo || project.size === 'large') {
    return 'pnpm - Workspaces 支持好，节省空间';
  }
  if (project.reactEcosystem) {
    return 'pnpm 或 Yarn - 与 React 配合好';
  }
  if (project.diskSpace === 'limited') {
    return 'pnpm - 节省 50-90% 空间';
  }
  if (project.stability === 'most-important') {
    return 'npm - 最稳定成熟';
  }
  return 'pnpm - 综合表现最好';
}

console.log('\n=== 选择建议 ===');
const testProjects = [
  { size: 'small', experience: 'beginner', desc: '小型项目/新手' },
  { size: 'large', monorepo: true, desc: '大型Monorepo' },
  { reactEcosystem: true, desc: 'React生态' },
  { diskSpace: 'limited', desc: '磁盘空间有限' },
  { stability: 'most-important', desc: '最看重稳定性' }
];
testProjects.forEach(p => {
  console.log(`  ${p.desc.padEnd(20)} → ${choosePackageManager(p)}`);
});

// 4. 核心概念回顾
const coreConcepts = {
  'package.json': '项目配置文件，包含依赖、脚本等',
  '语义化版本': 'MAJOR.MINOR.PATCH，规则更新',
  '版本范围': '^, ~, *, >, >= 等符号',
  '依赖类型': 'dependencies, devDependencies, peerDependencies',
  'Lock文件': 'package-lock.json/yarn.lock/pnpm-lock.yaml，锁定版本',
  'node_modules': '依赖安装目录',
  '脚本': 'npm scripts，定义常用命令',
  'Workspaces': 'Monorepo 支持',
  '注册表': '存储包的服务器，如 npmjs.com'
};

console.log('\n=== 核心概念回顾 ===');
Object.entries(coreConcepts).forEach(([term, desc]) => {
  console.log(`  ${term.padEnd(18)}: ${desc}`);
});

// 5. 最佳实践清单
const bestPracticeChecklist = [
  '✅ 提交 lock 文件到 Git',
  '✅ 不要提交 node_modules',
  '✅ 定期运行 npm audit',
  '✅ 使用 Dependabot 更新依赖',
  '✅ 区分 dependencies 和 devDependencies',
  '✅ 使用合理的版本范围（^或~）',
  '✅ 使用 cross-env 跨平台',
  '✅ 使用 rimraf 替代 rm -rf',
  '✅ 定期清理未使用的依赖',
  '✅ CI/CD 使用 npm ci/pnpm install --frozen-lockfile'
];

console.log('\n=== 最佳实践清单 ===');
bestPracticeChecklist.forEach((item, i) => console.log(`${i + 1}. ${item}`));

// 6. 学习路径回顾
const learningPath = [
  {
    章节: '01_Basic_Concepts',
    内容: '包管理器简介、对比、核心概念',
    重点: '理解包管理器的作用和区别'
  },
  {
    章节: '02_NPM',
    内容: 'npm 命令、配置、高级功能',
    重点: '掌握 npm 的常用操作'
  },
  {
    章节: '03_Yarn',
    内容: 'Yarn 特点、命令、Berry',
    重点: '了解 Yarn 的优势'
  },
  {
    章节: '04_Pnpm',
    内容: 'pnpm 原理、命令、优势',
    重点: '理解硬链接和严格依赖'
  },
  {
    章节: '05_Package_Management',
    内容: '包的结构、发布流程',
    重点: '学会如何发布包'
  },
  {
    章节: '06_Dependency_Management',
    内容: '依赖类型、版本、安全',
    重点: '掌握依赖管理'
  },
  {
    章节: '07_Scripts',
    内容: 'npm scripts、生命周期',
    重点: '编写高效的脚本'
  },
  {
    章节: '08_Publishing',
    内容: '发布流程、版本管理',
    重点: '学会发布和维护包'
  },
  {
    章节: '09_Best_Practices',
    内容: '最佳实践、安全、性能',
    重点: '应用到实际项目'
  },
  {
    章节: '10_Summary',
    内容: '总结回顾、速查表',
    重点: '巩固和应用'
  }
];

console.log('\n=== 学习路径回顾 ===');
learningPath.forEach((item, i) => {
  console.log(`\n${i + 1}. ${item.章节}`);
  console.log(`   内容: ${item.内容}`);
  console.log(`   重点: ${item.重点}`);
});

// 7. 推荐资源
const recommendedResources = {
  官方文档: [
    'npm: https://docs.npmjs.com/',
    'Yarn: https://yarnpkg.com/',
    'pnpm: https://pnpm.io/'
  ],
  工具: [
    'npm-check-updates: 更新依赖版本',
    'depcheck: 检查未使用的依赖',
    'snyk: 安全扫描',
    'Turborepo: Monorepo 构建工具'
  ],
  文章: [
    'Semantic Versioning: https://semver.org/',
    'Why pnpm?: https://pnpm.io/feature-comparison'
  ]
};

console.log('\n=== 推荐资源 ===');
Object.entries(recommendedResources).forEach(([category, items]) => {
  console.log(`\n【${category}】`);
  items.forEach(item => console.log(`  - ${item}`));
});

console.log('\n🎉 恭喜完成 npm/yarn/pnpm 学习专题！');
console.log('💡 记住：选择合适的工具，遵循最佳实践，定期维护依赖。');
console.log('🚀 现在你可以高效地管理项目依赖了！');
