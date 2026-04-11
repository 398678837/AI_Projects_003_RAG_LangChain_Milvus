# 06_Cancel_Request_取消请求

## 学习目标
- 掌握使用AbortController取消请求
- 掌握使用CancelToken取消请求
- 理解取消请求的使用场景
- 学会在实际项目中应用

## 知识点总结
1. **AbortController**：
   - 现代推荐方式
   - signal属性
   - abort()方法
2. **CancelToken**：
   - 旧版方式
   - axios.CancelToken
3. **使用场景**：
   - 组件卸载时
   - 搜索输入时
   - 标签页切换时
   - 重复请求时

## 参考资料
- [Axios 取消请求](https://axios-http.com/docs/cancellation)
