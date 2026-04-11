# 04_Network_网络请求

## 学习目标
- 掌握URLSession的使用
- 学会使用Alamofire库
- 理解JSON数据解析
- 掌握Codable协议
- 理解网络请求的最佳实践

## 关键要点
### 1. URLSession
- Apple原生网络请求API
- 类型：
  - shared：共享会话
  - default：默认配置
  - ephemeral：临时会话，不缓存
  - background：后台会话
- 任务类型：
  - dataTask：数据任务
  - downloadTask：下载任务
  - uploadTask：上传任务

### 2. HTTP方法
- GET：获取资源
- POST：提交资源
- PUT：更新资源
- DELETE：删除资源
- PATCH：部分更新资源

### 3. JSON解析
- Codable协议：Encodable + Decodable
- JSONEncoder：编码
- JSONDecoder：解码
- CodingKeys：自定义键名
- dateDecodingStrategy：日期格式
- keyDecodingStrategy：键转换策略

### 4. Alamofire
- 流行的第三方网络库
- 链式调用
- 自动JSON解析
- 上传/下载支持
- 响应验证

### 5. 最佳实践
- 使用后台会话处理大文件下载
- 缓存策略
- 请求超时
- 错误处理
- 网络状态监测

## 实践任务
1. 使用URLSession发起GET请求
2. 使用URLSession发起POST请求
3. 使用Codable解析JSON
4. 使用Alamofire进行网络请求

## 参考资料
- URLSession官方文档
- Alamofire文档：https://github.com/Alamofire/Alamofire
