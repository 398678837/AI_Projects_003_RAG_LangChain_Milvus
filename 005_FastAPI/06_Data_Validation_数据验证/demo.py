#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI数据验证
展示FastAPI的数据验证功能，包括Pydantic模型验证、字段验证等
"""

from fastapi import FastAPI, HTTPException, Query, Path, Body
from pydantic import BaseModel, Field, EmailStr, validator, root_validator
from typing import Optional, List, Dict, Union
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI数据验证示例",
    description="展示FastAPI的数据验证功能",
    version="1.0.0"
)

# 1. 基本数据验证
class Item(BaseModel):
    name: str = Field(..., title="项目名称", description="项目的名称", min_length=3, max_length=50)
    description: Optional[str] = Field(None, title="项目描述", description="项目的详细描述", max_length=200)
    price: float = Field(..., title="项目价格", description="项目的价格", gt=0)
    tax: Optional[float] = Field(None, title="税率", description="项目的税率", ge=0, le=1)
    tags: List[str] = Field(default_factory=list, title="标签", description="项目的标签")

@app.post("/items/")
def create_item(item: Item):
    """创建项目"""
    return {"item": item}

# 2. 嵌套模型
class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(..., min_length=5, max_length=10)

class User(BaseModel):
    name: str
    email: EmailStr
    address: Address

@app.post("/users/")
def create_user(user: User):
    """创建用户"""
    return {"user": user}

# 3. 列表模型
class ItemList(BaseModel):
    items: List[Item]

@app.post("/item-lists/")
def create_item_list(item_list: ItemList):
    """创建项目列表"""
    return {"item_count": len(item_list.items), "items": item_list.items}

# 4. 字典模型
class ItemDict(BaseModel):
    items: Dict[str, Item]

@app.post("/item-dicts/")
def create_item_dict(item_dict: ItemDict):
    """创建项目字典"""
    return {"item_count": len(item_dict.items), "items": item_dict.items}

# 5. 联合类型
class ItemCreate(BaseModel):
    name: str
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Union[ItemCreate, ItemUpdate]):
    """更新项目"""
    return {"item_id": item_id, "item": item}

# 6. 自定义验证器
class Product(BaseModel):
    name: str
    price: float
    discount: Optional[float] = None
    discounted_price: Optional[float] = None
    
    @validator("discount")
    def discount_must_be_less_than_price(cls, v, values):
        if v is not None and "price" in values:
            if v >= values["price"]:
                raise ValueError("折扣必须小于价格")
        return v
    
    @root_validator(pre=False)
    def calculate_discounted_price(cls, values):
        price = values.get("price")
        discount = values.get("discount")
        if price and discount:
            values["discounted_price"] = price - discount
        return values

@app.post("/products/")
def create_product(product: Product):
    """创建产品"""
    return {"product": product}

# 7. 查询参数验证
@app.get("/items/")
def read_items(
    skip: int = Query(0, ge=0, description="跳过的项目数"),
    limit: int = Query(10, ge=1, le=100, description="返回的项目数"),
    q: Optional[str] = Query(None, min_length=3, max_length=50, description="搜索关键词")
):
    """获取项目列表"""
    return {"skip": skip, "limit": limit, "q": q}

# 8. 路径参数验证
@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., title="项目ID", description="项目的唯一标识符", ge=1, le=1000)
):
    """获取单个项目"""
    return {"item_id": item_id}

# 9. 请求体验证
@app.post("/items/{item_id}")
def update_item(
    item_id: int = Path(..., title="项目ID", ge=1),
    item: Item = Body(..., title="项目数据", description="项目的更新数据")
):
    """更新项目"""
    return {"item_id": item_id, "item": item}

# 10. 复杂验证
class Order(BaseModel):
    order_id: str = Field(..., regex=r"^ORD-\d{6}$")
    items: List[Item]
    total: float
    
    @root_validator(pre=False)
    def validate_total(cls, values):
        items = values.get("items")
        total = values.get("total")
        if items:
            calculated_total = sum(item.price * (1 + (item.tax or 0)) for item in items)
            if abs(calculated_total - total) > 0.01:
                raise ValueError("总金额与项目金额不符")
        return values

@app.post("/orders/")
def create_order(order: Order):
    """创建订单"""
    return {"order": order}

# 11. 可选字段
class OptionalItem(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    tags: Optional[List[str]] = None

@app.post("/optional-items/")
def create_optional_item(item: OptionalItem):
    """创建可选字段的项目"""
    return {"item": item}

# 12. 字段默认值
class DefaultItem(BaseModel):
    name: str
    price: float
    tax: float = 0.1
    tags: List[str] = Field(default_factory=lambda: ["default"])

@app.post("/default-items/")
def create_default_item(item: DefaultItem):
    """创建带默认值的项目"""
    return {"item": item}

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

数据验证示例：
- 基本数据验证：POST http://127.0.0.1:8000/items/ 带JSON请求体
- 嵌套模型：POST http://127.0.0.1:8000/users/ 带JSON请求体
- 列表模型：POST http://127.0.0.1:8000/item-lists/ 带JSON请求体
- 字典模型：POST http://127.0.0.1:8000/item-dicts/ 带JSON请求体
- 联合类型：PUT http://127.0.0.1:8000/items/1 带JSON请求体
- 自定义验证器：POST http://127.0.0.1:8000/products/ 带JSON请求体
- 查询参数验证：http://127.0.0.1:8000/items/?skip=0&limit=10&q=test
- 路径参数验证：http://127.0.0.1:8000/items/1
- 复杂验证：POST http://127.0.0.1:8000/orders/ 带JSON请求体

API文档：http://127.0.0.1:8000/docs
"""
