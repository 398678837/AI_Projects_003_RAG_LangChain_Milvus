# 01_Basic_Concepts_基础概念

## 学习目标
- 了解苹果开发生态系统
- 掌握Swift语言基础
- 理解Xcode开发环境
- 理解iOS/macOS应用架构
- 掌握应用生命周期

## 关键要点
### 1. 苹果开发生态系统
- iOS：移动设备操作系统
- macOS：桌面操作系统
- watchOS：手表操作系统
- tvOS：电视操作系统
- iPadOS：平板操作系统
- Swift：苹果官方编程语言
- SwiftUI：现代UI框架
- UIKit/AppKit：传统UI框架

### 2. Swift语言基础
- 变量和常量：var、let
- 数据类型：Int、Double、String、Bool、Array、Dictionary
- 控制流：if、switch、for-in、while
- 函数：func，支持参数标签、默认值、可变参数
- 闭包：匿名函数，尾随闭包语法
- 可选类型：Optional，处理可能为nil的值
- 结构体和类：struct（值类型）、class（引用类型）

### 3. Xcode开发环境
- 项目导航：管理项目文件
- 编辑器：编写代码
- Interface Builder：设计UI
- 调试器：Debug工具
- 模拟器：测试应用
- 文档和参考：快速查询API

### 4. 应用架构
- MVC模式：Model-View-Controller
- MVVM模式：Model-View-ViewModel
- 单例模式：共享实例
- 代理模式：Delegate
- 通知中心：NotificationCenter

### 5. 应用生命周期
- UIApplicationDelegate：iOS应用生命周期
  - application(_:didFinishLaunchingWithOptions:)：应用启动完成
  - applicationDidBecomeActive(_:)：应用进入前台
  - applicationWillResignActive(_:)：应用即将失去活动状态
  - applicationDidEnterBackground(_:)：应用进入后台
  - applicationWillEnterForeground(_:)：应用即将进入前台
  - applicationWillTerminate(_:)：应用即将终止

## 实践任务
1. 创建第一个Swift Playground
2. 学习Swift基础语法
3. 熟悉Xcode界面
4. 创建简单的iOS应用

## 参考资料
- Swift官方文档：https://docs.swift.org
- Apple Developer：https://developer.apple.com
- 《Swift编程权威指南》
