// 微信小程序API示例代码

// 1. 界面交互API
const uiAPI = `
// 提示框
wx.showToast({
  title: '成功',
  icon: 'success',
  duration: 2000
});

wx.showToast({
  title: '加载中',
  icon: 'loading',
  duration: 10000
});

// 模态框
wx.showModal({
  title: '提示',
  content: '这是一个模态弹窗',
  success(res) {
    if (res.confirm) {
      console.log('用户点击确定');
    } else if (res.cancel) {
      console.log('用户点击取消');
    }
  }
});

// 加载提示
wx.showLoading({
  title: '加载中...',
  mask: true
});

setTimeout(() => {
  wx.hideLoading();
}, 2000);

// 操作菜单
wx.showActionSheet({
  itemList: ['拍照', '从相册选择', '取消'],
  success(res) {
    console.log(res.tapIndex);
  }
});
`;

console.log('=== 界面交互API ===');
console.log(uiAPI);

// 2. 路由API
const navigationAPI = `
// 保留当前页面，跳转到新页面
wx.navigateTo({
  url: '/pages/detail/detail?id=1&name=test',
  success() {
    console.log('跳转成功');
  },
  fail(err) {
    console.error('跳转失败', err);
  }
});

// 关闭当前页面，跳转到新页面
wx.redirectTo({
  url: '/pages/home/home'
});

// 关闭所有页面，跳转到新页面
wx.reLaunch({
  url: '/pages/home/home'
});

// 切换到TabBar页面
wx.switchTab({
  url: '/pages/mine/mine'
});

// 返回上一页
wx.navigateBack({
  delta: 1,
  success() {
    console.log('返回成功');
  }
});

// 获取页面栈
const pages = getCurrentPages();
const currentPage = pages[pages.length - 1];
console.log('当前页面:', currentPage.route);
`;

console.log('\n=== 路由API ===');
console.log(navigationAPI);

// 3. 网络请求API
const networkAPI = `
// GET请求
wx.request({
  url: 'https://api.example.com/users',
  method: 'GET',
  data: {
    page: 1,
    pageSize: 10
  },
  header: {
    'content-type': 'application/json',
    'Authorization': 'Bearer token'
  },
  success(res) {
    console.log('请求成功', res.data);
  },
  fail(err) {
    console.error('请求失败', err);
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
  success(res) {
    console.log('创建成功', res.data);
  }
});

// Promise封装
function request(options) {
  return new Promise((resolve, reject) => {
    wx.request({
      ...options,
      success: resolve,
      fail: reject
    });
  });
}

// 使用
async function fetchUsers() {
  try {
    const res = await request({
      url: 'https://api.example.com/users',
      method: 'GET'
    });
    console.log(res.data);
  } catch (err) {
    console.error(err);
  }
}
`;

console.log('\n=== 网络请求API ===');
console.log(networkAPI);

// 4. 媒体API
const mediaAPI = `
// 选择图片
wx.chooseImage({
  count: 9,
  sizeType: ['original', 'compressed'],
  sourceType: ['album', 'camera'],
  success(res) {
    const tempFilePaths = res.tempFilePaths;
    console.log(tempFilePaths);
  }
});

// 预览图片
wx.previewImage({
  current: 'https://example.com/image1.jpg',
  urls: [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    'https://example.com/image3.jpg'
  ]
});

// 上传文件
wx.uploadFile({
  url: 'https://api.example.com/upload',
  filePath: tempFilePath,
  name: 'file',
  formData: {
    user: 'test'
  },
  success(res) {
    const data = JSON.parse(res.data);
    console.log('上传成功', data);
  }
});

// 下载文件
wx.downloadFile({
  url: 'https://example.com/file.pdf',
  success(res) {
    if (res.statusCode === 200) {
      console.log('下载成功', res.tempFilePath);
    }
  }
});

// 保存图片到相册
wx.saveImageToPhotosAlbum({
  filePath: tempFilePath,
  success() {
    wx.showToast({ title: '保存成功' });
  }
});
`;

console.log('\n=== 媒体API ===');
console.log(mediaAPI);

// 5. 存储API
const storageAPI = `
// 同步存储
wx.setStorageSync('username', '张三');
wx.setStorageSync('userInfo', { id: 1, name: '张三' });

// 同步读取
const username = wx.getStorageSync('username');
const userInfo = wx.getStorageSync('userInfo');
console.log(username, userInfo);

// 同步删除
wx.removeStorageSync('username');

// 清空所有
wx.clearStorageSync();

// 异步存储
wx.setStorage({
  key: 'token',
  data: 'abc123',
  success() {
    console.log('存储成功');
  }
});

// 异步读取
wx.getStorage({
  key: 'token',
  success(res) {
    console.log(res.data);
  }
});

// 获取存储信息
wx.getStorageInfo({
  success(res) {
    console.log('所有key:', res.keys);
    console.log('已用大小:', res.currentSize);
    console.log('限制大小:', res.limitSize);
  }
});
`;

console.log('\n=== 存储API ===');
console.log(storageAPI);

// 6. 位置API
const locationAPI = `
// 获取当前位置
wx.getLocation({
  type: 'wgs84',
  success(res) {
    const latitude = res.latitude;
    const longitude = res.longitude;
    console.log('位置:', latitude, longitude);
  }
});

// 选择位置
wx.chooseLocation({
  success(res) {
    console.log('选择的位置:', res.name, res.address);
    console.log('经纬度:', res.latitude, res.longitude);
  }
});

// 打开地图
wx.openLocation({
  latitude: 23.099994,
  longitude: 113.324520,
  scale: 18,
  name: '腾讯大厦',
  address: '广东省深圳市南山区'
});
`;

console.log('\n=== 位置API ===');
console.log(locationAPI);

// 7. 设备API
const deviceAPI = `
// 获取系统信息
wx.getSystemInfo({
  success(res) {
    console.log('手机型号:', res.model);
    console.log('操作系统:', res.system);
    console.log('微信版本:', res.version);
    console.log('屏幕宽度:', res.windowWidth);
    console.log('屏幕高度:', res.windowHeight);
    console.log('状态栏高度:', res.statusBarHeight);
  }
});

// 获取网络类型
wx.getNetworkType({
  success(res) {
    console.log('网络类型:', res.networkType);
  }
});

// 监听网络状态变化
wx.onNetworkStatusChange(res => {
  console.log('网络变化:', res.isConnected, res.networkType);
});

// 震动
wx.vibrateShort({
  type: 'light'
});

wx.vibrateLong();

// 剪贴板
wx.setClipboardData({
  data: '要复制的文本',
  success() {
    wx.showToast({ title: '复制成功' });
  }
});

wx.getClipboardData({
  success(res) {
    console.log('剪贴板内容:', res.data);
  }
});
`;

console.log('\n=== 设备API ===');
console.log(deviceAPI);

// 8. 登录和用户信息API
const authAPI = `
// 登录
wx.login({
  success(res) {
    if (res.code) {
      console.log('code:', res.code);
    }
  }
});

// 获取用户信息 - 旧版
wx.getUserInfo({
  success(res) {
    console.log('用户信息:', res.userInfo);
  }
});

// 获取用户信息 - 新版（需按钮触发）
Page({
  handleGetUserInfo(e) {
    if (e.detail.userInfo) {
      console.log('用户信息:', e.detail.userInfo);
    }
  }
});

// WXML
<button open-type="getUserInfo" bindgetuserinfo="handleGetUserInfo">
  获取用户信息
</button>

// 获取用户授权设置
wx.getSetting({
  success(res) {
    console.log('授权设置:', res.authSetting);
    if (res.authSetting['scope.userLocation']) {
      console.log('已授权位置');
    }
  }
});

// 打开授权设置
wx.openSetting({
  success(res) {
    console.log('授权设置:', res.authSetting);
  }
});
`;

console.log('\n=== 登录和用户信息API ===');
console.log(authAPI);

console.log('=== 微信小程序API ===');
