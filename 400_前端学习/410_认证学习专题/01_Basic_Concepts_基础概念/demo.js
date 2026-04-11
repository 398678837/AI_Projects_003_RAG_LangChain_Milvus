// 认证基础概念示例代码

// 1. 认证 vs 授权
const authComparison = {
  认证_Authentication: {
    定义: '验证用户身份',
    问题: '你是谁？',
    示例: '登录验证用户名密码',
    方式: '密码、指纹、人脸识别'
  },
  授权_Authorization: {
    定义: '验证用户权限',
    问题: '你能做什么？',
    示例: '管理员可以删除用户',
    方式: '角色、权限列表'
  }
};

console.log('=== 认证 vs 授权 ===');
Object.entries(authComparison).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  定义: ${info.定义}`);
  console.log(`  问题: ${info.问题}`);
  console.log(`  示例: ${info.示例}`);
  console.log(`  方式: ${info.方式}`);
});

// 2. 常见认证方式对比
const authMethods = {
  'Cookie + Session': {
    特点: '服务器存储状态，客户端存SessionID',
    优点: '简单易用，服务器可控',
    缺点: '扩展性差，CSRF风险',
    适用: '传统Web应用'
  },
  Token: {
    特点: '无状态，客户端存储',
    优点: '扩展性好，跨平台',
    缺点: '令牌撤销困难',
    适用: 'SPA、移动应用'
  },
  JWT: {
    特点: '自包含，可验证',
    优点: '无需查库，可传递数据',
    缺点: 'payload不能过大',
    适用: '微服务、分布式'
  },
  OAuth2: {
    特点: '第三方授权',
    优点: '无需分享密码',
    缺点: '流程复杂',
    适用: '第三方登录（微信、GitHub）'
  }
};

console.log('\n=== 常见认证方式 ===');
Object.entries(authMethods).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  特点: ${info.特点}`);
  console.log(`  优点: ${info.优点}`);
  console.log(`  缺点: ${info.缺点}`);
  console.log(`  适用: ${info.适用}`);
});

// 3. 认证流程演示
function authWorkflow() {
  console.log('\n=== 认证流程 ===');
  
  const steps = [
    '1. 用户访问受保护资源',
    '2. 服务器返回401未授权',
    '3. 用户跳转到登录页',
    '4. 用户输入用户名密码',
    '5. 服务器验证凭证',
    '6. 验证成功，颁发令牌',
    '7. 客户端存储令牌',
    '8. 后续请求携带令牌',
    '9. 服务器验证令牌',
    '10. 返回受保护资源'
  ];
  
  steps.forEach((step, i) => console.log(`${i + 1}. ${step}`));
}

authWorkflow();

// 4. 基本认证术语
const authTerms = {
  凭证_Credentials: '用于验证身份的信息（密码、令牌等）',
  令牌_Token: '代表用户身份的字符串',
  会话_Session: '服务器存储的用户状态',
  签名_Signature: '验证数据完整性的加密值',
  过期时间_Expiration: '令牌失效时间',
  刷新令牌_RefreshToken: '用于获取新的访问令牌',
  作用域_Scope: '令牌的权限范围',
  签发者_Issuer: '签发令牌的服务器'
};

console.log('\n=== 认证术语 ===');
Object.entries(authTerms).forEach(([term, desc]) => {
  console.log(`  ${term}: ${desc}`);
});

// 5. 简单的用户认证模拟
class SimpleAuth {
  constructor() {
    this.users = new Map();
    this.users.set('admin', { password: 'admin123', role: 'admin' });
    this.users.set('user', { password: 'user123', role: 'user' });
  }

  login(username, password) {
    const user = this.users.get(username);
    if (user && user.password === password) {
      console.log(`✅ ${username} 登录成功，角色: ${user.role}`);
      return { success: true, user: { username, role: user.role } };
    }
    console.log(`❌ ${username} 登录失败`);
    return { success: false, error: '用户名或密码错误' };
  }

  checkPermission(user, requiredRole) {
    const roles = { user: 1, admin: 2 };
    return roles[user.role] >= roles[requiredRole];
  }
}

console.log('\n=== 简单认证模拟 ===');
const auth = new SimpleAuth();
const adminLogin = auth.login('admin', 'admin123');
const userLogin = auth.login('user', 'user123');
const wrongLogin = auth.login('admin', 'wrongpassword');

if (adminLogin.success) {
  console.log('管理员权限检查:', auth.checkPermission(adminLogin.user, 'admin'));
}

// 6. 安全最佳实践
const securityTips = [
  '🔒 始终使用HTTPS传输凭证',
  '🔑 密码需要加盐哈希存储',
  '⏰ 设置合理的令牌过期时间',
  '📱 安全存储客户端令牌',
  '🚫 不要在URL中传递敏感信息',
  '🔄 使用刷新令牌机制',
  '📋 实现权限最小化原则',
  '📝 记录登录和操作日志'
];

console.log('\n=== 安全最佳实践 ===');
securityTips.forEach(tip => console.log(tip));

// 7. 认证方案选择决策树
function chooseAuthMethod(scenario) {
  const decisions = {
    '传统Web应用': 'Cookie + Session',
    'SPA单页应用': 'Token/JWT',
    '移动App': 'Token/JWT',
    '微服务架构': 'JWT',
    '第三方登录': 'OAuth2',
    '企业内部系统': 'Cookie + Session 或 SSO'
  };
  return decisions[scenario] || '根据具体情况分析';
}

console.log('\n=== 认证方案选择 ===');
const scenarios = ['传统Web应用', 'SPA单页应用', '移动App', '微服务架构', '第三方登录'];
scenarios.forEach(s => {
  console.log(`  ${s} → ${chooseAuthMethod(s)}`);
});
