# 09_Fragments_片段

## 学习目标
- 理解Fragment的基本概念
- 掌握Fragment的生命周期
- 学会添加Fragment的方式
- 掌握Fragment之间的通信
- 理解FragmentManager和FragmentTransaction

## 关键要点
### 1. Fragment概述
- Fragment是Activity中的可重用部分
- 有自己的布局和生命周期
- 可以在一个Activity中组合多个Fragment
- 可以动态添加、移除、替换Fragment
- 适用于平板等大屏幕设备的自适应布局

### 2. Fragment生命周期
- onAttach()：Fragment与Activity关联时调用
- onCreate()：Fragment创建时调用
- onCreateView()：创建Fragment的视图时调用
- onActivityCreated()：Activity的onCreate()完成后调用
- onStart()：Fragment可见时调用
- onResume()：Fragment获得焦点时调用
- onPause()：Fragment失去焦点时调用
- onStop()：Fragment不可见时调用
- onDestroyView()：Fragment的视图被移除时调用
- onDestroy()：Fragment销毁时调用
- onDetach()：Fragment与Activity解除关联时调用

### 3. 添加Fragment的方式
- 静态添加：在XML布局文件中使用&lt;fragment&gt;标签
- 动态添加：使用FragmentManager和FragmentTransaction
  - add()：添加Fragment
  - remove()：移除Fragment
  - replace()：替换Fragment
  - addToBackStack()：添加到返回栈
  - commit()：提交事务

### 4. Fragment通信
- Fragment访问Activity：getActivity()
- Activity访问Fragment：FragmentManager.findFragmentById()或findFragmentByTag()
- Fragment之间通信：
  - 通过Activity作为中介
  - 使用接口回调
  - 使用ViewModel
  - 使用EventBus

### 5. FragmentManager
- 管理Activity中的Fragment
- 方法：
  - findFragmentById()：通过ID查找Fragment
  - findFragmentByTag()：通过Tag查找Fragment
  - beginTransaction()：开始Fragment事务
  - popBackStack()：弹出返回栈
  - executePendingTransactions()：立即执行待处理事务

## 实践任务
1. 静态添加Fragment到Activity
2. 动态添加、替换Fragment
3. 实现Fragment与Activity的通信
4. 实现两个Fragment之间的通信

## 参考资料
- Android官方文档：Fragments
