// 发布包示例代码

// 1. 发布前检查清单
const prePublishChecklist = [
  '✅ package.json 完整',
  '   name, version, description, author, license',
  '   main/module/types 入口正确',
  '   scripts (build, test)',
  '   dependencies 正确',
  '',
  '✅ 代码已构建',
  '   dist/ 目录存在',
  '   构建产物正确',
  '',
  '✅ 测试通过',
  '   npm test 全部通过',
  '',
  '✅ README.md 完善',
  '   安装说明',
  '   使用示例',
  '   API 文档',
  '',
  '✅ 许可证文件',
  '   LICENSE 文件存在',
  '',
  '✅ .npmignore 配置',
  '   不发布不必要的文件',
  '',
  '✅ Git 仓库干净',
  '   没有未提交的修改'
];

console.log('=== 发布前检查清单 ===');
prePublishChecklist.forEach(item => console.log(`  ${item}`));

// 2. 完整的发布流程
const publishFlow = [
  {
    step: '1. 注册 npm 账号',
    command: '访问 https://www.npmjs.com/signup'
  },
  {
    step: '2. 登录 npm',
    command: 'npm login'
  },
  {
    step: '3. 验证登录',
    command: 'npm whoami'
  },
  {
    step: '4. 检查包名是否可用',
    command: 'npm view <package-name>'
  },
  {
    step: '5. 初始化 Git（如果还没有）',
    command: 'git init && git add . && git commit -m "Initial commit"'
  },
  {
    step: '6. 更新版本',
    command: 'npm version patch|minor|major'
  },
  {
    step: '7. 发布包',
    command: 'npm publish'
  },
  {
    step: '8. 验证发布',
    command: 'npm view <package-name>'
  }
];

console.log('\n=== 完整发布流程 ===');
publishFlow.forEach(item => {
  console.log(`\n${item.step}`);
  console.log(`   ${item.command}`);
});

// 3. 版本号管理
const versionManagement = {
  '首次发布': '1.0.0',
  'Bug 修复': 'npm version patch  (1.0.0 → 1.0.1)',
  '新功能（向后兼容）': 'npm version minor  (1.0.0 → 1.1.0)',
  '破坏性更新': 'npm version major  (1.0.0 → 2.0.0)',
  '预发布版本': 'npm version prerelease --preid=beta  (1.0.0 → 1.0.1-beta.0)'
};

console.log('\n=== 版本号管理 ===');
Object.entries(versionManagement).forEach(([type, cmd]) => {
  console.log(`  ${type.padEnd(25)}: ${cmd}`);
});

// 4. package.json 发布配置
const publishConfig = {
  name: '@my-scope/my-package',
  version: '1.0.0',
  description: 'My awesome package',
  main: 'dist/index.js',
  module: 'dist/index.esm.js',
  types: 'dist/index.d.ts',
  files: ['dist', 'README.md', 'LICENSE'],
  scripts: {
    build: 'rollup -c',
    test: 'jest',
    prepublishOnly: 'npm run build && npm test',
    version: 'npm run build && git add -A dist',
    postversion: 'git push && git push --tags'
  },
  publishConfig: {
    access: 'public',
    registry: 'https://registry.npmjs.org/'
  },
  repository: {
    type: 'git',
    url: 'https://github.com/my-scope/my-package.git'
  },
  keywords: ['awesome', 'package', 'utility'],
  author: 'Your Name',
  license: 'MIT'
};

console.log('\n=== 发布用 package.json ===');
console.log(JSON.stringify(publishConfig, null, 2));

// 5. 发布标签（Tags）
const publishTags = {
  'latest': {
    说明: '默认标签，稳定版',
    命令: 'npm publish 或 npm publish --tag latest',
    安装: 'npm install <package>'
  },
  'beta': {
    说明: '测试版',
    命令: 'npm publish --tag beta',
    安装: 'npm install <package>@beta'
  },
  'next': {
    说明: '下一个主要版本',
    命令: 'npm publish --tag next',
    安装: 'npm install <package>@next'
  },
  'canary': {
    说明: '每日构建版',
    命令: 'npm publish --tag canary',
    安装: 'npm install <package>@canary'
  },
  'dev': {
    说明: '开发版',
    命令: 'npm publish --tag dev',
    安装: 'npm install <package>@dev'
  }
};

console.log('\n=== 发布标签 ===');
Object.entries(publishTags).forEach(([tag, info]) => {
  console.log(`\n【${tag}】`);
  console.log(`  说明: ${info.说明}`);
  console.log(`  发布: ${info.命令}`);
  console.log(`  安装: ${info.安装}`);
});

// 6. Scoped Packages
const scopedPackages = {
  什么是: '带命名空间的包，如 @vue/reactivity',
  创建: 'npm init --scope=my-scope',
  发布: 'npm publish --access=public',
  安装: 'npm install @my-scope/my-package',
  优势: [
    '避免命名冲突',
    '组织内部包管理',
    '清晰的包归属'
  ]
};

console.log('\n=== Scoped Packages ===');
console.log('什么是:', scopedPackages.什么是);
console.log('创建:', scopedPackages.创建);
console.log('发布:', scopedPackages.发布);
console.log('安装:', scopedPackages.安装);
console.log('优势:', scopedPackages.优势);

// 7. 发布后的维护
const postPublishMaintenance = [
  {
    任务: '处理 Issue',
    说明: '及时回复和修复 bug'
  },
  {
    任务: '发布安全更新',
    说明: '定期运行 npm audit，及时修复'
  },
  {
    任务: '更新文档',
    说明: '保持 README 和 API 文档更新'
  },
  {
    任务: '版本回退',
    说明: 'npm deprecate <pkg>@<version> "message"'
  },
  {
    任务: '弃用包',
    说明: 'npm deprecate <pkg> "This package is deprecated"'
  }
];

console.log('\n=== 发布后维护 ===');
postPublishMaintenance.forEach(item => {
  console.log(`\n【${item.任务}】`);
  console.log(`  ${item.说明}`);
});

// 8. README 模板
const readmeTemplate = `
# my-package

> A brief description of what this package does

## Installation

\`\`\`bash
npm install my-package
# or
yarn add my-package
# or
pnpm add my-package
\`\`\`

## Usage

\`\`\`javascript
import { myFunction } from 'my-package';

const result = myFunction('hello');
console.log(result);
\`\`\`

## API

### myFunction(input)

- \`input\` (string): Input string
- Returns: string

## License

MIT © Your Name
`;

console.log('\n=== README 模板 ===');
console.log(readmeTemplate);

// 9. 常见问题
const faq = [
  {
    Q: '403 Forbidden 错误？',
    A: [
      '包名已被占用',
      '未登录或登录过期 (npm login)',
      'scope 包需要 --access=public'
    ]
  },
  {
    Q: '如何修改已发布的版本？',
    A: '不能修改，只能发布新版本！'
  },
  {
    Q: '如何删除已发布的包？',
    A: [
      '发布 24 小时内可以 unpublish',
      '超过 24 小时只能 deprecate',
      'npm unpublish <pkg> --force'
    ]
  }
];

console.log('\n=== 常见问题 ===');
faq.forEach(item => {
  console.log(`\nQ: ${item.Q}`);
  console.log('A:');
  if (Array.isArray(item.A)) {
    item.A.forEach(a => console.log(`   - ${a}`));
  } else {
    console.log(`   ${item.A}`);
  }
});
