import React, { useState, useEffect } from 'react';

// 1. 基本 API 调用示例 (使用 fetch)
function BasicFetch() {
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

  if (loading) return <div style={{ padding: '20px' }}>Loading...</div>;
  if (error) return <div style={{ padding: '20px', color: 'red' }}>Error: {error}</div>;

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Basic Fetch Example</h3>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {users.map(user => (
          <li key={user.id} style={{ padding: '8px', borderBottom: '1px solid #dee2e6' }}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

// 2. 带参数的 API 调用示例
function FetchWithParams() {
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [postId, setPostId] = useState(1);

  useEffect(() => {
    const fetchPost = async () => {
      try {
        setLoading(true);
        const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`);
        if (!response.ok) {
          throw new Error('Failed to fetch post');
        }
        const data = await response.json();
        setPost(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPost();
  }, [postId]);

  if (loading) return <div style={{ padding: '20px' }}>Loading...</div>;
  if (error) return <div style={{ padding: '20px', color: 'red' }}>Error: {error}</div>;
  if (!post) return <div style={{ padding: '20px' }}>No post found</div>;

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Fetch with Parameters</h3>
      <div style={{ margin: '16px 0' }}>
        <label>Post ID: </label>
        <input
          type="number"
          value={postId}
          onChange={(e) => setPostId(parseInt(e.target.value))}
          min="1"
          max="100"
          style={{ padding: '4px', marginLeft: '8px' }}
        />
      </div>
      <h4>{post.title}</h4>
      <p>{post.body}</p>
      <p>User ID: {post.userId}</p>
    </div>
  );
}

// 3. 提交数据示例
function PostData() {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [responseData, setResponseData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      setError(null);
      setSuccess(false);
      const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title,
          body,
          userId: 1
        })
      });
      if (!response.ok) {
        throw new Error('Failed to create post');
      }
      const data = await response.json();
      setResponseData(data);
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
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Post Data Example</h3>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {success && responseData && (
        <div style={{ margin: '16px 0', padding: '16px', backgroundColor: '#d4edda', borderRadius: '4px' }}>
          <p>Post created successfully!</p>
          <p>ID: {responseData.id}</p>
          <p>Title: {responseData.title}</p>
          <p>Body: {responseData.body}</p>
        </div>
      )}
      <form onSubmit={handleSubmit}>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            style={{ padding: '8px', width: '300px' }}
          />
        </div>
        <div style={{ margin: '8px 0' }}>
          <label style={{ display: 'block', marginBottom: '4px' }}>Body:</label>
          <textarea
            value={body}
            onChange={(e) => setBody(e.target.value)}
            style={{ padding: '8px', width: '300px', height: '100px' }}
          />
        </div>
        <button 
          type="submit" 
          style={{ padding: '8px 16px', marginTop: '8px' }}
          disabled={loading}
        >
          {loading ? 'Creating...' : 'Create Post'}
        </button>
      </form>
    </div>
  );
}

// 4. 自定义 Hook 示例
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const result = await response.json();
        setData(result);
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

function CustomHookExample() {
  const { data: posts, loading, error } = useFetch('https://jsonplaceholder.typicode.com/posts');

  if (loading) return <div style={{ padding: '20px' }}>Loading...</div>;
  if (error) return <div style={{ padding: '20px', color: 'red' }}>Error: {error}</div>;
  if (!posts) return <div style={{ padding: '20px' }}>No posts found</div>;

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Custom Hook Example</h3>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {posts.slice(0, 5).map(post => (
          <li key={post.id} style={{ padding: '8px', borderBottom: '1px solid #dee2e6' }}>
            <h4>{post.title}</h4>
            <p>{post.body.substring(0, 100)}...</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

// 5. 错误处理和加载状态示例
function ErrorHandlingExample() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [url, setUrl] = useState('https://jsonplaceholder.typicode.com/users');

  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`);
      }
      const result = await response.json();
      setData(result);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Error Handling Example</h3>
      <div style={{ margin: '16px 0' }}>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{ padding: '8px', width: '300px', marginRight: '8px' }}
        />
        <button onClick={fetchData} disabled={loading} style={{ padding: '8px 16px' }}>
          {loading ? 'Fetching...' : 'Fetch Data'}
        </button>
      </div>
      {loading && <div style={{ padding: '20px' }}>Loading...</div>}
      {error && <div style={{ padding: '20px', color: 'red' }}>Error: {error}</div>}
      {data && (
        <div>
          <h4>Results:</h4>
          <pre style={{ backgroundColor: '#f8f9fa', padding: '16px', borderRadius: '4px', overflow: 'auto' }}>
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

// 主应用组件
function App() {
  return (
    <div className="App" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <h1>React API Integration Example</h1>

      <BasicFetch />
      <FetchWithParams />
      <PostData />
      <CustomHookExample />
      <ErrorHandlingExample />
    </div>
  );
}

export default App;