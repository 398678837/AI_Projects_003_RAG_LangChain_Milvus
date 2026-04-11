// 认证最佳实践示例代码

// 1. 认证方案选择决策树
function chooseAuthSolution(scenario) {
  const solutions = {
    '传统Web应用（PHP/Java/.NET）': {
      方案: 'Cookie + Session + Redis',
      理由: '成熟稳定，服务器可控',
      推荐: '⭐⭐⭐⭐⭐'
    },
    'SPA单页应用（React/Vue/Angular）': {
      方案: 'JWT + Refresh Token',
      理由: '无状态，跨平台',
      推荐: '⭐⭐⭐⭐'
    },
    '移动App（iOS/Android/Flutter）': {
      方案: 'JWT + Refresh Token + Keychain',
      理由: '安全存储，长期登录',
      推荐: '⭐⭐⭐⭐'
    },
    '微服务架构': {
      方案: 'JWT + API Gateway',
      理由: '分布式，统一认证',
      推荐: '⭐⭐⭐⭐⭐'
    },
    '企业内部系统': {
      方案: 'SSO（SAML/OIDC）',
      理由: '统一登录，用户体验好',
      推荐: '⭐⭐⭐⭐⭐'
    },
    '第三方登录': {
      方案: 'OAuth2 + OpenID Connect',
      理由: '无需分享密码',
      推荐: '⭐⭐⭐⭐'
    }
  };
  return solutions[scenario] || { 方案: '根据具体情况分析', 理由: '', 推荐: '' };
}

console.log('=== 认证方案选择 ===');
const scenarios = ['传统Web应用（PHP/Java/.NET）', 'SPA单页应用（React/Vue/Angular）', '移动App（iOS/Android/Flutter）', '微服务架构', '企业内部系统'];
scenarios.forEach(s => {
  const solution = chooseAuthSolution(s);
  console.log(`\n【${s}】`);
  console.log(`  方案: ${solution.方案}`);
  console.log(`  理由: ${solution.理由}`);
  console.log(`  推荐: ${solution.推荐}`);
});

// 2. 安全设计原则
const securityPrinciples = [
  {
    原则: '最小权限原则',
    说明: '用户只拥有完成任务所需的最小权限',
    实践: 'RBAC角色权限控制，细粒度权限管理'
  },
  {
    原则: '纵深防御',
    说明: '多层防护，一层失效还有其他层',
    实践: 'HTTPS + HttpOnly Cookie + CSRF Token + CSP'
  },
  {
    原则: '不要重复造轮子',
    说明: '使用成熟的库和框架，不要自己实现加密算法',
    实践: '使用 bcrypt、jsonwebtoken、Passport.js'
  },
  {
    原则: '默认安全',
    说明: '安全选项默认开启，而不是需要手动配置',
    实践: '默认启用 HSTS、CSP、SameSite=Strict'
  },
  {
    原则: '失效安全',
    说明: '系统失败时保持安全状态',
    实践: '认证失败时拒绝访问，而不是默认允许'
  },
  {
    原则: '公开设计',
    说明: '安全不依赖于算法保密，只依赖于密钥',
    实践: '使用公开的标准算法（AES、RSA、SHA-256）'
  }
];

console.log('\n=== 安全设计原则 ===');
securityPrinciples.forEach((p, i) => {
  console.log(`\n${i + 1}. ${p.原则}`);
  console.log(`   说明: ${p.说明}`);
  console.log(`   实践: ${p.实践}`);
});

// 3. 完整的认证系统架构
const authSystemArchitecture = {
  '1. 接入层': [
    'HTTPS 加密',
    'WAF 防火墙',
    'CDN 加速',
    '负载均衡'
  ],
  '2. 网关层': [
    'API Gateway',
    '认证拦截',
    '权限校验',
    '限流熔断'
  ],
  '3. 认证服务': [
    '登录/注册',
    'Token 签发',
    'Session 管理',
    'MFA 验证'
  ],
  '4. 用户服务': [
    '用户信息',
    '角色权限',
    '密码管理',
    '审计日志'
  ],
  '5. 存储层': [
    '用户数据库',
    'Session Redis',
    'Token 黑名单',
    '日志存储'
  ],
  '6. 第三方集成': [
    'OAuth2 提供商',
    '短信服务',
    '邮件服务',
    '验证码服务'
  ]
};

console.log('\n=== 认证系统架构 ===');
Object.entries(authSystemArchitecture).forEach(([layer, components]) => {
  console.log(`\n${layer}:`);
  components.forEach(c => console.log(`  - ${c}`));
});

// 4. 认证流程最佳实践
const authFlowBestPractices = {
  '登录流程': [
    '✅ 显示登录尝试次数',
    '✅ 失败时不要提示"用户名不存在"',
    '✅ 实现速率限制',
    '✅ 支持验证码',
    '✅ 支持"记住我"',
    '✅ HTTPS 传输'
  ],
  '注册流程': [
    '✅ 邮箱/手机号验证',
    '✅ 密码强度提示',
    '✅ 确认密码',
    '✅ 服务条款',
    '✅ 发送欢迎邮件'
  ],
  '密码重置': [
    '✅ 发送带有时效 token 的链接',
    '✅ token 一次性使用',
    '✅ 设置过期时间（1小时）',
    '✅ 重置后失效所有会话',
    '✅ 通知用户密码已更改'
  ],
  '登出流程': [
    '✅ 清除 Cookie',
    '✅ 销毁 Session',
    '✅ 加入 Token 黑名单',
    '✅ 重定向到登录页'
  ]
};

console.log('\n=== 认证流程最佳实践 ===');
Object.entries(authFlowBestPractices).forEach(([flow, practices]) => {
  console.log(`\n【${flow}】`);
  practices.forEach(p => console.log(`  ${p}`));
});

// 5. 不要做的事情
const dontDoList = [
  '❌ 不要自己实现加密算法',
  '❌ 不要在客户端存储密码',
  '❌ 不要用明文传输密码',
  '❌ 不要在 URL 中传递 Token',
  '❌ 不要在 JWT payload 存敏感数据',
  '❌ 不要关闭 HttpOnly',
  '❌ 不要使用弱随机数生成 SessionID',
  '❌ 不要永久保存 Session',
  '❌ 不要忽略安全更新',
  '❌ 不要只依赖单一认证方式'
];

console.log('\n=== 不要做的事情 ===');
dontDoList.forEach(item => console.log(item));

// 6. 推荐的库和工具
const recommendedLibraries = {
  'Node.js': [
    'bcrypt / argon2 - 密码哈希',
    'jsonwebtoken / jose - JWT',
    'express-session + connect-redis - Session',
    'passport.js - 认证中间件',
    'helmet - 安全头'
  ],
  'Java': [
    'Spring Security',
    'JJWT / Nimbus JOSE+JWT',
    'Spring Session'
  ],
  'Python': [
    'bcrypt / argon2-cffi',
    'PyJWT / authlib',
    'Flask-Login / Django Auth'
  ],
  '前端': [
    'jose - JWT 验证',
    'js-cookie - Cookie 操作',
    'store.js - 存储封装'
  ]
};

console.log('\n=== 推荐的库和工具 ===');
Object.entries(recommendedLibraries).forEach(([platform, libs]) => {
  console.log(`\n【${platform}】`);
  libs.forEach(lib => console.log(`  - ${lib}`));
});

// 7. 测试清单
const testingChecklist = [
  '✅ XSS 攻击测试',
  '✅ CSRF 攻击测试',
  '✅ SQL 注入测试',
  '✅ 暴力破解测试',
  '✅ 会话固定测试',
  '✅ Token 泄露测试',
  '✅ 权限绕过测试',
  '✅ 并发登录测试',
  '✅ 密码重置测试',
  '✅ 登出测试'
];

console.log('\n=== 测试清单 ===');
testingChecklist.forEach(item => console.log(item));

// 8. 监控和告警
const monitoringItems = [
  '📊 登录失败率（异常升高告警）',
  '📊 异常地理位置登录',
  '📊 密码重置频率',
  '📊 MFA 使用率',
  '📊 会话持续时间',
  '📊 Token 刷新频率',
  '📊 API 调用频率（限流触发）',
  '📊 安全事件日志'
];

console.log('\n=== 监控和告警 ===');
monitoringItems.forEach(item => console.log(item));
