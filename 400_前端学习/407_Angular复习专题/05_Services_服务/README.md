# 05_Services_服务

## 学习目标
- 理解服务的概念和作用
- 掌握服务的创建和注入
- 理解依赖注入的原理
- 学会使用服务实现组件间通信
- 了解服务的作用域

## 知识点总结
1. **服务的作用**：封装可复用的业务逻辑，实现组件间通信
2. **创建服务**：使用 ng generate service 命令或 @Injectable 装饰器
3. **依赖注入**：
   - 在构造函数中注入服务
   - 提供商配置：providedIn、providers 数组
4. **服务的作用域**：
   - 根级服务：单例，整个应用共享
   - 模块级服务：模块内共享
   - 组件级服务：组件及其子组件共享
5. **服务通信方式**：
   - 通过属性共享数据
   - 通过 Observable 和 Subject 实现事件通信

## 参考资料
- [Angular 服务与依赖注入](https://angular.cn/guide/architecture-services)
- [Angular 依赖注入](https://angular.cn/guide/dependency-injection)
