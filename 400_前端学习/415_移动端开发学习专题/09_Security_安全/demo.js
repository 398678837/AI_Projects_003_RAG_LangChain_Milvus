// 移动端安全示例代码

// 1. 数据加密
const dataEncryption = `
// 数据加密

// 1.1 加密算法选择
const encryptionAlgorithms = {
  // 对称加密
  symmetric: [
    { name: 'AES-256-GCM', keySize: 256, mode: 'GCM', authenticated: true },
    { name: 'AES-256-CBC', keySize: 256, mode: 'CBC', authenticated: false }
  ],
  
  // 非对称加密
  asymmetric: [
    { name: 'RSA-2048', keySize: 2048, use: '密钥交换' },
    { name: 'RSA-4096', keySize: 4096, use: '密钥交换' },
    { name: 'ECC-P256', keySize: 256, use: '密钥交换' }
  ],
  
  // 哈希算法
  hash: [
    { name: 'SHA-256', outputSize: 256 },
    { name: 'SHA-384', outputSize: 384 },
    { name: 'SHA-512', outputSize: 512 }
  ],
  
  // 密钥派生
  kdf: [
    { name: 'PBKDF2', iterations: 100000 },
    { name: 'Argon2', iterations: 3 }
  ]
};

// 1.2 Web Crypto API 加密
const webCryptoExample = \`
// 使用 Web Crypto API

// 生成 AES 密钥
async function generateAESKey() {
  const key = await crypto.subtle.generateKey(
    { name: 'AES-GCM', length: 256 },
    true,
    ['encrypt', 'decrypt']
  );
  return key;
}

// 加密
async function encrypt(data, key) {
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const encodedData = new TextEncoder().encode(data);
  
  const encrypted = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv },
    key,
    encodedData
  );
  
  return {
    iv: Array.from(iv),
    data: Array.from(new Uint8Array(encrypted))
  };
}

// 解密
async function decrypt(encrypted, key) {
  const iv = new Uint8Array(encrypted.iv);
  const data = new Uint8Array(encrypted.data);
  
  const decrypted = await crypto.subtle.decrypt(
    { name: 'AES-GCM', iv },
    key,
    data
  );
  
  return new TextDecoder().decode(decrypted);
}

// 导出密钥
async function exportKey(key) {
  const exported = await crypto.subtle.exportKey('raw', key);
  return Array.from(new Uint8Array(exported));
}

// 导入密钥
async function importKey(keyData) {
  const key = await crypto.subtle.importKey(
    'raw',
    new Uint8Array(keyData),
    { name: 'AES-GCM', length: 256 },
    true,
    ['encrypt', 'decrypt']
  );
  return key;
}

// 使用示例
async function example() {
  const key = await generateAESKey();
  const encrypted = await encrypt('敏感数据', key);
  const decrypted = await decrypt(encrypted, key);
  console.log('解密结果:', decrypted);
}
\`;

// 1.3 哈希和签名
const hashSignExample = \`
// 哈希和签名

// SHA-256 哈希
async function sha256(data) {
  const encoded = new TextEncoder().encode(data);
  const hashBuffer = await crypto.subtle.digest('SHA-256', encoded);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// PBKDF2 密钥派生
async function pbkdf2(password, salt, iterations = 100000) {
  const encoder = new TextEncoder();
  const passwordKey = await crypto.subtle.importKey(
    'raw',
    encoder.encode(password),
    { name: 'PBKDF2' },
    false,
    ['deriveBits', 'deriveKey']
  );
  
  const key = await crypto.subtle.deriveKey(
    {
      name: 'PBKDF2',
      salt: encoder.encode(salt),
      iterations,
      hash: 'SHA-256'
    },
    passwordKey,
    { name: 'AES-GCM', length: 256 },
    true,
    ['encrypt', 'decrypt']
  );
  
  return key;
}

// HMAC
async function hmac(data, secret) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw',
    encoder.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign', 'verify']
  );
  
  const signature = await crypto.subtle.sign(
    'HMAC',
    key,
    encoder.encode(data)
  );
  
  return Array.from(new Uint8Array(signature))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');
}

// 使用示例
async function example() {
  const hash = await sha256('要哈希的数据');
  console.log('SHA-256:', hash);
  
  const key = await pbkdf2('password123', 'somesalt');
  console.log('PBKDF2 Key:', key);
  
  const signature = await hmac('data', 'secret');
  console.log('HMAC:', signature);
}
\`;

console.log('=== 数据加密 ===');
console.log('加密算法:', encryptionAlgorithms);
console.log('Web Crypto API:', webCryptoExample);
console.log('哈希和签名:', hashSignExample);
`;

console.log('=== 数据加密 ===');
console.log(dataEncryption);

// 2. 安全存储
const secureStorage = `
// 安全存储

// 2.1 iOS Keychain
const iosKeychain = \`
// iOS Keychain (使用 react-native-keychain)

import * as Keychain from 'react-native-keychain';

// 存储凭据
async function saveCredentials(username, password) {
  await Keychain.setGenericPassword(username, password);
}

// 获取凭据
async function getCredentials() {
  const credentials = await Keychain.getGenericPassword();
  if (credentials) {
    return {
      username: credentials.username,
      password: credentials.password
    };
  }
  return null;
}

// 删除凭据
async function resetCredentials() {
  await Keychain.resetGenericPassword();
}

// 存储通用数据
async function saveSecureData(key, value) {
  await Keychain.setInternetCredentials(
    'myapp',
    key,
    JSON.stringify(value)
  );
}

// 获取通用数据
async function getSecureData(key) {
  const credentials = await Keychain.getInternetCredentials('myapp', key);
  if (credentials) {
    return JSON.parse(credentials.password);
  }
  return null;
}

// 生物识别
async function saveWithBiometrics(username, password) {
  await Keychain.setGenericPassword(
    username,
    password,
    {
      accessible: Keychain.ACCESSIBLE.WHEN_UNLOCKED_THIS_DEVICE_ONLY,
      accessControl: Keychain.ACCESS_CONTROL.BIOMETRY_CURRENT_SET_OR_DEVICE_PASSCODE
    }
  );
}

async function getWithBiometrics() {
  try {
    const credentials = await Keychain.getGenericPassword({
      authenticationPrompt: {
        title: 'Authentication required',
        subtitle: 'Please authenticate to access your credentials',
        description: 'We need your permission to retrieve your credentials',
        cancel: 'Cancel'
      }
    });
    return credentials;
  } catch (error) {
    console.log('Authentication failed:', error);
    return null;
  }
}
\`;

// 2.2 Android Keystore
const androidKeystore = \`
// Android Keystore (使用 react-native-keychain)

import * as Keychain from 'react-native-keychain';

// 存储凭据
async function saveCredentials(username, password) {
  await Keychain.setGenericPassword(
    username,
    password,
    {
      storage: Keychain.STORAGE_TYPE.RSA,
      accessible: Keychain.ACCESSIBLE.WHEN_UNLOCKED
    }
  );
}

// 获取凭据
async function getCredentials() {
  const credentials = await Keychain.getGenericPassword();
  return credentials;
}

// 使用 expo-secure-store
import * as SecureStore from 'expo-secure-store';

// 存储数据
async function saveSecure(key, value) {
  await SecureStore.setItemAsync(key, JSON.stringify(value), {
    requireAuthentication: true,
    authenticationPrompt: 'Authenticate to access'
  });
}

// 获取数据
async function getSecure(key) {
  const value = await SecureStore.getItemAsync(key);
  if (value) {
    return JSON.parse(value);
  }
  return null;
}

// 删除数据
async function deleteSecure(key) {
  await SecureStore.deleteItemAsync(key);
}
\`;

// 2.3 存储安全最佳实践
const storageBestPractices = [
  '使用系统提供的安全存储机制',
  '不要在 SharedPreferences/UserDefaults 中存储敏感数据',
  '不要在日志中输出敏感数据',
  '使用硬件安全模块 (HSM)',
  '密钥和数据分开存储',
  '定期轮换密钥',
  '应用卸载时清除所有数据',
  '使用证书锁定防止中间人攻击',
  '敏感数据在内存中使用后立即清除',
  '使用加密数据库 (如 SQLCipher)'
];

console.log('=== 安全存储 ===');
console.log('iOS Keychain:', iosKeychain);
console.log('Android Keystore:', androidKeystore);
console.log('最佳实践:', storageBestPractices);
`;

console.log('\n=== 安全存储 ===');
console.log(secureStorage);

// 3. 网络安全
const networkSecurity = `
// 网络安全

// 3.1 HTTPS 配置
const httpsConfig = {
  // iOS ATS 配置
  ios: \`
    <!-- Info.plist -->
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <false/>
        <key>NSExceptionDomains</key>
        <dict>
            <key>yourdomain.com</key>
            <dict>
                <key>NSIncludesSubdomains</key>
                <true/>
                <key>NSExceptionAllowsInsecureHTTPLoads</key>
                <false/>
                <key>NSExceptionMinimumTLSVersion</key>
                <string>TLSv1.2</string>
            </dict>
        </dict>
    </dict>
  \`,
  
  // Android 网络配置
  android: \`
    <!-- res/xml/network_security_config.xml -->
    <?xml version="1.0" encoding="utf-8"?>
    <network-security-config>
        <base-config cleartextTrafficPermitted="false">
            <trust-anchors>
                <certificates src="system" />
            </trust-anchors>
        </base-config>
        
        <domain-config cleartextTrafficPermitted="false">
            <domain includeSubdomains="true">yourdomain.com</domain>
            <pin-set expiration="2025-01-01">
                <pin digest="SHA-256">abc123...</pin>
                <pin digest="SHA-256">def456...</pin>
            </pin-set>
        </domain-config>
    </network-security-config>
    
    <!-- AndroidManifest.xml -->
    <application
        android:networkSecurityConfig="@xml/network_security_config"
        ...>
    </application>
  \`
};

// 3.2 证书锁定
const certificatePinning = \`
// 证书锁定

// 使用 react-native-ssl-pinning
import RNSslPinning from 'react-native-ssl-pinning';

const certs = [
  \`-----BEGIN CERTIFICATE-----
  ...
  -----END CERTIFICATE-----\`
];

RNSslPinning.fetch('https://yourdomain.com/api', {
  method: 'POST',
  body: JSON.stringify(data),
  sslPinning: {
    certs: certs
  },
  headers: {
    'Content-Type': 'application/json; charset=utf-8'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err => {
  if (err.message.includes('SSL')) {
    console.log('证书验证失败');
  }
});

// 使用 axios 拦截器
import axios from 'axios';
import https from 'https';

const instance = axios.create({
  httpsAgent: new https.Agent({
    rejectUnauthorized: true,
    checkServerIdentity: (host, cert) => {
      // 自定义证书验证
      const certFingerprint = getFingerprint(cert);
      const trustedFingerprints = ['...'];
      
      if (!trustedFingerprints.includes(certFingerprint)) {
        throw new Error('证书不受信任');
      }
    }
  })
});

function getFingerprint(cert) {
  // 计算证书指纹
  return crypto.createHash('sha256')
    .update(cert.raw)
    .digest('base64');
}
\`;

// 3.3 API 请求安全
const apiSecurity = \`
// API 请求安全

// 1. 请求签名
import crypto from 'crypto';

function signRequest(data, secret) {
  const timestamp = Date.now();
  const nonce = crypto.randomBytes(16).toString('hex');
  const payload = JSON.stringify(data);
  const signatureString = \`\${timestamp}\${nonce}\${payload}\`;
  
  const signature = crypto
    .createHmac('sha256', secret)
    .update(signatureString)
    .digest('hex');
  
  return {
    timestamp,
    nonce,
    signature,
    data
  };
}

// 2. Token 管理
class TokenManager {
  constructor() {
    this.accessToken = null;
    this.refreshToken = null;
    this.tokenExpiry = null;
  }
  
  async getAccessToken() {
    if (this.isTokenExpired()) {
      await this.refreshAccessToken();
    }
    return this.accessToken;
  }
  
  isTokenExpired() {
    if (!this.tokenExpiry) return true;
    return Date.now() > this.tokenExpiry - 60000; // 提前1分钟刷新
  }
  
  async refreshAccessToken() {
    const response = await fetch('/api/refresh-token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refreshToken: this.refreshToken })
    });
    
    const data = await response.json();
    this.accessToken = data.accessToken;
    this.tokenExpiry = Date.now() + data.expiresIn * 1000;
    
    if (data.refreshToken) {
      this.refreshToken = data.refreshToken;
      await this.saveRefreshToken(data.refreshToken);
    }
  }
  
  async saveRefreshToken(token) {
    await Keychain.setGenericPassword('refresh_token', token);
  }
}

// 3. 请求拦截器
import axios from 'axios';

const api = axios.create({ baseURL: 'https://yourdomain.com/api' });

api.interceptors.request.use(
  async (config) => {
    const tokenManager = new TokenManager();
    const token = await tokenManager.getAccessToken();
    
    if (token) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Token 过期，尝试刷新
      try {
        const tokenManager = new TokenManager();
        await tokenManager.refreshAccessToken();
        // 重试原请求
        return api(error.config);
      } catch (refreshError) {
        // 刷新失败，跳转到登录
        navigateToLogin();
      }
    }
    return Promise.reject(error);
  }
);
\`;

console.log('=== 网络安全 ===');
console.log('HTTPS配置:', httpsConfig);
console.log('证书锁定:', certificatePinning);
console.log('API安全:', apiSecurity);
`;

console.log('\n=== 网络安全 ===');
console.log(networkSecurity);

console.log('\n🎉 移动端安全学习完成！');
console.log('💡 安全是移动应用的基石，不容忽视！');
`;

console.log('\n=== 安全 ===');
