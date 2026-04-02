# 核心语法

## 1. 运算符与表达式

### 算术运算符
```rust
let a = 10;
let b = 3;

println!("a + b = {}", a + b); // 加法
println!("a - b = {}", a - b); // 减法
println!("a * b = {}", a * b); // 乘法
println!("a / b = {}", a / b); // 除法
println!("a % b = {}", a % b); // 取模
```

### 比较运算符
```rust
let a = 10;
let b = 3;

println!("a == b = {}", a == b); // 等于
println!("a != b = {}", a != b); // 不等于
println!("a > b = {}", a > b); // 大于
println!("a < b = {}", a < b); // 小于
println!("a >= b = {}", a >= b); // 大于等于
println!("a <= b = {}", a <= b); // 小于等于
```

### 逻辑运算符
```rust
let a = true;
let b = false;

println!("a && b = {}", a && b); // 逻辑与
println!("a || b = {}", a || b); // 逻辑或
println!("!a = {}", !a); // 逻辑非
```

### 位运算符
```rust
let a = 0b1010;
let b = 0b1100;

println!("a & b = {:b}", a & b); // 按位与
println!("a | b = {:b}", a | b); // 按位或
println!("a ^ b = {:b}", a ^ b); // 按位异或
println!("!a = {:b}", !a); // 按位非
println!("a << 1 = {:b}", a << 1); // 左移
println!("a >> 1 = {:b}", a >> 1); // 右移
```

## 2. 控制流

### if表达式
```rust
let number = 7;

if number % 2 == 0 {
    println!("{} is even", number);
} else {
    println!("{} is odd", number);
}
```

### if作为表达式
```rust
let number = 7;

let result = if number % 2 == 0 {
    "even"
} else {
    "odd"
};

println!("{} is {}", number, result);
```

### loop循环
```rust
let mut count = 0;

loop {
    println!("count = {}", count);
    count += 1;
    
    if count == 5 {
        break;
    }
}
```

### while循环
```rust
let mut count = 0;

while count < 5 {
    println!("count = {}", count);
    count += 1;
}
```

### for循环
```rust
let arr = [10, 20, 30, 40, 50];

for element in arr.iter() {
    println!("element = {}", element);
}
```

### for循环与范围
```rust
// 左闭右开范围
for number in 1..5 {
    println!("number = {}", number);
}

// 左闭右闭范围
for number in 1..=5 {
    println!("number = {}", number);
}

// 反向范围
for number in (1..5).rev() {
    println!("number = {}", number);
}
```

## 3. 函数

### 函数定义
```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    let result = add(5, 3);
    println!("5 + 3 = {}", result);
}
```

### 函数参数
```rust
fn print_name(name: &str) {
    println!("Hello, {}", name);
}

fn main() {
    print_name("Alice");
}
```

### 函数返回值
```rust
fn multiply(a: i32, b: i32) -> i32 {
    a * b
}

fn main() {
    let result = multiply(5, 3);
    println!("5 * 3 = {}", result);
}
```

## 4. 结构体与枚举

### 结构体定义
```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    
    fn new(width: u32, height: u32) -> Rectangle {
        Rectangle { width, height }
    }
}

fn main() {
    let rect = Rectangle::new(10, 20);
    println!("Area: {}", rect.area());
}
```

### 枚举定义
```rust
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Direction {
    fn print(&self) {
        match self {
            Direction::Up => println!("Up"),
            Direction::Down => println!("Down"),
            Direction::Left => println!("Left"),
            Direction::Right => println!("Right"),
        }
    }
}

fn main() {
    let dir = Direction::Up;
    dir.print();
}
```

## 5. 模式匹配

### match表达式
```rust
let number = 7;

match number {
    1 => println!("One"),
    2 => println!("Two"),
    3 | 4 | 5 => println!("Three, four, or five"),
    6..=10 => println!("Six to ten"),
    _ => println!("Other"),
}
```

### if let表达式
```rust
let some_number: Option<i32> = Some(5);

if let Some(number) = some_number {
    println!("The number is {}", number);
} else {
    println!("No number");
}
```

---

**更新时间：2026-04-01**