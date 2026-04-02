use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;
use std::collections::HashMap;

fn main() {
    // 1. HTTP服务器
    println!("=== HTTP服务器 ===");
    println!("Starting server on http://127.0.0.1:8080");
    println!("Press Ctrl+C to stop");
    
    // 2. 路由
    println!("\n=== 路由 ===");
    
    let mut router = Router::new();
    router.add_route(String::from("/"), || String::from("Home Page"));
    router.add_route(String::from("/about"), || String::from("About Page"));
    
    println!("Home: {}", router.handle_request("/"));
    println!("About: {}", router.handle_request("/about"));
    println!("404: {}", router.handle_request("/notfound"));
    
    // 3. 中间件
    println!("\n=== 中间件 ===");
    
    let handler = |request: String| format!("Processed: {}", request);
    let middleware = Middleware::new(Box::new(handler));
    
    let result = middleware.handle(String::from("Hello, World!"));
    println!("Result: {}", result);
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();
    
    let get = b"GET / HTTP/1.1\r\n";
    
    let response: &[u8] = if buffer.starts_with(get) {
        b"HTTP/1.1 200 OK\r\n\r\nHello, World!"
    } else {
        b"HTTP/1.1 404 NOT FOUND\r\n\r\n404 Not Found"
    };
    
    stream.write(response).unwrap();
    stream.flush().unwrap();
}

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