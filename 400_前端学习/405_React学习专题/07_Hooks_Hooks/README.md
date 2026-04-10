# React Hooks

## 什么是 Hooks？

Hooks 是 React 16.8 引入的新特性，允许你在函数组件中使用状态和其他 React 特性，而不需要编写类组件。

## 常用 Hooks

### 1. useState

`useState` 是最基本的 Hook，用于在函数组件中管理状态。

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

### 2. useEffect

`useEffect` 用于在函数组件中执行副作用操作，相当于类组件的 `componentDidMount`、`componentDidUpdate` 和 `componentWillUnmount` 的组合。

```jsx
import React, { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;

    return () => {
      // 清理函数
    };
  }, [count]); // 依赖数组

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### 3. useContext

`useContext` 用于访问 React Context 中的值。

```jsx
import React, { useContext } from 'react';

const ThemeContext = React.createContext('light');

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button className={`btn btn-${theme}`}>Themed Button</button>;
}
```

### 4. useReducer

`useReducer` 是 `useState` 的替代方案，用于管理复杂的状态逻辑。

```jsx
import React, { useReducer } from 'react';

function counterReducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
    </div>
  );
}
```

### 5. useCallback

`useCallback` 用于缓存函数，避免在每次渲染时创建新的函数。

```jsx
import React, { useState, useCallback } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}
```

### 6. useMemo

`useMemo` 用于缓存计算结果，避免在每次渲染时重新计算。

```jsx
import React, { useState, useMemo } from 'react';

function ExpensiveCalculation() {
  const [count, setCount] = useState(0);

  const expensiveValue = useMemo(() => {
    let result = 0;
    for (let i = 0; i < 1000000000; i++) {
      result += i;
    }
    return result;
  }, []); // 空依赖数组，只计算一次

  return (
    <div>
      <p>Count: {count}</p>
      <p>Expensive value: {expensiveValue}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### 7. useRef

`useRef` 用于在组件之间共享数据，相当于类组件的实例属性。

```jsx
import React, { useRef, useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  const countRef = useRef(count);

  const handleClick = () => {
    setCount(count + 1);
    console.log('Current count:', countRef.current); // 注意：这里会打印旧值
  };

  useEffect(() => {
    countRef.current = count; // 同步更新 ref
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}
```

### 8. useLayoutEffect

`useLayoutEffect` 与 `useEffect` 类似，但在 DOM 更新后同步执行，相当于类组件的 `componentDidMount` 和 `componentDidUpdate`。

```jsx
import React, { useState, useLayoutEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  const [width, setWidth] = useState(0);
  const ref = useRef(null);

  useLayoutEffect(() => {
    if (ref.current) {
      setWidth(ref.current.offsetWidth);
    }
  }, [count]);

  return (
    <div ref={ref}>
      <p>Count: {count}</p>
      <p>Width: {width}px</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### 9. useDebugValue

`useDebugValue` 用于在 React DevTools 中显示自定义 Hook 的值。

```jsx
import React, { useState, useDebugValue } from 'react';

function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  useDebugValue(`Count: ${count}`);
  return [count, setCount];
}

function Counter() {
  const [count, setCount] = useCounter();
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

## 自定义 Hooks

你可以创建自己的自定义 Hooks，将逻辑提取到可复用的函数中。

```jsx
import React, { useState, useEffect } from 'react';

function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    const storedValue = localStorage.getItem(key);
    return storedValue ? JSON.parse(storedValue) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
}

function Counter() {
  const [count, setCount] = useLocalStorage('count', 0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

## Hooks 规则

1. **只能在函数组件的顶层调用 Hooks**，不能在条件语句、循环或嵌套函数中调用。
2. **只能在 React 函数组件中调用 Hooks**，不能在普通的 JavaScript 函数中调用。
3. **Hooks 的调用顺序必须保持一致**，每次渲染时都应该以相同的顺序调用 Hooks。

## 示例代码

### 1. 基本 Hooks 示例

```jsx
import React, { useState, useEffect, useContext, useCallback, useMemo } from 'react';

const ThemeContext = React.createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Counter />
    </ThemeContext.Provider>
  );
}

function Counter() {
  const [count, setCount] = useState(0);
  const theme = useContext(ThemeContext);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  const increment = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  const doubleCount = useMemo(() => {
    return count * 2;
  }, [count]);

  return (
    <div style={{ backgroundColor: theme === 'dark' ? '#333' : '#fff', color: theme === 'dark' ? '#fff' : '#333' }}>
      <p>Count: {count}</p>
      <p>Double count: {doubleCount}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}
```

### 2. 自定义 Hook 示例

```jsx
import React, { useState, useEffect } from 'react';

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const json = await response.json();
        setData(json);
      } catch (error) {
        setError(error);
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
  if (error) return <p>Error: {error.message}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## 学习资源

- [React 官方文档 - Hooks](https://react.dev/learn/hooks-intro)
- [React 官方文档 - useState](https://react.dev/learn/state-a-components-memory)
- [React 官方文档 - useEffect](https://react.dev/learn/synchronizing-with-effects)
- [React 官方文档 - 自定义 Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)