fn main() {
    // 1. 运算符与表达式
    println!("=== 运算符与表达式 ===");
    
    let a = 10;
    let b = 3;
    
    println!("a + b = {}", a + b);
    println!("a - b = {}", a - b);
    println!("a * b = {}", a * b);
    println!("a / b = {}", a / b);
    println!("a % b = {}", a % b);
    
    // 比较运算符
    println!("\na == b = {}", a == b);
    println!("a != b = {}", a != b);
    println!("a > b = {}", a > b);
    println!("a < b = {}", a < b);
    println!("a >= b = {}", a >= b);
    println!("a <= b = {}", a <= b);
    
    // 逻辑运算符
    let c = true;
    let d = false;
    
    println!("\nc && d = {}", c && d);
    println!("c || d = {}", c || d);
    println!("!c = {}", !c);
    
    // 位运算符
    let e = 0b1010;
    let f = 0b1100;
    
    println!("\ne & f = {:b}", e & f);
    println!("e | f = {:b}", e | f);
    println!("e ^ f = {:b}", e ^ f);
    println!("e << 1 = {:b}", e << 1);
    println!("e >> 1 = {:b}", e >> 1);
    
    // 2. 控制流
    println!("\n=== 控制流 ===");
    
    // if表达式
    let number = 7;
    
    if number % 2 == 0 {
        println!("{} is even", number);
    } else {
        println!("{} is odd", number);
    }
    
    // if作为表达式
    let result = if number % 2 == 0 {
        "even"
    } else {
        "odd"
    };
    
    println!("{} is {}", number, result);
    
    // loop循环
    let mut count = 0;
    
    loop {
        println!("count = {}", count);
        count += 1;
        
        if count == 5 {
            break;
        }
    }
    
    // while循环
    count = 0;
    
    while count < 5 {
        println!("count = {}", count);
        count += 1;
    }
    
    // for循环
    let arr = [10, 20, 30, 40, 50];
    
    for element in arr.iter() {
        println!("element = {}", element);
    }
    
    // for循环与范围
    println!("\n=== for循环与范围 ===");
    
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
    
    // 3. 函数
    println!("\n=== 函数 ===");
    
    let result = add(5, 3);
    println!("5 + 3 = {}", result);
    
    let result2 = multiply(5, 3);
    println!("5 * 3 = {}", result2);
    
    print_name("Alice");
    
    // 4. 结构体
    println!("\n=== 结构体 ===");
    
    let rect = Rectangle::new(10, 20);
    println!("Area: {}", rect.area());
    
    // 5. 枚举
    println!("\n=== 枚举 ===");
    
    let dir = Direction::Up;
    dir.print();
    
    let dir2 = Direction::Down;
    dir2.print();
    
    // 6. 模式匹配
    println!("\n=== 模式匹配 ===");
    
    let number = 7;
    
    match number {
        1 => println!("One"),
        2 => println!("Two"),
        3 | 4 | 5 => println!("Three, four, or five"),
        6..=10 => println!("Six to ten"),
        _ => println!("Other"),
    }
    
    // if let表达式
    let some_number: Option<i32> = Some(5);
    
    if let Some(number) = some_number {
        println!("The number is {}", number);
    } else {
        println!("No number");
    }
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn multiply(a: i32, b: i32) -> i32 {
    a * b
}

fn print_name(name: &str) {
    println!("Hello, {}", name);
}

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