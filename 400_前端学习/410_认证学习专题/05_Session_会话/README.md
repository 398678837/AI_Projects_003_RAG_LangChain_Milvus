# 05_Session_会话

## 学习目标
- 理解Session的工作原理
- 掌握Session的存储方式
- 学会使用Session实现认证
- 理解Session与Cookie的配合

## 知识点总结
1. **Session简介**：
   - 服务器端存储的用户状态
   - 与Cookie配合使用
   - 客户端存储SessionID
2. **Session工作原理**：
   - 用户登录，服务器创建Session
   - 服务器生成唯一SessionID
   - 通过Set-Cookie发送SessionID
   - 后续请求携带SessionID Cookie
   - 服务器通过SessionID查找Session数据
3. **Session存储方式**：
   - 内存存储（开发环境）
   - Redis（生产环境推荐）
   - 数据库存储
   - 文件存储
4. **Session安全**：
   - SessionID随机且不可预测
   - 设置HttpOnly和Secure
   - 定期轮换SessionID
   - 登出时销毁Session
5. **Session优缺点**：
   - 优点：服务器可控，易撤销
   - 缺点：需要存储，扩展性差

## 参考资料
- [Session 管理](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Session)
- [Express Session](https://github.com/expressjs/session)
