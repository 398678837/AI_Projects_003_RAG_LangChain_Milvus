# React 状态管理

## 什么是状态管理？

状态管理是管理 React 应用中状态的方式。在 React 中，状态可以是组件内部的状态，也可以是跨多个组件共享的状态。

## 状态管理的方式

### 1. 组件内部状态

使用 `useState` 或类组件的 `this.state` 来管理组件内部的状态。

```jsx
// 函数组件
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

// 类组件
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
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

### 2. 上下文 (Context)

使用 `useContext` 和 `createContext` 来共享跨组件的状态。

```jsx
// 创建上下文
const ThemeContext = createContext('light');

// 提供者组件
function App() {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Header />
      <MainContent />
    </ThemeContext.Provider>
  );
}

// 消费者组件
function Header() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <header style={{ backgroundColor: theme === 'dark' ? '#333' : '#fff' }}>
      <h1>My App</h1>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </header>
  );
}
```

### 3. 状态提升

将状态提升到共同的父组件，然后通过 props 传递给子组件。

```jsx
function Parent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <Child1 count={count} />
      <Child2 count={count} onIncrement={() => setCount(count + 1)} />
    </div>
  );
}

function Child1({ count }) {
  return <p>Count: {count}</p>;
}

function Child2({ count, onIncrement }) {
  return <button onClick={onIncrement}>Increment</button>;
}
```

### 4. 使用第三方状态管理库

对于复杂的应用，可以使用第三方状态管理库，如 Redux、MobX、Zustand 等。

#### Redux

```jsx
// store.js
import { createStore } from 'redux';

const initialState = { count: 0 };

function counterReducer(state = initialState, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

const store = createStore(counterReducer);

export default store;

// App.jsx
import { useSelector, useDispatch } from 'react-redux';

function Counter() {
  const count = useSelector(state => state.count);
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>Decrement</button>
    </div>
  );
}
```

#### Zustand

```jsx
// store.js
import create from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set(state => ({ count: state.count + 1 })),
  decrement: () => set(state => ({ count: state.count - 1 })),
}));

export default useStore;

// App.jsx
function Counter() {
  const { count, increment, decrement } = useStore();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
}
```

## 状态管理最佳实践

### 1. 状态拆分

将状态拆分为多个小的、专注的状态，而不是一个大的状态对象。

### 2. 状态位置

- 组件内部状态：只在单个组件中使用的状态
- 上下文状态：在多个组件中共享的状态
- 全局状态：在整个应用中共享的状态

### 3. 状态更新

- 使用不可变数据结构更新状态
- 避免直接修改状态
- 使用函数式更新来处理依赖于先前状态的更新

### 4. 性能优化

- 使用 `useMemo` 缓存计算结果
- 使用 `useCallback` 缓存函数
- 使用 `React.memo` 缓存组件渲染
- 使用 `useReducer` 处理复杂的状态逻辑

## 示例代码

### 1. 简单状态管理

```jsx
function TodoApp() {
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
    <div>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button onClick={handleAddTodo}>Add Todo</button>
      <ul>
        {todos.map(todo => (
          <li 
            key={todo.id}
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
            onClick={() => handleToggleTodo(todo.id)}
          >
            {todo.text}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### 2. 使用 Context 进行状态管理

```jsx
const TodoContext = createContext();

function TodoProvider({ children }) {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', completed: true },
    { id: 2, text: 'Build an app', completed: false },
  ]);

  const addTodo = (text) => {
    setTodos([...todos, { id: Date.now(), text, completed: false }]);
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  return (
    <TodoContext.Provider value={{ todos, addTodo, toggleTodo }}>
      {children}
    </TodoContext.Provider>
  );
}

function TodoList() {
  const { todos, toggleTodo } = useContext(TodoContext);

  return (
    <ul>
      {todos.map(todo => (
        <li 
          key={todo.id}
          style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
          onClick={() => toggleTodo(todo.id)}
        >
          {todo.text}
        </li>
      ))}
    </ul>
  );
}

function TodoForm() {
  const { addTodo } = useContext(TodoContext);
  const [inputText, setInputText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputText.trim()) {
      addTodo(inputText);
      setInputText('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button type="submit">Add Todo</button>
    </form>
  );
}

function App() {
  return (
    <TodoProvider>
      <TodoForm />
      <TodoList />
    </TodoProvider>
  );
}
```

## 学习资源

- [React 官方文档 - 状态管理](https://react.dev/learn/managing-state)
- [React 官方文档 - Context](https://react.dev/learn/passing-data-deeply-with-context)
- [Redux 官方文档](https://redux.js.org/)
- [Zustand 官方文档](https://zustand-demo.pmnd.rs/)