# 03_UI_Development_UI开发

## 学习目标
- 掌握常用UI控件的使用
- 理解Auto Layout约束
- 学会使用Interface Builder
- 掌握自定义视图
- 理解视图动画

## 关键要点
### 1. 常用控件
- UILabel：显示文本
- UITextField：输入文本
- UIButton：按钮
- UIImageView：显示图片
- UISwitch：开关
- UISlider：滑块
- UISegmentedControl：分段控制
- UIProgressView：进度条
- UITableView：列表
- UICollectionView：网格

### 2. Auto Layout
- 约束系统，适配不同屏幕
- 约束类型：
  - Leading/Trailing：前后边距
  - Top/Bottom：上下边距
  - Width/Height：宽高
  - CenterX/CenterY：居中
  - Aspect Ratio：宽高比
- 约束优先级
- Content Hugging/Compression Resistance

### 3. Interface Builder
- Storyboard：应用界面流程
- XIB：单个视图或视图控制器
- IBOutlet：连接代码和UI
- IBAction：连接事件和代码
- Size Classes：适配不同屏幕尺寸

### 4. 自定义视图
- 继承UIView
- 重写draw(_:)方法
- 使用CAShapeLayer
- @IBDesignable/@IBInspectable

### 5. 视图动画
- UIView.animate：基础动画
- duration：持续时间
- delay：延迟
- options：动画选项
- completion：完成回调

## 实践任务
1. 使用Auto Layout创建登录界面
2. 实现UITableView列表
3. 自定义视图并使用
4. 添加视图动画效果

## 参考资料
- UIKit官方文档
- Auto Layout Guide
