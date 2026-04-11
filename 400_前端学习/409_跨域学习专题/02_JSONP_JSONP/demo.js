// JSONP 示例代码

// 1. 简单的JSONP实现
function jsonp(url, callbackName = 'callback') {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    const uniqueCallback = `jsonp_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    
    window[uniqueCallback] = function(data) {
      resolve(data);
      document.body.removeChild(script);
      delete window[uniqueCallback];
    };
    
    script.onerror = function() {
      reject(new Error('JSONP 请求失败'));
      document.body.removeChild(script);
      delete window[uniqueCallback];
    };
    
    const separator = url.includes('?') ? '&' : '?';
    script.src = `${url}${separator}${callbackName}=${uniqueCallback}`;
    document.body.appendChild(script);
  });
}

console.log('=== JSONP 简单实现 ===');
console.log('使用方法: jsonp(url).then(data => console.log(data))');

// 2. JSONP 工厂函数（更完善的版本）
class JSONPRequest {
  constructor(options = {}) {
    this.timeout = options.timeout || 10000;
    this.callbackParam = options.callbackParam || 'callback';
    this.prefix = options.prefix || 'jsonp_callback';
  }

  request(url, data = {}) {
    return new Promise((resolve, reject) => {
      const callbackName = `${this.prefix}_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
      const script = document.createElement('script');
      let timeoutId = null;

      window[callbackName] = (response) => {
        if (timeoutId) clearTimeout(timeoutId);
        resolve(response);
        this.cleanup(script, callbackName);
      };

      script.onerror = () => {
        if (timeoutId) clearTimeout(timeoutId);
        reject(new Error('JSONP 请求失败'));
        this.cleanup(script, callbackName);
      };

      timeoutId = setTimeout(() => {
        reject(new Error('JSONP 请求超时'));
        this.cleanup(script, callbackName);
      }, this.timeout);

      const queryString = Object.entries(data)
        .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
        .join('&');

      const separator = url.includes('?') ? '&' : '?';
      script.src = `${url}${separator}${queryString}${queryString ? '&' : ''}${this.callbackParam}=${callbackName}`;
      document.body.appendChild(script);
    });
  }

  cleanup(script, callbackName) {
    if (script.parentNode) {
      script.parentNode.removeChild(script);
    }
    try {
      delete window[callbackName];
    } catch (e) {
      window[callbackName] = undefined;
    }
  }
}

console.log('\n=== JSONP 类实现 ===');
const jsonpClient = new JSONPRequest({ timeout: 15000 });
console.log('使用方法: jsonpClient.request(url, params).then(data => console.log(data))');

// 3. JSONP 工作原理演示
function jsonpWorkflowDemo() {
  console.log('\n=== JSONP 工作流程 ===');
  
  const steps = [
    '1. 前端定义回调函数: window.myCallback = function(data) { ... }',
    '2. 动态创建 &lt;script&gt; 标签',
    '3. 设置 src 为: http://api.example.com/data?callback=myCallback',
    '4. 服务器接收请求，返回: myCallback({ "name": "张三" })',
    '5. 浏览器执行 script 内容',
    '6. 调用 myCallback 函数，前端拿到数据'
  ];
  
  steps.forEach(step => console.log(step));
}

jsonpWorkflowDemo();

// 4. 模拟服务器端JSONP响应
function simulateServerResponse(callbackName, data) {
  console.log('\n=== 模拟服务器响应 ===');
  const response = `${callbackName}(${JSON.stringify(data)})`;
  console.log('服务器返回:', response);
  return response;
}

const sampleData = { id: 1, name: '张三', email: 'zhangsan@example.com' };
simulateServerResponse('handleData', sampleData);

// 5. JSONP 优缺点
const jsonpProsCons = {
  优点: [
    '兼容性非常好，支持所有浏览器',
    '实现简单，不需要服务器复杂配置',
    '不需要XMLHttpRequest或Fetch API'
  ],
  缺点: [
    '只支持 GET 请求，不支持 POST/PUT/DELETE',
    '安全性较低，容易受到XSS攻击',
    '没有错误处理机制（只能靠timeout）',
    '无法获取HTTP状态码',
    '需要服务器端配合修改响应格式'
  ]
};

console.log('\n=== JSONP 优缺点 ===');
console.log('优点:');
jsonpProsCons.优点.forEach(p => console.log(`  ✓ ${p}`));
console.log('缺点:');
jsonpProsCons.缺点.forEach(c => console.log(`  ✗ ${c}`));

// 6. JSONP 使用场景
const jsonpUseCases = [
  '旧项目维护，需要兼容老版本浏览器',
  '调用一些老旧的第三方API（只提供JSONP）',
  '简单的GET请求，数据量不大',
  '快速原型开发'
];

console.log('\n=== JSONP 适用场景 ===');
jsonpUseCases.forEach((uc, i) => console.log(`${i + 1}. ${uc}`));

// 7. JSONP 不推荐使用的场景
const jsonpNotRecommended = [
  '现代Web应用（推荐CORS）',
  '需要POST/PUT/DELETE等方法',
  '传输敏感数据',
  '需要精确的错误处理'
];

console.log('\n=== JSONP 不推荐场景 ===');
jsonpNotRecommended.forEach((nr, i) => console.log(`${i + 1}. ${nr}`));

// 8. 模拟实际使用（需要在浏览器中运行）
function jsonpUsageExample() {
  console.log('\n=== JSONP 使用示例 ===');
  
  const exampleCode = `
// 示例：获取天气数据
const weatherUrl = 'https://api.weather.com/data';

jsonp(weatherUrl, { city: 'beijing' })
  .then(data => {
    console.log('天气数据:', data);
    console.log('温度:', data.temperature);
  })
  .catch(error => {
    console.error('获取失败:', error);
  });
`;
  console.log(exampleCode);
}

jsonpUsageExample();

// 9. 安全提示
function jsonpSecurityTips() {
  console.log('\n=== JSONP 安全提示 ===');
  console.log('⚠️  不要使用JSONP传输敏感数据');
  console.log('⚠️  只信任可靠的数据源');
  console.log('⚠️  现代应用优先使用CORS');
  console.log('⚠️  考虑使用Content Security Policy');
}

jsonpSecurityTips();
