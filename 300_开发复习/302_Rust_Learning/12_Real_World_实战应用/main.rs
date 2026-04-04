use std::fs;
use std::io;
use std::process::Command;

fn main() {
    // 1. 系统编程
    println!("=== 系统编程 ===");
    
    // 文件系统操作
    match fs::create_dir("new_dir") {
        Ok(_) => println!("Directory created successfully"),
        Err(e) => println!("Error creating directory: {}", e),
    }
    
    match fs::write("new_dir/file.txt", "Hello, World!") {
        Ok(_) => println!("File written successfully"),
        Err(e) => println!("Error writing file: {}", e),
    }
    
    match fs::read_to_string("new_dir/file.txt") {
        Ok(content) => println!("File content: {}", content),
        Err(e) => println!("Error reading file: {}", e),
    }
    
    // 进程管理
    let output = Command::new("echo")
        .arg("Hello, World!")
        .output()
        .expect("Failed to execute command");
    
    println!("Command output: {}", String::from_utf8_lossy(&output.stdout));
    
    // 2. 网络编程
    println!("\n=== 网络编程 ===");
    println!("TCP client example");
    println!("UDP server example");
    
    // 3. 嵌入式开发
    println!("\n=== 嵌入式开发 ===");
    println!("Basic embedded program");
    
    // 4. WebAssembly
    println!("\n=== WebAssembly ===");
    println!("Basic Wasm program");
    
    // 5. 清理
    match fs::remove_dir_all("new_dir") {
        Ok(_) => println!("Directory removed successfully"),
        Err(e) => println!("Error removing directory: {}", e),
    }
}

// WebAssembly示例
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[no_mangle]
pub extern "C" fn subtract(a: i32, b: i32) -> i32 {
    a - b
}