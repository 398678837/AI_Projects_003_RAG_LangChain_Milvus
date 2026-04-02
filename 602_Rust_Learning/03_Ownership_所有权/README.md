# 所有权

## 1. 所有权规则

Rust的所有权系统是其最独特的特性，它让Rust无需垃圾回收即可保证内存安全。所有权规则如下：

1. Rust中的每个值都有一个所有者
2. 同一时间只能有一个所有者
3. 当所有者离开作用域，值将被丢弃

### 变量作用域
```rust
fn main() {
    // s 在这里无效，它尚未声明
    let s = "hello";
    // s 从这里开始有效
    println!("{}", s);
} // 这个作用域结束，s不再有效
```

## 2. 移动

### 字符串类型
```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // s1的值被移动到s2，s1不再有效
    
    // println!("{}, world!", s1); // 编译错误：s1已被移动
    println!("{}, world!", s2); // 正确
}
```

### 克隆
```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1.clone(); // 克隆s1的值，s1仍然有效
    
    println!("s1 = {}, s2 = {}", s1, s2); // 正确
}
```

## 3. 引用与借用

### 不可变引用
```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1); // 传递s1的引用
    
    println!("The length of '{}' is {}.", s1, len); // s1仍然有效
}

fn calculate_length(s: &String) -> usize {
    s.len()
} // s离开作用域，但它只是一个引用，不会释放内存
```

### 可变引用
```rust
fn main() {
    let mut s = String::from("hello");
    change(&mut s); // 传递可变引用
    
    println!("{}", s); // 输出 "hello, world"
}

fn change(s: &mut String) {
    s.push_str(", world");
}
```

### 引用规则
1. 同一时间只能有一个可变引用
2. 同一时间可以有多个不可变引用
3. 不能同时拥有可变引用和不可变引用

## 4. 切片

### 字符串切片
```rust
fn main() {
    let s = String::from("hello world");
    let hello = &s[0..5]; // 从索引0到4（不包括5）
    let world = &s[6..11]; // 从索引6到10（不包括11）
    
    println!("{} {}", hello, world); // 输出 "hello world"
}
```

### 数组切片
```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];
    let slice = &arr[1..3]; // 从索引1到2（不包括3）
    
    println!("slice = {:?}", slice); // 输出 "slice = [2, 3]"
}
```

## 5. 生命周期

### 生命周期注解
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn main() {
    let string1 = String::from("long string is long");
    let string2 = String::from("xyz");
    
    let result = longest(string1.as_str(), string2.as_str());
    println!("The longest string is {}", result);
}
```

### 结构体中的生命周期
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

---

**更新时间：2026-04-01**