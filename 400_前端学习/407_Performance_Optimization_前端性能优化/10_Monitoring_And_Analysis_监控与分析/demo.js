// 前端监控与分析示例

// 1. 性能指标监控示例
function performanceMetricsExample() {
  console.log('=== 性能指标监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'performance-metrics';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>性能指标监控示例</h2>
    <p>性能指标监控可以帮助我们了解页面的加载性能和用户体验。</p>
    
    <div class="metrics-container">
      <button id="metrics-btn">测试性能指标</button>
      <div id="metrics-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .performance-metrics {
      font-family: Arial, sans-serif;
    }
    
    .metrics-container {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    #metrics-btn {
      padding: 8px 16px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #metrics-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试性能指标
  const metricsBtn = document.getElementById('metrics-btn');
  const metricsResult = document.getElementById('metrics-result');
  
  metricsBtn.addEventListener('click', () => {
    console.log('测试性能指标');
    metricsResult.innerHTML = '<p>正在收集性能指标...</p>';
    
    if (window.performance) {
      // 获取导航时间
      const navigationTiming = performance.getEntriesByType('navigation')[0];
      
      if (navigationTiming) {
        const metrics = {
          'DNS解析时间': (navigationTiming.domainLookupEnd - navigationTiming.domainLookupStart).toFixed(2) + 'ms',
          'TCP连接时间': (navigationTiming.connectEnd - navigationTiming.connectStart).toFixed(2) + 'ms',
          '首字节时间': (navigationTiming.responseStart - navigationTiming.requestStart).toFixed(2) + 'ms',
          '内容加载时间': (navigationTiming.responseEnd - navigationTiming.responseStart).toFixed(2) + 'ms',
          'DOM加载时间': (navigationTiming.domContentLoadedEventEnd - navigationTiming.navigationStart).toFixed(2) + 'ms',
          '页面加载时间': (navigationTiming.loadEventEnd - navigationTiming.navigationStart).toFixed(2) + 'ms'
        };
        
        let html = '<h3>页面加载性能指标：</h3><ul>';
        for (const [key, value] of Object.entries(metrics)) {
          html += `<li>${key}: ${value}</li>`;
        }
        html += '</ul>';
        
        metricsResult.innerHTML = html;
        console.log('性能指标测试：', metrics);
      } else {
        metricsResult.innerHTML = '<p>无法获取导航时间数据</p>';
      }
    } else {
      metricsResult.innerHTML = '<p>浏览器不支持Performance API</p>';
    }
  });
  
  console.log('性能指标监控示例准备就绪');
  console.log('点击按钮测试性能指标');
}

// 2. 核心Web指标监控示例
function coreWebVitalsExample() {
  console.log('\n=== 核心Web指标监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'core-web-vitals';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>核心Web指标监控示例</h2>
    <p>核心Web指标是衡量用户体验的重要指标，包括LCP、FID和CLS。</p>
    
    <div class="vitals-container">
      <h3>核心Web指标</h3>
      <ul>
        <li><strong>LCP (Largest Contentful Paint)</strong>：最大内容绘制，衡量页面加载速度</li>
        <li><strong>FID (First Input Delay)</strong>：首次输入延迟，衡量页面交互性</li>
        <li><strong>CLS (Cumulative Layout Shift)</strong>：累积布局偏移，衡量页面稳定性</li>
      </ul>
      <div id="vitals-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .core-web-vitals {
      font-family: Arial, sans-serif;
    }
    
    .vitals-container {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .vitals-container h3 {
      margin-top: 0;
      color: #3498db;
    }
  `;
  document.head.appendChild(style);
  
  // 监控核心Web指标
  const vitalsResult = document.getElementById('vitals-result');
  
  // 监控LCP
  if ('PerformanceObserver' in window) {
    new PerformanceObserver((entryList) => {
      const entries = entryList.getEntries();
      const lastEntry = entries[entries.length - 1];
      console.log('LCP:', lastEntry.startTime);
      vitalsResult.innerHTML += `<p>LCP: ${lastEntry.startTime.toFixed(2)}ms</p>`;
    }).observe({ type: 'largest-contentful-paint', buffered: true });
    
    // 监控FID
    new PerformanceObserver((entryList) => {
      const entries = entryList.getEntries();
      entries.forEach((entry) => {
        console.log('FID:', entry.processingStart - entry.startTime);
        vitalsResult.innerHTML += `<p>FID: ${(entry.processingStart - entry.startTime).toFixed(2)}ms</p>`;
      });
    }).observe({ type: 'first-input', buffered: true });
    
    // 监控CLS
    new PerformanceObserver((entryList) => {
      const entries = entryList.getEntries();
      entries.forEach((entry) => {
        console.log('CLS:', entry.value);
        vitalsResult.innerHTML += `<p>CLS: ${entry.value.toFixed(4)}</p>`;
      });
    }).observe({ type: 'layout-shift', buffered: true });
  }
  
  console.log('核心Web指标监控示例准备就绪');
  console.log('页面加载完成后会显示核心Web指标');
}

// 3. 错误监控示例
function errorMonitoringExample() {
  console.log('\n=== 错误监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'error-monitoring';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>错误监控示例</h2>
    <p>错误监控可以帮助我们捕获和分析JavaScript错误，及时发现问题。</p>
    
    <div class="error-container">
      <button id="error-btn">触发错误</button>
      <button id="promise-error-btn">触发Promise错误</button>
      <div id="error-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .error-monitoring {
      font-family: Arial, sans-serif;
    }
    
    .error-container {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    button {
      padding: 8px 16px;
      margin: 5px 5px 5px 0;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    button:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试错误监控
  const errorBtn = document.getElementById('error-btn');
  const promiseErrorBtn = document.getElementById('promise-error-btn');
  const errorResult = document.getElementById('error-result');
  
  // 监控JavaScript错误
  window.addEventListener('error', function(event) {
    console.error('JavaScript错误:', event.error);
    console.error('错误位置:', event.filename, ':', event.lineno, ':', event.colno);
    
    errorResult.innerHTML += `
      <p><strong>JavaScript错误:</strong> ${event.error.message}</p>
      <p><strong>错误位置:</strong> ${event.filename}:${event.lineno}:${event.colno}</p>
    `;
  });
  
  // 监控未捕获的Promise拒绝
  window.addEventListener('unhandledrejection', function(event) {
    console.error('未捕获的Promise拒绝:', event.reason);
    
    errorResult.innerHTML += `
      <p><strong>Promise错误:</strong> ${event.reason.message || String(event.reason)}</p>
    `;
  });
  
  // 触发错误
  errorBtn.addEventListener('click', function() {
    console.log('触发JavaScript错误');
    // 故意触发错误
    nonExistentFunction();
  });
  
  // 触发Promise错误
  promiseErrorBtn.addEventListener('click', function() {
    console.log('触发Promise错误');
    // 故意触发Promise错误
    new Promise((resolve, reject) => {
      reject(new Error('Promise rejection error'));
    });
  });
  
  console.log('错误监控示例准备就绪');
  console.log('点击按钮触发错误，查看错误监控效果');
}

// 4. 用户行为监控示例
function userBehaviorMonitoringExample() {
  console.log('\n=== 用户行为监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'user-behavior';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>用户行为监控示例</h2>
    <p>用户行为监控可以帮助我们了解用户的使用习惯和行为模式。</p>
    
    <div class="behavior-container">
      <h3>点击测试</h3>
      <button class="test-btn" data-test="button1">按钮1</button>
      <button class="test-btn" data-test="button2">按钮2</button>
      <button class="test-btn" data-test="button3">按钮3</button>
      
      <h3 style="margin-top: 20px;">输入测试</h3>
      <input type="text" class="test-input" placeholder="输入测试" data-test="input1">
      
      <div id="behavior-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .user-behavior {
      font-family: Arial, sans-serif;
    }
    
    .behavior-container {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .behavior-container h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    button {
      padding: 8px 16px;
      margin: 5px 5px 5px 0;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    button:hover {
      background-color: #2980b9;
    }
    
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
  `;
  document.head.appendChild(style);
  
  // 测试用户行为监控
  const behaviorResult = document.getElementById('behavior-result');
  
  // 监控点击事件
  document.addEventListener('click', function(event) {
    if (event.target.classList.contains('test-btn')) {
      const testId = event.target.getAttribute('data-test');
      console.log('用户点击:', testId);
      
      behaviorResult.innerHTML += `<p>用户点击: ${testId}</p>`;
    }
  });
  
  // 监控输入事件
  document.addEventListener('input', function(event) {
    if (event.target.classList.contains('test-input')) {
      const testId = event.target.getAttribute('data-test');
      console.log('用户输入:', testId, event.target.value);
      
      behaviorResult.innerHTML += `<p>用户输入 [${testId}]: ${event.target.value}</p>`;
    }
  });
  
  // 监控页面停留时间
  let pageLoadTime = Date.now();
  
  window.addEventListener('beforeunload', function() {
    const stayTime = Date.now() - pageLoadTime;
    console.log('页面停留时间:', stayTime, 'ms');
    
    // 发送停留时间数据到监控平台
    // fetch('/api/staytime', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify({
    //     url: window.location.href,
    //     stayTime: stayTime
    //   })
    // });
  });
  
  console.log('用户行为监控示例准备就绪');
  console.log('点击按钮或输入文本，查看用户行为监控效果');
}

// 5. 网络请求监控示例
function networkMonitoringExample() {
  console.log('\n=== 网络请求监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'network-monitoring';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>网络请求监控示例</h2>
    <p>网络请求监控可以帮助我们了解网络请求的性能和状态。</p>
    
    <div class="network-container">
      <button id="network-btn">测试网络请求</button>
      <div id="network-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .network-monitoring {
      font-family: Arial, sans-serif;
    }
    
    .network-container {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    #network-btn {
      padding: 8px 16px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #network-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试网络请求监控
  const networkBtn = document.getElementById('network-btn');
  const networkResult = document.getElementById('network-result');
  
  // 监控网络请求
  if ('performance' in window && 'getEntries' in performance) {
    networkBtn.addEventListener('click', function() {
      console.log('测试网络请求监控');
      networkResult.innerHTML = '<p>正在发送网络请求...</p>';
      
      // 清除之前的性能条目
      if (performance.clearResourceTimings) {
        performance.clearResourceTimings();
      }
      
      // 发送测试请求
      fetch('https://jsonplaceholder.typicode.com/todos/1')
        .then(response => response.json())
        .then(data => {
          networkResult.innerHTML = `<p>网络请求成功: ${JSON.stringify(data)}</p>`;
          
          // 分析网络请求
          const resourceEntries = performance.getEntriesByType('resource');
          const networkEntries = resourceEntries.filter(entry => entry.initiatorType === 'fetch');
          
          if (networkEntries.length > 0) {
            const entry = networkEntries[networkEntries.length - 1];
            networkResult.innerHTML += `
              <p><strong>请求URL:</strong> ${entry.name}</p>
              <p><strong>请求时间:</strong> ${entry.duration.toFixed(2)}ms</p>
              <p><strong>开始时间:</strong> ${entry.startTime.toFixed(2)}ms</p>
              <p><strong>响应时间:</strong> ${(entry.responseEnd - entry.requestStart).toFixed(2)}ms</p>
            `;
            console.log('网络请求监控:', entry);
          }
        })
        .catch(error => {
          networkResult.innerHTML = `<p>网络请求失败: ${error.message}</p>`;
          console.error('网络请求失败:', error);
        });
    });
  } else {
    networkBtn.addEventListener('click', function() {
      networkResult.innerHTML = '<p>浏览器不支持Performance API</p>';
    });
  }
  
  console.log('网络请求监控示例准备就绪');
  console.log('点击按钮测试网络请求监控');
}

// 6. 性能分析工具示例
function performanceAnalysisToolsExample() {
  console.log('\n=== 性能分析工具示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'performance-tools';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>性能分析工具示例</h2>
    <p>性能分析工具可以帮助我们分析页面性能，找出性能瓶颈。</p>
    
    <div class="tools-container">
      <div class="tool">
        <h3>Chrome DevTools</h3>
        <p>提供网络、性能、内存等分析工具</p>
        <ul>
          <li>Network面板：分析网络请求</li>
          <li>Performance面板：分析页面性能</li>
          <li>Memory面板：分析内存使用</li>
          <li>Application面板：分析存储使用</li>
        </ul>
      </div>
      
      <div class="tool">
        <h3>Lighthouse</h3>
        <p>分析页面性能，提供优化建议</p>
        <ul>
          <li>性能评分</li>
          <li>可访问性评分</li>
          <li>最佳实践评分</li>
          <li>SEO评分</li>
        </ul>
      </div>
      
      <div class="tool">
        <h3>WebPageTest</h3>
        <p>提供详细的性能测试报告</p>
        <ul>
          <li>首次内容绘制</li>
          <li>最大内容绘制</li>
          <li>可交互时间</li>
          <li>累积布局偏移</li>
        </ul>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .performance-tools {
      font-family: Arial, sans-serif;
    }
    
    .tools-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .tool {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .tool h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .tool ul {
      margin-bottom: 0;
    }
  `;
  document.head.appendChild(style);
  
  console.log('性能分析工具示例准备就绪');
  console.log('查看页面中的性能分析工具示例');
}

// 7. 监控平台示例
function monitoringPlatformsExample() {
  console.log('\n=== 监控平台示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'monitoring-platforms';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>监控平台示例</h2>
    <p>监控平台可以帮助我们实时监控应用性能，及时发现问题。</p>
    
    <div class="platforms-container">
      <div class="platform">
        <h3>Sentry</h3>
        <p>专注于错误监控和异常追踪</p>
        <code>// 安装
npm install @sentry/browser

// 初始化
Sentry.init({
  dsn: 'YOUR_DSN'
});

// 捕获错误
try {
  // 代码
} catch (error) {
  Sentry.captureException(error);
}
</code>
      </div>
      
      <div class="platform">
        <h3>New Relic</h3>
        <p>提供应用性能监控、错误监控等</p>
        <code>// 安装
npm install newrelic

// 配置
// newrelic.js

// 引入
require('newrelic');
</code>
      </div>
      
      <div class="platform">
        <h3>LogRocket</h3>
        <p>录制用户会话，分析用户行为</p>
        <code>// 安装
npm install logrocket

// 初始化
LogRocket.init('YOUR_APP_ID');
</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .monitoring-platforms {
      font-family: Arial, sans-serif;
    }
    
    .platforms-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .platform {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .platform h3 {
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
  
  console.log('监控平台示例准备就绪');
  console.log('查看页面中的监控平台示例');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端监控与分析示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  performanceMetricsExample();
  coreWebVitalsExample();
  errorMonitoringExample();
  userBehaviorMonitoringExample();
  networkMonitoringExample();
  performanceAnalysisToolsExample();
  monitoringPlatformsExample();
  
  console.log('前端监控与分析示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}