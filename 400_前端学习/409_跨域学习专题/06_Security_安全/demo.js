// 跨域安全示例代码

// 1. XSS 攻击类型
const xssTypes = {
  存储型XSS: {
    描述: '恶意脚本存储在服务器数据库',
    示例: '评论区输入 &lt;script&gt;stealCookies()&lt;/script&gt;',
    危害: '所有访问该页面的用户受影响'
  },
  反射型XSS: {
    描述: '恶意脚本在URL中，服务器反射回来',
    示例: 'https://example.com/search?q=&lt;script&gt;alert(1)&lt;/script&gt;',
    危害: '需要诱导用户点击链接'
  },
  DOM型XSS: {
    描述: '恶意脚本在客户端DOM中执行',
    示例: 'document.getElementById("output").innerHTML = location.hash',
    危害: '不经过服务器，纯前端问题'
  }
};

console.log('=== XSS 攻击类型 ===');
Object.entries(xssTypes).forEach(([type, info]) => {
  console.log(`\n【${type}】`);
  console.log(`  描述: ${info.描述}`);
  console.log(`  示例: ${info.示例}`);
  console.log(`  危害: ${info.危害}`);
});

// 2. XSS 防护 - 输出编码
function escapeHtml(str) {
  if (typeof str !== 'string') return str;
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

console.log('\n=== XSS 防护 - HTML编码 ===');
const dangerousInput = '<script>alert("XSS")</script>';
console.log('原始输入:', dangerousInput);
console.log('编码后:', escapeHtml(dangerousInput));

// 3. XSS 防护 - 使用 textContent 而非 innerHTML
function safeInsertText(element, text) {
  element.textContent = text;
}

function unsafeInsertHtml(element, html) {
  element.innerHTML = html;
}

console.log('\n=== XSS 防护 - DOM操作 ===');
console.log('✓ 安全: element.textContent = text');
console.log('✗ 危险: element.innerHTML = html');

// 4. CSP (内容安全策略)
const cspExamples = {
  '严格模式': `default-src 'self'`,
  '允许图片CDN': `default-src 'self'; img-src 'self' https://img.example.com`,
  '允许内联样式': `default-src 'self'; style-src 'self' 'unsafe-inline'`,
  '允许非内联脚本': `default-src 'self'; script-src 'self' https://trusted-cdn.com`,
  '报告模式': `default-src 'self'; report-uri /csp-violation-report-endpoint`
};

console.log('\n=== CSP 配置示例 ===');
Object.entries(cspExamples).forEach(([name, policy]) => {
  console.log(`\n【${name}】`);
  console.log(`  ${policy}`);
});

// 5. 设置安全响应头
const securityHeaders = {
  'Content-Security-Policy': "default-src 'self'",
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'X-XSS-Protection': '1; mode=block',
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
  'Referrer-Policy': 'strict-origin-when-cross-origin'
};

console.log('\n=== 安全响应头 ===');
Object.entries(securityHeaders).forEach(([name, value]) => {
  console.log(`  ${name}: ${value}`);
});

// 6. CSRF 攻击原理
function csrfAttackDemo() {
  console.log('\n=== CSRF 攻击原理 ===');
  
  const attackFlow = [
    '1. 用户登录银行网站 A，获得 Session Cookie',
    '2. 用户访问恶意网站 B',
    '3. 恶意网站 B 构造表单/图片，自动提交到 A',
    '4. 浏览器自动带上 A 的 Cookie',
    '5. 银行网站 A 认为是用户的正常操作',
    '6. 转账成功，攻击完成'
  ];
  
  attackFlow.forEach(step => console.log(step));
}

csrfAttackDemo();

// 7. CSRF 防护 - CSRF Token
function generateCSRFToken() {
  return Math.random().toString(36).substring(2, 15) + 
         Math.random().toString(36).substring(2, 15);
}

function verifyCSRFToken(token, sessionToken) {
  return token === sessionToken;
}

console.log('\n=== CSRF 防护 - Token ===');
const csrfToken = generateCSRFToken();
console.log('生成 Token:', csrfToken);
console.log('验证 Token:', verifyCSRFToken(csrfToken, csrfToken));
console.log('验证失败:', verifyCSRFToken('wrong-token', csrfToken));

// 8. CSRF 防护 - SameSite Cookie
const sameSiteCookieOptions = {
  Strict: {
    说明: '完全禁止第三方Cookie，最严格',
    适用: '高安全要求'
  },
  Lax: {
    说明: '导航到目标网站时发送（默认值）',
    适用: '大多数场景'
  },
  None: {
    说明: '无限制，但必须配合 Secure',
    适用: '需要第三方使用Cookie'
  }
};

console.log('\n=== CSRF 防护 - SameSite Cookie ===');
Object.entries(sameSiteCookieOptions).forEach(([value, info]) => {
  console.log(`\n【SameSite=${value}】`);
  console.log(`  说明: ${info.说明}`);
  console.log(`  适用: ${info.适用}`);
});

// 9. CORS 安全配置
const corsSecurityConfig = {
  不要使用: {
    'Origin: *': '除非是完全公开的API',
    'Methods: *': '只允许需要的方法',
    'Headers: *': '只允许需要的头'
  },
  推荐配置: {
    Origin: '白名单验证，动态设置',
    Methods: 'GET,POST,PUT,DELETE,OPTIONS',
    Headers: 'Content-Type,Authorization',
    Credentials: '需要时才开启，配合具体Origin',
    MaxAge: '86400（缓存1天）'
  }
};

console.log('\n=== CORS 安全配置 ===');
console.log('❌ 不要使用:');
Object.entries(corsSecurityConfig['不要使用']).forEach(([item, reason]) => {
  console.log(`  ${item}: ${reason}`);
});
console.log('✓ 推荐配置:');
Object.entries(corsSecurityConfig['推荐配置']).forEach(([item, value]) => {
  console.log(`  ${item}: ${value}`);
});

// 10. 动态 Origin 白名单验证
function validateOrigin(origin, whitelist) {
  if (!origin) return false;
  return whitelist.includes(origin);
}

const allowedOrigins = [
  'https://www.example.com',
  'https://app.example.com',
  'http://localhost:5173'
];

console.log('\n=== Origin 白名单验证 ===');
console.log('白名单:', allowedOrigins);
console.log('https://www.example.com:', validateOrigin('https://www.example.com', allowedOrigins));
console.log('https://evil.com:', validateOrigin('https://evil.com', allowedOrigins));

// 11. 安全检查清单
const securityChecklist = {
  XSS: [
    '对用户输入进行输出编码',
    '使用textContent代替innerHTML',
    '设置CSP内容安全策略',
    'Cookie设置HttpOnly'
  ],
  CSRF: [
    '使用CSRF Token',
    '设置SameSite Cookie',
    '验证Referer/Origin',
    '重要操作二次确认'
  ],
  CORS: [
    '验证Origin白名单',
    '限制Methods和Headers',
    '谨慎使用Credentials',
    '不使用Origin: *'
  ],
  其他: [
    '设置安全响应头',
    '输入验证和清理',
    '使用HTTPS',
    '定期更新依赖'
  ]
};

console.log('\n=== 安全检查清单 ===');
Object.entries(securityChecklist).forEach(([category, items]) => {
  console.log(`\n【${category}】`);
  items.forEach(item => console.log(`  ✓ ${item}`));
});

// 12. 常见安全误区
const securityMistakes = [
  '❌ 认为前端验证就够了，后端不验证',
  '❌ 直接将用户输入拼接到SQL中（SQL注入）',
  '❌ 在URL中传递敏感信息',
  '❌ 不设置Cookie的Secure和HttpOnly',
  '❌ CORS配置Origin: *同时允许Credentials',
  '❌ 信任JSONP的数据源',
  '❌ 不在生产环境使用HTTPS'
];

console.log('\n=== 常见安全误区 ===');
securityMistakes.forEach(mistake => console.log(mistake));
