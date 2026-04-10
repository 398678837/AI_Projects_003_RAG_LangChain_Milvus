import React from 'react';
import { BrowserRouter, Routes, Route, Link, useParams, useNavigate, useLocation, useSearchParams, Outlet } from 'react-router-dom';

// 首页组件
function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Home</h1>
      <p>Welcome to the React Router example!</p>
      <nav style={{ margin: '20px 0' }}>
        <Link to="/about" style={{ marginRight: '16px' }}>About</Link>
        <Link to="/contact" style={{ marginRight: '16px' }}>Contact</Link>
        <Link to="/users/1" style={{ marginRight: '16px' }}>User 1</Link>
        <Link to="/products" style={{ marginRight: '16px' }}>Products</Link>
        <Link to="/dashboard" style={{ marginRight: '16px' }}>Dashboard</Link>
        <Link to="/search?q=react">Search</Link>
      </nav>
    </div>
  );
}

// 关于页面组件
function About() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: '20px' }}>
      <h1>About</h1>
      <p>This is the about page.</p>
      <button onClick={() => navigate('/')} style={{ marginTop: '16px' }}>
        Go back to Home
      </button>
    </div>
  );
}

// 联系页面组件
function Contact() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Contact</h1>
      <p>This is the contact page.</p>
    </div>
  );
}

// 用户页面组件（带参数）
function User() {
  const { id } = useParams();
  return (
    <div style={{ padding: '20px' }}>
      <h1>User {id}</h1>
      <p>This is the user page for user {id}.</p>
    </div>
  );
}

// 产品列表页面组件
function Products() {
  const navigate = useNavigate();
  return (
    <div style={{ padding: '20px' }}>
      <h1>Products</h1>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        <li style={{ margin: '8px 0' }}>
          <button onClick={() => navigate('/products/1')}>Product 1</button>
        </li>
        <li style={{ margin: '8px 0' }}>
          <button onClick={() => navigate('/products/2')}>Product 2</button>
        </li>
        <li style={{ margin: '8px 0' }}>
          <button onClick={() => navigate('/products/3')}>Product 3</button>
        </li>
      </ul>
    </div>
  );
}

// 产品详情页面组件（带参数）
function Product() {
  const { id } = useParams();
  return (
    <div style={{ padding: '20px' }}>
      <h1>Product {id}</h1>
      <p>This is the product page for product {id}.</p>
    </div>
  );
}

// 仪表板布局组件（嵌套路由）
function Dashboard() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Dashboard</h1>
      <nav style={{ margin: '20px 0' }}>
        <Link to="profile" style={{ marginRight: '16px' }}>Profile</Link>
        <Link to="settings" style={{ marginRight: '16px' }}>Settings</Link>
        <Link to="stats" style={{ marginRight: '16px' }}>Stats</Link>
      </nav>
      <Outlet /> {/* 子路由将在这里渲染 */}
    </div>
  );
}

// 仪表板子路由组件
function Profile() {
  return <h2>Profile</h2>;
}

function Settings() {
  return <h2>Settings</h2>;
}

function Stats() {
  return <h2>Stats</h2>;
}

// 搜索页面组件
function Search() {
  const [searchParams, setSearchParams] = useSearchParams();
  const query = searchParams.get('q');

  const handleSearch = (e) => {
    e.preventDefault();
    setSearchParams({ q: e.target.q.value });
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Search</h1>
      <form onSubmit={handleSearch} style={{ margin: '20px 0' }}>
        <input 
          type="text" 
          name="q" 
          value={query || ''} 
          placeholder="Search..."
          style={{ padding: '8px', width: '200px' }}
        />
        <button type="submit" style={{ marginLeft: '8px', padding: '8px 16px' }}>
          Search
        </button>
      </form>
      {query && <p>Search results for: {query}</p>}
    </div>
  );
}

// 404页面组件
function NotFound() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>404 Not Found</h1>
      <p>The page you are looking for does not exist.</p>
      <Link to="/">Go back to Home</Link>
    </div>
  );
}

// 主应用组件
function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header style={{ 
          backgroundColor: '#f8f9fa', 
          padding: '16px', 
          borderBottom: '1px solid #dee2e6' 
        }}>
          <h1 style={{ margin: 0 }}>React Router Example</h1>
        </header>
        
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/users/:id" element={<User />} />
          <Route path="/products" element={<Products />} />
          <Route path="/products/:id" element={<Product />} />
          <Route path="/dashboard" element={<Dashboard />}>
            <Route path="profile" element={<Profile />} />
            <Route path="settings" element={<Settings />} />
            <Route path="stats" element={<Stats />} />
          </Route>
          <Route path="/search" element={<Search />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;