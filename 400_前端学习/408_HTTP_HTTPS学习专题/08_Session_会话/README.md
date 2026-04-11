# 08_Session_会话

## 学习目标
- 理解Session的概念和作用
- 掌握Session的工作原理
- 了解Session和Cookie的区别
- 理解Session的安全问题

## 知识点总结
1. **Session简介**：服务器端存储的用户会话数据
2. **Session工作原理**：
   - 用户登录时创建Session
   - 生成Session ID
   - Session ID通过Cookie发给客户端
   - 后续请求携带Session ID
   - 服务器通过Session ID找到对应数据
3. **Session vs Cookie**：
   - 存储位置：服务器 vs 客户端
   - 安全性：Session更安全
   - 容量：Session容量更大
   - 性能：Cookie性能更好
4. **Session存储方式**：
   - 内存存储
   - 文件存储
   - 数据库存储
   - Redis存储（推荐）
5. **Session安全**：
   - Session ID复杂度
   - Session过期时间
   - HTTPS传输
   - 会话固定攻击防护

## 参考资料
- [Session 工作原理](https://www.cnblogs.com/xdp-gacl/p/3807138.html)
- [Session 与 Cookie 区别](https://www.ruanyifeng.com/blog/2018/07/cookie-and-session.html)
