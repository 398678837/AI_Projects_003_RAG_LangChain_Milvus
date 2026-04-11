// 前端缓存策略示例

// 1. 浏览器缓存示例
function browserCacheExample() {
  console.log('=== 浏览器缓存示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'browser-cache';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>浏览器缓存示例</h2>
    <p>浏览器缓存可以存储静态资源，减少重复请求，提高加载速度。</p>
    
    <div class="cache-types">
      <div class="cache-type">
        <h3>强缓存</h3>
        <p>使用Cache-Control和Expires头控制，浏览器直接从缓存中获取资源。</p>
        <button class="cache-test-btn" data-type="strong">测试强缓存</button>
      </div>
      <div class="cache-type">
        <h3>协商缓存</h3>
        <p>使用ETag和Last-Modified头控制，浏览器发送请求验证资源是否过期。</p>
        <button class="cache-test-btn" data-type="negotiated">测试协商缓存</button>
      </div>
    </div>
    
    <div id="cache-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .browser-cache {
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
  
  // 测试浏览器缓存
  const resultDiv = document.getElementById('cache-result');
  const buttons = document.querySelectorAll('.cache-test-btn');
  
  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const type = button.getAttribute('data-type');
      resultDiv.innerHTML = '';
      
      if (type === 'strong') {
        // 测试强缓存
        console.log('测试强缓存');
        
        // 创建一个带有缓存头的请求
        fetch('data:text/plain,Hello World', {
          headers: {
            'Cache-Control': 'public, max-age=31536000'
          }
        })
          .then(response => response.text())
          .then(data => {
            resultDiv.innerHTML = `<p>强缓存测试：成功获取数据: ${data}</p>`;
            console.log('强缓存测试：成功获取数据');
          })
          .catch(error => {
            resultDiv.innerHTML = `<p>强缓存测试：错误: ${error.message}</p>`;
            console.error('强缓存测试：错误', error);
          });
      } else if (type === 'negotiated') {
        // 测试协商缓存
        console.log('测试协商缓存');
        
        // 创建一个带有协商缓存头的请求
        fetch('data:text/plain,Hello World', {
          headers: {
            'Cache-Control': 'no-cache'
          }
        })
          .then(response => response.text())
          .then(data => {
            resultDiv.innerHTML = `<p>协商缓存测试：成功获取数据: ${data}</p>`;
            console.log('协商缓存测试：成功获取数据');
          })
          .catch(error => {
            resultDiv.innerHTML = `<p>协商缓存测试：错误: ${error.message}</p>`;
            console.error('协商缓存测试：错误', error);
          });
      }
    });
  });
  
  console.log('浏览器缓存示例准备就绪');
  console.log('点击按钮测试不同的缓存策略');
}

// 2. 本地存储示例
function localStorageExample() {
  console.log('\n=== 本地存储示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'local-storage';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>本地存储示例</h2>
    <p>本地存储包括localStorage、sessionStorage和IndexedDB，可以存储用户数据和应用状态。</p>
    
    <div class="storage-types">
      <div class="storage-type">
        <h3>localStorage</h3>
        <p>存储持久化数据，容量约5MB。</p>
        <input type="text" id="local-storage-input" placeholder="输入要存储的数据">
        <button id="local-storage-save">保存</button>
        <button id="local-storage-get">获取</button>
        <button id="local-storage-clear">清除</button>
        <p id="local-storage-result"></p>
      </div>
      
      <div class="storage-type">
        <h3>sessionStorage</h3>
        <p>存储会话数据，页面关闭后清除。</p>
        <input type="text" id="session-storage-input" placeholder="输入要存储的数据">
        <button id="session-storage-save">保存</button>
        <button id="session-storage-get">获取</button>
        <button id="session-storage-clear">清除</button>
        <p id="session-storage-result"></p>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .local-storage {
      font-family: Arial, sans-serif;
    }
    
    .storage-types {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .storage-type {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .storage-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    input {
      padding: 8px;
      margin: 10px 0;
      width: 100%;
      box-sizing: border-box;
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
    
    #local-storage-result,
    #session-storage-result {
      margin-top: 10px;
      padding: 10px;
      border: 1px solid #ddd;
      background-color: #f0f0f0;
    }
  `;
  document.head.appendChild(style);
  
  // 测试localStorage
  const localStorageInput = document.getElementById('local-storage-input');
  const localStorageSave = document.getElementById('local-storage-save');
  const localStorageGet = document.getElementById('local-storage-get');
  const localStorageClear = document.getElementById('local-storage-clear');
  const localStorageResult = document.getElementById('local-storage-result');
  
  localStorageSave.addEventListener('click', () => {
    const value = localStorageInput.value;
    localStorage.setItem('test-key', value);
    localStorageResult.textContent = `已保存: ${value}`;
    console.log('localStorage保存:', value);
  });
  
  localStorageGet.addEventListener('click', () => {
    const value = localStorage.getItem('test-key');
    localStorageResult.textContent = `获取到: ${value || '无数据'}`;
    console.log('localStorage获取:', value);
  });
  
  localStorageClear.addEventListener('click', () => {
    localStorage.removeItem('test-key');
    localStorageResult.textContent = '已清除';
    console.log('localStorage清除');
  });
  
  // 测试sessionStorage
  const sessionStorageInput = document.getElementById('session-storage-input');
  const sessionStorageSave = document.getElementById('session-storage-save');
  const sessionStorageGet = document.getElementById('session-storage-get');
  const sessionStorageClear = document.getElementById('session-storage-clear');
  const sessionStorageResult = document.getElementById('session-storage-result');
  
  sessionStorageSave.addEventListener('click', () => {
    const value = sessionStorageInput.value;
    sessionStorage.setItem('test-key', value);
    sessionStorageResult.textContent = `已保存: ${value}`;
    console.log('sessionStorage保存:', value);
  });
  
  sessionStorageGet.addEventListener('click', () => {
    const value = sessionStorage.getItem('test-key');
    sessionStorageResult.textContent = `获取到: ${value || '无数据'}`;
    console.log('sessionStorage获取:', value);
  });
  
  sessionStorageClear.addEventListener('click', () => {
    sessionStorage.removeItem('test-key');
    sessionStorageResult.textContent = '已清除';
    console.log('sessionStorage清除');
  });
  
  console.log('本地存储示例准备就绪');
  console.log('测试localStorage和sessionStorage的使用');
}

// 3. IndexedDB示例
function indexedDbExample() {
  console.log('\n=== IndexedDB示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'indexed-db';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>IndexedDB示例</h2>
    <p>IndexedDB是一种本地存储方案，用于存储结构化数据，容量更大。</p>
    
    <div class="db-operations">
      <h3>数据库操作</h3>
      <button id="init-db">初始化数据库</button>
      <button id="add-data">添加数据</button>
      <button id="get-data">获取数据</button>
      <button id="clear-data">清除数据</button>
      <div id="db-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .indexed-db {
      font-family: Arial, sans-serif;
    }
    
    .db-operations {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
      margin-top: 20px;
    }
    
    .db-operations h3 {
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
  `;
  document.head.appendChild(style);
  
  // 测试IndexedDB
  const initDbBtn = document.getElementById('init-db');
  const addDataBtn = document.getElementById('add-data');
  const getDataBtn = document.getElementById('get-data');
  const clearDataBtn = document.getElementById('clear-data');
  const dbResult = document.getElementById('db-result');
  
  let db;
  
  // 初始化数据库
  initDbBtn.addEventListener('click', () => {
    console.log('初始化IndexedDB');
    dbResult.innerHTML = '<p>正在初始化数据库...</p>';
    
    const request = indexedDB.open('test-db', 1);
    
    request.onupgradeneeded = (event) => {
      db = event.target.result;
      if (!db.objectStoreNames.contains('users')) {
        db.createObjectStore('users', { keyPath: 'id' });
      }
      dbResult.innerHTML = '<p>数据库初始化成功</p>';
      console.log('数据库初始化成功');
    };
    
    request.onsuccess = (event) => {
      db = event.target.result;
      dbResult.innerHTML = '<p>数据库连接成功</p>';
      console.log('数据库连接成功');
    };
    
    request.onerror = (event) => {
      dbResult.innerHTML = '<p>数据库初始化失败</p>';
      console.error('数据库初始化失败', event.target.error);
    };
  });
  
  // 添加数据
  addDataBtn.addEventListener('click', () => {
    if (!db) {
      dbResult.innerHTML = '<p>请先初始化数据库</p>';
      return;
    }
    
    console.log('添加数据到IndexedDB');
    dbResult.innerHTML = '<p>正在添加数据...</p>';
    
    const transaction = db.transaction(['users'], 'readwrite');
    const store = transaction.objectStore('users');
    
    const user = {
      id: Date.now(),
      name: 'John Doe',
      age: 30,
      email: 'john@example.com'
    };
    
    const request = store.add(user);
    
    request.onsuccess = () => {
      dbResult.innerHTML = `<p>数据添加成功: ${JSON.stringify(user)}</p>`;
      console.log('数据添加成功', user);
    };
    
    request.onerror = () => {
      dbResult.innerHTML = '<p>数据添加失败</p>';
      console.error('数据添加失败');
    };
  });
  
  // 获取数据
  getDataBtn.addEventListener('click', () => {
    if (!db) {
      dbResult.innerHTML = '<p>请先初始化数据库</p>';
      return;
    }
    
    console.log('从IndexedDB获取数据');
    dbResult.innerHTML = '<p>正在获取数据...</p>';
    
    const transaction = db.transaction(['users'], 'readonly');
    const store = transaction.objectStore('users');
    const request = store.getAll();
    
    request.onsuccess = () => {
      const users = request.result;
      dbResult.innerHTML = `<p>获取到 ${users.length} 条数据:</p><pre>${JSON.stringify(users, null, 2)}</pre>`;
      console.log('获取数据成功', users);
    };
    
    request.onerror = () => {
      dbResult.innerHTML = '<p>数据获取失败</p>';
      console.error('数据获取失败');
    };
  });
  
  // 清除数据
  clearDataBtn.addEventListener('click', () => {
    if (!db) {
      dbResult.innerHTML = '<p>请先初始化数据库</p>';
      return;
    }
    
    console.log('清除IndexedDB数据');
    dbResult.innerHTML = '<p>正在清除数据...</p>';
    
    const transaction = db.transaction(['users'], 'readwrite');
    const store = transaction.objectStore('users');
    const request = store.clear();
    
    request.onsuccess = () => {
      dbResult.innerHTML = '<p>数据清除成功</p>';
      console.log('数据清除成功');
    };
    
    request.onerror = () => {
      dbResult.innerHTML = '<p>数据清除失败</p>';
      console.error('数据清除失败');
    };
  });
  
  console.log('IndexedDB示例准备就绪');
  console.log('点击按钮测试IndexedDB的使用');
}

// 4. Service Worker缓存示例
function serviceWorkerExample() {
  console.log('\n=== Service Worker缓存示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'service-worker';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>Service Worker缓存示例</h2>
    <p>Service Worker可以缓存静态资源，提供离线访问能力。</p>
    
    <div class="sw-operations">
      <h3>Service Worker操作</h3>
      <button id="register-sw">注册Service Worker</button>
      <button id="check-sw">检查Service Worker状态</button>
      <button id="cache-resources">缓存资源</button>
      <div id="sw-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .service-worker {
      font-family: Arial, sans-serif;
    }
    
    .sw-operations {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
      margin-top: 20px;
    }
    
    .sw-operations h3 {
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
  `;
  document.head.appendChild(style);
  
  // 测试Service Worker
  const registerSwBtn = document.getElementById('register-sw');
  const checkSwBtn = document.getElementById('check-sw');
  const cacheResourcesBtn = document.getElementById('cache-resources');
  const swResult = document.getElementById('sw-result');
  
  // 注册Service Worker
  registerSwBtn.addEventListener('click', () => {
    console.log('注册Service Worker');
    swResult.innerHTML = '<p>正在注册Service Worker...</p>';
    
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('service-worker.js')
        .then(registration => {
          swResult.innerHTML = `<p>Service Worker注册成功: ${registration.scope}</p>`;
          console.log('Service Worker注册成功', registration);
        })
        .catch(error => {
          swResult.innerHTML = `<p>Service Worker注册失败: ${error.message}</p>`;
          console.error('Service Worker注册失败', error);
        });
    } else {
      swResult.innerHTML = '<p>浏览器不支持Service Worker</p>';
      console.log('浏览器不支持Service Worker');
    }
  });
  
  // 检查Service Worker状态
  checkSwBtn.addEventListener('click', () => {
    console.log('检查Service Worker状态');
    swResult.innerHTML = '<p>正在检查Service Worker状态...</p>';
    
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.ready
        .then(registration => {
          swResult.innerHTML = `<p>Service Worker状态: 就绪</p>`;
          console.log('Service Worker状态: 就绪', registration);
        })
        .catch(error => {
          swResult.innerHTML = `<p>Service Worker状态: 未就绪</p>`;
          console.log('Service Worker状态: 未就绪', error);
        });
    } else {
      swResult.innerHTML = '<p>浏览器不支持Service Worker</p>';
      console.log('浏览器不支持Service Worker');
    }
  });
  
  // 缓存资源
  cacheResourcesBtn.addEventListener('click', () => {
    console.log('缓存资源');
    swResult.innerHTML = '<p>正在缓存资源...</p>';
    
    if ('caches' in window) {
      caches.open('test-cache')
        .then(cache => {
          return cache.addAll([
            '/',
            '/index.html'
          ]);
        })
        .then(() => {
          swResult.innerHTML = '<p>资源缓存成功</p>';
          console.log('资源缓存成功');
        })
        .catch(error => {
          swResult.innerHTML = `<p>资源缓存失败: ${error.message}</p>`;
          console.error('资源缓存失败', error);
        });
    } else {
      swResult.innerHTML = '<p>浏览器不支持Cache API</p>';
      console.log('浏览器不支持Cache API');
    }
  });
  
  console.log('Service Worker示例准备就绪');
  console.log('点击按钮测试Service Worker的使用');
}

// 5. CDN缓存示例
function cdnCacheExample() {
  console.log('\n=== CDN缓存示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'cdn-cache';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>CDN缓存示例</h2>
    <p>CDN缓存可以将资源缓存在全球各地的边缘节点，减少网络延迟。</p>
    
    <div class="cdn-examples">
      <div class="cdn-example">
        <h3>静态资源CDN</h3>
        <img src="https://picsum.photos/id/252/400/300" alt="CDN image" style="max-width: 100%; height: auto;">
        <p>https://picsum.photos/id/252/400/300</p>
      </div>
      
      <div class="cdn-example">
        <h3>版本化URL</h3>
        <p>使用版本化URL确保资源更新时缓存失效</p>
        <code>https://cdn.example.com/style.css?v=1.0.0</code>
      </div>
      
      <div class="cdn-example">
        <h3>内容哈希</h3>
        <p>使用内容哈希确保资源内容变化时缓存失效</p>
        <code>https://cdn.example.com/style.5e7f9a.css</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .cdn-cache {
      font-family: Arial, sans-serif;
    }
    
    .cdn-examples {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .cdn-example {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .cdn-example h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .cdn-example p {
      font-size: 14px;
    }
    
    code {
      display: block;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      word-break: break-all;
    }
  `;
  document.head.appendChild(style);
  
  console.log('CDN缓存示例准备就绪');
  console.log('查看页面中的CDN缓存示例');
}

// 6. 缓存性能监控示例
function cachePerformanceExample() {
  console.log('\n=== 缓存性能监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'cache-performance';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>缓存性能监控示例</h2>
    <p>缓存性能监控可以帮助我们了解缓存的使用情况和效果。</p>
    
    <div class="performance-test">
      <h3>测试缓存性能</h3>
      <button id="performance-btn">测试缓存性能</button>
      <div id="performance-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .cache-performance {
      font-family: Arial, sans-serif;
    }
    
    .performance-test {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
      margin-top: 20px;
    }
    
    .performance-test h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    #performance-btn {
      padding: 8px 16px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #performance-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试缓存性能
  const performanceBtn = document.getElementById('performance-btn');
  const performanceResult = document.getElementById('performance-result');
  
  performanceBtn.addEventListener('click', () => {
    console.log('测试缓存性能');
    performanceResult.innerHTML = '<p>正在测试缓存性能...</p>';
    
    // 清除之前的性能条目
    if (performance.clearResourceTimings) {
      performance.clearResourceTimings();
    }
    
    // 测试缓存效果
    const startTime = performance.now();
    
    // 发起请求
    fetch('data:text/plain,Hello World')
      .then(response => response.text())
      .then(data => {
        const firstRequestTime = performance.now() - startTime;
        
        // 再次发起相同请求（应该从缓存中获取）
        const secondStartTime = performance.now();
        
        return fetch('data:text/plain,Hello World')
          .then(response => response.text())
          .then(data => {
            const secondRequestTime = performance.now() - secondStartTime;
            
            performanceResult.innerHTML = `
              <p>第一次请求时间: ${firstRequestTime.toFixed(2)}ms</p>
              <p>第二次请求时间: ${secondRequestTime.toFixed(2)}ms</p>
              <p>缓存效果: ${(1 - secondRequestTime / firstRequestTime * 100).toFixed(2)}% 时间节省</p>
            `;
            
            console.log('缓存性能测试：第一次请求时间', firstRequestTime, '第二次请求时间', secondRequestTime);
          });
      })
      .catch(error => {
        performanceResult.innerHTML = `<p>测试失败: ${error.message}</p>`;
        console.error('缓存性能测试失败', error);
      });
  });
  
  console.log('缓存性能监控示例准备就绪');
  console.log('点击按钮测试缓存性能');
}

// 7. 缓存策略最佳实践示例
function cacheBestPracticesExample() {
  console.log('\n=== 缓存策略最佳实践示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'cache-best-practices';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>缓存策略最佳实践示例</h2>
    <p>缓存策略的最佳实践可以帮助我们提高应用性能，提供更好的用户体验。</p>
    
    <div class="best-practices">
      <div class="best-practice">
        <h3>静态资源缓存</h3>
        <p>设置较长的缓存时间，使用版本化URL</p>
        <code>Cache-Control: public, max-age=31536000</code>
      </div>
      
      <div class="best-practice">
        <h3>动态资源缓存</h3>
        <p>使用协商缓存，设置较短的缓存时间</p>
        <code>Cache-Control: no-cache</code>
      </div>
      
      <div class="best-practice">
        <h3>Service Worker缓存</h3>
        <p>预缓存关键资源，使用运行时缓存</p>
        <code>// 预缓存静态资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        return cache.addAll(STATIC_ASSETS);
      })
  );
});</code>
      </div>
      
      <div class="best-practice">
        <h3>本地存储使用</h3>
        <p>存储用户偏好设置，避免存储敏感数据</p>
        <code>// 存储用户偏好
localStorage.setItem('userPreferences', JSON.stringify(preferences));</code>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .cache-best-practices {
      font-family: Arial, sans-serif;
    }
    
    .best-practices {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    
    .best-practice {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .best-practice h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .best-practice p {
      font-size: 14px;
      margin-bottom: 10px;
    }
    
    code {
      display: block;
      padding: 10px;
      background-color: #f0f0f0;
      border-radius: 4px;
      font-size: 12px;
      white-space: pre-wrap;
    }
  `;
  document.head.appendChild(style);
  
  console.log('缓存策略最佳实践示例准备就绪');
  console.log('查看页面中的缓存策略最佳实践');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端缓存策略示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  browserCacheExample();
  localStorageExample();
  indexedDbExample();
  serviceWorkerExample();
  cdnCacheExample();
  cachePerformanceExample();
  cacheBestPracticesExample();
  
  console.log('前端缓存策略示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}