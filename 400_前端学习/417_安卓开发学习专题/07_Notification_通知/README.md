# 07_Notification_通知

## 学习目标
- 理解通知的基本概念
- 掌握创建通知的步骤
- 学会设置通知的各种属性
- 掌握通知渠道的使用
- 理解通知的交互方式

## 关键要点
### 1. 通知概述
- 通知是应用在后台向用户展示信息的方式
- 显示在通知栏、锁屏等位置
- 可以包含文本、图片、操作按钮等
- 用户可以点击通知打开应用

### 2. 通知渠道（Notification Channel）
- Android 8.0（API 26）引入
- 每个通知必须属于一个渠道
- 用户可以按渠道管理通知（关闭声音、震动等）
- 创建渠道：NotificationManager.createNotificationChannel()

### 3. 创建通知步骤
1. 创建通知渠道（Android 8.0+）
2. 使用NotificationCompat.Builder构建通知
3. 设置通知内容：标题、内容、图标等
4. 设置PendingIntent（点击通知时触发）
5. 使用NotificationManager发送通知

### 4. 通知属性
- 小图标：setSmallIcon()（必须）
- 标题：setContentTitle()
- 内容：setContentText()
- 大图标：setLargeIcon()
- 优先级：setPriority()
- 声音：setSound()
- 震动：setVibrate()
- 灯光：setLights()
- 进度条：setProgress()
- 操作按钮：addAction()
- 展开式通知：setStyle()

### 5. 通知样式
- BigTextStyle：大文本样式
- BigPictureStyle：大图片样式
- InboxStyle：收件箱样式
- MessagingStyle：消息样式
- MediaStyle：媒体样式

### 6. 通知交互
- 点击通知：PendingIntent
- 操作按钮：addAction() + PendingIntent
- 删除通知：setAutoCancel()、setDeleteIntent()
- 前台服务通知：startForeground()

## 实践任务
1. 创建基本通知
2. 创建通知渠道
3. 实现展开式通知
4. 添加通知操作按钮

## 参考资料
- Android官方文档：Notifications
