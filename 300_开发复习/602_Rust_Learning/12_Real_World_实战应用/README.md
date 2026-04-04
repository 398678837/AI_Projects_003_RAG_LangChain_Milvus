# 实战应用

## 1. 系统编程

### 文件系统操作
```rust
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    // 创建目录
    fs::create_dir("new_dir")?;
    
    // 写入文件
    fs::write("new_dir/file.txt", "Hello, World!")?;
    
    // 读取文件
    let content = fs::read_to_string("new_dir/file.txt")?;
    println!("File content: {}", content);
    
    // 列出目录
    let entries = fs::read_dir(".")?;
    
    for entry in entries {
        let entry = entry?;
        let path = entry.path();
        println!("{:?}", path);
    }
    
    Ok(())
}
```

### 进程管理
```rust
use std::process::Command;

fn main() {
    // 执行外部命令
    let output = Command::new("echo")
        .arg("Hello, World!")
        .output()
        .expect("Failed to execute command");
    
    println!("Command output: {}", String::from_utf8_lossy(&output.stdout));
}
```

## 2. 网络编程

### TCP客户端
```rust
use std::io::prelude::*;
use std::net::TcpStream;

fn main() {
    let mut stream = TcpStream::connect("127.0.0.1:8080").unwrap();
    
    stream.write(b"GET / HTTP/1.1\r\n\r\n").unwrap();
    
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();
    
    println!("Response: {}", String::from_utf8_lossy(&buffer));
}
```

### UDP服务器
```rust
use std::net::UdpSocket;

fn main() {
    let socket = UdpSocket::bind("127.0.0.1:8080").unwrap();
    
    let mut buffer = [0; 512];
    
    loop {
        let (number_of_bytes, src_addr) = socket.recv_from(&mut buffer).unwrap();
        
        let data = &buffer[..number_of_bytes];
        println!("Received: {}", String::from_utf8_lossy(data));
        
        socket.send_to(data, src_addr).unwrap();
    }
}
```

## 3. 嵌入式开发

### 基本嵌入式程序
```rust
#![no_std]
#![no_main]

use cortex_m_rt::entry;
use panic_halt as _;
use stm32f1xx_hal as hal;

#[entry]
fn main() -> ! {
    let dp = hal::pac::Peripherals::take().unwrap();
    let mut rcc = dp.RCC.constrain();
    let mut gpioc = dp.GPIOC.split(&mut rcc.apb2);
    
    let mut led = gpioc.pc13.into_push_pull_output(&mut gpioc.crh);
    
    loop {
        led.set_high().unwrap();
        cortex_m::asm::delay(1_000_000);
        led.set_low().unwrap();
        cortex_m::asm::delay(1_000_000);
    }
}
```

## 4. WebAssembly

### 基本Wasm程序
```rust
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[no_mangle]
pub extern "C" fn subtract(a: i32, b: i32) -> i32 {
    a - b
}
```

---

**更新时间：2026-04-01**