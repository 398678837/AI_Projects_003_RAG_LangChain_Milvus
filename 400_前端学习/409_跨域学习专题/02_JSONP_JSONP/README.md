# 02_JSONP_JSONP

## 学习目标
- 理解JSONP的工作原理
- 掌握JSONP的实现方式
- 了解JSONP的优缺点
- 学会在项目中使用JSONP

## 知识点总结
1. **JSONP原理**：
   - 利用&lt;script&gt;标签没有跨域限制
   - 动态创建script标签
   - 回调函数处理返回数据
2. **JSONP流程**：
   - 前端定义回调函数
   - 创建script标签，src包含回调名
   - 服务器返回函数调用代码
   - 执行回调函数获取数据
3. **JSONP特点**：
   - 只支持GET请求
   - 需要服务器配合
   - 兼容性很好
   - 安全性较低
4. **JSONP实现**：
   - 原生JavaScript实现
   - jQuery的$.jsonp()
   - 第三方库
5. **JSONP vs AJAX**：
   - JSONP不是AJAX
   - JSONP使用script标签
   - AJAX使用XMLHttpRequest

## 参考资料
- [JSONP 原理解析](https://www.cnblogs.com/dowinning/archive/2012/04/19/2457264.html)
- [JSONP 教程](https://www.runoob.com/json/json-jsonp.html)
