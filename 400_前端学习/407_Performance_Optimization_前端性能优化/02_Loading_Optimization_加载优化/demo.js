// 前端加载优化示例

// 1. 代码分割示例
function codeSplittingExample() {
  console.log('=== 代码分割示例 ===');
  
  // 动态导入示例
  function loadModule() {
    console.log('开始加载模块...');
    import('./module.js')
      .then(module => {
        console.log('模块加载完成:', module.default());
      })
      .catch(error => {
        console.error('模块加载失败:', error);
      });
  }
  
  // 模拟点击事件触发代码分割
  const loadButton = document.createElement('button');
  loadButton.textContent = '加载模块';
  loadButton.style.padding = '10px';
  loadButton.style.margin = '10px';
  loadButton.addEventListener('click', loadModule);
  document.body.appendChild(loadButton);
  
  console.log('代码分割示例准备就绪，点击按钮加载模块');
}

// 2. 图片懒加载示例
function imageLazyLoadingExample() {
  console.log('\n=== 图片懒加载示例 ===');
  
  // 创建懒加载图片
  for (let i = 0; i < 10; i++) {
    const img = document.createElement('img');
    img.dataset.src = `https://picsum.photos/400/300?random=${i}`;
    img.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="400" height="300"%3E%3C/svg%3E';
    img.className = 'lazy';
    img.style.width = '400px';
    img.style.height = '300px';
    img.style.margin = '10px';
    img.alt = `示例图片 ${i+1}`;
    document.body.appendChild(img);
  }
  
  // 实现图片懒加载
  const images = document.querySelectorAll('img[data-src]');
  
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.remove('lazy');
        imageObserver.unobserve(img);
        console.log('图片懒加载完成:', img.src);
      }
    });
  });
  
  images.forEach(img => {
    imageObserver.observe(img);
  });
  
  console.log('图片懒加载示例准备就绪，滚动页面查看效果');
}

// 3. 资源预加载示例
function resourcePreloadingExample() {
  console.log('\n=== 资源预加载示例 ===');
  
  // 预加载图片
  function preloadImage() {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.href = 'https://picsum.photos/800/600?random=10';
    link.as = 'image';
    document.head.appendChild(link);
    console.log('预加载图片:', link.href);
  }
  
  // 预连接到域名
  function preconnect() {
    const link = document.createElement('link');
    link.rel = 'preconnect';
    link.href = 'https://api.example.com';
    document.head.appendChild(link);
    console.log('预连接到域名:', link.href);
  }
  
  // 预获取资源
  function prefetch() {
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = 'https://picsum.photos/800/600?random=11';
    document.head.appendChild(link);
    console.log('预获取资源:', link.href);
  }
  
  preloadImage();
  preconnect();
  prefetch();
  
  console.log('资源预加载示例完成');
}

// 4. 关键CSS内联示例
function criticalCssExample() {
  console.log('\n=== 关键CSS内联示例 ===');
  
  // 创建示例页面结构
  const container = document.createElement('div');
  container.innerHTML = `
    <div class="header">
      <h1>关键CSS内联示例</h1>
    </div>
    <div class="content">
      <p>这是一个示例页面，展示关键CSS内联的效果。</p>
      <p>关键CSS已经内联到HTML中，非关键CSS将异步加载。</p>
    </div>
    <div class="footer">
      <p>页脚内容</p>
    </div>
  `;
  document.body.appendChild(container);
  
  // 模拟异步加载非关键CSS
  function loadNonCriticalCss() {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'data:text/css, .footer { background-color: #f0f0f0; padding: 20px; }';
    link.media = 'print';
    link.onload = function() {
      this.media = 'all';
      console.log('非关键CSS加载完成');
    };
    document.head.appendChild(link);
  }
  
  // 添加内联关键CSS
  const style = document.createElement('style');
  style.textContent = `
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
    }
    .header {
      background-color: #333;
      color: white;
      padding: 20px;
    }
    .content {
      padding: 20px;
    }
  `;
  document.head.appendChild(style);
  
  // 异步加载非关键CSS
  loadNonCriticalCss();
  
  console.log('关键CSS内联示例完成');
}

// 5. 资源加载优先级示例
function resourcePriorityExample() {
  console.log('\n=== 资源加载优先级示例 ===');
  
  // 创建示例脚本标签
  const criticalScript = document.createElement('script');
  criticalScript.textContent = 'console.log("关键脚本执行");';
  document.head.appendChild(criticalScript);
  
  // 异步加载非关键脚本
  const asyncScript = document.createElement('script');
  asyncScript.src = 'data:text/javascript,console.log("异步脚本执行");';
  asyncScript.async = true;
  document.head.appendChild(asyncScript);
  
  // 延迟加载非关键脚本
  const deferScript = document.createElement('script');
  deferScript.src = 'data:text/javascript,console.log("延迟脚本执行");';
  deferScript.defer = true;
  document.head.appendChild(deferScript);
  
  console.log('资源加载优先级示例完成');
  console.log('执行顺序：关键脚本 -> HTML解析 -> 延迟脚本 -> 异步脚本');
}

// 6. 缓存策略示例
function cachingStrategyExample() {
  console.log('\n=== 缓存策略示例 ===');
  
  // 模拟缓存请求结果
  const cache = new Map();
  
  function fetchWithCache(url) {
    if (cache.has(url)) {
      console.log('从缓存获取数据:', url);
      return Promise.resolve(cache.get(url));
    }
    
    console.log('从网络获取数据:', url);
    // 模拟网络请求
    return new Promise((resolve) => {
      setTimeout(() => {
        const data = { timestamp: Date.now() };
        cache.set(url, data);
        resolve(data);
      }, 1000);
    });
  }
  
  // 测试缓存
  fetchWithCache('/api/data1').then(data => {
    console.log('数据1:', data);
    // 第二次调用会从缓存获取
    fetchWithCache('/api/data1').then(data => {
      console.log('数据1（从缓存）:', data);
    });
  });
  
  fetchWithCache('/api/data2').then(data => {
    console.log('数据2:', data);
  });
  
  console.log('缓存策略示例完成');
}

// 7. 网络请求优化示例
function networkOptimizationExample() {
  console.log('\n=== 网络请求优化示例 ===');
  
  // 优化前：多个独立请求
  function multipleRequests() {
    console.log('多个独立请求:');
    const start = Date.now();
    
    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(data => {
        console.log('数据1:', data);
        console.log('请求1耗时:', Date.now() - start, 'ms');
      });
    
    fetch('https://jsonplaceholder.typicode.com/todos/2')
      .then(response => response.json())
      .then(data => {
        console.log('数据2:', data);
        console.log('请求2耗时:', Date.now() - start, 'ms');
      });
    
    fetch('https://jsonplaceholder.typicode.com/todos/3')
      .then(response => response.json())
      .then(data => {
        console.log('数据3:', data);
        console.log('请求3耗时:', Date.now() - start, 'ms');
      });
  }
  
  // 优化后：并行请求
  function parallelRequests() {
    console.log('并行请求:');
    const start = Date.now();
    
    Promise.all([
      fetch('https://jsonplaceholder.typicode.com/todos/4').then(response => response.json()),
      fetch('https://jsonplaceholder.typicode.com/todos/5').then(response => response.json()),
      fetch('https://jsonplaceholder.typicode.com/todos/6').then(response => response.json())
    ]).then(([data1, data2, data3]) => {
      console.log('数据4:', data1);
      console.log('数据5:', data2);
      console.log('数据6:', data3);
      console.log('并行请求总耗时:', Date.now() - start, 'ms');
    });
  }
  
  multipleRequests();
  
  // 延迟执行并行请求
  setTimeout(parallelRequests, 2000);
  
  console.log('网络请求优化示例完成');
}

// 8. 构建工具优化示例
function buildToolOptimizationExample() {
  console.log('\n=== 构建工具优化示例 ===');
  
  console.log('Webpack优化配置示例:');
  console.log(`
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendors: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    },
    runtimeChunk: 'single'
  }
};
  `);
  
  console.log('Vite优化配置示例:');
  console.log(`
// vite.config.js
export default {
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          router: ['react-router-dom']
        }
      }
    }
  }
};
  `);
  
  console.log('构建工具优化示例完成');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端加载优化示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  codeSplittingExample();
  imageLazyLoadingExample();
  resourcePreloadingExample();
  criticalCssExample();
  resourcePriorityExample();
  cachingStrategyExample();
  networkOptimizationExample();
  buildToolOptimizationExample();
  
  // 创建模块文件
  const moduleScript = document.createElement('script');
  moduleScript.type = 'module';
  moduleScript.textContent = `
export default function() {
  return '模块加载成功！';
}
  `;
  moduleScript.id = 'module.js';
  document.head.appendChild(moduleScript);
  
  console.log('前端加载优化示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}