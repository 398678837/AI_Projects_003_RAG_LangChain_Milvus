// Axios 实战应用示例代码

// 1. 用户认证流程
const authFlow = `
// 登录 API
import request from '../api';

export interface LoginParams {
  username: string;
  password: string;
}

export interface LoginResult {
  token: string;
  refreshToken: string;
  user: {
    id: number;
    name: string;
    avatar: string;
  };
}

export const authAPI = {
  login: async (params: LoginParams): Promise<LoginResult> => {
    const result = await request.post('/auth/login', params);
    const { token, refreshToken, user } = result;
    
    localStorage.setItem('token', token);
    localStorage.setItem('refreshToken', refreshToken);
    localStorage.setItem('user', JSON.stringify(user));
    
    return result;
  },
  
  logout: async (): Promise<void> => {
    await request.post('/auth/logout');
    
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('user');
  },
  
  getCurrentUser: (): Promise<any> => {
    return request.get('/auth/me');
  }
};

// 使用
async function handleLogin(username: string, password: string) {
  try {
    const result = await authAPI.login({ username, password });
    console.log('登录成功:', result.user);
    return result;
  } catch (error) {
    console.error('登录失败:', error);
    throw error;
  }
}
`;

console.log('=== 用户认证流程 ===');
console.log(authFlow);

// 2. 列表查询与分页
const listPagination = `
import request from '../api';

export interface User {
  id: number;
  name: string;
  email: string;
  avatar: string;
  status: 'active' | 'inactive';
  createdAt: string;
}

export interface UserListParams {
  page: number;
  pageSize: number;
  keyword?: string;
  status?: string;
}

export interface UserListResult {
  list: User[];
  total: number;
  page: number;
  pageSize: number;
}

export const userAPI = {
  getList: (params: UserListParams): Promise<UserListResult> => {
    return request.get('/users', { params });
  },
  
  getDetail: (id: number): Promise<User> => {
    return request.get(\`/users/\${id}\`);
  },
  
  create: (data: Omit<User, 'id' | 'createdAt'>): Promise<User> => {
    return request.post('/users', data);
  },
  
  update: (id: number, data: Partial<Omit<User, 'id' | 'createdAt'>>): Promise<User> => {
    return request.put(\`/users/\${id}\`, data);
  },
  
  delete: (id: number): Promise<void> => {
    return request.delete(\`/users/\${id}\`);
  },
  
  batchDelete: (ids: number[]): Promise<void> => {
    return request.post('/users/batch-delete', { ids });
  }
};

// 在组件中使用
import { ref, reactive, onMounted } from 'vue';
import { userAPI, type User, type UserListParams } from '../api';

export function useUserList() {
  const loading = ref(false);
  const list = ref<User[]>([]);
  const total = ref(0);
  
  const params = reactive<UserListParams>({
    page: 1,
    pageSize: 10,
    keyword: '',
    status: ''
  });

  const fetchList = async () => {
    loading.value = true;
    try {
      const result = await userAPI.getList(params);
      list.value = result.list;
      total.value = result.total;
    } catch (error) {
      console.error('获取用户列表失败:', error);
    } finally {
      loading.value = false;
    }
  };

  const handleSearch = () => {
    params.page = 1;
    fetchList();
  };

  const handlePageChange = (page: number) => {
    params.page = page;
    fetchList();
  };

  const handleDelete = async (id: number) => {
    if (!confirm('确定要删除吗？')) return;
    
    try {
      await userAPI.delete(id);
      fetchList();
    } catch (error) {
      console.error('删除失败:', error);
    }
  };

  onMounted(() => {
    fetchList();
  });

  return {
    loading,
    list,
    total,
    params,
    fetchList,
    handleSearch,
    handlePageChange,
    handleDelete
  };
}
`;

console.log('\n=== 列表查询与分页 ===');
console.log(listPagination);

// 3. 文件上传
const fileUpload = `
import request from '../api';

export interface UploadResult {
  url: string;
  filename: string;
  size: number;
}

export const uploadAPI = {
  uploadFile: async (
    file: File,
    onProgress?: (percent: number) => void
  ): Promise<UploadResult> => {
    const formData = new FormData();
    formData.append('file', file);

    return request.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      onUploadProgress: (progressEvent) => {
        if (progressEvent.total && onProgress) {
          const percent = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          onProgress(percent);
        }
      }
    });
  },

  uploadMultipleFiles: async (
    files: File[],
    onProgress?: (index: number, percent: number) => void
  ): Promise<UploadResult[]> => {
    const results: UploadResult[] = [];
    
    for (let i = 0; i < files.length; i++) {
      const result = await uploadAPI.uploadFile(files[i], (percent) => {
        onProgress?.(i, percent);
      });
      results.push(result);
    }
    
    return results;
  },

  uploadWithParams: async (
    file: File,
    params: Record<string, any>,
    onProgress?: (percent: number) => void
  ): Promise<UploadResult> => {
    const formData = new FormData();
    formData.append('file', file);
    Object.entries(params).forEach(([key, value]) => {
      formData.append(key, value);
    });

    return request.post('/upload-with-params', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      onUploadProgress: (progressEvent) => {
        if (progressEvent.total && onProgress) {
          const percent = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          onProgress(percent);
        }
      }
    });
  }
};

// 在组件中使用
import { ref } from 'vue';
import { uploadAPI, type UploadResult } from '../api';

export function useFileUpload() {
  const uploading = ref(false);
  const uploadProgress = ref(0);
  const uploadedFiles = ref<UploadResult[]>([]);

  const handleFileChange = async (event: Event) => {
    const target = event.target as HTMLInputElement;
    const files = Array.from(target.files || []);
    
    if (files.length === 0) return;

    uploading.value = true;
    uploadProgress.value = 0;
    uploadedFiles.value = [];

    try {
      const results = await uploadAPI.uploadMultipleFiles(
        files,
        (index, percent) => {
          const totalPercent = Math.round(
            ((index + percent / 100) / files.length) * 100
          );
          uploadProgress.value = totalPercent;
        }
      );
      
      uploadedFiles.value = results;
    } catch (error) {
      console.error('上传失败:', error);
    } finally {
      uploading.value = false;
      uploadProgress.value = 0;
    }
  };

  return {
    uploading,
    uploadProgress,
    uploadedFiles,
    handleFileChange
  };
}
`;

console.log('\n=== 文件上传 ===');
console.log(fileUpload);

// 4. 文件下载
const fileDownload = `
import request from '../api';

export const downloadAPI = {
  downloadFile: async (
    url: string,
    filename: string,
    onProgress?: (percent: number) => void
  ): Promise<void> => {
    const response = await request.get(url, {
      responseType: 'blob',
      onDownloadProgress: (progressEvent) => {
        if (progressEvent.total && onProgress) {
          const percent = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          onProgress(percent);
        }
      }
    });

    const blob = new Blob([response]);
    const downloadUrl = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(downloadUrl);
  },

  downloadWithParams: async (
    url: string,
    params: Record<string, any>,
    filename: string,
    onProgress?: (percent: number) => void
  ): Promise<void> => {
    const response = await request.get(url, {
      params,
      responseType: 'blob',
      onDownloadProgress: (progressEvent) => {
        if (progressEvent.total && onProgress) {
          const percent = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          onProgress(percent);
        }
      }
    });

    const blob = new Blob([response]);
    const downloadUrl = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(downloadUrl);
  }
};

// 在组件中使用
import { ref } from 'vue';
import { downloadAPI } from '../api';

export function useFileDownload() {
  const downloading = ref(false);
  const downloadProgress = ref(0);

  const handleDownload = async (url: string, filename: string) => {
    downloading.value = true;
    downloadProgress.value = 0;

    try {
      await downloadAPI.downloadFile(url, filename, (percent) => {
        downloadProgress.value = percent;
      });
    } catch (error) {
      console.error('下载失败:', error);
    } finally {
      downloading.value = false;
      downloadProgress.value = 0;
    }
  };

  return {
    downloading,
    downloadProgress,
    handleDownload
  };
}
`;

console.log('\n=== 文件下载 ===');
console.log(fileDownload);

// 5. 完整的项目示例
const completeProject = `
// 项目结构
src/
├── api/
│   ├── index.ts              # Axios 实例
│   ├── types.ts              # 类型定义
│   ├── constants.ts          # 常量
│   └── modules/
│       ├── auth.ts           # 认证 API
│       ├── user.ts           # 用户 API
│       ├── order.ts          # 订单 API
│       ├── product.ts        # 产品 API
│       └── upload.ts         # 上传 API
├── stores/
│   ├── user.ts               # 用户状态
│   └── app.ts                # 应用状态
├── hooks/
│   ├── useRequest.ts         # 请求 Hook
│   ├── useList.ts            # 列表 Hook
│   └── useUpload.ts          # 上传 Hook
├── utils/
│   ├── storage.ts            # 存储
│   └── auth.ts               # 认证工具
└── main.ts

// 使用示例
import { userAPI } from '@/api/modules/user';
import { useList } from '@/hooks/useList';

export default {
  setup() {
    const { loading, list, total, fetchList, handleDelete } = useList({
      api: userAPI.getList,
      defaultParams: { page: 1, pageSize: 10 }
    });

    return {
      loading,
      list,
      total,
      fetchList,
      handleDelete
    };
  }
};
`;

console.log('\n=== 完整的项目示例 ===');
console.log(completeProject);

console.log('\n🎉 Axios 学习专题完成！');
console.log('💡 记住：合理封装 API，统一错误处理，注重用户体验！');
console.log('🚀 现在你可以在项目中高效使用 Axios 了！');
