# 04_Request_Methods_请求方法

## 学习目标
- 掌握常见的HTTP请求方法
- 理解各方法的用途和区别
- 了解幂等性和安全性
- 学会在实际开发中选择合适的方法

## 知识点总结
1. **GET**：获取资源，安全且幂等
2. **POST**：创建资源，不安全且不幂等
3. **PUT**：更新资源（完整替换），幂等
4. **PATCH**：部分更新资源，不一定幂等
5. **DELETE**：删除资源，幂等
6. **HEAD**：获取响应头，不获取响应体
7. **OPTIONS**：获取服务器支持的方法
8. **TRACE**：回显请求，用于诊断
9. **CONNECT**：建立隧道
10. **安全性**：不会改变服务器状态
11. **幂等性**：多次执行结果相同

## 参考资料
- [MDN HTTP 请求方法](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods)
- [RESTful API 设计指南](https://www.ruanyifeng.com/blog/2014/05/restful_api.html)
