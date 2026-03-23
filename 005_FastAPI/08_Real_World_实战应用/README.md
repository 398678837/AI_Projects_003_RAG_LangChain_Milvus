# FastAPI实战应用

本示例展示了FastAPI在实际应用中的使用，包括用户认证、数据库操作、文件上传等。

## 功能说明

- 用户认证：基于OAuth2的用户认证
- 用户管理：获取当前用户信息
- 项目管理：创建、获取、更新、删除项目
- 文件上传：上传和下载文件
- 健康检查：检查服务健康状态

## 代码结构

```python
# 1. 配置
# 2. 模拟数据库
# 3. 数据模型
# 4. 工具函数
# 5. 依赖
# 6. 认证路由
# 7. 用户路由
# 8. 项目路由
# 9. 文件上传路由
# 10. 健康检查路由
# 11. 启动服务器
```

## 配置说明

1. **依赖包**：
   - fastapi
   - uvicorn
   - pydantic
   - python-jose (用于JWT认证)

2. **安装依赖**：
   ```bash
   pip install -r ../../requirements.txt
   ```

## 运行示例

1. 运行示例代码：
   ```bash
   python demo.py
   ```
   或
   ```bash
   uvicorn demo:app --reload
   ```

2. 访问方式：
   - 认证：POST http://127.0.0.1:8000/token 带表单数据（username=admin, password=password）
   - 获取用户信息：GET http://127.0.0.1:8000/users/me 带Authorization头
   - 获取项目列表：GET http://127.0.0.1:8000/items/ 带Authorization头
   - 创建项目：POST http://127.0.0.1:8000/items/ 带JSON请求体和Authorization头
   - 上传文件：POST http://127.0.0.1:8000/uploadfile/ 带文件和Authorization头
   - 健康检查：GET http://127.0.0.1:8000/health

## 学习要点

- **用户认证**：如何实现基于OAuth2的用户认证
- **JWT令牌**：如何创建和验证JWT令牌
- **项目管理**：如何实现CRUD操作
- **文件上传**：如何处理文件上传和下载
- **权限控制**：如何实现基于用户的权限控制
- **健康检查**：如何实现服务健康检查

## 扩展建议

- 尝试使用真实的数据库
- 学习如何实现更复杂的认证机制
- 探索如何实现API版本控制
- 学习如何部署FastAPI应用到生产环境
- 尝试实现更复杂的业务逻辑