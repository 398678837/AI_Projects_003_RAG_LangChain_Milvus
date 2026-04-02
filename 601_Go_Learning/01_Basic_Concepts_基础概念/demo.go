package main

import (
    "fmt"
    "math"
)

func main() {
    // 1. 变量声明
    var name string = "Go"
    var age int = 10
    var isGood bool = true
    
    fmt.Println("Name:", name)
    fmt.Println("Age:", age)
    fmt.Println("IsGood:", isGood)
    
    // 2. 类型推断
    var language = "Go"
    fmt.Println("Language:", language)
    
    // 3. 短变量声明
    version := 1.22
    fmt.Println("Version:", version)
    
    // 4. 常量
    const PI = 3.14159
    fmt.Println("PI:", PI)
    
    // 5. 数据类型
    var i int = 100
    var f float64 = 3.14
    var s string = "Hello"
    var b bool = true
    
    fmt.Printf("Type of i: %T\n", i)
    fmt.Printf("Type of f: %T\n", f)
    fmt.Printf("Type of s: %T\n", s)
    fmt.Printf("Type of b: %T\n", b)
    
    // 6. 类型转换
    var x int = 10
    var y float64 = float64(x)
    fmt.Println("x:", x, "y:", y)
    
    // 7. 数学运算
    a := 10
    b1 := 3
    fmt.Println("a + b =", a+b1)
    fmt.Println("a - b =", a-b1)
    fmt.Println("a * b =", a*b1)
    fmt.Println("a / b =", a/b1)
    fmt.Println("a % b =", a%b1)
    
    // 8. 数学函数
    fmt.Println("sqrt(16) =", math.Sqrt(16))
    fmt.Println("sin(π/2) =", math.Sin(math.Pi/2))
    fmt.Println("cos(π) =", math.Cos(math.Pi))
    
    // 9. 字符串操作
    str := "Hello, Go!"
    fmt.Println("Length of str:", len(str))
    fmt.Println("Substring:", str[0:5])
    fmt.Println("Concatenation:", str+" Welcome!")
    
    // 10. 格式化输出
    fmt.Printf("%d + %d = %d\n", a, b1, a+b1)
    fmt.Printf("%f\n", math.Pi)
    fmt.Printf("%.2f\n", math.Pi)
    fmt.Printf("%s\n", str)
    fmt.Printf("%v\n", str)
    fmt.Printf("%#v\n", str)
}