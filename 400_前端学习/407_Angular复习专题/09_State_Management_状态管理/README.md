# 09_State_Management_状态管理

## 学习目标
- 理解状态管理的概念和必要性
- 掌握使用服务管理状态
- 理解RxJS在状态管理中的应用
- 了解NgRx等状态管理库的基本概念

## 知识点总结
1. **状态管理的作用**：
   - 统一管理应用状态
   - 简化组件间通信
   - 提高代码可维护性
2. **服务 + RxJS 状态管理**：
   - 使用 BehaviorSubject 存储状态
   - 使用 Observable 暴露状态
   - 提供方法修改状态
3. **状态管理核心概念**：
   - State：状态
   - Action：动作
   - Reducer：纯函数，计算新状态
   - Store：存储状态
4. **NgRx 简介**：
   - Store：状态容器
   - Actions：描述发生了什么
   - Reducers：处理状态变化
   - Effects：处理副作用
   - Selectors：查询状态

## 参考资料
- [Angular 状态管理](https://angular.cn/guide/state-management)
- [NgRx 官方文档](https://ngrx.io/docs)
- [RxJS 官方文档](https://rxjs.dev/)
