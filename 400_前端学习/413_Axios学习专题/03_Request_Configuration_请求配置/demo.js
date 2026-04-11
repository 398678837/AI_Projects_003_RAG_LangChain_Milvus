// Axios 请求配置示例代码

// 1. 完整的请求配置
const fullConfig = `
{
  // 请求地址
  url: '/user',
  
  // 请求方法
  method: 'get',
  
  // 基础 URL，会和 url 拼接
  baseURL: 'https://api.example.com',
  
  // 请求头
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token'
  },
  
  // URL 参数，会拼接到 URL
  params: {
    ID: 12345
  },
  
  // 请求体数据（POST/PUT/PATCH）
  data: {
    firstName: 'Fred'
  },
  
  // 超时时间（毫秒）
  timeout: 10000,
  
  // 跨域请求是否携带凭证
  withCredentials: false,
  
  // 响应数据类型
  responseType: 'json',
  
  // 响应编码
  responseEncoding: 'utf8',
  
  // xsrf 配置
  xsrfCookieName: 'XSRF-TOKEN',
  xsrfHeaderName: 'X-XSRF-TOKEN',
  
  // 上传进度
  onUploadProgress: function (progressEvent) {
    // 处理上传进度
  },
  
  // 下载进度
  onDownloadProgress: function (progressEvent) {
    // 处理下载进度
  },
  
  // 自定义状态码验证
  validateStatus: function (status) {
    return status >= 200 && status < 300;
  },
  
  // 最大重定向次数
  maxRedirects: 5,
  
  // HTTP 代理
  proxy: {
    host: '127.0.0.1',
    port: 9000
  }
}
`;

console.log('=== 完整的请求配置 ===');
console.log(fullConfig);

// 2. 全局默认配置
const globalDefaults = `
// 设置全局 baseURL
axios.defaults.baseURL = 'https://api.example.com';

// 设置全局超时
axios.defaults.timeout = 5000;

// 设置全局请求头
axios.defaults.headers.common['Authorization'] = 'Bearer token';
axios.defaults.headers.post['Content-Type'] = 'application/json';

// 设置全局 withCredentials
axios.defaults.withCredentials = true;

// 使用全局配置
axios.get('/users')  // 实际请求: https://api.example.com/users
axios.post('/users', { name: 'John' });
`;

console.log('\n=== 全局默认配置 ===');
console.log(globalDefaults);

// 3. 配置示例
async function configExamples() {
  console.log('\n=== 配置示例 ===');
  
  // 示例 1: 带参数的 GET 请求
  console.log('\n--- 带参数的 GET 请求 ---');
  const getWithParams = `
axios.get('https://api.example.com/users', {
  params: {
    page: 1,
    limit: 10,
    sort: 'name',
    order: 'asc'
  },
  headers: {
    'Authorization': 'Bearer my-token'
  },
  timeout: 10000
})
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
`;
  console.log(getWithParams);
  
  // 示例 2: POST 请求带数据
  console.log('\n--- POST 请求带数据 ---');
  const postWithData = `
axios.post('https://api.example.com/users', {
  name: 'John Doe',
  email: 'john@example.com',
  age: 30
}, {
  headers: {
    'Content-Type': 'application/json',
    'X-Custom-Header': 'value'
  },
  timeout: 8000
})
  .then(response => console.log('创建成功:', response.data))
  .catch(error => console.error(error));
`;
  console.log(postWithData);
  
  // 示例 3: 文件上传
  console.log('\n--- 文件上传 ---');
  const fileUpload = `
const formData = new FormData();
formData.append('avatar', fileInput.files[0]);
formData.append('userId', '123');

axios.post('https://api.example.com/upload', formData, {
  headers: {
    'Content-Type': 'multipart/form-data'
  },
  onUploadProgress: (progressEvent) => {
    const percent = Math.round(
      (progressEvent.loaded * 100) / progressEvent.total
    );
    console.log(\`上传进度: \${percent}%\`);
  }
})
  .then(response => console.log('上传成功'))
  .catch(error => console.error(error));
`;
  console.log(fileUpload);
}

// 4. 配置优先级
const configPriority = `
// 配置优先级（从高到低）:
// 1. 请求配置
// 2. 实例配置
// 3. 全局配置
// 4. 默认配置

// 全局配置
axios.defaults.baseURL = 'https://api.example.com';
axios.defaults.timeout = 5000;

// 实例配置
const instance = axios.create({
  baseURL: 'https://api.instance.com',
  timeout: 8000
});

// 请求配置（优先级最高）
instance.get('/users', {
  timeout: 10000  // 覆盖实例和全局配置
});
`;

console.log('\n=== 配置优先级 ===');
console.log(configPriority);

// 5. 动态配置 baseURL
const dynamicBaseURL = `
// 根据环境设置 baseURL
const getBaseURL = () => {
  if (import.meta.env.DEV) {
    return 'http://localhost:3000/api';
  } else if (import.meta.env.MODE === 'staging') {
    return 'https://staging.example.com/api';
  } else {
    return 'https://api.example.com';
  }
};

axios.defaults.baseURL = getBaseURL();

// 或者使用环境变量
// .env
// VITE_API_BASE_URL=https://api.example.com

axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL;
`;

console.log('\n=== 动态配置 baseURL ===');
console.log(dynamicBaseURL);

// 6. 认证配置
const authConfig = `
// 方式 1: 使用 auth 配置
axios.get('/api/data', {
  auth: {
    username: 'user',
    password: 'pass'
  }
});

// 方式 2: 使用 Authorization header
axios.get('/api/data', {
  headers: {
    'Authorization': 'Basic ' + btoa('user:pass')
  }
});

// 方式 3: Bearer Token
axios.get('/api/data', {
  headers: {
    'Authorization': 'Bearer ' + token
  }
});

// 方式 4: 全局设置
axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
`;

console.log('\n=== 认证配置 ===');
console.log(authConfig);

// 7. 完整的配置示例
const completeConfigExample = `
// 创建一个完整配置的实例
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'https://api.example.com',
  timeout: 10000,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// 用户 API
const userAPI = {
  getUsers: (params) => api.get('/users', { params }),
  getUser: (id) => api.get(\`/users/\${id}\`),
  createUser: (data) => api.post('/users', data),
  updateUser: (id, data) => api.put(\`/users/\${id}\`, data),
  deleteUser: (id) => api.delete(\`/users/\${id}\`)
};

// 使用
userAPI.getUsers({ page: 1, limit: 10 })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
`;

console.log('\n=== 完整的配置示例 ===');
console.log(completeConfigExample);

console.log('=== Axios 请求配置 ===');
