# FastAPI数据验证

本示例展示了FastAPI的数据验证功能，包括Pydantic模型验证、字段验证等。

## 功能说明

- 基本数据验证：使用Field验证字段
- 嵌套模型：验证嵌套的Pydantic模型
- 列表模型：验证列表类型的数据
- 字典模型：验证字典类型的数据
- 联合类型：验证多种类型的数据
- 自定义验证器：使用validator和root_validator进行自定义验证
- 查询参数验证：验证查询参数
- 路径参数验证：验证路径参数
- 请求体验证：验证请求体
- 复杂验证：复杂的业务逻辑验证
- 可选字段：验证可选字段
- 字段默认值：设置字段的默认值

## 代码结构

```python
# 1. 基本数据验证
# 2. 嵌套模型
# 3. 列表模型
# 4. 字典模型
# 5. 联合类型
# 6. 自定义验证器
# 7. 查询参数验证
# 8. 路径参数验证
# 9. 请求体验证
# 10. 复杂验证
# 11. 可选字段
# 12. 字段默认值
```

## 配置说明

1. **依赖包**：
   - fastapi
   - uvicorn
   - pydantic
   - email-validator (用于EmailStr验证)

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
   - 基本数据验证：POST http://127.0.0.1:8000/items/ 带JSON请求体
   - 嵌套模型：POST http://127.0.0.1:8000/users/ 带JSON请求体
   - 列表模型：POST http://127.0.0.1:8000/item-lists/ 带JSON请求体
   - 字典模型：POST http://127.0.0.1:8000/item-dicts/ 带JSON请求体
   - 联合类型：PUT http://127.0.0.1:8000/items/1 带JSON请求体
   - 自定义验证器：POST http://127.0.0.1:8000/products/ 带JSON请求体
   - 查询参数验证：http://127.0.0.1:8000/items/?skip=0&limit=10&q=test
   - 路径参数验证：http://127.0.0.1:8000/items/1
   - 复杂验证：POST http://127.0.0.1:8000/orders/ 带JSON请求体

## 学习要点

- **Pydantic模型**：如何使用Pydantic模型定义数据结构
- **字段验证**：如何使用Field进行字段验证
- **嵌套模型**：如何验证嵌套的数据结构
- **自定义验证器**：如何使用validator和root_validator进行自定义验证
- **查询参数验证**：如何验证查询参数
- **路径参数验证**：如何验证路径参数
- **复杂验证**：如何实现复杂的业务逻辑验证

## 扩展建议

- 尝试使用更多的验证器类型
- 学习如何自定义验证器
- 探索如何使用Pydantic V2的新特性
- 学习如何处理验证错误
- 尝试实现更复杂的数据验证逻辑