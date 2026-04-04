#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI RESTful风格API
展示如何使用FastAPI创建符合RESTful风格的API
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title="RESTful API示例",
    description="使用FastAPI创建符合RESTful风格的API",
    version="1.0.0"
)

# 模拟数据库
items = [
    {"id": 1, "name": "Item 1", "description": "First item", "price": 10.99, "tax": 0.1},
    {"id": 2, "name": "Item 2", "description": "Second item", "price": 19.99, "tax": 0.1},
    {"id": 3, "name": "Item 3", "description": "Third item", "price": 5.99, "tax": 0.1}
]

# 数据模型
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    name: Optional[str] = None
    price: Optional[float] = None

class Item(ItemBase):
    id: int
    
    class Config:
        from_attributes = True

# GET /items/ - 获取所有项目
@app.get("/items/", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 10):
    """获取所有项目"""
    return items[skip:skip+limit]

# GET /items/{item_id} - 获取单个项目
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """获取单个项目"""
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# POST /items/ - 创建新项目
@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    """创建新项目"""
    new_id = max(item["id"] for item in items) + 1 if items else 1
    new_item = {
        "id": new_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax
    }
    items.append(new_item)
    return new_item

# PUT /items/{item_id} - 更新项目
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    """更新项目"""
    for index, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            updated_item = existing_item.copy()
            if item.name is not None:
                updated_item["name"] = item.name
            if item.description is not None:
                updated_item["description"] = item.description
            if item.price is not None:
                updated_item["price"] = item.price
            if item.tax is not None:
                updated_item["tax"] = item.tax
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE /items/{item_id} - 删除项目
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """删除项目"""
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(index)
            return None
    raise HTTPException(status_code=404, detail="Item not found")

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

RESTful API端点：
- GET /items/ - 获取所有项目
- GET /items/{item_id} - 获取单个项目
- POST /items/ - 创建新项目
- PUT /items/{item_id} - 更新项目
- DELETE /items/{item_id} - 删除项目

API文档：http://127.0.0.1:8000/docs
"""
