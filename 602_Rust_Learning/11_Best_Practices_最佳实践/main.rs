fn main() {
    // 1. 代码规范
    println!("=== 代码规范 ===");
    
    let person = Person {
        first_name: String::from("Alice"),
        last_name: String::from("Smith"),
    };
    
    let name = get_person_name(&person);
    println!("Person name: {}", name);
    
    // 2. 性能优化
    println!("\n=== 性能优化 ===");
    
    // 避免不必要的克隆
    let s = String::from("Hello, World!");
    let result = process_string(&s);
    println!("Processed string: {}", result);
    
    // 使用迭代器
    let result: Vec<i32> = (0..10).map(|i| i * 2).collect();
    println!("Iterator result: {:?}", result);
    
    // 3. 错误处理
    println!("\n=== 错误处理 ===");
    
    match divide(10, 2) {
        Ok(result) => println!("Result: {}", result),
        Err(error) => println!("Error: {}", error),
    }
    
    match divide(10, 0) {
        Ok(result) => println!("Result: {}", result),
        Err(error) => println!("Error: {}", error),
    }
    
    // 4. 测试
    println!("\n=== 测试 ===");
    println!("Running tests...");
}

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

// 避免不必要的克隆
fn process_string(s: &str) -> String {
    format!("Processed: {}", s)
}

// 使用Result类型
fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}

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