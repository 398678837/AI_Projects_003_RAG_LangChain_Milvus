// JWT 示例代码

// 1. JWT 结构说明
const jwtStructure = {
  Header: {
    alg: 'HS256',
    typ: 'JWT'
  },
  Payload: {
    iss: 'myapp.com',
    sub: 'user123',
    exp: Math.floor(Date.now() / 1000) + 3600,
    name: '张三',
    role: 'admin'
  },
  Signature: 'HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)'
};

console.log('=== JWT 结构 ===');
console.log(JSON.stringify(jwtStructure, null, 2));

// 2. Base64URL 编码（JWT使用）
function base64UrlEncode(str) {
  const base64 = btoa(str);
  return base64
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

function base64UrlDecode(str) {
  str = str
    .replace(/-/g, '+')
    .replace(/_/g, '/');
  while (str.length % 4) {
    str += '=';
  }
  return atob(str);
}

console.log('\n=== Base64URL 编码 ===');
const testStr = JSON.stringify({ alg: 'HS256', typ: 'JWT' });
const encoded = base64UrlEncode(testStr);
const decoded = base64UrlDecode(encoded);
console.log('原始:', testStr);
console.log('编码:', encoded);
console.log('解码:', decoded);

// 3. 简单的 JWT 实现（演示用，生产环境请使用成熟库）
class SimpleJWT {
  constructor(secret) {
    this.secret = secret;
  }

  sign(payload, options = {}) {
    const header = {
      alg: 'HS256',
      typ: 'JWT',
      ...options.header
    };

    const now = Math.floor(Date.now() / 1000);
    const jwtPayload = {
      iat: now,
      exp: now + (options.expiresIn || 3600),
      ...payload
    };

    const headerB64 = base64UrlEncode(JSON.stringify(header));
    const payloadB64 = base64UrlEncode(JSON.stringify(jwtPayload));
    
    const signature = this.simpleSign(headerB64 + '.' + payloadB64);
    const signatureB64 = base64UrlEncode(signature);
    
    return `${headerB64}.${payloadB64}.${signatureB64}`;
  }

  verify(token) {
    const parts = token.split('.');
    if (parts.length !== 3) {
      return { valid: false, error: '无效的JWT格式' };
    }

    const [headerB64, payloadB64, signatureB64] = parts;
    
    const expectedSignature = this.simpleSign(headerB64 + '.' + payloadB64);
    const expectedSignatureB64 = base64UrlEncode(expectedSignature);
    
    if (signatureB64 !== expectedSignatureB64) {
      return { valid: false, error: '签名验证失败' };
    }

    try {
      const payload = JSON.parse(base64UrlDecode(payloadB64));
      
      if (payload.exp && Math.floor(Date.now() / 1000) > payload.exp) {
        return { valid: false, error: 'Token已过期' };
      }
      
      return { valid: true, payload };
    } catch (e) {
      return { valid: false, error: 'Payload解析失败' };
    }
  }

  decode(token) {
    const parts = token.split('.');
    if (parts.length !== 3) return null;
    
    try {
      return {
        header: JSON.parse(base64UrlDecode(parts[0])),
        payload: JSON.parse(base64UrlDecode(parts[1]))
      };
    } catch {
      return null;
    }
  }

  simpleSign(data) {
    let hash = 0;
    for (let i = 0; i < data.length; i++) {
      const char = data.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash;
    }
    return hash.toString(36) + this.secret.substring(0, 5);
  }
}

console.log('\n=== JWT 使用 ===');
const jwt = new SimpleJWT('my-secret-key');

const token = jwt.sign({ 
  userId: 1, 
  username: '张三', 
  role: 'admin' 
}, { expiresIn: 3600 });

console.log('生成的JWT:', token);

const decoded = jwt.decode(token);
console.log('解码JWT:', decoded);

const verified = jwt.verify(token);
console.log('验证JWT:', verified);

// 4. JWT 声明类型
const jwtClaims = {
  注册声明: {
    iss: '签发者 (Issuer)',
    sub: '主题 (Subject)',
    aud: '受众 (Audience)',
    exp: '过期时间 (Expiration Time)',
    nbf: '生效时间 (Not Before)',
    iat: '签发时间 (Issued At)',
    jti: 'JWT ID'
  },
  公共声明: {
    name: '姓名',
    email: '邮箱',
    role: '角色'
  },
  私有声明: {
    custom_field: '自定义字段'
  }
};

console.log('\n=== JWT 声明 ===');
console.log('注册声明:', jwtClaims.注册声明);
console.log('公共声明:', jwtClaims.公共声明);
console.log('私有声明:', jwtClaims.私有声明);

// 5. JWT 认证流程
function jwtAuthWorkflow() {
  console.log('\n=== JWT 认证流程 ===');
  
  const steps = [
    '1. 用户 POST /login { username, password }',
    '2. 服务器验证凭证',
    '3. 服务器生成 JWT (Header.Payload.Signature)',
    '4. 返回 { access_token: "xxx" }',
    '5. 客户端存储 JWT',
    '6. 请求受保护资源: GET /api/data',
    '7. 客户端添加 Header: Authorization: Bearer xxx',
    '8. 服务器验证签名',
    '9. 验证 exp 过期时间',
    '10. 解析 payload 获取用户信息',
    '11. 返回数据'
  ];
  
  steps.forEach(step => console.log(step));
}

jwtAuthWorkflow();

// 6. JWT vs Session Token 对比
const jwtVsSession = {
  'JWT': {
    状态: '无状态',
    服务器存储: '不需要',
    扩展性: '好',
    撤销: '困难',
    payload: '可见（Base64）',
    适用: '微服务、分布式'
  },
  'Session Token': {
    状态: '有状态',
    服务器存储: '需要（Redis/DB）',
    扩展性: '一般',
    撤销: '容易',
    payload: '服务器端存储',
    适用: '传统Web应用'
  }
};

console.log('\n=== JWT vs Session Token ===');
console.log('          JWT        Session Token');
console.log(`状态:     无状态       有状态`);
console.log(`服务器存储: 不需要      需要`);
console.log(`扩展性:    好          一般`);
console.log(`撤销:      困难        容易`);

// 7. JWT 安全最佳实践
const jwtSecurity = [
  '🔒 始终使用 HTTPS',
  '🔑 使用强密钥签名',
  '📊 使用 RS256 而非 HS256（非对称加密）',
  '⏰ 设置合理的过期时间',
  '🚫 不要在 payload 存储敏感信息',
  '🔄 实现刷新 Token 机制',
  '✅ 验证所有声明（exp, iss, aud）',
  '📋 考虑使用 JWT 库（jsonwebtoken, jose）'
];

console.log('\n=== JWT 安全最佳实践 ===');
jwtSecurity.forEach(tip => console.log(tip));

// 8. 使用 jsonwebtoken 库（Node.js示例）
const jsonwebtokenExample = `
// npm install jsonwebtoken
const jwt = require('jsonwebtoken');

// 生成 Token
const token = jwt.sign(
  { userId: 1, username: '张三' },
  'your-secret-key',
  { 
    expiresIn: '1h',
    issuer: 'myapp.com',
    subject: 'user123'
  }
);

// 验证 Token
try {
  const decoded = jwt.verify(token, 'your-secret-key');
  console.log('验证成功:', decoded);
} catch (error) {
  console.log('验证失败:', error.message);
}

// 只解码不验证
const decoded = jwt.decode(token);
console.log('解码:', decoded);
`;

console.log('\n=== jsonwebtoken 库示例 ===');
console.log(jsonwebtokenExample);

// 9. JWT 常见误区
const commonMistakes = [
  '❌ 在 payload 存储密码',
  '❌ 不设置过期时间',
  '❌ 使用 HS256 但密钥太弱',
  '❌ 认为 payload 是加密的（只是Base64）',
  '❌ 不信任成熟的库，自己实现',
  '❌ 不验证 exp、iss 等声明'
];

console.log('\n=== JWT 常见误区 ===');
commonMistakes.forEach(mistake => console.log(mistake));
