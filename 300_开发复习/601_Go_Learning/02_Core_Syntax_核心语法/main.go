package main

import "fmt"

func main() {
    // 1. 运算符与表达式
    fmt.Println("=== 运算符与表达式 ===")
    
    a := 10
    b := 3
    
    fmt.Printf("a + b = %d\n", a + b)
    fmt.Printf("a - b = %d\n", a - b)
    fmt.Printf("a * b = %d\n", a * b)
    fmt.Printf("a / b = %d\n", a / b)
    fmt.Printf("a %% b = %d\n", a % b)
    
    // 比较运算符
    fmt.Printf("\n=== 比较运算符 ===")
    fmt.Printf("a == b = %t\n", a == b)
    fmt.Printf("a != b = %t\n", a != b)
    fmt.Printf("a > b = %t\n", a > b)
    fmt.Printf("a < b = %t\n", a < b)
    fmt.Printf("a >= b = %t\n", a >= b)
    fmt.Printf("a <= b = %t\n", a <= b)
    
    // 逻辑运算符
    fmt.Printf("\n=== 逻辑运算符 ===")
    c := true
    d := false
    
    fmt.Printf("c && d = %t\n", c && d)
    fmt.Printf("c || d = %t\n", c || d)
    fmt.Printf("!c = %t\n", !c)
    
    // 2. 控制流
    fmt.Println("\n=== 控制流 ===")
    
    // if语句
    if a > b {
        fmt.Println("a is greater than b")
    } else {
        fmt.Println("a is less than or equal to b")
    }
    
    // for循环
    for i := 0; i < 5; i++ {
        fmt.Printf("i = %d\n", i)
    }
    
    // while循环
    j := 0
    for j < 5 {
        fmt.Printf("j = %d\n", j)
        j++
    }
    
    // switch语句
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
    
    // 3. 函数
    fmt.Println("\n=== 函数 ===")
    
    result := add(2, 3)
    fmt.Printf("add(2, 3) = %d\n", result)
    
    printName("Alice")
    
    result, err := divide(10, 2)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    fmt.Printf("divide(10, 2) = %d\n", result)
}

func add(x, y int) int {
    return x + y
}

func printName(name string) {
    fmt.Printf("Name: %s\n", name)
}

func divide(x, y int) (int, error) {
    if y == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return x / y, nil
}