# Web开发

## 1. HTTP服务器

### 基本HTTP服务器
```rust
use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();
    
    let get = b"GET / HTTP/1.1\r\n";
    
    let response = if buffer.starts_with(get) {
        b"HTTP/1.1 200 OK\r\n\r\nHello, World!"
    } else {
        b"HTTP/1.1 404 NOT FOUND\r\n\r\n404 Not Found"
    };
    
    stream.write(response).unwrap();
    stream.flush().unwrap();
}
```

## 2. 路由

### 基本路由
```rust
use std::collections::HashMap;

struct Router {
    routes: HashMap<String, fn() -> String>,
}

impl Router {
    fn new() -> Router {
        Router { routes: HashMap::new() }
    }
    
    fn add_route(&mut self, path: String, handler: fn() -> String) {
        self.routes.insert(path, handler);
    }
    
    fn handle_request(&self, path: &str) -> String {
        match self.routes.get(path) {
            Some(handler) => handler(),
            None => String::from("404 Not Found"),
        }
    }
}
```

## 3. 中间件

### 基本中间件
```rust
struct Middleware {
    next: Box<dyn Fn(String) -> String>,
}

impl Middleware {
    fn new(next: Box<dyn Fn(String) -> String>) -> Middleware {
        Middleware { next }
    }
    
    fn handle(&self, request: String) -> String {
        println!("Processing request: {}", request);
        (self.next)(request)
    }
}
```

## 4. Web框架

### 使用Actix Web
```rust
use actix_web::{web, App, HttpResponse, HttpServer};

async fn index() -> HttpResponse {
    HttpResponse::Ok().body("Hello, World!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(index))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
```

---

**更新时间：2026-04-01**