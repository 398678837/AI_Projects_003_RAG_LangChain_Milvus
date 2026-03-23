# FastAPI RESTful风格API

本示例展示了如何使用FastAPI创建符合RESTful风格的API，包括资源的增删改查操作。

## 功能说明

- GET /items/ - 获取所有项目
- GET /items/{item_id} - 获取单个项目
- POST /items/ - 创建新项目
- PUT /items/{item_id} - 更新项目
- DELETE /items/{item_id} - 删除项目

## 代码结构

```python
# 1. 创建FastAPI应用实例
# 2. 模拟数据库
# 3. 数据模型定义
# 4. GET /items/ - 获取所有项目
# 5. GET /items/{item_id} - 获取单个项目
# 6. POST /items/ - 创建新项目
# 7. PUT /items/{item_id} - 更新项目
# 8. DELETE /items/{item_id} - 删除项目
# 9. 启动服务器
```

## 配置说明

1. **依赖包**：
   - fastapi
   - uvicorn
   - pydantic

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
   - 获取所有项目：http://127.0.0.1:8000/items/
   - 获取单个项目：http://127.0.0.1:8000/items/1
   - API文档：http://127.0.0.1:8000/docs

## 学习要点

- **RESTful API设计**：如何设计符合RESTful风格的API
- **HTTP方法**：如何使用不同的HTTP方法（GET, POST, PUT, DELETE）
- **状态码**：如何使用适当的HTTP状态码
- **数据验证**：如何使用Pydantic进行数据验证
- **错误处理**：如何处理错误和异常

## 扩展建议

- 尝试添加更多资源和关系
- 学习如何实现分页和过滤
- 探索如何添加认证和授权
- 学习如何处理文件上传和下载
- 尝试实现更复杂的业务逻辑