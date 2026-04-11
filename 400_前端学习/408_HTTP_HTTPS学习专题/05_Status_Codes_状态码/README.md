# 05_Status_Codes_状态码

## 学习目标
- 掌握HTTP状态码的分类
- 理解常见状态码的含义
- 学会在开发中正确使用状态码
- 了解各状态码的使用场景

## 知识点总结
1. **1xx（信息性）**：请求已接收，继续处理
   - 100 Continue
   - 101 Switching Protocols
2. **2xx（成功）**：请求已成功处理
   - 200 OK
   - 201 Created
   - 204 No Content
3. **3xx（重定向）**：需要进一步操作
   - 301 Moved Permanently
   - 302 Found
   - 304 Not Modified
4. **4xx（客户端错误）**：请求有错误
   - 400 Bad Request
   - 401 Unauthorized
   - 403 Forbidden
   - 404 Not Found
   - 405 Method Not Allowed
   - 409 Conflict
5. **5xx（服务器错误）**：服务器处理出错
   - 500 Internal Server Error
   - 502 Bad Gateway
   - 503 Service Unavailable

## 参考资料
- [MDN HTTP 状态码](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)
- [HTTP 状态码详解](https://www.runoob.com/http/http-status-codes.html)
