import React, { useState } from 'react';

// 条件渲染示例
function Greeting({ isLoggedIn }) {
  if (isLoggedIn) {
    return <h2>Welcome back!</h2>;
  }
  return <h2>Please sign up.</h2>;
}

// 列表渲染示例
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>
          {todo.text} {todo.completed && '(completed)'}
        </li>
      ))}
    </ul>
  );
}

// 表单处理示例
function Form() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitted:', { name, email });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </div>
      <div>
        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}

// 事件处理示例
function Button() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Clicked {count} times</p>
      <button onClick={handleClick}>Click me</button>
    </div>
  );
}

// 组合组件示例
function Header() {
  return <header><h1>React Core Syntax</h1></header>;
}

function Footer() {
  return <footer><p>© 2026 React Learning</p></footer>;
}

// 主应用组件
function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const todos = [
    { id: 1, text: 'Learn React', completed: true },
    { id: 2, text: 'Build an app', completed: false },
    { id: 3, text: 'Deploy to production', completed: false }
  ];

  return (
    <div className="App">
      <Header />
      
      <section>
        <h2>1. JSX 语法</h2>
        <div>
          <p>Hello, {isLoggedIn ? 'User' : 'Guest'}!</p>
          <p>Current time: {new Date().toLocaleTimeString()}</p>
        </div>
      </section>

      <section>
        <h2>2. 条件渲染</h2>
        <Greeting isLoggedIn={isLoggedIn} />
        <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
          {isLoggedIn ? 'Log out' : 'Log in'}
        </button>
      </section>

      <section>
        <h2>3. 列表渲染</h2>
        <TodoList todos={todos} />
      </section>

      <section>
        <h2>4. 表单处理</h2>
        <Form />
      </section>

      <section>
        <h2>5. 事件处理</h2>
        <Button />
      </section>

      <Footer />
    </div>
  );
}

export default App;