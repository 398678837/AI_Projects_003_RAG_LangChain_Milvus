// 依赖管理示例代码

// 1. 版本范围详解
const versionRanges = {
  '精确版本': {
    '1.2.3': '必须等于 1.2.3'
  },
  'Patch 更新': {
    '~1.2.3': '>=1.2.3 <1.3.0',
    '~1.2': '>=1.2.0 <1.3.0'
  },
  'Minor 更新': {
    '^1.2.3': '>=1.2.3 <2.0.0',
    '^0.2.3': '>=0.2.3 <0.3.0',
    '^0.0.3': '>=0.0.3 <0.0.4'
  },
  '比较符': {
    '>1.2.3': '大于 1.2.3',
    '>=1.2.3': '大于等于 1.2.3',
    '<1.2.3': '小于 1.2.3',
    '<=1.2.3': '小于等于 1.2.3'
  },
  '范围组合': {
    '1.2.3 - 1.5.0': '>=1.2.3 <=1.5.0',
    '>=1.2.3 <1.5.0': '同上',
    '1.x': '>=1.0.0 <2.0.0',
    '1.2.x': '>=1.2.0 <1.3.0'
  },
  '最新版本': {
    '*': '任意版本（不推荐）',
    'latest': '最新版本',
    'x': '同 *'
  },
  '预发布版本': {
    '1.2.3-beta.1': '精确预发布版本',
    '^1.2.3-beta.1': '包含预发布版本'
  }
};

console.log('=== 版本范围详解 ===');
Object.entries(versionRanges).forEach(([category, ranges]) => {
  console.log(`\n【${category}】`);
  Object.entries(ranges).forEach(([range, desc]) => {
    console.log(`  ${range.padEnd(18)} → ${desc}`);
  });
});

// 2. 依赖类型
const dependencyTypes = {
  dependencies: {
    说明: '生产环境必需的依赖',
    安装命令: 'npm install <pkg>',
    示例: 'express, react, lodash',
    打包: '会被打包到生产代码'
  },
  devDependencies: {
    说明: '仅开发环境需要',
    安装命令: 'npm install -D <pkg>',
    示例: 'eslint, jest, webpack',
    打包: '不会被打包到生产代码'
  },
  peerDependencies: {
    说明: '需要宿主环境提供',
    安装命令: '不需要手动安装',
    示例: '插件依赖核心库',
    场景: 'react组件依赖 react'
  },
  optionalDependencies: {
    说明: '可选依赖，安装失败不影响',
    安装命令: 'npm install -O <pkg>',
    示例: 'fsevents (macOS only)',
    处理: '需要代码判断是否存在'
  }
};

console.log('\n=== 依赖类型 ===');
Object.entries(dependencyTypes).forEach(([type, info]) => {
  console.log(`\n【${type}】`);
  console.log(`  说明: ${info.说明}`);
  console.log(`  安装: ${info.安装命令}`);
  console.log(`  示例: ${info.示例}`);
});

// 3. peerDependencies 示例
const peerDepsExample = {
  '插件 package.json': {
    name: 'my-react-plugin',
    peerDependencies: {
      react: '>=17.0.0 <19.0.0',
      'react-dom': '>=17.0.0 <19.0.0'
    }
  },
  '宿主项目 package.json': {
    dependencies: {
      react: '^18.0.0',
      'react-dom': '^18.0.0',
      'my-react-plugin': '^1.0.0'
    }
  }
};

console.log('\n=== peerDependencies 示例 ===');
console.log('插件 package.json:', JSON.stringify(peerDepsExample['插件 package.json'], null, 2));

// 4. 锁定文件对比
const lockFiles = {
  'package-lock.json': {
    包管理器: 'npm',
    格式: 'JSON',
    作用: '锁定依赖版本，确保一致安装'
  },
  'yarn.lock': {
    包管理器: 'Yarn',
    格式: 'YAML',
    作用: '锁定依赖版本'
  },
  'pnpm-lock.yaml': {
    包管理器: 'pnpm',
    格式: 'YAML',
    作用: '锁定依赖版本'
  }
};

console.log('\n=== 锁定文件 ===');
Object.entries(lockFiles).forEach(([file, info]) => {
  console.log(`\n【${file}】`);
  console.log(`  包管理器: ${info.包管理器}`);
  console.log(`  作用: ${info.作用}`);
});
console.log('\n💡 锁定文件应该提交到 Git！');

// 5. 查看依赖树
const dependencyTreeCommands = [
  'npm list              # 查看所有依赖',
  'npm list --depth=0    # 只看直接依赖',
  'npm list <pkg>        # 查看指定包',
  'npm why <pkg>         # 查看为什么安装',
  'yarn why <pkg>',
  'pnpm why <pkg>'
];

console.log('\n=== 查看依赖树 ===');
dependencyTreeCommands.forEach(cmd => console.log(`  ${cmd}`));

// 6. 安全审计
const auditCommands = [
  'npm audit              # 检查安全漏洞',
  'npm audit fix          # 尝试自动修复',
  'npm audit fix --force  # 强制修复（可能破坏性）',
  'npm audit --json       # JSON 格式输出',
  'yarn audit',
  'pnpm audit'
];

console.log('\n=== 安全审计 ===');
auditCommands.forEach(cmd => console.log(`  ${cmd}`));

// 7. 更新依赖
const updateCommands = [
  'npm outdated           # 检查过时的包',
  'npm update             # 更新所有（遵循 package.json）',
  'npm update <pkg>       # 更新指定包',
  'yarn upgrade-interactive',
  'pnpm update -i',
  'npx npm-check-updates -u  # 更新 package.json 版本'
];

console.log('\n=== 更新依赖 ===');
updateCommands.forEach(cmd => console.log(`  ${cmd}`));

// 8. 常见问题处理
const commonIssues = [
  {
    问题: 'ERESOLVE unable to resolve dependency tree',
    原因: 'peerDependencies 冲突',
    解决: [
      '1. npm install --legacy-peer-deps',
      '2. 检查并更新依赖版本',
      '3. 使用 --force (谨慎)'
    ]
  },
  {
    问题: 'node_modules 过大',
    原因: '扁平结构，重复安装',
    解决: [
      '1. 使用 pnpm（硬链接节省空间）',
      '2. 清理缓存: npm cache clean --force',
      '3. 删除 node_modules 重新安装'
    ]
  },
  {
    问题: '幽灵依赖',
    原因: '使用了未在 package.json 声明的依赖',
    解决: [
      '1. 使用 pnpm 严格模式',
      '2. 添加到 dependencies',
      '3. 使用 ESLint 检测'
    ]
  }
];

console.log('\n=== 常见问题处理 ===');
commonIssues.forEach((issue, i) => {
  console.log(`\n${i + 1}. ${issue.问题}`);
  console.log(`   原因: ${issue.原因}`);
  console.log(`   解决:`);
  issue.解决.forEach(s => console.log(`     ${s}`));
});

// 9. 清理命令
const cleanupCommands = [
  'rm -rf node_modules package-lock.json && npm install',
  'npm cache clean --force',
  'pnpm store prune',
  'yarn cache clean'
];

console.log('\n=== 清理命令 ===');
cleanupCommands.forEach(cmd => console.log(`  ${cmd}`));
