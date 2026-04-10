import React, { useState, useEffect, useContext, useCallback, useMemo, useRef, useReducer, useLayoutEffect } from 'react';

// 1. useState 示例
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>useState Example</h3>
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

// 2. useEffect 示例
function EffectExample() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  // 依赖于 count 的 effect
  useEffect(() => {
    document.title = `Count: ${count}`;
    console.log('Count changed:', count);
  }, [count]);

  // 只在组件挂载时执行的 effect
  useEffect(() => {
    console.log('Component mounted');
    return () => {
      console.log('Component unmounted');
    };
  }, []);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>useEffect Example</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)} style={{ marginRight: '8px' }}>
        Increment
      </button>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
        style={{ marginLeft: '16px' }}
      />
      <p>Name: {name}</p>
    </div>
  );
}

// 3. useContext 示例
const ThemeContext = React.createContext('light');

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>useContext Example</h3>
      <p>Current theme: {theme}</p>
      <button 
        onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
        style={{
          padding: '8px 16px',
          border: 'none',
          borderRadius: '4px',
          backgroundColor: theme === 'light' ? '#007bff' : '#6c757d',
          color: 'white'
        }}
      >
        Toggle Theme
      </button>
    </div>
  );
}

// 4. useReducer 示例
function counterReducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return { count: 0 };
    default:
      return state;
  }
}

function ReducerExample() {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>useReducer Example</h3>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })} style={{ marginRight: '8px' }}>
        Increment
      </button>
      <button onClick={() => dispatch({ type: 'decrement' })} style={{ marginRight: '8px' }}>
        Decrement
      </button>
      <button onClick={() => dispatch({ type: 'reset' })}>
        Reset
      </button>
    </div>
  );
}

// 5. useCallback 示例
function CallbackExample() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  // 缓存 increment 函数
  const increment = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>useCallback Example</h3>
      <p>Count: {count}</p>
      <button onClick={increment} style={{ marginRight: '16px' }}>
        Increment
      </button>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      <p>Name: {name}</p>
    </div>
  );
}

// 6. useMemo 示例
function MemoExample() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  // 缓存计算结果
  const expensiveValue = useMemo(() => {
    console.log('Calculating expensive value...');
    let result = 0;
    for (let i = 0; i < 1000000; i++) {
      result += i;
    }
    return result;
  }, []);

  const doubleCount = useMemo(() => {
    return count * 2;
  }, [count]);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>useMemo Example</h3>
      <p>Count: {count}</p>
      <p>Double count: {doubleCount}</p>
      <p>Expensive value: {expensiveValue}</p>
      <button onClick={() => setCount(count + 1)} style={{ marginRight: '16px' }}>
        Increment
      </button>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      <p>Name: {name}</p>
    </div>
  );
}

// 7. useRef 示例
function RefExample() {
  const [count, setCount] = useState(0);
  const countRef = useRef(count);
  const inputRef = useRef(null);

  const handleClick = () => {
    setCount(count + 1);
    console.log('Current count (ref):', countRef.current); // 注意：这里会打印旧值
  };

  useEffect(() => {
    countRef.current = count; // 同步更新 ref
  }, [count]);

  const focusInput = () => {
    inputRef.current.focus();
  };

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>useRef Example</h3>
      <p>Count: {count}</p>
      <p>Count (from ref): {countRef.current}</p>
      <button onClick={handleClick} style={{ marginRight: '16px' }}>
        Increment
      </button>
      <button onClick={focusInput}>
        Focus Input
      </button>
      <input
        ref={inputRef}
        type="text"
        placeholder="Enter something"
        style={{ marginLeft: '16px' }}
      />
    </div>
  );
}

// 8. 自定义 Hook 示例
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

function CustomHookExample() {
  const [count, setCount] = useLocalStorage('count', 0);

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Custom Hook Example (useLocalStorage)</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)} style={{ marginRight: '8px' }}>
        Increment
      </button>
      <button onClick={() => setCount(0)}>
        Reset
      </button>
      <p>Check your browser's local storage to see the persisted value.</p>
    </div>
  );
}

// 主应用组件
function App() {
  return (
    <ThemeProvider>
      <div className="App" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        <h1>React Hooks Example</h1>

        <Counter />
        <EffectExample />
        <ThemedButton />
        <ReducerExample />
        <CallbackExample />
        <MemoExample />
        <RefExample />
        <CustomHookExample />
      </div>
    </ThemeProvider>
  );
}

export default App;