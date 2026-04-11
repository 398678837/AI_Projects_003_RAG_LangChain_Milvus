# 06_OAuth2_OAuth2

## 学习目标
- 理解OAuth2的核心概念
- 掌握OAuth2的授权流程
- 学会使用OAuth2实现第三方登录
- 理解OAuth2的安全注意事项

## 知识点总结
1. **OAuth2简介**：
   - 开放授权协议
   - 第三方应用授权访问
   - 无需分享密码
2. **OAuth2角色**：
   - Resource Owner：资源所有者（用户）
   - Client：客户端（第三方应用）
   - Authorization Server：授权服务器
   - Resource Server：资源服务器
3. **OAuth2授权流程**：
   - Authorization Code：授权码流程（推荐）
   - Implicit：隐式流程（已废弃）
   - Password：密码流程（不推荐）
   - Client Credentials：客户端凭证
4. **OAuth2令牌**：
   - Access Token：访问令牌
   - Refresh Token：刷新令牌
   - ID Token：身份令牌（OpenID Connect）
5. **OAuth2安全**：
   - 使用HTTPS
   - 验证state参数
   - 使用PKCE
   - 合理设置scope
6. **OpenID Connect**：
   - 基于OAuth2的身份层
   - 提供身份认证
   - 返回ID Token

## 参考资料
- [OAuth 2.0 官网](https://oauth.net/2/)
- [OAuth 2.0 Simplified](https://aaronparecki.com/oauth-2-simplified/)
