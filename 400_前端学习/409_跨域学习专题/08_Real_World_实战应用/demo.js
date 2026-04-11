// 跨域实战应用示例代码

// 1. 场景一：前后端分离完整配置
const fullStackConfig = {
  '开发环境': {
    前端: 'Vite + 代理',
    后端: 'Node.js + CORS',
    配置: `
// vite.config.js
proxy: {
  '/api': {
    target: 'http://localhost:3000',
    changeOrigin: true,
    rewrite: path => path.replace(/^\\/api/, '')
  }
}

// 前端调用
fetch('/api/users')
`
  },
  '生产环境 - Nginx代理': {
    架构: 'Nginx → 前端静态文件 + 后端API',
    配置: `
server {
  listen 80;
  server_name example.com;
  
  location / {
    root /var/www/dist;
    try_files $uri $uri/ /index.html;
  }
  
  location /api/ {
    proxy_pass http://localhost:3000/;
    proxy_set_header Host $host;
  }
}
`
  },
  '生产环境 - CORS': {
    架构: '前端(https://www.example.com) + 后端(https://api.example.com)',
    配置: `
// 后端CORS配置
const corsOptions = {
  origin: 'https://www.example.com',
  credentials: true
};

// 前端调用
fetch('https://api.example.com/users', {
  credentials: 'include'
})
`
  }
};

console.log('=== 场景一：前后端分离 ===');
Object.entries(fullStackConfig).forEach(([env, info]) => {
  console.log(`\n【${env}】`);
  if (info.前端) console.log(`  前端: ${info.前端}`);
  if (info.后端) console.log(`  后端: ${info.后端}`);
  if (info.架构) console.log(`  架构: ${info.架构}`);
  console.log(`  配置:\n${info.配置}`);
});

// 2. 场景二：微服务架构 + API网关
const microserviceConfig = `
=== 场景二：微服务架构 ===

架构图:
  浏览器 → Nginx → API网关 → 用户服务
                          → 订单服务
                          → 商品服务

配置:

1. API网关 (Kong/Nginx/Express Gateway) 统一处理CORS:

location /api/ {
  add_header Access-Control-Allow-Origin "https://www.example.com";
  add_header Access-Control-Allow-Methods "GET,POST,PUT,DELETE,OPTIONS";
  add_header Access-Control-Allow-Credentials "true";
  
  if ($request_method = 'OPTIONS') {
    return 204;
  }
  
  # 路由到不同服务
  rewrite ^/api/users/(.*) /users/$1 break;
  proxy_pass http://user-service;
  
  rewrite ^/api/orders/(.*) /orders/$1 break;
  proxy_pass http://order-service;
}

优势:
- 跨域在网关统一处理
- 微服务之间无需考虑跨域
- 统一的认证、限流、日志
`;

console.log('\n' + microserviceConfig);

// 3. 场景三：调用第三方API
const thirdPartyAPI = {
  方案一: '后端代理（推荐）',
  说明: '前端请求自己后端，后端转发第三方API',
  流程: '浏览器 → 你的后端 → 第三方API',
  优点: '无跨域，安全可控',
  示例代码: `
// 后端 (Node.js)
app.get('/api/weather', async (req, res) => {
  const { city } = req.query;
  const response = await fetch(
    \`https://api.weather.com/data?city=\${city}&key=YOUR_KEY\`
  );
  const data = await response.json();
  res.json(data);
});

// 前端
fetch('/api/weather?city=beijing')
  .then(res => res.json())
  .then(data => console.log(data));
`
};

console.log('\n=== 场景三：调用第三方API ===');
console.log(`【${thirdPartyAPI.方案一}】`);
console.log(`说明: ${thirdPartyAPI.说明}`);
console.log(`流程: ${thirdPartyAPI.流程}`);
console.log(`优点: ${thirdPartyAPI.优点}`);
console.log(`代码:\n${thirdPartyAPI.示例代码}`);

// 4. 场景四：微信公众号开发
const wechatDev = `
=== 场景四：微信公众号开发 ===

需求:
- 本地开发测试微信回调
- 微信服务器需要访问公网地址

解决方案: Ngrok内网穿透

步骤:
1. 启动本地服务: npm run dev (端口8080)
2. 启动Ngrok: ngrok http 8080
3. 获取公网地址: https://abc123.ngrok.io
4. 配置微信后台: 将URL设置为Ngrok地址
5. 测试: 微信服务器回调本地服务

Ngrok命令:
  ngrok http --domain=mywechat.ngrok.io 8080

注意:
- 免费版域名随机，每次重启会变
- 付费版可固定域名
- 测试完成记得关闭隧道
`;

console.log('\n' + wechatDev);

// 5. 场景五：OAuth 登录
const oauthLogin = `
=== 场景五：OAuth 登录 (GitHub/Google/微信) ===

流程:
1. 用户点击"GitHub登录"
2. 跳转到 GitHub 授权页面
3. 用户授权后，GitHub 回调到你的后端
4. 后端处理，设置 Cookie，跳转回前端
5. 前端已登录

前端代码:
<a href="https://github.com/login/oauth/authorize?client_id=xxx&redirect_uri=https://api.example.com/auth/github/callback">
  GitHub登录
</a>

后端回调处理:
app.get('/auth/github/callback', async (req, res) => {
  const { code } = req.query;
  const token = await exchangeCodeForToken(code);
  const user = await getUserInfo(token);
  
  res.cookie('sessionId', createSession(user), {
    httpOnly: true,
    secure: true,
    sameSite: 'lax'
  });
  
  res.redirect('https://www.example.com/dashboard');
});

跨域处理:
- 回调是服务器到服务器，无跨域
- 前端跳转到第三方，无跨域
- Cookie设置在同域下
`;

console.log('\n' + oauthLogin);

// 6. 场景六：混合 App 开发 (H5 + Native)
const hybridApp = `
=== 场景六：混合 App 开发 ===

方案一：H5 页面在 WebView 中
- WebView 配置允许跨域
- iOS: WKWebView.configuration.preferences.setValue(true, forKey: "allowFileAccessFromFileURLs")
- Android: webSettings.setAllowFileAccess(true)

方案二：JSBridge 通信
// 前端调用原生
window.NativeBridge.getUserInfo((user) => {
  console.log(user);
});

// 原生调用前端
window.receiveDataFromNative = function(data) {
  console.log(data);
};

方案三：HTTP 接口
- App 内置本地服务器
- H5 通过 http://localhost:port 访问
- 无跨域问题（同源）
`;

console.log('\n' + hybridApp);

// 7. 部署方案对比
const deploymentComparison = [
  {
    方案: '同域部署',
    说明: '前端和后端在同一域名下',
    优点: '无跨域问题，简单',
    缺点: '部署耦合',
    适用: '小型项目'
  },
  {
    方案: '子域名 + CORS',
    说明: '前端 www.example.com, 后端 api.example.com',
    优点: '职责分离，可独立部署',
    缺点: '需要配置CORS',
    适用: '中大型项目'
  },
  {
    方案: 'Nginx反向代理',
    说明: 'Nginx统一入口，/ 前端, /api 后端',
    优点: '对前端透明，无跨域',
    缺点: '需要Nginx配置',
    适用: '推荐，生产环境'
  }
];

console.log('\n=== 部署方案对比 ===');
deploymentComparison.forEach((item, i) => {
  console.log(`\n${i + 1}. ${item.方案}`);
  console.log(`   说明: ${item.说明}`);
  console.log(`   优点: ${item.优点}`);
  console.log(`   缺点: ${item.缺点}`);
  console.log(`   适用: ${item.适用}`);
});

// 8. 完整项目配置示例
const completeProject = `
=== 完整项目配置示例 ===

项目结构:
my-app/
├── frontend/              # 前端
│   ├── src/
│   ├── vite.config.js
│   └── package.json
├── backend/               # 后端
│   ├── src/
│   ├── app.js
│   └── package.json
└── nginx/                 # Nginx配置
    └── nginx.conf

开发环境:
- 前端: Vite代理到后端
- 后端: 开启CORS允许localhost

生产环境:
- Nginx代理所有请求
- / → 前端dist
- /api → 后端服务
- 无跨域问题
`;

console.log('\n' + completeProject);
