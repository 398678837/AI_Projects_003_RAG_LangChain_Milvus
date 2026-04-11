// Axios 错误处理示例代码

// 1. 错误对象结构
const errorStructure = `
axios.get('/api/data')
  .catch(function (error) {
    if (error.response) {
      // 1. 请求已发出，服务器响应了，但状态码不是 2xx
      console.log('响应数据:', error.response.data);
      console.log('状态码:', error.response.status);
      console.log('响应头:', error.response.headers);
    } else if (error.request) {
      // 2. 请求已发出，但没有收到响应
      console.log('请求对象:', error.request);
    } else {
      // 3. 请求配置出错
      console.log('错误信息:', error.message);
    }
    
    // 4. 请求配置
    console.log('请求配置:', error.config);
  });
`;

console.log('=== 错误对象结构 ===');
console.log(errorStructure);

// 2. 不同状态码的处理
const statusCodeHandling = `
axios.get('/api/data')
  .catch(function (error) {
    if (error.response) {
      switch (error.response.status) {
        case 400:
          console.error('请求参数错误');
          break;
        case 401:
          console.error('未授权，请重新登录');
          localStorage.removeItem('token');
          window.location.href = '/login';
          break;
        case 403:
          console.error('没有权限访问');
          break;
        case 404:
          console.error('请求的资源不存在');
          break;
        case 408:
          console.error('请求超时');
          break;
        case 422:
          console.error('数据验证失败:', error.response.data.errors);
          break;
        case 429:
          console.error('请求过于频繁，请稍后再试');
          break;
        case 500:
          console.error('服务器内部错误');
          break;
        case 502:
          console.error('网关错误');
          break;
        case 503:
          console.error('服务暂时不可用');
          break;
        case 504:
          console.error('网关超时');
          break;
        default:
          console.error('请求失败:', error.response.status);
      }
    } else if (error.request) {
      console.error('网络错误，请检查网络连接');
    } else {
      console.error('请求配置错误:', error.message);
    }
  });
`;

console.log('\n=== 不同状态码的处理 ===');
console.log(statusCodeHandling);

// 3. 使用 async/await 处理错误
const asyncErrorHandling = `
async function fetchData() {
  try {
    const response = await axios.get('/api/data');
    console.log('成功:', response.data);
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('服务器错误:', error.response.status);
    } else if (error.request) {
      console.error('网络错误');
    } else {
      console.error('配置错误:', error.message);
    }
    throw error; // 继续抛出错误让上层处理
  }
}

// 使用
async function main() {
  try {
    const data = await fetchData();
  } catch (error) {
    console.error('最终错误处理');
  }
}
`;

console.log('\n=== 使用 async/await 处理错误 ===');
console.log(asyncErrorHandling);

// 4. 错误提示
const errorNotification = `
import { ElMessage } from 'element-plus';

axios.get('/api/data')
  .catch(function (error) {
    let message = '请求失败';
    
    if (error.response) {
      switch (error.response.status) {
        case 401:
          message = '登录已过期，请重新登录';
          break;
        case 403:
          message = '没有权限';
          break;
        case 404:
          message = '资源不存在';
          break;
        case 500:
          message = '服务器错误';
          break;
        default:
          message = error.response.data?.message || '请求失败';
      }
    } else if (error.code === 'ECONNABORTED') {
      message = '请求超时';
    } else if (error.request) {
      message = '网络连接失败';
    }
    
    ElMessage.error(message);
  });
`;

console.log('\n=== 错误提示 ===');
console.log(errorNotification);

// 5. 重试机制
const retryMechanism = `
// 简单的重试函数
async function requestWithRetry(config, retries = 3, delay = 1000) {
  try {
    return await axios(config);
  } catch (error) {
    if (retries > 0 && isRetryable(error)) {
      console.log(\`重试剩余 \${retries} 次...\`);
      await sleep(delay);
      return requestWithRetry(config, retries - 1, delay * 2); // 指数退避
    }
    throw error;
  }
}

function isRetryable(error) {
  // 网络错误或 5xx 错误可以重试
  return !error.response || error.response.status >= 500;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// 使用
requestWithRetry({ method: 'get', url: '/api/data' })
  .then(response => console.log('成功:', response.data))
  .catch(error => console.error('失败:', error));
`;

console.log('\n=== 重试机制 ===');
console.log(retryMechanism);

// 6. 使用 axios-retry 插件
const axiosRetryPlugin = `
import axios from 'axios';
import axiosRetry from 'axios-retry';

// 安装
// npm install axios-retry

// 配置
axiosRetry(axios, {
  retries: 3, // 重试次数
  retryDelay: (retryCount) => {
    return retryCount * 1000; // 每次重试间隔 1s, 2s, 3s
  },
  retryCondition: (error) => {
    // 网络错误或 5xx 错误重试
    return axiosRetry.isNetworkOrIdempotentRequestError(error);
  }
});

// 使用
axios.get('/api/data')
  .then(response => console.log('成功:', response.data))
  .catch(error => console.error('失败:', error));
`;

console.log('\n=== 使用 axios-retry 插件 ===');
console.log(axiosRetryPlugin);

// 7. 错误日志
const errorLogging = `
import axios from 'axios';

// 错误日志记录
function logError(error) {
  const errorInfo = {
    url: error.config?.url,
    method: error.config?.method,
    status: error.response?.status,
    message: error.message,
    timestamp: new Date().toISOString()
  };
  
  console.error('请求错误:', errorInfo);
  
  // 发送错误日志到服务器
  axios.post('/api/logs/error', errorInfo)
    .catch(() => {}); // 忽略日志请求的错误
}

// 在拦截器中使用
axios.interceptors.response.use(
  response => response,
  error => {
    logError(error);
    return Promise.reject(error);
  }
);
`;

console.log('\n=== 错误日志 ===');
console.log(errorLogging);

// 8. 完整的错误处理示例
const completeErrorHandling = `
import axios from 'axios';
import { ElMessage } from 'element-plus';

const api = axios.create({
  baseURL: '/api',
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
    } else {
      ElMessage.error(message || '请求失败');
      return Promise.reject(new Error(message));
    }
  },
  error => {
    let message = '请求失败';
    
    if (error.response) {
      const { status, data } = error.response;
      
      switch (status) {
        case 400:
          message = data?.message || '请求参数错误';
          break;
        case 401:
          message = '登录已过期，请重新登录';
          localStorage.removeItem('token');
          window.location.href = '/login';
          break;
        case 403:
          message = '没有权限';
          break;
        case 404:
          message = '资源不存在';
          break;
        case 500:
          message = '服务器错误';
          break;
        default:
          message = data?.message || '请求失败';
      }
    } else if (error.code === 'ECONNABORTED') {
      message = '请求超时';
    } else if (error.request) {
      message = '网络连接失败，请检查网络';
    } else {
      message = error.message;
    }
    
    ElMessage.error(message);
    return Promise.reject(error);
  }
);

export default api;
`;

console.log('\n=== 完整的错误处理示例 ===');
console.log(completeErrorHandling);

console.log('=== Axios 错误处理 ===');
