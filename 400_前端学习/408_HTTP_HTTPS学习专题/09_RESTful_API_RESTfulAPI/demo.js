// RESTful API 示例代码

// 1. REST 架构风格特点
const restArchitecturalStyle = {
  客户端服务器: '分离关注点，提高可移植性',
  无状态: '每个请求包含所有必要信息',
  缓存: '利用缓存提高性能',
  统一接口: '统一的资源标识和操作方式',
  分层系统: '分层架构，提高可扩展性',
  按需代码: '可选，服务器可以返回可执行代码'
};

console.log('REST 架构风格特点:', restArchitecturalStyle);

// 2. RESTful API 路由设计示例
const restfulRoutes = {
  用户管理: {
    'GET /users': '获取用户列表',
    'GET /users/:id': '获取单个用户',
    'POST /users': '创建用户',
    'PUT /users/:id': '更新用户（完整替换）',
    'PATCH /users/:id': '更新用户（部分更新）',
    'DELETE /users/:id': '删除用户'
  },
  文章管理: {
    'GET /posts': '获取文章列表',
    'GET /posts/:id': '获取单篇文章',
    'POST /posts': '创建文章',
    'PUT /posts/:id': '更新文章',
    'DELETE /posts/:id': '删除文章',
    'GET /posts/:id/comments': '获取文章评论',
    'POST /posts/:id/comments': '添加评论'
  },
  订单管理: {
    'GET /orders': '获取订单列表',
    'GET /orders/:id': '获取订单详情',
    'POST /orders': '创建订单',
    'PUT /orders/:id/status': '更新订单状态'
  }
};

console.log('\nRESTful API 路由设计:', restfulRoutes);

// 3. HTTP 方法与 CRUD 对应
const httpMethodsCRUD = {
  GET: {
    CRUD: 'Read',
    用途: '获取资源',
    幂等: '是',
    安全: '是',
    示例: 'GET /users, GET /users/1'
  },
  POST: {
    CRUD: 'Create',
    用途: '创建资源',
    幂等: '否',
    安全: '否',
    示例: 'POST /users'
  },
  PUT: {
    CRUD: 'Update',
    用途: '更新资源（完整替换）',
    幂等: '是',
    安全: '否',
    示例: 'PUT /users/1'
  },
  PATCH: {
    CRUD: 'Update',
    用途: '更新资源（部分更新）',
    幂等: '否',
    安全: '否',
    示例: 'PATCH /users/1'
  },
  DELETE: {
    CRUD: 'Delete',
    用途: '删除资源',
    幂等: '是',
    安全: '否',
    示例: 'DELETE /users/1'
  }
};

console.log('\nHTTP 方法与 CRUD:', httpMethodsCRUD);

// 4. 统一响应格式
function successResponse(data, message = '成功') {
  return {
    success: true,
    message: message,
    data: data,
    timestamp: new Date().toISOString()
  };
}

function errorResponse(code, message, details = null) {
  return {
    success: false,
    error: {
      code: code,
      message: message,
      details: details
    },
    timestamp: new Date().toISOString()
  };
}

console.log('\n成功响应:', successResponse({ id: 1, name: '张三' }));
console.log('\n错误响应:', errorResponse('NOT_FOUND', '资源不存在', { resource: 'user', id: 1 }));

// 5. 查询参数使用示例
const queryParamsExamples = {
  分页: 'GET /users?page=1&limit=10',
  排序: 'GET /users?sort=name&order=asc',
  过滤: 'GET /users?status=active&role=admin',
  搜索: 'GET /users?q=张三',
  字段选择: 'GET /users?fields=id,name,email',
  包含关联: 'GET /users?include=posts,orders'
};

console.log('\n查询参数示例:', queryParamsExamples);

// 6. API 版本管理
const apiVersioning = {
  URL路径: '/api/v1/users, /api/v2/users',
  查询参数: '/api/users?version=1',
  请求头: 'Accept: application/vnd.example.v1+json'
};

console.log('\nAPI 版本管理:', apiVersioning);

// 7. 模拟 RESTful API 服务
class MockAPIService {
  constructor() {
    this.users = [
      { id: 1, name: '张三', email: 'zhangsan@example.com', status: 'active' },
      { id: 2, name: '李四', email: 'lisi@example.com', status: 'active' },
      { id: 3, name: '王五', email: 'wangwu@example.com', status: 'inactive' }
    ];
    this.nextId = 4;
  }

  async getUsers(params = {}) {
    let result = [...this.users];
    
    if (params.status) {
      result = result.filter(u => u.status === params.status);
    }
    
    if (params.sort) {
      result.sort((a, b) => {
        const aVal = a[params.sort];
        const bVal = b[params.sort];
        const order = params.order === 'desc' ? -1 : 1;
        return aVal > bVal ? order : -order;
      });
    }
    
    return successResponse(result);
  }

  async getUser(id) {
    const user = this.users.find(u => u.id === parseInt(id));
    if (!user) {
      return errorResponse('NOT_FOUND', '用户不存在');
    }
    return successResponse(user);
  }

  async createUser(data) {
    const newUser = {
      id: this.nextId++,
      name: data.name,
      email: data.email,
      status: 'active'
    };
    this.users.push(newUser);
    return successResponse(newUser, '创建成功');
  }

  async updateUser(id, data) {
    const index = this.users.findIndex(u => u.id === parseInt(id));
    if (index === -1) {
      return errorResponse('NOT_FOUND', '用户不存在');
    }
    this.users[index] = { ...this.users[index], ...data };
    return successResponse(this.users[index], '更新成功');
  }

  async deleteUser(id) {
    const index = this.users.findIndex(u => u.id === parseInt(id));
    if (index === -1) {
      return errorResponse('NOT_FOUND', '用户不存在');
    }
    this.users.splice(index, 1);
    return successResponse(null, '删除成功');
  }
}

// 使用模拟API
console.log('\n=== 模拟 RESTful API ===');
const api = new MockAPIService();

async function runAPIDemo() {
  console.log('获取所有用户:', await api.getUsers());
  console.log('获取活跃用户:', await api.getUsers({ status: 'active' }));
  console.log('获取用户1:', await api.getUser(1));
  console.log('创建用户:', await api.createUser({ name: '赵六', email: 'zhaoliu@example.com' }));
  console.log('更新用户1:', await api.updateUser(1, { name: '张三三' }));
  console.log('删除用户3:', await api.deleteUser(3));
}

runAPIDemo();

// 8. RESTful API 设计最佳实践
const bestPractices = {
  使用名词: '资源用名词复数（/users），不用动词',
  HTTP方法: '用HTTP方法表示操作（GET/POST/PUT/PATCH/DELETE）',
  状态码: '正确使用HTTP状态码（200/201/400/401/404/500）',
  版本管理: 'API版本化（/api/v1/）',
  分页: '列表接口支持分页',
  过滤排序: '支持过滤、排序、搜索',
  统一格式: '统一响应格式',
  错误处理: '清晰的错误信息',
  文档: '完善的API文档',
  HATEOAS: '超媒体作为应用状态引擎（可选）'
};

console.log('\nRESTful API 设计最佳实践:', bestPractices);

// 9. 常见错误码对应
const errorStatusCodes = {
  400: '请求参数错误',
  401: '未授权，需要登录',
  403: '权限不足',
  404: '资源不存在',
  405: '方法不允许',
  409: '资源冲突',
  422: '验证失败',
  429: '请求过于频繁',
  500: '服务器内部错误',
  503: '服务不可用'
};

console.log('\n常见错误码:', errorStatusCodes);
