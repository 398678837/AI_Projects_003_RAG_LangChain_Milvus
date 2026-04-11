// Axios 最佳实践示例代码

// 1. 推荐的项目结构
const projectStructure = `
src/
├── api/
│   ├── index.ts              # Axios 实例创建
│   ├── types.ts              # 类型定义
│   ├── constants.ts          # 常量
│   ├── utils/
│   │   └── request.ts        # 请求工具
│   └── modules/
│       ├── user.ts           # 用户 API
│       ├── order.ts          # 订单 API
│       └── product.ts        # 产品 API
├── stores/
│   └── user.ts               # 用户状态
├── utils/
│   └── storage.ts            # 存储工具
└── main.ts
`;

console.log('=== 推荐的项目结构 ===');
console.log(projectStructure);

// 2. 统一的 API 配置
const apiConfig = `
// api/constants.ts
export const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://api.example.com';
export const API_TIMEOUT = 10000;
export const TOKEN_KEY = 'auth_token';
export const REFRESH_TOKEN_KEY = 'refresh_token';

// api/types.ts
export interface ApiResponse<T = any> {
  code: number;
  message: string;
  data: T;
}

export interface PageParams {
  page: number;
  pageSize: number;
}

export interface PageResult<T> {
  list: T[];
  total: number;
  page: number;
  pageSize: number;
}

export interface User {
  id: number;
  name: string;
  email: string;
}
`;

console.log('\n=== 统一的 API 配置 ===');
console.log(apiConfig);

// 3. 创建统一的请求实例
const requestInstance = `
// api/index.ts
import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';
import { API_BASE_URL, API_TIMEOUT, TOKEN_KEY } from './constants';
import type { ApiResponse } from './types';
import { ElMessage } from 'element-plus';

// 创建实例
const request: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json'
  }
});

// 请求拦截器
request.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    const token = localStorage.getItem(TOKEN_KEY);
    if (token && config.headers) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    return config;
  },
  (error: AxiosError) => Promise.reject(error)
);

// 响应拦截器
request.interceptors.response.use(
  <T>(response: AxiosResponse<ApiResponse<T>>) => {
    const { code, message, data } = response.data;
    
    if (code === 0) {
      return data as T;
    }
    
    ElMessage.error(message || '请求失败');
    return Promise.reject(new Error(message));
  },
  (error: AxiosError) => {
    if (error.response) {
      const { status } = error.response;
      
      switch (status) {
        case 401:
          localStorage.removeItem(TOKEN_KEY);
          window.location.href = '/login';
          break;
        case 403:
          ElMessage.error('没有权限访问');
          break;
        case 404:
          ElMessage.error('请求的资源不存在');
          break;
        case 500:
          ElMessage.error('服务器错误');
          break;
        default:
          ElMessage.error('请求失败');
      }
    } else if (error.code === 'ECONNABORTED') {
      ElMessage.error('请求超时');
    } else if (error.request) {
      ElMessage.error('网络连接失败');
    }
    
    return Promise.reject(error);
  }
);

export default request;
`;

console.log('\n=== 创建统一的请求实例 ===');
console.log(requestInstance);

// 4. API 模块封装
const apiModules = `
// api/modules/user.ts
import request from '../index';
import type { User, PageParams, PageResult } from '../types';

export interface CreateUserParams {
  name: string;
  email: string;
  password: string;
}

export interface UpdateUserParams extends Partial<CreateUserParams> {
  id: number;
}

export const userAPI = {
  getList: (params: PageParams): Promise<PageResult<User>> => {
    return request.get('/users', { params });
  },
  
  getDetail: (id: number): Promise<User> => {
    return request.get(\`/users/\${id}\`);
  },
  
  create: (data: CreateUserParams): Promise<User> => {
    return request.post('/users', data);
  },
  
  update: (data: UpdateUserParams): Promise<User> => {
    return request.put(\`/users/\${data.id}\`, data);
  },
  
  delete: (id: number): Promise<void> => {
    return request.delete(\`/users/\${id}\`);
  }
};

export default userAPI;

// api/modules/order.ts
import request from '../index';
import type { PageParams, PageResult } from '../types';

export interface Order {
  id: number;
  status: string;
  total: number;
}

export const orderAPI = {
  getList: (params: PageParams & { status?: string }): Promise<PageResult<Order>> => {
    return request.get('/orders', { params });
  },
  
  getDetail: (id: number): Promise<Order> => {
    return request.get(\`/orders/\${id}\`);
  },
  
  cancel: (id: number): Promise<void> => {
    return request.post(\`/orders/\${id}/cancel\`);
  }
};
`;

console.log('\n=== API 模块封装 ===');
console.log(apiModules);

// 5. 请求缓存
const requestCache = `
// api/utils/cache.ts
interface CacheItem<T> {
  data: T;
  expireTime: number;
}

class RequestCache {
  private cache = new Map<string, CacheItem<any>>();
  private defaultTTL = 5 * 60 * 1000; // 默认 5 分钟

  set<T>(key: string, data: T, ttl?: number): void {
    this.cache.set(key, {
      data,
      expireTime: Date.now() + (ttl || this.defaultTTL)
    });
  }

  get<T>(key: string): T | null {
    const item = this.cache.get(key);
    if (!item) return null;
    
    if (Date.now() > item.expireTime) {
      this.cache.delete(key);
      return null;
    }
    
    return item.data;
  }

  remove(key: string): void {
    this.cache.delete(key);
  }

  clear(): void {
    this.cache.clear();
  }
}

export const cache = new RequestCache();

// 使用缓存的请求
import { cache } from './utils/cache';

export const userAPI = {
  getList: async (params: PageParams, useCache = true) => {
    const key = \`users:\${JSON.stringify(params)}\`;
    
    if (useCache) {
      const cached = cache.get<PageResult<User>>(key);
      if (cached) {
        return cached;
      }
    }
    
    const data = await request.get('/users', { params });
    cache.set(key, data);
    return data;
  }
};
`;

console.log('\n=== 请求缓存 ===');
console.log(requestCache);

// 6. 请求防抖
const requestDebounce = `
// api/utils/debounce.ts
export function debounceRequest<T extends (...args: any[]) => any>(
  fn: T,
  delay = 300
): (...args: Parameters<T>) => Promise<ReturnType<T>> {
  let timeoutId: ReturnType<typeof setTimeout> | null = null;
  
  return (...args: Parameters<T>): Promise<ReturnType<T>> => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    
    return new Promise((resolve, reject) => {
      timeoutId = setTimeout(async () => {
        try {
          const result = await fn(...args);
          resolve(result);
        } catch (error) {
          reject(error);
        }
      }, delay);
    });
  };
}

// 使用
import { debounceRequest } from './utils/debounce';

const searchAPI = {
  search: debounceRequest(async (keyword: string) => {
    return request.get('/search', { params: { q: keyword } });
  }, 500)
};
`;

console.log('\n=== 请求防抖 ===');
console.log(requestDebounce);

// 7. 取消重复请求
const cancelDuplicate = `
// api/utils/pending.ts
import { AxiosRequestConfig } from 'axios';

const pendingRequests = new Map<string, AbortController>();

function getRequestKey(config: AxiosRequestConfig): string {
  const { method, url, params, data } = config;
  return [method, url, JSON.stringify(params), JSON.stringify(data)].join('&');
}

export function addPendingRequest(config: AxiosRequestConfig): void {
  const key = getRequestKey(config);
  
  if (pendingRequests.has(key)) {
    pendingRequests.get(key)?.abort();
  }
  
  const controller = new AbortController();
  config.signal = controller.signal;
  pendingRequests.set(key, controller);
}

export function removePendingRequest(config: AxiosRequestConfig): void {
  const key = getRequestKey(config);
  pendingRequests.delete(key);
}

export function cancelAllRequests(): void {
  pendingRequests.forEach(controller => controller.abort());
  pendingRequests.clear();
}

// 在拦截器中使用
request.interceptors.request.use(
  (config) => {
    addPendingRequest(config);
    return config;
  },
  (error) => Promise.reject(error)
);

request.interceptors.response.use(
  (response) => {
    removePendingRequest(response.config);
    return response;
  },
  (error) => {
    if (error.config) {
      removePendingRequest(error.config);
    }
    return Promise.reject(error);
  }
);
`;

console.log('\n=== 取消重复请求 ===');
console.log(cancelDuplicate);

// 8. Token 刷新
const tokenRefresh = `
// api/utils/refreshToken.ts
import { TOKEN_KEY, REFRESH_TOKEN_KEY } from '../constants';

let isRefreshing = false;
let refreshSubscribers: ((token: string) => void)[] = [];

function subscribeTokenRefresh(callback: (token: string) => void): void {
  refreshSubscribers.push(callback);
}

function onTokenRefreshed(token: string): void {
  refreshSubscribers.forEach(callback => callback(token));
  refreshSubscribers = [];
}

async function refreshToken(): Promise<string> {
  const refreshToken = localStorage.getItem(REFRESH_TOKEN_KEY);
  if (!refreshToken) {
    throw new Error('No refresh token');
  }
  
  const response = await axios.post('/auth/refresh', { refreshToken });
  const { token, refreshToken: newRefreshToken } = response.data;
  
  localStorage.setItem(TOKEN_KEY, token);
  localStorage.setItem(REFRESH_TOKEN_KEY, newRefreshToken);
  
  return token;
}

// 在响应拦截器中使用
request.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;
    
    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        return new Promise(resolve => {
          subscribeTokenRefresh(token => {
            originalRequest.headers.Authorization = \`Bearer \${token}\`;
            resolve(request(originalRequest));
          });
        });
      }
      
      originalRequest._retry = true;
      isRefreshing = true;
      
      try {
        const token = await refreshToken();
        onTokenRefreshed(token);
        originalRequest.headers.Authorization = \`Bearer \${token}\`;
        return request(originalRequest);
      } catch (refreshError) {
        localStorage.removeItem(TOKEN_KEY);
        localStorage.removeItem(REFRESH_TOKEN_KEY);
        window.location.href = '/login';
        return Promise.reject(refreshError);
      } finally {
        isRefreshing = false;
      }
    }
    
    return Promise.reject(error);
  }
);
`;

console.log('\n=== Token 刷新 ===');
console.log(tokenRefresh);

console.log('=== Axios 最佳实践 ===');
