#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI依赖注入
展示FastAPI的依赖注入功能，包括简单依赖、依赖链、全局依赖等
"""

from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI依赖注入示例",
    description="展示FastAPI的依赖注入功能",
    version="1.0.0"
)

# 1. 简单依赖
async def get_query_params(skip: int = 0, limit: int = 10):
    """获取查询参数"""
    return {"skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(params: dict = Depends(get_query_params)):
    """获取项目列表"""
    return {"params": params}

# 2. 依赖类
class Pagination:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit

@app.get("/users/")
async def read_users(pagination: Pagination = Depends()):
    """获取用户列表"""
    return {"skip": pagination.skip, "limit": pagination.limit}

# 3. 依赖链
async def get_db():
    """获取数据库连接"""
    db = {"name": "test_db"}
    try:
        yield db
    finally:
        pass

async def get_user(db: dict = Depends(get_db), user_id: int = Query(..., description="用户ID")):
    """获取用户"""
    user = {"id": user_id, "name": f"User {user_id}", "db": db}
    return user

@app.get("/users/{user_id}")
async def read_user(user: dict = Depends(get_user)):
    """获取单个用户"""
    return user

# 4. 全局依赖
from fastapi import Request

async def log_requests(request: Request):
    """记录请求"""
    print(f"Request: {request.method} {request.url}")
    yield

app.dependency_overrides[log_requests] = lambda: None  # 暂时禁用全局依赖

# 5. 安全依赖
security = HTTPBasic()

async def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    """获取当前用户"""
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {"username": credentials.username}

@app.get("/secure")
async def secure_endpoint(current_user: dict = Depends(get_current_user)):
    """安全端点"""
    return {"message": "Secure endpoint", "user": current_user}

# 6. 依赖注入与路径操作装饰器
class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(
    item: Item,
    db: dict = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """创建项目"""
    return {"item": item, "db": db, "user": current_user}

# 7. 可选依赖
async def get_optional_param(q: Optional[str] = None):
    """获取可选参数"""
    return q

@app.get("/optional")
async def optional_endpoint(q: Optional[str] = Depends(get_optional_param)):
    """可选参数端点"""
    return {"q": q}

# 8. 依赖注入与响应模型
class User(BaseModel):
    id: int
    name: str
    email: str

async def get_user_model(user_id: int = Query(..., description="用户ID")):
    """获取用户模型"""
    return User(id=user_id, name=f"User {user_id}", email=f"user{user_id}@example.com")

@app.get("/user-model", response_model=User)
async def read_user_model(user: User = Depends(get_user_model)):
    """获取用户模型"""
    return user

# 9. 依赖注入与错误处理
async def get_validated_user(user_id: int = Query(..., description="用户ID")):
    """获取验证后的用户"""
    if user_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    return {"id": user_id, "name": f"User {user_id}"}

@app.get("/validated-user")
async def read_validated_user(user: dict = Depends(get_validated_user)):
    """获取验证后的用户"""
    return user

# 10. 依赖注入与后台任务
from fastapi import BackgroundTasks

async def send_email(email: str, message: str):
    """发送邮件"""
    print(f"Sending email to {email}: {message}")

@app.post("/send-email")
async def send_email_endpoint(
    email: str = Query(..., description="邮箱地址"),
    message: str = Query(..., description="邮件内容"),
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    """发送邮件端点"""
    background_tasks.add_task(send_email, email, message)
    return {"message": "Email sent in background"}

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

依赖注入示例：
- 简单依赖：http://127.0.0.1:8000/items/?skip=0&limit=10
- 依赖类：http://127.0.0.1:8000/users/?skip=0&limit=10
- 依赖链：http://127.0.0.1:8000/users/1?user_id=1
- 安全依赖：http://127.0.0.1:8000/secure (需要输入用户名admin，密码password)
- 可选依赖：http://127.0.0.1:8000/optional
- 依赖注入与响应模型：http://127.0.0.1:8000/user-model?user_id=1
- 依赖注入与错误处理：http://127.0.0.1:8000/validated-user?user_id=1
- 依赖注入与后台任务：http://127.0.0.1:8000/send-email?email=test@example.com&message=Hello

API文档：http://127.0.0.1:8000/docs
"""
