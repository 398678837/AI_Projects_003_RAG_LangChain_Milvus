# 特征

## 1. Trait定义

### 基本Trait定义
```rust
trait Summary {
    fn summarize(&self) -> String;
}
```

### 包含默认实现的Trait
```rust
trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

## 2. Trait实现

### 为类型实现Trait
```rust
struct NewsArticle {
    headline: String,
    location: String,
    author: String,
    content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}
```

### 为多个类型实现Trait
```rust
struct Tweet {
    username: String,
    content: String,
    reply: bool,
    retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

## 3. Trait作为参数

### 基本用法
```rust
fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

### Trait Bound语法
```rust
fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

### 多个Trait Bound
```rust
fn notify<T: Summary + Display>(item: &T) {
    // ...
}
```

## 4. Trait对象

### 基本用法
```rust
fn notify(item: &dyn Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

### 动态分发
```rust
let article = NewsArticle {
    headline: String::from("Penguins win the Stanley Cup Championship!"),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from("The Pittsburgh Penguins once again are the best hockey team in the NHL."),
};

let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from("of course, as you probably already know, people"),
    reply: false,
    retweet: false,
};

let items: Vec<&dyn Summary> = vec![&article, &tweet];

for item in items {
    println!("{} ", item.summarize());
}
```

## 5. 泛型与Trait

### 泛型函数
```rust
fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];
    
    for &item in list {
        if item > largest {
            largest = item;
        }
    }
    
    largest
}
```

### 关联类型
```rust
trait Iterator {
    type Item;
    
    fn next(&mut self) -> Option<Self::Item>;
}
```

---

**更新时间：2026-04-01**