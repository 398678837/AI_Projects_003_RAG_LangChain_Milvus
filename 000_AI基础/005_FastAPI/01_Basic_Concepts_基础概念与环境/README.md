# FastAPI基础概念与环境

本示例展示了FastAPI的基本概念、环境配置和简单示例，帮助您快速上手FastAPI框架。

## 功能说明

- 创建FastAPI应用实例
- 定义根路径
- 带路径参数的路由
- 带查询参数的路由
- 带请求体的路由
- 启动服务器

## 代码结构

```python
# 1. 创建FastAPI应用实例
# 2. 根路径
# 3. 带路径参数的路由
# 4. 带查询参数的路由
# 5. 带请求体的路由
# 6. 启动服务器
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
   - 根路径：http://127.0.0.1:8000/
   - 带路径参数：http://127.0.0.1:8000/items/1
   - 带查询参数：http://127.0.0.1:8000/users/?skip=0&limit=10
   - API文档：http://127.0.0.1:8000/docs
   - ReDoc文档：http://127.0.0.1:8000/redoc

## 学习要点

- **FastAPI应用实例**：如何创建和配置FastAPI应用
- **路由定义**：如何定义不同类型的路由
- **参数处理**：如何处理路径参数、查询参数和请求体
- **数据验证**：如何使用Pydantic进行数据验证
- **API文档**：如何访问自动生成的API文档

## 扩展建议

- 尝试添加更多类型的路由和参数
- 学习如何使用FastAPI的依赖注入系统
- 探索FastAPI的异步特性
- 学习如何处理错误和异常
- 尝试部署FastAPI应用到生产环境