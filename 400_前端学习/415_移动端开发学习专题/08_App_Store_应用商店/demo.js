// 应用商店发布示例代码

// 1. 应用发布准备
const appPreparation = `
// 应用发布准备清单

const appPreparationChecklist = {
  // 开发者账号
  developerAccount: [
    '注册 Apple Developer Program ($99/年)',
    '注册 Google Play Developer ($25一次性)',
    '完善开发者信息',
    '配置税务和银行信息'
  ],
  
  // 应用信息
  appInfo: [
    '应用名称 (30字符以内)',
    '应用副标题 (App Store)',
    '应用描述 (4000字符以内)',
    '关键词 (100字符以内)',
    '应用分类',
    '年龄分级',
    '版权信息',
    '技术支持URL',
    '营销URL',
    '隐私政策URL'
  ],
  
  // 应用图标
  appIcon: {
    iOS: [
      '1024x1024 (App Store)',
      '180x180 (iPhone @3x)',
      '120x120 (iPhone @2x)',
      '167x167 (iPad Pro)',
      '152x152 (iPad)',
      '80x80 (Spotlight)',
      '58x58 (Settings)'
    ],
    Android: [
      '512x512 (Google Play)',
      '192x192 (xxxhdpi)',
      '144x144 (xxhdpi)',
      '96x96 (xhdpi)',
      '72x72 (hdpi)',
      '48x48 (mdpi)'
    ],
    requirements: [
      'PNG格式',
      '不包含透明通道',
      '不包含圆角',
      '不包含阴影'
    ]
  },
  
  // 应用截图
  screenshots: {
    iOS: [
      'iPhone 6.7" (1290x2796)',
      'iPhone 6.5" (1242x2688)',
      'iPhone 5.5" (1242x2208)',
      'iPad Pro 12.9" (2048x2732)',
      'iPad 11" (1668x2388)'
    ],
    Android: [
      '手机截图 (1080x1920)',
      '7寸平板截图',
      '10寸平板截图'
    ],
    requirements: [
      'JPG或PNG格式',
      '不包含状态栏',
      '不包含设备边框',
      '可以添加文字说明',
      '展示核心功能'
    ],
    count: '3-10张'
  },
  
  // 预览视频
  previewVideo: {
    iOS: [
      'MOV格式',
      '30fps',
      '15-30秒',
      '设备尺寸'
    ],
    Android: [
      'MP4格式',
      '1080p或4K',
      '30-60fps',
      '最长2分钟'
    ]
  }
};

console.log('=== 应用发布准备 ===');
console.log('检查清单:', appPreparationChecklist);
`;

console.log('=== 应用发布准备 ===');
console.log(appPreparation);

// 2. iOS App Store 发布
const iosAppStore = `
// iOS App Store 发布流程

// 2.1 Xcode 配置
const xcodeConfig = \`
// 1. 配置 Bundle Identifier
// Xcode -> Project -> General -> Bundle Identifier
// 格式: com.yourcompany.yourapp

// 2. 配置版本号和构建号
// Version: 1.0.0 (语义化版本)
// Build: 1 (每次提交递增)

// 3. 配置签名
// Xcode -> Project -> Signing & Capabilities
// 选择 Team
// 勾选 Automatically manage signing

// 4. 添加必要的权限
// Info.plist
<key>NSCameraUsageDescription</key>
<string>需要访问相机以拍照</string>

<key>NSPhotoLibraryUsageDescription</key>
<string>需要访问相册以选择照片</string>

<key>NSLocationWhenInUseUsageDescription</key>
<string>需要访问位置以提供附近服务</string>

// 5. 配置 App 图标和启动图
// Assets.xcassets -> AppIcon
// Assets.xcassets -> LaunchScreen
\`;

// 2.2 打包和上传
const buildAndUpload = \`
// 方法1: 使用 Xcode
1. Product -> Archive
2. 等待 Archive 完成
3. 在 Organizer 中选择 Archive
4. 点击 Distribute App
5. 选择 App Store Connect
6. 等待上传完成

// 方法2: 使用命令行
# 清理
xcodebuild clean -workspace MyApp.xcworkspace -scheme MyApp

# Archive
xcodebuild archive \\
  -workspace MyApp.xcworkspace \\
  -scheme MyApp \\
  -archivePath MyApp.xcarchive

# 导出
xcodebuild -exportArchive \\
  -archivePath MyApp.xcarchive \\
  -exportPath ./Export \\
  -exportOptionsPlist ExportOptions.plist

# ExportOptions.plist 示例
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>method</key>
    <string>app-store</string>
    <key>teamID</key>
    <string>YOUR_TEAM_ID</string>
</dict>
</plist>

# 上传到 App Store Connect
xcrun altool --upload-app \\
  --type ios \\
  --file MyApp.ipa \\
  --apiKey YOUR_API_KEY \\
  --apiIssuer YOUR_ISSUER_ID
\`;

// 2.3 App Store Connect 配置
const appStoreConnect = \`
// App Store Connect (https://appstoreconnect.apple.com)

// 1. 创建应用
- 我的 App -> 新建 App
- 选择平台: iOS
- 填写应用名称
- 选择主要语言
- 选择套装 ID (Bundle ID)
- 填写 SKU (唯一标识符)

// 2. 填写应用信息
- 应用名称
- 副标题
- 描述
- 关键词
- 技术支持 URL
- 营销 URL
- 隐私政策 URL

// 3. 上传截图和预览
- 选择设备类型
- 上传截图
- 上传预览视频 (可选)

// 4. 填写通用信息
- 分类
- 年龄分级
- 版权
- 开发者网站

// 5. 定价和销售范围
- 选择价格等级
- 选择销售地区

// 6. 提交审核
- 选择构建版本
- 填写审核信息
  * 登录信息 (如需要)
  * 联系信息
  * 备注
- 选择发布方式
  * 手动发布
  * 自动发布
  * 定时发布
- 提交审核
\`;

// 2.4 审核注意事项
const reviewGuidelines = \`
// App Store 审核常见拒绝原因

1. 功能不完整
   ❌ 应用存在未完成的功能
   ❌ 点击按钮没有响应
   ✅ 确保所有功能正常工作

2. 包含隐藏功能
   ❌ 应用包含未描述的功能
   ❌ 有后门或私有 API
   ✅ 所有功能都在描述中说明

3. 用户界面问题
   ❌ 界面在某些设备上显示异常
   ❌ 不符合 iOS 设计规范
   ✅ 在所有设备上测试

4. 隐私问题
   ❌ 没有隐私政策
   ❌ 权限描述不清晰
   ❌ 收集不必要的数据
   ✅ 添加隐私政策 URL
   ✅ 清晰说明权限用途

5. 性能问题
   ❌ 启动时间过长
   ❌ 崩溃或卡顿
   ❌ 消耗过多电量
   ✅ 进行性能测试

6. 内容问题
   ❌ 包含成人内容
   ❌ 侵犯版权
   ❌ 虚假信息
   ✅ 确保内容合规

7. 商业问题
   ❌ 误导性描述
   ❌ 不完整的内购
   ❌ 隐藏费用
   ✅ 诚实描述应用

8. 元数据问题
   ❌ 截图不匹配实际应用
   ❌ 关键词不相关
   ❌ 图标不符合要求
   ✅ 确保元数据准确
\`;

console.log('=== iOS App Store 发布 ===');
console.log('Xcode配置:', xcodeConfig);
console.log('打包上传:', buildAndUpload);
console.log('App Store Connect:', appStoreConnect);
console.log('审核注意事项:', reviewGuidelines);
`;

console.log('\n=== iOS App Store 发布 ===');
console.log(iosAppStore);

// 3. Google Play 发布
const googlePlay = `
// Google Play 发布流程

// 3.1 配置 build.gradle
const gradleConfig = \`
// android/app/build.gradle

android {
    defaultConfig {
        applicationId "com.yourcompany.yourapp"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "1.0.0"
    }
    
    signingConfigs {
        release {
            storeFile file("release.keystore")
            storePassword "your-store-password"
            keyAlias "your-key-alias"
            keyPassword "your-key-password"
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

// 生成密钥库
keytool -genkey -v \\
  -keystore release.keystore \\
  -alias your-key-alias \\
  -keyalg RSA \\
  -keysize 2048 \\
  -validity 10000
\`;

// 3.2 配置 AndroidManifest.xml
const manifestConfig = \`
<!-- android/app/src/main/AndroidManifest.xml -->

<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.yourcompany.yourapp">

    <!-- 必要权限 -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    
    <!-- 可选权限 -->
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application
        android:label="应用名称"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:usesCleartextTraffic="false"
        android:networkSecurityConfig="@xml/network_security_config">
        
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>

<!-- res/xml/network_security_config.xml -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">yourdomain.com</domain>
    </domain-config>
</network-security-config>
\`;

// 3.3 构建 APK/AAB
const buildApk = \`
// 构建 APK
flutter build apk --release

// 构建 App Bundle (推荐)
flutter build appbundle --release

// 或者使用 Gradle
./gradlew assembleRelease
./gradlew bundleRelease

// 输出位置
// APK: build/app/outputs/flutter-apk/app-release.apk
// AAB: build/app/outputs/bundle/release/app-release.aab
\`;

// 3.4 Google Play Console 配置
const playConsole = \`
// Google Play Console (https://play.google.com/console)

// 1. 创建应用
- 所有应用 -> 创建应用
- 填写应用名称
- 选择默认语言
- 选择应用类型 (应用/游戏)
- 选择是否免费
- 声明合规声明
- 创建应用

// 2. 设置商店页面
- 商店设置 -> 主要商店列表
- 应用名称
- 简短描述 (80字符)
- 完整描述 (4000字符)
- 应用图标 (512x512 PNG)
- 特色图片 (1024x500 PNG)
- 手机截图 (最多8张)
- 7寸平板截图
- 10寸平板截图
- 宣传视频 (可选)
- 应用类型和分类
- 内容分级 (需要完成问卷)
- 联系方式
- 隐私权政策

// 3. 设置应用内容
- 政策 -> 应用内容
- 隐私权政策
- 目标受众
- 内容分级
- 应用广告 (如适用)
- 数据安全 (需要填写数据收集表单)

// 4. 制作和测试
- 测试 -> 内部测试 (可选)
- 测试 -> 封闭测试 (可选)
- 测试 -> 开放测试 (可选)
- 上传 APK/AAB
- 添加测试人员
- 发布测试版本

// 5. 发布正式版
- 制作 -> 正式版
- 创建新版本
- 上传 APK/AAB
- 填写发布说明
- 选择发布国家/地区
- 审核并发布
\`;

// 3.5 审核注意事项
const playReviewGuidelines = \`
// Google Play 审核常见拒绝原因

1. 内容政策违规
   ❌ 包含受限内容
   ❌ 知识产权侵权
   ❌ 虚假或误导性内容
   ❌ 垃圾内容

2. 用户数据政策违规
   ❌ 没有隐私政策
   ❌ 过度收集数据
   ❌ 数据使用不透明
   ❌ 没有数据安全表单

3. 应用质量问题
   ❌ 应用崩溃
   ❌ 性能差
   ❌ 功能不完整
   ❌ 用户体验差

4. 元数据问题
   ❌ 图标不符合要求
   ❌ 截图质量差
   ❌ 描述不真实
   ❌ 关键词堆砌

5. 商店展示和用户体验
   ❌ 误导性展示
   ❌ 应用未按描述工作
   ❌ 应用与设备不兼容

6. 恶意行为
   ❌ 包含恶意代码
   ❌ 收集敏感数据
   ❌ 未经授权的行为
   ❌ 影响其他应用

7. 支付政策违规
   ❌ 未使用 Google Play 结算
   ❌ 隐藏购买
   ❌ 误导性订阅
   ❌ 未经授权的数字商品

8. 家庭政策违规
   ❌ 未正确设置目标受众
   ❌ 内容不适合儿童
   ❌ 广告不符合要求
\`;

console.log('=== Google Play 发布 ===');
console.log('Gradle配置:', gradleConfig);
console.log('Manifest配置:', manifestConfig);
console.log('构建APK:', buildApk);
console.log('Play Console:', playConsole);
console.log('审核注意事项:', playReviewGuidelines);
`;

console.log('\n=== Google Play 发布 ===');
console.log(googlePlay);

// 4. 应用商店优化 (ASO)
const aso = `
// 应用商店优化 (ASO)

// 4.1 关键词优化
const keywordOptimization = {
  // 关键词研究
  research: [
    '使用 App Annie, Sensor Tower, Mobile Action 等工具',
    '分析竞争对手的关键词',
    '查看搜索建议',
    '考虑用户搜索意图'
  ],
  
  // 关键词选择
  selection: [
    '相关性: 与应用功能相关',
    '搜索量: 有一定的搜索量',
    '竞争度: 竞争不过于激烈',
    '组合使用: 核心词 + 长尾词'
  ],
  
  // iOS 关键词
  ios: {
    location: 'App Store Connect 中的关键词字段',
    limit: '100字符',
    tips: [
      '用逗号分隔',
      '不要用空格',
      '不要重复',
      '使用单数形式',
      '包含错误拼写'
    ]
  },
  
  // Google Play 关键词
  android: {
    location: '标题、简短描述、完整描述',
    tips: [
      '标题中包含核心关键词',
      '简短描述中重复核心词',
      '完整描述中自然融入',
      '关键词密度 2-3%'
    ]
  }
};

// 4.2 转化率优化
const conversionOptimization = {
  // 应用图标
  icon: [
    '设计简洁、易于识别',
    '使用独特的配色',
    '避免文字过多',
    '在小尺寸下也清晰',
    'A/B测试不同版本'
  ],
  
  // 截图
  screenshots: [
    '前3张最重要',
    '展示核心功能',
    '按使用顺序排列',
    '添加简短说明文字',
    '保持风格一致',
    '使用真实设备边框'
  ],
  
  // 描述
  description: [
    '开头3行最重要',
    '使用短句和段落',
    '包含关键词',
    '突出独特卖点',
    '使用表情符号增加吸引力',
    '添加功能列表',
    '包含用户评价'
  ],
  
  // 视频
  video: [
    '展示实际使用场景',
    '前3秒抓住注意力',
    '保持30秒以内',
    '添加背景音乐',
    '添加文字说明'
  ]
};

// 4.3 评分和评论优化
const ratingReviewOptimization = {
  // 提高评分
  improveRating: [
    '在合适的时机请求评分',
    '避免在用户遇到问题时请求',
    '用户完成积极操作后请求',
    '提供良好的用户体验',
    '快速响应用户反馈'
  ],
  
  // 请求评分时机
  requestTiming: [
    '用户完成第N次操作后',
    '用户使用应用N天后',
    '用户完成重要任务后',
    '用户连续打开应用N次后'
  ],
  
  // 回复评论
  replyReviews: [
    '及时回复所有评论',
    '感谢正面评价',
    '解决负面评价中的问题',
    '保持专业和友好',
    '邀请用户重新评价'
  ]
};

// 4.4 ASO 工具
const asoTools = {
  keywordResearch: [
    'App Annie',
    'Sensor Tower',
    'Mobile Action',
    'TheTool',
    'AppFollow'
  ],
  analytics: [
    'App Store Connect Analytics',
    'Google Play Console',
    'Firebase Analytics',
    'Mixpanel',
    'Amplitude'
  ],
  aBTesting: [
    'StoreMaven',
    'SplitMetrics',
    'Storemetrics',
    'Google Play Experiments'
  ]
};

console.log('=== 应用商店优化 (ASO) ===');
console.log('关键词优化:', keywordOptimization);
console.log('转化率优化:', conversionOptimization);
console.log('评分评论优化:', ratingReviewOptimization);
console.log('ASO工具:', asoTools);
`;

console.log('\n=== 应用商店优化 (ASO) ===');
console.log(aso);

console.log('\n🎉 应用商店学习完成！');
console.log('💡 好的发布和ASO能让更多用户发现你的应用！');
`;

console.log('\n=== 应用商店 ===');
