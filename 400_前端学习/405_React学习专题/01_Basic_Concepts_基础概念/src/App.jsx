import React, { useState } from 'react';

// 函数组件
function Greeting({ name }) {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>Welcome to React.</p>
    </div>
  );
}

// 类组件
class CounterClass extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  decrement = () => {
    this.setState({ count: this.state.count - 1 });
  };

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.increment}>Increment</button>
        <button onClick={this.decrement}>Decrement</button>
      </div>
    );
  }
}

// 使用 Hooks 的函数组件
function CounterFunction() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
}

// 主应用组件
function App() {
  return (
    <div className="App">
      <h1>React 基础概念示例</h1>
      
      <section>
        <h2>1. 函数组件</h2>
        <Greeting name="World" />
      </section>

      <section>
        <h2>2. 类组件</h2>
        <CounterClass />
      </section>

      <section>
        <h2>3. 函数组件 + Hooks</h2>
        <CounterFunction />
      </section>

      <section>
        <h2>4. JSX 示例</h2>
        <div>
          <p>当前时间: {new Date().toLocaleTimeString()}</p>
          <ul>
            {['React', 'Vue', 'Angular'].map((framework, index) => (
              <li key={index}>{framework}</li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}

export default App;