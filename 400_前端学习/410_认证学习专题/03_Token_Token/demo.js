// Token 认证示例代码

// 1. 简单 Token 生成器
function generateToken() {
  const random = Math.random().toString(36).substring(2, 15) + 
                 Math.random().toString(36).substring(2, 15);
  const timestamp = Date.now().toString(36);
  return `tk_${timestamp}_${random}`;
}

console.log('=== Token 生成 ===');
const token1 = generateToken();
const token2 = generateToken();
console.log('Token 1:', token1);
console.log('Token 2:', token2);

// 2. Token 管理器
class TokenManager {
  constructor() {
    this.tokens = new Map();
  }

  createToken(userId, data = {}) {
    const token = generateToken();
    const tokenData = {
      userId,
      data,
      createdAt: new Date(),
      expiresAt: new Date(Date.now() + 24 * 60 * 60 * 1000)
    };
    this.tokens.set(token, tokenData);
    console.log(`✅ 为用户 ${userId} 创建Token`);
    return token;
  }

  verifyToken(token) {
    const tokenData = this.tokens.get(token);
    if (!tokenData) {
      return { valid: false, error: 'Token不存在' };
    }
    if (new Date() > tokenData.expiresAt) {
      this.tokens.delete(token);
      return { valid: false, error: 'Token已过期' };
    }
    return { valid: true, data: tokenData };
  }

  revokeToken(token) {
    this.tokens.delete(token);
    console.log('❌ Token已撤销');
  }

  cleanupExpiredTokens() {
    const now = new Date();
    for (const [token, data] of this.tokens) {
      if (now > data.expiresAt) {
        this.tokens.delete(token);
      }
    }
  }
}

console.log('\n=== Token 管理器 ===');
const tokenManager = new TokenManager();
const userToken = tokenManager.createToken(1, { username: '张三', role: 'admin' });
console.log('创建的Token:', userToken);
console.log('验证Token:', tokenManager.verifyToken(userToken));
console.log('验证无效Token:', tokenManager.verifyToken('invalid_token'));

// 3. 客户端 Token 存储
class ClientTokenStorage {
  constructor(storageType = 'localStorage') {
    this.storageType = storageType;
    this.tokenKey = 'auth_token';
  }

  getStorage() {
    switch (this.storageType) {
      case 'localStorage':
        return typeof localStorage !== 'undefined' ? localStorage : null;
      case 'sessionStorage':
        return typeof sessionStorage !== 'undefined' ? sessionStorage : null;
      default:
        return null;
    }
  }

  saveToken(token) {
    const storage = this.getStorage();
    if (storage) {
      storage.setItem(this.tokenKey, token);
      console.log('✅ Token已保存到', this.storageType);
    }
  }

  getToken() {
    const storage = this.getStorage();
    return storage ? storage.getItem(this.tokenKey) : null;
  }

  removeToken() {
    const storage = this.getStorage();
    if (storage) {
      storage.removeItem(this.tokenKey);
      console.log('❌ Token已从', this.storageType, '移除');
    }
  }
}

console.log('\n=== 客户端 Token 存储 ===');
const localStorageToken = new ClientTokenStorage('localStorage');
const sessionStorageToken = new ClientTokenStorage('sessionStorage');

// 4. Token 认证流程
function tokenAuthWorkflow() {
  console.log('\n=== Token 认证流程 ===');
  
  const steps = [
    '1. 用户 POST /login { username, password }',
    '2. 服务器验证凭证',
    '3. 服务器生成 Token',
    '4. 返回 { token: "xxx" }',
    '5. 客户端存储 Token',
    '6. 请求受保护资源: GET /api/data',
    '7. 客户端添加 Header: Authorization: Bearer xxx',
    '8. 服务器验证 Token',
    '9. 验证通过，返回数据'
  ];
  
  steps.forEach(step => console.log(step));
}

tokenAuthWorkflow();

// 5. 前端请求封装（带 Token）
class AuthRequest {
  constructor(baseURL, tokenStorage) {
    this.baseURL = baseURL;
    this.tokenStorage = tokenStorage;
  }

  async request(url, options = {}) {
    const token = this.tokenStorage.getToken();
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers
    };
    
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    
    try {
      const response = await fetch(this.baseURL + url, {
        ...options,
        headers
      });
      
      if (response.status === 401) {
        this.tokenStorage.removeToken();
        console.log('❌ Token无效，已清除');
      }
      
      return response;
    } catch (error) {
      console.error('请求错误:', error);
      throw error;
    }
  }

  get(url) {
    return this.request(url, { method: 'GET' });
  }

  post(url, data) {
    return this.request(url, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }
}

console.log('\n=== 前端请求封装 ===');
console.log('使用示例:');
console.log(`
const tokenStorage = new ClientTokenStorage();
const api = new AuthRequest('https://api.example.com', tokenStorage);
api.get('/users').then(res => res.json());
`);

// 6. Token 存储方式对比
const storageComparison = {
  localStorage: {
    持久化: '是',
    容量: '~5MB',
    XSS风险: '高',
    CSRF风险: '无',
    自动发送: '否',
    适用: '非敏感数据'
  },
  sessionStorage: {
    持久化: '否（标签页关闭清除）',
    容量: '~5MB',
    XSS风险: '高',
    CSRF风险: '无',
    自动发送: '否',
    适用: '临时会话'
  },
  'Cookie (HttpOnly)': {
    持久化: '可配置',
    容量: '~4KB',
    XSS风险: '低',
    CSRF风险: '有',
    自动发送: '是',
    适用: '认证Token（推荐）'
  },
  '内存变量': {
    持久化: '否（刷新丢失）',
    容量: '无限制',
    XSS风险: '中',
    CSRF风险: '无',
    自动发送: '否',
    适用: '配合刷新Token'
  }
};

console.log('\n=== Token 存储方式对比 ===');
console.log('          localStorage  sessionStorage  Cookie(HttpOnly)  内存变量');
console.log('持久化:     ✓           ✗               ✓              ✗');
console.log('XSS风险:    高           高               低              中');
console.log('CSRF风险:   无           无               有              无');
console.log('自动发送:   否           否               是              否');

// 7. Token 安全最佳实践
const tokenSecurity = [
  '🔒 始终使用 HTTPS 传输 Token',
  '⏰ 设置合理的过期时间（15分钟-2小时）',
  '🔄 实现刷新 Token 机制',
  '📱 安全存储 Token（HttpOnly Cookie 优先）',
  '🚫 不要在 URL 中传递 Token',
  '📋 实现 Token 撤销机制',
  '🔍 验证 Token 完整性',
  '⚠️  检测异常使用（如异地登录）'
];

console.log('\n=== Token 安全最佳实践 ===');
tokenSecurity.forEach(tip => console.log(tip));

// 8. 刷新 Token 机制
function refreshTokenFlow() {
  console.log('\n=== 刷新 Token 机制 ===');
  
  const flow = [
    '1. 登录时返回 access_token 和 refresh_token',
    '2. access_token: 有效期短（15分钟），用于API请求',
    '3. refresh_token: 有效期长（7天），用于刷新',
    '4. access_token 过期后',
    '5. 使用 refresh_token 请求 /refresh',
    '6. 获取新的 access_token',
    '7. refresh_token 过期需要重新登录'
  ];
  
  flow.forEach(step => console.log(step));
}

refreshTokenFlow();
