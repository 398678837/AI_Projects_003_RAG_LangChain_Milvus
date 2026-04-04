package main

import (
    "fmt"
    "os"
    "time"
    "sync"
    "net"
    "net/http"
    "io/ioutil"
)

func main() {
    // 1. 标准库基础
    fmt.Println("=== 标准库基础 ===")
    
    // fmt包
    fmt.Println("\n=== fmt包 ===")
    fmt.Println("Hello, World!")
    fmt.Printf("Name: %s, Age: %d\n", "Alice", 25)
    
    // os包
    fmt.Println("\n=== os包 ===")
    // 获取环境变量
    home := os.Getenv("HOME")
    fmt.Printf("HOME: %s\n", home)
    
    // 设置环境变量
    os.Setenv("TEST", "value")
    fmt.Printf("TEST: %s\n", os.Getenv("TEST"))
    
    // 获取命令行参数
    args := os.Args
    fmt.Printf("Args: %v\n", args)
    
    // time包
    fmt.Println("\n=== time包 ===")
    // 获取当前时间
    now := time.Now()
    fmt.Printf("Now: %v\n", now)
    
    // 格式化时间
    fmt.Printf("Formatted: %s\n", now.Format("2006-01-02 15:04:05"))
    
    // 时间休眠
    time.Sleep(1 * time.Second)
    fmt.Println("After sleep")
    
    // 2. 集合包
    fmt.Println("\n=== 集合包 ===")
    
    // slice
    fmt.Println("\n=== slice ===")
    // 创建slice
    s := []int{1, 2, 3, 4, 5}
    fmt.Printf("Slice: %v\n", s)
    
    // 切片操作
    s2 := s[1:3]
    fmt.Printf("Slice 1:3: %v\n", s2)
    
    // 添加元素
    s = append(s, 6)
    fmt.Printf("After append: %v\n", s)
    
    // map
    fmt.Println("\n=== map ===")
    // 创建map
    m := make(map[string]int)
    m["Alice"] = 25
    m["Bob"] = 30
    
    // 访问元素
    fmt.Printf("Alice: %d\n", m["Alice"])
    
    // 遍历map
    for key, value := range m {
        fmt.Printf("%s: %d\n", key, value)
    }
    
    // sync包
    fmt.Println("\n=== sync包 ===")
    // 互斥锁
    var mu sync.Mutex
    var counter int
    
    // 等待组
    var wg sync.WaitGroup
    
    // 启动多个goroutine
    for i := 0; i < 1000; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            mu.Lock()
            defer mu.Unlock()
            counter++
        }()
    }
    
    wg.Wait()
    fmt.Printf("Counter: %d\n", counter)
    
    // 3. 网络包
    fmt.Println("\n=== 网络包 ===")
    
    // net包
    fmt.Println("\n=== net包 ===")
    // 解析域名
    addr, err := net.LookupIP("google.com")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    } else {
        for _, ip := range addr {
            fmt.Printf("IP: %v\n", ip)
        }
    }
    
    // http包
    fmt.Println("\n=== http包 ===")
    // 发送HTTP请求
    resp, err := http.Get("https://example.com")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    } else {
        defer resp.Body.Close()
        
        // 读取响应体
        body, err := ioutil.ReadAll(resp.Body)
        if err != nil {
            fmt.Printf("Error: %v\n", err)
        } else {
            fmt.Printf("Response length: %d bytes\n", len(body))
            fmt.Printf("Response: %s\n", body[:100])
        }
    }
}