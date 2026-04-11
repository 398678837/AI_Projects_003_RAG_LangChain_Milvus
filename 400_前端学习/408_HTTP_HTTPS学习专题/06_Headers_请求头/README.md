# 06_Headers_请求头

## 学习目标
- 理解HTTP请求头和响应头的作用
- 掌握常见的请求头
- 掌握常见的响应头
- 学会在开发中使用和设置头信息

## 知识点总结
1. **通用头**：请求和响应都使用
   - Date、Cache-Control、Connection
2. **请求头**：客户端发送给服务器
   - Host、User-Agent、Accept、Accept-Language
   - Authorization、Cookie、Content-Type、Content-Length
   - Referer、Origin
3. **响应头**：服务器返回给客户端
   - Content-Type、Content-Length、Set-Cookie
   - Location、Server、ETag、Last-Modified
   - Access-Control-Allow-Origin（CORS）
4. **安全相关头**：
   - Strict-Transport-Security（HSTS）
   - Content-Security-Policy（CSP）
   - X-Content-Type-Options
   - X-Frame-Options
   - X-XSS-Protection

## 参考资料
- [MDN HTTP 头](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers)
- [HTTP 头字段详解](https://www.cnblogs.com/xybaby/p/7787034.html)
