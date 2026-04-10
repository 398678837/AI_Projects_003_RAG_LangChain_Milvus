# 08_Authentication_认证

## 学习目标
- 理解用户认证的基本概念和流程
- 掌握密码加密和JWT token的使用
- 熟悉注册、登录、注销和密码重置功能
- 学会实现认证中间件和保护路由

## 知识点总结
1. **密码加密**：使用bcrypt进行密码加密
2. **JWT token**：生成和验证JSON Web Token
3. **注册**：创建新用户并加密密码
4. **登录**：验证用户凭证并生成token
5. **认证中间件**：验证token并保护路由
6. **受保护的路由**：需要认证才能访问的路由
7. **刷新token**：更新过期的token
8. **注销**：处理用户注销
9. **密码重置**：生成重置令牌和更新密码

## 参考资料
- [bcrypt 文档](https://www.npmjs.com/package/bcrypt)
- [jsonwebtoken 文档](https://www.npmjs.com/package/jsonwebtoken)
- [JWT 官方文档](https://jwt.io/)
