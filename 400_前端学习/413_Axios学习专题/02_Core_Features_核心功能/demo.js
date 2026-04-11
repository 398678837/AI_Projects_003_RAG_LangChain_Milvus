// Axios 核心功能示例代码

// 1. 请求方法别名
const requestMethods = `
// GET 请求 - 获取资源
axios.get('/user', { params: { ID: 12345 } })

// POST 请求 - 创建资源
axios.post('/user', { firstName: 'Fred', lastName: 'Flintstone' })

// PUT 请求 - 更新资源（完整替换）
axios.put('/user/12345', { firstName: 'Fred', lastName: 'Smith' })

// PATCH 请求 - 更新资源（部分更新）
axios.patch('/user/12345', { lastName: 'Smith' })

// DELETE 请求 - 删除资源
axios.delete('/user/12345')

// HEAD 请求 - 获取响应头
axios.head('/user/12345')

// OPTIONS 请求 - 获取支持的方法
axios.options('/user')

// 通用请求方法
axios.request({
  method: 'get',
  url: '/user/12345'
})
`;

console.log('=== 请求方法别名 ===');
console.log(requestMethods);

// 2. URL 参数
async function urlParams() {
  console.log('\n=== URL 参数 ===');
  
  // 方式1: 使用 params 配置
  const response1 = await axios.get('https://jsonplaceholder.typicode.com/posts', {
    params: {
      _page: 1,
      _limit: 5,
      _sort: 'id',
      _order: 'desc'
    }
  });
  console.log('方式1 - 文章数量:', response1.data.length);
  
  // 方式2: 直接拼接到 URL
  const response2 = await axios.get(
    'https://jsonplaceholder.typicode.com/posts?_page=1&_limit=3'
  );
  console.log('方式2 - 文章数量:', response2.data.length);
  
  // 方式3: 使用 URLSearchParams
  const params = new URLSearchParams();
  params.append('_page', '1');
  params.append('_limit', '2');
  const response3 = await axios.get(
    'https://jsonplaceholder.typicode.com/posts?' + params
  );
  console.log('方式3 - 文章数量:', response3.data.length);
}

// 3. 请求头
async function requestHeaders() {
  console.log('\n=== 请求头 ===');
  
  const response = await axios.get('https://jsonplaceholder.typicode.com/posts/1', {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer your-token-here',
      'X-Requested-With': 'XMLHttpRequest',
      'Accept': 'application/json'
    }
  });
  
  console.log('请求成功!');
  console.log('响应头:', response.headers);
}

// 4. 并发请求
async function concurrentRequests() {
  console.log('\n=== 并发请求 ===');
  
  // 使用 Promise.all (推荐)
  try {
    const [posts, users, comments] = await Promise.all([
      axios.get('https://jsonplaceholder.typicode.com/posts?_limit=3'),
      axios.get('https://jsonplaceholder.typicode.com/users?_limit=3'),
      axios.get('https://jsonplaceholder.typicode.com/comments?_limit=3')
    ]);
    
    console.log('文章:', posts.data.length);
    console.log('用户:', users.data.length);
    console.log('评论:', comments.data.length);
  } catch (error) {
    console.log('请求失败:', error.message);
  }
  
  // 使用 axios.all + axios.spread (旧写法)
  console.log('\n--- 使用 axios.all ---');
  try {
    await axios.all([
      axios.get('https://jsonplaceholder.typicode.com/posts?_limit=2'),
      axios.get('https://jsonplaceholder.typicode.com/users?_limit=2')
    ]).then(axios.spread((posts, users) => {
      console.log('文章:', posts.data.length);
      console.log('用户:', users.data.length);
    }));
  } catch (error) {
    console.log('请求失败:', error.message);
  }
}

// 5. 文件上传
async function fileUpload() {
  console.log('\n=== 文件上传 ===');
  
  // 使用 FormData
  const formData = new FormData();
  formData.append('username', 'john');
  // formData.append('avatar', fileInput.files[0]);
  
  const uploadExample = `
// 实际使用示例
const fileInput = document.querySelector('input[type="file"]');

async function uploadFile() {
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  formData.append('description', 'My file');
  
  try {
    const response = await axios.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      onUploadProgress: (progressEvent) => {
        const percentCompleted = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
        console.log(\`上传进度: \${percentCompleted}%\`);
      }
    });
    console.log('上传成功!');
  } catch (error) {
    console.log('上传失败:', error.message);
  }
}
`;
  
  console.log(uploadExample);
}

// 6. 下载文件
async function fileDownload() {
  console.log('\n=== 下载文件 ===');
  
  const downloadExample = `
// 下载文件示例
async function downloadFile() {
  try {
    const response = await axios.get('/download/file.pdf', {
      responseType: 'blob'  // 重要：指定响应类型为 blob
    });
    
    // 创建下载链接
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'file.pdf');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    console.log('下载完成!');
  } catch (error) {
    console.log('下载失败:', error.message);
  }
}

// 显示下载进度
async function downloadWithProgress() {
  try {
    const response = await axios.get('/download/large-file.zip', {
      responseType: 'blob',
      onDownloadProgress: (progressEvent) => {
        const percentCompleted = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
        console.log(\`下载进度: \${percentCompleted}%\`);
      }
    });
    // 处理下载...
  } catch (error) {
    console.log('下载失败:', error.message);
  }
}
`;
  
  console.log(downloadExample);
}

// 7. 请求和响应转换
async function transformData() {
  console.log('\n=== 请求和响应转换 ===');
  
  const transformExample = `
// 请求转换 - 在发送请求前修改数据
const client = axios.create({
  transformRequest: [
    function (data, headers) {
      // 修改请求数据
      console.log('请求数据:', data);
      return JSON.stringify(data);
    },
    ...axios.defaults.transformRequest
  ],
  
  transformResponse: [
    ...axios.defaults.transformResponse,
    function (data) {
      // 修改响应数据
      console.log('响应数据:', data);
      if (data && data.data) {
        return data.data;
      }
      return data;
    }
  ]
});

// 使用示例
client.get('/api/data')
  .then(response => {
    console.log('处理后的响应:', response);
  });
`;
  
  console.log(transformExample);
}

// 8. 超时设置
async function timeoutExample() {
  console.log('\n=== 超时设置 ===');
  
  const timeoutConfig = `
// 单次请求超时
axios.get('/api/slow', {
  timeout: 5000  // 5 秒超时
})
  .then(response => console.log('成功:', response))
  .catch(error => {
    if (error.code === 'ECONNABORTED') {
      console.log('请求超时!');
    }
  });

// 全局默认超时
axios.defaults.timeout = 10000;  // 10 秒

// 实例超时
const instance = axios.create({
  timeout: 8000
});
`;
  
  console.log(timeoutConfig);
}

// 9. 验证状态码
async function validateStatus() {
  console.log('\n=== 验证状态码 ===');
  
  const statusConfig = `
// 自定义验证状态码
axios.get('/api/data', {
  validateStatus: function (status) {
    return status >= 200 && status < 300;  // 默认行为
    // 或者接受更多状态码
    // return status < 500;  // 接受小于 500 的状态码
  }
})
  .then(response => console.log('响应:', response))
  .catch(error => console.log('错误:', error));

// 接受 404 作为成功
axios.get('/api/maybe-not-exists', {
  validateStatus: status => status === 200 || status === 404
})
  .then(response => {
    if (response.status === 404) {
      console.log('资源不存在');
    } else {
      console.log('成功:', response.data);
    }
  });
`;
  
  console.log(statusConfig);
}

console.log('=== Axios 核心功能 ===');
console.log('请在浏览器环境中运行这些示例');
