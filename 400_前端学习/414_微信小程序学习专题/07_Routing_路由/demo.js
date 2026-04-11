// 微信小程序路由示例代码

// 1. 路由方式
const routingMethods = `
// 1. wx.navigateTo - 保留当前页面，跳转到新页面
wx.navigateTo({
  url: '/pages/detail/detail?id=1&name=test',
  success() {
    console.log('跳转成功');
  },
  fail(err) {
    console.error('跳转失败', err);
  }
});

// 特点：
// - 保留当前页面（压入页面栈）
// - 可以返回
// - 页面栈最多10层

// 2. wx.redirectTo - 关闭当前页面，跳转到新页面
wx.redirectTo({
  url: '/pages/home/home'
});

// 特点：
// - 关闭当前页面（替换页面栈）
// - 不能返回到原页面
// - 不增加页面栈深度

// 3. wx.switchTab - 跳转到TabBar页面
wx.switchTab({
  url: '/pages/mine/mine'
});

// 特点：
// - 只能跳转到TabBar页面
// - 会关闭所有非TabBar页面
// - 不能传递参数

// 4. wx.reLaunch - 关闭所有页面，跳转到新页面
wx.reLaunch({
  url: '/pages/home/home'
});

// 特点：
// - 关闭所有页面（清空页面栈）
// - 可以跳转到任意页面
// - 可以传递参数

// 5. wx.navigateBack - 返回上一页
wx.navigateBack({
  delta: 1,
  success() {
    console.log('返回成功');
  }
});

// 特点：
// - 返回上一页或多页
// - delta表示返回几层
// - delta超过页面栈则返回首页
`;

console.log('=== 路由方式 ===');
console.log(routingMethods);

// 2. 参数传递
const parameterPassing = `
// 1. URL参数传递
// 页面A - 跳转时传参
wx.navigateTo({
  url: '/pages/detail/detail?id=1&name=张三&age=18'
});

// 页面B - 接收参数
Page({
  onLoad(options) {
    console.log(options.id);      // '1'
    console.log(options.name);    // '张三'
    console.log(options.age);     // '18'
    
    // 注意：所有参数都是字符串类型
    const id = parseInt(options.id);
    const age = parseInt(options.age);
  }
});

// 2. 传递复杂数据
// 页面A - 使用encodeURIComponent
const user = { id: 1, name: '张三', age: 18 };
wx.navigateTo({
  url: '/pages/detail/detail?data=' + encodeURIComponent(JSON.stringify(user))
});

// 页面B - 接收并解析
Page({
  onLoad(options) {
    if (options.data) {
      const user = JSON.parse(decodeURIComponent(options.data));
      console.log(user);
    }
  }
});

// 3. 使用全局数据
// app.js
App({
  globalData: {
    userInfo: null
  }
});

// 页面A - 设置全局数据
const app = getApp();
app.globalData.userInfo = { id: 1, name: '张三' };
wx.navigateTo({ url: '/pages/detail/detail' });

// 页面B - 获取全局数据
Page({
  onLoad() {
    const app = getApp();
    console.log(app.globalData.userInfo);
  }
});

// 4. 使用本地存储
// 页面A
wx.setStorageSync('userInfo', { id: 1, name: '张三' });
wx.navigateTo({ url: '/pages/detail/detail' });

// 页面B
Page({
  onLoad() {
    const userInfo = wx.getStorageSync('userInfo');
    console.log(userInfo);
  }
});

// 5. 使用页面栈（返回时传参）
// 页面A
Page({
  data: { message: '' },
  onShow() {
    const pages = getCurrentPages();
    const currentPage = pages[pages.length - 1];
    if (currentPage.data.returnData) {
      this.setData({
        message: currentPage.data.returnData
      });
    }
  },
  goToDetail() {
    wx.navigateTo({ url: '/pages/detail/detail' });
  }
});

// 页面B
Page({
  goBack() {
    const pages = getCurrentPages();
    const prevPage = pages[pages.length - 2];
    prevPage.setData({
      returnData: '来自页面B的数据'
    });
    wx.navigateBack();
  }
});
`;

console.log('\n=== 参数传递 ===');
console.log(parameterPassing);

// 3. 页面栈
const pageStack = `
// 获取页面栈
const pages = getCurrentPages();
console.log('页面栈长度:', pages.length);
console.log('当前页面:', pages[pages.length - 1]);
console.log('上一页面:', pages[pages.length - 2]);
console.log('首页:', pages[0]);

// 页面信息
const currentPage = pages[pages.length - 1];
console.log('页面路径:', currentPage.route);
console.log('页面数据:', currentPage.data);
console.log('页面选项:', currentPage.options);

// 示例：判断是否可以返回
function canGoBack() {
  const pages = getCurrentPages();
  return pages.length > 1;
}

// 示例：返回首页
function goHome() {
  const pages = getCurrentPages();
  const delta = pages.length - 1;
  wx.navigateBack({ delta });
}

// 示例：获取特定页面
function getPageByRoute(route) {
  const pages = getCurrentPages();
  return pages.find(page => page.route === route);
}

// 注意事项：
// 1. 页面栈最多10层
// 2. switchTab会清空非TabBar页面
// 3. reLaunch会清空所有页面
`;

console.log('\n=== 页面栈 ===');
console.log(pageStack);

// 4. TabBar配置
const tabBarConfig = `
// app.json
{
  "pages": [
    "pages/index/index",
    "pages/category/category",
    "pages/cart/cart",
    "pages/mine/mine"
  ],
  "tabBar": {
    "color": "#666666",
    "selectedColor": "#07c160",
    "backgroundColor": "#ffffff",
    "borderStyle": "black",
    "list": [
      {
        "pagePath": "pages/index/index",
        "text": "首页",
        "iconPath": "assets/tabbar/home.png",
        "selectedIconPath": "assets/tabbar/home-active.png"
      },
      {
        "pagePath": "pages/category/category",
        "text": "分类",
        "iconPath": "assets/tabbar/category.png",
        "selectedIconPath": "assets/tabbar/category-active.png"
      },
      {
        "pagePath": "pages/cart/cart",
        "text": "购物车",
        "iconPath": "assets/tabbar/cart.png",
        "selectedIconPath": "assets/tabbar/cart-active.png"
      },
      {
        "pagePath": "pages/mine/mine",
        "text": "我的",
        "iconPath": "assets/tabbar/mine.png",
        "selectedIconPath": "assets/tabbar/mine-active.png"
      }
    ]
  }
}

// TabBar页面配置
Page({
  onTabItemTap(item) {
    console.log('Tab点击:', item.index);
    console.log('Tab路径:', item.pagePath);
    console.log('Tab文字:', item.text);
  }
});

// 切换TabBar
wx.switchTab({
  url: '/pages/mine/mine'
});
`;

console.log('\n=== TabBar配置 ===');
console.log(tabBarConfig);

// 5. 路由拦截
const routingIntercept = `
// 1. 登录拦截
function navigateToWithAuth(url) {
  const token = wx.getStorageSync('token');
  if (!token) {
    wx.showModal({
      title: '提示',
      content: '请先登录',
      success(res) {
        if (res.confirm) {
          wx.navigateTo({ url: '/pages/login/login' });
        }
      }
    });
    return;
  }
  wx.navigateTo({ url });
}

// 使用
navigateToWithAuth('/pages/order/order');

// 2. 封装路由工具
// utils/router.js
function navigate(url, params = {}) {
  const queryString = Object.keys(params)
    .map(key => \`\${key}=\${encodeURIComponent(params[key])}\`)
    .join('&');
  const fullUrl = queryString ? \`\${url}?\${queryString}\` : url;
  wx.navigateTo({ url: fullUrl });
}

function redirect(url, params = {}) {
  const queryString = Object.keys(params)
    .map(key => \`\${key}=\${encodeURIComponent(params[key])}\`)
    .join('&');
  const fullUrl = queryString ? \`\${url}?\${queryString}\` : url;
  wx.redirectTo({ url: fullUrl });
}

function back(delta = 1) {
  wx.navigateBack({ delta });
}

function switchTab(url) {
  wx.switchTab({ url });
}

function reLaunch(url, params = {}) {
  const queryString = Object.keys(params)
    .map(key => \`\${key}=\${encodeURIComponent(params[key])}\`)
    .join('&');
  const fullUrl = queryString ? \`\${url}?\${queryString}\` : url;
  wx.reLaunch({ url: fullUrl });
}

module.exports = {
  navigate,
  redirect,
  back,
  switchTab,
  reLaunch
};

// 使用
const router = require('@/utils/router');

router.navigate('/pages/detail/detail', { id: 1 });
router.back();
`;

console.log('\n=== 路由拦截 ===');
console.log(routingIntercept);

console.log('=== 微信小程序路由 ===');
