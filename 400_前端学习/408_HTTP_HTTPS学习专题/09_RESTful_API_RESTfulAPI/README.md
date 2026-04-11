# 09_RESTful_API_RESTfulAPI

## 学习目标
- 理解REST架构风格
- 掌握RESTful API设计原则
- 学会设计RESTful API
- 理解资源和HTTP方法的对应关系

## 知识点总结
1. **REST简介**：表述性状态转移，一种架构风格
2. **REST核心概念**：
   - 资源（Resource）：任何事物都可以是资源
   -  URI：统一资源标识符
   - 表示（Representation）：资源的表现形式
   - 状态转移：通过HTTP方法改变资源状态
3. **RESTful API设计原则**：
   - 使用名词复数表示资源
   - 使用HTTP方法表示操作
   - 使用HTTP状态码表示结果
   - 使用查询参数过滤、排序、分页
   - 版本管理
4. **HTTP方法对应操作**：
   - GET：获取资源
   - POST：创建资源
   - PUT：更新资源（完整替换）
   - PATCH：更新资源（部分更新）
   - DELETE：删除资源
5. **API响应格式**：JSON、统一错误格式

## 参考资料
- [RESTful API 设计指南](https://www.ruanyifeng.com/blog/2014/05/restful_api.html)
- [REST API 最佳实践](https://learn.microsoft.com/zh-cn/azure/architecture/best-practices/api-design)
