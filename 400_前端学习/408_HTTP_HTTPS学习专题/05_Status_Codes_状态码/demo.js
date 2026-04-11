// HTTP 状态码示例代码

// 1. 状态码分类
const statusCodeCategories = {
  '1xx 信息性': {
    description: '请求已接收，继续处理',
    codes: [
      { code: 100, text: 'Continue', meaning: '继续，客户端应继续请求' },
      { code: 101, text: 'Switching Protocols', meaning: '切换协议' }
    ]
  },
  '2xx 成功': {
    description: '请求已成功处理',
    codes: [
      { code: 200, text: 'OK', meaning: '请求成功' },
      { code: 201, text: 'Created', meaning: '资源创建成功' },
      { code: 204, text: 'No Content', meaning: '成功但无内容返回' }
    ]
  },
  '3xx 重定向': {
    description: '需要进一步操作',
    codes: [
      { code: 301, text: 'Moved Permanently', meaning: '永久重定向' },
      { code: 302, text: 'Found', meaning: '临时重定向' },
      { code: 304, text: 'Not Modified', meaning: '资源未修改，使用缓存' }
    ]
  },
  '4xx 客户端错误': {
    description: '请求有错误',
    codes: [
      { code: 400, text: 'Bad Request', meaning: '请求参数错误' },
      { code: 401, text: 'Unauthorized', meaning: '未授权' },
      { code: 403, text: 'Forbidden', meaning: '禁止访问' },
      { code: 404, text: 'Not Found', meaning: '资源未找到' },
      { code: 405, text: 'Method Not Allowed', meaning: '方法不允许' },
      { code: 409, text: 'Conflict', meaning: '资源冲突' }
    ]
  },
  '5xx 服务器错误': {
    description: '服务器处理出错',
    codes: [
      { code: 500, text: 'Internal Server Error', meaning: '服务器内部错误' },
      { code: 502, text: 'Bad Gateway', meaning: '网关错误' },
      { code: 503, text: 'Service Unavailable', meaning: '服务不可用' }
    ]
  }
};

console.log('HTTP 状态码分类:', statusCodeCategories);

// 2. 常见状态码速查表
const commonStatusCodes = {
  200: 'GET请求成功，返回数据',
  201: 'POST请求成功，资源已创建',
  204: 'DELETE/PUT请求成功，无内容返回',
  301: '永久重定向，更新书签',
  302: '临时重定向，保持原方法',
  304: '缓存有效，使用本地缓存',
  400: '请求参数错误，检查输入',
  401: '未登录或token过期',
  403: '权限不足，禁止访问',
  404: '资源不存在，检查URL',
  405: '请求方法错误',
  409: '资源冲突，如重复注册',
  500: '服务器出错，联系后端',
  502: '网关错误，后端服务挂了',
  503: '服务过载，稍后重试'
};

console.log('\n常见状态码速查表:', commonStatusCodes);

// 3. 模拟不同状态码的响应
function simulateStatusCode(code) {
  const responses = {
    200: {
      status: 200,
      statusText: 'OK',
      data: { message: '请求成功', result: [1, 2, 3] }
    },
    201: {
      status: 201,
      statusText: 'Created',
      data: { message: '资源创建成功', id: 100 }
    },
    204: {
      status: 204,
      statusText: 'No Content',
      data: null
    },
    400: {
      status: 400,
      statusText: 'Bad Request',
      error: { code: 'INVALID_PARAM', message: '请求参数错误' }
    },
    401: {
      status: 401,
      statusText: 'Unauthorized',
      error: { code: 'UNAUTHORIZED', message: '未授权，请先登录' }
    },
    403: {
      status: 403,
      statusText: 'Forbidden',
      error: { code: 'FORBIDDEN', message: '权限不足' }
    },
    404: {
      status: 404,
      statusText: 'Not Found',
      error: { code: 'NOT_FOUND', message: '资源不存在' }
    },
    500: {
      status: 500,
      statusText: 'Internal Server Error',
      error: { code: 'INTERNAL_ERROR', message: '服务器内部错误' }
    }
  };
  
  return responses[code] || {
    status: code,
    statusText: 'Unknown',
    error: { code: 'UNKNOWN', message: '未知状态码' }
  };
}

console.log('\n模拟状态码响应:');
console.log('200:', simulateStatusCode(200));
console.log('404:', simulateStatusCode(404));
console.log('500:', simulateStatusCode(500));

// 4. 根据状态码处理响应
function handleResponse(response) {
  const { status } = response;
  
  switch (true) {
    case status >= 200 && status < 300:
      return { success: true, data: response.data };
    case status >= 300 && status < 400:
      return { redirect: true, location: '新位置' };
    case status >= 400 && status < 500:
      return { success: false, error: response.error, type: 'client' };
    case status >= 500 && status < 600:
      return { success: false, error: response.error, type: 'server' };
    default:
      return { success: false, error: '未知错误' };
  }
}

console.log('\n响应处理:');
console.log('200 处理:', handleResponse(simulateStatusCode(200)));
console.log('404 处理:', handleResponse(simulateStatusCode(404)));
console.log('500 处理:', handleResponse(simulateStatusCode(500)));

// 5. RESTful API 状态码使用场景
const restfulStatusCodes = {
  'GET /users': [200, 401, 403, 500],
  'GET /users/:id': [200, 401, 403, 404, 500],
  'POST /users': [201, 400, 401, 403, 409, 500],
  'PUT /users/:id': [200, 204, 400, 401, 403, 404, 500],
  'DELETE /users/:id': [204, 401, 403, 404, 500]
};

console.log('\nRESTful API 状态码使用场景:', restfulStatusCodes);

// 6. 友好的状态码提示
const userFriendlyMessages = {
  200: '操作成功',
  201: '创建成功',
  204: '删除成功',
  400: '请检查您的输入',
  401: '请先登录',
  403: '您没有权限执行此操作',
  404: '页面不存在',
  409: '数据已存在，请检查',
  500: '服务器开小差了，请稍后重试',
  502: '服务暂时不可用',
  503: '服务繁忙，请稍后再试'
};

console.log('\n友好提示:', userFriendlyMessages);

// 7. 实际获取状态码示例
async function fetchStatusExample() {
  console.log('\n=== 实际获取状态码 ===');
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    console.log('状态码:', response.status);
    console.log('状态文本:', response.statusText);
    console.log('是否成功:', response.ok);
  } catch (error) {
    console.error('请求错误:', error);
  }
}

fetchStatusExample();
