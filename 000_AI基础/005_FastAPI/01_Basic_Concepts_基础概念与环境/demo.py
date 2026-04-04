#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI基础概念与环境
展示FastAPI的基本概念、环境配置和简单示例
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI基础示例",
    description="FastAPI基础概念与环境配置示例",
    version="1.0.0"
)

# 根路径
@app.get("/")
def read_root():
    """根路径"""
    return {"message": "Hello, FastAPI!"}

# 带路径参数的路由
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """带路径参数的路由"""
    return {"item_id": item_id, "q": q}

# 带查询参数的路由
@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10):
    """带查询参数的路由"""
    return {"skip": skip, "limit": limit}

# 带请求体的路由
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    """带请求体的路由"""
    return {"item_name": item.name, "item_price": item.price}

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

访问方式：
- 根路径：http://127.0.0.1:8000/
- 带路径参数：http://127.0.0.1:8000/items/1
- 带查询参数：http://127.0.0.1:8000/users/?skip=0&limit=10
- API文档：http://127.0.0.1:8000/docs
- ReDoc文档：http://127.0.0.1:8000/redoc
"""
