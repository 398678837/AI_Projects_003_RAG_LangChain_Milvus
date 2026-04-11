// 前端打包优化示例

// 1. 代码分割示例
function codeSplittingExample() {
  console.log('=== 代码分割示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'code-splitting';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>代码分割示例</h2>
    <p>代码分割可以将代码分割成多个小文件，实现按需加载，提高页面加载速度。</p>
    
    <div class="splitting-types">
      <div class="splitting-type">
        <h3>动态导入</h3>
        <p>使用动态导入实现代码分割</p>
        <button id="dynamic-import-btn">动态导入模块</button>
        <div id="dynamic-import-result" style="margin-top: 10px;"></div>
      </div>
      
      <div class="splitting-type">
        <h3>路由分割</h3>
        <p>根据路由分割代码</p>
        <code>const LazyComponent = React.lazy(() => import('./LazyComponent'));</code>
      </div>
      
      <div class="splitting-type">
        <h3>第三方库分割</h3>
        <p>将第三方库单独打包</p>
        <code>// Webpack配置
splitChunks: {
  chunks: 'all',
  cacheGroups: {
    vendor: {
      name: 'vendor',
      test: /[\\/]node_modules[\\/]/,
      chunks: 'all'
    }
  }
}</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .code-splitting {
      font-family: Arial, sans-serif;
    }
    
    .splitting-types {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .splitting-type {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .splitting-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    #dynamic-import-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #dynamic-import-btn:hover {
      background-color: #2980b9;
    }
    
    #dynamic-import-result {
      padding: 10px;
      border: 1px solid #ddd;
      background-color: #f0f0f0;
      margin-top: 10px;
    }
    
    code {
      display: block;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      white-space: pre-wrap;
      margin-top: 10px;
    }
  `;
  document.head.appendChild(style);
  
  // 测试动态导入
  const dynamicImportBtn = document.getElementById('dynamic-import-btn');
  const dynamicImportResult = document.getElementById('dynamic-import-result');
  
  dynamicImportBtn.addEventListener('click', () => {
    console.log('测试动态导入');
    dynamicImportResult.textContent = '正在动态导入模块...';
    
    // 模拟动态导入
    const moduleCode = `
      export default function() {
        return '动态导入模块成功！';
      }
    `;
    
    const blob = new Blob([moduleCode], { type: 'application/javascript' });
    const url = URL.createObjectURL(blob);
    
    import(url)
      .then(module => {
        dynamicImportResult.textContent = module.default();
        console.log('动态导入成功:', module.default());
        URL.revokeObjectURL(url);
      })
      .catch(error => {
        dynamicImportResult.textContent = `导入失败: ${error.message}`;
        console.error('动态导入失败:', error);
      });
  });
  
  console.log('代码分割示例准备就绪');
  console.log('点击按钮测试动态导入');
}

// 2. Tree Shaking示例
function treeShakingExample() {
  console.log('\n=== Tree Shaking示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'tree-shaking';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>Tree Shaking示例</h2>
    <p>Tree Shaking可以移除未使用的代码，减少打包后的文件大小。</p>
    
    <div class="tree-shaking-example">
      <h3>未使用的代码</h3>
      <p>下面的代码中，未使用的函数会被Tree Shaking移除。</p>
      <pre><code>// 模块代码
export function usedFunction() {
  return '这是一个被使用的函数';
}

export function unusedFunction() {
  return '这是一个未被使用的函数';
}

// 导入代码
import { usedFunction } from './module';
console.log(usedFunction());
</code></pre>
      <p>打包后，未使用的函数会被移除，减少文件大小。</p>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .tree-shaking {
      font-family: Arial, sans-serif;
    }
    
    .tree-shaking-example {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
      margin-top: 20px;
    }
    
    .tree-shaking-example h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    pre {
      background-color: #f0f0f0;
      padding: 10px;
      border-radius: 4px;
      overflow-x: auto;
    }
    
    code {
      font-size: 14px;
    }
  `;
  document.head.appendChild(style);
  
  console.log('Tree Shaking示例准备就绪');
  console.log('查看页面中的Tree Shaking示例');
}

// 3. 代码压缩示例
function codeMinificationExample() {
  console.log('\n=== 代码压缩示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'code-minification';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>代码压缩示例</h2>
    <p>代码压缩可以减少文件大小，提高加载速度。</p>
    
    <div class="minification-types">
      <div class="minification-type">
        <h3>JavaScript压缩</h3>
        <div class="code-comparison">
          <div class="code-original">
            <h4>原始代码</h4>
            <pre><code>function calculateSum(a, b) {
  // 计算两个数的和
  return a + b;
}

console.log(calculateSum(1, 2));
</code></pre>
          </div>
          <div class="code-minified">
            <h4>压缩后代码</h4>
            <pre><code>function calculateSum(a,b){return a+b}console.log(calculateSum(1,2))
</code></pre>
          </div>
        </div>
      </div>
      
      <div class="minification-type">
        <h3>CSS压缩</h3>
        <div class="code-comparison">
          <div class="code-original">
            <h4>原始代码</h4>
            <pre><code>.container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
</code></pre>
          </div>
          <div class="code-minified">
            <h4>压缩后代码</h4>
            <pre><code>.container{width:100%;height:100%;margin:0;padding:0}
</code></pre>
          </div>
        </div>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .code-minification {
      font-family: Arial, sans-serif;
    }
    
    .minification-types {
      margin-top: 20px;
    }
    
    .minification-type {
      margin-bottom: 20px;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .minification-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .code-comparison {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 10px;
    }
    
    .code-original,
    .code-minified {
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
      background-color: #f0f0f0;
    }
    
    .code-original h4,
    .code-minified h4 {
      margin-top: 0;
      font-size: 14px;
      color: #666;
    }
    
    pre {
      margin: 10px 0 0 0;
      padding: 10px;
      background-color: #e0e0e0;
      border-radius: 4px;
      overflow-x: auto;
      font-size: 12px;
    }
    
    code {
      font-size: 12px;
    }
  `;
  document.head.appendChild(style);
  
  console.log('代码压缩示例准备就绪');
  console.log('查看页面中的代码压缩示例');
}

// 4. 构建优化示例
function buildOptimizationExample() {
  console.log('\n=== 构建优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'build-optimization';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>构建优化示例</h2>
    <p>构建优化可以提高构建速度，提升开发效率。</p>
    
    <div class="build-optimizations">
      <div class="build-optimization-item">
        <h3>缓存配置</h3>
        <p>使用持久化缓存，提高构建速度</p>
        <code>// Webpack配置
module.exports = {
  cache: {
    type: 'filesystem',
    buildDependencies: {
      config: [__filename]
    }
  }
};
</code>
      </div>
      
      <div class="build-optimization-item">
        <h3>并行构建</h3>
        <p>使用多线程并行构建，提高构建速度</p>
        <code>// Webpack配置
const os = require('os');

module.exports = {
  optimization: {
    minimizer: [
      new TerserPlugin({
        parallel: os.cpus().length - 1
      })
    ]
  }
};
</code>
      </div>
      
      <div class="build-optimization-item">
        <h3>增量构建</h3>
        <p>只构建修改的文件，提高构建速度</p>
        <code>// Vite配置
export default defineConfig({
  server: {
    watch: {
      usePolling: true
    }
  }
});
</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .build-optimization {
      font-family: Arial, sans-serif;
    }
    
    .build-optimizations {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .build-optimization-item {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .build-optimization-item h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    code {
      display: block;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      white-space: pre-wrap;
      margin-top: 10px;
    }
  `;
  document.head.appendChild(style);
  
  console.log('构建优化示例准备就绪');
  console.log('查看页面中的构建优化示例');
}

// 5. 输出优化示例
function outputOptimizationExample() {
  console.log('\n=== 输出优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'output-optimization';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>输出优化示例</h2>
    <p>输出优化可以提高文件加载速度，利用浏览器缓存。</p>
    
    <div class="output-optimizations">
      <div class="output-optimization-item">
        <h3>文件名哈希</h3>
        <p>使用内容哈希命名文件，利用浏览器缓存</p>
        <code>// Webpack配置
output: {
  filename: '[name].[contenthash].js',
  chunkFilename: '[name].[contenthash].chunk.js'
}
</code>
      </div>
      
      <div class="output-optimization-item">
        <h3>输出目录结构</h3>
        <p>优化输出目录结构，便于管理</p>
        <code>// 输出目录结构
dist/
├── assets/
│   ├── images/
│   ├── fonts/
│   └── styles/
├── js/
│   ├── main.5e7f9a.js
│   ├── vendor.8d3f2b.js
│   └── runtime.1a2b3c.js
└── index.html
</code>
      </div>
      
      <div class="output-optimization-item">
        <h3>资源路径</h3>
        <p>配置正确的资源路径，确保资源加载正常</p>
        <code>// Webpack配置
output: {
  publicPath: '/'
}
</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .output-optimization {
      font-family: Arial, sans-serif;
    }
    
    .output-optimizations {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .output-optimization-item {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .output-optimization-item h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    code {
      display: block;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      white-space: pre-wrap;
      margin-top: 10px;
    }
  `;
  document.head.appendChild(style);
  
  console.log('输出优化示例准备就绪');
  console.log('查看页面中的输出优化示例');
}

// 6. 打包分析示例
function bundleAnalysisExample() {
  console.log('\n=== 打包分析示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'bundle-analysis';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>打包分析示例</h2>
    <p>打包分析可以帮助我们了解打包结果，找出性能瓶颈。</p>
    
    <div class="analysis-tools">
      <div class="analysis-tool">
        <h3>Webpack Bundle Analyzer</h3>
        <p>分析Webpack打包结果，生成可视化报告</p>
        <code>// 安装
npm install --save-dev webpack-bundle-analyzer

// 使用
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin()
  ]
};
</code>
      </div>
      
      <div class="analysis-tool">
        <h3>SpeedMeasurePlugin</h3>
        <p>分析Webpack构建速度，找出瓶颈</p>
        <code>// 安装
npm install --save-dev speed-measure-webpack-plugin

// 使用
const SpeedMeasurePlugin = require('speed-measure-webpack-plugin');
const smp = new SpeedMeasurePlugin();

module.exports = smp.wrap({
  // Webpack配置
});
</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .bundle-analysis {
      font-family: Arial, sans-serif;
    }
    
    .analysis-tools {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .analysis-tool {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .analysis-tool h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    code {
      display: block;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      white-space: pre-wrap;
      margin-top: 10px;
    }
  `;
  document.head.appendChild(style);
  
  console.log('打包分析示例准备就绪');
  console.log('查看页面中的打包分析示例');
}

// 7. 打包工具示例
function bundlerExample() {
  console.log('\n=== 打包工具示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'bundler-example';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>打包工具示例</h2>
    <p>不同的打包工具有不同的特点和适用场景。</p>
    
    <div class="bundlers">
      <div class="bundler">
        <h3>Webpack</h3>
        <p>功能强大的打包工具，支持代码分割、Tree Shaking等</p>
        <code>// 基本配置
module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  }
};
</code>
      </div>
      
      <div class="bundler">
        <h3>Vite</h3>
        <p>基于ES模块的构建工具，开发速度快</p>
        <code>// 基本配置
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist'
  }
});
</code>
      </div>
      
      <div class="bundler">
        <h3>Rollup</h3>
        <p>专注于库的打包，Tree Shaking效果好</p>
        <code>// 基本配置
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
};
</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .bundler-example {
      font-family: Arial, sans-serif;
    }
    
    .bundlers {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .bundler {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .bundler h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    code {
      display: block;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      white-space: pre-wrap;
      margin-top: 10px;
    }
  `;
  document.head.appendChild(style);
  
  console.log('打包工具示例准备就绪');
  console.log('查看页面中的打包工具示例');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端打包优化示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  codeSplittingExample();
  treeShakingExample();
  codeMinificationExample();
  buildOptimizationExample();
  outputOptimizationExample();
  bundleAnalysisExample();
  bundlerExample();
  
  console.log('前端打包优化示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}