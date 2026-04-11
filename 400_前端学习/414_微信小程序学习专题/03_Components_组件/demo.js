// 微信小程序组件示例代码

// 1. 基础组件
const basicComponents = `
<!-- view 组件 - 类似div -->
<view class="container">
  <view>我是一个view</view>
  
  <!-- text 组件 - 类似span -->
  <text>我是一段文本</text>
  
  <!-- image 组件 -->
  <image 
    src="https://example.com/image.jpg" 
    mode="aspectFill"
    lazy-load
  />
  
  <!-- button 组件 -->
  <button type="primary">主要按钮</button>
  <button type="default">默认按钮</button>
  <button size="mini">小按钮</button>
  <button plain>镂空按钮</button>
  <button disabled>禁用按钮</button>
  <button loading>加载中...</button>
  
  <!-- input 组件 -->
  <input placeholder="请输入内容" />
  <input type="number" placeholder="请输入数字" />
  <input type="password" placeholder="请输入密码" />
  <input disabled placeholder="禁用输入框" />
  
  <!-- textarea 组件 -->
  <textarea placeholder="请输入多行内容" maxlength="200" />
</view>
`;

console.log('=== 基础组件 ===');
console.log(basicComponents);

// 2. 表单组件
const formComponents = `
<!-- 表单组件 -->
<form bindsubmit="handleSubmit" bindreset="handleReset">
  
  <!-- input -->
  <view class="form-item">
    <text>用户名</text>
    <input name="username" placeholder="请输入用户名" />
  </view>
  
  <!-- textarea -->
  <view class="form-item">
    <text>简介</text>
    <textarea name="bio" placeholder="请输入简介" />
  </view>
  
  <!-- radio - 单选 -->
  <view class="form-item">
    <text>性别</text>
    <radio-group name="gender">
      <radio value="male" checked>男</radio>
      <radio value="female">女</radio>
    </radio-group>
  </view>
  
  <!-- checkbox - 多选 -->
  <view class="form-item">
    <text>爱好</text>
    <checkbox-group name="hobbies">
      <checkbox value="reading">阅读</checkbox>
      <checkbox value="music">音乐</checkbox>
      <checkbox value="sports">运动</checkbox>
    </checkbox-group>
  </view>
  
  <!-- switch - 开关 -->
  <view class="form-item">
    <text>记住我</text>
    <switch name="remember" />
  </view>
  
  <!-- slider - 滑块 -->
  <view class="form-item">
    <text>音量</text>
    <slider name="volume" min="0" max="100" value="50" />
  </view>
  
  <!-- picker - 选择器 -->
  <view class="form-item">
    <text>城市</text>
    <picker 
      mode="selector" 
      range="{{ cities }}" 
      bindchange="handleCityChange"
    >
      <view>{{ selectedCity || '请选择城市' }}</view>
    </picker>
  </view>
  
  <!-- 日期选择器 -->
  <view class="form-item">
    <text>日期</text>
    <picker 
      mode="date" 
      bindchange="handleDateChange"
    >
      <view>{{ selectedDate || '请选择日期' }}</view>
    </picker>
  </view>
  
  <button form-type="submit">提交</button>
  <button form-type="reset">重置</button>
</form>

// JS
Page({
  data: {
    cities: ['北京', '上海', '广州', '深圳'],
    selectedCity: '',
    selectedDate: ''
  },
  
  handleSubmit(e) {
    console.log('表单数据:', e.detail.value);
  },
  
  handleReset() {
    console.log('表单重置');
  },
  
  handleCityChange(e) {
    this.setData({
      selectedCity: this.data.cities[e.detail.value]
    });
  },
  
  handleDateChange(e) {
    this.setData({
      selectedDate: e.detail.value
    });
  }
});
`;

console.log('\n=== 表单组件 ===');
console.log(formComponents);

// 3. 导航和媒体组件
const navigationMedia = `
<!-- navigator - 页面导航 -->
<navigator url="/pages/detail/detail?id=1">跳转到详情页</navigator>
<navigator url="/pages/about/about" open-type="redirect">重定向</navigator>
<navigator open-type="switchTab" url="/pages/mine/mine">切换Tab</navigator>
<navigator open-type="navigateBack">返回上一页</navigator>

<!-- scroll-view - 滚动视图 -->
<scroll-view scroll-y style="height: 500rpx;">
  <view wx:for="{{ list }}" wx:key="id">
    {{ item.name }}
  </view>
</scroll-view>

<!-- swiper - 轮播图 -->
<swiper 
  indicator-dots 
  autoplay 
  interval="3000" 
  duration="500"
  circular
>
  <swiper-item wx:for="{{ banners }}" wx:key="id">
    <image src="{{ item.image }}" mode="aspectFill" />
  </swiper-item>
</swiper>

<!-- video - 视频 -->
<video 
  src="https://example.com/video.mp4" 
  controls 
  autoplay
  poster="https://example.com/poster.jpg"
/>

<!-- camera - 相机 -->
<camera 
  device-position="back" 
  flash="auto"
  binderror="handleCameraError"
>
  <cover-view class="camera-controls">
    <cover-button bindtap="takePhoto">拍照</cover-button>
  </cover-view>
</camera>

<!-- map - 地图 -->
<map 
  longitude="113.324520" 
  latitude="23.099994" 
  scale="14"
  markers="{{ markers }}"
/>
`;

console.log('\n=== 导航和媒体组件 ===');
console.log(navigationMedia);

// 4. 自定义组件
const customComponents = `
// 1. 创建组件 - components/my-button/
// components/my-button/my-button.js
Component({
  properties: {
    text: {
      type: String,
      value: '按钮'
    },
    type: {
      type: String,
      value: 'primary'
    },
    disabled: {
      type: Boolean,
      value: false
    }
  },
  
  data: {
    isPressed: false
  },
  
  methods: {
    handleTap() {
      if (this.properties.disabled) return;
      
      this.triggerEvent('tap', {
        time: Date.now()
      });
    }
  }
});

// components/my-button/my-button.wxml
<view 
  class="custom-button custom-button-{{ type }}"
  bindtap="handleTap"
>
  <text>{{ text }}</text>
</view>

// components/my-button/my-button.wxss
.custom-button {
  padding: 20rpx 40rpx;
  border-radius: 8rpx;
  text-align: center;
}

.custom-button-primary {
  background: #07c160;
  color: white;
}

.custom-button-default {
  background: white;
  color: #333;
  border: 1rpx solid #e5e5e5;
}

// 2. 使用组件
// pages/index/index.json
{
  "usingComponents": {
    "my-button": "/components/my-button/my-button"
  }
}

// pages/index/index.wxml
<view>
  <my-button text="自定义按钮" bind:tap="handleButtonTap" />
  <my-button text="默认按钮" type="default" />
  <my-button text="禁用按钮" disabled />
</view>

// pages/index/index.js
Page({
  handleButtonTap(e) {
    console.log('按钮被点击', e.detail);
  }
});
`;

console.log('\n=== 自定义组件 ===');
console.log(customComponents);

// 5. 组件通信
const componentCommunication = `
// 1. 父传子 - properties
// 子组件
Component({
  properties: {
    title: String,
    count: {
      type: Number,
      value: 0
    },
    user: Object
  }
});

// 父组件使用
<my-component 
  title="标题" 
  count="{{ 10 }}" 
  user="{{ user }}" 
/>

// 2. 子传父 - triggerEvent
// 子组件
Component({
  methods: {
    sendToParent() {
      this.triggerEvent('myevent', {
        message: '来自子组件的消息',
        data: { id: 1, name: 'test' }
      });
    }
  }
});

// 父组件接收
<my-component bind:myevent="handleMyEvent" />

Page({
  handleMyEvent(e) {
    console.log(e.detail.message);
    console.log(e.detail.data);
  }
});

// 3. 获取组件实例 - selectComponent
// 父组件
Page({
  getChild() {
    const child = this.selectComponent('#myComponent');
    child.someMethod();
  }
});

<my-component id="myComponent" />
`;

console.log('\n=== 组件通信 ===');
console.log(componentCommunication);

console.log('=== 微信小程序组件 ===');
