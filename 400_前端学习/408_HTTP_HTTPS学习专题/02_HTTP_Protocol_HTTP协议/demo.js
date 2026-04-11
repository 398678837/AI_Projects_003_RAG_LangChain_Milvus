// HTTP 协议示例代码

// 1. HTTP 请求结构示例
const httpRequestExample = {
  requestLine: 'GET /api/users/1 HTTP/1.1',
  headers: {
    'Host': 'api.example.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive'
  },
  body: null
};

console.log('HTTP 请求结构示例:', httpRequestExample);

// 2. HTTP 响应结构示例
const httpResponseExample = {
  statusLine: 'HTTP/1.1 200 OK',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': '123',
    'Server': 'nginx',
    'Date': 'Sat, 11 Apr 2026 12:00:00 GMT',
    'Connection': 'keep-alive'
  },
  body: JSON.stringify({
    id: 1,
    name: '张三',
    email: 'zhangsan@example.com'
  })
};

console.log('HTTP 响应结构示例:', httpResponseExample);

// 3. 使用 XMLHttpRequest 发送请求
function xhrExample() {
  const xhr = new XMLHttpRequest();
  
  xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts/1', true);
  
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        console.log('XHR示例 - 响应:', JSON.parse(xhr.responseText));
        console.log('XHR示例 - 状态码:', xhr.status);
        console.log('XHR示例 - 响应头:', xhr.getAllResponseHeaders());
      } else {
        console.error('XHR示例 - 错误:', xhr.status);
      }
    }
  };
  
  xhr.send();
}

xhrExample();

// 4. POST 请求示例
async function postRequestExample() {
  const data = {
    title: 'foo',
    body: 'bar',
    userId: 1
  };
  
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    
    const result = await response.json();
    console.log('POST请求示例 - 响应:', result);
  } catch (error) {
    console.error('POST请求示例 - 错误:', error);
  }
}

postRequestExample();

// 5. HTTP 版本对比
const httpVersions = {
  'HTTP/1.0': {
    features: ['每次请求建立新连接', '无持久连接'],
    performance: '较低'
  },
  'HTTP/1.1': {
    features: ['持久连接', '请求流水线', 'Host头', '缓存控制'],
    performance: '中等'
  },
  'HTTP/2': {
    features: ['二进制协议', '多路复用', '服务器推送', '头部压缩'],
    performance: '高'
  },
  'HTTP/3': {
    features: ['基于QUIC', 'UDP传输', '0-RTT握手', '连接迁移'],
    performance: '最高'
  }
};

console.log('HTTP 版本对比:', httpVersions);

// 6. 解析响应头
function parseResponseHeaders(headersString) {
  const headers = {};
  const lines = headersString.trim().split('\n');
  lines.forEach(line => {
    const [key, value] = line.split(': ');
    if (key && value) {
      headers[key] = value;
    }
  });
  return headers;
}

const sampleHeaders = `Content-Type: application/json
Content-Length: 123
Server: nginx
Date: Sat, 11 Apr 2026 12:00:00 GMT`;

console.log('解析响应头:', parseResponseHeaders(sampleHeaders));
