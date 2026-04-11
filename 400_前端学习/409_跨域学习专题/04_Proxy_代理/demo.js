// 代理跨域示例代码

// 1. 代理工作原理
function proxyWorkflow() {
  console.log('=== 代理工作原理 ===');
  
  const workflow = [
    '浏览器请求: http://localhost:5173/api/users',
    '开发服务器拦截: 识别 /api 前缀',
    '转发请求: http://api.example.com/users',
    '目标服务器响应: 返回数据',
    '开发服务器转发: 数据返回给浏览器',
    '结果: 浏览器认为是同域请求，没有跨域问题'
  ];
  
  workflow.forEach((step, i) => console.log(`${i + 1}. ${step}`));
}

proxyWorkflow();

// 2. Vite 代理配置
const viteProxyConfig = `
// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\\/api/, '')
      },
      '/auth': {
        target: 'https://auth.example.com',
        changeOrigin: true,
        secure: false
      },
      '/ws': {
        target: 'ws://localhost:8080',
        ws: true
      }
    }
  }
});
`;

console.log('\n=== Vite 代理配置 ===');
console.log(viteProxyConfig);

// 3. Webpack DevServer 代理配置
const webpackProxyConfig = `
// webpack.config.js
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }
      },
      '/socket.io': {
        target: 'http://localhost:3000',
        ws: true,
        changeOrigin: true
      }
    }
  }
};
`;

console.log('\n=== Webpack DevServer 代理配置 ===');
console.log(webpackProxyConfig);

// 4. Create React App 代理配置
const craProxyConfig = {
  'package.json简单配置': `
{
  "name": "my-app",
  "proxy": "http://localhost:3000"
}
`,
  'setupProxy.js高级配置': `
// src/setupProxy.js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://localhost:3000',
      changeOrigin: true,
      pathRewrite: { '^/api': '' }
    })
  );
};
`
};

console.log('\n=== Create React App 代理配置 ===');
Object.entries(craProxyConfig).forEach(([name, config]) => {
  console.log(`\n【${name}】`);
  console.log(config);
});

// 5. Nginx 反向代理配置
const nginxProxyConfig = `
server {
  listen 80;
  server_name example.com;

  # 前端静态文件
  location / {
    root /var/www/dist;
    try_files $uri $uri/ /index.html;
  }

  # API 代理
  location /api/ {
    proxy_pass http://localhost:3000/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    # CORS 头（如果需要）
    add_header Access-Control-Allow-Origin *;
  }

  # WebSocket 代理
  location /ws/ {
    proxy_pass http://localhost:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
  }
}
`;

console.log('\n=== Nginx 反向代理配置 ===');
console.log(nginxProxyConfig);

// 6. Node.js 中间件代理（Express + http-proxy-middleware）
const nodeProxyConfig = `
// server.js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

app.use(express.static('dist'));

app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3000',
  changeOrigin: true,
  pathRewrite: { '^/api': '' },
  onProxyReq: (proxyReq, req, res) => {
    console.log('代理请求:', req.method, req.url);
  },
  onProxyRes: (proxyRes, req, res) => {
    console.log('代理响应:', proxyRes.statusCode);
  }
}));

app.listen(8080, () => {
  console.log('服务器运行在 http://localhost:8080');
});
`;

console.log('\n=== Node.js 中间件代理 ===');
console.log(nodeProxyConfig);

// 7. 代理配置选项说明
const proxyOptions = {
  target: '目标服务器地址',
  changeOrigin: '修改请求头中的Origin为target',
  secure: '是否验证SSL证书（false忽略）',
  rewrite/pathRewrite: '路径重写规则',
  ws: '是否代理WebSocket',
  headers: '额外添加的请求头',
  onProxyReq: '代理请求前的回调',
  onProxyRes: '代理响应后的回调',
  onError: '错误处理回调'
};

console.log('\n=== 代理配置选项 ===');
Object.entries(proxyOptions).forEach(([option, desc]) => {
  console.log(`  ${option}: ${desc}`);
});

// 8. 路径重写示例
const pathRewriteExamples = [
  {
    配置: 'rewrite: (path) => path.replace(/^\\/api/, "")',
    请求: '/api/users/1',
    目标: '/users/1'
  },
  {
    配置: 'rewrite: (path) => "/v1" + path',
    请求: '/users/1',
    目标: '/v1/users/1'
  },
  {
    配置: 'pathRewrite: { "^/old": "/new" }',
    请求: '/old/api/data',
    目标: '/new/api/data'
  }
];

console.log('\n=== 路径重写示例 ===');
pathRewriteExamples.forEach((ex, i) => {
  console.log(`\n示例 ${i + 1}:`);
  console.log(`  配置: ${ex.配置}`);
  console.log(`  请求: ${ex.请求}`);
  console.log(`  目标: ${ex.目标}`);
});

// 9. 多环境代理配置
const multiEnvProxy = `
// vite.config.js
import { defineConfig, loadEnv } from 'vite';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd());
  
  return {
    server: {
      proxy: {
        '/api': {
          target: env.VITE_API_URL || 'http://localhost:3000',
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\\/api/, '')
        }
      }
    }
  };
});

// .env.development
VITE_API_URL=http://localhost:3000

// .env.staging
VITE_API_URL=https://staging-api.example.com

// .env.production
VITE_API_URL=https://api.example.com
`;

console.log('\n=== 多环境代理配置 ===');
console.log(multiEnvProxy);

// 10. 代理 vs CORS 对比
const proxyVsCors = {
  代理: {
    优点: [
      '前端配置简单',
      '无需修改后端',
      '安全性好',
      '开发生产一致'
    ],
    缺点: [
      '需要代理服务器',
      '增加一层网络开销'
    ],
    适用: '开发环境、生产环境都推荐'
  },
  CORS: {
    优点: [
      '标准方案',
      '不需要额外服务器',
      '直接通信'
    ],
    缺点: [
      '需要后端配置',
      '预检请求增加开销'
    ],
    适用: '第三方API、公开API'
  }
};

console.log('\n=== 代理 vs CORS ===');
Object.entries(proxyVsCors).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log('优点:');
  info.优点.forEach(p => console.log(`  ✓ ${p}`));
  console.log('缺点:');
  info.缺点.forEach(c => console.log(`  ✗ ${c}`));
  console.log(`适用: ${info.适用}`);
});

// 11. 常见问题排查
const proxyTroubleshooting = {
  '代理不生效': [
    '检查路径匹配是否正确',
    '确认开发服务器已重启',
    '检查target地址是否正确'
  ],
  '404 Not Found': [
    '检查pathRewrite是否正确',
    '确认目标服务器路径存在',
    '查看代理转发后的完整URL'
  ],
  '504 Gateway Timeout': [
    '检查目标服务器是否启动',
    '确认网络连接正常',
    '增加timeout配置'
  ],
  '仍报CORS错误': [
    '确认请求走了代理（看Network）',
    '检查代理路径前缀',
    '可能是其他跨域问题'
  ]
};

console.log('\n=== 代理常见问题排查 ===');
Object.entries(proxyTroubleshooting).forEach(([issue, solutions]) => {
  console.log(`\n【${issue}】`);
  solutions.forEach(s => console.log(`  - ${s}`));
});
