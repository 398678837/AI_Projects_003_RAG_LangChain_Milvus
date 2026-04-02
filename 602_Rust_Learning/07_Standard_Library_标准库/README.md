# 标准库

## 1. std::fmt

### 格式化输出
```rust
use std::fmt;

struct Point {
    x: i32,
    y: i32,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

fn main() {
    let p = Point { x: 1, y: 2 };
    println!("Point: {}", p);
}
```

### Debug格式化
```rust
#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 1, y: 2 };
    println!("Point: {:?}", p);
    println!("Point: {:#?}", p);
}
```

## 2. std::collections

### 向量
```rust
use std::collections::VecDeque;

fn main() {
    let mut vec = Vec::new();
    vec.push(1);
    vec.push(2);
    vec.push(3);
    
    println!("vec: {:?}", vec);
    println!("vec[0]: {}", vec[0]);
    
    let mut vec_deque = VecDeque::new();
    vec_deque.push_back(1);
    vec_deque.push_back(2);
    vec_deque.push_front(0);
    
    println!("vec_deque: {:?}", vec_deque);
}
```

### 哈希映射
```rust
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    
    println!("scores: {:?}", scores);
    
    let team_name = String::from("Blue");
    let score = scores.get(&team_name);
    
    println!("score: {:?}", score);
}
```

## 3. std::fs

### 读取文件
```rust
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let content = fs::read_to_string("file.txt")?;
    println!("File content: {}", content);
    Ok(())
}
```

### 写入文件
```rust
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    fs::write("file.txt", "Hello, world!")?;
    Ok(())
}
```

## 4. std::net

### TCP服务器
```rust
use std::io::Read;
use std::net::TcpListener;
use std::net::TcpStream;

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    stream.read(&mut buffer).unwrap();
    println!("Received: {}", String::from_utf8_lossy(&buffer));
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        handle_client(stream);
    }
}
```

---

**更新时间：2026-04-01**