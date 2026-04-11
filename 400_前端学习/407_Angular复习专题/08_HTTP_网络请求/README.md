# 08_HTTP_网络请求

## 学习目标
- 理解 HttpClient 的使用
- 掌握 GET、POST、PUT、DELETE 请求
- 学会处理请求头和请求参数
- 理解错误处理
- 掌握拦截器的使用

## 知识点总结
1. **HttpClient**：
   - 导入 HttpClientModule
   - 在服务中注入 HttpClient
2. **常用请求方法**：
   - get()：获取数据
   - post()：提交数据
   - put()：更新数据
   - delete()：删除数据
3. **请求配置**：
   - headers：设置请求头
   - params：设置查询参数
   - observe：设置响应类型
4. **错误处理**：
   - 使用 catchError 操作符
   - 使用 retry 操作符重试
5. **拦截器**：
   - HttpInterceptor 接口
   - 实现 intercept 方法
   - 用于统一处理请求和响应

## 参考资料
- [Angular HttpClient](https://angular.cn/guide/http)
- [Angular HTTP 客户端](https://angular.cn/guide/http-client)
