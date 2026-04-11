// 跨域问题排查示例代码

// 1. 常见 CORS 错误及解决方案
const corsErrors = [
  {
    错误: 'Access to fetch at "..." from origin "..." has been blocked by CORS policy: No "Access-Control-Allow-Origin" header is present on the requested resource.',
    原因: '响应头缺少 Access-Control-Allow-Origin',
    解决: [
      '后端配置 CORS，添加该响应头',
      '使用代理服务器',
      '检查 Origin 是否在白名单'
    ]
  },
  {
    错误: 'Access to fetch at "..." from origin "..." has been blocked by CORS policy: The value of the "Access-Control-Allow-Origin" header in the response must not be the wildcard "*" when the request\'s credentials mode is "include".',
    原因: 'withCredentials=true 时，Origin 不能是 *',
    解决: [
      '将 Origin 设置为具体域名，而非 *',
      '如果不需要凭证，去掉 credentials: "include"',
      '使用动态 Origin 白名单'
    ]
  },
  {
    错误: 'Access to fetch at "..." from origin "..." has been blocked by CORS policy: Method XXX is not allowed by Access-Control-Allow-Methods in preflight response.',
    原因: '请求方法不在 Allow-Methods 中',
    解决: [
      '后端添加该方法到 Access-Control-Allow-Methods',
      '检查是否需要该方法，或改用允许的方法'
    ]
  },
  {
    错误: 'Access to fetch at "..." from origin "..." has been blocked by CORS policy: Request header field XXX is not allowed by Access-Control-Allow-Headers in preflight response.',
    原因: '自定义头不在 Allow-Headers 中',
    解决: [
      '后端添加该头到 Access-Control-Allow-Headers',
      '确认是否真的需要该自定义头'
    ]
  },
  {
    错误: 'Response to preflight request doesn\'t pass access control check: It does not have HTTP ok status.',
    原因: 'OPTIONS 预检请求返回非 200 状态码',
    解决: [
      '后端正确处理 OPTIONS 请求，返回 200 或 204',
      '检查后端路由是否匹配'
    ]
  }
];

console.log('=== 常见 CORS 错误 ===');
corsErrors.forEach((item, i) => {
  console.log(`\n${i + 1}. 错误:`);
  console.log(`   ${item.错误}`);
  console.log(`   原因: ${item.原因}`);
  console.log(`   解决:`);
  item.解决.forEach(s => console.log(`     ✓ ${s}`));
});

// 2. 代理问题排查
const proxyIssues = [
  {
    问题: '代理不生效，还是报 CORS 错误',
    排查: [
      '检查请求 URL 是否匹配代理前缀',
      '确认开发服务器已重启',
      '查看 Network 面板，请求是否发给了代理',
      '确认代理配置语法正确'
    ]
  },
  {
    问题: '代理请求返回 404 Not Found',
    排查: [
      '检查 pathRewrite/rewrite 配置',
      '去掉 pathRewrite 测试看是否是路径问题',
      '确认目标服务器路径是否正确',
      '查看代理转发后的完整 URL'
    ]
  },
  {
    问题: '504 Gateway Timeout',
    排查: [
      '确认目标服务已启动',
      '检查目标端口是否正确',
      '确认网络连通性',
      '增加代理超时时间'
    ]
  },
  {
    问题: 'POST 请求变成 GET',
    排查: [
      '检查是否有重定向 (301/302)',
      '确认目标服务器是否强制 HTTPS',
      '查看 Network 面板的请求链'
    ]
  }
];

console.log('\n=== 代理问题排查 ===');
proxyIssues.forEach((item, i) => {
  console.log(`\n${i + 1}. 问题: ${item.问题}`);
  console.log(`   排查:`);
  item.排查.forEach(c => console.log(`     - ${c}`));
});

// 3. 排查步骤清单
const troubleshootingSteps = [
  {
    步骤: '1. 确认问题',
    操作: [
      '打开浏览器 Console',
      '查看错误信息',
      '确认是否有 CORS 关键词'
    ]
  },
  {
    步骤: '2. 检查 Network',
    操作: [
      '打开 Network 面板',
      '找到失败的请求',
      '查看 Request/Response 详情',
      '检查是否有预检请求 (OPTIONS)'
    ]
  },
  {
    步骤: '3. 简化场景',
    操作: [
      '去掉自定义头',
      '改用 GET 请求',
      '去掉 credentials',
      '用 Postman/curl 直接测试后端'
    ]
  },
  {
    步骤: '4. 验证配置',
    操作: [
      '检查后端 CORS 配置',
      '确认 Origin 白名单',
      '验证 Methods/Headers 配置',
      '检查代理配置 (开发环境)'
    ]
  },
  {
    步骤: '5. 查看日志',
    操作: [
      '后端日志',
      '代理日志',
      'Nginx 访问/错误日志'
    ]
  }
];

console.log('\n=== 排查步骤 ===');
troubleshootingSteps.forEach(step => {
  console.log(`\n${step.步骤}`);
  step.操作.forEach(op => console.log(`  - ${op}`));
});

// 4. 浏览器 DevTools 使用技巧
const devtoolsTips = {
  Network面板: [
    '勾选 "Preserve log" 保留日志',
    'Filter 输入 "cors" 过滤相关请求',
    '查看请求的 Headers 标签',
    '检查 Response 标签看服务器返回',
    '注意请求是否标红 (失败)'
  ],
  Console面板: [
    '错误信息会直接显示',
    '点击错误链接跳转到 Network',
    '使用 console.log 调试'
  ],
  Application面板: [
    '查看 Cookies 是否正确设置',
    '检查 SameSite 属性',
    '清除 Storage 重试'
  ]
};

console.log('\n=== DevTools 技巧 ===');
Object.entries(devtoolsTips).forEach(([panel, tips]) => {
  console.log(`\n【${panel}】`);
  tips.forEach(tip => console.log(`  ✓ ${tip}`));
});

// 5. 抓包工具使用
const packetCapture = {
  Charles: {
    作用: 'HTTP/HTTPS 代理调试',
    功能: [
      '查看请求响应详情',
      '修改请求/响应',
      '重放请求',
      'HTTPS 解密'
    ],
    适用: '移动端调试、线上问题'
  },
  Fiddler: {
    作用: 'Web 调试代理',
    功能: [
      '类似 Charles',
      'Windows 平台常用',
      '强大的脚本功能'
    ],
    适用: 'Windows 开发'
  },
  Wireshark: {
    作用: '网络包分析',
    功能: [
      '底层网络包',
      'TCP/UDP 分析',
      '深入调试网络问题'
    ],
    适用: '复杂网络问题'
  }
};

console.log('\n=== 抓包工具 ===');
Object.entries(packetCapture).forEach(([tool, info]) => {
  console.log(`\n【${tool}】`);
  console.log(`  作用: ${info.作用}`);
  console.log(`  功能: ${info.功能.join(', ')}`);
  console.log(`  适用: ${info.适用}`);
});

// 6. 常用测试命令
const testCommands = {
  curl: `
# 测试后端是否正常
curl -v http://localhost:3000/api/users

# 测试 CORS 头
curl -I -X OPTIONS \\
  -H "Origin: http://localhost:5173" \\
  -H "Access-Control-Request-Method: GET" \\
  http://localhost:3000/api/users
`,
  Postman: `
1. 创建请求
2. 发送到后端地址
3. 查看响应
4. 在 Headers 标签查看 CORS 头
5. 排除前端问题，确认后端正常
`
};

console.log('\n=== 测试命令 ===');
console.log('【curl】');
console.log(testCommands.curl);
console.log('【Postman】');
console.log(testCommands.Postman);

// 7. 常见误区
const commonMistakes = [
  '❌ 只看前端错误，不检查后端是否正常',
  '❌ 改了配置不重启服务',
  '❌ 复制粘贴配置，不理解含义',
  '❌ 不看完整错误信息，只看开头',
  '❌ 同时尝试多种方案，不知道哪个生效',
  '❌ 怀疑是跨域，但其实是其他问题 (404/500)',
  '❌ 生产环境照搬开发环境配置'
];

console.log('\n=== 常见误区 ===');
commonMistakes.forEach(mistake => console.log(mistake));

// 8. 快速验证清单
const quickChecklist = [
  {
    问题: '是跨域问题吗？',
    检查: 'Console 有 CORS 错误吗？'
  },
  {
    问题: '后端正常吗？',
    检查: '用 Postman/curl 直接调用后端'
  },
  {
    问题: '配置生效了吗？',
    检查: '重启服务了吗？'
  },
  {
    问题: 'Origin 对吗？',
    检查: 'Response 有 Allow-Origin 吗？'
  },
  {
    问题: '用代理了吗？',
    检查: '请求 URL 是代理地址吗？'
  }
];

console.log('\n=== 快速验证清单 ===');
quickChecklist.forEach((item, i) => {
  console.log(`${i + 1}. ${item.问题}`);
  console.log(`   → ${item.检查}`);
});

// 9. 简化问题方法
function simplifyProblem() {
  console.log('\n=== 简化问题方法 ===');
  
  const steps = [
    '1. 创建一个最简单的测试页面',
    '   <script>fetch("http://localhost:3000/test")</script>',
    '',
    '2. 后端创建最简单的接口',
    '   app.get("/test", (req, res) => res.json({ ok: true }))',
    '',
    '3. 先让简单的跑通',
    '',
    '4. 再逐步添加复杂功能（自定义头、凭证等）'
  ];
  
  steps.forEach(step => console.log(step));
}

simplifyProblem();
