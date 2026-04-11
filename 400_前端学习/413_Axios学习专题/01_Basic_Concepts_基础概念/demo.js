// Axios 基础概念示例代码

// 1. 安装 Axios
const installAxios = `
# npm
npm install axios

# yarn
yarn add axios

# pnpm
pnpm add axios

# CDN 引入
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
`;

console.log('=== 安装 Axios ===');
console.log(installAxios);

// 2. 引入 Axios
const importAxios = `
// ES Modules
import axios from 'axios'

// CommonJS
const axios = require('axios')

// 浏览器直接使用
// <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
`;

console.log('\n=== 引入 Axios ===');
console.log(importAxios);

// 3. 第一个 GET 请求 - Promise 方式
function firstGetRequest() {
  console.log('\n=== 第一个 GET 请求 ===');
  
  axios.get('https://jsonplaceholder.typicode.com/posts/1')
    .then(function (response) {
      console.log('请求成功!');
      console.log('状态码:', response.status);
      console.log('响应数据:', response.data);
    })
    .catch(function (error) {
      console.log('请求失败:', error.message);
    })
    .finally(function () {
      console.log('请求完成（无论成功或失败）');
    });
}

// 4. 使用 async/await
async function getRequestWithAsyncAwait() {
  console.log('\n=== 使用 async/await ===');
  
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
    console.log('请求成功!');
    console.log('标题:', response.data.title);
    console.log('内容:', response.data.body);
  } catch (error) {
    console.log('请求失败:', error.message);
  }
}

// 5. POST 请求
async function postRequest() {
  console.log('\n=== POST 请求 ===');
  
  const newPost = {
    title: 'foo',
    body: 'bar',
    userId: 1
  };
  
  try {
    const response = await axios.post(
      'https://jsonplaceholder.typicode.com/posts',
      newPost
    );
    console.log('POST 成功!');
    console.log('创建的文章 ID:', response.data.id);
    console.log('响应数据:', response.data);
  } catch (error) {
    console.log('POST 失败:', error.message);
  }
}

// 6. PUT 请求
async function putRequest() {
  console.log('\n=== PUT 请求 ===');
  
  const updatedPost = {
    id: 1,
    title: 'foo updated',
    body: 'bar updated',
    userId: 1
  };
  
  try {
    const response = await axios.put(
      'https://jsonplaceholder.typicode.com/posts/1',
      updatedPost
    );
    console.log('PUT 成功!');
    console.log('更新后的标题:', response.data.title);
  } catch (error) {
    console.log('PUT 失败:', error.message);
  }
}

// 7. DELETE 请求
async function deleteRequest() {
  console.log('\n=== DELETE 请求 ===');
  
  try {
    const response = await axios.delete(
      'https://jsonplaceholder.typicode.com/posts/1'
    );
    console.log('DELETE 成功!');
    console.log('状态码:', response.status);
  } catch (error) {
    console.log('DELETE 失败:', error.message);
  }
}

// 8. 响应结构
async function responseStructure() {
  console.log('\n=== 响应结构 ===');
  
  const response = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
  
  console.log('响应对象包含:');
  console.log('- data:', response.data);            // 服务器返回的数据
  console.log('- status:', response.status);        // HTTP 状态码
  console.log('- statusText:', response.statusText); // HTTP 状态信息
  console.log('- headers:', response.headers);      // 响应头
  console.log('- config:', response.config);        // 请求配置
}

// 9. 同时发起多个请求
async function multipleRequests() {
  console.log('\n=== 同时发起多个请求 ===');
  
  try {
    const [postsResponse, usersResponse] = await Promise.all([
      axios.get('https://jsonplaceholder.typicode.com/posts?_limit=3'),
      axios.get('https://jsonplaceholder.typicode.com/users?_limit=3')
    ]);
    
    console.log('文章数量:', postsResponse.data.length);
    console.log('用户数量:', usersResponse.data.length);
  } catch (error) {
    console.log('请求失败:', error.message);
  }
}

// 10. 使用配置对象方式
async function requestWithConfig() {
  console.log('\n=== 使用配置对象方式 ===');
  
  try {
    const response = await axios({
      method: 'get',
      url: 'https://jsonplaceholder.typicode.com/posts/1',
      timeout: 5000
    });
    console.log('请求成功!');
    console.log('标题:', response.data.title);
  } catch (error) {
    console.log('请求失败:', error.message);
  }
}

// 运行示例
console.log('=== Axios 基础概念 ===');
console.log('请在浏览器环境中运行这些示例');
console.log('\n主要内容:');
console.log('1. 安装和引入');
console.log('2. GET/POST/PUT/DELETE 请求');
console.log('3. Promise 和 async/await');
console.log('4. 响应结构');
console.log('5. 多个请求并发');
