# 06_Permissions_权限管理

## 学习目标
- 理解Android权限机制
- 掌握正常权限和危险权限的区别
- 学会在AndroidManifest.xml中声明权限
- 掌握运行时权限请求流程
- 理解权限组的概念

## 关键要点
### 1. 权限分类
- 正常权限（Normal Permissions）：
  - 对用户隐私和安全风险较小
  - 系统自动授予，无需用户确认
  - 例如：INTERNET、ACCESS_NETWORK_STATE、BLUETOOTH
- 危险权限（Dangerous Permissions）：
  - 涉及用户隐私或可能影响用户安全
  - 需要在运行时动态请求用户授权
  - 例如：CAMERA、READ_CONTACTS、READ_EXTERNAL_STORAGE
- 特殊权限（Special Permissions）：
  - 需要特殊处理，如SYSTEM_ALERT_WINDOW、WRITE_SETTINGS

### 2. 权限组
- 危险权限按功能分组
- 同一组内的任一权限被授权，同组其他权限自动授权
- 例如：CONTACTS组包括READ_CONTACTS、WRITE_CONTACTS、GET_ACCOUNTS

### 3. 权限声明
- 在AndroidManifest.xml中使用&lt;uses-permission&gt;标签声明
- 示例：
  &lt;uses-permission android:name="android.permission.CAMERA" /&gt;
  &lt;uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" /&gt;

### 4. 运行时权限请求流程
1. 检查是否已授权：ContextCompat.checkSelfPermission()
2. 如果未授权，检查是否需要解释：ActivityCompat.shouldShowRequestPermissionRationale()
3. 请求权限：ActivityCompat.requestPermissions()
4. 处理授权结果：onRequestPermissionsResult()

### 5. Android 6.0+适配
- Android 6.0（API 23）引入运行时权限
- targetSdkVersion &gt;= 23的应用必须适配运行时权限
- 用户可以在设置中随时撤销权限

## 实践任务
1. 声明相机和存储权限
2. 实现运行时权限请求
3. 处理权限拒绝情况
4. 适配不同Android版本

## 参考资料
- Android官方文档：Permissions overview
