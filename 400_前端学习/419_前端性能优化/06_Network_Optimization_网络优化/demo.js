// 前端网络优化示例

// 1. 资源提示示例
function resourceHintsExample() {
  console.log('=== 资源提示示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'resource-hints';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>资源提示示例</h2>
    <p>资源提示（Resource Hints）是一种优化技术，用于告诉浏览器哪些资源可能会被需要，从而提前进行相关操作。</p>
    <div class="hint-types">
      <div class="hint-type">
        <h3>preload</h3>
        <p>预加载关键资源，如CSS、JavaScript等。</p>
      </div>
      <div class="hint-type">
        <h3>prefetch</h3>
        <p>预获取可能需要的资源，如后续页面的资源。</p>
      </div>
      <div class="hint-type">
        <h3>preconnect</h3>
        <p>预连接到将要使用的域名，减少DNS解析时间。</p>
      </div>
      <div class="hint-type">
        <h3>dns-prefetch</h3>
        <p>预解析域名，减少DNS解析时间。</p>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .resource-hints {
      font-family: Arial, sans-serif;
    }
    
    .hint-types {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .hint-type {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .hint-type h3 {
      margin-top: 0;
      color: #3498db;
    }
  `;
  document.head.appendChild(style);
  
  // 添加资源提示
  const preloadLink = document.createElement('link');
  preloadLink.rel = 'preload';
  preloadLink.href = 'data:text/css, .preloaded { color: red; }';
  preloadLink.as = 'style';
  document.head.appendChild(preloadLink);
  
  const prefetchLink = document.createElement('link');
  prefetchLink.rel = 'prefetch';
  prefetchLink.href = 'data:text/javascript, console.log("Prefetched script loaded");';
  document.head.appendChild(prefetchLink);
  
  const preconnectLink = document.createElement('link');
  preconnectLink.rel = 'preconnect';
  preconnectLink.href = 'https://api.example.com';
  document.head.appendChild(preconnectLink);
  
  const dnsPrefetchLink = document.createElement('link');
  dnsPrefetchLink.rel = 'dns-prefetch';
  dnsPrefetchLink.href = 'https://cdn.example.com';
  document.head.appendChild(dnsPrefetchLink);
  
  console.log('资源提示示例准备就绪');
  console.log('查看页面中的资源提示类型');
}

// 2. 缓存策略示例
function cachingStrategyExample() {
  console.log('\n=== 缓存策略示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'caching-strategy';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>缓存策略示例</h2>
    <p>缓存策略是提高前端性能的重要手段，包括浏览器缓存、Service Worker缓存和本地存储。</p>
    <div class="cache-types">
      <div class="cache-type">
        <h3>浏览器缓存</h3>
        <p>使用HTTP缓存头控制资源缓存。</p>
        <button class="cache-test-btn" data-type="browser">测试浏览器缓存</button>
      </div>
      <div class="cache-type">
        <h3>本地存储</h3>
        <p>使用localStorage存储数据。</p>
        <button class="cache-test-btn" data-type="local">测试本地存储</button>
      </div>
      <div class="cache-type">
        <h3>Session存储</h3>
        <p>使用sessionStorage存储会话数据。</p>
        <button class="cache-test-btn" data-type="session">测试Session存储</button>
      </div>
    </div>
    <div id="cache-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .caching-strategy {
      font-family: Arial, sans-serif;
    }
    
    .cache-types {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .cache-type {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .cache-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .cache-test-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .cache-test-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试缓存策略
  const resultDiv = document.getElementById('cache-result');
  const buttons = document.querySelectorAll('.cache-test-btn');
  
  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const type = button.getAttribute('data-type');
      resultDiv.innerHTML = '';
      
      if (type === 'browser') {
        // 测试浏览器缓存
        console.log('测试浏览器缓存');
        fetch('data:text/plain,Hello World')
          .then(response => response.text())
          .then(data => {
            resultDiv.innerHTML = `<p>浏览器缓存测试：成功获取数据: ${data}</p>`;
            console.log('浏览器缓存测试：成功获取数据');
          })
          .catch(error => {
            resultDiv.innerHTML = `<p>浏览器缓存测试：错误: ${error.message}</p>`;
            console.error('浏览器缓存测试：错误', error);
          });
      } else if (type === 'local') {
        // 测试本地存储
        console.log('测试本地存储');
        localStorage.setItem('test-key', 'test-value');
        const value = localStorage.getItem('test-key');
        resultDiv.innerHTML = `<p>本地存储测试：存储的值: ${value}</p>`;
        console.log('本地存储测试：存储的值', value);
      } else if (type === 'session') {
        // 测试Session存储
        console.log('测试Session存储');
        sessionStorage.setItem('test-key', 'test-value');
        const value = sessionStorage.getItem('test-key');
        resultDiv.innerHTML = `<p>Session存储测试：存储的值: ${value}</p>`;
        console.log('Session存储测试：存储的值', value);
      }
    });
  });
  
  console.log('缓存策略示例准备就绪');
  console.log('点击按钮测试不同的缓存策略');
}

// 3. 资源压缩示例
function resourceCompressionExample() {
  console.log('\n=== 资源压缩示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'resource-compression';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>资源压缩示例</h2>
    <p>资源压缩是减少网络传输大小的重要手段，包括Gzip和Brotli压缩。</p>
    <div class="compression-types">
      <div class="compression-type">
        <h3>文本压缩</h3>
        <p>压缩HTML、CSS、JavaScript等文本资源。</p>
        <button class="compression-test-btn" data-type="text">测试文本压缩</button>
      </div>
      <div class="compression-type">
        <h3>图片压缩</h3>
        <p>压缩图片资源，减少图片大小。</p>
        <button class="compression-test-btn" data-type="image">测试图片压缩</button>
      </div>
    </div>
    <div id="compression-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .resource-compression {
      font-family: Arial, sans-serif;
    }
    
    .compression-types {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .compression-type {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .compression-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .compression-test-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .compression-test-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试资源压缩
  const resultDiv = document.getElementById('compression-result');
  const buttons = document.querySelectorAll('.compression-test-btn');
  
  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const type = button.getAttribute('data-type');
      resultDiv.innerHTML = '';
      
      if (type === 'text') {
        // 测试文本压缩
        console.log('测试文本压缩');
        const originalText = 'This is a test text for compression. ' + 'It contains multiple repeated words and phrases. '.repeat(10);
        const originalSize = new Blob([originalText]).size;
        
        // 模拟压缩（实际压缩在服务器端进行）
        resultDiv.innerHTML = `
          <p>原始文本大小: ${originalSize} bytes</p>
          <p>压缩后大小: ~${Math.round(originalSize * 0.3)} bytes (模拟Gzip压缩)</p>
          <p>压缩率: ~70%</p>
        `;
        console.log('文本压缩测试：原始大小', originalSize);
      } else if (type === 'image') {
        // 测试图片压缩
        console.log('测试图片压缩');
        
        // 创建一个简单的图片
        const canvas = document.createElement('canvas');
        canvas.width = 100;
        canvas.height = 100;
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = '#3498db';
        ctx.fillRect(0, 0, 100, 100);
        
        // 转换为base64
        const originalDataUrl = canvas.toDataURL('image/png');
        const originalSize = Math.round((originalDataUrl.length - 22) * 3 / 4); // 估算原始大小
        
        // 模拟压缩
        const compressedDataUrl = canvas.toDataURL('image/jpeg', 0.5);
        const compressedSize = Math.round((compressedDataUrl.length - 22) * 3 / 4); // 估算压缩后大小
        
        resultDiv.innerHTML = `
          <p>原始图片大小: ${originalSize} bytes</p>
          <p>压缩后图片大小: ${compressedSize} bytes</p>
          <p>压缩率: ~${Math.round((1 - compressedSize / originalSize) * 100)}%</p>
          <img src="${compressedDataUrl}" alt="Compressed Image" style="margin-top: 10px; width: 100px; height: 100px;">
        `;
        console.log('图片压缩测试：原始大小', originalSize, '压缩后大小', compressedSize);
      }
    });
  });
  
  console.log('资源压缩示例准备就绪');
  console.log('点击按钮测试不同的资源压缩');
}

// 4. 网络请求优化示例
function networkRequestOptimizationExample() {
  console.log('\n=== 网络请求优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'network-request-optimization';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>网络请求优化示例</h2>
    <p>网络请求优化包括减少请求次数、优化请求大小、使用HTTP/2等技术。</p>
    <div class="request-types">
      <div class="request-type">
        <h3>批量请求</h3>
        <p>将多个请求合并为一个，减少HTTP请求次数。</p>
        <button class="request-test-btn" data-type="batch">测试批量请求</button>
      </div>
      <div class="request-type">
        <h3>延迟加载</h3>
        <p>延迟加载非关键资源，提高首屏加载速度。</p>
        <button class="request-test-btn" data-type="lazy">测试延迟加载</button>
      </div>
      <div class="request-type">
        <h3>HTTP/2</h3>
        <p>使用HTTP/2的多路复用特性，提高传输效率。</p>
        <button class="request-test-btn" data-type="http2">测试HTTP/2</button>
      </div>
    </div>
    <div id="request-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .network-request-optimization {
      font-family: Arial, sans-serif;
    }
    
    .request-types {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .request-type {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .request-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .request-test-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .request-test-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试网络请求优化
  const resultDiv = document.getElementById('request-result');
  const buttons = document.querySelectorAll('.request-test-btn');
  
  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const type = button.getAttribute('data-type');
      resultDiv.innerHTML = '';
      
      if (type === 'batch') {
        // 测试批量请求
        console.log('测试批量请求');
        
        // 模拟多个请求
        const requests = [
          fetch('data:text/plain,Data 1'),
          fetch('data:text/plain,Data 2'),
          fetch('data:text/plain,Data 3')
        ];
        
        resultDiv.innerHTML = '<p>正在执行批量请求...</p>';
        
        Promise.all(requests)
          .then(responses => Promise.all(responses.map(response => response.text())))
          .then(data => {
            resultDiv.innerHTML = `<p>批量请求完成，获取到 ${data.length} 个响应:</p><ul>${data.map(item => `<li>${item}</li>`).join('')}</ul>`;
            console.log('批量请求测试：成功获取数据', data);
          })
          .catch(error => {
            resultDiv.innerHTML = `<p>批量请求错误: ${error.message}</p>`;
            console.error('批量请求测试：错误', error);
          });
      } else if (type === 'lazy') {
        // 测试延迟加载
        console.log('测试延迟加载');
        
        resultDiv.innerHTML = '<p>正在延迟加载资源...</p>';
        
        // 模拟延迟加载
        setTimeout(() => {
          const script = document.createElement('script');
          script.textContent = 'console.log("Lazy loaded script executed");';
          document.head.appendChild(script);
          
          resultDiv.innerHTML = '<p>延迟加载完成，脚本已执行</p>';
          console.log('延迟加载测试：脚本已执行');
        }, 2000);
      } else if (type === 'http2') {
        // 测试HTTP/2
        console.log('测试HTTP/2');
        
        // 检查当前协议
        const protocol = window.location.protocol;
        const http2Supported = protocol === 'https:'; // HTTP/2通常在HTTPS上启用
        
        resultDiv.innerHTML = `
          <p>当前协议: ${protocol}</p>
          <p>HTTP/2支持: ${http2Supported ? '是' : '否'}</p>
          <p>HTTP/2特性: 多路复用、头部压缩、服务器推送等</p>
        `;
        console.log('HTTP/2测试：当前协议', protocol, 'HTTP/2支持', http2Supported);
      }
    });
  });
  
  console.log('网络请求优化示例准备就绪');
  console.log('点击按钮测试不同的网络请求优化');
}

// 5. CDN示例
function cdnExample() {
  console.log('\n=== CDN示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'cdn-example';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>CDN示例</h2>
    <p>CDN（内容分发网络）可以将静态资源分发到全球各地的边缘节点，减少网络延迟。</p>
    <div class="cdn-test">
      <h3>测试CDN加载</h3>
      <p>使用CDN加载第三方库，如jQuery、React等。</p>
      <button id="cdn-test-btn">测试CDN加载</button>
    </div>
    <div id="cdn-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .cdn-example {
      font-family: Arial, sans-serif;
    }
    
    .cdn-test {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .cdn-test h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    #cdn-test-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #cdn-test-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试CDN加载
  const resultDiv = document.getElementById('cdn-result');
  const button = document.getElementById('cdn-test-btn');
  
  button.addEventListener('click', () => {
    console.log('测试CDN加载');
    resultDiv.innerHTML = '<p>正在从CDN加载jQuery...</p>';
    
    // 从CDN加载jQuery
    const script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    script.onload = () => {
      resultDiv.innerHTML = '<p>jQuery加载成功！版本: ' + $.fn.jquery + '</p>';
      console.log('CDN测试：jQuery加载成功，版本', $.fn.jquery);
    };
    script.onerror = () => {
      resultDiv.innerHTML = '<p>jQuery加载失败</p>';
      console.error('CDN测试：jQuery加载失败');
    };
    document.head.appendChild(script);
  });
  
  console.log('CDN示例准备就绪');
  console.log('点击按钮测试CDN加载');
}

// 6. 网络性能监控示例
function networkPerformanceMonitoringExample() {
  console.log('\n=== 网络性能监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'network-performance-monitoring';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>网络性能监控示例</h2>
    <p>网络性能监控可以帮助我们了解页面加载过程中的网络性能指标。</p>
    <button id="performance-test-btn">测试网络性能</button>
    <div id="performance-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .network-performance-monitoring {
      font-family: Arial, sans-serif;
    }
    
    #performance-test-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #performance-test-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试网络性能
  const resultDiv = document.getElementById('performance-result');
  const button = document.getElementById('performance-test-btn');
  
  button.addEventListener('click', () => {
    console.log('测试网络性能');
    
    // 检查是否支持Performance API
    if (window.performance) {
      // 获取导航时间
      const navigationTiming = performance.getEntriesByType('navigation')[0];
      
      if (navigationTiming) {
        const metrics = {
          'DNS解析时间': navigationTiming.domainLookupEnd - navigationTiming.domainLookupStart,
          'TCP连接时间': navigationTiming.connectEnd - navigationTiming.connectStart,
          '首字节时间': navigationTiming.responseStart - navigationTiming.requestStart,
          '内容加载时间': navigationTiming.responseEnd - navigationTiming.responseStart,
          'DOM加载时间': navigationTiming.domContentLoadedEventEnd - navigationTiming.navigationStart,
          '页面加载时间': navigationTiming.loadEventEnd - navigationTiming.navigationStart
        };
        
        let html = '<h3>网络性能指标：</h3><ul>';
        for (const [key, value] of Object.entries(metrics)) {
          html += `<li>${key}: ${value.toFixed(2)}ms</li>`;
        }
        html += '</ul>';
        
        resultDiv.innerHTML = html;
        console.log('网络性能测试：', metrics);
      } else {
        resultDiv.innerHTML = '<p>无法获取导航时间数据</p>';
      }
    } else {
      resultDiv.innerHTML = '<p>浏览器不支持Performance API</p>';
    }
  });
  
  console.log('网络性能监控示例准备就绪');
  console.log('点击按钮测试网络性能');
}

// 7. 图片优化示例
function imageOptimizationExample() {
  console.log('\n=== 图片优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'image-optimization';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>图片优化示例</h2>
    <p>图片优化包括使用适当的图片格式、压缩图片、使用WebP格式等。</p>
    <div class="image-types">
      <div class="image-type">
        <h3>原图</h3>
        <canvas id="original-image" width="200" height="200"></canvas>
      </div>
      <div class="image-type">
        <h3>压缩后</h3>
        <canvas id="compressed-image" width="200" height="200"></canvas>
      </div>
    </div>
    <button id="image-test-btn">测试图片优化</button>
    <div id="image-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .image-optimization {
      font-family: Arial, sans-serif;
    }
    
    .image-types {
      display: flex;
      gap: 20px;
      margin-top: 20px;
    }
    
    .image-type {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
      text-align: center;
    }
    
    .image-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    canvas {
      border: 1px solid #ddd;
      margin-top: 10px;
    }
    
    #image-test-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #image-test-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 绘制测试图片
  const originalCanvas = document.getElementById('original-image');
  const compressedCanvas = document.getElementById('compressed-image');
  const originalCtx = originalCanvas.getContext('2d');
  const compressedCtx = compressedCanvas.getContext('2d');
  
  // 绘制原图
  originalCtx.fillStyle = '#3498db';
  originalCtx.fillRect(0, 0, 200, 200);
  originalCtx.fillStyle = 'white';
  originalCtx.font = '20px Arial';
  originalCtx.textAlign = 'center';
  originalCtx.textBaseline = 'middle';
  originalCtx.fillText('Original', 100, 100);
  
  // 测试图片优化
  const resultDiv = document.getElementById('image-result');
  const button = document.getElementById('image-test-btn');
  
  button.addEventListener('click', () => {
    console.log('测试图片优化');
    
    // 压缩图片
    const originalDataUrl = originalCanvas.toDataURL('image/png');
    const compressedDataUrl = originalCanvas.toDataURL('image/jpeg', 0.5);
    
    // 计算大小
    const originalSize = Math.round((originalDataUrl.length - 22) * 3 / 4); // 估算原始大小
    const compressedSize = Math.round((compressedDataUrl.length - 22) * 3 / 4); // 估算压缩后大小
    
    // 显示压缩后的图片
    const img = new Image();
    img.onload = () => {
      compressedCtx.drawImage(img, 0, 0, 200, 200);
    };
    img.src = compressedDataUrl;
    
    resultDiv.innerHTML = `
      <p>原始图片大小: ${originalSize} bytes</p>
      <p>压缩后图片大小: ${compressedSize} bytes</p>
      <p>压缩率: ~${Math.round((1 - compressedSize / originalSize) * 100)}%</p>
      <p>图片优化建议：</p>
      <ul>
        <li>使用适当的图片格式（JPEG、PNG、WebP）</li>
        <li>压缩图片减少文件大小</li>
        <li>使用响应式图片（srcset）</li>
        <li>懒加载图片</li>
      </ul>
    `;
    
    console.log('图片优化测试：原始大小', originalSize, '压缩后大小', compressedSize);
  });
  
  console.log('图片优化示例准备就绪');
  console.log('点击按钮测试图片优化');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端网络优化示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  resourceHintsExample();
  cachingStrategyExample();
  resourceCompressionExample();
  networkRequestOptimizationExample();
  cdnExample();
  networkPerformanceMonitoringExample();
  imageOptimizationExample();
  
  console.log('前端网络优化示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}