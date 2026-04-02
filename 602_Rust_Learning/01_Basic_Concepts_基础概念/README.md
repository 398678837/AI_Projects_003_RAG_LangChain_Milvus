# 基础概念

## 1. Rust语言简介

Rust是一种系统编程语言，专注于安全、速度和并发。它由Mozilla开发，于2010年首次发布。

### 特点
- 内存安全（无需垃圾回收）
- 零成本抽象
- 并发安全
- 高性能
- 丰富的类型系统

## 2. 开发环境搭建

### 安装Rust
```bash
# 使用rustup安装
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 验证安装
rustc --version
cargo --version
```

### 更新Rust
```bash
rustup update
```

### 卸载Rust
```bash
rustup self uninstall
```

## 3. 第一个Rust程序

```rust
fn main() {
    println!("Hello, World!");
}
```

### 编译运行
```bash
rustc hello.rs
./hello
```

### 使用Cargo
```bash
# 创建新项目
cargo new hello_world
cd hello_world

# 构建项目
cargo build

# 运行项目
cargo run

# 测试项目
cargo test

# 发布项目
cargo build --release
```

## 4. 变量与常量

### 变量声明
```rust
// 可变变量
let mut x = 5;
x = 6;

// 不可变变量
let y = 5;

// 常量
const MAX_POINTS: u32 = 100_000;

// 类型注解
let z: i32 = 5;
```

### 变量遮蔽
```rust
let x = 5;
let x = x + 1;
let x = x * 2;
println!("The value of x is: {}", x); // 输出12
```

## 5. 数据类型

### 标量类型
- 整数：i8, i16, i32, i64, i128, u8, u16, u32, u64, u128, isize, usize
- 浮点数：f32, f64
- 布尔值：bool
- 字符：char

### 复合类型
- 元组：(T1, T2, ..., Tn)
- 数组：[T; N]

## 6. 函数

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    let result = add(5, 3);
    println!("5 + 3 = {}", result);
}
```

---

**更新时间：2026-04-01**