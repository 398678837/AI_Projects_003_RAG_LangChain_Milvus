# 03_CORS_跨域资源共享

## 学习目标
- 理解CORS的工作原理
- 掌握CORS相关的响应头
- 理解简单请求和预检请求
- 学会在服务器端配置CORS
- 理解携带凭证的请求

## 知识点总结
1. **CORS简介**：
   - 跨域资源共享（Cross-Origin Resource Sharing）
   - W3C标准，现代浏览器支持
   - 通过HTTP头控制跨域访问
2. **简单请求**：
   - GET/HEAD/POST
   - Content-Type: text/plain/multipart/form-data/application/x-www-form-urlencoded
   - 没有自定义头
   - 直接发送，不需要预检
3. **预检请求**：
   - OPTIONS方法
   - 检查服务器是否允许
   - 非简单请求会先预检
4. **CORS响应头**：
   - Access-Control-Allow-Origin
   - Access-Control-Allow-Methods
   - Access-Control-Allow-Headers
   - Access-Control-Allow-Credentials
   - Access-Control-Max-Age
5. **携带凭证**：
   - withCredentials: true
   - 服务器需要Allow-Credentials: true
   - Origin不能为*

## 参考资料
- [MDN CORS](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS)
- [CORS 详解](https://www.ruanyifeng.com/blog/2016/04/cors.html)
