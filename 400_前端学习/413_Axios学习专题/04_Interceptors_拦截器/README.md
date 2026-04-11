# 04_Interceptors_拦截器

## 学习目标
- 掌握请求拦截器
- 掌握响应拦截器
- 理解拦截器的执行顺序
- 学会移除拦截器

## 知识点总结
1. **请求拦截器**：
   - 在发送请求前执行
   - 可修改请求配置
   - 用于添加token等
2. **响应拦截器**：
   - 收到响应后执行
   - 可修改响应数据
   - 用于统一错误处理
3. **拦截器链**：
   - 按添加顺序执行
   - 可添加多个拦截器
4. **移除拦截器**：
   - axios.interceptors.request.eject()
   - axios.interceptors.response.eject()

## 参考资料
- [Axios 拦截器](https://axios-http.com/docs/interceptors)
