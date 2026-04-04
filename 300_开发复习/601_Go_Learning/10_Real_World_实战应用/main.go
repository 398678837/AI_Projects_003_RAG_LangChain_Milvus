package main

import (
    "fmt"
    "os"
    "strconv"
    "log"
    "net/http"
    "flag"
    "time"
)

func getEnv(key, defaultValue string) string {
    if value := os.Getenv(key); value != "" {
        return value
    }
    return defaultValue
}

func getEnvAsInt(key string, defaultValue int) int {
    if value := os.Getenv(key); value != "" {
        if intValue, err := strconv.Atoi(value); err == nil {
            return intValue
        }
    }
    return defaultValue
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, World!")
}

func main() {
    // 1. 配置管理
    fmt.Println("=== 配置管理 ===")
    
    // 从环境变量获取配置
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }
    
    // 从环境变量获取配置（带默认值）
    host := getEnv("HOST", "localhost")
    maxConnections := getEnvAsInt("MAX_CONNECTIONS", 100)
    
    fmt.Printf("Host: %s, Port: %s, Max Connections: %d\n", host, port, maxConnections)
    
    // 2. 日志管理
    fmt.Println("\n=== 日志管理 ===")
    
    // 创建日志文件
    logFile, err := os.OpenFile("app.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        log.Fatal(err)
    }
    defer logFile.Close()
    
    // 设置日志输出
    log.SetOutput(logFile)
    log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)
    
    // 记录日志
    log.Println("Application started")
    log.Printf("Server listening on port %s\n", port)
    
    // 3. 命令行工具
    fmt.Println("\n=== 命令行工具 ===")
    
    // 定义命令行参数
    name := flag.String("name", "World", "Name to greet")
    age := flag.Int("age", 0, "Age of the person")
    
    // 解析命令行参数
    flag.Parse()
    
    // 使用命令行参数
    fmt.Printf("Hello, %s!\n", *name)
    if *age > 0 {
        fmt.Printf("You are %d years old.\n", *age)
    }
    
    // 4. Web服务器（后台运行）
    fmt.Println("\n=== Web服务器 ===")
    
    // 注册路由
    http.HandleFunc("/", helloHandler)
    
    // 启动服务器（后台运行）
    go func() {
        fmt.Printf("Server listening on %s:%s\n", host, port)
        if err := http.ListenAndServe(fmt.Sprintf(":%s", port), nil); err != nil {
            log.Printf("Error: %v\n", err)
        }
    }()
    
    // 等待一段时间，让服务器有时间启动
    time.Sleep(2 * time.Second)
    
    // 5. 模拟数据库操作
    fmt.Println("\n=== 数据库操作（模拟）===")
    fmt.Println("Connecting to database...")
    fmt.Println("Executing query: SELECT id, name FROM users")
    fmt.Println("Results:")
    fmt.Println("ID: 1, Name: Alice")
    fmt.Println("ID: 2, Name: Bob")
    fmt.Println("ID: 3, Name: Charlie")
    
    // 6. 实战最佳实践
    fmt.Println("\n=== 实战最佳实践 ===")
    fmt.Println("1. 代码组织: 按功能模块划分包")
    fmt.Println("2. 性能优化: 使用缓存, 减少内存分配")
    fmt.Println("3. 部署与监控: 容器化, CI/CD, 监控应用状态")
    
    // 保持程序运行
    fmt.Println("\nApplication running...")
    fmt.Println("Press Ctrl+C to exit")
    
    // 无限循环，保持程序运行
    select {}
}