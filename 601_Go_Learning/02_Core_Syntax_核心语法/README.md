# 核心语法

## 1. 运算符与表达式

### 算术运算符
```go
package main

import "fmt"

func main() {
    a := 10
    b := 3
    
    fmt.Printf("a + b = %d\n", a + b)
    fmt.Printf("a - b = %d\n", a - b)
    fmt.Printf("a * b = %d\n", a * b)
    fmt.Printf("a / b = %d\n", a / b)
    fmt.Printf("a %% b = %d\n", a % b)
}
```

### 比较运算符
```go
package main

import "fmt"

func main() {
    a := 10
    b := 3
    
    fmt.Printf("a == b = %t\n", a == b)
    fmt.Printf("a != b = %t\n", a != b)
    fmt.Printf("a > b = %t\n", a > b)
    fmt.Printf("a < b = %t\n", a < b)
    fmt.Printf("a >= b = %t\n", a >= b)
    fmt.Printf("a <= b = %t\n", a <= b)
}
```

### 逻辑运算符
```go
package main

import "fmt"

func main() {
    a := true
    b := false
    
    fmt.Printf("a && b = %t\n", a && b)
    fmt.Printf("a || b = %t\n", a || b)
    fmt.Printf("!a = %t\n", !a)
}
```

## 2. 控制流

### if语句
```go
package main

import "fmt"

func main() {
    a := 10
    b := 3
    
    if a > b {
        fmt.Println("a is greater than b")
    } else {
        fmt.Println("a is less than or equal to b")
    }
}
```

### for循环
```go
package main

import "fmt"

func main() {
    for i := 0; i < 5; i++ {
        fmt.Printf("i = %d\n", i)
    }
}
```

### while循环
```go
package main

import "fmt"

func main() {
    i := 0
    for i < 5 {
        fmt.Printf("i = %d\n", i)
        i++
    }
}
```

### switch语句
```go
package main

import "fmt"

func main() {
    day := 3
    switch day {
    case 1:
        fmt.Println("Monday")
    case 2:
        fmt.Println("Tuesday")
    case 3:
        fmt.Println("Wednesday")
    default:
        fmt.Println("Other day")
    }
}
```

## 3. 函数

### 函数定义
```go
package main

import "fmt"

func add(x, y int) int {
    return x + y
}

func main() {
    result := add(2, 3)
    fmt.Printf("add(2, 3) = %d\n", result)
}
```

### 函数参数
```go
package main

import "fmt"

func printName(name string) {
    fmt.Printf("Name: %s\n", name)
}

func main() {
    printName("Alice")
}
```

### 函数返回值
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
    fmt.Printf("divide(10, 2) = %d\n", result)
}
```

---

**更新时间：2026-04-01**