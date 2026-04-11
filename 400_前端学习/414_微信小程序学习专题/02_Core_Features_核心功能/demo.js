// 微信小程序核心功能示例代码

// 1. 事件处理
const eventHandling = `
// 页面JS
Page({
  data: {
    message: '点击按钮试试',
    count: 0
  },
  
  handleTap(e) {
    console.log('点击事件', e);
    this.setData({
      message: '按钮被点击了!',
      count: this.data.count + 1
    });
  },
  
  handleInput(e) {
    console.log('输入事件', e.detail.value);
    this.setData({
      inputValue: e.detail.value
    });
  },
  
  handleFormSubmit(e) {
    console.log('表单提交', e.detail.value);
    wx.showToast({
      title: '提交成功',
      icon: 'success'
    });
  },
  
  handleTouchStart(e) {
    console.log('触摸开始', e);
  },
  
  handleTouchMove(e) {
    console.log('触摸移动', e);
  },
  
  handleTouchEnd(e) {
    console.log('触摸结束', e);
  }
});

// 页面WXML
<view class="container">
  <view>{{ message }}</view>
  <view>计数: {{ count }}</view>
  
  <button bindtap="handleTap">点击我</button>
  
  <input 
    placeholder="请输入内容" 
    bindinput="handleInput" 
  />
  
  <form bindsubmit="handleFormSubmit">
    <input name="username" placeholder="用户名" />
    <button form-type="submit">提交</button>
  </form>
  
  <view 
    bindtouchstart="handleTouchStart"
    bindtouchmove="handleTouchMove"
    bindtouchend="handleTouchEnd"
    style="width: 200rpx; height: 200rpx; background: #07c160;"
  >
    触摸我
  </view>
</view>
`;

console.log('=== 事件处理 ===');
console.log(eventHandling);

// 2. setData使用
const setDataUsage = `
// setData使用示例
Page({
  data: {
    text: '原始文本',
    array: [1, 2, 3],
    object: {
      name: '张三',
      age: 18
    }
  },
  
  // 修改普通字段
  updateText() {
    this.setData({
      text: '新的文本'
    });
  },
  
  // 修改数组元素
  updateArrayItem() {
    this.setData({
      'array[1]': 99
    });
  },
  
  // 修改对象属性
  updateObjectProperty() {
    this.setData({
      'object.age': 20
    });
  },
  
  // 追加数组
  appendToArray() {
    const newArray = [...this.data.array, 4, 5];
    this.setData({
      array: newArray
    });
  },
  
  // 回调函数
  updateWithCallback() {
    this.setData(
      { text: '带回调的更新' },
      () => {
        console.log('更新完成');
      }
    );
  },
  
  // 注意：不要频繁调用setData
  // 推荐做法：合并多次更新
  updateAll() {
    this.setData({
      text: '合并更新',
      'object.age': 25
    });
  }
});

// WXML
<view>{{ text }}</view>
<view>{{ array }}</view>
<view>{{ object.name }} - {{ object.age }}</view>

<button bindtap="updateText">修改文本</button>
<button bindtap="updateArrayItem">修改数组</button>
<button bindtap="updateObjectProperty">修改对象</button>
<button bindtap="appendToArray">追加数组</button>
`;

console.log('\n=== setData使用 ===');
console.log(setDataUsage);

// 3. 数据双向绑定
const dataBinding = `
// 双向绑定示例
Page({
  data: {
    username: '',
    password: '',
    rememberMe: false,
    agree: false
  },
  
  handleSubmit() {
    console.log('用户名:', this.data.username);
    console.log('密码:', this.data.password);
    console.log('记住我:', this.data.rememberMe);
    console.log('同意协议:', this.data.agree);
  }
});

// WXML - 使用model:前缀实现双向绑定
<view class="form">
  <input 
    model:value="{{ username }}" 
    placeholder="请输入用户名" 
  />
  
  <input 
    model:value="{{ password }}" 
    type="password" 
    placeholder="请输入密码" 
  />
  
  <checkbox-group bindchange="handleAgree">
    <checkbox value="agree" checked="{{ agree }}">同意协议</checkbox>
  </checkbox-group>
  
  <switch model:checked="{{ rememberMe }}" />
  <text>记住我</text>
  
  <button bindtap="handleSubmit">提交</button>
</view>

// 注意：双向绑定在简单表单场景非常有用，但复杂场景仍需要手动处理
`;

console.log('\n=== 数据双向绑定 ===');
console.log(dataBinding);

// 4. 条件渲染
const conditionalRendering = `
// 条件渲染示例
Page({
  data: {
    isLogin: false,
    userType: 'admin', // admin, user, guest
    score: 85
  }
});

// WXML - wx:if
<view wx:if="{{ isLogin }}">
  <text>欢迎回来!</text>
</view>
<view wx:else>
  <text>请先登录</text>
</view>

// WXML - wx:elif
<view wx:if="{{ userType === 'admin' }}">
  <text>管理员</text>
</view>
<view wx:elif="{{ userType === 'user' }}">
  <text>普通用户</text>
</view>
<view wx:else>
  <text>访客</text>
</view>

// WXML - hidden (推荐使用，性能更好)
<view hidden="{{ !isLogin }}">
  只有登录才显示
</view>

// WXML - 多条件
<view>
  <view wx:if="{{ score >= 90 }}">优秀</view>
  <view wx:elif="{{ score >= 80 }}">良好</view>
  <view wx:elif="{{ score >= 60 }}">及格</view>
  <view wx:else>不及格</view>
</view>

// 区别：
// - wx:if: 真正的条件渲染，不满足条件时不渲染DOM
// - hidden: 只是控制显示/隐藏，始终在DOM中
// - 频繁切换用hidden，条件很少变化用wx:if
`;

console.log('\n=== 条件渲染 ===');
console.log(conditionalRendering);

// 5. 列表渲染
const listRendering = `
// 列表渲染示例
Page({
  data: {
    list: [
      { id: 1, name: '张三', age: 20 },
      { id: 2, name: '李四', age: 22 },
      { id: 3, name: '王五', age: 18 }
    ]
  }
});

// WXML - 基本列表渲染
<view wx:for="{{ list }}" wx:key="id">
  <view>索引: {{ index }}</view>
  <view>姓名: {{ item.name }}</view>
  <view>年龄: {{ item.age }}</view>
</view>

// WXML - 自定义变量名
<view 
  wx:for="{{ list }}" 
  wx:for-item="user" 
  wx:for-index="idx"
  wx:key="id"
>
  <view>索引: {{ idx }}</view>
  <view>姓名: {{ user.name }}</view>
  <view>年龄: {{ user.age }}</view>
</view>

// WXML - 多层列表
Page({
  data: {
    categories: [
      {
        name: '水果',
        items: ['苹果', '香蕉', '橙子']
      },
      {
        name: '蔬菜',
        items: ['白菜', '萝卜', '西红柿']
      }
    ]
  }
});

<view wx:for="{{ categories }}" wx:key="name">
  <view>{{ item.name }}</view>
  <view 
    wx:for="{{ item.items }}" 
    wx:for-item="subItem"
    wx:key="*this"
  >
    {{ subItem }}
  </view>
</view>
`;

console.log('\n=== 列表渲染 ===');
console.log(listRendering);

console.log('=== 微信小程序核心功能 ===');
