import React, { useState } from 'react';

// 基础组件
function Button({ children, onClick, variant = 'primary' }) {
  return (
    <button 
      onClick={onClick}
      style={{
        padding: '8px 16px',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
        backgroundColor: variant === 'primary' ? '#007bff' : '#6c757d',
        color: 'white'
      }}
    >
      {children}
    </button>
  );
}

// 复合组件
function Card({ title, children }) {
  return (
    <div style={{
      border: '1px solid #dee2e6',
      borderRadius: '8px',
      margin: '16px 0',
      overflow: 'hidden'
    }}>
      <div style={{
        padding: '12px',
        backgroundColor: '#f8f9fa',
        borderBottom: '1px solid #dee2e6'
      }}>
        <h3 style={{ margin: 0 }}>{title}</h3>
      </div>
      <div style={{
        padding: '16px'
      }}>
        {children}
      </div>
    </div>
  );
}

// 列表项组件
function TodoItem({ todo, onToggle }) {
  return (
    <li style={{
      padding: '8px',
      borderBottom: '1px solid #dee2e6',
      textDecoration: todo.completed ? 'line-through' : 'none',
      cursor: 'pointer'
    }} onClick={() => onToggle(todo.id)}>
      {todo.text}
    </li>
  );
}

// 待办事项列表组件
function TodoList({ todos, onToggle }) {
  return (
    <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
      {todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} onToggle={onToggle} />
      ))}
    </ul>
  );
}

// 表单组件
function TodoForm({ onAdd }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onAdd(text);
      setText('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '16px' }}>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add a new todo"
        style={{
          padding: '8px',
          width: '70%',
          border: '1px solid #dee2e6',
          borderRadius: '4px'
        }}
      />
      <Button style={{ marginLeft: '8px' }}>
        Add Todo
      </Button>
    </form>
  );
}

// 统计组件
function TodoStats({ todos }) {
  const completedCount = todos.filter(todo => todo.completed).length;
  const totalCount = todos.length;

  return (
    <p style={{ margin: '8px 0' }}>
      {completedCount} out of {totalCount} todos completed
    </p>
  );
}

// 主应用组件
function App() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React components', completed: true },
    { id: 2, text: 'Build a todo app', completed: false },
    { id: 3, text: 'Deploy to production', completed: false }
  ]);

  const handleAddTodo = (text) => {
    const newTodo = {
      id: Date.now(),
      text,
      completed: false
    };
    setTodos([...todos, newTodo]);
  };

  const handleToggleTodo = (id) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  return (
    <div className="App" style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h1>React Components Example</h1>

      <Card title="Todo List">
        <TodoForm onAdd={handleAddTodo} />
        <TodoList todos={todos} onToggle={handleToggleTodo} />
        <TodoStats todos={todos} />
      </Card>

      <Card title="Component Showcase">
        <h3>Button Component</h3>
        <div style={{ margin: '16px 0' }}>
          <Button>Primary Button</Button>
          <Button variant="secondary" style={{ marginLeft: '8px' }}>
            Secondary Button
          </Button>
        </div>

        <h3>Card Component</h3>
        <Card title="Nested Card">
          <p>This is a nested card component.</p>
          <Button>Click me</Button>
        </Card>
      </Card>
    </div>
  );
}

export default App;