// Axios 实例示例代码

// 1. 创建基本实例
const basicInstance = `
import axios from 'axios';

// 创建实例
const instance = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000
});

// 使用实例
instance.get('/users')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));

instance.post('/users', { name: 'John' })
  .then(response => console.log(response.data));
`;

console.log('=== 创建基本实例 ===');
console.log(basicInstance);

// 2. 完整配置的实例
const fullConfigInstance = `
import axios from 'axios';

const api = axios.create({
  // 基础 URL
  baseURL: import.meta.env.VITE_API_URL || 'https://api.example.com',
  
  // 超时时间
  timeout: 10000,
  
  // 请求头
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  },
  
  // 跨域携带凭证
  withCredentials: true,
  
  // 响应类型
  responseType: 'json',
  
  // 自定义状态码验证
  validateStatus: status => status >= 200 && status < 300
});

export default api;
`;

console.log('\n=== 完整配置的实例 ===');
console.log(fullConfigInstance);

// 3. 多个实例
const multipleInstances = `
import axios from 'axios';

// 主 API 实例
const api = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000
});

// 文件上传实例
const uploadApi = axios.create({
  baseURL: 'https://upload.example.com',
  timeout: 30000,
  headers: {
    'Content-Type': 'multipart/form-data'
  }
});

// 第三方 API 实例
const thirdPartyApi = axios.create({
  baseURL: 'https://third-party.example.com',
  timeout: 5000
});

// 使用
api.get('/users');
uploadApi.post('/upload', formData);
thirdPartyApi.get('/data');

export { api, uploadApi, thirdPartyApi };
`;

console.log('\n=== 多个实例 ===');
console.log(multipleInstances);

// 4. 实例的拦截器
const instanceInterceptors = `
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com'
});

// 实例的请求拦截器
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    return config;
  },
  error => Promise.reject(error)
);

// 实例的响应拦截器
api.interceptors.response.use(
  response => response.data,
  error => {
    if (error.response?.status === 401) {
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
`;

console.log('\n=== 实例的拦截器 ===');
console.log(instanceInterceptors);

// 5. 实例方法
const instanceMethods = `
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com'
});

// 所有方法都可用
api.get('/users');
api.post('/users', data);
api.put('/users/1', data);
api.patch('/users/1', data);
api.delete('/users/1');
api.head('/users/1');
api.options('/users');
api.request({ method: 'get', url: '/users' });
`;

console.log('\n=== 实例方法 ===');
console.log(instanceMethods);

// 6. 修改实例默认配置
const modifyInstanceConfig = `
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000
});

// 修改实例的默认配置
api.defaults.baseURL = 'https://new-api.example.com';
api.defaults.timeout = 5000;
api.defaults.headers.common['Authorization'] = 'Bearer new-token';

console.log('新的 baseURL:', api.defaults.baseURL);
`;

console.log('\n=== 修改实例默认配置 ===');
console.log(modifyInstanceConfig);

// 7. 封装 API 模块
const apiModule = `
import axios from 'axios';

// 创建实例
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000
});

// 请求拦截器
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    return config;
  },
  error => Promise.reject(error)
);

// 响应拦截器
api.interceptors.response.use(
  response => {
    const { code, message, data } = response.data;
    if (code === 0) {
      return data;
    }
    return Promise.reject(new Error(message || '请求失败'));
  },
  error => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// 用户 API
export const userAPI = {
  getList: (params) => api.get('/users', { params }),
  getDetail: (id) => api.get(\`/users/\${id}\`),
  create: (data) => api.post('/users', data),
  update: (id, data) => api.put(\`/users/\${id}\`, data),
  delete: (id) => api.delete(\`/users/\${id}\`)
};

// 订单 API
export const orderAPI = {
  getList: (params) => api.get('/orders', { params }),
  getDetail: (id) => api.get(\`/orders/\${id}\`),
  create: (data) => api.post('/orders', data),
  cancel: (id) => api.post(\`/orders/\${id}/cancel\`)
};

export default api;
`;

console.log('\n=== 封装 API 模块 ===');
console.log(apiModule);

// 8. 使用封装的 API
const useApi = `
import { userAPI, orderAPI } from './api';

// 获取用户列表
async function fetchUsers() {
  try {
    const users = await userAPI.getList({ page: 1, limit: 10 });
    console.log('用户列表:', users);
  } catch (error) {
    console.error('获取用户列表失败:', error);
  }
}

// 创建用户
async function createUser(userData) {
  try {
    const user = await userAPI.create(userData);
    console.log('创建成功:', user);
  } catch (error) {
    console.error('创建失败:', error);
  }
}

// 获取订单列表
async function fetchOrders() {
  try {
    const orders = await orderAPI.getList({ status: 'pending' });
    console.log('订单列表:', orders);
  } catch (error) {
    console.error('获取订单列表失败:', error);
  }
}
`;

console.log('\n=== 使用封装的 API ===');
console.log(useApi);

// 9. 全局配置 vs 实例配置
const globalVsInstance = `
// 全局配置
axios.defaults.baseURL = 'https://global.example.com';
axios.defaults.timeout = 10000;

// 实例配置
const instance = axios.create({
  baseURL: 'https://instance.example.com',  // 覆盖全局
  timeout: 5000                             // 覆盖全局
});

// 请求配置（优先级最高）
instance.get('/users', {
  timeout: 8000  // 覆盖实例配置
});

// 优先级：请求配置 > 实例配置 > 全局配置
`;

console.log('\n=== 全局配置 vs 实例配置 ===');
console.log(globalVsInstance);

console.log('=== Axios 实例 ===');
