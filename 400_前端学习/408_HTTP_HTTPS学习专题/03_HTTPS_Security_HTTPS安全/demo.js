// HTTPS 安全示例代码

// 1. HTTPS vs HTTP 对比
const httpsVsHttp = {
  安全性: {
    HTTP: '明文传输，易被窃听和篡改',
    HTTPS: '加密传输，安全可靠'
  },
  端口: {
    HTTP: 80,
    HTTPS: 443
  },
  证书: {
    HTTP: '不需要',
    HTTPS: '需要SSL/TLS证书'
  },
  性能: {
    HTTP: '较快，无需加密解密',
    HTTPS: '稍慢，有加密解密开销'
  },
  SEO: {
    HTTP: '搜索引擎不优先',
    HTTPS: '搜索引擎优先收录'
  }
};

console.log('HTTPS vs HTTP 对比:', httpsVsHttp);

// 2. 简单的加密解密模拟（演示概念）
function simpleEncryptionDemo() {
  console.log('\n=== 加密解密演示 ===');
  
  const message = '这是一条敏感信息';
  console.log('原始消息:', message);
  
  const simpleEncrypt = (text, key) => {
    return text.split('').map(char => 
      String.fromCharCode(char.charCodeAt(0) + key)
    ).join('');
  };
  
  const simpleDecrypt = (text, key) => {
    return text.split('').map(char => 
      String.fromCharCode(char.charCodeAt(0) - key)
    ).join('');
  };
  
  const key = 5;
  const encrypted = simpleEncrypt(message, key);
  console.log('加密后:', encrypted);
  
  const decrypted = simpleDecrypt(encrypted, key);
  console.log('解密后:', decrypted);
}

simpleEncryptionDemo();

// 3. 数字证书信息展示
const certificateInfo = {
  subject: {
    commonName: 'www.example.com',
    organization: 'Example Inc',
    country: 'CN'
  },
  issuer: {
    commonName: 'Example CA',
    organization: 'Certificate Authority'
  },
  validFrom: '2024-01-01',
  validTo: '2026-01-01',
  publicKeyAlgorithm: 'RSA',
  signatureAlgorithm: 'SHA256withRSA'
};

console.log('\n数字证书信息:', certificateInfo);

// 4. TLS 握手过程演示
function tlsHandshakeDemo() {
  console.log('\n=== TLS 握手过程 ===');
  
  const steps = [
    '1. Client Hello: 客户端发送支持的TLS版本、加密套件、随机数',
    '2. Server Hello: 服务器选择TLS版本、加密套件、发送随机数',
    '3. Certificate: 服务器发送数字证书',
    '4. Server Hello Done: 服务器问候完成',
    '5. Client Key Exchange: 客户端生成预主密钥，用服务器公钥加密发送',
    '6. Change Cipher Spec: 客户端切换到加密模式',
    '7. Finished: 客户端发送加密的握手完成消息',
    '8. Change Cipher Spec: 服务器切换到加密模式',
    '9. Finished: 服务器发送加密的握手完成消息',
    '10. 加密通信: 开始加密数据传输'
  ];
  
  steps.forEach(step => console.log(step));
}

tlsHandshakeDemo();

// 5. 检查URL是否使用HTTPS
function isHttps(url) {
  try {
    const urlObj = new URL(url);
    return urlObj.protocol === 'https:';
  } catch {
    return false;
  }
}

console.log('\n检查HTTPS:');
console.log('https://example.com:', isHttps('https://example.com'));
console.log('http://example.com:', isHttps('http://example.com'));

// 6. 常见的安全头
const securityHeaders = {
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
  'Content-Security-Policy': "default-src 'self'",
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'X-XSS-Protection': '1; mode=block'
};

console.log('\n常见安全头:', securityHeaders);

// 7. 使用HTTPS的fetch请求
async function httpsFetchExample() {
  console.log('\n=== HTTPS Fetch 示例 ===');
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const data = await response.json();
    console.log('HTTPS请求成功:', data);
    console.log('协议:', response.url.split(':')[0]);
  } catch (error) {
    console.error('HTTPS请求错误:', error);
  }
}

httpsFetchExample();
