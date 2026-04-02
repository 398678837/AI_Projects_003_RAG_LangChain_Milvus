use std::collections::HashMap;

fn main() {
    // 1. SQL数据库
    println!("=== SQL数据库 ===");
    println!("SQLite example");
    
    // 2. NoSQL数据库
    println!("\n=== NoSQL数据库 ===");
    println!("Redis example");
    
    // 3. ORM框架
    println!("\n=== ORM框架 ===");
    println!("Diesel example");
    
    // 模拟数据库操作
    let mut db = Database::new();
    db.insert(String::from("1"), String::from("Alice"));
    db.insert(String::from("2"), String::from("Bob"));
    
    println!("\n模拟数据库操作：");
    println!("Get 1: {}", db.get(&String::from("1")));
    println!("Get 2: {}", db.get(&String::from("2")));
    println!("Get 3: {}", db.get(&String::from("3")));
}

struct Database {
    data: HashMap<String, String>,
}

impl Database {
    fn new() -> Database {
        Database { data: HashMap::new() }
    }
    
    fn insert(&mut self, key: String, value: String) {
        self.data.insert(key, value);
    }
    
    fn get(&self, key: &String) -> &str {
        match self.data.get(key) {
            Some(value) => value,
            None => "Not found",
        }
    }
}