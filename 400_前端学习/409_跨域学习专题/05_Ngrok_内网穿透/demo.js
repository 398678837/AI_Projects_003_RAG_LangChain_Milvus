// Ngrok 内网穿透示例代码

// 1. Ngrok 常用命令
const ngrokCommands = {
  '安装 Ngrok': {
    Windows: 'choco install ngrok 或 下载zip解压',
    macOS: 'brew install ngrok',
    Linux: 'snap install ngrok'
  },
  '认证配置': 'ngrok config add-authtoken YOUR_AUTH_TOKEN',
  '启动HTTP隧道': 'ngrok http 8080',
  '启动HTTPS隧道': 'ngrok http https://localhost:8080',
  '指定域名（付费）': 'ngrok http --domain=myapp.ngrok.io 8080',
  'TCP隧道': 'ngrok tcp 3306',
  '启动Web界面': 'ngrok http 8080 --log=stdout',
  '查看帮助': 'ngrok help'
};

console.log('=== Ngrok 常用命令 ===');
Object.entries(ngrokCommands).forEach(([name, cmd]) => {
  console.log(`\n【${name}】`);
  if (typeof cmd === 'string') {
    console.log(`  ${cmd}`);
  } else {
    Object.entries(cmd).forEach(([os, c]) => {
      console.log(`  ${os}: ${c}`);
    });
  }
});

// 2. Ngrok 使用场景
const useCases = [
  {
    场景: '微信公众号开发',
    说明: '本地测试微信回调',
    命令: 'ngrok http 80'
  },
  {
    场景: 'Webhook 测试',
    说明: '测试GitHub、Slack等Webhook',
    命令: 'ngrok http 3000'
  },
  {
    场景: '移动端API测试',
    说明: '手机访问本地开发服务器',
    命令: 'ngrok http 5173'
  },
  {
    场景: '第三方服务集成',
    说明: 'OAuth回调、支付回调',
    命令: 'ngrok http --domain=myapp.ngrok.io 8080'
  },
  {
    场景: '客户演示',
    说明: '快速给客户展示本地开发的功能',
    命令: 'ngrok http 8080'
  }
];

console.log('\n=== Ngrok 使用场景 ===');
useCases.forEach((uc, i) => {
  console.log(`\n${i + 1}. ${uc.场景}`);
  console.log(`   说明: ${uc.说明}`);
  console.log(`   命令: ${uc.命令}`);
});

// 3. Ngrok 配置文件示例
const ngrokConfig = `
# ~/.ngrok2/ngrok.yml
version: "2"
authtoken: YOUR_AUTH_TOKEN_HERE

tunnels:
  web:
    proto: http
    addr: 8080
    domain: myapp.ngrok.io
  
  api:
    proto: http
    addr: 3000
    domain: api.ngrok.io
  
  database:
    proto: tcp
    addr: 3306
`;

console.log('\n=== Ngrok 配置文件示例 ===');
console.log(ngrokConfig);

// 4. 使用配置文件启动
console.log('\n=== 使用配置文件 ===');
console.log('启动所有隧道: ngrok start --all');
console.log('启动指定隧道: ngrok start web api');

// 5. Node.js 中使用 ngrok 包
const nodeNgrokExample = `
// npm install ngrok

const ngrok = require('ngrok');

async function startTunnel() {
  try {
    const url = await ngrok.connect({
      proto: 'http',
      addr: 8080,
      authtoken: 'YOUR_AUTH_TOKEN'
    });
    
    console.log('隧道已建立:', url);
    
    const api = ngrok.getApi();
    const tunnels = await api.listTunnels();
    console.log('活跃隧道:', tunnels);
    
  } catch (error) {
    console.error('启动失败:', error);
  }
}

startTunnel();

// 关闭隧道
// ngrok.kill();
`;

console.log('\n=== Node.js ngrok 包示例 ===');
console.log(nodeNgrokExample);

// 6. ngrok Inspector (Web界面)
const inspectorFeatures = [
  '查看所有请求和响应',
  '重放请求',
  '修改请求重发',
  '查看请求详情（Headers、Body）',
  '导出请求日志'
];

console.log('\n=== Ngrok Inspector 功能 ===');
console.log('访问地址: http://127.0.0.1:4040');
inspectorFeatures.forEach(f => console.log(`  ✓ ${f}`));

// 7. 其他内网穿透工具
const otherTools = {
  frp: {
    特点: '开源免费，功能强大',
    官网: 'https://github.com/fatedier/frp',
    适用: '有公网服务器，可自行部署'
  },
  localtunnel: {
    特点: '简单易用，npm安装',
    官网: 'https://localtunnel.github.io/www/',
    命令: 'npx localtunnel --port 8080'
  },
  花生壳: {
    特点: '国内服务，稳定',
    官网: 'https://hsk.oray.com/',
    适用: '国内用户'
  },
  钉钉内网穿透: {
    特点: '免费，适合国内',
    官网: 'https://developers.dingtalk.com/',
    适用: '钉钉开发'
  }
};

console.log('\n=== 其他内网穿透工具 ===');
Object.entries(otherTools).forEach(([name, info]) => {
  console.log(`\n【${name}】`);
  console.log(`  特点: ${info.特点}`);
  console.log(`  官网: ${info.官网}`);
  if (info.命令) console.log(`  命令: ${info.命令}`);
  if (info.适用) console.log(`  适用: ${info.适用}`);
});

// 8. frp 配置示例
const frpConfig = `
# frps.ini (服务端)
[common]
bind_port = 7000
vhost_http_port = 80

# frpc.ini (客户端)
[common]
server_addr = your-server-ip
server_port = 7000

[web]
type = http
local_port = 8080
custom_domains = your-domain.com
`;

console.log('\n=== frp 配置示例 ===');
console.log(frpConfig);

// 9. 安全注意事项
const securityTips = [
  '⚠️  不要将本地数据库直接暴露到公网',
  '⚠️  生产环境不要使用免费工具的随机域名',
  '⚠️  注意保护Auth Token',
  '⚠️  测试完成后及时关闭隧道',
  '⚠️  使用HTTPS隧道传输敏感数据',
  '⚠️  配置访问限制和认证'
];

console.log('\n=== 安全注意事项 ===');
securityTips.forEach(tip => console.log(tip));

// 10. 调试技巧
const debugTips = [
  '使用 ngrok Inspector 查看请求详情',
  '检查本地服务是否正常启动',
  '确认端口没有被占用',
  '查看 ngrok 日志排查问题',
  '尝试重启 ngrok 隧道'
];

console.log('\n=== 调试技巧 ===');
debugTips.forEach((tip, i) => console.log(`${i + 1}. ${tip}`));

// 11. 快速开始指南
const quickStart = `
=== Ngrok 快速开始 ===

1. 注册账号: https://ngrok.com/
2. 获取 Authtoken: https://dashboard.ngrok.com/get-started/your-authtoken
3. 下载安装: https://ngrok.com/download
4. 配置认证: ngrok config add-authtoken YOUR_TOKEN
5. 启动隧道: ngrok http 8080
6. 访问公网地址: 复制显示的 Forwarding URL
7. 查看请求: 打开 http://127.0.0.1:4040
`;

console.log('\n' + quickStart);
