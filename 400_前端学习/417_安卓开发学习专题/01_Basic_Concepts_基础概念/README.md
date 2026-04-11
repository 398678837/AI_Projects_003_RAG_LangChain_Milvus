# 01_Basic_Concepts_基础概念

## 学习目标
- 了解Android系统架构
- 掌握Android应用的基本结构
- 理解四大组件的概念
- 学会配置AndroidManifest.xml
- 掌握Activity生命周期

## 关键要点
### 1. Android系统架构
- Linux内核层：硬件驱动、内存管理、进程管理
- 系统运行库层：C/C++库、Android运行时
- 应用框架层：ActivityManager、PackageManager等
- 应用层：用户应用程序

### 2. 应用基本结构
- src/main/java：Java/Kotlin源代码
- src/main/res：资源文件（布局、字符串、图片等）
- AndroidManifest.xml：应用清单文件
- build.gradle：构建配置文件

### 3. 四大组件
- Activity：应用界面，用户交互的入口
- Service：后台服务，无界面的长时间运行任务
- BroadcastReceiver：广播接收器，接收系统或应用广播
- ContentProvider：内容提供者，应用间数据共享

### 4. Activity生命周期
- onCreate：Activity创建时调用
- onStart：Activity可见时调用
- onResume：Activity获得焦点时调用
- onPause：Activity失去焦点时调用
- onStop：Activity不可见时调用
- onDestroy：Activity销毁时调用
- onRestart：Activity从停止状态重新启动时调用

## 实践任务
1. 创建一个简单的Android应用
2. 在MainActivity中打印生命周期日志
3. 配置AndroidManifest.xml
4. 添加应用图标和名称

## 参考资料
- Android官方文档：https://developer.android.com/docs
- 《第一行代码》
