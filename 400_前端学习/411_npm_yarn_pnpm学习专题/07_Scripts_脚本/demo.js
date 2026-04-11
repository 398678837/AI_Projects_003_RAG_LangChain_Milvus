// npm scripts 示例代码

// 1. 基本 scripts 示例
const basicScripts = {
  name: 'my-project',
  scripts: {
    start: 'node index.js',
    dev: 'nodemon index.js',
    build: 'webpack --mode production',
    test: 'jest',
    lint: 'eslint src',
    format: 'prettier --write src',
    clean: 'rm -rf dist',
    prepare: 'npm run build'
  }
};

console.log('=== 基本 scripts 示例 ===');
console.log(JSON.stringify(basicScripts, null, 2));
console.log('\n运行方式:');
console.log('  npm start');
console.log('  npm run dev');
console.log('  npm run build');

// 2. 脚本生命周期
const scriptLifecycle = {
  'prepublish': '发布前运行',
  'prepare': '打包前、安装后运行',
  'prepublishOnly': 'publish前运行',
  'prepack': '打包前运行',
  'postpack': '打包后运行',
  'publish': '发布',
  'postpublish': '发布后运行',
  'preinstall': '安装前',
  'install': '安装',
  'postinstall': '安装后',
  'preuninstall': '卸载前',
  'uninstall': '卸载',
  'postuninstall': '卸载后',
  'preversion': '版本前',
  'version': '版本',
  'postversion': '版本后',
  'pretest': '测试前',
  'test': '测试',
  'posttest': '测试后',
  'prestop': '停止前',
  'stop': '停止',
  'poststop': '停止后',
  'prestart': '启动前',
  'start': '启动',
  'poststart': '启动后'
};

console.log('\n=== 脚本生命周期 ===');
console.log('自定义脚本也有 pre 和 post:');
console.log('  "prebuild": "...", "build": "...", "postbuild": "..."');

// 3. pre/post 示例
const prePostExample = {
  scripts: {
    prebuild: 'npm run clean',
    build: 'webpack',
    postbuild: 'echo "Build complete!"',
    clean: 'rm -rf dist',
    pretest: 'npm run lint',
    test: 'jest',
    posttest: 'echo "Tests done!"'
  }
};

console.log('\n=== pre/post 示例 ===');
console.log(JSON.stringify(prePostExample, null, 2));

// 4. 串行和并行执行
const executionScripts = {
  scripts: {
    'build:css': 'sass src/css dist/css',
    'build:js': 'webpack',
    'build:images': 'imagemin src/images dist/images',
    
    'build:serial': 'npm run build:css && npm run build:js && npm run build:images',
    'build:parallel': 'npm-run-all -p build:css build:js build:images',
    
    'dev': 'npm-run-all -p watch:*',
    'watch:css': 'sass --watch src/css dist/css',
    'watch:js': 'webpack --watch'
  }
};

console.log('\n=== 串行和并行执行 ===');
console.log('串行: &&');
console.log('并行: & (Unix) / start (Windows)');
console.log('推荐工具: npm-run-all, concurrently');
console.log('\n示例:');
console.log('  "build:serial": "npm run build:css && npm run build:js"');
console.log('  "build:parallel": "npm-run-all -p build:*"');

// 5. 传递参数
const passArgsExample = {
  scripts: {
    test: 'jest',
    lint: 'eslint'
  }
};

console.log('\n=== 传递参数 ===');
console.log('使用 -- 传递参数:');
console.log('  npm test -- --watch');
console.log('  npm run lint -- src/utils.js --fix');
console.log('\n等价于:');
console.log('  jest --watch');
console.log('  eslint src/utils.js --fix');

// 6. 使用环境变量
const envScripts = {
  scripts: {
    'dev': 'NODE_ENV=development nodemon',
    'build': 'NODE_ENV=production webpack',
    'start': 'cross-env NODE_ENV=production node index.js'
  }
};

console.log('\n=== 环境变量 ===');
console.log('Unix:');
console.log('  "dev": "NODE_ENV=development nodemon"');
console.log('\n跨平台 (推荐 cross-env):');
console.log('  "start": "cross-env NODE_ENV=production node index.js"');
console.log('\n安装: npm install -D cross-env');

// 7. 常用工具包
const scriptTools = {
  'npm-run-all': '并行/串行运行多个脚本',
  'concurrently': '同时运行多个命令',
  'cross-env': '跨平台设置环境变量',
  'rimraf': '跨平台删除文件/目录',
  'ncp': '跨平台复制',
  'wait-on': '等待资源可用',
  'nodemon': '监控文件变化自动重启'
};

console.log('\n=== 常用脚本工具 ===');
Object.entries(scriptTools).forEach(([tool, desc]) => {
  console.log(`  ${tool.padEnd(15)}: ${desc}`);
});

// 8. 完整的项目 scripts 示例
const completeScripts = {
  name: 'my-full-stack-app',
  scripts: {
    'clean': 'rimraf dist .next',
    'prebuild': 'npm run clean',
    'build': 'npm-run-all build:*',
    'build:client': 'webpack --mode production',
    'build:server': 'tsc -p tsconfig.server.json',
    
    'dev': 'npm-run-all -p dev:*',
    'dev:client': 'webpack serve --mode development',
    'dev:server': 'nodemon src/server/index.ts',
    
    'test': 'npm-run-all test:*',
    'test:unit': 'jest',
    'test:e2e': 'cypress run',
    
    'lint': 'eslint src --ext .ts,.tsx',
    'lint:fix': 'eslint src --ext .ts,.tsx --fix',
    'format': 'prettier --write "src/**/*.{ts,tsx,css,json}"',
    
    'typecheck': 'tsc --noEmit',
    
    'precommit': 'npm-run-all lint typecheck test:unit',
    'prepublishOnly': 'npm run build',
    
    'docker:build': 'docker build -t myapp .',
    'docker:run': 'docker run -p 3000:3000 myapp'
  }
};

console.log('\n=== 完整项目 scripts 示例 ===');
console.log(JSON.stringify(completeScripts, null, 2));

// 9. 脚本最佳实践
const bestPractices = [
  '✅ 使用有意义的脚本名称',
  '✅ 组合小脚本形成复杂流程',
  '✅ 使用 pre/post 钩子',
  '✅ 使用 cross-env 跨平台',
  '✅ 使用 rimraf 替代 rm -rf',
  '✅ 文档化复杂脚本',
  '✅ 避免过长的单行命令',
  '✅ 使用 npm-run-all 管理多脚本'
];

console.log('\n=== 脚本最佳实践 ===');
bestPractices.forEach(p => console.log(`  ${p}`));
