# 生命周期

## 1. 生命周期注解

### 基本概念
生命周期注解描述了引用的存活时间，帮助Rust编译器确保引用始终有效。

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

### 生命周期参数命名
- 生命周期参数以单引号开头，通常使用小写字母命名
- 常见的生命周期参数：'a, 'b, 'c

## 2. 结构体中的生命周期

### 包含引用的结构体
```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt { part: first_sentence };
}
```

### 多个生命周期参数
```rust
struct Point<'a, 'b> {
    x: &'a i32,
    y: &'b i32,
}
```

## 3. 函数中的生命周期

### 输入生命周期
```rust
fn first_word<'a>(s: &'a str) -> &'a str {
    let bytes = s.as_bytes();
    
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    
    &s[..]
}
```

### 输出生命周期
```rust
fn combine<'a>(x: &'a str, y: &'a str) -> &'a str {
    format!("{} {}", x, y).as_str() // 编译错误：返回临时值的引用
}
```

## 4. 静态生命周期

### 'static生命周期
```rust
let s: &'static str = "I have a static lifetime.";
```

### 静态生命周期的使用
```rust
fn get_static_string() -> &'static str {
    "Hello, world!"
}
```

## 5. 生命周期省略

### 省略规则
1. 每个参数是一个引用时，为每个参数分配不同的生命周期
2. 如果只有一个输入生命周期参数，输出生命周期参数等于输入生命周期参数
3. 如果有多个输入生命周期参数，但其中一个是&self或&mut self，输出生命周期参数等于self的生命周期

### 省略示例
```rust
// 原始函数
fn first_word<'a>(s: &'a str) -> &'a str {
    // ...
}

// 省略后的函数
fn first_word(s: &str) -> &str {
    // ...
}
```

---

**更新时间：2026-04-01**