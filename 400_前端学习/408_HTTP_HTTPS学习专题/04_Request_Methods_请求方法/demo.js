// HTTP 请求方法示例代码

// 1. 请求方法对比表
const requestMethods = {
  GET: {
    description: '获取资源',
    safe: true,
    idempotent: true,
    hasBody: false,
    useCase: '获取用户列表、查询数据'
  },
  POST: {
    description: '创建资源',
    safe: false,
    idempotent: false,
    hasBody: true,
    useCase: '创建用户、提交表单'
  },
  PUT: {
    description: '更新资源（完整替换）',
    safe: false,
    idempotent: true,
    hasBody: true,
    useCase: '更新整个用户信息'
  },
  PATCH: {
    description: '部分更新资源',
    safe: false,
    idempotent: false,
    hasBody: true,
    useCase: '只更新用户的邮箱'
  },
  DELETE: {
    description: '删除资源',
    safe: false,
    idempotent: true,
    hasBody: false,
    useCase: '删除用户'
  },
  HEAD: {
    description: '获取响应头',
    safe: true,
    idempotent: true,
    hasBody: false,
    useCase: '检查资源是否存在'
  },
  OPTIONS: {
    description: '获取支持的方法',
    safe: true,
    idempotent: true,
    hasBody: false,
    useCase: '预检请求、CORS'
  }
};

console.log('HTTP 请求方法对比:', requestMethods);

// 2. GET 请求示例
async function getExample() {
  console.log('\n=== GET 请求示例 ===');
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=3');
    const data = await response.json();
    console.log('GET - 获取的帖子:', data);
  } catch (error) {
    console.error('GET - 错误:', error);
  }
}

// 3. POST 请求示例
async function postExample() {
  console.log('\n=== POST 请求示例 ===');
  const newPost = {
    title: '新帖子标题',
    body: '新帖子内容',
    userId: 1
  };
  
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newPost)
    });
    const data = await response.json();
    console.log('POST - 创建的帖子:', data);
  } catch (error) {
    console.error('POST - 错误:', error);
  }
}

// 4. PUT 请求示例
async function putExample() {
  console.log('\n=== PUT 请求示例 ===');
  const updatedPost = {
    id: 1,
    title: '更新后的标题',
    body: '更新后的内容',
    userId: 1
  };
  
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updatedPost)
    });
    const data = await response.json();
    console.log('PUT - 更新的帖子:', data);
  } catch (error) {
    console.error('PUT - 错误:', error);
  }
}

// 5. PATCH 请求示例
async function patchExample() {
  console.log('\n=== PATCH 请求示例 ===');
  const partialUpdate = {
    title: '只更新标题'
  };
  
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(partialUpdate)
    });
    const data = await response.json();
    console.log('PATCH - 部分更新的帖子:', data);
  } catch (error) {
    console.error('PATCH - 错误:', error);
  }
}

// 6. DELETE 请求示例
async function deleteExample() {
  console.log('\n=== DELETE 请求示例 ===');
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
      method: 'DELETE'
    });
    console.log('DELETE - 状态码:', response.status);
    console.log('DELETE - 删除成功');
  } catch (error) {
    console.error('DELETE - 错误:', error);
  }
}

// 7. HEAD 请求示例
async function headExample() {
  console.log('\n=== HEAD 请求示例 ===');
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
      method: 'HEAD'
    });
    console.log('HEAD - 状态码:', response.status);
    console.log('HEAD - Content-Type:', response.headers.get('Content-Type'));
    console.log('HEAD - Content-Length:', response.headers.get('Content-Length'));
  } catch (error) {
    console.error('HEAD - 错误:', error);
  }
}

// 8. RESTful API 路由示例
const restfulRoutes = {
  'GET /users': '获取用户列表',
  'GET /users/:id': '获取单个用户',
  'POST /users': '创建用户',
  'PUT /users/:id': '更新用户（完整替换）',
  'PATCH /users/:id': '更新用户（部分更新）',
  'DELETE /users/:id': '删除用户'
};

console.log('\nRESTful API 路由示例:', restfulRoutes);

// 9. 幂等性演示
console.log('\n=== 幂等性演示 ===');
console.log('GET: 多次调用结果相同 ✓');
console.log('PUT: 多次调用结果相同 ✓');
console.log('DELETE: 多次调用结果相同 ✓');
console.log('POST: 多次调用创建多个资源 ✗');
console.log('PATCH: 不一定幂等 ✗');

// 运行所有示例
async function runAllExamples() {
  await getExample();
  await postExample();
  await putExample();
  await patchExample();
  await deleteExample();
  await headExample();
}

runAllExamples();
