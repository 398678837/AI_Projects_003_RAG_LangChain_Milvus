// 微信小程序最佳实践示例代码

// 1. 推荐的项目结构
const projectStructure = `
project-root/
├── pages/                    # 页面
│   ├── index/
│   │   ├── index.js
│   │   ├── index.json
│   │   ├── index.wxml
│   │   └── index.wxss
│   └── detail/
├── components/               # 组件
│   ├── my-button/
│   └── my-card/
├── utils/                    # 工具函数
│   ├── request.js            # 网络请求
│   ├── storage.js            # 存储
│   ├── auth.js               # 认证
│   └── format.js             # 格式化
├── api/                      # API接口
│   ├── user.js
│   ├── order.js
│   └── product.js
├── assets/                   # 静态资源
│   ├── images/
│   └── tabbar/
├── constants/                # 常量
│   ├── index.js
│   └── config.js
├── app.js
├── app.json
├── app.wxss
├── sitemap.json
└── project.config.json
`;

console.log('=== 推荐的项目结构 ===');
console.log(projectStructure);

// 2. setData性能优化
const setDataOpt = `
// ❌ 错误做法 - 频繁调用setData
Page({
  data: { count: 0 },
  badPractice() {
    for (let i = 0; i < 100; i++) {
      this.setData({ count: this.data.count + 1 });
    }
  }
});

// ✅ 正确做法 - 合并更新
Page({
  data: { count: 0 },
  goodPractice() {
    let count = this.data.count;
    for (let i = 0; i < 100; i++) {
      count++;
    }
    this.setData({ count });
  }
});

// ✅ 正确做法 - 只更新需要的字段
Page({
  data: {
    user: { name: '张三', age: 18, avatar: '...' },
    list: [1, 2, 3, 4, 5]
  },
  updateAge() {
    this.setData({
      'user.age': 20  // 只更新age字段
    });
  },
  updateListItem() {
    this.setData({
      'list[2]': 99  // 只更新数组某一项
    });
  }
});

// ✅ 正确做法 - 使用setData回调
Page({
  data: { loading: false, list: [] },
  fetchData() {
    this.setData({ loading: true }, () => {
      // 确保loading更新后再请求
      this.requestData();
    });
  }
});

// ✅ 正确做法 - 大数据列表使用虚拟滚动
// 只渲染可视区域的内容
Page({
  data: {
    allList: [],      // 所有数据
    visibleList: [],  // 可视区域数据
    startIndex: 0,
    endIndex: 20
  },
  onScroll(e) {
    const scrollTop = e.detail.scrollTop;
    const startIndex = Math.floor(scrollTop / 100); // 每项高度100rpx
    this.setVisibleList(startIndex);
  },
  setVisibleList(startIndex) {
    const endIndex = startIndex + 20;
    const visibleList = this.data.allList.slice(startIndex, endIndex);
    this.setData({
      visibleList,
      startIndex,
      endIndex
    });
  }
});
`;

console.log('\n=== setData性能优化 ===');
console.log(setDataOpt);

// 3. 图片优化
const imageOpt = `
// ✅ 使用WebP格式
// 在支持WebP的设备上使用WebP
<image 
  src="{{ imageUrl }}" 
  mode="aspectFill" 
  webp
  lazy-load
/>

// ✅ 使用懒加载
<image 
  src="{{ item.image }}" 
  lazy-load
  wx:for="{{ list }}" 
  wx:key="id"
/>

// ✅ 图片压缩
// 上传前压缩图片
wx.chooseImage({
  count: 1,
  sizeType: ['compressed'],  // 使用压缩图
  sourceType: ['album', 'camera'],
  success(res) {
    const tempFilePath = res.tempFilePaths[0];
    console.log('压缩后的图片:', tempFilePath);
  }
});

// ✅ 图片尺寸适配
// 根据设备像素比选择合适的图片
function getImageUrl(baseUrl, width) {
  const systemInfo = wx.getSystemInfoSync();
  const pixelRatio = systemInfo.pixelRatio;
  const realWidth = Math.ceil(width * pixelRatio);
  return \`\${baseUrl}?w=\${realWidth}\`;
}

// ✅ 图片占位
// 使用占位图或骨架屏
<view class="image-container">
  <image 
    src="{{ imageUrl }}" 
    mode="aspectFill"
    bindload="onImageLoad"
    class="{{ loaded ? 'loaded' : '' }}"
  />
  <view wx:if="{{ !loaded }}" class="placeholder"></view>
</view>

// ✅ 使用CDN
// 将图片上传到CDN，使用CDN链接
const CDN_BASE = 'https://cdn.example.com';
function getCDNUrl(path) {
  return \`\${CDN_BASE}\${path}\`;
}
`;

console.log('\n=== 图片优化 ===');
console.log(imageOpt);

// 4. 分包加载
const subPackages = `
// app.json - 分包配置
{
  "pages": [
    "pages/index/index",
    "pages/mine/mine"
  ],
  "subPackages": [
    {
      "root": "pages/mall",
      "name": "mall",
      "pages": [
        "product/list",
        "product/detail",
        "cart/index",
        "order/index"
      ]
    },
    {
      "root": "pages/user",
      "name": "user",
      "pages": [
        "profile/index",
        "settings/index",
        "address/list",
        "address/edit"
      ]
    }
  ],
  "preloadRule": {
    "pages/index/index": {
      "network": "wifi",
      "packages": ["mall"]
    },
    "pages/mine/mine": {
      "network": "all",
      "packages": ["user"]
    }
  }
}

// 独立分包
{
  "subPackages": [
    {
      "root": "pages/game",
      "name": "game",
      "independent": true,  // 独立分包
      "pages": [
        "index",
        "play"
      ]
    }
  ]
}

// 预加载分包
// 进入首页时预加载商城分包
Page({
  onLoad() {
    // 分包会根据preloadRule自动预加载
  },
  goToMall() {
    // 跳转到分包页面
    wx.navigateTo({
      url: '/pages/mall/product/list'
    });
  }
});
`;

console.log('\n=== 分包加载 ===');
console.log(subPackages);

// 5. 用户体验优化
const uxOpt = `
// ✅ 加载状态
Page({
  data: { loading: false },
  async fetchData() {
    this.setData({ loading: true });
    try {
      const data = await request.get('/api/data');
      this.setData({ data });
    } catch (err) {
      console.error(err);
    } finally {
      this.setData({ loading: false });
    }
  }
});

// WXML
<view wx:if="{{ loading }}" class="loading">
  <text>加载中...</text>
</view>
<view wx:else>
  <!-- 内容 -->
</view>

// ✅ 错误处理
Page({
  data: { error: null },
  async fetchData() {
    try {
      const data = await request.get('/api/data');
      this.setData({ data, error: null });
    } catch (err) {
      this.setData({ error: err.message });
    }
  },
  retry() {
    this.fetchData();
  }
});

// WXML
<view wx:if="{{ error }}" class="error">
  <text>{{ error }}</text>
  <button bindtap="retry">重试</button>
</view>

// ✅ 空状态
Page({
  data: { list: [] },
  async fetchList() {
    const list = await request.get('/api/list');
    this.setData({ list });
  }
});

// WXML
<view wx:if="{{ list.length === 0 }}" class="empty">
  <image src="/assets/empty.png" />
  <text>暂无数据</text>
  <button bindtap="fetchList">刷新</button>
</view>
<view wx:else>
  <view wx:for="{{ list }}" wx:key="id">
    {{ item.name }}
  </view>
</view>

// ✅ 下拉刷新和上拉加载
Page({
  data: {
    list: [],
    page: 1,
    pageSize: 10,
    hasMore: true
  },
  
  onLoad() {
    this.fetchList();
  },
  
  onPullDownRefresh() {
    this.setData({ page: 1 });
    this.fetchList(true).then(() => {
      wx.stopPullDownRefresh();
    });
  },
  
  onReachBottom() {
    if (this.data.hasMore) {
      this.setData({ page: this.data.page + 1 });
      this.fetchList();
    }
  },
  
  async fetchList(isRefresh = false) {
    const { page, pageSize, list } = this.data;
    const data = await request.get('/api/list', { page, pageSize });
    
    this.setData({
      list: isRefresh ? data.list : [...list, ...data.list],
      hasMore: data.list.length === pageSize
    });
  }
});
`;

console.log('\n=== 用户体验优化 ===');
console.log(uxOpt);

// 6. 安全实践
const security = `
// ✅ 数据校验
function validateUser(data) {
  if (!data.name || data.name.trim() === '') {
    throw new Error('用户名不能为空');
  }
  if (data.name.length < 2 || data.name.length > 20) {
    throw new Error('用户名长度应为2-20个字符');
  }
  if (!data.email || !/^\\S+@\\S+\\.\\S+$/.test(data.email)) {
    throw new Error('邮箱格式不正确');
  }
  return true;
}

// ✅ 防止XSS
function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// ✅ Token安全存储
// 不要在URL中传递Token
// 使用Authorization header
const request = {
  header: {
    'Authorization': \`Bearer \${token}\`
  }
};

// ✅ 接口签名
function generateSignature(params, secret) {
  const sortedKeys = Object.keys(params).sort();
  const signStr = sortedKeys
    .map(key => \`\${key}=\${params[key]}\`)
    .join('&') + secret;
  
  return md5(signStr);
}

// ✅ 权限控制
function checkPermission(permission) {
  const userInfo = wx.getStorageSync('userInfo');
  if (!userInfo) {
    wx.navigateTo({ url: '/pages/login/login' });
    return false;
  }
  return userInfo.permissions.includes(permission);
}

// ✅ 敏感数据脱敏
function maskPhone(phone) {
  return phone.replace(/(\\d{3})\\d{4}(\\d{4})/, '$1****$2');
}

function maskIdCard(idCard) {
  return idCard.replace(/(\\d{6})\\d{8}(\\d{4})/, '$1********$2');
}

// ✅ HTTPS
// 所有接口都使用HTTPS
// 在小程序后台配置合法域名
`;

console.log('\n=== 安全实践 ===');
console.log(security);

// 7. 代码规范
const codeStyle = `
// ✅ 命名规范
// 文件名：小写+连字符
// pages/user-profile/user-profile.js

// 变量名：小驼峰
const userName = '张三';
const getUserInfo = () => {};

// 常量名：大写下划线
const MAX_COUNT = 100;
const API_BASE_URL = 'https://api.example.com';

// 组件名：大驼峰
// components/MyButton/MyButton.js

// ✅ 注释规范
/**
 * 获取用户信息
 * @param {number} userId - 用户ID
 * @returns {Promise<Object>} 用户信息
 */
async function getUserInfo(userId) {
  return request.get(\`/users/\${userId}\`);
}

// ✅ 模块化
// utils/auth.js
const TOKEN_KEY = 'token';

function setToken(token) {
  wx.setStorageSync(TOKEN_KEY, token);
}

function getToken() {
  return wx.getStorageSync(TOKEN_KEY);
}

function removeToken() {
  wx.removeStorageSync(TOKEN_KEY);
}

module.exports = {
  setToken,
  getToken,
  removeToken
};

// ✅ 错误处理
async function fetchData() {
  try {
    const data = await request.get('/api/data');
    return data;
  } catch (err) {
    console.error('获取数据失败:', err);
    wx.showToast({
      title: err.message || '获取数据失败',
      icon: 'none'
    });
    throw err;
  }
}

// ✅ 使用ES6+
const arr = [1, 2, 3];
const newArr = [...arr, 4, 5];

const obj = { a: 1, b: 2 };
const newObj = { ...obj, c: 3 };

async function asyncFunc() {
  const result = await someAsyncFunction();
  return result;
}
`;

console.log('\n=== 代码规范 ===');
console.log(codeStyle);

console.log('\n🎉 微信小程序学习专题完成！');
console.log('💡 记住：注重性能优化，提升用户体验，保持代码规范！');
console.log('🚀 现在你可以开发优秀的微信小程序了！');
`;

console.log('\n=== 微信小程序最佳实践 ===');
console.log(codeStyle);
