// 跨域基础概念示例代码

// 1. 同源判断函数
function isSameOrigin(url1, url2) {
  try {
    const u1 = new URL(url1);
    const u2 = new URL(url2);
    return u1.protocol === u2.protocol &&
           u1.hostname === u2.hostname &&
           u1.port === u2.port;
  } catch {
    return false;
  }
}

// 测试同源判断
const testUrls = [
  ['http://example.com/page1', 'http://example.com/page2', '同源 ✓'],
  ['http://example.com', 'https://example.com', '协议不同 ✗'],
  ['http://a.example.com', 'http://b.example.com', '域名不同 ✗'],
  ['http://example.com:8080', 'http://example.com:3000', '端口不同 ✗'],
  ['http://example.com', 'http://www.example.com', '子域名不同 ✗']
];

console.log('=== 同源判断测试 ===');
testUrls.forEach(([url1, url2, expected]) => {
  const result = isSameOrigin(url1, url2);
  console.log(`${url1} vs ${url2}: ${result ? '同源' : '跨域'} (期望: ${expected})`);
});

// 2. 解析URL的组成部分
function parseURL(url) {
  const urlObj = new URL(url);
  return {
    protocol: urlObj.protocol,
    hostname: urlObj.hostname,
    port: urlObj.port || (urlObj.protocol === 'https:' ? '443' : '80'),
    origin: urlObj.origin,
    pathname: urlObj.pathname
  };
}

console.log('\n=== URL 解析 ===');
console.log('http://api.example.com:3000/users:', parseURL('http://api.example.com:3000/users'));
console.log('https://www.example.com/page:', parseURL('https://www.example.com/page'));

// 3. 跨域场景示例
const crossOriginScenarios = [
  {
    name: '前后端分离',
    description: '前端运行在 localhost:5173，后端API在 localhost:3000',
    frontend: 'http://localhost:5173',
    backend: 'http://localhost:3000',
    isCrossOrigin: true
  },
  {
    name: '第三方API',
    description: '调用天气、地图等第三方服务',
    frontend: 'https://myapp.com',
    backend: 'https://api.weather.com',
    isCrossOrigin: true
  },
  {
    name: '微服务',
    description: '多个服务运行在不同端口',
    serviceA: 'http://service-a:8001',
    serviceB: 'http://service-b:8002',
    isCrossOrigin: true
  },
  {
    name: '同域开发',
    description: '前后端在同一域名下',
    frontend: 'https://example.com',
    backend: 'https://example.com/api',
    isCrossOrigin: false
  }
];

console.log('\n=== 常见跨域场景 ===');
crossOriginScenarios.forEach(scenario => {
  console.log(`\n【${scenario.name}】`);
  console.log(`描述: ${scenario.description}`);
  console.log(`是否跨域: ${scenario.isCrossOrigin ? '是' : '否'}`);
});

// 4. 跨域解决方案对比
const solutions = {
  JSONP: {
    优点: '兼容性好，简单',
    缺点: '只支持GET，不安全',
    适用: '旧浏览器，简单需求'
  },
  CORS: {
    优点: '标准方案，支持所有方法',
    缺点: '需要服务器配置',
    适用: '现代浏览器，推荐'
  },
  代理: {
    优点: '前端无感知，安全',
    缺点: '需要代理服务器',
    适用: '开发环境，生产环境'
  },
  postMessage: {
    优点: '窗口间通信',
    缺点: '需要双方配合',
    适用: 'iframe通信'
  }
};

console.log('\n=== 跨域解决方案对比 ===');
Object.entries(solutions).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`优点: ${info.优点}`);
  console.log(`缺点: ${info.缺点}`);
  console.log(`适用: ${info.适用}`);
});

// 5. 模拟跨域请求错误
async function simulateCrossOriginError() {
  console.log('\n=== 模拟跨域请求错误 ===');
  try {
    const response = await fetch('https://example.com/api/data');
    console.log('响应:', response);
  } catch (error) {
    console.log('跨域错误类型:', error.name);
    console.log('错误信息:', error.message);
    console.log('提示: 这是典型的跨域错误，浏览器拦截了请求');
  }
}

// 6. 检查当前页面的origin
function getCurrentOrigin() {
  if (typeof window !== 'undefined') {
    return {
      origin: window.location.origin,
      protocol: window.location.protocol,
      hostname: window.location.hostname,
      port: window.location.port
    };
  }
  return { message: '请在浏览器环境中运行' };
}

console.log('\n=== 当前页面Origin ===');
console.log(getCurrentOrigin());

// 7. 跨域限制演示
const crossOriginRestrictions = {
  'Cookie/LocalStorage': '无法读取不同源的存储',
  'DOM访问': '无法操作不同源的DOM',
  'AJAX请求': '默认被浏览器拦截',
  'Canvas': '跨域图片会污染canvas'
};

console.log('\n=== 跨域限制 ===');
Object.entries(crossOriginRestrictions).forEach(([item, desc]) => {
  console.log(`${item}: ${desc}`);
});

// 8. 子域名跨域（document.domain）
function subdomainCrossOrigin() {
  console.log('\n=== 子域名跨域 ===');
  console.log('场景: a.example.com 和 b.example.com');
  console.log('解决方案: 设置 document.domain = "example.com"');
  console.log('注意: 只适用于主域相同的子域名');
}

subdomainCrossOrigin();
