// 包管理器基础概念示例代码

// 1. 包管理器对比
const packageManagers = {
  npm: {
    发布时间: '2010年',
    特点: 'Node.js官方，使用广泛',
    优点: '生态完善，文档丰富',
    缺点: 'node_modules 体积大，安装较慢'
  },
  Yarn: {
    发布时间: '2016年',
    特点: 'Facebook开发，注重速度和安全',
    优点: '安装速度快，离线模式',
    缺点: '需要额外安装'
  },
  pnpm: {
    发布时间: '2017年',
    特点: '节省磁盘空间，速度快',
    优点: '硬链接节省空间，严格的依赖管理',
    缺点: '相对较新，生态稍小'
  }
};

console.log('=== 包管理器对比 ===');
Object.entries(packageManagers).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  发布时间: ${info.发布时间}`);
  console.log(`  特点: ${info.特点}`);
  console.log(`  优点: ${info.优点}`);
  console.log(`  缺点: ${info.缺点}`);
});

// 2. package.json 结构示例
const packageJsonExample = {
  name: 'my-project',
  version: '1.0.0',
  description: '我的项目描述',
  main: 'index.js',
  scripts: {
    start: 'node index.js',
    dev: 'nodemon index.js',
    test: 'jest',
    build: 'webpack --mode production'
  },
  keywords: ['nodejs', 'javascript'],
  author: 'Your Name',
  license: 'MIT',
  dependencies: {
    'express': '^4.18.0',
    'lodash': '~4.17.21'
  },
  devDependencies: {
    'nodemon': '^2.0.20',
    'jest': '^29.0.0'
  },
  engines: {
    'node': '>=16.0.0'
  }
};

console.log('\n=== package.json 结构 ===');
console.log(JSON.stringify(packageJsonExample, null, 2));

// 3. 语义化版本（Semantic Versioning）
const semverExplained = {
  'MAJOR.MINOR.PATCH': {
    MAJOR: '主版本号，不兼容的API修改',
    MINOR: '次版本号，向下兼容的功能性新增',
    PATCH: '修订号，向下兼容的问题修正'
  },
  版本符号: {
    '^': '允许MINOR和PATCH更新（^1.2.3 → 1.x.x）',
    '~': '只允许PATCH更新（~1.2.3 → 1.2.x）',
    '*': '最新版本',
    '': '精确版本'
  },
  示例: {
    '^1.2.3': '>=1.2.3 <2.0.0',
    '~1.2.3': '>=1.2.3 <1.3.0',
    '1.2.3': '精确等于1.2.3'
  }
};

console.log('\n=== 语义化版本 ===');
console.log('MAJOR.MINOR.PATCH:');
Object.entries(semverExplained['MAJOR.MINOR.PATCH']).forEach(([part, desc]) => {
  console.log(`  ${part}: ${desc}`);
});
console.log('\n版本符号:');
Object.entries(semverExplained['版本符号']).forEach(([symbol, desc]) => {
  console.log(`  ${symbol}: ${desc}`);
});

// 4. 依赖类型
const dependencyTypes = {
  dependencies: {
    说明: '生产环境依赖',
    安装命令: 'npm install package-name',
    示例: 'express, react, vue'
  },
  devDependencies: {
    说明: '开发环境依赖',
    安装命令: 'npm install --save-dev package-name',
    示例: 'eslint, jest, webpack'
  },
  peerDependencies: {
    说明: '同伴依赖，要求宿主环境安装',
    安装命令: '不需要手动安装',
    示例: '插件依赖宿主的核心库'
  },
  optionalDependencies: {
    说明: '可选依赖，安装失败不影响',
    安装命令: 'npm install --save-optional package-name',
    示例: '可选的增强功能'
  }
};

console.log('\n=== 依赖类型 ===');
Object.entries(dependencyTypes).forEach(([type, info]) => {
  console.log(`\n【${type}】`);
  console.log(`  说明: ${info.说明}`);
  console.log(`  安装命令: ${info.安装命令}`);
  console.log(`  示例: ${info.示例}`);
});

// 5. 核心概念解释
const coreConcepts = {
  包_Package: '一组代码的集合，可以被其他项目使用',
  依赖_Dependency: '项目运行所需要的其他包',
  注册表_Registry: '存储包的服务器（如 npmjs.com）',
  锁文件_LockFile: '锁定依赖版本，确保团队一致（package-lock.json/yarn.lock/pnpm-lock.yaml）',
  node_modules: '存放安装的依赖的目录',
  工作区_Workspaces: '管理多个包的 monorepo 功能'
};

console.log('\n=== 核心概念 ===');
Object.entries(coreConcepts).forEach(([term, desc]) => {
  console.log(`  ${term}: ${desc}`);
});

// 6. 包管理器发展历史
const history = [
  '2009年: Node.js 发布',
  '2010年: npm 诞生，成为 Node.js 官方包管理器',
  '2016年: Yarn 发布，解决 npm 的速度和安全问题',
  '2017年: pnpm 出现，通过硬链接节省磁盘空间',
  '2020年: npm 7 发布，支持 workspaces',
  '2022年: pnpm 成为很多大型项目的首选'
];

console.log('\n=== 包管理器发展历史 ===');
history.forEach((event, i) => console.log(`${i + 1}. ${event}`));

// 7. 常用命令对比
const commonCommands = {
  '初始化项目': {
    npm: 'npm init',
    yarn: 'yarn init',
    pnpm: 'pnpm init'
  },
  '安装依赖': {
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
  '运行脚本': {
    npm: 'npm run <script>',
    yarn: 'yarn <script>',
    pnpm: 'pnpm <script>'
  }
};

console.log('\n=== 常用命令对比 ===');
console.log('操作            npm                yarn              pnpm');
Object.entries(commonCommands).forEach(([action, cmds]) => {
  console.log(`${action.padEnd(12)}  ${cmds.npm.padEnd(18)}  ${cmds.yarn.padEnd(16)}  ${cmds.pnpm}`);
});

// 8. 选择建议
function choosePackageManager(projectType) {
  const recommendations = {
    '小型项目/学习': 'npm（最简单，无需额外安装）',
    '中型项目': 'pnpm（节省空间，速度快）',
    '大型项目/Monorepo': 'pnpm（workspaces 支持好）',
    '追求稳定性': 'npm（生态最成熟）',
    'Facebook生态': 'Yarn（与React配合好）'
  };
  return recommendations[projectType] || '根据具体需求选择';
}

console.log('\n=== 选择建议 ===');
const scenarios = ['小型项目/学习', '中型项目', '大型项目/Monorepo', '追求稳定性', 'Facebook生态'];
scenarios.forEach(s => {
  console.log(`  ${s} → ${choosePackageManager(s)}`);
});
