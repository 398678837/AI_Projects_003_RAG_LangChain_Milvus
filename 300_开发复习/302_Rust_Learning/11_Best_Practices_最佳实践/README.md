# 最佳实践

## 1. 代码规范

### 命名规范
```rust
// 结构体使用大驼峰
struct Person {
    // 字段使用小驼峰
    first_name: String,
    last_name: String,
}

// 函数使用小驼峰
fn get_person_name(person: &Person) -> String {
    format!("{} {}", person.first_name, person.last_name)
}

// 常量使用全大写
const MAX_AGE: u32 = 100;
```

### 注释规范
```rust
/// 计算两个数的和
/// 
/// # 参数
/// * `a` - 第一个数
/// * `b` - 第二个数
/// 
/// # 返回值
/// 两个数的和
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

## 2. 性能优化

### 避免不必要的克隆
```rust
// 不好的写法
fn process_string(s: String) -> String {
    let s_clone = s.clone();
    // ...
    s_clone
}

// 好的写法
fn process_string(s: &str) -> String {
    // ...
    s.to_string()
}
```

### 使用迭代器
```rust
// 不好的写法
let mut result = Vec::new();
for i in 0..10 {
    result.push(i * 2);
}

// 好的写法
let result: Vec<i32> = (0..10).map(|i| i * 2).collect();
```

## 3. 错误处理

### 使用Result类型
```rust
fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}

fn main() {
    match divide(10, 2) {
        Ok(result) => println!("Result: {}", result),
        Err(error) => println!("Error: {}", error),
    }
}
```

### 使用thiserror库
```rust
use thiserror::Error;

#[derive(Error, Debug)]
enum MyError {
    #[error("IO error: {0}")]
    IoError(#[from] std::io::Error),
    
    #[error("Parse error: {0}")]
    ParseError(String),
}
```

## 4. 测试

### 单元测试
```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
    
    #[test]
    fn test_divide() {
        assert_eq!(divide(10, 2), Ok(5));
        assert_eq!(divide(10, 0), Err(String::from("Division by zero")));
    }
}
```

### 集成测试
```rust
// tests/integration_test.rs
use my_crate::add;

#[test]
fn test_add() {
    assert_eq!(add(2, 3), 5);
}
```

---

**更新时间：2026-04-01**