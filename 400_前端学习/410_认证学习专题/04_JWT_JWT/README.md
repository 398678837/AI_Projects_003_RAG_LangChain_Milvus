# 04_JWT_JWT

## 学习目标
- 理解JWT的结构和原理
- 掌握JWT的生成和验证
- 学会使用JWT实现认证
- 理解JWT的优缺点和安全

## 知识点总结
1. **JWT简介**：
   - JSON Web Token
   - 自包含的令牌
   - 三部分组成：Header.Payload.Signature
2. **JWT结构**：
   - Header：算法和类型
   - Payload：声明（claims）
   - Signature：签名
3. **JWT声明**：
   - iss：签发者
   - exp：过期时间
   - sub：主题
   - aud：受众
   - 自定义声明
4. **JWT流程**：
   - 用户登录
   - 服务器生成JWT
   - 客户端存储JWT
   - 后续请求携带JWT
   - 服务器验证签名和声明
5. **JWT优缺点**：
   - 优点：无状态、可扩展、自包含
   - 缺点：无法撤销、payload可见、体积较大
6. **安全注意事项**：
   - 使用HTTPS
   - 使用强签名算法
   - 设置过期时间
   - 不要在payload存敏感数据

## 参考资料
- [JWT 官网](https://jwt.io/)
- [Introduction to JWT](https://jwt.io/introduction)
