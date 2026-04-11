// 认证实战应用示例代码

// 1. SPA + JWT 完整流程（前端）
const spaJwtFlow = {
  前端存储: {
    accessToken: 'localStorage 或内存变量',
    refreshToken: 'HttpOnly Cookie'
  },
  流程: [
    '1. 用户输入用户名密码',
    '2. 前端 POST /api/login',
    '3. 后端验证，返回 access_token 和 refresh_token',
    '4. 前端保存 access_token 到内存，refresh_token 通过 Cookie 自动保存',
    '5. 请求 API 时添加 Authorization: Bearer {access_token}',
    '6. access_token 过期（401）',
    '7. 前端自动 POST /api/refresh（携带 refresh_token Cookie）',
    '8. 获取新的 access_token',
    '9. 重试原请求',
    '10. refresh_token 也过期 → 跳转登录页'
  ]
};

console.log('=== SPA + JWT 完整流程 ===');
console.log('前端存储:', spaJwtFlow.前端存储);
spaJwtFlow.流程.forEach((step, i) => console.log(`${i + 1}. ${step}`));

// 2. 前端 Axios 拦截器实现
const axiosInterceptorExample = `
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com',
  withCredentials: true
});

let isRefreshing = false;
let refreshSubscribers = [];

function subscribeTokenRefresh(callback) {
  refreshSubscribers.push(callback);
}

function onTokenRefreshed(token) {
  refreshSubscribers.forEach(callback => callback(token));
  refreshSubscribers = [];
}

api.interceptors.request.use(
  (config) => {
    const token = getAccessToken();
    if (token) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    
    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        return new Promise(resolve => {
          subscribeTokenRefresh(token => {
            originalRequest.headers.Authorization = \`Bearer \${token}\`;
            resolve(api(originalRequest));
          });
        });
      }
      
      originalRequest._retry = true;
      isRefreshing = true;
      
      try {
        const response = await api.post('/auth/refresh');
        const newToken = response.data.access_token;
        setAccessToken(newToken);
        onTokenRefreshed(newToken);
        originalRequest.headers.Authorization = \`Bearer \${newToken}\`;
        return api(originalRequest);
      } catch (refreshError) {
        clearAuthState();
        window.location.href = '/login';
        return Promise.reject(refreshError);
      } finally {
        isRefreshing = false;
      }
    }
    
    return Promise.reject(error);
  }
);

export default api;
`;

console.log('\n=== Axios 拦截器实现 ===');
console.log(axiosInterceptorExample);

// 3. 后端实现（Node.js/Express）
const backendExample = `
const express = require('express');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');

const app = express();
app.use(cookieParser());
app.use(express.json());

const ACCESS_TOKEN_SECRET = 'your-access-secret';
const REFRESH_TOKEN_SECRET = 'your-refresh-secret';
const refreshTokens = new Set();

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  
  if (validateUser(username, password)) {
    const user = getUser(username);
    
    const accessToken = jwt.sign(
      { userId: user.id, username: user.username, role: user.role },
      ACCESS_TOKEN_SECRET,
      { expiresIn: '15m' }
    );
    
    const refreshToken = jwt.sign(
      { userId: user.id },
      REFRESH_TOKEN_SECRET,
      { expiresIn: '7d' }
    );
    
    refreshTokens.add(refreshToken);
    
    res.cookie('refresh_token', refreshToken, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'Strict',
      maxAge: 7 * 24 * 60 * 60 * 1000,
      path: '/api/auth/refresh'
    });
    
    res.json({ access_token: accessToken, user });
  } else {
    res.status(401).json({ error: 'Invalid credentials' });
  }
});

app.post('/api/auth/refresh', (req, res) => {
  const refreshToken = req.cookies.refresh_token;
  
  if (!refreshToken || !refreshTokens.has(refreshToken)) {
    return res.status(401).json({ error: 'Invalid refresh token' });
  }
  
  try {
    const decoded = jwt.verify(refreshToken, REFRESH_TOKEN_SECRET);
    const user = getUserById(decoded.userId);
    
    const accessToken = jwt.sign(
      { userId: user.id, username: user.username, role: user.role },
      ACCESS_TOKEN_SECRET,
      { expiresIn: '15m' }
    );
    
    res.json({ access_token: accessToken });
  } catch (error) {
    res.status(401).json({ error: 'Invalid refresh token' });
  }
});

app.post('/api/logout', (req, res) => {
  const refreshToken = req.cookies.refresh_token;
  if (refreshToken) {
    refreshTokens.delete(refreshToken);
  }
  res.clearCookie('refresh_token');
  res.json({ success: true });
});

const authMiddleware = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  const token = authHeader.substring(7);
  try {
    const decoded = jwt.verify(token, ACCESS_TOKEN_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
};

app.get('/api/user', authMiddleware, (req, res) => {
  res.json(req.user);
});

app.listen(3000);
`;

console.log('\n=== 后端实现 ===');
console.log(backendExample);

// 4. 微服务架构认证
const microserviceAuth = {
  架构: [
    '用户 → API Gateway → 服务A/服务B/服务C',
    'API Gateway 统一认证',
    '服务间通过内部 Token 通信'
  ],
  方案: [
    {
      名称: 'Gateway 认证 + JWT 透传',
      说明: 'Gateway 验证 Token，解析用户信息，传递给下游服务',
      优点: '服务不需要认证逻辑',
      缺点: '依赖 Gateway'
    },
    {
      名称: '每个服务独立认证',
      说明: '每个服务自己验证 JWT',
      优点: '解耦',
      缺点: '重复代码'
    },
    {
      名称: '共享认证服务',
      说明: '独立的认证服务，其他服务调用验证',
      优点: '统一管理',
      缺点: '多一次网络调用'
    }
  ]
};

console.log('\n=== 微服务架构认证 ===');
console.log('架构:', microserviceAuth.架构);
microserviceAuth.方案.forEach((s, i) => {
  console.log(`\n方案 ${i + 1}: ${s.名称}`);
  console.log(`  说明: ${s.说明}`);
  console.log(`  优点: ${s.优点}`);
  console.log(`  缺点: ${s.缺点}`);
});

// 5. 第三方登录流程（GitHub）
const githubLoginFlow = [
  '1. 用户点击"使用 GitHub 登录"',
  '2. 前端跳转: https://github.com/login/oauth/authorize?client_id=xxx&redirect_uri=xxx&scope=user&state=xxx',
  '3. 用户在 GitHub 授权',
  '4. GitHub 重定向回: https://your-app.com/callback?code=xxx&state=xxx',
  '5. 前端将 code 发送给后端',
  '6. 后端 POST https://github.com/login/oauth/access_token { client_id, client_secret, code }',
  '7. GitHub 返回 access_token',
  '8. 后端 GET https://api.github.com/user (Authorization: Bearer xxx)',
  '9. 获取用户信息',
  '10. 查找或创建用户',
  '11. 生成自己的 JWT',
  '12. 返回给前端'
];

console.log('\n=== GitHub 登录流程 ===');
githubLoginFlow.forEach((step, i) => console.log(`${i + 1}. ${step}`));

// 6. 多设备登录管理
const multiDeviceManagement = {
  功能: [
    '查看已登录设备',
    '设备信息（IP、User-Agent、位置、登录时间）',
    '远程登出指定设备',
    '登出所有其他设备',
    '新设备登录通知'
  ],
  实现: {
    存储: 'Redis/数据库存储活跃会话',
    字段: 'userId, deviceId, deviceInfo, ip, location, lastActive, createdAt',
    验证: '每次请求更新 lastActive',
    清理: '定期清理过期会话'
  }
};

console.log('\n=== 多设备登录管理 ===');
console.log('功能:', multiDeviceManagement.功能);
console.log('实现:', multiDeviceManagement.实现);
