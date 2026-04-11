// HTTP 请求头示例代码

// 1. 常见请求头
const commonRequestHeaders = {
  'Host': '指定请求的服务器域名和端口',
  'User-Agent': '客户端信息（浏览器、操作系统等）',
  'Accept': '客户端能接受的内容类型',
  'Accept-Language': '客户端能接受的语言',
  'Accept-Encoding': '客户端能接受的编码方式',
  'Connection': '连接管理（keep-alive、close）',
  'Authorization': '认证信息（token等）',
  'Cookie': '发送给服务器的Cookie',
  'Content-Type': '请求体的类型',
  'Content-Length': '请求体的长度',
  'Referer': '发起请求的页面URL',
  'Origin': '请求的来源（CORS用）',
  'If-Modified-Since': '缓存验证',
  'If-None-Match': '缓存验证（ETag）'
};

console.log('常见请求头:', commonRequestHeaders);

// 2. 常见响应头
const commonResponseHeaders = {
  'Content-Type': '响应体的类型',
  'Content-Length': '响应体的长度',
  'Content-Encoding': '响应体的编码方式',
  'Set-Cookie': '设置Cookie',
  'Location': '重定向的目标URL',
  'Server': '服务器信息',
  'Date': '响应生成时间',
  'Cache-Control': '缓存控制',
  'ETag': '资源标识符',
  'Last-Modified': '资源最后修改时间',
  'Access-Control-Allow-Origin': 'CORS允许的来源',
  'Access-Control-Allow-Methods': 'CORS允许的方法',
  'Access-Control-Allow-Headers': 'CORS允许的头',
  'Strict-Transport-Security': '强制HTTPS',
  'Content-Security-Policy': '内容安全策略'
};

console.log('\n常见响应头:', commonResponseHeaders);

// 3. 在fetch中设置请求头
async function fetchWithHeaders() {
  console.log('\n=== Fetch 中设置请求头 ===');
  
  const headers = new Headers();
  headers.append('Content-Type', 'application/json');
  headers.append('Authorization', 'Bearer your-token-here');
  headers.append('X-Custom-Header', 'custom-value');
  
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
      method: 'GET',
      headers: headers
    });
    
    console.log('响应头:', response.headers);
    console.log('Content-Type:', response.headers.get('Content-Type'));
    console.log('Cache-Control:', response.headers.get('Cache-Control'));
    
    const data = await response.json();
    console.log('响应数据:', data);
  } catch (error) {
    console.error('请求错误:', error);
  }
}

fetchWithHeaders();

// 4. Content-Type 常见值
const contentTypeValues = {
  'application/json': 'JSON数据',
  'application/x-www-form-urlencoded': '表单数据',
  'multipart/form-data': '文件上传',
  'text/plain': '纯文本',
  'text/html': 'HTML',
  'text/css': 'CSS',
  'application/javascript': 'JavaScript',
  'image/png': 'PNG图片',
  'image/jpeg': 'JPEG图片',
  'application/pdf': 'PDF文档'
};

console.log('\nContent-Type 常见值:', contentTypeValues);

// 5. Cache-Control 值
const cacheControlValues = {
  'no-cache': '每次都验证缓存',
  'no-store': '不缓存任何内容',
  'public': '可以被任何缓存存储',
  'private': '只能被用户浏览器缓存',
  'max-age=3600': '缓存有效期1小时',
  's-maxage=3600': '共享缓存有效期1小时'
};

console.log('\nCache-Control 值:', cacheControlValues);

// 6. 安全相关头
const securityHeaders = {
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
  'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline'",
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'X-XSS-Protection': '1; mode=block',
  'Referrer-Policy': 'strict-origin-when-cross-origin'
};

console.log('\n安全相关头:', securityHeaders);

// 7. 解析和操作头
function parseHeaders(headersString) {
  const headers = {};
  const lines = headersString.trim().split('\n');
  lines.forEach(line => {
    const colonIndex = line.indexOf(':');
    if (colonIndex > 0) {
      const key = line.substring(0, colonIndex).trim();
      const value = line.substring(colonIndex + 1).trim();
      headers[key] = value;
    }
  });
  return headers;
}

const sampleHeaders = `Content-Type: application/json
Content-Length: 123
Cache-Control: public, max-age=3600
Server: nginx
Date: Sat, 11 Apr 2026 12:00:00 GMT`;

console.log('\n解析头:', parseHeaders(sampleHeaders));

// 8. CORS 相关头
const corsHeaders = {
  request: {
    'Origin': '请求来源',
    'Access-Control-Request-Method': '预检请求的方法',
    'Access-Control-Request-Headers': '预检请求的头'
  },
  response: {
    'Access-Control-Allow-Origin': '允许的来源',
    'Access-Control-Allow-Methods': '允许的方法',
    'Access-Control-Allow-Headers': '允许的头',
    'Access-Control-Allow-Credentials': '允许携带凭证',
    'Access-Control-Max-Age': '预检结果缓存时间'
  }
};

console.log('\nCORS 相关头:', corsHeaders);

// 9. 获取响应头的所有值
async function getAllResponseHeaders() {
  console.log('\n=== 获取所有响应头 ===');
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    
    console.log('所有响应头:');
    response.headers.forEach((value, key) => {
      console.log(`  ${key}: ${value}`);
    });
  } catch (error) {
    console.error('错误:', error);
  }
}

getAllResponseHeaders();
