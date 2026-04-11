// Session 会话示例代码

// 1. 简单的 Session 实现
class SimpleSessionStore {
  constructor() {
    this.sessions = new Map();
    this.sessionTimeout = 30 * 60 * 1000;
  }

  generateSessionId() {
    return 'sess_' + Date.now().toString(36) + '_' + 
           Math.random().toString(36).substring(2, 15);
  }

  createSession(data = {}) {
    const sessionId = this.generateSessionId();
    const session = {
      id: sessionId,
      data: { ...data },
      createdAt: new Date(),
      lastAccessedAt: new Date(),
      expiresAt: new Date(Date.now() + this.sessionTimeout)
    };
    this.sessions.set(sessionId, session);
    console.log(`✅ 创建 Session: ${sessionId}`);
    return sessionId;
  }

  getSession(sessionId) {
    const session = this.sessions.get(sessionId);
    if (!session) {
      return null;
    }
    if (new Date() > session.expiresAt) {
      this.destroySession(sessionId);
      return null;
    }
    session.lastAccessedAt = new Date();
    session.expiresAt = new Date(Date.now() + this.sessionTimeout);
    return session;
  }

  updateSession(sessionId, data) {
    const session = this.sessions.get(sessionId);
    if (session) {
      session.data = { ...session.data, ...data };
      session.lastAccessedAt = new Date();
      console.log(`✅ 更新 Session: ${sessionId}`);
      return true;
    }
    return false;
  }

  destroySession(sessionId) {
    this.sessions.delete(sessionId);
    console.log(`❌ 销毁 Session: ${sessionId}`);
  }

  cleanupExpiredSessions() {
    const now = new Date();
    for (const [sessionId, session] of this.sessions) {
      if (now > session.expiresAt) {
        this.sessions.delete(sessionId);
      }
    }
  }

  getActiveSessionCount() {
    this.cleanupExpiredSessions();
    return this.sessions.size;
  }
}

console.log('=== Session 存储 ===');
const sessionStore = new SimpleSessionStore();
const sessionId = sessionStore.createSession({ 
  userId: 1, 
  username: '张三',
  role: 'admin'
});
console.log('Session ID:', sessionId);
console.log('获取 Session:', sessionStore.getSession(sessionId));
console.log('活跃会话数:', sessionStore.getActiveSessionCount());

// 2. Session 存储方式对比
const sessionStorageOptions = {
  '内存存储': {
    优点: '简单快速',
    缺点: '重启丢失，多实例不共享',
    适用: '开发环境'
  },
  'Redis': {
    优点: '高性能，支持过期，可共享',
    缺点: '需要额外服务',
    适用: '生产环境推荐'
  },
  '数据库': {
    优点: '持久化，可查询',
    缺点: '性能较低',
    适用: '小流量应用'
  },
  '文件存储': {
    优点: '简单',
    缺点: '性能差，不共享',
    适用: '不推荐'
  }
};

console.log('\n=== Session 存储方式 ===');
Object.entries(sessionStorageOptions).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  优点: ${info.优点}`);
  console.log(`  缺点: ${info.缺点}`);
  console.log(`  适用: ${info.适用}`);
});

// 3. Express + Session 完整示例
const expressSessionExample = `
// server.js
const express = require('express');
const session = require('express-session');
const RedisStore = require('connect-redis').default;
const { createClient } = require('redis');

const app = express();

const redisClient = createClient({
  url: 'redis://localhost:6379'
});
redisClient.connect().catch(console.error);

app.use(session({
  secret: 'your-secret-key-change-in-production',
  resave: false,
  saveUninitialized: false,
  store: new RedisStore({ client: redisClient }),
  cookie: {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'Strict',
    maxAge: 30 * 60 * 1000
  }
}));

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  if (validateUser(username, password)) {
    req.session.userId = getUserId(username);
    req.session.username = username;
    req.session.role = getUserRole(username);
    
    res.json({ success: true, user: req.session });
  } else {
    res.status(401).json({ error: '登录失败' });
  }
});

app.get('/user', (req, res) => {
  if (req.session.userId) {
    res.json({
      userId: req.session.userId,
      username: req.session.username,
      role: req.session.role
    });
  } else {
    res.status(401).json({ error: '未登录' });
  }
});

app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      res.status(500).json({ error: '登出失败' });
    } else {
      res.clearCookie('connect.sid');
      res.json({ success: true });
    }
  });
});

app.listen(3000);
`;

console.log('\n=== Express Session 示例 ===');
console.log(expressSessionExample);

// 4. Session 安全最佳实践
const sessionSecurity = [
  '🔐 SessionID 使用强随机数生成',
  '🍪 Cookie 设置 HttpOnly',
  '🔒 Cookie 设置 Secure（生产环境）',
  '🛡️  Cookie 设置 SameSite=Strict',
  '⏰ 设置合理的过期时间',
  '🔄 登录成功后重新生成 SessionID',
  '❌ 登出时销毁 Session',
  '📊 使用 Redis 存储 Session',
  '📝 记录 Session 活动日志'
];

console.log('\n=== Session 安全最佳实践 ===');
sessionSecurity.forEach(tip => console.log(tip));

// 5. Session 固定攻击防护
function sessionFixationProtection() {
  console.log('\n=== Session 固定攻击防护 ===');
  
  const protectionMeasures = [
    '1. 登录成功后重新生成 SessionID',
    '2. 权限变更时重新生成 SessionID',
    '3. 设置合理的 Session 过期时间',
    '4. 检测异常的 IP/User-Agent 变化',
    '5. 实现 Session 超时自动销毁'
  ];
  
  protectionMeasures.forEach(measure => console.log(measure));
}

sessionFixationProtection();

// 6. Session vs JWT 对比
const sessionVsJWT = {
  'Session': {
    状态: '有状态',
    服务器存储: '需要',
    扩展性: '一般（需要共享存储）',
    撤销: '容易',
    适用: '传统Web应用'
  },
  'JWT': {
    状态: '无状态',
    服务器存储: '不需要',
    扩展性: '好',
    撤销: '困难',
    适用: 'SPA、微服务'
  }
};

console.log('\n=== Session vs JWT ===');
console.log('          Session        JWT');
console.log(`状态:     有状态         无状态`);
console.log(`存储:     需要           不需要`);
console.log(`扩展性:   一般           好`);
console.log(`撤销:     容易           困难`);

// 7. Session 常见问题
const commonIssues = [
  {
    问题: 'Session 丢失',
    原因: '服务器重启、Cookie 被清除、过期',
    解决: '使用 Redis 存储、检查 Cookie 设置'
  },
  {
    问题: '多实例 Session 不共享',
    原因: '内存存储，实例间不共享',
    解决: '使用 Redis 或数据库存储'
  },
  {
    问题: 'Session 被劫持',
    原因: 'XSS、CSRF 攻击',
    解决: 'HttpOnly、SameSite、HTTPS'
  }
];

console.log('\n=== Session 常见问题 ===');
commonIssues.forEach((issue, i) => {
  console.log(`\n${i + 1}. ${issue.问题}`);
  console.log(`   原因: ${issue.原因}`);
  console.log(`   解决: ${issue.解决}`);
});
