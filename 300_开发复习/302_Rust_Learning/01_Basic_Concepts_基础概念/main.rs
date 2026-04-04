fn main() {
    // 1. 变量声明
    let x = 5;
    println!("The value of x is: {}", x);
    
    // 2. 可变变量
    let mut y = 5;
    println!("The value of y is: {}", y);
    y = 6;
    println!("The value of y is now: {}", y);
    
    // 3. 常量
    const MAX_POINTS: u32 = 100_000;
    println!("The maximum points are: {}", MAX_POINTS);
    
    // 4. 类型注解
    let z: i32 = 5;
    println!("The value of z is: {}", z);
    
    // 5. 变量遮蔽
    let a = 5;
    let a = a + 1;
    println!("The value of a is: {}", a);
    
    // 6. 标量类型
    let integer: i32 = 42;
    let float: f64 = 3.14;
    let boolean: bool = true;
    let character: char = '😎';
    
    println!("Integer: {}", integer);
    println!("Float: {}", float);
    println!("Boolean: {}", boolean);
    println!("Character: {}", character);
    
    // 7. 元组
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    println!("The tuple is: {:?}", tup);
    
    // 解构元组
    let (x, y, z) = tup;
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
    println!("The value of z is: {}", z);
    
    // 访问元组元素
    let five_hundred = tup.0;
    let six_point_four = tup.1;
    let one = tup.2;
    
    println!("The value of five_hundred is: {}", five_hundred);
    println!("The value of six_point_four is: {}", six_point_four);
    println!("The value of one is: {}", one);
    
    // 8. 数组
    let arr = [1, 2, 3, 4, 5];
    println!("The array is: {:?}", arr);
    
    // 访问数组元素
    let first = arr[0];
    let second = arr[1];
    
    println!("The first element is: {}", first);
    println!("The second element is: {}", second);
    
    // 9. 函数调用
    let result = add(5, 3);
    println!("5 + 3 = {}", result);
    
    let result2 = multiply(5, 3);
    println!("5 * 3 = {}", result2);
    
    // 10. 控制流
    let number = 7;
    
    if number % 2 == 0 {
        println!("{} is even", number);
    } else {
        println!("{} is odd", number);
    }
    
    // 11. 循环
    let mut count = 0;
    
    while count < 5 {
        println!("Count: {}", count);
        count += 1;
    }
    
    // 12. for循环
    let arr2 = [10, 20, 30, 40, 50];
    
    for element in arr2.iter() {
        println!("Element: {}", element);
    }
    
    // 13. 范围
    for number in (1..4).rev() {
        println!("Number: {}", number);
    }
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn multiply(a: i32, b: i32) -> i32 {
    a * b
}