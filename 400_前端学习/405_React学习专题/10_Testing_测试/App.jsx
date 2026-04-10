import React, { useState } from 'react';

// 1. 可测试的组件示例
function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  const decrement = () => {
    setCount(count - 1);
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Counter Component</h3>
      <p data-testid="count">Count: {count}</p>
      <button 
        onClick={increment} 
        data-testid="increment-button"
        style={{ marginRight: '8px' }}
      >
        Increment
      </button>
      <button 
        onClick={decrement} 
        data-testid="decrement-button"
      >
        Decrement
      </button>
    </div>
  );
}

// 2. 表单组件示例
function Form({ onSubmit }) {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ name, email });
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Form Component</h3>
      <form onSubmit={handleSubmit} data-testid="form">
        <div style={{ margin: '8px 0' }}>
          <label htmlFor="name">Name:</label>
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            data-testid="name-input"
            style={{ padding: '8px', marginLeft: '8px' }}
          />
        </div>
        <div style={{ margin: '8px 0' }}>
          <label htmlFor="email">Email:</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            data-testid="email-input"
            style={{ padding: '8px', marginLeft: '8px' }}
          />
        </div>
        <button 
          type="submit" 
          data-testid="submit-button"
          style={{ padding: '8px 16px', marginTop: '8px' }}
        >
          Submit
        </button>
      </form>
    </div>
  );
}

// 3. 条件渲染组件示例
function ConditionalRendering() {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Conditional Rendering Component</h3>
      <button 
        onClick={() => setIsVisible(!isVisible)}
        data-testid="toggle-button"
        style={{ padding: '8px 16px' }}
      >
        {isVisible ? 'Hide' : 'Show'}
      </button>
      {isVisible && (
        <div data-testid="visible-content" style={{ marginTop: '16px', padding: '16px', backgroundColor: '#f8f9fa' }}>
          <p>This content is visible when the button is clicked.</p>
        </div>
      )}
    </div>
  );
}

// 4. 列表组件示例
function ListComponent({ items }) {
  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>List Component</h3>
      {items.length === 0 ? (
        <p data-testid="empty-list">No items found</p>
      ) : (
        <ul data-testid="item-list" style={{ listStyle: 'none', padding: 0 }}>
          {items.map((item, index) => (
            <li key={index} data-testid={`item-${index}`} style={{ padding: '8px', borderBottom: '1px solid #dee2e6' }}>
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// 5. API 调用组件示例
function ApiComponent() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
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

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>API Component</h3>
      <button 
        onClick={fetchData}
        data-testid="fetch-button"
        style={{ padding: '8px 16px' }}
      >
        Fetch Data
      </button>
      {loading && <p data-testid="loading">Loading...</p>}
      {error && <p data-testid="error" style={{ color: 'red' }}>Error: {error}</p>}
      {data && (
        <ul data-testid="api-data" style={{ listStyle: 'none', padding: 0, marginTop: '16px' }}>
          {data.slice(0, 3).map(user => (
            <li key={user.id} data-testid={`user-${user.id}`} style={{ padding: '8px', borderBottom: '1px solid #dee2e6' }}>
              {user.name} - {user.email}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// 主应用组件
function App() {
  const handleFormSubmit = (data) => {
    console.log('Form submitted:', data);
  };

  const items = ['Item 1', 'Item 2', 'Item 3'];

  return (
    <div className="App" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <h1>React Testing Example</h1>

      <Counter />
      <Form onSubmit={handleFormSubmit} />
      <ConditionalRendering />
      <ListComponent items={items} />
      <ApiComponent />

      <div style={{ marginTop: '32px', padding: '16px', backgroundColor: '#f8f9fa' }}>
        <h3>Testing Tips</h3>
        <ul>
          <li>Use data-testid attributes to make elements easier to find in tests</li>
          <li>Test component behavior, not implementation details</li>
          <li>Mock external dependencies like API calls</li>
          <li>Test edge cases like empty data, error states, etc.</li>
        </ul>
      </div>
    </div>
  );
}

export default App;