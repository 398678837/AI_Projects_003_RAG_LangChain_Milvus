# 02_Core_Components_核心组件

## 学习目标
- 深入理解Activity的使用
- 掌握Service的两种启动方式
- 学会使用BroadcastReceiver
- 理解ContentProvider的作用
- 掌握Intent的使用

## 关键要点
### 1. Activity
- 启动方式：显式Intent、隐式Intent
- 数据传递：Intent.putExtra()、Bundle
- 启动模式：standard、singleTop、singleTask、singleInstance
- 返回结果：startActivityForResult()

### 2. Service
- 启动方式：startService()、bindService()
- 生命周期：onCreate()、onStartCommand()、onBind()、onDestroy()
- 前台服务：显示通知，提高优先级
- IntentService：异步处理，自动停止

### 3. BroadcastReceiver
- 注册方式：静态注册（AndroidManifest.xml）、动态注册（代码）
- 系统广播：开机启动、网络变化、电量变化等
- 自定义广播：sendBroadcast()、sendOrderedBroadcast()
- 本地广播：LocalBroadcastManager，仅应用内传播

### 4. ContentProvider
- 作用：应用间数据共享
- URI：content://authority/path/id
- 操作：query()、insert()、update()、delete()
- 权限：readPermission、writePermission

### 5. Intent
- 显式Intent：指定组件名
- 隐式Intent：指定action、category、data
- Intent Filter：匹配隐式Intent

## 实践任务
1. 创建两个Activity，实现跳转和数据传递
2. 创建一个Service，实现音乐播放
3. 创建BroadcastReceiver，监听网络变化
4. 使用ContentProvider访问系统联系人

## 参考资料
- Android官方文档：Components
