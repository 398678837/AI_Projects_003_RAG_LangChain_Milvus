// Axios + TypeScript 示例代码

// 1. 基本类型使用
const basicTypes = `
import axios, { AxiosResponse, AxiosError } from 'axios';

// 定义响应数据类型
interface User {
  id: number;
  name: string;
  email: string;
}

// 使用泛型指定响应类型
async function getUser(id: number): Promise<User> {
  const response: AxiosResponse<User> = await axios.get<User>(
    \`https://api.example.com/users/\${id}\`
  );
  return response.data;
}

// 使用
async function main() {
  try {
    const user = await getUser(1);
    console.log(user.name);  // 类型安全
  } catch (error) {
    const axiosError = error as AxiosError;
    console.error(axiosError.message);
  }
}
`;

console.log('=== 基本类型使用 ===');
console.log(basicTypes);

// 2. 定义 API 响应类型
const responseTypes = `
// 通用的 API 响应类型
interface ApiResponse<T = any> {
  code: number;
  message: string;
  data: T;
}

// 用户类型
interface User {
  id: number;
  name: string;
  email: string;
  avatar?: string;
}

// 分页类型
interface Page<T> {
  list: T[];
  total: number;
  page: number;
  pageSize: number;
}

// 使用
async function getUsers(params: { page: number; pageSize: number }) {
  const response = await axios.get<ApiResponse<Page<User>>>(
    '/api/users',
    { params }
  );
  
  const { code, message, data } = response.data;
  
  if (code === 0) {
    return data;
  }
  
  throw new Error(message);
}
`;

console.log('\n=== 定义 API 响应类型 ===');
console.log(responseTypes);

// 3. 创建类型安全的实例
const typedInstance = `
import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';

// API 响应类型
interface ApiResponse<T = any> {
  code: number;
  message: string;
  data: T;
}

// 创建实例
const api: AxiosInstance = axios.create({
  baseURL: '/api',
  timeout: 10000
});

// 请求拦截器
api.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    const token = localStorage.getItem('token');
    if (token && config.headers) {
      config.headers.Authorization = \`Bearer \${token}\`;
    }
    return config;
  },
  (error: AxiosError) => Promise.reject(error)
);

// 响应拦截器
api.interceptors.response.use(
  <T>(response: AxiosResponse<ApiResponse<T>>) => {
    const { code, message, data } = response.data;
    
    if (code === 0) {
      return data as T;
    }
    
    return Promise.reject(new Error(message || '请求失败'));
  },
  (error: AxiosError) => {
    if (error.response?.status === 401) {
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
`;

console.log('\n=== 创建类型安全的实例 ===');
console.log(typedInstance);

// 4. 定义 API 方法类型
const apiMethods = `
import api from './api';

// 用户类型
interface User {
  id: number;
  name: string;
  email: string;
}

// 创建用户参数
interface CreateUserParams {
  name: string;
  email: string;
  password: string;
}

// 更新用户参数
interface UpdateUserParams extends Partial<CreateUserParams> {
  id: number;
}

// 分页参数
interface PageParams {
  page: number;
  pageSize: number;
}

// 分页结果
interface PageResult<T> {
  list: T[];
  total: number;
}

// 用户 API
export const userAPI = {
  getList: (params: PageParams): Promise<PageResult<User>> => {
    return api.get('/users', { params });
  },
  
  getDetail: (id: number): Promise<User> => {
    return api.get(\`/users/\${id}\`);
  },
  
  create: (data: CreateUserParams): Promise<User> => {
    return api.post('/users', data);
  },
  
  update: (data: UpdateUserParams): Promise<User> => {
    return api.put(\`/users/\${data.id}\`, data);
  },
  
  delete: (id: number): Promise<void> => {
    return api.delete(\`/users/\${id}\`);
  }
};
`;

console.log('\n=== 定义 API 方法类型 ===');
console.log(apiMethods);

// 5. 在组件中使用
const useInComponent = `
import { userAPI } from './api';
import type { User, PageParams } from './api';

// Vue 3 + TypeScript
<script setup lang="ts">
import { ref, onMounted } from 'vue';

const users = ref<User[]>([]);
const loading = ref(false);
const params = ref<PageParams>({
  page: 1,
  pageSize: 10
});

const fetchUsers = async () => {
  loading.value = true;
  try {
    const result = await userAPI.getList(params.value);
    users.value = result.list;
  } catch (error) {
    console.error('获取用户列表失败:', error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchUsers();
});
</script>

// React + TypeScript
import { useState, useEffect } from 'react';
import { userAPI } from './api';
import type { User, PageParams } from './api';

function UserList() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(false);
  const [params] = useState<PageParams>({
    page: 1,
    pageSize: 10
  });

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const result = await userAPI.getList(params);
      setUsers(result.list);
    } catch (error) {
      console.error('获取用户列表失败:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div>
      {loading && <div>Loading...</div>}
      {users.map(user => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
}
`;

console.log('\n=== 在组件中使用 ===');
console.log(useInComponent);

// 6. 错误处理类型
const errorHandling = `
import axios, { AxiosError } from 'axios';

// 自定义错误类型
interface ApiErrorResponse {
  code: number;
  message: string;
  errors?: Record<string, string[]>;
}

type ApiError = AxiosError<ApiErrorResponse>;

// 错误处理函数
function handleApiError(error: unknown) {
  const axiosError = error as ApiError;
  
  if (axiosError.response) {
    const { status, data } = axiosError.response;
    
    switch (status) {
      case 400:
        console.error('请求错误:', data?.message);
        break;
      case 401:
        console.error('未授权');
        break;
      case 422:
        console.error('验证错误:', data?.errors);
        break;
      case 500:
        console.error('服务器错误');
        break;
      default:
        console.error('请求失败:', data?.message);
    }
  } else if (axiosError.request) {
    console.error('网络错误');
  } else {
    console.error('请求配置错误:', axiosError.message);
  }
  
  throw axiosError;
}

// 使用
async function fetchData() {
  try {
    const data = await api.get('/data');
    return data;
  } catch (error) {
    handleApiError(error);
  }
}
`;

console.log('\n=== 错误处理类型 ===');
console.log(errorHandling);

// 7. 完整的类型定义文件
const typeDefinitions = `
// types/api.ts

// 通用 API 响应
export interface ApiResponse<T = any> {
  code: number;
  message: string;
  data: T;
}

// 分页参数
export interface PageParams {
  page: number;
  pageSize: number;
}

// 分页结果
export interface PageResult<T> {
  list: T[];
  total: number;
  page: number;
  pageSize: number;
}

// 用户类型
export interface User {
  id: number;
  name: string;
  email: string;
  avatar?: string;
  createdAt: string;
  updatedAt: string;
}

// 创建用户参数
export interface CreateUserInput {
  name: string;
  email: string;
  password: string;
  avatar?: string;
}

// 更新用户参数
export interface UpdateUserInput extends Partial<Omit<CreateUserInput, 'email'>> {
  id: number;
}

// 订单类型
export interface Order {
  id: number;
  userId: number;
  status: 'pending' | 'paid' | 'shipped' | 'delivered';
  total: number;
  createdAt: string;
  updatedAt: string;
}
`;

console.log('\n=== 完整的类型定义文件 ===');
console.log(typeDefinitions);

console.log('=== Axios + TypeScript ===');
