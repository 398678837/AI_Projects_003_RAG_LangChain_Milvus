// 跨域知识总结

// 1. 跨域知识体系
const knowledgeSystem = {
  基础概念: [
    '同源策略',
    '什么是跨域',
    '跨域的影响'
  ],
  解决方案: {
    CORS: [
      '简单请求',
      '预检请求',
      '响应头配置',
      '携带凭证'
    ],
    代理: [
      '开发环境代理',
      'Nginx反向代理',
      '路径重写',
      '多环境配置'
    ],
    JSONP: [
      '原理',
      '实现',
      '优缺点'
    ],
    其他: [
      'postMessage',
      'document.domain',
      'window.name'
    ]
  },
  安全: [
    'XSS防护',
    'CSRF防护',
    'CORS安全配置',
    '安全响应头'
  ],
  实战: [
    '前后端分离',
    '微服务架构',
    '第三方API调用',
    '部署方案'
  ],
  工具: [
    'Ngrok内网穿透',
    'Charles抓包',
    'DevTools调试'
  ]
};

console.log('=== 跨域知识体系 ===');
console.log(JSON.stringify(knowledgeSystem, null, 2));

// 2. 方案决策树
function decisionTree(scenario) {
  console.log('\n=== 方案决策 ===');
  
  if (scenario === '现代应用 + 控制后端') {
    return '推荐: CORS';
  }
  if (scenario === '前后端分离开发') {
    return '推荐: 开发代理 + 生产CORS/Nginx';
  }
  if (scenario === '调用第三方API') {
    return '推荐: 后端代理';
  }
  if (scenario === '兼容IE等旧浏览器') {
    return '推荐: JSONP(简单) 或 代理';
  }
  if (scenario === 'iframe通信') {
    return '推荐: postMessage';
  }
  
  return '根据具体情况分析';
}

console.log('\n现代应用 + 控制后端:', decisionTree('现代应用 + 控制后端'));
console.log('前后端分离开发:', decisionTree('前后端分离开发'));
console.log('调用第三方API:', decisionTree('调用第三方API'));

// 3. 核心概念速查
const quickReference = {
  同源判断: '协议 + 域名 + 端口 完全一致',
  CORS响应头: {
    Origin: '允许的来源',
    Methods: '允许的方法',
    Headers: '允许的头',
    Credentials: '是否允许凭证',
    MaxAge: '预检缓存时间'
  },
  代理配置: {
    target: '目标服务器',
    changeOrigin: '修改Origin头',
    rewrite: '路径重写'
  },
  安全头: [
    'CSP',
    'X-Frame-Options',
    'X-XSS-Protection',
    'HSTS'
  ]
};

console.log('\n=== 核心概念速查 ===');
console.log(JSON.stringify(quickReference, null, 2));

// 4. 常见配置代码片段
const codeSnippets = {
  'Vite代理': `
proxy: {
  '/api': {
    target: 'http://localhost:3000',
    changeOrigin: true,
    rewrite: path => path.replace(/^\\/api/, '')
  }
}
`,
  'Express CORS': `
const cors = require('cors');
app.use(cors({
  origin: ['https://example.com', 'http://localhost:5173'],
  credentials: true
}));
`,
  'Nginx代理': `
location /api/ {
  proxy_pass http://localhost:3000/;
  proxy_set_header Host $host;
}
`,
  '安全响应头': `
res.setHeader('Content-Security-Policy', "default-src 'self'");
res.setHeader('X-Frame-Options', 'DENY');
res.setHeader('X-XSS-Protection', '1; mode=block');
`
};

console.log('\n=== 常见配置代码片段 ===');
Object.entries(codeSnippets).forEach(([name, code]) => {
  console.log(`\n【${name}】`);
  console.log(code);
});

// 5. 学习路径
const learningPath = [
  '1. 基础概念',
  '   - 理解同源策略',
  '   - 了解跨域产生的原因',
  '   - 知道跨域的影响',
  '',
  '2. 解决方案',
  '   - JSONP（简单了解）',
  '   - CORS（重点掌握）',
  '   - 代理（开发常用）',
  '   - 其他方案',
  '',
  '3. 安全防护',
  '   - XSS防护',
  '   - CSRF防护',
  '   - CORS安全配置',
  '',
  '4. 实战应用',
  '   - 前后端分离',
  '   - 微服务架构',
  '   - 部署方案',
  '',
  '5. 问题排查',
  '   - 调试工具',
  '   - 常见错误',
  '   - 排查技巧'
];

console.log('\n=== 学习路径 ===');
learningPath.forEach(step => console.log(step));

// 6. 总结回顾
console.log('\n=== 总结回顾 ===');
console.log('✓ 同源策略是浏览器的安全机制');
console.log('✓ 跨域是违反同源策略的请求');
console.log('✓ CORS是现代标准解决方案');
console.log('✓ 代理是开发和生产常用方案');
console.log('✓ 安全始终要放在第一位');
console.log('✓ 掌握调试技巧很重要');
console.log('\n跨域学习完成！继续探索更多Web知识吧！');
