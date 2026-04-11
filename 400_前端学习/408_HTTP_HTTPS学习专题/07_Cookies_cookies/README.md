# 07_Cookies_cookies

## 学习目标
- 理解Cookie的概念和作用
- 掌握Cookie的设置和读取
- 了解Cookie的属性
- 理解Cookie的安全问题

## 知识点总结
1. **Cookie简介**：存储在客户端的小型文本数据
2. **Cookie用途**：
   - 会话管理（登录状态）
   - 个性化设置
   - 追踪分析
3. **Cookie属性**：
   - Name/Value：名称和值
   - Expires/Max-Age：过期时间
   - Domain：作用域域名
   - Path：作用域路径
   - Secure：仅HTTPS传输
   - HttpOnly：防止XSS读取
   - SameSite：防止CSRF
4. **Cookie操作**：
   - 设置：document.cookie = "key=value"
   - 读取：document.cookie
   - 删除：设置过期时间为过去
5. **安全问题**：
   - XSS攻击：HttpOnly缓解
   - CSRF攻击：SameSite缓解
   - 不要存储敏感信息

## 参考资料
- [MDN Cookie](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Cookies)
- [Cookie 详解](https://www.ruanyifeng.com/blog/2018/07/cookie.html)
