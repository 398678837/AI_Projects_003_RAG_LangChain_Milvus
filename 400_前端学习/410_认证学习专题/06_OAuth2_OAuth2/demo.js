// OAuth2 示例代码

// 1. OAuth2 核心角色
const oauth2Roles = {
  'Resource Owner 资源所有者': {
    描述: '拥有受保护资源的实体',
    示例: '用户、你自己'
  },
  'Client 客户端': {
    描述: '需要访问资源的应用',
    示例: '你的Web应用、移动App'
  },
  'Authorization Server 授权服务器': {
    描述: '验证身份并颁发令牌',
    示例: 'GitHub授权服务器、微信开放平台'
  },
  'Resource Server 资源服务器': {
    描述: '存储受保护资源的服务器',
    示例: 'GitHub API、微信用户信息API'
  }
};

console.log('=== OAuth2 核心角色 ===');
Object.entries(oauth2Roles).forEach(([role, info]) => {
  console.log(`\n【${role}】`);
  console.log(`  描述: ${info.描述}`);
  console.log(`  示例: ${info.示例}`);
});

// 2. OAuth2 授权流程对比
const oauth2Flows = {
  'Authorization Code 授权码流程': {
    特点: '最安全，需要后端',
    适用: 'Web应用（有后端）',
    安全: '最高',
    推荐: '⭐⭐⭐⭐⭐'
  },
  'Authorization Code with PKCE': {
    特点: '授权码+PKCE，更安全',
    适用: 'SPA、移动App',
    安全: '很高',
    推荐: '⭐⭐⭐⭐⭐'
  },
  'Client Credentials 客户端凭证': {
    特点: '机器对机器',
    适用: '服务间通信',
    安全: '高',
    推荐: '⭐⭐⭐⭐'
  },
  'Implicit 隐式流程': {
    特点: '直接返回令牌',
    适用: '已不推荐使用',
    安全: '低',
    推荐: '❌ 已废弃'
  },
  'Password 密码流程': {
    特点: '需要用户密码',
    适用: '高度信任的应用',
    安全: '低',
    推荐: '❌ 不推荐'
  }
};

console.log('\n=== OAuth2 授权流程 ===');
Object.entries(oauth2Flows).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  特点: ${info.特点}`);
  console.log(`  适用: ${info.适用}`);
  console.log(`  推荐: ${info.推荐}`);
});

// 3. Authorization Code 流程
function authorizationCodeFlow() {
  console.log('\n=== Authorization Code 流程 ===');
  
  const steps = [
    '1. 用户点击"使用GitHub登录"',
    '2. 客户端重定向到授权服务器',
    '   GET /authorize?response_type=code&client_id=xxx&redirect_uri=xxx&scope=user&state=xxx',
    '3. 用户同意授权',
    '4. 授权服务器重定向回客户端',
    '   GET /callback?code=xxx&state=xxx',
    '5. 客户端后端用code换取access_token',
    '   POST /token { grant_type: "authorization_code", code: xxx, client_id: xxx, client_secret: xxx, redirect_uri: xxx }',
    '6. 授权服务器返回 access_token',
    '7. 客户端使用 access_token 访问资源服务器',
    '8. 资源服务器返回受保护资源'
  ];
  
  steps.forEach(step => console.log(step));
}

authorizationCodeFlow();

// 4. GitHub OAuth2 登录示例（前端）
const githubOAuthExample = `
// 前端 - 发起授权请求
function loginWithGitHub() {
  const clientId = 'YOUR_CLIENT_ID';
  const redirectUri = encodeURIComponent('https://your-app.com/callback');
  const scope = encodeURIComponent('user:email');
  const state = generateRandomString();
  
  sessionStorage.setItem('oauth_state', state);
  
  const authUrl = \`https://github.com/login/oauth/authorize?\` +
    \`client_id=\${clientId}&\` +
    \`redirect_uri=\${redirectUri}&\` +
    \`scope=\${scope}&\` +
    \`state=\${state}\`;
  
  window.location.href = authUrl;
}

// 回调页面 - 处理授权码
async function handleCallback() {
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get('code');
  const state = urlParams.get('state');
  const savedState = sessionStorage.getItem('oauth_state');
  
  if (state !== savedState) {
    throw new Error('Invalid state parameter');
  }
  
  const response = await fetch('/api/auth/github', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code })
  });
  
  const data = await response.json();
  localStorage.setItem('access_token', data.access_token);
}

// 后端 - 换取 access_token（Node.js）
app.post('/api/auth/github', async (req, res) => {
  const { code } = req.body;
  
  const tokenResponse = await fetch('https://github.com/login/oauth/access_token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify({
      client_id: 'YOUR_CLIENT_ID',
      client_secret: 'YOUR_CLIENT_SECRET',
      code: code
    })
  });
  
  const tokenData = await tokenResponse.json();
  const accessToken = tokenData.access_token;
  
  const userResponse = await fetch('https://api.github.com/user', {
    headers: { 'Authorization': \`Bearer \${accessToken}\` }
  });
  
  const userData = await userResponse.json();
  res.json({ access_token: accessToken, user: userData });
});
`;

console.log('\n=== GitHub OAuth2 示例 ===');
console.log(githubOAuthExample);

// 5. OAuth2 常用参数
const oauth2Params = {
  response_type: '响应类型（code, token）',
  client_id: '客户端ID',
  client_secret: '客户端密钥',
  redirect_uri: '回调地址',
  scope: '权限范围',
  state: '防CSRF随机字符串',
  code: '授权码',
  grant_type: '授权类型',
  access_token: '访问令牌',
  refresh_token: '刷新令牌'
};

console.log('\n=== OAuth2 常用参数 ===');
Object.entries(oauth2Params).forEach(([param, desc]) => {
  console.log(`  ${param}: ${desc}`);
});

// 6. OAuth2 安全最佳实践
const oauth2Security = [
  '🔒 始终使用 HTTPS',
  '🔐 验证 state 参数（防止CSRF）',
  '📱 SPA/移动App 使用 PKCE',
  '🔑 client_secret 仅在后端使用',
  '🌐 redirect_uri 必须预注册',
  '📋 最小化 scope 权限',
  '⏰ 设置合理的过期时间',
  '🔄 使用 refresh_token 机制'
];

console.log('\n=== OAuth2 安全最佳实践 ===');
oauth2Security.forEach(tip => console.log(tip));

// 7. OpenID Connect (OIDC)
const oidcInfo = {
  简介: '基于OAuth2的身份层',
  作用: '提供身份认证，不仅是授权',
  新增: 'ID Token（JWT格式，包含用户身份信息）',
  端点: {
    authorization_endpoint: '授权端点',
    token_endpoint: '令牌端点',
    userinfo_endpoint: '用户信息端点',
    jwks_uri: '公钥端点'
  },
  流程: {
    Authorization Code Flow: '授权码流程',
    Implicit Flow: '隐式流程',
    Hybrid Flow: '混合流程'
  }
};

console.log('\n=== OpenID Connect ===');
console.log('简介:', oidcInfo.简介);
console.log('作用:', oidcInfo.作用);
console.log('新增:', oidcInfo.新增);
console.log('端点:', oidcInfo.端点);

// 8. ID Token 示例
const idTokenExample = {
  header: {
    alg: 'RS256',
    kid: 'key-id'
  },
  payload: {
    iss: 'https://accounts.google.com',
    sub: '1234567890',
    aud: 'your-client-id',
    exp: 1311281970,
    iat: 1311280970,
    name: '张三',
    email: 'zhangsan@example.com',
    picture: 'https://example.com/photo.jpg'
  },
  signature: '...签名...'
};

console.log('\n=== ID Token 示例 ===');
console.log(JSON.stringify(idTokenExample, null, 2));
