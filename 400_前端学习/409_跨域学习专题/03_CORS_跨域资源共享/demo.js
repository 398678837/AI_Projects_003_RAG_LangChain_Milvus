// CORS 跨域资源共享示例代码

// 1. CORS 响应头说明
const corsHeaders = {
  'Access-Control-Allow-Origin': {
    说明: '允许的来源',
    示例: ['*', 'https://example.com', 'https://a.example.com,https://b.example.com']
  },
  'Access-Control-Allow-Methods': {
    说明: '允许的HTTP方法',
    示例: ['GET,POST,PUT,DELETE,OPTIONS']
  },
  'Access-Control-Allow-Headers': {
    说明: '允许的请求头',
    示例: ['Content-Type,Authorization,X-Custom-Header']
  },
  'Access-Control-Allow-Credentials': {
    说明: '是否允许携带凭证',
    示例: ['true']
  },
  'Access-Control-Max-Age': {
    说明: '预检结果缓存时间（秒）',
    示例: ['86400']
  },
  'Access-Control-Expose-Headers': {
    说明: '暴露给客户端的响应头',
    示例: ['X-Total-Count,X-Page-Count']
  }
};

console.log('=== CORS 响应头 ===');
Object.entries(corsHeaders).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`说明: ${info.说明}`);
  console.log(`示例: ${info.示例.join(' | ')}`);
});

// 2. 简单请求 vs 预检请求
const requestTypes = {
  简单请求: {
    条件: [
      '方法: GET/HEAD/POST',
      'Content-Type: text/plain/multipart/form-data/application/x-www-form-urlencoded',
      '无自定义请求头',
      '无Request.readableStream'
    ],
    特点: '直接发送，不需要预检'
  },
  预检请求: {
    条件: [
      '方法: PUT/PATCH/DELETE/CONNECT/OPTIONS/TRACE',
      'Content-Type: application/json等',
      '有自定义请求头',
      '使用ReadableStream'
    ],
    特点: '先发OPTIONS预检，通过后再发实际请求'
  }
};

console.log('\n=== 简单请求 vs 预检请求 ===');
Object.entries(requestTypes).forEach(([type, info]) => {
  console.log(`\n【${type}】`);
  console.log('条件:');
  info.条件.forEach(c => console.log(`  - ${c}`));
  console.log(`特点: ${info.特点}`);
});

// 3. 预检请求流程
function preflightWorkflow() {
  console.log('\n=== 预检请求流程 ===');
  
  const steps = [
    '1. 浏览器检测到非简单请求',
    '2. 自动发送 OPTIONS 预检请求',
    '3. 预检请求包含:',
    '   - Access-Control-Request-Method: 实际请求的方法',
    '   - Access-Control-Request-Headers: 实际请求的头',
    '4. 服务器返回CORS响应头',
    '5. 浏览器检查是否允许',
    '6. 允许则发送实际请求，否则报错'
  ];
  
  steps.forEach(step => console.log(step));
}

preflightWorkflow();

// 4. 前端CORS请求示例
function corsRequestExamples() {
  console.log('\n=== 前端CORS请求示例 ===');
  
  const examples = {
    '简单GET请求': `
fetch('https://api.example.com/data')
  .then(res => res.json())
  .then(data => console.log(data));
`,
    '带自定义头的请求': `
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123',
    'X-Custom-Header': 'value'
  },
  body: JSON.stringify({ name: '张三' })
});
`,
    '携带凭证的请求': `
fetch('https://api.example.com/data', {
  method: 'GET',
  credentials: 'include',
  headers: {
    'Cookie': 'sessionId=abc123'
  }
});
`,
    'XMLHttpRequest方式': `
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data');
xhr.withCredentials = true;
xhr.onload = () => console.log(xhr.response);
xhr.send();
`
  };
  
  Object.entries(examples).forEach(([name, code]) => {
    console.log(`\n【${name}】`);
    console.log(code);
  });
}

corsRequestExamples();

// 5. 服务器端CORS配置示例（Node.js/Express）
function serverCorsConfig() {
  console.log('\n=== 服务器端CORS配置示例 ===');
  
  const configs = {
    'Express - cors中间件': `
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors({
  origin: 'https://example.com',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,
  maxAge: 86400
}));
`,
    'Express - 手动设置': `
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'https://example.com');
  res.header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type,Authorization');
  res.header('Access-Control-Allow-Credentials', 'true');
  
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  next();
});
`,
    'Nginx配置': `
location /api {
  add_header 'Access-Control-Allow-Origin' 'https://example.com';
  add_header 'Access-Control-Allow-Methods' 'GET,POST,PUT,DELETE,OPTIONS';
  add_header 'Access-Control-Allow-Headers' 'Content-Type,Authorization';
  add_header 'Access-Control-Allow-Credentials' 'true';
  
  if ($request_method = 'OPTIONS') {
    return 204;
  }
}
`
  };
  
  Object.entries(configs).forEach(([name, config]) => {
    console.log(`\n【${name}】`);
    console.log(config);
  });
}

serverCorsConfig();

// 6. CORS 常见问题
const corsIssues = {
  'No Access-Control-Allow-Origin': {
    原因: '响应头缺少Access-Control-Allow-Origin',
    解决: '服务器设置该头'
  },
  'Allow-Origin不能为*同时带凭证': {
    原因: 'withCredentials=true时，Origin不能是*',
    解决: '指定具体的Origin'
  },
  '预检请求失败': {
    原因: 'OPTIONS请求未正确处理',
    解决: '服务器处理OPTIONS并返回200'
  },
  '自定义头被拒绝': {
    原因: '未在Allow-Headers中声明',
    解决: '添加到Allow-Headers'
  }
};

console.log('\n=== CORS 常见问题 ===');
Object.entries(corsIssues).forEach(([issue, info]) => {
  console.log(`\n【${issue}】`);
  console.log(`原因: ${info.原因}`);
  console.log(`解决: ${info.解决}`);
});

// 7. CORS 安全最佳实践
const corsSecurity = {
  不要使用Origin: '*': '除非是公开API，否则指定具体域名',
  验证Origin: '动态检查请求头的Origin是否在白名单',
  限制Methods: '只允许需要的HTTP方法',
  限制Headers: '只允许必要的请求头',
  谨慎使用Credentials: '需要时才开启，并配合具体Origin',
  设置合理的Max-Age: '缓存预检结果，减少请求'
};

console.log('\n=== CORS 安全最佳实践 ===');
Object.entries(corsSecurity).forEach(([practice, desc]) => {
  console.log(`✓ ${practice}: ${desc}`);
});

// 8. 动态Origin验证示例
function dynamicOriginCheck() {
  console.log('\n=== 动态Origin验证 ===');
  
  const code = `
// 服务器端示例
const allowedOrigins = [
  'https://a.example.com',
  'https://b.example.com',
  'https://localhost:5173'
];

app.use((req, res, next) => {
  const origin = req.headers.origin;
  if (allowedOrigins.includes(origin)) {
    res.header('Access-Control-Allow-Origin', origin);
  }
  next();
});
`;
  console.log(code);
}

dynamicOriginCheck();
