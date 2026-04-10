import React, { useState, useEffect, useRef } from 'react';

// 类组件生命周期示例
class ClassComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    console.log('Class Component: Constructor');
  }

  static getDerivedStateFromProps(props, state) {
    console.log('Class Component: getDerivedStateFromProps');
    return null;
  }

  componentDidMount() {
    console.log('Class Component: componentDidMount');
    this.timer = setInterval(() => {
      this.setState({ count: this.state.count + 1 });
    }, 1000);
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('Class Component: shouldComponentUpdate');
    return true;
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log('Class Component: getSnapshotBeforeUpdate');
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log('Class Component: componentDidUpdate');
  }

  componentWillUnmount() {
    console.log('Class Component: componentWillUnmount');
    clearInterval(this.timer);
  }

  render() {
    console.log('Class Component: Render');
    return (
      <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
        <h3>Class Component</h3>
        <p>Count: {this.state.count}</p>
        <p>Props: {this.props.message}</p>
      </div>
    );
  }
}

// 函数组件生命周期示例 (使用 Hooks)
function FunctionComponent({ message }) {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  const inputRef = useRef(null);

  // 相当于 componentDidMount 和 componentDidUpdate
  useEffect(() => {
    console.log('Function Component: useEffect (mounted/updated)');
    document.title = `Count: ${count}`;
  });

  // 相当于 componentDidMount
  useEffect(() => {
    console.log('Function Component: useEffect (mounted)');
    const timer = setInterval(() => {
      setCount(prevCount => prevCount + 1);
    }, 1000);

    // 相当于 componentWillUnmount
    return () => {
      console.log('Function Component: useEffect cleanup (unmounted)');
      clearInterval(timer);
    };
  }, []); // 空依赖数组

  // 当 message 变化时执行
  useEffect(() => {
    console.log('Function Component: useEffect (message changed)');
    inputRef.current.focus();
  }, [message]);

  console.log('Function Component: Render');

  return (
    <div style={{ border: '1px solid #dee2e6', padding: '16px', margin: '16px 0' }}>
      <h3>Function Component (with Hooks)</h3>
      <p>Count: {count}</p>
      <p>Props: {message}</p>
      <input
        ref={inputRef}
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
        style={{ margin: '8px 0' }}
      />
      <p>Name: {name}</p>
    </div>
  );
}

// 主应用组件
function App() {
  const [message, setMessage] = useState('Hello, React!');
  const [showComponents, setShowComponents] = useState(true);

  return (
    <div className="App" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <h1>React Lifecycle Example</h1>

      <div style={{ margin: '16px 0' }}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          style={{ padding: '8px', width: '300px' }}
        />
        <button 
          onClick={() => setShowComponents(!showComponents)}
          style={{ marginLeft: '8px', padding: '8px 16px' }}
        >
          {showComponents ? 'Hide Components' : 'Show Components'}
        </button>
      </div>

      {showComponents && (
        <div>
          <ClassComponent message={message} />
          <FunctionComponent message={message} />
        </div>
      )}

      <div style={{ marginTop: '32px' }}>
        <h3>Console Output</h3>
        <p>Check the browser console to see the lifecycle events.</p>
      </div>
    </div>
  );
}

export default App;