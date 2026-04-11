# 08_Services_服务

## 学习目标
- 理解Service的基本概念
- 掌握Service的两种启动方式
- 理解Service的生命周期
- 学会使用前台服务
- 掌握IntentService的使用

## 关键要点
### 1. Service概述
- Service是可以在后台长时间运行的应用组件
- 没有用户界面
- 即使用户切换到其他应用，Service仍可继续运行
- 运行在主线程，耗时操作需开启子线程

### 2. Service启动方式
- 启动式服务（Started Service）：
  - 通过startService()启动
  - 执行单一操作，不返回结果给调用者
  - 启动后独立运行，即使启动者被销毁
  - 需要调用stopSelf()或stopService()停止
- 绑定式服务（Bound Service）：
  - 通过bindService()启动
  - 提供客户端-服务器接口
  - 可以与组件交互、发送请求、获取结果
  - 多个组件可以绑定到同一个服务
  - 所有绑定都解除后，服务自动销毁

### 3. Service生命周期
- onCreate()：服务首次创建时调用
- onStartCommand()：每次通过startService()启动时调用
- onBind()：通过bindService()绑定时调用
- onUnbind()：所有绑定都解除时调用
- onDestroy()：服务销毁时调用

### 4. 前台服务
- 显示在通知栏的服务
- 优先级较高，不易被系统杀死
- 必须显示通知
- 使用startForeground()启动
- 需要FOREGROUND_SERVICE权限

### 5. IntentService
- Service的子类
- 使用工作线程依次处理所有启动请求
- 处理完所有请求后自动停止
- 实现onHandleIntent()方法处理异步任务

### 6. 注意事项
- Service默认运行在主线程
- 耗时操作需开启子线程或使用IntentService
- 前台服务必须显示通知
- 绑定服务需要实现ServiceConnection

## 实践任务
1. 创建启动式服务
2. 创建绑定式服务
3. 创建前台服务
4. 使用IntentService处理异步任务

## 参考资料
- Android官方文档：Services
