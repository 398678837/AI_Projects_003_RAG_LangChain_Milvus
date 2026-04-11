// 微信小程序网络示例代码

// 1. 基本网络请求
const basicRequest = `
// GET请求
wx.request({
  url: 'https://api.example.com/users',
  method: 'GET',
  data: {
    page: 1,
    pageSize: 10
  },
  header: {
    'content-type': 'application/json'
  },
  success(res) {
    console.log('请求成功', res);
    console.log('状态码:', res.statusCode);
    console.log('响应数据:', res.data);
  },
  fail(err) {
    console.error('请求失败', err);
  },
  complete() {
    console.log('请求完成');
  }
});

// POST请求
wx.request({
  url: 'https://api.example.com/users',
  method: 'POST',
  data: {
    name: '张三',
    age: 18
  },
  header: {
    'content-type': 'application/json'
  },
  success(res) {
    console.log('创建成功', res.data);
  }
});

// PUT请求
wx.request({
  url: 'https://api.example.com/users/1',
  method: 'PUT',
  data: {
    name: '李四',
    age: 20
  },
  success(res) {
    console.log('更新成功', res.data);
  }
});

// DELETE请求
wx.request({
  url: 'https://api.example.com/users/1',
  method: 'DELETE',
  success(res) {
    console.log('删除成功');
  }
});
`;

console.log('=== 基本网络请求 ===');
console.log(basicRequest);

// 2. Promise封装
const promiseWrapper = `
// 简单封装
function request(options) {
  return new Promise((resolve, reject) => {
    wx.request({
      ...options,
      success: (res) => {
        if (res.statusCode === 200) {
          resolve(res.data);
        } else {
          reject(new Error('请求失败'));
        }
      },
      fail: reject
    });
  });
}

// 使用
async function getUsers() {
  try {
    const data = await request({
      url: 'https://api.example.com/users',
      method: 'GET'
    });
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
`;

console.log('\n=== Promise封装 ===');
console.log(promiseWrapper);

// 3. 完整的请求封装
const completeWrapper = `
// utils/request.js
const BASE_URL = 'https://api.example.com';

class Request {
  constructor() {
    this.baseURL = BASE_URL;
    this.timeout = 10000;
  }

  // 请求拦截器
  requestInterceptor(config) {
    const token = wx.getStorageSync('token');
    if (token) {
      config.header = {
        ...config.header,
        'Authorization': \`Bearer \${token}\`
      };
    }
    return config;
  }

  // 响应拦截器
  responseInterceptor(response) {
    const { statusCode, data } = response;
    
    if (statusCode === 200) {
      const { code, message, result } = data;
      
      if (code === 0) {
        return result;
      } else if (code === 401) {
        wx.removeStorageSync('token');
        wx.navigateTo({ url: '/pages/login/login' });
        return Promise.reject(new Error(message || '未登录'));
      } else {
        wx.showToast({
          title: message || '请求失败',
          icon: 'none'
        });
        return Promise.reject(new Error(message));
      }
    } else {
      wx.showToast({
        title: '网络错误',
        icon: 'none'
      });
      return Promise.reject(new Error('网络错误'));
    }
  }

  // 错误处理
  errorHandler(error) {
    console.error('请求错误:', error);
    
    if (error.errMsg.includes('timeout')) {
      wx.showToast({
        title: '请求超时',
        icon: 'none'
      });
    } else if (error.errMsg.includes('fail')) {
      wx.showToast({
        title: '网络连接失败',
        icon: 'none'
      });
    }
    
    return Promise.reject(error);
  }

  // 通用请求方法
  request(options) {
    const config = {
      url: this.baseURL + options.url,
      method: options.method || 'GET',
      data: options.data,
      header: options.header,
      timeout: this.timeout
    };

    const finalConfig = this.requestInterceptor(config);

    return new Promise((resolve, reject) => {
      wx.request({
        ...finalConfig,
        success: (response) => {
          try {
            const result = this.responseInterceptor(response);
            resolve(result);
          } catch (err) {
            reject(err);
          }
        },
        fail: (error) => {
          this.errorHandler(error);
          reject(error);
        }
      });
    });
  }

  // 快捷方法
  get(url, data, options = {}) {
    return this.request({
      url,
      method: 'GET',
      data,
      ...options
    });
  }

  post(url, data, options = {}) {
    return this.request({
      url,
      method: 'POST',
      data,
      ...options
    });
  }

  put(url, data, options = {}) {
    return this.request({
      url,
      method: 'PUT',
      data,
      ...options
    });
  }

  delete(url, data, options = {}) {
    return this.request({
      url,
      method: 'DELETE',
      data,
      ...options
    });
  }
}

module.exports = new Request();

// 使用示例
const request = require('@/utils/request');

// GET
async function getUsers() {
  const users = await request.get('/users', { page: 1, pageSize: 10 });
  return users;
}

// POST
async function createUser(data) {
  const user = await request.post('/users', data);
  return user;
}

// PUT
async function updateUser(id, data) {
  const user = await request.put(\`/users/\${id}\`, data);
  return user;
}

// DELETE
async function deleteUser(id) {
  await request.delete(\`/users/\${id}\`);
}
`;

console.log('\n=== 完整的请求封装 ===');
console.log(completeWrapper);

// 4. 文件上传
const fileUpload = `
// 选择图片并上传
function uploadImage() {
  wx.chooseImage({
    count: 1,
    sizeType: ['compressed'],
    sourceType: ['album', 'camera'],
    success(res) {
      const tempFilePath = res.tempFilePaths[0];
      
      wx.showLoading({ title: '上传中...' });
      
      wx.uploadFile({
        url: 'https://api.example.com/upload',
        filePath: tempFilePath,
        name: 'file',
        header: {
          'Authorization': 'Bearer ' + wx.getStorageSync('token')
        },
        formData: {
          type: 'avatar'
        },
        success(res) {
          wx.hideLoading();
          const data = JSON.parse(res.data);
          if (data.code === 0) {
            wx.showToast({ title: '上传成功' });
            console.log('图片URL:', data.url);
          } else {
            wx.showToast({ 
              title: data.message || '上传失败', 
              icon: 'none' 
            });
          }
        },
        fail(err) {
          wx.hideLoading();
          wx.showToast({ 
            title: '上传失败', 
            icon: 'none' 
          });
        }
      });
    }
  });
}

// 多文件上传
async function uploadMultipleFiles(filePaths) {
  const results = [];
  
  for (const filePath of filePaths) {
    const result = await new Promise((resolve, reject) => {
      wx.uploadFile({
        url: 'https://api.example.com/upload',
        filePath,
        name: 'file',
        success: resolve,
        fail: reject
      });
    });
    results.push(JSON.parse(result.data));
  }
  
  return results;
}

// 上传进度
function uploadWithProgress(filePath) {
  const uploadTask = wx.uploadFile({
    url: 'https://api.example.com/upload',
    filePath,
    name: 'file',
    success(res) {
      console.log('上传成功', res);
    }
  });
  
  uploadTask.onProgressUpdate((res) => {
    console.log('上传进度', res.progress);
    console.log('已上传', res.totalBytesSent);
    console.log('总大小', res.totalBytesExpectedToSend);
  });
  
  // 取消上传
  setTimeout(() => {
    uploadTask.abort();
  }, 5000);
}
`;

console.log('\n=== 文件上传 ===');
console.log(fileUpload);

// 5. 文件下载
const fileDownload = `
// 下载文件
function downloadFile(url) {
  wx.showLoading({ title: '下载中...' });
  
  wx.downloadFile({
    url,
    success(res) {
      wx.hideLoading();
      if (res.statusCode === 200) {
        const filePath = res.tempFilePath;
        console.log('下载成功:', filePath);
        
        // 预览文件
        wx.openDocument({
          filePath,
          success() {
            console.log('打开文件成功');
          }
        });
      }
    },
    fail(err) {
      wx.hideLoading();
      wx.showToast({ 
        title: '下载失败', 
        icon: 'none' 
      });
    }
  });
}

// 保存图片到相册
function saveImageToAlbum(url) {
  wx.downloadFile({
    url,
    success(res) {
      if (res.statusCode === 200) {
        wx.saveImageToPhotosAlbum({
          filePath: res.tempFilePath,
          success() {
            wx.showToast({ title: '保存成功' });
          },
          fail(err) {
            if (err.errMsg.includes('auth deny')) {
              wx.showModal({
                title: '提示',
                content: '需要您授权保存图片到相册',
                success(res) {
                  if (res.confirm) {
                    wx.openSetting();
                  }
                }
              });
            }
          }
        });
      }
    }
  });
}

// 下载进度
function downloadWithProgress(url) {
  const downloadTask = wx.downloadFile({
    url,
    success(res) {
      console.log('下载成功', res);
    }
  });
  
  downloadTask.onProgressUpdate((res) => {
    console.log('下载进度', res.progress);
    console.log('已下载', res.totalBytesWritten);
    console.log('总大小', res.totalBytesExpectedToWrite);
  });
  
  // 取消下载
  setTimeout(() => {
    downloadTask.abort();
  }, 5000);
}
`;

console.log('\n=== 文件下载 ===');
console.log(fileDownload);

// 6. 网络状态
const networkStatus = `
// 获取当前网络类型
wx.getNetworkType({
  success(res) {
    console.log('网络类型:', res.networkType);
    // wifi / 2g / 3g / 4g / 5g / unknown / none
  }
});

// 监听网络状态变化
wx.onNetworkStatusChange((res) => {
  console.log('网络状态变化:', res.isConnected);
  console.log('网络类型:', res.networkType);
  
  if (!res.isConnected) {
    wx.showToast({
      title: '网络已断开',
      icon: 'none'
    });
  } else {
    wx.showToast({
      title: '网络已连接',
      icon: 'success'
    });
  }
});

// 取消监听
// wx.offNetworkStatusChange(callback);

// 检查网络并请求
async function requestWithNetworkCheck(options) {
  return new Promise((resolve, reject) => {
    wx.getNetworkType({
      success(res) {
        if (res.networkType === 'none') {
          wx.showToast({
            title: '请检查网络连接',
            icon: 'none'
          });
          reject(new Error('无网络连接'));
        } else {
          wx.request({
            ...options,
            success: resolve,
            fail: reject
          });
        }
      }
    });
  });
}
`;

console.log('\n=== 网络状态 ===');
console.log(networkStatus);

console.log('=== 微信小程序网络 ===');
