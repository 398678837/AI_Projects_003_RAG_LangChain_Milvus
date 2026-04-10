# React 核心语法

## JSX 语法

JSX 是 JavaScript 的扩展语法，允许你在 JavaScript 代码中编写类似 HTML 的标记。

### 基本语法

```jsx
// 基本元素
const element = <h1>Hello, world!</h1>;

// 嵌套元素
const element = (
  <div>
    <h1>Hello</h1>
    <p>Welcome to React</p>
  </div>
);

// 使用表达式
const name = 'John';
const element = <h1>Hello, {name}!</h1>;

// 使用条件渲染
const isLoggedIn = true;
const element = isLoggedIn ? <UserGreeting /> : <GuestGreeting />;

// 使用列表渲染
const items = ['React', 'Vue', 'Angular'];
const element = (
  <ul>
    {items.map((item, index) => (
      <li key={index}>{item}</li>
    ))}
  </ul>
);
```

## 组件语法

### 函数组件

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

### 类组件

```jsx
class Greeting extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

## Props

Props 是从父组件传递给子组件的数据。

```jsx
function Greeting({ name, age }) {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
    </div>
  );
}

// 使用组件
<Greeting name="John" age={30} />
```

## State

State 是组件内部的可变数据。

### 类组件中的状态

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.increment}>Increment</button>
      </div>
    );
  }
}
```

### 函数组件中的状态 (使用 Hooks)

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

## 事件处理

```jsx
function Button() {
  const handleClick = () => {
    console.log('Button clicked!');
  };

  return <button onClick={handleClick}>Click me</button>;
}
```

## 表单处理

```jsx
function Form() {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitted:', name);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

## 条件渲染

```jsx
function Greeting({ isLoggedIn }) {
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

// 或者使用三元运算符
function Greeting({ isLoggedIn }) {
  return isLoggedIn ? <UserGreeting /> : <GuestGreeting />;
}

// 或者使用逻辑与运算符
function Greeting({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn && <UserGreeting />}
      {!isLoggedIn && <GuestGreeting />}
    </div>
  );
}
```

## 列表渲染

```jsx
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}
```

## 组合组件

```jsx
function App() {
  return (
    <div>
      <Header />
      <MainContent />
      <Footer />
    </div>
  );
}
```

## 学习资源

- [React 官方文档 - JSX](https://react.dev/learn/writing-markup-with-jsx)
- [React 官方文档 - 组件和 Props](https://react.dev/learn/passing-props-to-a-component)
- [React 官方文档 - 状态](https://react.dev/learn/state-a-components-memory)