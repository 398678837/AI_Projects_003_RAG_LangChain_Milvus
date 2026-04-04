fn main() {
    // 1. 变量作用域
    println!("=== 变量作用域 ===");
    
    // s 在这里无效，它尚未声明
    let s = "hello";
    // s 从这里开始有效
    println!("{}", s);
    // 这个作用域结束，s不再有效
    
    // 2. 移动
    println!("\n=== 移动 ===");
    
    let s1 = String::from("hello");
    let s2 = s1; // s1的值被移动到s2，s1不再有效
    
    // println!("{}, world!", s1); // 编译错误：s1已被移动
    println!("{}, world!", s2); // 正确
    
    // 3. 克隆
    println!("\n=== 克隆 ===");
    
    let s3 = String::from("hello");
    let s4 = s3.clone(); // 克隆s3的值，s3仍然有效
    
    println!("s3 = {}, s4 = {}", s3, s4); // 正确
    
    // 4. 引用与借用
    println!("\n=== 引用与借用 ===");
    
    let s5 = String::from("hello");
    let len = calculate_length(&s5); // 传递s5的引用
    
    println!("The length of '{}' is {}.", s5, len); // s5仍然有效
    
    // 可变引用
    let mut s6 = String::from("hello");
    change(&mut s6); // 传递可变引用
    
    println!("{}", s6); // 输出 "hello, world"
    
    // 多个不可变引用
    let s7 = String::from("hello");
    let r1 = &s7;
    let r2 = &s7;
    
    println!("r1 = {}, r2 = {}", r1, r2); // 正确
    
    // 5. 切片
    println!("\n=== 切片 ===");
    
    let s8 = String::from("hello world");
    let hello = &s8[0..5]; // 从索引0到4（不包括5）
    let world = &s8[6..11]; // 从索引6到10（不包括11）
    
    println!("{} {}", hello, world); // 输出 "hello world"
    
    // 数组切片
    let arr = [1, 2, 3, 4, 5];
    let slice = &arr[1..3]; // 从索引1到2（不包括3）
    
    println!("slice = {:?}", slice); // 输出 "slice = [2, 3]"
    
    // 6. 生命周期
    println!("\n=== 生命周期 ===");
    
    let string1 = String::from("long string is long");
    let string2 = String::from("xyz");
    
    let result = longest(string1.as_str(), string2.as_str());
    println!("The longest string is {}", result);
    
    // 结构体中的生命周期
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt { part: first_sentence };
    
    println!("Important excerpt: {}", i.part);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn change(s: &mut String) {
    s.push_str(", world");
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