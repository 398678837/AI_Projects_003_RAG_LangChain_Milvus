// 微信小程序页面生命周期示例代码

// 1. 应用生命周期
const appLifecycle = `
// app.js
App({
  onLaunch(options) {
    console.log('=== 应用启动 onLaunch ===');
    console.log('启动参数:', options);
    
    // 初始化数据
    this.initData();
    
    // 获取用户信息
    this.getUserInfo();
  },
  
  onShow(options) {
    console.log('=== 应用显示 onShow ===');
    console.log('场景值:', options.scene);
    
    // 应用从后台进入前台时触发
    this.checkUpdate();
  },
  
  onHide() {
    console.log('=== 应用隐藏 onHide ===');
    
    // 应用从前台进入后台时触发
    this.saveData();
  },
  
  onError(error) {
    console.error('=== 应用错误 onError ===');
    console.error('错误信息:', error);
    
    // 上报错误
    this.reportError(error);
  },
  
  onPageNotFound(options) {
    console.log('=== 页面不存在 onPageNotFound ===');
    console.log('路径:', options.path);
    
    // 跳转到首页
    wx.redirectTo({
      url: '/pages/index/index'
    });
  },
  
  globalData: {
    userInfo: null,
    token: null
  },
  
  initData() {
    console.log('初始化数据');
  },
  
  getUserInfo() {
    const userInfo = wx.getStorageSync('userInfo');
    if (userInfo) {
      this.globalData.userInfo = userInfo;
    }
  },
  
  checkUpdate() {
    console.log('检查更新');
  },
  
  saveData() {
    console.log('保存数据');
  },
  
  reportError(error) {
    console.log('上报错误:', error);
  }
});
`;

console.log('=== 应用生命周期 ===');
console.log(appLifecycle);

// 2. 页面生命周期
const pageLifecycle = `
// pages/index/index.js
Page({
  data: {
    message: 'Hello',
    list: []
  },
  
  onLoad(options) {
    console.log('=== 页面加载 onLoad ===');
    console.log('页面参数:', options);
    
    // 页面加载时触发，只触发一次
    // 适合：获取页面参数、初始化数据
    this.initPage(options);
    this.fetchData();
  },
  
  onShow() {
    console.log('=== 页面显示 onShow ===');
    
    // 页面显示时触发，每次显示都会触发
    // 适合：刷新数据、恢复状态
    this.refreshData();
  },
  
  onReady() {
    console.log('=== 页面渲染完成 onReady ===');
    
    // 页面初次渲染完成时触发，只触发一次
    // 适合：获取DOM节点、动画初始化
    this.initAnimation();
  },
  
  onHide() {
    console.log('=== 页面隐藏 onHide ===');
    
    // 页面隐藏时触发
    // 适合：暂停动画、保存状态
    this.pauseAnimation();
    this.saveState();
  },
  
  onUnload() {
    console.log('=== 页面卸载 onUnload ===');
    
    // 页面卸载时触发
    // 适合：清理定时器、取消请求
    this.clearTimer();
    this.cancelRequest();
  },
  
  onPullDownRefresh() {
    console.log('=== 下拉刷新 onPullDownRefresh ===');
    
    // 下拉刷新时触发
    // 适合：刷新列表数据
    this.refreshList();
    
    // 停止下拉刷新
    setTimeout(() => {
      wx.stopPullDownRefresh();
    }, 1000);
  },
  
  onReachBottom() {
    console.log('=== 触底加载 onReachBottom ===');
    
    // 页面滚动到底部时触发
    // 适合：加载更多数据
    this.loadMore();
  },
  
  onPageScroll(options) {
    console.log('=== 页面滚动 onPageScroll ===');
    console.log('滚动距离:', options.scrollTop);
    
    // 页面滚动时触发
    // 适合：滚动动画、导航栏变化
    this.handleScroll(options.scrollTop);
  },
  
  onShareAppMessage() {
    console.log('=== 分享 onShareAppMessage ===');
    
    // 用户点击分享时触发
    return {
      title: '分享标题',
      path: '/pages/index/index',
      imageUrl: 'https://example.com/share.jpg'
    };
  },
  
  onShareTimeline() {
    console.log('=== 分享到朋友圈 onShareTimeline ===');
    
    // 用户分享到朋友圈时触发
    return {
      title: '分享标题',
      imageUrl: 'https://example.com/share.jpg'
    };
  },
  
  onResize(options) {
    console.log('=== 尺寸变化 onResize ===');
    console.log('窗口尺寸:', options.size);
    
    // 屏幕旋转时触发
    this.handleResize(options.size);
  },
  
  onTabItemTap(options) {
    console.log('=== Tab点击 onTabItemTap ===');
    console.log('点击的Tab:', options.index);
    
    // 点击Tab时触发（仅TabBar页面）
    this.handleTabClick(options.index);
  },
  
  initPage(options) {
    console.log('初始化页面，参数:', options);
  },
  
  fetchData() {
    console.log('获取数据');
  },
  
  refreshData() {
    console.log('刷新数据');
  },
  
  initAnimation() {
    console.log('初始化动画');
  },
  
  pauseAnimation() {
    console.log('暂停动画');
  },
  
  saveState() {
    console.log('保存状态');
  },
  
  clearTimer() {
    console.log('清除定时器');
  },
  
  cancelRequest() {
    console.log('取消请求');
  },
  
  refreshList() {
    console.log('刷新列表');
  },
  
  loadMore() {
    console.log('加载更多');
  },
  
  handleScroll(scrollTop) {
    console.log('处理滚动，距离:', scrollTop);
  },
  
  handleResize(size) {
    console.log('处理尺寸变化:', size);
  },
  
  handleTabClick(index) {
    console.log('处理Tab点击:', index);
  }
});
`;

console.log('\n=== 页面生命周期 ===');
console.log(pageLifecycle);

// 3. 生命周期触发顺序
const lifecycleOrder = `
// 应用启动 → 页面加载
App.onLaunch()
  → App.onShow()
    → Page.onLoad()
      → Page.onShow()
        → Page.onReady()

// 页面跳转（navigateTo）
当前页面: Page.onHide()
  → 新页面: Page.onLoad()
    → Page.onShow()
      → Page.onReady()

// 页面返回（navigateBack）
当前页面: Page.onUnload()
  → 上一页: Page.onShow()

// 应用切换到后台
App.onHide()
  → 所有页面: Page.onHide()

// 应用从后台切换到前台
App.onShow()
  → 当前页面: Page.onShow()

// 页面重定向（redirectTo）
当前页面: Page.onUnload()
  → 新页面: Page.onLoad()
    → Page.onShow()
      → Page.onReady()

// 页面重启（reLaunch）
所有页面: Page.onUnload()
  → 新页面: Page.onLoad()
    → Page.onShow()
      → Page.onReady()
`;

console.log('\n=== 生命周期触发顺序 ===');
console.log(lifecycleOrder);

// 4. 页面配置
const pageConfig = `
// pages/index/index.json
{
  "navigationBarTitleText": "首页",
  "navigationBarBackgroundColor": "#07c160",
  "navigationBarTextStyle": "white",
  "backgroundColor": "#f5f5f5",
  "enablePullDownRefresh": true,
  "onReachBottomDistance": 50,
  "disableScroll": false
}

// 配置项说明：
// - navigationBarTitleText: 导航栏标题
// - navigationBarBackgroundColor: 导航栏背景色
// - navigationBarTextStyle: 导航栏标题颜色（white/black）
// - backgroundColor: 页面背景色
// - enablePullDownRefresh: 是否开启下拉刷新
// - onReachBottomDistance: 触底距离
// - disableScroll: 是否禁止滚动
`;

console.log('\n=== 页面配置 ===');
console.log(pageConfig);

console.log('=== 微信小程序页面生命周期 ===');
