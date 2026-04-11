# 03_Token_Token

## 学习目标
- 理解Token认证的原理
- 掌握Token的生成和验证
- 学会使用Token实现认证
- 理解Token的安全存储

## 知识点总结
1. **Token简介**：
   - 代表用户身份的字符串
   - 无状态，服务器不存储
   - 客户端存储和发送
2. **Token认证流程**：
   - 用户登录
   - 服务器生成Token
   - 返回Token给客户端
   - 客户端存储Token
   - 后续请求携带Token（Authorization头）
   - 服务器验证Token
3. **Token格式**：
   - 随机字符串
   - 有意义的编码字符串
   - JWT（结构化Token）
4. **Token存储**：
   - LocalStorage
   - SessionStorage
   - Memory（内存变量）
   - Cookie（HttpOnly）
5. **安全注意事项**：
   - 使用HTTPS传输
   - 设置过期时间
   - 实现刷新机制
   - 防止Token泄露

## 参考资料
- [Token 认证](https://jwt.io/introduction)
- [Token 最佳实践](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/)
