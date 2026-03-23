#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI请求处理
展示FastAPI的请求处理功能，包括查询参数、路径参数、请求体、表单数据等
"""

from fastapi import FastAPI, Query, Path, Body, Form, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI请求处理示例",
    description="展示FastAPI的请求处理功能",
    version="1.0.0"
)

# 1. 查询参数处理
@app.get("/items/")
def read_items(
    skip: int = Query(0, ge=0, description="跳过的项目数"),
    limit: int = Query(10, ge=1, le=100, description="返回的项目数"),
    q: Optional[str] = Query(None, min_length=3, max_length=50, description="搜索关键词")
):
    """查询参数处理"""
    return {"skip": skip, "limit": limit, "q": q}

# 2. 路径参数处理
@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., title="项目ID", description="项目的唯一标识符", ge=1),
    q: Optional[str] = Query(None, description="额外的查询参数")
):
    """路径参数处理"""
    return {"item_id": item_id, "q": q}

# 3. 请求体处理
class Item(BaseModel):
    name: str = Field(..., title="项目名称", description="项目的名称")
    description: Optional[str] = Field(None, title="项目描述", description="项目的详细描述")
    price: float = Field(..., title="项目价格", description="项目的价格", gt=0)
    tax: Optional[float] = Field(None, title="税率", description="项目的税率")

@app.post("/items/")
def create_item(item: Item):
    """请求体处理"""
    return {"item": item}

# 4. 混合参数处理
@app.put("/items/{item_id}")
def update_item(
    item_id: int = Path(..., title="项目ID", ge=1),
    item: Item = Body(..., title="项目数据", description="项目的更新数据"),
    q: Optional[str] = Query(None, description="额外的查询参数")
):
    """混合参数处理"""
    return {"item_id": item_id, "item": item, "q": q}

# 5. 表单数据处理
@app.post("/login/")
def login(
    username: str = Form(..., title="用户名", description="用户的用户名"),
    password: str = Form(..., title="密码", description="用户的密码")
):
    """表单数据处理"""
    return {"username": username}

# 6. 文件上传处理
@app.post("/uploadfile/")
def create_upload_file(
    file: UploadFile = File(..., title="文件", description="要上传的文件")
):
    """文件上传处理"""
    return {"filename": file.filename, "content_type": file.content_type}

# 7. 多文件上传处理
@app.post("/uploadfiles/")
def create_upload_files(
    files: List[UploadFile] = File(..., title="文件", description="要上传的文件列表")
):
    """多文件上传处理"""
    return [{"filename": file.filename, "content_type": file.content_type} for file in files]

# 8. 复杂请求体处理
class User(BaseModel):
    name: str
    age: int

class Address(BaseModel):
    city: str
    country: str

@app.post("/users/")
def create_user(
    user: User = Body(..., embed=True, title="用户数据"),
    address: Address = Body(..., embed=True, title="地址数据")
):
    """复杂请求体处理"""
    return {"user": user, "address": address}

# 9. 原始请求体处理
@app.post("/raw/")
def read_raw_body(body: bytes = Body(...)):
    """原始请求体处理"""
    return {"body_length": len(body)}

# 10. 查询参数列表
@app.get("/items/list/")
def read_item_list(
    ids: List[int] = Query(..., title="项目ID列表", description="要获取的项目ID列表")
):
    """查询参数列表"""
    return {"ids": ids}

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

请求处理示例：
- 查询参数：http://127.0.0.1:8000/items/?skip=0&limit=10&q=test
- 路径参数：http://127.0.0.1:8000/items/1
- 请求体：POST http://127.0.0.1:8000/items/ 带JSON请求体
- 表单数据：POST http://127.0.0.1:8000/login/ 带表单数据
- 文件上传：POST http://127.0.0.1:8000/uploadfile/ 带文件
- 查询参数列表：http://127.0.0.1:8000/items/list/?ids=1&ids=2&ids=3

API文档：http://127.0.0.1:8000/docs
"""
