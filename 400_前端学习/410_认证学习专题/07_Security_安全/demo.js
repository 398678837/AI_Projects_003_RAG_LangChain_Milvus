// 认证安全示例代码

// 1. 常见安全威胁
const securityThreats = {
  'XSS 跨站脚本攻击': {
    描述: '攻击者注入恶意脚本',
    危害: '窃取Cookie、会话劫持',
    防护: '输入过滤、输出编码、CSP'
  },
  'CSRF 跨站请求伪造': {
    描述: '诱导用户在已登录网站执行操作',
    危害: '未经授权的操作',
    防护: 'CSRF Token、SameSite Cookie'
  },
  '密码破解': {
    描述: '暴力破解、字典攻击',
    危害: '账号被盗',
    防护: '强密码策略、加盐哈希、速率限制'
  },
  '会话劫持': {
    描述: '窃取会话ID冒充用户',
    危害: '账号接管',
    防护: 'HttpOnly Cookie、HTTPS、会话超时'
  },
  'MITM 中间人攻击': {
    描述: '拦截和篡改通信',
    危害: '数据泄露、篡改',
    防护: 'HTTPS、证书验证、HSTS'
  },
  'SQL注入': {
    描述: '注入SQL代码',
    危害: '数据泄露、篡改',
    防护: '参数化查询、ORM'
  }
};

console.log('=== 常见安全威胁 ===');
Object.entries(securityThreats).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  描述: ${info.描述}`);
  console.log(`  危害: ${info.危害}`);
  console.log(`  防护: ${info.防护}`);
});

// 2. 密码安全 - 强度检查
function checkPasswordStrength(password) {
  let score = 0;
  const feedback = [];

  if (password.length >= 8) score++;
  else feedback.push('密码至少8位');

  if (/[a-z]/.test(password)) score++;
  else feedback.push('需要小写字母');

  if (/[A-Z]/.test(password)) score++;
  else feedback.push('需要大写字母');

  if (/[0-9]/.test(password)) score++;
  else feedback.push('需要数字');

  if (/[^a-zA-Z0-9]/.test(password)) score++;
  else feedback.push('需要特殊字符');

  if (password.length >= 12) score++;

  const levels = ['极弱', '弱', '一般', '强', '很强', '极强'];

  return {
    score,
    level: levels[Math.min(score, 5)],
    feedback
  };
}

console.log('\n=== 密码强度检查 ===');
const testPasswords = ['123456', 'password', 'Password123', 'Pass@123456', 'My$tr0ngP@ssw0rd!'];
testPasswords.forEach(pwd => {
  const result = checkPasswordStrength(pwd);
  console.log(`  ${pwd.padEnd(20)} → ${result.level} (${result.score}/6)`);
});

// 3. 密码安全 - 加盐哈希（Node.js示例）
const passwordHashingExample = `
// 推荐使用 bcrypt 或 argon2
// npm install bcrypt
const bcrypt = require('bcrypt');

async function hashPassword(password) {
  const saltRounds = 12;
  const salt = await bcrypt.genSalt(saltRounds);
  const hash = await bcrypt.hash(password, salt);
  return hash;
}

async function verifyPassword(password, hash) {
  return await bcrypt.compare(password, hash);
}

// 使用示例
const hashedPassword = await hashPassword('MyPassword123!');
console.log('Hash:', hashedPassword);

const isValid = await verifyPassword('MyPassword123!', hashedPassword);
console.log('验证:', isValid);
`;

console.log('\n=== 密码哈希示例 ===');
console.log(passwordHashingExample);

// 4. 密码算法对比
const hashAlgorithms = {
  'MD5': {
    安全: '❌ 已不安全',
    速度: '极快',
    推荐: '不推荐'
  },
  'SHA-1': {
    安全: '❌ 已不安全',
    速度: '快',
    推荐: '不推荐'
  },
  'SHA-256': {
    安全: '⚠️  不够安全（太快）',
    速度: '快',
    推荐: '不推荐单独使用'
  },
  'bcrypt': {
    安全: '✅ 安全',
    速度: '可调整',
    推荐: '⭐⭐⭐⭐ 推荐'
  },
  'argon2': {
    安全: '✅ 最安全',
    速度: '可调整',
    推荐: '⭐⭐⭐⭐⭐ 首选'
  },
  'scrypt': {
    安全: '✅ 安全',
    速度: '可调整',
    推荐: '⭐⭐⭐⭐ 推荐'
  }
};

console.log('\n=== 哈希算法对比 ===');
console.log('算法          安全        速度        推荐');
Object.entries(hashAlgorithms).forEach(([name, info]) => {
  console.log(`${name.padEnd(12)}  ${info.安全.padEnd(12)}  ${info.速度.padEnd(8)}  ${info.推荐}`);
});

// 5. 安全响应头
const securityHeaders = {
  'Strict-Transport-Security': 'HSTS，强制HTTPS',
  'X-Content-Type-Options': 'nosniff，防止MIME类型嗅探',
  'X-Frame-Options': 'DENY/SAMEORIGIN，防止点击劫持',
  'X-XSS-Protection': 'XSS保护（现代浏览器已内置）',
  'Content-Security-Policy': 'CSP，内容安全策略',
  'Referrer-Policy': '控制Referer头',
  'Permissions-Policy': '控制浏览器API权限'
};

console.log('\n=== 安全响应头 ===');
Object.entries(securityHeaders).forEach(([header, desc]) => {
  console.log(`  ${header}: ${desc}`);
});

// 6. CSP 内容安全策略示例
const cspExamples = {
  '基础CSP': "default-src 'self'",
  '严格CSP': "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'",
  '仅报告模式': "default-src 'self'; report-uri /csp-violation-report-endpoint"
};

console.log('\n=== CSP 示例 ===');
Object.entries(cspExamples).forEach(([name, policy]) => {
  console.log(`\n【${name}】`);
  console.log(`  ${policy}`);
});

// 7. 安全最佳实践清单
const securityChecklist = [
  '🔒 全程使用 HTTPS',
  '🔑 密码使用 bcrypt/argon2 加盐哈希',
  '🍪 Cookie 设置 HttpOnly、Secure、SameSite=Strict',
  '🛡️  实现 CSRF Token 保护',
  '📋 实施 CSP 内容安全策略',
  '⏱️  实现登录速率限制',
  '📱 验证码防止暴力破解',
  '🔄 敏感操作需要重新验证',
  '📝 记录安全相关日志',
  '🔍 定期安全审计'
];

console.log('\n=== 安全最佳实践清单 ===');
securityChecklist.forEach(item => console.log(item));

// 8. 速率限制
class RateLimiter {
  constructor(options = {}) {
    this.windowMs = options.windowMs || 15 * 60 * 1000;
    this.maxRequests = options.maxRequests || 5;
    this.requests = new Map();
  }

  isAllowed(key) {
    const now = Date.now();
    const windowStart = now - this.windowMs;
    
    let userRequests = this.requests.get(key) || [];
    userRequests = userRequests.filter(time => time > windowStart);
    
    this.requests.set(key, userRequests);
    
    if (userRequests.length >= this.maxRequests) {
      return { allowed: false, retryAfter: Math.ceil((userRequests[0] + this.windowMs - now) / 1000) };
    }
    
    userRequests.push(now);
    this.requests.set(key, userRequests);
    return { allowed: true, remaining: this.maxRequests - userRequests.length };
  }

  cleanup() {
    const now = Date.now();
    const windowStart = now - this.windowMs;
    for (const [key, requests] of this.requests) {
      const filtered = requests.filter(time => time > windowStart);
      if (filtered.length === 0) {
        this.requests.delete(key);
      } else {
        this.requests.set(key, filtered);
      }
    }
  }
}

console.log('\n=== 速率限制示例 ===');
const rateLimiter = new RateLimiter({ windowMs: 60000, maxRequests: 3 });
const testKey = 'user-123';
for (let i = 1; i <= 5; i++) {
  const result = rateLimiter.isAllowed(testKey);
  console.log(`  请求 ${i}:`, result);
}

// 9. 多因素认证 (MFA)
const mfaInfo = {
  类型: [
    'SMS 短信验证码',
    'Email 邮件验证码',
    'TOTP 时间-based 一次性密码（Google Authenticator）',
    'HOTP 计数-based 一次性密码',
    '硬件密钥（YubiKey）',
    '生物识别（指纹、人脸）'
  ],
  推荐: 'TOTP 或 硬件密钥',
  优势: '即使密码泄露也能保护账号'
};

console.log('\n=== 多因素认证 ===');
console.log('类型:', mfaInfo.类型);
console.log('推荐:', mfaInfo.推荐);
console.log('优势:', mfaInfo.优势);
