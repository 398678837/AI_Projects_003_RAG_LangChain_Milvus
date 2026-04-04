# 错误处理

## 1. 错误基础

### 错误类型
```go
package main

import "fmt"

func divide(x, y int) (int, error) {
    if y == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return x / y, nil
}

func main() {
    result, err := divide(10, 2)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    fmt.Printf("Result: %d\n", result)
}
```

### 错误处理
```go
package main

import "fmt"

func divide(x, y int) (int, error) {
    if y == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return x / y, nil
}

func main() {
    result, err := divide(10, 0)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    fmt.Printf("Result: %d\n", result)
}
```

### 自定义错误
```go
package main

import "fmt"
import "errors"

// 自定义错误
var ErrDivisionByZero = errors.New("division by zero")

func divide(x, y int) (int, error) {
    if y == 0 {
        return 0, ErrDivisionByZero
    }
    return x / y, nil
}

func main() {
    result, err := divide(10, 0)
    if err != nil {
        if err == ErrDivisionByZero {
            fmt.Println("Custom error: division by zero")
        } else {
            fmt.Printf("Error: %v\n", err)
        }
        return
    }
    fmt.Printf("Result: %d\n", result)
}
```

## 2. 错误包装

### 错误包装
```go
package main

import "fmt"
import "errors"

func readFile() error {
    return errors.New("file not found")
}

func processFile() error {
    if err := readFile(); err != nil {
        return fmt.Errorf("process file failed: %w", err)
    }
    return nil
}

func main() {
    if err := processFile(); err != nil {
        fmt.Printf("Error: %v\n", err)
    }
}
```

### 错误检查
```go
package main

import "fmt"
import "errors"

func readFile() error {
    return errors.New("file not found")
}

func processFile() error {
    if err := readFile(); err != nil {
        return fmt.Errorf("process file failed: %w", err)
    }
    return nil
}

func main() {
    if err := processFile(); err != nil {
        fmt.Printf("Error: %v\n", err)
        if errors.Is(err, errors.New("file not found")) {
            fmt.Println("File not found error")
        }
    }
}
```

## 3. 错误处理最佳实践

### 错误处理最佳实践
```go
package main

import "fmt"
import "os"

func readFile(filename string) ([]byte, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("read file %s failed: %w", filename, err)
    }
    return data, nil
}

func main() {
    data, err := readFile("nonexistent.txt")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    fmt.Printf("File content: %s\n", data)
}
```

### 错误处理模式
```go
package main

import "fmt"
import "os"

func main() {
    // 模式1: 立即返回错误
    data, err := os.ReadFile("nonexistent.txt")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    fmt.Printf("File content: %s\n", data)
    
    // 模式2: 延迟处理错误
    var err2 error
    data2, err2 := os.ReadFile("nonexistent.txt")
    if err2 != nil {
        fmt.Printf("Error: %v\n", err2)
        return
    }
    fmt.Printf("File content: %s\n", data2)
}
```

---

**更新时间：2026-04-04**