// HTTP/HTTPS 基础概念示例代码

// 1. URL 解析示例
function parseURL(url) {
  const urlObj = new URL(url);
  return {
    protocol: urlObj.protocol,
    hostname: urlObj.hostname,
    port: urlObj.port,
    pathname: urlObj.pathname,
    search: urlObj.search,
    hash: urlObj.hash,
    origin: urlObj.origin
  };
}

// 示例URL
const exampleUrl = 'https://www.example.com:8080/path/to/page?param1=value1&param2=value2#section1';
console.log('URL解析结果:', parseURL(exampleUrl));

// 2. 构建URL示例
function buildURL(baseUrl, params = {}) {
  const url = new URL(baseUrl);
  Object.keys(params).forEach(key => {
    url.searchParams.append(key, params[key]);
  });
  return url.toString();
}

const baseUrl = 'https://api.example.com/users';
const params = { page: 1, limit: 10, sort: 'name' };
console.log('构建的URL:', buildURL(baseUrl, params));

// 3. 简单的HTTP请求示例（使用fetch）
async function fetchExample() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const data = await response.json();
    console.log('Fetch示例 - 响应数据:', data);
    console.log('Fetch示例 - 状态码:', response.status);
    console.log('Fetch示例 - 响应头:', response.headers);
  } catch (error) {
    console.error('Fetch示例 - 错误:', error);
  }
}

fetchExample();

// 4. HTTP与HTTPS对比
const httpVsHttps = {
  HTTP: {
    protocol: 'http://',
    defaultPort: 80,
    security: '不加密，数据明文传输',
    useCase: '内部网络、测试环境'
  },
  HTTPS: {
    protocol: 'https://',
    defaultPort: 443,
    security: '加密传输，使用SSL/TLS',
    useCase: '生产环境、敏感数据传输'
  }
};

console.log('HTTP vs HTTPS:', httpVsHttps);

// 5. 查询参数解析
function parseQueryString(url) {
  const urlObj = new URL(url);
  const params = {};
  urlObj.searchParams.forEach((value, key) => {
    params[key] = value;
  });
  return params;
}

const queryUrl = 'https://example.com/search?q=javascript&sort=price&order=desc';
console.log('查询参数解析:', parseQueryString(queryUrl));
