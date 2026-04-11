# 06_Security_安全

## 学习目标
- 理解跨域相关的安全风险
- 掌握XSS攻击和防护
- 理解CSRF攻击和防护
- 学会安全配置CORS

## 知识点总结
1. **XSS攻击**：
   - 跨站脚本攻击
   - 注入恶意脚本
   - 类型：存储型、反射型、DOM型
   - 防护：输出编码、CSP、HttpOnly
2. **CSRF攻击**：
   - 跨站请求伪造
   - 利用用户登录状态
   - 防护：CSRF Token、SameSite Cookie、验证Referer
3. **CORS安全配置**：
   - 不要使用Origin: *
   - 白名单验证Origin
   - 限制Methods和Headers
   - 谨慎使用Credentials
4. **JSONP安全**：
   - JSONP容易XSS
   - 只信任可靠数据源
   - 现代应用优先CORS
5. **其他安全**：
   - 内容安全策略CSP
   - 安全相关响应头
   - 输入验证和输出编码

## 参考资料
- [OWASP XSS](https://owasp.org/www-community/attacks/xss/)
- [OWASP CSRF](https://owasp.org/www-community/attacks/csrf)
- [MDN CSP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP)
