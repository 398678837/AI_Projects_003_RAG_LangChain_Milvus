// Cookie 示例代码

// 1. Cookie 属性说明
const cookieAttributes = {
  name: 'Cookie名称',
  value: 'Cookie值',
  expires: '过期时间（Date对象）',
  'max-age': '有效期（秒）',
  domain: '作用域名',
  path: '作用路径',
  secure: '仅HTTPS传输',
  httponly: 'JavaScript无法读取',
  samesite: 'SameSite策略（Strict/Lax/None）'
};

console.log('Cookie 属性:', cookieAttributes);

// 2. 设置Cookie的工具函数
function setCookie(name, value, options = {}) {
  let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;
  
  if (options.expires) {
    cookieString += `; expires=${options.expires.toUTCString()}`;
  }
  
  if (options['max-age']) {
    cookieString += `; max-age=${options['max-age']}`;
  }
  
  if (options.domain) {
    cookieString += `; domain=${options.domain}`;
  }
  
  if (options.path) {
    cookieString += `; path=${options.path}`;
  }
  
  if (options.secure) {
    cookieString += '; secure';
  }
  
  if (options.httponly) {
    cookieString += '; HttpOnly';
  }
  
  if (options.samesite) {
    cookieString += `; samesite=${options.samesite}`;
  }
  
  document.cookie = cookieString;
  console.log('设置Cookie:', cookieString);
}

// 3. 读取Cookie的工具函数
function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    const [cookieName, cookieValue] = cookie.trim().split('=');
    if (cookieName === encodeURIComponent(name)) {
      return decodeURIComponent(cookieValue);
    }
  }
  return null;
}

// 4. 删除Cookie的工具函数
function deleteCookie(name, options = {}) {
  setCookie(name, '', {
    ...options,
    'max-age': -1
  });
}

// 5. 获取所有Cookie
function getAllCookies() {
  const cookies = {};
  if (document.cookie) {
    document.cookie.split(';').forEach(cookie => {
      const [name, value] = cookie.trim().split('=');
      if (name && value) {
        cookies[decodeURIComponent(name)] = decodeURIComponent(value);
      }
    });
  }
  return cookies;
}

// 6. 使用示例
console.log('\n=== Cookie 操作示例 ===');

// 设置Cookie
setCookie('username', '张三', { 'max-age': 86400 });
setCookie('theme', 'dark', { 'max-age': 86400 });
setCookie('language', 'zh-CN', { 'max-age': 86400 });

// 读取Cookie
console.log('读取 username:', getCookie('username'));
console.log('读取 theme:', getCookie('theme'));

// 获取所有Cookie
console.log('所有Cookie:', getAllCookies());

// 7. Cookie 过期时间设置示例
function setCookieWithExpiration() {
  console.log('\n=== 设置过期时间 ===');
  
  const now = new Date();
  
  // 1小时后过期
  const oneHourLater = new Date(now.getTime() + 60 * 60 * 1000);
  setCookie('sessionId', 'abc123', { expires: oneHourLater });
  
  // 7天后过期
  setCookie('rememberMe', 'true', { 'max-age': 7 * 24 * 60 * 60 });
  
  // 会话Cookie（关闭浏览器就失效）
  setCookie('temp', '临时数据');
}

setCookieWithExpiration();

// 8. SameSite 属性说明
const sameSiteValues = {
  Strict: '严格模式，完全禁止第三方Cookie',
  Lax: '宽松模式，导航到目标网址时发送（默认）',
  None: '无限制，但必须配合Secure'
};

console.log('\nSameSite 值:', sameSiteValues);

// 9. 安全的Cookie设置示例
function setSecureCookie() {
  console.log('\n=== 安全Cookie设置 ===');
  
  const secureOptions = {
    'max-age': 86400,
    path: '/',
    secure: true,
    httponly: true,
    samesite: 'Strict'
  };
  
  console.log('安全Cookie选项:', secureOptions);
}

setSecureCookie();

// 10. Cookie 注意事项
const cookieNotes = {
  大小限制: '每个Cookie约4KB',
  数量限制: '每个域名约50个',
  安全性: '不要存储密码等敏感信息',
  编码: '特殊字符需要编码',
  HttpOnly: '防止XSS攻击',
  SameSite: '防止CSRF攻击'
};

console.log('\nCookie 注意事项:', cookieNotes);

// 11. 简单的Cookie存储类
class CookieStorage {
  constructor(defaultOptions = {}) {
    this.defaultOptions = defaultOptions;
  }

  set(name, value, options = {}) {
    setCookie(name, value, { ...this.defaultOptions, ...options });
  }

  get(name) {
    return getCookie(name);
  }

  delete(name, options = {}) {
    deleteCookie(name, { ...this.defaultOptions, ...options });
  }

  getAll() {
    return getAllCookies();
  }
}

// 使用示例
const storage = new CookieStorage({ path: '/' });
storage.set('user', JSON.stringify({ id: 1, name: '测试' }), { 'max-age': 3600 });
console.log('\nCookieStorage 存储的用户:', JSON.parse(storage.get('user')));
