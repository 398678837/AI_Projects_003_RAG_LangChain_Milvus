package main

import (
    "fmt"
    "errors"
    "os"
)

// 自定义错误
var ErrDivisionByZero = errors.New("division by zero")

func divide(x, y int) (int, error) {
    if y == 0 {
        return 0, ErrDivisionByZero
    }
    return x / y, nil
}

func readFile() error {
    return errors.New("file not found")
}

func processFile() error {
    if err := readFile(); err != nil {
        return fmt.Errorf("process file failed: %w", err)
    }
    return nil
}

func readFileWithName(filename string) ([]byte, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("read file %s failed: %w", filename, err)
    }
    return data, nil
}

func main() {
    // 1. 错误基础
    fmt.Println("=== 错误基础 ===")
    
    // 错误处理
    result, err := divide(10, 2)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    fmt.Printf("Result: %d\n", result)
    
    // 错误处理
    result, err = divide(10, 0)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    
    // 2. 自定义错误
    fmt.Println("\n=== 自定义错误 ===")
    
    result, err = divide(10, 0)
    if err != nil {
        if err == ErrDivisionByZero {
            fmt.Println("Custom error: division by zero")
        } else {
            fmt.Printf("Error: %v\n", err)
        }
    }
    
    // 3. 错误包装
    fmt.Println("\n=== 错误包装 ===")
    
    if err := processFile(); err != nil {
        fmt.Printf("Error: %v\n", err)
    }
    
    // 4. 错误处理最佳实践
    fmt.Println("\n=== 错误处理最佳实践 ===")
    
    data, err := readFileWithName("nonexistent.txt")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    } else {
        fmt.Printf("File content: %s\n", data)
    }
    
    // 5. 错误处理模式
    fmt.Println("\n=== 错误处理模式 ===")
    
    // 模式1: 立即返回错误
    data, err = os.ReadFile("nonexistent.txt")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    } else {
        fmt.Printf("File content: %s\n", data)
    }
    
    // 模式2: 延迟处理错误
    var err2 error
    data, err2 = os.ReadFile("nonexistent.txt")
    if err2 != nil {
        fmt.Printf("Error: %v\n", err2)
    } else {
        fmt.Printf("File content: %s\n", data)
    }
}