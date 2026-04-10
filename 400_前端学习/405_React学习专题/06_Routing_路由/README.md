# React 路由

## 什么是路由？

路由是指根据 URL 的变化来显示不同的内容。在 React 应用中，路由允许我们创建单页应用 (SPA)，其中不同的 URL 对应不同的组件。

## React Router

React Router 是 React 官方推荐的路由库，它允许我们在 React 应用中实现客户端路由。

### 安装 React Router

```bash
npm install react-router-dom
```

## 基本路由

### 1. 设置路由

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### 2. 路由参数

```jsx
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';

function User() {
  const { id } = useParams();
  return <h1>User {id}</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/users/1">User 1</Link>
        <Link to="/users/2">User 2</Link>
      </nav>
      <Routes>
        <Route path="/users/:id" element={<User />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### 3. 嵌套路由

```jsx
import { BrowserRouter, Routes, Route, Link, Outlet } from 'react-router-dom';

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <nav>
        <Link to="profile">Profile</Link>
        <Link to="settings">Settings</Link>
      </nav>
      <Outlet /> {/* 子路由将在这里渲染 */}
    </div>
  );
}

function Profile() {
  return <h2>Profile</h2>;
}

function Settings() {
  return <h2>Settings</h2>;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />}>
          <Route path="profile" element={<Profile />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
```

### 4. 重定向

```jsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/old-path" element={<Navigate to="/new-path" />} />
        <Route path="/new-path" element={<NewPath />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### 5. 404 页面

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function NotFound() {
  return <h1>404 Not Found</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

## 路由 Hooks

### 1. useNavigate

用于导航到不同的页面。

```jsx
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/about');
  };

  return (
    <div>
      <h1>Home</h1>
      <button onClick={handleClick}>Go to About</button>
    </div>
  );
}
```

### 2. useParams

用于获取 URL 中的参数。

```jsx
import { useParams } from 'react-router-dom';

function User() {
  const { id } = useParams();
  return <h1>User {id}</h1>;
}
```

### 3. useLocation

用于获取当前 URL 的信息。

```jsx
import { useLocation } from 'react-router-dom';

function Home() {
  const location = useLocation();
  return <h1>Current path: {location.pathname}</h1>;
}
```

### 4. useSearchParams

用于获取和修改 URL 查询参数。

```jsx
import { useSearchParams } from 'react-router-dom';

function Search() {
  const [searchParams, setSearchParams] = useSearchParams();
  const query = searchParams.get('q');

  const handleSearch = (e) => {
    e.preventDefault();
    setSearchParams({ q: e.target.q.value });
  };

  return (
    <div>
      <form onSubmit={handleSearch}>
        <input type="text" name="q" value={query || ''} />
        <button type="submit">Search</button>
      </form>
      {query && <p>Search results for: {query}</p>}
    </div>
  );
}
```

## 路由最佳实践

### 1. 组织路由结构

- 将路由配置集中管理
- 使用嵌套路由来组织相关的页面
- 使用路由参数来传递动态数据

### 2. 保护路由

- 使用高阶组件或布局组件来保护需要认证的路由
- 实现路由守卫来检查用户权限

### 3. 代码分割

- 使用 `React.lazy` 和 `Suspense` 来实现路由级别的代码分割
- 减少初始加载时间

### 4. 导航体验

- 使用 `navigate` 函数进行编程式导航
- 使用 `Link` 组件进行声明式导航
- 实现平滑的页面过渡效果

## 示例代码

### 1. 基本路由示例

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function Home() {
  return <h1>Home</h1>;
}

function About() {
  return <h1>About</h1>;
}

function Contact() {
  return <h1>Contact</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### 2. 带参数的路由示例

```jsx
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';

function Product() {
  const { id } = useParams();
  return <h1>Product {id}</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/products/1">Product 1</Link>
        <Link to="/products/2">Product 2</Link>
      </nav>
      <Routes>
        <Route path="/products/:id" element={<Product />} />
      </Routes>
    </BrowserRouter>
  );
}
```

## 学习资源

- [React Router 官方文档](https://reactrouter.com/en/main)
- [React 官方文档 - 路由](https://react.dev/learn/passing-data-deeply-with-context)
- [MDN Web Docs - 客户端路由](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_client-side_routing)