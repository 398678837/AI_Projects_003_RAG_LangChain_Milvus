// Axios 拦截器示例代码

// 1. 请求拦截器
const requestInterceptor = `
// 添加请求拦截器
axios.interceptors.request.use(
  function (config) {
    // 在发送请求之前做些什么
    console.log('请求拦截器 - 发送请求:', config.url);
    
    // 添加 token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    
    // 添加时间戳
    config.params = {
      ...config.params,
      _t: Date.now()
    };
    
    return config;
  },
  function (error) {
    // 对请求错误做些什么
    console.error('请求拦截器 - 请求错误:', error);
    return Promise.reject(error);
  }
);
`;

console.log('=== 请求拦截器 ===');
console.log(requestInterceptor);

// 2. 响应拦截器
const responseInterceptor = `
// 添加响应拦截器
axios.interceptors.response.use(
  function (response) {
    // 2xx 范围内的状态码都会触发该函数
    console.log('响应拦截器 - 响应成功:', response.status);
    
    // 直接返回 data
    return response.data;
  },
  function (error) {
    // 超出 2xx 范围的状态码都会触发该函数
    console.error('响应拦截器 - 响应错误:', error.response?.status);
    
    // 统一错误处理
    if (error.response) {
      // 服务器响应了，但状态码不在 2xx 范围内
      switch (error.response.status) {
        case 400:
          console.error('请求错误');
          break;
        case 401:
          console.error('未授权，请重新登录');
          localStorage.removeItem('token');
          window.location.href = '/login';
          break;
        case 403:
          console.error('拒绝访问');
          break;
        case 404:
          console.error('请求的资源不存在');
          break;
        case 500:
          console.error('服务器错误');
          break;
        default:
          console.error('请求失败');
      }
    } else if (error.request) {
      // 请求已发出，但没有收到响应
      console.error('网络错误，请稍后重试');
    } else {
      // 发送请求时出了问题
      console.error('请求配置错误:', error.message);
    }
    
    return Promise.reject(error);
  }
);
`;

console.log('\n=== 响应拦截器 ===');
console.log(responseInterceptor);

// 3. 多个拦截器
const multipleInterceptors = `
// 可以添加多个拦截器

// 请求拦截器 1
axios.interceptors.request.use(config => {
  console.log('请求拦截器 1');
  return config;
});

// 请求拦截器 2
axios.interceptors.request.use(config => {
  console.log('请求拦截器 2');
  return config;
});

// 响应拦截器 1
axios.interceptors.response.use(response => {
  console.log('响应拦截器 1');
  return response;
});

// 响应拦截器 2
axios.interceptors.response.use(response => {
  console.log('响应拦截器 2');
  return response;
});

// 执行顺序：
// 请求拦截器：2 -> 1（后添加的先执行）
// 响应拦截器：1 -> 2（先添加的先执行）
`;

console.log('\n=== 多个拦截器 ===');
console.log(multipleInterceptors);

// 4. 移除拦截器
const removeInterceptor = `
// 添加拦截器时保存 ID
const requestInterceptorId = axios.interceptors.request.use(config => {
  console.log('请求拦截器');
  return config;
});

const responseInterceptorId = axios.interceptors.response.use(response => {
  console.log('响应拦截器');
  return response;
});

// 移除拦截器
axios.interceptors.request.eject(requestInterceptorId);
axios.interceptors.response.eject(responseInterceptorId);
`;

console.log('\n=== 移除拦截器 ===');
console.log(removeInterceptor);

// 5. 完整的拦截器示例
const completeInterceptors = `
import axios from 'axios';

// 创建实例
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000
});

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 添加 token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    
    // 添加请求 ID
    config.headers['X-Request-ID'] = Date.now().toString(36) + Math.random().toString(36).substr(2);
    
    // 显示加载状态
    store.commit('setLoading', true);
    
    console.log('请求:', config.method?.toUpperCase(), config.url);
    
    return config;
  },
  (error) => {
    store.commit('setLoading', false);
    return Promise.reject(error);
  }
);

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    store.commit('setLoading', false);
    
    console.log('响应:', response.status, response.config.url);
    
    // 统一返回格式处理
    if (response.data && response.data.code === 0) {
      return response.data.data;
    } else {
      return Promise.reject(new Error(response.data?.message || '请求失败'));
    }
  },
  (error) => {
    store.commit('setLoading', false);
    
    console.error('请求错误:', error);
    
    // 错误处理
    if (error.response) {
      const { status, data } = error.response;
      
      switch (status) {
        case 401:
          localStorage.removeItem('token');
          window.location.href = '/login';
          break;
        case 403:
          alert('没有权限访问');
          break;
        case 404:
          alert('请求的资源不存在');
          break;
        case 500:
          alert('服务器错误，请稍后重试');
          break;
        default:
          alert(data?.message || '请求失败');
      }
    } else if (error.request) {
      alert('网络错误，请检查网络连接');
    } else {
      alert('请求配置错误');
    }
    
    return Promise.reject(error);
  }
);

export default api;
`;

console.log('\n=== 完整的拦截器示例 ===');
console.log(completeInterceptors);

// 6. 实例的拦截器
const instanceInterceptors = `
// 全局拦截器会影响所有请求
axios.interceptors.request.use(config => {
  console.log('全局拦截器');
  return config;
});

// 实例拦截器只影响该实例
const instance = axios.create();
instance.interceptors.request.use(config => {
  console.log('实例拦截器');
  return config;
});

// 执行顺序：
// 实例拦截器 -> 全局拦截器
`;

console.log('\n=== 实例的拦截器 ===');
console.log(instanceInterceptors);

console.log('=== Axios 拦截器 ===');
