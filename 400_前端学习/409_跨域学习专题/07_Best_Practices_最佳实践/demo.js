// 跨域最佳实践示例代码

// 1. 跨域方案选择决策树
function chooseCrossOriginSolution(scenario) {
  const solutions = {
    '现代Web应用 + 控制后端': {
      推荐: 'CORS',
      理由: '标准方案，灵活安全'
    },
    '前后端分离开发': {
      推荐: '开发代理 + 生产CORS/Nginx',
      理由: '开发体验好，生产安全'
    },
    '需要兼容IE等旧浏览器': {
      推荐: 'JSONP（简单GET）或 代理',
      理由: '兼容性好'
    },
    '调用第三方API且无法修改': {
      推荐: '服务器端代理',
      理由: '前端无感知'
    },
    'iframe间通信': {
      推荐: 'postMessage',
      理由: '专门为窗口通信设计'
    },
    '子域名间通信': {
      推荐: 'document.domain + CORS',
      理由: '简单有效'
    }
  };
  
  return solutions[scenario] || { 推荐: '根据具体情况分析', 理由: '' };
}

console.log('=== 跨域方案选择 ===');
const scenarios = Object.keys({
  '现代Web应用 + 控制后端': '',
  '前后端分离开发': '',
  '需要兼容IE等旧浏览器': '',
  '调用第三方API且无法修改': '',
  'iframe间通信': '',
  '子域名间通信': ''
});

scenarios.forEach(s => {
  const result = chooseCrossOriginSolution(s);
  console.log(`\n【${s}】`);
  console.log(`  推荐: ${result.推荐}`);
  console.log(`  理由: ${result.理由}`);
});

// 2. 完整的 CORS 配置（Express示例）
const completeCorsConfig = `
// server.js
const express = require('express');
const cors = require('cors');
const app = express();

const allowedOrigins = [
  'https://www.example.com',
  'https://app.example.com',
  'http://localhost:5173',
  'http://localhost:3000'
];

const corsOptions = {
  origin: (origin, callback) => {
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-CSRF-Token'],
  exposedHeaders: ['X-Total-Count', 'X-Page'],
  credentials: true,
  maxAge: 86400
};

app.use(cors(corsOptions));

app.options('*', cors(corsOptions));
`;

console.log('\n=== 完整的 CORS 配置 ===');
console.log(completeCorsConfig);

// 3. 多环境代理配置（Vite示例）
const multiEnvProxy = `
// vite.config.js
import { defineConfig, loadEnv } from 'vite';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd());
  
  return {
    server: {
      proxy: {
        '/api': {
          target: env.VITE_API_URL,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\\/api/, ''),
          configure: (proxy, options) => {
            proxy.on('proxyReq', (proxyReq, req, res) => {
              console.log('[Proxy]', req.method, req.url);
            });
            proxy.on('proxyRes', (proxyRes, req, res) => {
              console.log('[Proxy]', proxyRes.statusCode, req.url);
            });
            proxy.on('error', (err, req, res) => {
              console.error('[Proxy Error]', err);
            });
          }
        },
        '/ws': {
          target: env.VITE_WS_URL,
          ws: true,
          changeOrigin: true
        }
      }
    }
  };
});

// .env.development
VITE_API_URL=http://localhost:3000
VITE_WS_URL=ws://localhost:8080

// .env.staging
VITE_API_URL=https://staging-api.example.com
VITE_WS_URL=wss://staging-ws.example.com
`;

console.log('\n=== 多环境代理配置 ===');
console.log(multiEnvProxy);

// 4. 安全响应头中间件
const securityHeadersMiddleware = `
// securityHeaders.js
function securityHeaders(req, res, next) {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  
  if (req.secure) {
    res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  }
  
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; " +
    "script-src 'self' 'unsafe-inline' https://trusted-cdn.com; " +
    "style-src 'self' 'unsafe-inline'; " +
    "img-src 'self' data: https:; " +
    "font-src 'self';"
  );
  
  next();
}

module.exports = securityHeaders;
`;

console.log('\n=== 安全响应头中间件 ===');
console.log(securityHeadersMiddleware);

// 5. 请求封装（带重试和超时）
const requestWrapper = `
// request.js
class Request {
  constructor(baseURL, options = {}) {
    this.baseURL = baseURL;
    this.timeout = options.timeout || 10000;
    this.retries = options.retries || 3;
  }

  async fetch(url, options = {}) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);
    
    try {
      const response = await fetch(this.baseURL + url, {
        ...options,
        signal: controller.signal,
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        }
      });
      
      clearTimeout(timeoutId);
      
      if (!response.ok) {
        throw new Error(\`HTTP \${response.status}\`);
      }
      
      return response.json();
    } catch (error) {
      clearTimeout(timeoutId);
      throw error;
    }
  }

  async fetchWithRetry(url, options = {}) {
    let lastError;
    for (let i = 0; i < this.retries; i++) {
      try {
        return await this.fetch(url, options);
      } catch (error) {
        lastError = error;
        if (i < this.retries - 1) {
          await this.delay(1000 * (i + 1));
        }
      }
    }
    throw lastError;
  }

  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

const api = new Request('https://api.example.com');
export default api;
`;

console.log('\n=== 请求封装 ===');
console.log(requestWrapper);

// 6. 调试技巧清单
const debuggingTips = [
  {
    工具: '浏览器 DevTools',
    面板: 'Network',
    作用: '查看请求响应、CORS错误'
  },
  {
    工具: 'Console',
    面板: 'Console',
    作用: '查看错误信息、日志'
  },
  {
    工具: 'Charles/Fiddler',
    面板: '-',
    作用: '抓包分析、修改请求'
  },
  {
    工具: 'curl/Postman',
    面板: '-',
    作用: '直接测试API，排除前端问题'
  }
];

console.log('\n=== 调试技巧 ===');
debuggingTips.forEach((tip, i) => {
  console.log(`\n${i + 1}. ${tip.工具}`);
  console.log(`   面板: ${tip.面板}`);
  console.log(`   作用: ${tip.作用}`);
});

// 7. 常见错误快速排查
const quickTroubleshooting = {
  'CORS 错误 No Access-Control-Allow-Origin': [
    '检查服务器CORS配置',
    '确认Origin在白名单',
    '查看预检请求OPTIONS'
  ],
  '代理请求 404': [
    '检查路径重写配置',
    '确认目标服务器路径',
    '查看代理转发后的URL'
  ],
  'Cookie 不发送': [
    '检查 withCredentials: true',
    '确认 SameSite 设置',
    '查看 Secure 属性（HTTPS）'
  ],
  '预检请求失败': [
    '确认服务器处理OPTIONS',
    '检查 Allow-Methods/Headers',
    '查看预检响应头'
  ]
};

console.log('\n=== 快速排查 ===');
Object.entries(quickTroubleshooting).forEach(([error, checks]) => {
  console.log(`\n【${error}】`);
  checks.forEach(c => console.log(`  ✓ ${c}`));
});

// 8. 项目结构建议
const projectStructure = `
project/
├── src/
│   ├── api/
│   │   ├── index.js          # 请求封装
│   │   └── modules/          # API模块
│   │       └── user.js
│   ├── config/
│   │   └── api.js            # API配置
│   └── utils/
│       └── request.js        # 请求工具
├── .env.development
├── .env.staging
├── .env.production
└── vite.config.js            # 代理配置
`;

console.log('\n=== 项目结构建议 ===');
console.log(projectStructure);

// 9. 性能优化建议
const performanceTips = [
  '预检请求缓存: Access-Control-Max-Age: 86400',
  '使用HTTP/2: 减少连接开销',
  '合并请求: 减少跨域次数',
  'CDN加速: 静态资源使用CDN',
  '合理缓存: 利用浏览器缓存'
];

console.log('\n=== 性能优化 ===');
performanceTips.forEach((tip, i) => console.log(`${i + 1}. ${tip}`));

// 10. 最佳实践总结
const bestPracticesSummary = {
  '开发阶段': [
    '使用开发代理，体验好',
    '配置多环境变量',
    '添加代理日志便于调试'
  ],
  '生产阶段': [
    '优先使用CORS',
    '或Nginx反向代理',
    '配置安全响应头'
  ],
  '安全方面': [
    '验证Origin白名单',
    '设置CSP策略',
    '使用SameSite Cookie'
  ],
  '维护方面': [
    '统一请求封装',
    '完善错误处理',
    '记录请求日志'
  ]
};

console.log('\n=== 最佳实践总结 ===');
Object.entries(bestPracticesSummary).forEach(([phase, practices]) => {
  console.log(`\n【${phase}】`);
  practices.forEach(p => console.log(`  ✓ ${p}`));
});
