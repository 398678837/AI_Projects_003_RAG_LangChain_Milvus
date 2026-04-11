# 08_Real_World_实战应用

## 学习目标
- 掌握前后端分离项目的跨域配置
- 学会微服务架构的跨域处理
- 理解第三方API调用的跨域方案
- 实战配置开发和生产环境

## 知识点总结
1. **前后端分离项目**：
   - 开发环境：Vite/Webpack代理
   - 生产环境：Nginx代理或CORS
   - 多环境配置管理
2. **微服务架构**：
   - API网关统一处理跨域
   - 服务间调用无跨域问题
   - 网关配置CORS或代理
3. **第三方API调用**：
   - 后端代理转发
   - 利用JSONP（如果支持）
   - 服务端发起请求
4. **部署方案**：
   - 同域部署（前端后端一起）
   - 子域名部署（CORS）
   - Nginx反向代理
5. **实战案例**：
   - 微信公众号开发
   - OAuth登录
   - Webhook接收
   - 混合App开发

## 参考资料
- [前后端分离实践](https://developer.aliyun.com/article/764913)
- [微服务API网关](https://microservices.io/patterns/apigateway.html)
