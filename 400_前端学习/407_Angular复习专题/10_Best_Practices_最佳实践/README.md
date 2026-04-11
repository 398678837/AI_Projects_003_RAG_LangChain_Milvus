# 10_Best_Practices_最佳实践

## 学习目标
- 了解Angular开发的最佳实践
- 掌握项目结构组织
- 理解性能优化技巧
- 学会代码规范和测试

## 知识点总结
1. **项目结构**：
   - 按功能模块组织代码
   - 核心模块、共享模块、特性模块分离
   - 使用 barrel 文件简化导入
2. **组件设计**：
   - 保持组件小巧专注
   - 使用输入输出属性通信
   - 利用内容投影提高复用性
3. **性能优化**：
   - 使用 OnPush 变更检测策略
   - 懒加载模块
   - 使用 trackBy 优化 *ngFor
   - 避免在模板中调用复杂方法
4. **代码规范**：
   - 遵循 Angular 风格指南
   - 使用有意义的命名
   - 添加适当的注释
5. **测试**：
   - 单元测试组件和服务
   - 使用 TestBed 配置测试模块
   - 测试异步操作

## 参考资料
- [Angular 风格指南](https://angular.cn/guide/style-guide)
- [Angular 性能优化](https://angular.cn/guide/performance)
- [Angular 测试](https://angular.cn/guide/testing)
