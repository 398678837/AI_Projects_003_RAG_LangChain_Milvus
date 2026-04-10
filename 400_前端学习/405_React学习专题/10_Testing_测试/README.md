# React 测试

## 什么是测试？

测试是确保代码质量和功能正确性的过程。在 React 应用中，测试可以帮助我们验证组件的行为是否符合预期，以及在代码变更时是否会引入回归问题。

## 测试类型

### 1. 单元测试

单元测试是测试应用中最小的可测试单元，通常是单个函数或组件。

### 2. 集成测试

集成测试是测试多个组件或模块之间的交互。

### 3. 端到端测试

端到端测试是测试整个应用的流程，模拟用户的真实操作。

## 测试工具

### 1. Jest

Jest 是 Facebook 开发的测试框架，是 React 项目的默认测试框架。

### 2. React Testing Library

React Testing Library 是一个用于测试 React 组件的库，它提供了一系列工具来模拟用户交互和测试组件的行为。

### 3. Enzyme

Enzyme 是 Airbnb 开发的 React 测试工具，它提供了更灵活的 API 来测试组件的内部状态和方法。

## 安装测试依赖

```bash
npm install --save-dev jest @testing-library/react @testing-library/jest-dom
```

## 基本测试示例

### 1. 测试组件渲染

```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

### 2. 测试用户交互

```jsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

test('increments counter when button is clicked', () => {
  render(<Counter />);
  const incrementButton = screen.getByText('Increment');
  const counterElement = screen.getByText('Count: 0');
  
  fireEvent.click(incrementButton);
  
  expect(screen.getByText('Count: 1')).toBeInTheDocument();
});
```

### 3. 测试表单处理

```jsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Form from './Form';

test('submits form with correct data', () => {
  const onSubmit = jest.fn();
  render(<Form onSubmit={onSubmit} />);
  
  const nameInput = screen.getByLabelText('Name:');
  const emailInput = screen.getByLabelText('Email:');
  const submitButton = screen.getByText('Submit');
  
  fireEvent.change(nameInput, { target: { value: 'John Doe' } });
  fireEvent.change(emailInput, { target: { value: 'john@example.com' } });
  fireEvent.click(submitButton);
  
  expect(onSubmit).toHaveBeenCalledWith({
    name: 'John Doe',
    email: 'john@example.com'
  });
});
```

### 4. 测试 API 调用

```jsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import UserList from './UserList';

// Mock fetch API
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve([
      { id: 1, name: 'John Doe' },
      { id: 2, name: 'Jane Smith' }
    ])
  })
);

test('fetches and displays users', async () => {
  render(<UserList />);
  
  // Wait for users to be fetched and displayed
  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
  
  expect(screen.getByText('Jane Smith')).toBeInTheDocument();
});
```

## 测试最佳实践

### 1. 测试行为，而不是实现

测试组件的行为和输出，而不是内部实现细节。这使得测试更加稳定，当组件的实现细节改变时，测试不需要修改。

### 2. 模拟外部依赖

模拟外部依赖，如 API 调用、本地存储等，使得测试更加可控和快速。

### 3. 测试边界情况

测试边界情况，如空数据、错误状态等，确保组件在各种情况下都能正常工作。

### 4. 保持测试简洁

保持测试简洁明了，每个测试只测试一个功能，使得测试更容易理解和维护。

### 5. 测试覆盖率

使用测试覆盖率工具来确保测试覆盖了代码的主要部分，但不要追求 100% 的覆盖率，因为有些代码可能不需要测试。

## 测试配置

### 1. Jest 配置

在 `package.json` 文件中配置 Jest：

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  },
  "jest": {
    "testEnvironment": "jsdom",
    "setupFilesAfterEnv": ["<rootDir>/src/setupTests.js"]
  }
}
```

### 2. 测试设置文件

创建 `src/setupTests.js` 文件，配置测试环境：

```js
import '@testing-library/jest-dom';
```

## 示例代码

### 1. 单元测试示例

```jsx
// Counter.js
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
}

export default Counter;

// Counter.test.js
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

test('renders counter component', () => {
  render(<Counter />);
  expect(screen.getByText('Count: 0')).toBeInTheDocument();
});

test('increments counter when increment button is clicked', () => {
  render(<Counter />);
  const incrementButton = screen.getByText('Increment');
  fireEvent.click(incrementButton);
  expect(screen.getByText('Count: 1')).toBeInTheDocument();
});

test('decrements counter when decrement button is clicked', () => {
  render(<Counter />);
  const decrementButton = screen.getByText('Decrement');
  fireEvent.click(decrementButton);
  expect(screen.getByText('Count: -1')).toBeInTheDocument();
});
```

### 2. 集成测试示例

```jsx
// UserList.js
import React, { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUsers = async () => {
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
      const data = await response.json();
      setUsers(data);
      setLoading(false);
    };

    fetchUsers();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

export default UserList;

// UserList.test.js
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import UserList from './UserList';

// Mock fetch API
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve([
      { id: 1, name: 'John Doe' },
      { id: 2, name: 'Jane Smith' }
    ])
  })
);

test('fetches and displays users', async () => {
  render(<UserList />);
  
  // Check loading state
  expect(screen.getByText('Loading...')).toBeInTheDocument();
  
  // Wait for users to be fetched and displayed
  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
  
  expect(screen.getByText('Jane Smith')).toBeInTheDocument();
});
```

### 3. 端到端测试示例

使用 Cypress 进行端到端测试：

```bash
npm install --save-dev cypress
```

```js
// cypress/integration/app.spec.js
describe('App', () => {
  it('should display welcome message', () => {
    cy.visit('/');
    cy.contains('Welcome to React');
  });

  it('should increment counter when button is clicked', () => {
    cy.visit('/');
    cy.contains('Count: 0');
    cy.get('button').contains('Increment').click();
    cy.contains('Count: 1');
  });
});
```

## 学习资源

- [Jest 官方文档](https://jestjs.io/docs/getting-started)
- [React Testing Library 官方文档](https://testing-library.com/docs/react-testing-library/intro/)
- [Cypress 官方文档](https://docs.cypress.io/)
- [React 官方文档 - 测试](https://react.dev/learn/testing-recipes)