use std::fmt;
use std::collections::{VecDeque, HashMap};
use std::fs;
use std::io;

fn main() {
    // 1. std::fmt
    println!("=== std::fmt ===");
    
    let p = Point { x: 1, y: 2 };
    println!("Point: {}", p);
    
    // Debug格式化
    let p2 = Point2 { x: 1, y: 2 };
    println!("Point: {:?}", p2);
    println!("Point: {:#?}", p2);
    
    // 2. std::collections
    println!("\n=== std::collections ===");
    
    // 向量
    let mut vec = Vec::new();
    vec.push(1);
    vec.push(2);
    vec.push(3);
    
    println!("vec: {:?}", vec);
    println!("vec[0]: {}", vec[0]);
    
    // VecDeque
    let mut vec_deque = VecDeque::new();
    vec_deque.push_back(1);
    vec_deque.push_back(2);
    vec_deque.push_front(0);
    
    println!("vec_deque: {:?}", vec_deque);
    
    // 哈希映射
    let mut scores = HashMap::new();
    
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    
    println!("scores: {:?}", scores);
    
    let team_name = String::from("Blue");
    let score = scores.get(&team_name);
    
    println!("score: {:?}", score);
    
    // 3. std::fs
    println!("\n=== std::fs ===");
    
    // 写入文件
    match fs::write("file.txt", "Hello, world!") {
        Ok(_) => println!("File written successfully"),
        Err(e) => println!("Error writing file: {}", e),
    }
    
    // 读取文件
    match fs::read_to_string("file.txt") {
        Ok(content) => println!("File content: {}", content),
        Err(e) => println!("Error reading file: {}", e),
    }
    
    // 4. std::net
    println!("\n=== std::net ===");
    println!("TCP server example");
}

struct Point {
    x: i32,
    y: i32,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

#[derive(Debug)]
struct Point2 {
    x: i32,
    y: i32,
}