# 09_Troubleshooting_问题排查

## 学习目标
- 学会排查常见的跨域问题
- 掌握调试工具和方法
- 理解错误信息的含义
- 快速定位和解决问题

## 知识点总结
1. **常见CORS错误**：
   - No Access-Control-Allow-Origin
   - Allow-Origin不能为*同时带凭证
   - Method not allowed
   - Header not allowed
2. **代理问题排查**：
   - 代理不生效
   - 404 Not Found
   - 504 Gateway Timeout
   - 路径重写错误
3. **调试工具**：
   - 浏览器DevTools Network
   - Console查看错误
   - Charles/Fiddler抓包
   - 服务端日志
4. **排查步骤**：
   - 确认是否真的是跨域问题
   - 查看浏览器错误信息
   - 检查Network面板请求详情
   - 验证服务器配置
   - 测试简化场景
5. **常见误区**：
   - 只看前端，忽略后端
   - 不看错误信息
   - 乱改配置
   - 不重启服务

## 参考资料
- [CORS 错误排查](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS/Errors)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
