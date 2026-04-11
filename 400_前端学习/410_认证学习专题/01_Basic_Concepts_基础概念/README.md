# 01_Basic_Concepts_基础概念

## 学习目标
- 理解认证和授权的概念
- 掌握常见的认证方式
- 理解认证流程
- 了解认证相关的基本术语

## 知识点总结
1. **认证与授权**：
   - 认证（Authentication）：验证用户身份（你是谁）
   - 授权（Authorization）：验证用户权限（你能做什么）
2. **常见认证方式**：
   - Cookie/Session
   - Token
   - JWT
   - OAuth2
3. **认证流程**：
   - 用户提交凭证
   - 服务器验证凭证
   - 颁发认证令牌
   - 后续请求携带令牌
   - 服务器验证令牌
4. **基本术语**：
   - 凭证（Credentials）
   - 令牌（Token）
   - 会话（Session）
   - 签名（Signature）
   - 过期时间（Expiration）
5. **安全原则**：
   - 最小权限原则
   - 密码安全
   - HTTPS传输
   - 令牌安全存储

## 参考资料
- [MDN 认证](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Authentication)
- [认证与授权](https://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)
