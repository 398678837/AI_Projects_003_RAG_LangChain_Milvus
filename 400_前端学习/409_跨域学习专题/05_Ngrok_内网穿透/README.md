# 05_Ngrok_内网穿透

## 学习目标
- 理解内网穿透的概念
- 掌握Ngrok的使用方法
- 学会配置Ngrok实现本地服务公网访问
- 了解其他内网穿透工具

## 知识点总结
1. **内网穿透简介**：
   - 将本地服务暴露到公网
   - 让外部可以访问本地开发环境
   - 用于测试Webhook、第三方回调等
2. **Ngrok简介**：
   - 流行的内网穿透工具
   - 提供免费和付费版本
   - 支持HTTP、TCP、TLS隧道
3. **Ngrok使用**：
   - 注册账号获取authtoken
   - 安装Ngrok
   - 启动隧道：ngrok http 8080
4. **Ngrok功能**：
   - 随机域名
   - 自定义子域名（付费）
   - 请求日志和重放
   - Web界面查看请求
5. **其他工具**：
   - frp（开源）
   - localtunnel
   - 花生壳

## 参考资料
- [Ngrok 官网](https://ngrok.com/)
- [Ngrok 文档](https://ngrok.com/docs)
