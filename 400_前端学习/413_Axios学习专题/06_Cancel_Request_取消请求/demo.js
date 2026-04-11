// Axios 取消请求示例代码

// 1. 使用 AbortController（推荐）
const abortController = `
// 创建 AbortController
const controller = new AbortController();
const signal = controller.signal;

// 发送请求
axios.get('/api/data', {
  signal: signal
})
  .then(response => console.log('成功:', response.data))
  .catch(error => {
    if (axios.isCancel(error)) {
      console.log('请求被取消:', error.message);
    } else {
      console.error('请求失败:', error);
    }
  });

// 取消请求
controller.abort();
`;

console.log('=== 使用 AbortController（推荐） ===');
console.log(abortController);

// 2. 使用 CancelToken（旧版）
const cancelToken = `
// 创建 CancelToken
const source = axios.CancelToken.source();

// 发送请求
axios.get('/api/data', {
  cancelToken: source.token
})
  .then(response => console.log('成功:', response.data))
  .catch(error => {
    if (axios.isCancel(error)) {
      console.log('请求被取消:', error.message);
    } else {
      console.error('请求失败:', error);
    }
  });

// 取消请求
source.cancel('用户取消了请求');
`;

console.log('\n=== 使用 CancelToken（旧版） ===');
console.log(cancelToken);

// 3. 组件卸载时取消请求（React）
const reactUnmountCancel = `
import { useEffect, useRef } from 'react';
import axios from 'axios';

function MyComponent() {
  const controllerRef = useRef(null);

  useEffect(() => {
    const controller = new AbortController();
    controllerRef.current = controller;

    const fetchData = async () => {
      try {
        const response = await axios.get('/api/data', {
          signal: controller.signal
        });
        console.log('数据:', response.data);
      } catch (error) {
        if (!axios.isCancel(error)) {
          console.error('请求失败:', error);
        }
      }
    };

    fetchData();

    // 组件卸载时取消请求
    return () => {
      controller.abort();
    };
  }, []);

  return <div>My Component</div>;
}
`;

console.log('\n=== 组件卸载时取消请求（React） ===');
console.log(reactUnmountCancel);

// 4. 组件卸载时取消请求（Vue）
const vueUnmountCancel = `
<template>
  <div>My Component</div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue';
import axios from 'axios';

const controller = ref(null);

const fetchData = async () => {
  try {
    const response = await axios.get('/api/data', {
      signal: controller.value.signal
    });
    console.log('数据:', response.data);
  } catch (error) {
    if (!axios.isCancel(error)) {
      console.error('请求失败:', error);
    }
  }
};

onMounted(() => {
  controller.value = new AbortController();
  fetchData();
});

onUnmounted(() => {
  controller.value?.abort();
});
</script>
`;

console.log('\n=== 组件卸载时取消请求（Vue） ===');
console.log(vueUnmountCancel);

// 5. 搜索输入时取消上一次请求
const searchDebounceCancel = `
import { ref } from 'vue';
import axios from 'axios';

const searchQuery = ref('');
let controller = null;

const search = async () => {
  // 取消上一次请求
  if (controller) {
    controller.abort();
  }

  if (!searchQuery.value.trim()) {
    return;
  }

  controller = new AbortController();

  try {
    const response = await axios.get('/api/search', {
      params: { q: searchQuery.value },
      signal: controller.signal
    });
    console.log('搜索结果:', response.data);
  } catch (error) {
    if (!axios.isCancel(error)) {
      console.error('搜索失败:', error);
    }
  }
};

// 使用防抖
let timeoutId = null;
const debouncedSearch = () => {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(search, 300);
};

// 监听输入
searchQuery.value = 'hello';
debouncedSearch();
`;

console.log('\n=== 搜索输入时取消上一次请求 ===');
console.log(searchDebounceCancel);

// 6. 多个请求管理
const multipleRequests = `
const pendingRequests = new Map();

// 添加请求
function addRequest(key, controller) {
  // 如果已有相同 key 的请求，先取消
  if (pendingRequests.has(key)) {
    pendingRequests.get(key).abort();
  }
  pendingRequests.set(key, controller);
}

// 移除请求
function removeRequest(key) {
  pendingRequests.delete(key);
}

// 取消所有请求
function cancelAllRequests() {
  for (const [key, controller] of pendingRequests) {
    controller.abort();
  }
  pendingRequests.clear();
}

// 使用
async function fetchUser(userId) {
  const key = \`user-\${userId}\`;
  const controller = new AbortController();
  
  addRequest(key, controller);

  try {
    const response = await axios.get(\`/api/users/\${userId}\`, {
      signal: controller.signal
    });
    return response.data;
  } catch (error) {
    if (!axios.isCancel(error)) {
      throw error;
    }
  } finally {
    removeRequest(key);
  }
}

// 使用
fetchUser(1);
fetchUser(2); // 取消上一个请求

// 路由切换时取消所有
cancelAllRequests();
`;

console.log('\n=== 多个请求管理 ===');
console.log(multipleRequests);

// 7. 封装取消请求的 Hook
const cancelHook = `
import { ref } from 'vue';

export function useCancelableRequest() {
  const controller = ref(null);
  const isCancelled = ref(false);

  const request = async (config) => {
    // 取消上一次请求
    if (controller.value) {
      controller.value.abort();
    }

    isCancelled.value = false;
    controller.value = new AbortController();

    try {
      const response = await axios({
        ...config,
        signal: controller.value.signal
      });
      return response.data;
    } catch (error) {
      if (axios.isCancel(error)) {
        isCancelled.value = true;
      }
      throw error;
    }
  };

  const cancel = () => {
    if (controller.value) {
      controller.value.abort();
      isCancelled.value = true;
    }
  };

  return {
    request,
    cancel,
    isCancelled
  };
}

// 使用
const { request, cancel, isCancelled } = useCancelableRequest();

// 发送请求
request({ method: 'get', url: '/api/data' })
  .then(data => console.log(data))
  .catch(error => {
    if (!isCancelled.value) {
      console.error(error);
    }
  });

// 取消
cancel();
`;

console.log('\n=== 封装取消请求的 Hook ===');
console.log(cancelHook);

// 8. 判断是否是取消错误
const checkCancelError = `
axios.get('/api/data', { signal: controller.signal })
  .catch(error => {
    // 方式 1
    if (axios.isCancel(error)) {
      console.log('请求被取消');
    }

    // 方式 2
    if (error.name === 'CanceledError') {
      console.log('请求被取消');
    }

    // 方式 3
    if (error.code === 'ERR_CANCELED') {
      console.log('请求被取消');
    }
  });
`;

console.log('\n=== 判断是否是取消错误 ===');
console.log(checkCancelError);

console.log('=== Axios 取消请求 ===');
