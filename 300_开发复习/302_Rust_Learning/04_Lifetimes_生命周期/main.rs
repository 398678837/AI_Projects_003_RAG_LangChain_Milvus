fn main() {
    // 1. 生命周期注解
    println!("=== 生命周期注解 ===");
    
    let string1 = String::from("long string is long");
    let string2 = String::from("xyz");
    
    let result = longest(string1.as_str(), string2.as_str());
    println!("The longest string is {}", result);
    
    // 2. 结构体中的生命周期
    println!("\n=== 结构体中的生命周期 ===");
    
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt { part: first_sentence };
    
    println!("Important excerpt: {}", i.part);
    
    // 多个生命周期参数
    let x = 5;
    let y = 10;
    let point = Point { x: &x, y: &y };
    
    println!("Point: x = {}, y = {}", point.x, point.y);
    
    // 3. 函数中的生命周期
    println!("\n=== 函数中的生命周期 ===");
    
    let s = String::from("hello world");
    let word = first_word(&s);
    
    println!("First word: {}", word);
    
    // 4. 静态生命周期
    println!("\n=== 静态生命周期 ===");
    
    let static_string: &'static str = "I have a static lifetime.";
    println!("{} ", static_string);
    
    let another_static = get_static_string();
    println!("{} ", another_static);
    
    // 5. 生命周期省略
    println!("\n=== 生命周期省略 ===");
    
    let s2 = String::from("hello rust");
    let word2 = first_word_omitted(&s2);
    
    println!("First word (omitted): {}", word2);
}

fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

struct ImportantExcerpt<'a> {
    part: &'a str,
}

struct Point<'a, 'b> {
    x: &'a i32,
    y: &'b i32,
}

fn first_word<'a>(s: &'a str) -> &'a str {
    let bytes = s.as_bytes();
    
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    
    &s[..]
}

fn get_static_string() -> &'static str {
    "Hello, world!"
}

// 生命周期省略
fn first_word_omitted(s: &str) -> &str {
    let bytes = s.as_bytes();
    
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    
    &s[..]
}