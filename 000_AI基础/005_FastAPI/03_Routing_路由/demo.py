#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI路由
展示FastAPI的路由功能，包括路径参数、查询参数、嵌套路由等
"""

from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI路由示例",
    description="展示FastAPI的路由功能",
    version="1.0.0"
)

# 1. 基本路由
@app.get("/")
def read_root():
    """根路径"""
    return {"message": "Hello, FastAPI!"}

# 2. 路径参数
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """带路径参数的路由"""
    return {"item_id": item_id, "q": q}

# 3. 带验证的路径参数
@app.get("/users/{user_id}")
def read_user(
    user_id: int = Path(..., title="用户ID", description="用户的唯一标识符", ge=1, le=1000)
):
    """带验证的路径参数"""
    return {"user_id": user_id}

# 4. 查询参数
@app.get("/items/")
def read_items(
    skip: int = Query(0, ge=0, description="跳过的项目数"),
    limit: int = Query(10, ge=1, le=100, description="返回的项目数")
):
    """带查询参数的路由"""
    return {"skip": skip, "limit": limit}

# 5. 混合参数
@app.get("/items/{item_id}/details")
def read_item_details(
    item_id: int = Path(..., title="项目ID", ge=1),
    q: Optional[str] = Query(None, title="查询参数", description="额外的查询信息"),
    category: Optional[str] = Query(None, title="类别", description="项目类别")
):
    """混合路径参数和查询参数"""
    return {"item_id": item_id, "q": q, "category": category}

# 6. 嵌套路由
# 创建子路由
from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
def get_items():
    """获取所有项目"""
    return [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]

@router.get("/items/{item_id}")
def get_item(item_id: int):
    """获取单个项目"""
    return {"id": item_id, "name": f"Item {item_id}"}

# 注册子路由
app.include_router(router, prefix="/api", tags=["items"])

# 7. 带请求体的路由
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
def create_item(item: Item):
    """创建新项目"""
    return {"item": item}

# 8. 路径转换器
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    """处理包含斜杠的路径"""
    return {"file_path": file_path}

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

路由示例：
- 基本路由：http://127.0.0.1:8000/
- 路径参数：http://127.0.0.1:8000/items/1
- 带验证的路径参数：http://127.0.0.1:8000/users/5
- 查询参数：http://127.0.0.1:8000/items/?skip=0&limit=10
- 混合参数：http://127.0.0.1:8000/items/1/details?q=test&category=electronics
- 嵌套路由：http://127.0.0.1:8000/api/items/
- 路径转换器：http://127.0.0.1:8000/files/path/to/file.txt

API文档：http://127.0.0.1:8000/docs
"""
