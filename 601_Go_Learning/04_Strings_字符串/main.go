package main

import (
    "fmt"
    "strings"
)

func main() {
    // 1. 字符串基础
    fmt.Println("=== 字符串基础 ===")
    
    // 字符串声明
    var str string
    
    // 字符串初始化
    str = "Hello, World!"
    
    // 字符串输出
    fmt.Printf("String: %s\n", str)
    
    // 字符串初始化
    str2 := "Hello, World!"
    
    // 字符串输出
    fmt.Printf("\n=== 字符串初始化 ===")
    fmt.Printf("String: %s\n", str2)
    
    // 字符串长度
    fmt.Printf("\n=== 字符串长度 ===")
    fmt.Printf("String length: %d\n", len(str2))
    
    // 2. 字符串操作
    fmt.Println("\n=== 字符串操作 ===")
    
    // 字符串拼接
    str3 := "Hello, "
    str4 := "World!"
    
    // 字符串拼接
    str5 := str3 + str4
    
    // 字符串输出
    fmt.Printf("\n=== 字符串拼接 ===")
    fmt.Printf("String: %s\n", str5)
    
    // 字符串截取
    str6 := "Hello, World!"
    
    // 字符串截取
    substr := str6[0:5]
    
    // 字符串输出
    fmt.Printf("\n=== 字符串截取 ===")
    fmt.Printf("Substring: %s\n", substr)
    
    // 字符串查找
    str7 := "Hello, World!"
    
    // 字符串查找
    index := strings.Index(str7, "World")
    
    // 字符串输出
    fmt.Printf("\n=== 字符串查找 ===")
    fmt.Printf("Index: %d\n", index)
    
    // 字符串替换
    str8 := "Hello, World!"
    
    // 字符串替换
    newStr := strings.Replace(str8, "World", "Go", -1)
    
    // 字符串输出
    fmt.Printf("\n=== 字符串替换 ===")
    fmt.Printf("New string: %s\n", newStr)
    
    // 字符串分割
    str9 := "Hello, World!"
    
    // 字符串分割
    parts := strings.Split(str9, ", ")
    
    // 字符串输出
    fmt.Printf("\n=== 字符串分割 ===")
    for i := 0; i < len(parts); i++ {
        fmt.Printf("Part %d: %s\n", i, parts[i])
    }
    
    // 3. 字符串格式化
    fmt.Println("\n=== 字符串格式化 ===")
    
    // 格式化输出
    str10 := "Hello, World!"
    
    // 格式化输出
    fmt.Printf("\n=== 格式化输出 ===")
    fmt.Printf("String: %s\n", str10)
    fmt.Printf("String length: %d\n", len(str10))
    fmt.Printf("First character: %c\n", str10[0])
    
    // 格式化输入
    fmt.Printf("\n=== 格式化输入 ===")
    var str11 string
    
    // 格式化输入
    fmt.Scanf("%s", &str11)
    
    // 字符串输出
    fmt.Printf("String: %s\n", str11)
}