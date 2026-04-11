# 02_Core_Components_核心组件

## 学习目标
- 掌握UIViewController的使用
- 理解视图和视图层级
- 学会使用UIWindow和UIScene
- 掌握导航控制器和标签栏控制器
- 理解应用Delegate和SceneDelegate

## 关键要点
### 1. UIViewController
- 视图控制器，管理视图和业务逻辑
- 生命周期：
  - viewDidLoad()：视图加载完成
  - viewWillAppear(_:)：视图即将显示
  - viewDidAppear(_:)：视图已显示
  - viewWillDisappear(_:)：视图即将消失
  - viewDidDisappear(_:)：视图已消失
- 内容容器，管理子视图控制器

### 2. UIView
- 视图基类，所有可视化组件的父类
- 层级结构，每个视图可以有子视图
- 属性：frame、bounds、center、backgroundColor
- 手势识别：UITapGestureRecognizer等
- 动画：UIView.animate

### 3. UIWindow
- 应用的窗口，显示内容的容器
- iOS 13+使用UIScene管理多个窗口
- keyWindow：接收键盘事件的窗口

### 4. 容器视图控制器
- UINavigationController：导航控制器，管理视图控制器栈
- UITabBarController：标签栏控制器，管理多个并列的视图控制器
- UISplitViewController：分栏控制器，适用于iPad

### 5. 数据传递
- 属性：直接设置属性
- 初始化：通过构造函数传递
- Delegate：代理模式
- Closure：闭包回调
- NotificationCenter：通知中心
- Singleton：单例共享

### 6. 响应链
- 事件传递机制
- 从第一响应者开始，沿响应链向上传递
- hitTest(_:with:)：寻找最佳响应者

## 实践任务
1. 创建多个UIViewController
2. 使用UINavigationController实现页面跳转
3. 使用UITabBarController创建多标签应用
4. 实现页面间数据传递

## 参考资料
- UIKit官方文档
- View Controller Programming Guide
