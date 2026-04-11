# 04_Network_网络请求

## 学习目标
- 掌握HttpURLConnection的使用
- 学会使用OkHttp库
- 理解Retrofit的使用
- 掌握JSON数据解析
- 学会处理网络权限

## 关键要点
### 1. 网络权限
- AndroidManifest.xml中添加：
  - &lt;uses-permission android:name="android.permission.INTERNET" /&gt;
  - &lt;uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /&gt;

### 2. HttpURLConnection
- 原生API，不需要额外依赖
- GET/POST请求
- 输入输出流处理
- 必须在子线程中执行

### 3. OkHttp
- Square公司开源的HTTP客户端
- 支持同步/异步请求
- 拦截器机制
- 连接池复用
- 使用简单，性能优秀

### 4. Retrofit
- 基于OkHttp的RESTful API封装
- 注解定义接口
- 自动JSON解析（Gson/Jackson）
- RxJava支持

### 5. JSON解析
- JSONObject/JSONArray：原生API
- Gson：Google开源库
- Moshi：Square开源库
- 自动序列化/反序列化

### 6. 注意事项
- 网络请求不能在主线程
- 使用AsyncTask/Handler/RxJava/Kotlin协程切换线程
- 处理网络异常
- 缓存策略

## 实践任务
1. 使用HttpURLConnection发起GET请求
2. 使用OkHttp发起GET/POST请求
3. 使用Retrofit调用RESTful API
4. 解析JSON数据并显示

## 参考资料
- OkHttp文档：https://square.github.io/okhttp/
- Retrofit文档：https://square.github.io/retrofit/
- Gson文档：https://github.com/google/gson
