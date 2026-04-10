# React API 集成

## 什么是 API 集成？

API 集成是指在 React 应用中与后端 API 进行通信的过程，包括发送请求、处理响应、处理错误等。

## API 调用的方式

### 1. 使用 fetch API

`fetch` 是浏览器内置的 API，用于发送 HTTP 请求。

```jsx
import React, { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        if (!response.ok) {
          throw new Error('Failed to fetch users');
        }
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### 2. 使用 Axios

Axios 是一个流行的 HTTP 客户端库，提供了更简洁的 API 和更好的错误处理。

```bash
npm install axios
```

```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        const response = await axios.get('https://jsonplaceholder.typicode.com/users');
        setUsers(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### 3. 使用自定义 Hook

创建自定义 Hook 来封装 API 调用逻辑，提高代码复用性。

```jsx
import { useState, useEffect } from 'react';
import axios from 'axios';

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await axios.get(url);
        setData(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
}

function UserList() {
  const { data: users, loading, error } = useFetch('https://jsonplaceholder.typicode.com/users');

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## API 调用的类型

### 1. GET 请求

用于获取数据。

```jsx
const response = await fetch('https://jsonplaceholder.typicode.com/users');
const data = await response.json();
```

### 2. POST 请求

用于创建数据。

```jsx
const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ title: 'New Post', body: 'Hello World', userId: 1 })
});
const data = await response.json();
```

### 3. PUT 请求

用于更新数据。

```jsx
const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ title: 'Updated Post', body: 'Hello World Updated', userId: 1 })
});
const data = await response.json();
```

### 4. DELETE 请求

用于删除数据。

```jsx
const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'DELETE'
});
const data = await response.json();
```

## 错误处理

### 1. 网络错误

处理网络连接问题或服务器响应失败的情况。

```jsx
try {
  const response = await fetch('https://jsonplaceholder.typicode.com/users');
  if (!response.ok) {
    throw new Error('Failed to fetch users');
  }
  const data = await response.json();
  setUsers(data);
} catch (error) {
  setError(error.message);
}
```

### 2. 超时处理

设置请求超时，避免请求无限期等待。

```jsx
const fetchWithTimeout = async (url, options = {}, timeout = 5000) => {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);
  
  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal
    });
    clearTimeout(id);
    return response;
  } catch (error) {
    clearTimeout(id);
    throw error;
  }
};

// 使用
const response = await fetchWithTimeout('https://jsonplaceholder.typicode.com/users');
```

## 状态管理

### 1. 使用 React 状态

对于简单的 API 调用，可以使用 React 的 `useState` 和 `useEffect` 来管理状态。

### 2. 使用状态管理库

对于复杂的应用，可以使用状态管理库如 Redux、Zustand 等来管理 API 调用状态。

```jsx
// 使用 Zustand
import create from 'zustand';
import axios from 'axios';

const useUserStore = create((set) => ({
  users: [],
  loading: false,
  error: null,
  fetchUsers: async () => {
    set({ loading: true, error: null });
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/users');
      set({ users: response.data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  }
}));

function UserList() {
  const { users, loading, error, fetchUsers } = useUserStore();

  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## API 集成最佳实践

### 1. 集中管理 API 调用

将 API 调用逻辑集中到单独的文件中，提高代码复用性和可维护性。

```jsx
// api.js
import axios from 'axios';

const API_BASE_URL = 'https://jsonplaceholder.typicode.com';

export const api = {
  getUsers: () => axios.get(`${API_BASE_URL}/users`),
  getUser: (id) => axios.get(`${API_BASE_URL}/users/${id}`),
  createUser: (user) => axios.post(`${API_BASE_URL}/users`, user),
  updateUser: (id, user) => axios.put(`${API_BASE_URL}/users/${id}`, user),
  deleteUser: (id) => axios.delete(`${API_BASE_URL}/users/${id}`)
};

// 使用
import { api } from './api';

const response = await api.getUsers();
```

### 2. 错误处理

统一处理 API 错误，提供一致的错误信息。

### 3. 加载状态

显示加载状态，提供更好的用户体验。

### 4. 缓存

对于频繁访问的数据，可以实现缓存机制，减少 API 调用。

### 5. 重试机制

对于网络错误，可以实现重试机制，提高 API 调用的可靠性。

## 示例代码

### 1. 基本 API 调用

```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        const response = await axios.get('https://jsonplaceholder.typicode.com/users');
        setUsers(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### 2. 带参数的 API 调用

```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PostDetail() {
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [postId, setPostId] = useState(1);

  useEffect(() => {
    const fetchPost = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`https://jsonplaceholder.typicode.com/posts/${postId}`);
        setPost(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPost();
  }, [postId]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!post) return <p>No post found</p>;

  return (
    <div>
      <input
        type="number"
        value={postId}
        onChange={(e) => setPostId(parseInt(e.target.value))}
        min="1"
        max="100"
      />
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}
```

### 3. 提交数据

```jsx
import React, { useState } from 'react';
import axios from 'axios';

function CreatePost() {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      setError(null);
      setSuccess(false);
      const response = await axios.post('https://jsonplaceholder.typicode.com/posts', {
        title,
        body,
        userId: 1
      });
      setSuccess(true);
      setTitle('');
      setBody('');
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Create Post</h1>
      {error && <p>Error: {error}</p>}
      {success && <p>Post created successfully!</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label>Body:</label>
          <textarea
            value={body}
            onChange={(e) => setBody(e.target.value)}
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Creating...' : 'Create'}
        </button>
      </form>
    </div>
  );
}
```

## 学习资源

- [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Axios 官方文档](https://axios-http.com/docs/intro)
- [React 官方文档 - 数据获取](https://react.dev/learn/synchronizing-with-effects#fetching-data)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - 用于测试的 REST API