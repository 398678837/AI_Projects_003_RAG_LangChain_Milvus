# 06_Routing_路由

## 学习目标
- 理解路由的概念和作用
- 掌握路由配置的方法
- 学会使用路由导航
- 理解路由参数的传递和获取
- 掌握子路由和懒加载
- 了解路由守卫

## 知识点总结
1. **路由配置**：使用 RouterModule.forRoot() 配置路由
2. **路由出口**：使用 <router-outlet> 显示路由组件
3. **路由导航**：
   - 使用 routerLink 指令导航
   - 使用 Router 服务编程导航
4. **路由参数**：
   - 路径参数：/:id
   - 查询参数：?key=value
   - 片段：#fragment
5. **子路由**：使用 children 配置子路由
6. **路由守卫**：CanActivate、CanActivateChild、CanDeactivate、Resolve、CanLoad
7. **懒加载**：使用 loadChildren 实现模块懒加载

## 参考资料
- [Angular 路由与导航](https://angular.cn/guide/router)
- [Angular 路由入门](https://angular.cn/guide/router-tutorial)
