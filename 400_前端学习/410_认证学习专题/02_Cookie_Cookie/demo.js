// Cookie 认证示例代码

// 1. Cookie 属性说明
const cookieAttributes = {
  name: 'Cookie名称',
  value: 'Cookie值',
  expires: '过期日期（Date对象）',
  'max-age': '有效期（秒）',
  domain: '作用域名',
  path: '作用路径',
  secure: '仅HTTPS传输',
  httponly: 'JavaScript无法读取',
  samesite: 'SameSite策略（Strict/Lax/None）'
};

console.log('=== Cookie 属性 ===');
Object.entries(cookieAttributes).forEach(([attr, desc]) => {
  console.log(`  ${attr}: ${desc}`);
});

// 2. 安全的 Cookie 设置
function setSecureCookie(name, value, options = {}) {
  const defaultOptions = {
    'max-age': 86400 * 7,
    path: '/',
    secure: true,
    httponly: true,
    samesite: 'Strict'
  };
  
  const finalOptions = { ...defaultOptions, ...options };
  let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;
  
  if (finalOptions.expires) {
    cookieString += `; expires=${finalOptions.expires.toUTCString()}`;
  }
  if (finalOptions['max-age']) {
    cookieString += `; max-age=${finalOptions['max-age']}`;
  }
  if (finalOptions.domain) {
    cookieString += `; domain=${finalOptions.domain}`;
  }
  if (finalOptions.path) {
    cookieString += `; path=${finalOptions.path}`;
  }
  if (finalOptions.secure) {
    cookieString += '; secure';
  }
  if (finalOptions.httponly) {
    cookieString += '; HttpOnly';
  }
  if (finalOptions.samesite) {
    cookieString += `; samesite=${finalOptions.samesite}`;
  }
  
  return cookieString;
}

console.log('\n=== 安全Cookie设置 ===');
const sessionCookie = setSecureCookie('sessionId', 'sess_abc123def456');
console.log('Session Cookie:', sessionCookie);

// 3. SameSite 属性详解
const sameSiteValues = {
  Strict: {
    说明: '完全禁止第三方Cookie',
    行为: '只有同站请求才发送',
    安全: '最高',
    适用: '高安全要求'
  },
  Lax: {
    说明: '宽松模式（浏览器默认）',
    行为: '导航到目标站点时发送',
    安全: '中等',
    适用: '大多数场景'
  },
  None: {
    说明: '无限制',
    行为: '所有请求都发送',
    安全: '最低',
    适用: '必须配合Secure'
  }
};

console.log('\n=== SameSite 属性 ===');
Object.entries(sameSiteValues).forEach(([value, info]) => {
  console.log(`\n【SameSite=${value}】`);
  console.log(`  说明: ${info.说明}`);
  console.log(`  安全: ${info.安全}`);
  console.log(`  适用: ${info.适用}`);
});

// 4. 服务器端 Cookie 设置（Node.js/Express示例）
const serverCookieExample = `
// server.js - Express
const express = require('express');
const app = express();

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  if (validateUser(username, password)) {
    const sessionId = generateSessionId();
    storeSession(sessionId, { username });
    
    res.cookie('sessionId', sessionId, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'Strict',
      maxAge: 7 * 24 * 60 * 60 * 1000,
      path: '/'
    });
    
    res.json({ success: true });
  }
});

app.get('/user', (req, res) => {
  const sessionId = req.cookies.sessionId;
  const user = getSession(sessionId);
  
  if (user) {
    res.json(user);
  } else {
    res.status(401).json({ error: '未登录' });
  }
});

app.post('/logout', (req, res) => {
  res.clearCookie('sessionId', {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'Strict',
    path: '/'
  });
  res.json({ success: true });
});
`;

console.log('\n=== 服务器端 Cookie 设置 ===');
console.log(serverCookieExample);

// 5. Cookie 认证流程
function cookieAuthWorkflow() {
  console.log('\n=== Cookie 认证流程 ===');
  
  const steps = [
    '1. 用户访问 /login 页面',
    '2. 输入用户名密码，提交 POST /login',
    '3. 服务器验证凭证',
    '4. 服务器生成 SessionID',
    '5. 服务器 Set-Cookie: sessionId=xxx; HttpOnly; Secure; SameSite=Strict',
    '6. 浏览器保存 Cookie',
    '7. 用户访问 /profile',
    '8. 浏览器自动携带 Cookie',
    '9. 服务器通过 SessionID 找到用户',
    '10. 返回用户数据'
  ];
  
  steps.forEach(step => console.log(step));
}

cookieAuthWorkflow();

// 6. Cookie 安全检查清单
const securityChecklist = [
  '✅ 设置 HttpOnly 防止 XSS',
  '✅ 设置 Secure 仅 HTTPS 传输',
  '✅ 设置 SameSite 防止 CSRF',
  '✅ 合理设置过期时间',
  '✅ 不存储敏感数据',
  '✅ 使用签名防止篡改',
  '✅ 登出时清除 Cookie',
  '✅ 使用 path 限制作用范围'
];

console.log('\n=== Cookie 安全清单 ===');
securityChecklist.forEach(item => console.log(item));

// 7. Cookie vs LocalStorage 对比
const cookieVsStorage = {
  Cookie: {
    容量: '~4KB',
    自动发送: '是（同域请求）',
    HttpOnly: '支持',
    Secure: '支持',
    SameSite: '支持',
    过期: '支持',
    适用: '认证、会话管理'
  },
  LocalStorage: {
    容量: '~5MB',
    自动发送: '否',
    HttpOnly: '不支持',
    Secure: '不支持',
    SameSite: '不适用',
    过期: '不支持（永久）',
    适用: '非敏感数据、客户端缓存'
  }
};

console.log('\n=== Cookie vs LocalStorage ===');
console.log('          Cookie        LocalStorage');
console.log(`容量:     ${cookieVsStorage.Cookie.容量}        ${cookieVsStorage.LocalStorage.容量}`);
console.log(`自动发送: ${cookieVsStorage.Cookie.自动发送}           ${cookieVsStorage.LocalStorage.自动发送}`);
console.log(`HttpOnly: ${cookieVsStorage.Cookie.HttpOnly}           ${cookieVsStorage.LocalStorage.HttpOnly}`);
console.log(`Secure:   ${cookieVsStorage.Cookie.Secure}           ${cookieVsStorage.LocalStorage.Secure}`);
console.log(`适用:     ${cookieVsStorage.Cookie.适用}  ${cookieVsStorage.LocalStorage.适用}`);

// 8. 常见 Cookie 安全误区
const commonMistakes = [
  '❌ 不设置 HttpOnly，容易被 XSS 窃取',
  '❌ 不设置 Secure，HTTP 环境下传输',
  '❌ SameSite=None 但不配合 Secure',
  '❌ 在 Cookie 中存储密码',
  '❌ 过期时间设置过长',
  '❌ 不验证 Cookie 完整性',
  '❌ 登出时不清除 Cookie'
];

console.log('\n=== 常见安全误区 ===');
commonMistakes.forEach(mistake => console.log(mistake));
