#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FastAPI响应处理
展示FastAPI的响应处理功能，包括不同类型的响应、自定义响应等
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import (
    JSONResponse, HTMLResponse, PlainTextResponse, 
    RedirectResponse, FileResponse, StreamingResponse, Response
)
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
import io

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI响应处理示例",
    description="展示FastAPI的响应处理功能",
    version="1.0.0"
)

# 1. JSON响应
@app.get("/json")
def get_json():
    """返回JSON响应"""
    return {"message": "Hello, FastAPI!", "status": "success"}

# 2. 自定义JSON响应
@app.get("/custom-json")
def get_custom_json():
    """返回自定义JSON响应"""
    content = {"message": "Hello, FastAPI!", "status": "success"}
    return JSONResponse(content=content, status_code=200, headers={"X-Custom-Header": "value"})

# 3. HTML响应
@app.get("/html", response_class=HTMLResponse)
def get_html():
    """返回HTML响应"""
    html_content = """
    <html>
        <head>
            <title>FastAPI HTML响应</title>
        </head>
        <body>
            <h1>Hello, FastAPI!</h1>
            <p>这是一个HTML响应示例</p>
        </body>
    </html>
    """
    return html_content

# 4. 纯文本响应
@app.get("/text", response_class=PlainTextResponse)
def get_text():
    """返回纯文本响应"""
    return "Hello, FastAPI! 这是一个纯文本响应"

# 5. 重定向响应
@app.get("/redirect")
def get_redirect():
    """返回重定向响应"""
    return RedirectResponse(url="/json")

# 6. 文件响应
@app.get("/file")
def get_file():
    """返回文件响应"""
    return FileResponse(path="demo.py", media_type="text/plain")

# 7. 流式响应
@app.get("/stream")
def get_stream():
    """返回流式响应"""
    def generate():
        for i in range(5):
            yield f"Line {i+1}\n"
    return StreamingResponse(generate(), media_type="text/plain")

# 8. 字节响应
@app.get("/bytes")
def get_bytes():
    """返回字节响应"""
    # content = b"Hello, FastAPI! 这是一个字节响应"
    return Response(content=content, media_type="application/octet-stream")

# 9. 错误响应
@app.get("/error")
def get_error():
    """返回错误响应"""
    raise HTTPException(status_code=404, detail="资源未找到")

# 10. 自定义错误响应
@app.get("/custom-error")
def get_custom_error():
    """返回自定义错误响应"""
    return JSONResponse(
        status_code=400,
        content={"detail": "自定义错误消息", "code": "INVALID_REQUEST"}
    )

# 11. 响应模型
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/item", response_model=Item)
def get_item():
    """返回符合响应模型的数据"""
    return {"name": "Item 1", "price": 10.99, "tax": 0.1}

# 12. 响应模型列表
@app.get("/items", response_model=List[Item])
def get_items():
    """返回符合响应模型的列表"""
    return [
        {"name": "Item 1", "price": 10.99, "tax": 0.1},
        {"name": "Item 2", "price": 19.99, "tax": 0.1}
    ]

# 13. 响应状态码
@app.post("/items", status_code=201)
def create_item(item: Item):
    """创建项目并返回201状态码"""
    return item

# 14. 响应头
@app.get("/headers")
def get_headers():
    """返回带有自定义响应头的响应"""
    content = {"message": "Hello, FastAPI!"}
    headers = {"X-Custom-Header": "value", "X-Another-Header": "another-value"}
    return JSONResponse(content=content, headers=headers)

# 15. 空响应
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """删除项目并返回204状态码"""
    return None

# 启动服务器
if __name__ == "__main__":
    uvicorn.run("demo:app", host="127.0.0.1", port=8000, reload=True)

"""
运行方式：
1. 直接运行本文件：python demo.py
2. 使用uvicorn命令：uvicorn demo:app --reload

响应处理示例：
- JSON响应：http://127.0.0.1:8000/json
- 自定义JSON响应：http://127.0.0.1:8000/custom-json
- HTML响应：http://127.0.0.1:8000/html
- 纯文本响应：http://127.0.0.1:8000/text
- 重定向响应：http://127.0.0.1:8000/redirect
- 文件响应：http://127.0.0.1:8000/file
- 流式响应：http://127.0.0.1:8000/stream
- 错误响应：http://127.0.0.1:8000/error
- 响应模型：http://127.0.0.1:8000/item
- 响应模型列表：http://127.0.0.1:8000/items

API文档：http://127.0.0.1:8000/docs
"""
