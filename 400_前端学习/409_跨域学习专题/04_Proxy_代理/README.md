# 04_Proxy_代理

## 学习目标
- 理解代理解决跨域的原理
- 掌握开发环境代理配置
- 了解生产环境代理方案
- 学会配置Nginx反向代理

## 知识点总结
1. **代理原理**：
   - 浏览器 → 代理服务器 → 目标服务器
   - 服务器之间没有同源限制
   - 对前端透明
2. **开发环境代理**：
   - Vite代理配置
   - Webpack devServer代理
   - Create React App代理
3. **生产环境代理**：
   - Nginx反向代理
   - Node.js中间件代理
   - API网关
4. **代理配置要点**：
   - target：目标服务器
   - changeOrigin：修改Origin头
   - pathRewrite：路径重写
5. **代理优势**：
   - 无需修改后端代码
   - 前端配置简单
   - 安全性好

## 参考资料
- [Vite 代理配置](https://cn.vitejs.dev/config/server-options.html#server-proxy)
- [Webpack DevServer Proxy](https://webpack.js.org/configuration/dev-server/#devserverproxy)
- [Nginx 反向代理](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
