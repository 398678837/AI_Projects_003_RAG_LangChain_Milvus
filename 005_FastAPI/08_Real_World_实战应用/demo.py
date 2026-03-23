#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI实战应用
展示FastAPI在实际应用中的使用，包括用户认证、数据库操作、文件上传等
"""

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from typing import Optional, List
import uvicorn
import jwt
import datetime
import os

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI实战应用",
    description="展示FastAPI在实际应用中的使用",
    version="1.0.0"
)

# 配置
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 模拟数据库
users_db = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # password
        "disabled": False,
    }
}

items_db = [
    {"id": 1, "name": "Item 1", "description": "First item", "price": 10.99, "owner": "admin"},
    {"id": 2, "name": "Item 2", "description": "Second item", "price": 19.99, "owner": "admin"}
]

# 数据模型
class User(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    owner: Optional[str] = None

class ItemCreate(Item):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

# 工具函数
def verify_password(plain_password, hashed_password):
    """验证密码"""
    return plain_password == "password"  # 简化示例

def get_user(db, username: str):
    """获取用户"""
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    """认证用户"""
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    """创建访问令牌"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 依赖
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """获取当前用户"""
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user(users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """获取当前活跃用户"""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# 路由

# 认证路由
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """用户登录"""
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 用户路由
@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """获取当前用户信息"""
    return current_user

# 项目路由
@app.get("/items/", response_model=List[Item])
async def read_items(current_user: User = Depends(get_current_active_user)):
    """获取项目列表"""
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, current_user: User = Depends(get_current_active_user)):
    """获取单个项目"""
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate, current_user: User = Depends(get_current_active_user)):
    """创建项目"""
    new_id = max(item["id"] for item in items_db) + 1 if items_db else 1
    new_item = {
        "id": new_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "owner": current_user.username
    }
    items_db.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate, current_user: User = Depends(get_current_active_user)):
    """更新项目"""
    for index, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            if existing_item["owner"] != current_user.username:
                raise HTTPException(status_code=403, detail="Not authorized to update this item")
            updated_item = existing_item.copy()
            if item.name is not None:
                updated_item["name"] = item.name
            if item.description is not None:
                updated_item["description"] = item.description
            if item.price is not None:
                updated_item["price"] = item.price
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int, current_user: User = Depends(get_current_active_user)):
    """删除项目"""
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            if item["owner"] != current_user.username:
                raise HTTPException(status_code=403, detail="Not authorized to delete this item")
            items_db.pop(index)
            return None
    raise HTTPException(status_code=404, detail="Item not found")

# 文件上传路由
@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(..., description="要上传的文件"),
    current_user: User = Depends(get_current_active_user)
):
    """上传文件"""
    # 确保上传目录存在
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    # 保存文件
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    return {"filename": file.filename, "path": file_path}

@app.get("/downloadfile/{filename}")
async def download_file(
    filename: str,
    current_user: User = Depends(get_current_active_user)
):
    """下载文件"""
    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=file_path, filename=filename)

# 健康检查路由
@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

实战应用示例：
- 认证：POST http://127.0.0.1:8000/token 带表单数据（username=admin, password=password）
- 获取用户信息：GET http://127.0.0.1:8000/users/me 带Authorization头
- 获取项目列表：GET http://127.0.0.1:8000/items/ 带Authorization头
- 创建项目：POST http://127.0.0.1:8000/items/ 带JSON请求体和Authorization头
- 上传文件：POST http://127.0.0.1:8000/uploadfile/ 带文件和Authorization头
- 健康检查：GET http://127.0.0.1:8000/health

API文档：http://127.0.0.1:8000/docs
"""
