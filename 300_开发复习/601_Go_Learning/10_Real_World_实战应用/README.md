# 实战应用

## 1. 实战基础

### 项目结构
```go
// 典型的Go项目结构
// ├── cmd/
// │   └── app/
// │       └── main.go
// ├── internal/
// │   ├── config/
// │   ├── handler/
// │   ├── service/
// │   └── repository/
// ├── pkg/
// │   └── utils/
// ├── go.mod
// └── go.sum
```

### 配置管理
```go
package main

import "fmt"
import "os"
import "strconv"

func main() {
    // 从环境变量获取配置
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }
    
    // 从环境变量获取配置（带默认值）
    host := getEnv("HOST", "localhost")
    maxConnections := getEnvAsInt("MAX_CONNECTIONS", 100)
    
    fmt.Printf("Host: %s, Port: %s, Max Connections: %d\n", host, port, maxConnections)
}

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
```

### 日志管理
```go
package main

import "fmt"
import "log"
import "os"

func main() {
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
    log.Printf("Server listening on port %s\n", "8080")
    
    // 记录错误
    if err != nil {
        log.Printf("Error: %v\n", err)
    }
}
```

## 2. 实战应用

### Web服务器
```go
package main

import "fmt"
import "net/http"

func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, World!")
}

func main() {
    // 注册路由
    http.HandleFunc("/", helloHandler)
    
    // 启动服务器
    fmt.Println("Server listening on port 8080")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        fmt.Printf("Error: %v\n", err)
    }
}
```

### 数据库操作
```go
package main

import "fmt"
import "database/sql"
import _ "github.com/go-sql-driver/mysql"

func main() {
    // 连接数据库
    db, err := sql.Open("mysql", "user:password@tcp(localhost:3306)/dbname")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    defer db.Close()
    
    // 测试连接
    if err := db.Ping(); err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    
    // 查询数据
    rows, err := db.Query("SELECT id, name FROM users")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    defer rows.Close()
    
    for rows.Next() {
        var id int
        var name string
        if err := rows.Scan(&id, &name); err != nil {
            fmt.Printf("Error: %v\n", err)
            return
        }
        fmt.Printf("ID: %d, Name: %s\n", id, name)
    }
}
```

### 命令行工具
```go
package main

import "fmt"
import "flag"

func main() {
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
}
```

## 3. 实战最佳实践

### 代码组织
```go
// 良好的代码组织
// 1. 按功能模块划分包
// 2. 使用接口定义依赖
// 3. 保持函数简短
// 4. 使用错误处理
// 5. 编写测试
```

### 性能优化
```go
// 性能优化
// 1. 使用缓存
// 2. 减少内存分配
// 3. 使用并发
// 4. 优化数据库查询
// 5. 使用适当的数据结构
```

### 部署与监控
```go
// 部署与监控
// 1. 使用容器化
// 2. 配置CI/CD
// 3. 监控应用状态
// 4. 日志管理
// 5. 性能分析
```

---

**更新时间：2026-04-04**