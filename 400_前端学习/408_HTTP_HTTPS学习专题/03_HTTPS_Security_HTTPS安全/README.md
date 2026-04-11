# 03_HTTPS_Security_HTTPS安全

## 学习目标
- 理解HTTPS的工作原理
- 掌握SSL/TLS协议
- 了解数字证书和CA
- 理解加密算法和握手过程

## 知识点总结
1. **HTTPS简介**：HTTP + SSL/TLS，提供加密传输
2. **SSL/TLS协议**：
   - SSL：安全套接字层（已过时）
   - TLS：传输层安全（现代使用）
3. **加密方式**：
   - 对称加密：加密解密用同一密钥
   - 非对称加密：公钥加密，私钥解密
   - 混合加密：结合两者优点
4. **数字证书**：
   - CA（证书颁发机构）
   - 证书包含：公钥、域名、有效期、CA签名
5. **TLS握手过程**：
   - Client Hello
   - Server Hello
   - 证书验证
   - 密钥交换
   - 加密通信
6. **HTTPS优势**：
   - 数据加密
   - 身份认证
   - 数据完整性

## 参考资料
- [MDN HTTPS 概述](https://developer.mozilla.org/zh-CN/docs/Web/Security/HTTPS)
- [HTTPS 原理解析](https://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)
