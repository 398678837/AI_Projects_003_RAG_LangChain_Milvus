# 01_Basic_Concepts_基础概念

## 学习目标
- 理解什么是跨域
- 掌握同源策略的概念
- 了解跨域产生的原因
- 理解跨域的各种解决方案

## 知识点总结
1. **同源策略（Same-Origin Policy）**：
   - 浏览器的安全机制
   - 协议、域名、端口必须完全一致
   - 限制不同源之间的资源访问
2. **什么是跨域**：
   - 违反同源策略的请求就是跨域
   - 协议不同（http vs https）
   - 域名不同（a.com vs b.com）
   - 端口不同（8080 vs 3000）
3. **跨域的影响**：
   - 无法读取Cookie、LocalStorage
   - 无法获取DOM
   - AJAX请求被拦截
4. **常见跨域场景**：
   - 前后端分离开发
   - 调用第三方API
   - 微服务架构
5. **跨域解决方案**：
   - JSONP
   - CORS
   - 代理服务器
   - postMessage
   - document.domain
   - window.name

## 参考资料
- [MDN 同源策略](https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy)
- [跨域资源共享 CORS 详解](https://www.ruanyifeng.com/blog/2016/04/cors.html)
