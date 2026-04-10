# React 生命周期

## 什么是生命周期？

React 组件从创建到销毁的过程中会经历多个阶段，这些阶段称为生命周期。了解生命周期对于理解 React 组件的行为和优化组件性能非常重要。

## 类组件的生命周期

### 1. 挂载阶段 (Mounting)

- **constructor()**: 组件实例化时调用，用于初始化状态和绑定方法
- **static getDerivedStateFromProps()**: 在渲染前调用，根据 props 更新状态
- **render()**: 渲染组件
- **componentDidMount()**: 组件挂载后调用，用于执行副作用操作（如数据获取、事件监听等）

### 2. 更新阶段 (Updating)

- **static getDerivedStateFromProps()**: 在渲染前调用，根据 props 更新状态
- **shouldComponentUpdate()**: 决定组件是否需要重新渲染
- **render()**: 渲染组件
- **getSnapshotBeforeUpdate()**: 在 DOM 更新前调用，获取更新前的 DOM 状态
- **componentDidUpdate()**: 组件更新后调用，用于执行副作用操作

### 3. 卸载阶段 (Unmounting)

- **componentWillUnmount()**: 组件卸载前调用，用于清理副作用（如清除定时器、取消事件监听等）

### 4. 错误处理阶段 (Error Handling)

- **static getDerivedStateFromError()**: 捕获子组件的错误，更新状态
- **componentDidCatch()**: 捕获子组件的错误，执行副作用操作

## 函数组件的生命周期 (使用 Hooks)

React 16.8 引入了 Hooks，使函数组件也可以使用生命周期特性。

### 1. useState()

用于在函数组件中管理状态。

### 2. useEffect()

用于在函数组件中执行副作用操作，相当于类组件的 `componentDidMount`、`componentDidUpdate` 和 `componentWillUnmount` 的组合。

### 3. useLayoutEffect()

与 `useEffect` 类似，但在 DOM 更新后同步执行，相当于类组件的 `componentDidMount` 和 `componentDidUpdate`。

### 4. useCallback()

用于缓存函数，避免在每次渲染时创建新的函数。

### 5. useMemo()

用于缓存计算结果，避免在每次渲染时重新计算。

### 6. useRef()

用于在组件之间共享数据，相当于类组件的实例属性。

## 生命周期最佳实践

### 1. 避免在 render() 方法中执行副作用操作

`render()` 方法应该是纯函数，只负责渲染 UI，不应该执行副作用操作（如数据获取、修改 DOM 等）。

### 2. 使用 componentDidMount() 执行副作用操作

数据获取、事件监听等副作用操作应该在 `componentDidMount()` 中执行。

### 3. 使用 componentWillUnmount() 清理副作用

定时器、事件监听等副作用应该在 `componentWillUnmount()` 中清理，避免内存泄漏。

### 4. 使用 shouldComponentUpdate() 优化性能

对于复杂的组件，可以使用 `shouldComponentUpdate()` 方法来避免不必要的重新渲染。

### 5. 使用 Hooks 管理副作用

在函数组件中，应该使用 `useEffect()` 来管理副作用，并确保在 effect 函数的返回值中清理副作用。

## 示例代码

### 1. 类组件生命周期示例

```jsx
class LifecycleExample extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    console.log('Constructor');
  }

  static getDerivedStateFromProps(props, state) {
    console.log('getDerivedStateFromProps');
    return null;
  }

  componentDidMount() {
    console.log('componentDidMount');
    this.timer = setInterval(() => {
      this.setState({ count: this.state.count + 1 });
    }, 1000);
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('shouldComponentUpdate');
    return true;
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log('getSnapshotBeforeUpdate');
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log('componentDidUpdate');
  }

  componentWillUnmount() {
    console.log('componentWillUnmount');
    clearInterval(this.timer);
  }

  render() {
    console.log('Render');
    return <div>Count: {this.state.count}</div>;
  }
}
```

### 2. 函数组件生命周期示例 (使用 Hooks)

```jsx
function LifecycleExample() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('Component mounted or updated');
    const timer = setInterval(() => {
      setCount(prevCount => prevCount + 1);
    }, 1000);

    return () => {
      console.log('Component unmounted');
      clearInterval(timer);
    };
  }, []); // 空依赖数组表示只在组件挂载和卸载时执行

  return <div>Count: {count}</div>;
}
```

## 学习资源

- [React 官方文档 - 生命周期](https://react.dev/learn/lifecycle-of-components)
- [React 官方文档 - useEffect](https://react.dev/learn/synchronizing-with-effects)
- [React 官方文档 - Hooks](https://react.dev/learn/hooks-intro)