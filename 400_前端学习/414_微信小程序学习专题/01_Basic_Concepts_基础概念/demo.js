// 微信小程序基础概念示例代码

// 1. app.js - 小程序入口文件
const appJs = `
// app.js
App({
  onLaunch() {
    console.log('小程序启动');
    this.getUserInfo();
  },
  
  onShow() {
    console.log('小程序显示');
  },
  
  onHide() {
    console.log('小程序隐藏');
  },
  
  onError(error) {
    console.error('小程序错误:', error);
  },
  
  globalData: {
    userInfo: null,
    token: null
  },
  
  getUserInfo() {
    const userInfo = wx.getStorageSync('userInfo');
    if (userInfo) {
      this.globalData.userInfo = userInfo;
    }
  }
});
`;

console.log('=== app.js - 小程序入口文件 ===');
console.log(appJs);

// 2. app.json - 全局配置
const appJson = `
// app.json
{
  "pages": [
    "pages/index/index",
    "pages/about/about",
    "pages/detail/detail"
  ],
  "window": {
    "backgroundTextStyle": "light",
    "navigationBarBackgroundColor": "#07c160",
    "navigationBarTitleText": "我的小程序",
    "navigationBarTextStyle": "white",
    "backgroundColor": "#f5f5f5"
  },
  "tabBar": {
    "color": "#666666",
    "selectedColor": "#07c160",
    "backgroundColor": "#ffffff",
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
        "pagePath": "pages/mine/mine",
        "text": "我的",
        "iconPath": "assets/tabbar/mine.png",
        "selectedIconPath": "assets/tabbar/mine-active.png"
      }
    ]
  },
  "style": "v2",
  "sitemapLocation": "sitemap.json"
}
`;

console.log('\n=== app.json - 全局配置 ===');
console.log(appJson);

// 3. app.wxss - 全局样式
const appWxss = `
/* app.wxss */
page {
  background-color: #f5f5f5;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
}

.container {
  padding: 20rpx;
}

.text-primary {
  color: #07c160;
}

.text-secondary {
  color: #999999;
}

.btn-primary {
  background-color: #07c160;
  color: #ffffff;
  border-radius: 8rpx;
}

.btn-secondary {
  background-color: #ffffff;
  color: #333333;
  border: 1rpx solid #e5e5e5;
  border-radius: 8rpx;
}
`;

console.log('\n=== app.wxss - 全局样式 ===');
console.log(appWxss);

// 4. 页面结构示例
const pageStructure = `
// pages/index/
├── index.js        // 页面逻辑
├── index.json      // 页面配置
├── index.wxml      // 页面结构
└── index.wxss      // 页面样式
`;

console.log('\n=== 页面结构示例 ===');
console.log(pageStructure);

// 5. 简单的页面代码示例
const simplePage = `
// pages/index/index.js
Page({
  data: {
    message: 'Hello 小程序!',
    count: 0
  },
  
  onLoad(options) {
    console.log('页面加载', options);
  },
  
  onShow() {
    console.log('页面显示');
  },
  
  onReady() {
    console.log('页面渲染完成');
  },
  
  onHide() {
    console.log('页面隐藏');
  },
  
  onUnload() {
    console.log('页面卸载');
  },
  
  handleTap() {
    this.setData({
      count: this.data.count + 1
    });
  }
});

// pages/index/index.wxml
<view class="container">
  <text>{{ message }}</text>
  <view>
    <text>计数: {{ count }}</text>
    <button bindtap="handleTap">点击+1</button>
  </view>
</view>

// pages/index/index.wxss
.container {
  text-align: center;
  padding-top: 200rpx;
}

// pages/index/index.json
{
  "navigationBarTitleText": "首页"
}
`;

console.log('\n=== 简单的页面代码示例 ===');
console.log(simplePage);

console.log('=== 微信小程序基础概念 ===');
