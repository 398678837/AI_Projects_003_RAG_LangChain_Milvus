# React 组件

## 什么是组件？

组件是 React 应用的基本构建块。组件可以是函数组件或类组件，它们接受输入（称为 props）并返回 React 元素，描述应该在屏幕上显示什么。

## 组件类型

### 1. 函数组件

函数组件是使用 JavaScript 函数定义的组件。它们是 React 16.8 引入 Hooks 后最常用的组件类型。

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

### 2. 类组件

类组件是使用 ES6 类定义的组件。它们在 Hooks 引入之前是 React 中定义有状态组件的主要方式。

```jsx
class Greeting extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

## 组件组合

组件可以组合在一起，形成更复杂的用户界面。

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

## 组件通信

### 1. 父组件向子组件传递数据

使用 props 从父组件向子组件传递数据。

```jsx
// 父组件
function Parent() {
  return <Child name="John" age={30} />;
}

// 子组件
function Child({ name, age }) {
  return (
    <div>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
    </div>
  );
}
```

### 2. 子组件向父组件传递数据

使用回调函数从子组件向父组件传递数据。

```jsx
// 父组件
function Parent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <Child onIncrement={() => setCount(count + 1)} />
    </div>
  );
}

// 子组件
function Child({ onIncrement }) {
  return <button onClick={onIncrement}>Increment</button>;
}
```

## 组件设计原则

### 1. 单一职责

每个组件应该只负责一件事情。如果一个组件变得太大，应该将其拆分为更小的、可复用的组件。

### 2. 可复用性

设计组件时应该考虑它们的可复用性。通过 props 传递数据和行为，使组件更加灵活。

### 3. 可维护性

编写清晰、简洁的组件代码，使用有意义的命名，添加适当的注释。

## 组件最佳实践

### 1. 命名规范

- 组件名称应该使用 PascalCase（首字母大写）
- 文件名应该与组件名称一致
- props 名称应该使用 camelCase

### 2. 代码组织

- 将相关组件放在同一个目录中
- 使用索引文件导出组件
- 分离关注点，将样式、逻辑和模板分开

### 3. 性能优化

- 使用 `React.memo` 缓存组件渲染
- 使用 `useMemo` 和 `useCallback` 缓存计算和函数
- 避免在渲染过程中创建新的函数和对象

## 示例代码

### 1. 基础组件

```jsx
function Button({ children, onClick, variant = 'primary' }) {
  return (
    <button 
      onClick={onClick}
      className={`btn btn-${variant}`}
    >
      {children}
    </button>
  );
}
```

### 2. 复合组件

```jsx
function Card({ title, children }) {
  return (
    <div className="card">
      <div className="card-header">
        <h3>{title}</h3>
      </div>
      <div className="card-body">
        {children}
      </div>
    </div>
  );
}
```

### 3. 高阶组件

```jsx
function withLogging(WrappedComponent) {
  return function LoggedComponent(props) {
    console.log('Component rendered:', WrappedComponent.name);
    return <WrappedComponent {...props} />;
  };
}

const LoggedButton = withLogging(Button);
```

## 学习资源

- [React 官方文档 - 组件和 Props](https://react.dev/learn/passing-props-to-a-component)
- [React 官方文档 - 组件组合](https://react.dev/learn/sharing-state-between-components)
- [React 官方文档 - 组件优化](https://react.dev/learn/optimizing-performance)