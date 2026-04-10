# 07_Middleware_中间件

## 学习目标
- 理解Express中间件的概念和工作原理
- 掌握应用级中间件、路由级中间件和错误处理中间件
- 熟悉内置中间件和第三方中间件
- 学会创建和使用自定义中间件

## 知识点总结
1. **中间件概念**：在请求和响应之间执行的函数
2. **应用级中间件**：应用于整个应用的中间件
3. **路由级中间件**：应用于特定路由的中间件
4. **错误处理中间件**：处理错误的中间件
5. **内置中间件**：Express内置的中间件，如express.json()
6. **第三方中间件**：第三方库提供的中间件，如helmet
7. **中间件链**：多个中间件的顺序执行
8. **中间件顺序**：中间件的定义顺序决定了执行顺序

## 参考资料
- [Express 中间件文档](https://expressjs.com/zh-cn/guide/using-middleware.html)
- [Express 内置中间件](https://expressjs.com/zh-cn/api.html#express.static)
