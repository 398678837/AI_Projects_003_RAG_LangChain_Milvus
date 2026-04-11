# 02_Cookie_Cookie

## 学习目标
- 理解Cookie在认证中的作用
- 掌握Cookie的安全属性
- 学会使用Cookie实现认证
- 理解Session与Cookie的配合

## 知识点总结
1. **Cookie简介**：
   - 存储在客户端的小型文本数据
   - 由服务器通过Set-Cookie头设置
   - 浏览器自动在同域请求中携带
2. **Cookie安全属性**：
   - HttpOnly：防止XSS读取
   - Secure：仅HTTPS传输
   - SameSite：防止CSRF
   - Expires/Max-Age：过期时间
3. **Cookie认证流程**：
   - 用户登录
   - 服务器设置SessionID Cookie
   - 后续请求携带Cookie
   - 服务器验证Session
4. **Session与Cookie**：
   - Cookie存储SessionID
   - Session数据存储在服务器
   - 配合使用实现状态保持
5. **安全注意事项**：
   - 不要存储敏感数据
   - 设置HttpOnly和Secure
   - 使用SameSite
   - 合理设置过期时间

## 参考资料
- [MDN Cookie](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Cookies)
- [Cookie 安全](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Cookies#security)
