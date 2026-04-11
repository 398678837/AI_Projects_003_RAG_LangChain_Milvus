// 移动端开发基础概念示例代码

// 1. 移动端开发方式对比
const developmentComparison = `
// 原生开发 vs 混合开发 vs 跨平台开发对比

// 原生开发 (Native Development)
const nativeDev = {
  iOS: {
    language: ['Swift',
    tools: ['Xcode', 'SwiftUI', 'UIKit'],
    pros: [
      '性能最佳',
      '体验最好',
      '可访问全部原生API',
      'App Store支持最好'
    ],
    cons: [
      '需要学习新语言',
      '开发成本高',
      '维护两套代码'
    ]
  },
  Android: {
    language: ['Kotlin', 'Java'],
    tools: ['Android Studio', 'Jetpack Compose'],
    pros: [
      '性能最佳',
      '体验最好',
      '可访问全部原生API',
      'Google Play支持'
    ],
    cons: [
      '需要学习新语言',
      '开发成本高',
      '维护两套代码'
    ]
  }
};

// 混合开发 (Hybrid Development)
const hybridDev = {
  frameworks: ['Cordova', 'Ionic', 'Capacitor'],
  language: ['HTML', 'CSS', 'JavaScript'],
  pros: [
    '开发速度快',
    '一套代码多端运行',
    'Web技术栈',
    '成本低'
  ],
  cons: [
    '性能一般',
    '体验不如原生',
    '部分原生API受限'
  ]
};

// 跨平台开发 (Cross-Platform Development)
const crossPlatformDev = {
  ReactNative: {
    language: ['JavaScript', 'TypeScript'],
    framework: 'React Native',
    pros: [
      '性能接近原生',
      '一套代码多端运行',
      'React生态',
      '热更新'
    ],
    cons: [
      '部分功能需原生开发',
      '需要学习React'
    ]
  },
  Flutter: {
    language: ['Dart'],
    framework: 'Flutter',
    pros: [
      '性能最佳',
      'UI一致性好',
      '热重载',
      '开发效率高'
    ],
    cons: [
      '需要学习Dart',
      '包体积较大'
    ]
  },
  UniApp: {
    language: ['Vue.js'],
    framework: 'uni-app',
    pros: [
      'Vue技术栈',
      '多端发布',
      '生态丰富'
    ],
    cons: [
      '部分平台受限'
    ]
  }
};

console.log('=== 开发方式对比');
console.log('原生开发:', nativeDev);
console.log('混合开发:', hybridDev);
console.log('跨平台开发:', crossPlatformDev);
`;

console.log('=== 移动端开发方式对比 ===');
console.log(developmentComparison);

// 2. 技术选型指南
const techSelectionGuide = `
// 技术选型决策树

function chooseTechStack(requirements) {
  const { 
    performance, 
    budget, 
    timeline, 
    teamSkills,
    platforms
  } = requirements;

  if (performance === '极致' && platforms === '单一') {
    return '原生开发';
  }

  if (teamSkills.includes('React') && performance === '良好') {
    return 'React Native';
  }

  if (teamSkills.includes('Vue')) {
    return 'uni-app / Flutter';
  }

  if (budget === '低' && timeline === '短') {
    return '混合开发 (Ionic/Capacitor)';
  }

  if (performance === '最佳' && platforms === '多端') {
    return 'Flutter';
  }

  return '根据具体需求具体分析';
}

// 示例1：电商App，需要最佳性能，团队熟悉Vue
const requirements1 = {
  performance: '最佳',
  budget: '中',
  timeline: '中',
  teamSkills: ['Vue', 'JavaScript'],
  platforms: '多端'
};
console.log('电商App推荐:', chooseTechStack(requirements1));

// 示例2：快速原型，预算低，时间紧
const requirements2 = {
  performance: '一般',
  budget: '低',
  timeline: '短',
  teamSkills: ['HTML', 'CSS', 'JavaScript'],
  platforms: '多端'
};
console.log('快速原型推荐:', chooseTechStack(requirements2));
`;

console.log('\n=== 技术选型指南 ===');
console.log(techSelectionGuide);

// 3. 移动端特点
const mobileFeatures = `
// 移动端设备特点

const mobileDeviceFeatures = {
  screen: {
    sizes: ['小屏', '中屏', '大屏', '折叠屏'],
    orientations: ['竖屏', '横屏'],
    densities: ['ldpi', 'mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']
  },
  input: {
    types: ['触摸', '手势', '语音', '笔'],
    gestures: ['点击', '滑动', '捏合', '拖拽', '旋转']
  },
  sensors: {
    types: ['GPS', '陀螺仪', '加速度计', '指南针', '光线传感器', '距离传感器']
  },
  connectivity: {
    types: ['WiFi', '4G', '5G', 'Bluetooth', 'NFC'],
    states: ['在线', '离线', '弱网']
  },
  storage: {
    types: ['内置存储', 'SD卡'],
    limitations: ['空间限制', '性能差异']
  },
  power: {
    states: ['充电中', '电池中', '低电量'],
    optimizations: ['省电模式', '性能模式']
  }
};

// 移动端设计原则
const mobileDesignPrinciples = [
  '简洁至上',
  '触摸友好',
  '快速响应',
  '离线可用',
  '省电优化',
  '流量优化',
  '安全第一',
  '适配多样'
];

console.log('=== 移动端特点 ===');
console.log('设备特点:', mobileDeviceFeatures);
console.log('设计原则:', mobileDesignPrinciples);
`;

console.log('\n=== 移动端特点 ===');
console.log(mobileFeatures);

// 4. 响应式设计基础
const responsiveDesign = `
// 响应式设计基础

// CSS媒体查询
const mediaQueries = \`
/* 小屏幕手机 */
@media (max-width: 480px) {
  .container {
    padding: 10px;
  }
}

/* 中等屏幕手机 */
@media (min-width: 481px) and (max-width: 768px) {
  .container {
    padding: 15px;
  }
}

/* 平板 */
@media (min-width: 769px) and (max-width: 1024px) {
  .container {
    padding: 20px;
  }
}

/* 横屏 */
@media (orientation: landscape) {
  .sidebar {
    display: block;
  }
}

/* 竖屏 */
@media (orientation: portrait) {
  .sidebar {
    display: none;
  }
}

/* 高DPI屏幕 */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .image {
    background-image: url('image@2x.png');
  }
}
\`;

// 视口设置
const viewportMeta = \`
<meta name="viewport" content="
  width=device-width,
  initial-scale=1.0,
  maximum-scale=1.0,
  user-scalable=no
">
\`;

// 触摸事件
const touchEvents = \`
// JavaScript触摸事件
const touchEventsDemo = \`
// 触摸开始
element.addEventListener('touchstart', (e) => {
  console.log('触摸开始', e.touches);
});

// 触摸移动
element.addEventListener('touchmove', (e) => {
  e.preventDefault();
  console.log('触摸移动', e.touches);
});

// 触摸结束
element.addEventListener('touchend', (e) => {
  console.log('触摸结束', e.changedTouches);
});

// 触摸取消
element.addEventListener('touchcancel', (e) => {
  console.log('触摸取消');
});

// 手势事件库（如Hammer.js）
const hammer = new Hammer(element);
hammer.on('swipeleft', () => {
  console.log('左滑');
});
hammer.on('swiperight', () => {
  console.log('右滑');
});
hammer.on('pinch', () => {
  console.log('捏合');
});
\`;
\`;

console.log('=== 响应式设计基础 ===');
console.log('媒体查询:', mediaQueries);
console.log('视口设置:', viewportMeta);
console.log('触摸事件:', touchEvents);
`;

console.log('\n=== 响应式设计基础 ===');
console.log(responsiveDesign);

// 5. 移动端开发环境准备清单
const devEnvironmentChecklist = `
// 移动端开发环境检查清单

const checklists = {
  iOS: [
    '安装Xcode',
    '注册Apple Developer账号',
    '配置开发证书',
    '配置Provisioning Profile',
    '准备测试设备',
    '学习Swift/SwiftUI'
  ],
  Android: [
    '安装Android Studio',
    '配置Android SDK',
    '创建虚拟设备',
    '准备测试设备',
    '学习Kotlin',
    '注册Google Play开发者账号'
  ],
  ReactNative: [
    '安装Node.js',
    '安装React Native CLI',
    '配置Android开发环境',
    '配置iOS开发环境',
    '学习React'
  ],
  Flutter: [
    '安装Flutter SDK',
    '配置Android开发环境',
    '配置iOS开发环境',
    '学习Dart'
  ],
  uniApp: [
    '安装HBuilderX',
    '安装微信开发者工具',
    '学习Vue.js'
  ]
};

// 快速开始模板
const quickStartTemplates = {
  ReactNative: \`
# 创建React Native项目
npx react-native init MyApp
cd MyApp
npm run android  # 运行Android
npm run ios    # 运行iOS
\`,
  Flutter: \`
# 创建Flutter项目
flutter create my_app
cd my_app
flutter run       # 运行
\`,
  uniApp: \`
# 使用HBuilderX创建项目
# 或使用Vue CLI
vue create -p dcloudio/uni-preset-vue my-project
\`
};

console.log('=== 开发环境检查清单 ===');
console.log('检查清单:', checklists);
console.log('快速开始:', quickStartTemplates);
`;

console.log('\n=== 开发环境准备 ===');
console.log(devEnvironmentChecklist);

console.log('\n🎉 移动端开发基础概念学习完成！');
console.log('💡 记住：根据需求选择合适的技术栈！');
console.log('🚀 现在你已经了解移动端开发的基础了！');
`;

console.log('\n=== 移动端开发基础概念 ===');
