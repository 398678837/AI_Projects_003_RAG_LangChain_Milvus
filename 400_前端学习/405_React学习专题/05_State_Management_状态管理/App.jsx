import React, { useState, createContext, useContext } from 'react';

// 1. 组件内部状态示例
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Component State</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)} style={{ marginRight: '8px' }}>
        Increment
      </button>
      <button onClick={() => setCount(count - 1)}>
        Decrement
      </button>
    </div>
  );
}

// 2. Context 状态管理示例
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function ThemeToggle() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Context State</h3>
      <p>Current theme: {theme}</p>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </div>
  );
}

function ThemedButton() {
  const { theme } = useContext(ThemeContext);

  return (
    <button style={{
      padding: '8px 16px',
      border: 'none',
      borderRadius: '4px',
      backgroundColor: theme === 'light' ? '#007bff' : '#6c757d',
      color: 'white'
    }}>
      Themed Button
    </button>
  );
}

// 3. 状态提升示例
function ParentComponent() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', completed: true },
    { id: 2, text: 'Build an app', completed: false },
  ]);

  const [inputText, setInputText] = useState('');

  const handleAddTodo = () => {
    if (inputText.trim()) {
      setTodos([...todos, { id: Date.now(), text: inputText, completed: false }]);
      setInputText('');
    }
  };

  const handleToggleTodo = (id) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>State Lifting</h3>
      <TodoForm 
        inputText={inputText} 
        setInputText={setInputText} 
        onAddTodo={handleAddTodo} 
      />
      <TodoList todos={todos} onToggleTodo={handleToggleTodo} />
    </div>
  );
}

function TodoForm({ inputText, setInputText, onAddTodo }) {
  return (
    <div style={{ marginBottom: '16px' }}>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Add a new todo"
        style={{ padding: '8px', width: '200px' }}
      />
      <button onClick={onAddTodo} style={{ marginLeft: '8px', padding: '8px 16px' }}>
        Add Todo
      </button>
    </div>
  );
}

function TodoList({ todos, onToggleTodo }) {
  return (
    <ul style={{ listStyle: 'none', padding: 0 }}>
      {todos.map(todo => (
        <li 
          key={todo.id}
          style={{ 
            padding: '8px', 
            borderBottom: '1px solid #dee2e6',
            textDecoration: todo.completed ? 'line-through' : 'none',
            cursor: 'pointer'
          }}
          onClick={() => onToggleTodo(todo.id)}
        >
          {todo.text}
        </li>
      ))}
    </ul>
  );
}

// 4. 复杂状态管理示例
function ComplexStateExample() {
  const [user, setUser] = useState({
    name: 'John',
    age: 30,
    address: {
      street: '123 Main St',
      city: 'New York',
      country: 'USA'
    }
  });

  const updateName = (name) => {
    setUser({ ...user, name });
  };

  const updateCity = (city) => {
    setUser({
      ...user,
      address: {
        ...user.address,
        city
      }
    });
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Complex State</h3>
      <p>Name: {user.name}</p>
      <p>Age: {user.age}</p>
      <p>Address: {user.address.street}, {user.address.city}, {user.address.country}</p>
      <div style={{ margin: '16px 0' }}>
        <input
          type="text"
          value={user.name}
          onChange={(e) => updateName(e.target.value)}
          style={{ padding: '8px', width: '200px', marginRight: '8px' }}
        />
        <input
          type="text"
          value={user.address.city}
          onChange={(e) => updateCity(e.target.value)}
          style={{ padding: '8px', width: '200px' }}
        />
      </div>
    </div>
  );
}

// 主应用组件
function App() {
  return (
    <ThemeProvider>
      <div className="App" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        <h1>React State Management Example</h1>

        <Counter />

        <div>
          <ThemeToggle />
          <ThemedButton />
        </div>

        <ParentComponent />

        <ComplexStateExample />
      </div>
    </ThemeProvider>
  );
}

export default App;