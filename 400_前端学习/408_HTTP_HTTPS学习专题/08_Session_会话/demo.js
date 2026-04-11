// Session 会话示例代码

// 1. Session 与 Cookie 对比
const sessionVsCookie = {
  存储位置: {
    Session: '服务器端',
    Cookie: '客户端（浏览器）'
  },
  安全性: {
    Session: '较高，数据不在客户端',
    Cookie: '较低，数据可被查看/修改'
  },
  存储容量: {
    Session: '较大（取决于服务器）',
    Cookie: '较小（每个约4KB）'
  },
  性能: {
    Session: '稍低（需要服务器查询）',
    Cookie: '较高（直接在客户端）'
  },
  有效期: {
    Session: '默认会话结束（关闭浏览器）',
    Cookie: '可设置过期时间'
  },
  典型用途: {
    Session: '登录状态、购物车',
    Cookie: '记住我、主题设置'
  }
};

console.log('Session vs Cookie:', sessionVsCookie);

// 2. 模拟Session存储（服务器端）
class SessionStore {
  constructor() {
    this.sessions = new Map();
  }

  createSession(userId, userData) {
    const sessionId = this.generateSessionId();
    const session = {
      id: sessionId,
      userId: userId,
      data: userData,
      createdAt: new Date(),
      expiresAt: new Date(Date.now() + 24 * 60 * 60 * 1000)
    };
    this.sessions.set(sessionId, session);
    console.log('创建Session:', sessionId);
    return sessionId;
  }

  getSession(sessionId) {
    const session = this.sessions.get(sessionId);
    if (!session) {
      return null;
    }
    if (new Date() > session.expiresAt) {
      this.sessions.delete(sessionId);
      return null;
    }
    return session;
  }

  updateSession(sessionId, data) {
    const session = this.sessions.get(sessionId);
    if (session) {
      session.data = { ...session.data, ...data };
      session.expiresAt = new Date(Date.now() + 24 * 60 * 60 * 1000);
      return session;
    }
    return null;
  }

  deleteSession(sessionId) {
    this.sessions.delete(sessionId);
    console.log('删除Session:', sessionId);
  }

  generateSessionId() {
    return 'sess_' + Math.random().toString(36).substring(2, 15) + 
           Math.random().toString(36).substring(2, 15);
  }

  cleanupExpiredSessions() {
    const now = new Date();
    for (const [id, session] of this.sessions) {
      if (now > session.expiresAt) {
        this.sessions.delete(id);
      }
    }
  }
}

// 3. 模拟Session管理器
class SessionManager {
  constructor() {
    this.sessionStore = new SessionStore();
  }

  login(userId, username) {
    const sessionId = this.sessionStore.createSession(userId, {
      username: username,
      loginTime: new Date(),
      isLoggedIn: true
    });
    console.log(`${username} 登录成功，Session ID: ${sessionId}`);
    return sessionId;
  }

  logout(sessionId) {
    this.sessionStore.deleteSession(sessionId);
    console.log('登出成功');
  }

  getUser(sessionId) {
    const session = this.sessionStore.getSession(sessionId);
    if (session) {
      return session.data;
    }
    return null;
  }

  isLoggedIn(sessionId) {
    const user = this.getUser(sessionId);
    return user && user.isLoggedIn;
  }

  updateUser(sessionId, data) {
    return this.sessionStore.updateSession(sessionId, data);
  }
}

// 4. 使用示例
console.log('\n=== Session 使用示例 ===');

const sessionManager = new SessionManager();

// 用户1登录
const sessionId1 = sessionManager.login(1, '张三');
console.log('用户1信息:', sessionManager.getUser(sessionId1));
console.log('用户1是否登录:', sessionManager.isLoggedIn(sessionId1));

// 用户2登录
const sessionId2 = sessionManager.login(2, '李四');
console.log('用户2信息:', sessionManager.getUser(sessionId2));

// 更新用户信息
sessionManager.updateUser(sessionId1, { theme: 'dark', language: 'zh-CN' });
console.log('更新后用户1信息:', sessionManager.getUser(sessionId1));

// 用户1登出
sessionManager.logout(sessionId1);
console.log('登出后用户1是否登录:', sessionManager.isLoggedIn(sessionId1));

// 5. Session 工作流程
console.log('\n=== Session 工作流程 ===');
const sessionWorkflow = [
  '1. 用户访问网站',
  '2. 服务器创建Session，生成Session ID',
  '3. 服务器通过Set-Cookie头将Session ID发给浏览器',
  '4. 浏览器保存Session ID到Cookie',
  '5. 用户后续请求时，浏览器自动带上Session ID',
  '6. 服务器通过Session ID找到对应的Session数据',
  '7. 用户登出或过期时，删除Session'
];

sessionWorkflow.forEach(step => console.log(step));

// 6. Session 安全最佳实践
const sessionSecurity = {
  SessionID: '使用足够长且随机的Session ID',
  HTTPS: '始终使用HTTPS传输Session ID',
  HttpOnly: '设置HttpOnly防止XSS',
  SameSite: '设置SameSite防止CSRF',
  过期时间: '设置合理的过期时间',
  重新生成: '登录后重新生成Session ID',
  敏感数据: '不要在Session中存储密码等敏感数据'
};

console.log('\nSession 安全最佳实践:', sessionSecurity);

// 7. 会话固定攻击防护
console.log('\n=== 会话固定攻击防护 ===');
function preventSessionFixation(sessionManager, oldSessionId, userId, username) {
  console.log('旧Session ID:', oldSessionId);
  if (oldSessionId) {
    sessionManager.logout(oldSessionId);
  }
  const newSessionId = sessionManager.login(userId, username);
  console.log('新Session ID:', newSessionId);
  return newSessionId;
}

// 8. Session 存储方式对比
const sessionStorageTypes = {
  内存存储: {
    优点: '速度快',
    缺点: '重启丢失，多机无法共享',
    适用: '开发环境，单机部署'
  },
  文件存储: {
    优点: '持久化，简单',
    缺点: '速度较慢，I/O开销',
    适用: '小型应用'
  },
  数据库存储: {
    优点: '持久化，可查询',
    缺点: '速度一般，有数据库开销',
    适用: '中型应用'
  },
  Redis存储: {
    优点: '速度快，支持过期，可共享',
    缺点: '需要额外部署Redis',
    适用: '生产环境，推荐'
  }
};

console.log('\nSession 存储方式对比:', sessionStorageTypes);

// 9. 带购物车的Session示例
console.log('\n=== 购物车示例 ===');

class ShoppingCartSession {
  constructor(sessionManager) {
    this.sessionManager = sessionManager;
  }

  addToCart(sessionId, product) {
    const user = this.sessionManager.getUser(sessionId);
    if (!user) {
      console.log('请先登录');
      return;
    }
    
    if (!user.cart) {
      user.cart = [];
    }
    user.cart.push(product);
    this.sessionManager.updateUser(sessionId, { cart: user.cart });
    console.log('已添加到购物车:', product.name);
  }

  getCart(sessionId) {
    const user = this.sessionManager.getUser(sessionId);
    return user?.cart || [];
  }

  getCartTotal(sessionId) {
    const cart = this.getCart(sessionId);
    return cart.reduce((total, item) => total + item.price, 0);
  }
}

const cartSession = new ShoppingCartSession(sessionManager);
const cartSessionId = sessionManager.login(3, '王五');
cartSession.addToCart(cartSessionId, { id: 1, name: '商品A', price: 100 });
cartSession.addToCart(cartSessionId, { id: 2, name: '商品B', price: 200 });
console.log('购物车内容:', cartSession.getCart(cartSessionId));
console.log('购物车总价:', cartSession.getCartTotal(cartSessionId));
