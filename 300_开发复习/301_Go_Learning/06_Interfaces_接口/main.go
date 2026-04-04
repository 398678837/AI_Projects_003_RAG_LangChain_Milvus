package main

import "fmt"

// 接口定义
type Shape interface {
    Area() float64
    Perimeter() float64
}

// 接口定义
type Drawer interface {
    Draw()
}

// 接口定义
type ShapeWithDraw interface {
    Area() float64
    Perimeter() float64
    Drawer
}

// 结构体定义
type Circle struct {
    radius float64
}

// 实现Shape接口
func (c Circle) Area() float64 {
    return 3.14 * c.radius * c.radius
}

func (c Circle) Perimeter() float64 {
    return 2 * 3.14 * c.radius
}

func (c Circle) Draw() {
    fmt.Println("Drawing a circle")
}

// 结构体定义
type Rectangle struct {
    width float64
    height float64
}

// 实现Shape接口
func (r Rectangle) Area() float64 {
    return r.width * r.height
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.width + r.height)
}

func (r Rectangle) Draw() {
    fmt.Println("Drawing a rectangle")
}

// 函数接受接口类型参数
func printShapeInfo(s Shape) {
    fmt.Printf("Area: %f\n", s.Area())
    fmt.Printf("Perimeter: %f\n", s.Perimeter())
}

func main() {
    // 1. 接口基础
    fmt.Println("=== 接口基础 ===")
    
    // 接口使用
    var s Shape
    s = Circle{radius: 5}
    fmt.Printf("Circle - Area: %f, Perimeter: %f\n", s.Area(), s.Perimeter())
    
    s = Rectangle{width: 10, height: 5}
    fmt.Printf("Rectangle - Area: %f, Perimeter: %f\n", s.Area(), s.Perimeter())
    
    // 2. 接口方法
    fmt.Println("\n=== 接口方法 ===")
    
    // 接口方法调用
    c := Circle{radius: 5}
    printShapeInfo(c)
    
    r := Rectangle{width: 10, height: 5}
    printShapeInfo(r)
    
    // 3. 接口类型断言
    fmt.Println("\n=== 接口类型断言 ===")
    
    var s2 Shape
    
    s2 = Circle{radius: 5}
    
    // 类型断言
    if c, ok := s2.(Circle); ok {
        fmt.Printf("Circle radius: %f\n", c.radius)
    }
    
    s2 = Rectangle{width: 10, height: 5}
    
    // 类型断言
    if r, ok := s2.(Rectangle); ok {
        fmt.Printf("Rectangle width: %f, height: %f\n", r.width, r.height)
    }
    
    // 4. 接口组合
    fmt.Println("\n=== 接口组合 ===")
    
    var s3 ShapeWithDraw
    s3 = Circle{radius: 5}
    fmt.Printf("Area: %f\n", s3.Area())
    fmt.Printf("Perimeter: %f\n", s3.Perimeter())
    s3.Draw()
    
    s3 = Rectangle{width: 10, height: 5}
    fmt.Printf("Area: %f\n", s3.Area())
    fmt.Printf("Perimeter: %f\n", s3.Perimeter())
    s3.Draw()
    
    // 5. 空接口
    fmt.Println("\n=== 空接口 ===")
    
    // 空接口可以接受任何类型
    var i interface{}
    
    i = 10
    fmt.Printf("Type: %T, Value: %v\n", i, i)
    
    i = "Hello"
    fmt.Printf("Type: %T, Value: %v\n", i, i)
    
    i = true
    fmt.Printf("Type: %T, Value: %v\n", i, i)
}