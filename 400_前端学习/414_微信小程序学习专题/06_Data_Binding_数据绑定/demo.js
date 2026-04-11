// 微信小程序数据绑定示例代码

// 1. 基本数据绑定
const basicBinding = `
// JS
Page({
  data: {
    message: 'Hello 小程序',
    count: 0,
    isShow: true,
    userName: '张三',
    avatar: 'https://example.com/avatar.jpg'
  }
});

// WXML - 文本绑定
<view>{{ message }}</view>
<view>计数: {{ count }}</view>

// WXML - 属性绑定
<image src="{{ avatar }}" />
<view class="item {{ isShow ? 'show' : 'hide' }}">
  {{ userName }}
</view>

// WXML - 控制属性绑定
<view wx:if="{{ isShow }}">显示内容</view>
<view hidden="{{ !isShow }}">隐藏内容</view>
<button disabled="{{ count === 0 }}">按钮</button>

// WXML - 样式绑定
<view style="color: {{ isShow ? 'red' : 'blue' }}">
  动态颜色
</view>

// WXML - 数据运算
<view>{{ count + 1 }}</view>
<view>{{ count > 10 ? '大于10' : '小于等于10' }}</view>
<view>{{ message.toUpperCase() }}</view>
`;

console.log('=== 基本数据绑定 ===');
console.log(basicBinding);

// 2. setData使用
const setDataUsage = `
// JS
Page({
  data: {
    text: '原始文本',
    number: 10,
    array: [1, 2, 3],
    object: {
      name: '张三',
      age: 18
    }
  },
  
  // 修改基本类型
  updateText() {
    this.setData({
      text: '新的文本'
    });
  },
  
  updateNumber() {
    this.setData({
      number: this.data.number + 1
    });
  },
  
  // 修改数组
  updateArray() {
    this.setData({
      'array[1]': 99
    });
  },
  
  appendArray() {
    const newArray = [...this.data.array, 4, 5];
    this.setData({
      array: newArray
    });
  },
  
  // 修改对象
  updateObject() {
    this.setData({
      'object.age': 20
    });
  },
  
  replaceObject() {
    this.setData({
      object: {
        name: '李四',
        age: 25
      }
    });
  },
  
  // 批量更新
  batchUpdate() {
    this.setData({
      text: '批量更新',
      number: 100,
      'object.name': '王五'
    });
  },
  
  // 使用回调
  updateWithCallback() {
    this.setData(
      { text: '带回调的更新' },
      () => {
        console.log('更新完成，新值:', this.data.text);
      }
    );
  }
});
`;

console.log('\n=== setData使用 ===');
console.log(setDataUsage);

// 3. 双向绑定
const twoWayBinding = `
// JS
Page({
  data: {
    username: '',
    password: '',
    agree: false,
    volume: 50,
    gender: 'male'
  }
});

// WXML - 输入框双向绑定
<input 
  model:value="{{ username }}" 
  placeholder="请输入用户名" 
/>
<view>用户名: {{ username }}</view>

// WXML - 密码框
<input 
  model:value="{{ password }}" 
  type="password" 
  placeholder="请输入密码" 
/>

// WXML - 开关
<switch model:checked="{{ agree }}" />
<view>同意协议: {{ agree }}</view>

// WXML - 滑块
<slider model:value="{{ volume }}" min="0" max="100" />
<view>音量: {{ volume }}</view>

// WXML - 单选框（需要手动处理）
<radio-group bindchange="handleGenderChange">
  <radio value="male" checked="{{ gender === 'male' }}">男</radio>
  <radio value="female" checked="{{ gender === 'female' }}">女</radio>
</radio-group>

// JS - 单选框处理
Page({
  data: {
    gender: 'male'
  },
  handleGenderChange(e) {
    this.setData({
      gender: e.detail.value
    });
  }
});
`;

console.log('\n=== 双向绑定 ===');
console.log(twoWayBinding);

// 4. 列表渲染
const listRendering = `
// JS
Page({
  data: {
    list: [
      { id: 1, name: '张三', age: 20 },
      { id: 2, name: '李四', age: 22 },
      { id: 3, name: '王五', age: 18 }
    ],
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

// WXML - 基本列表
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
<view wx:for="{{ categories }}" wx:key="name">
  <view class="category">{{ item.name }}</view>
  <view 
    wx:for="{{ item.items }}" 
    wx:for-item="subItem"
    wx:key="*this"
    class="item"
  >
    {{ subItem }}
  </view>
</view>

// WXML - block标签（不渲染DOM）
<block wx:for="{{ list }}" wx:key="id">
  <view>{{ item.name }}</view>
  <view>{{ item.age }}</view>
</block>
`;

console.log('\n=== 列表渲染 ===');
console.log(listRendering);

// 5. 条件渲染
const conditionalRendering = `
// JS
Page({
  data: {
    isLogin: false,
    userType: 'admin',
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
  管理员
</view>
<view wx:elif="{{ userType === 'user' }}">
  普通用户
</view>
<view wx:else>
  访客
</view>

// WXML - hidden
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

// 6. setData性能优化
const performance = `
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
    user: { name: '张三', age: 18 },
    list: [1, 2, 3]
  },
  updateUser() {
    this.setData({
      'user.age': 20  // 只更新age字段
    });
  }
});

// ✅ 正确做法 - 使用setData回调
Page({
  data: { list: [] },
  fetchData() {
    this.setData({ loading: true }, () => {
      console.log('loading状态已更新');
    });
  }
});

// ✅ 正确做法 - 大数据列表使用虚拟滚动
// 使用虚拟滚动库或自定义实现，只渲染可视区域
`;

console.log('\n=== setData性能优化 ===');
console.log(performance);

console.log('=== 微信小程序数据绑定 ===');
