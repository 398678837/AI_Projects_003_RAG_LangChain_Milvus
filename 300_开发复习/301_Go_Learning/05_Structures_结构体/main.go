package main

import "fmt"

// 结构体定义
type Person struct {
    name string
    age int
    gender string
}

// 结构体定义
type Address struct {
    street string
    city string
    state string
    zip string
}

// 结构体定义
type PersonWithAddress struct {
    name string
    age int
    gender string
    address Address
}

// 结构体定义
type PersonWithAddressPtr struct {
    name string
    age int
    gender string
    address *Address
}

// 结构体方法定义
func (p Person) GetName() string {
    return p.name
}

// 结构体指针方法定义
func (p *Person) SetName(name string) {
    p.name = name
}

func main() {
    // 1. 结构体基础
    fmt.Println("=== 结构体基础 ===")
    
    // 结构体初始化
    var p Person
    p.name = "Alice"
    p.age = 25
    p.gender = "M"
    
    // 结构体输出
    fmt.Printf("Name: %s\n", p.name)
    fmt.Printf("Age: %d\n", p.age)
    fmt.Printf("Gender: %s\n", p.gender)
    
    // 结构体初始化
    p2 := Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体输出
    fmt.Printf("\n=== 结构体初始化 ===")
    fmt.Printf("Name: %s\n", p2.name)
    fmt.Printf("Age: %d\n", p2.age)
    fmt.Printf("Gender: %s\n", p2.gender)
    
    // 结构体指针
    p3 := &Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体输出
    fmt.Printf("\n=== 结构体指针 ===")
    fmt.Printf("Name: %s\n", p3.name)
    fmt.Printf("Age: %d\n", p3.age)
    fmt.Printf("Gender: %s\n", p3.gender)
    
    // 2. 结构体方法
    fmt.Println("\n=== 结构体方法 ===")
    
    // 结构体方法调用
    p4 := Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体方法调用
    fmt.Printf("\n=== 结构体方法定义 ===")
    fmt.Printf("Name: %s\n", p4.GetName())
    
    // 结构体指针方法调用
    p5 := &Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体指针方法调用
    fmt.Printf("\n=== 结构体指针方法定义 ===")
    p5.SetName("Bob")
    fmt.Printf("Name: %s\n", p5.name)
    
    // 3. 结构体嵌套
    fmt.Println("\n=== 结构体嵌套 ===")
    
    // 结构体嵌套
    p6 := PersonWithAddress{
        name: "Alice",
        age: 25,
        gender: "M",
        address: Address{
            street: "123 Main St",
            city: "New York",
            state: "NY",
            zip: "10001",
        },
    }
    
    // 结构体输出
    fmt.Printf("\n=== 结构体嵌套 ===")
    fmt.Printf("Name: %s\n", p6.name)
    fmt.Printf("Age: %d\n", p6.age)
    fmt.Printf("Gender: %s\n", p6.gender)
    fmt.Printf("Address: %s, %s, %s %s\n", p6.address.street, p6.address.city, p6.address.state, p6.address.zip)
    
    // 结构体指针嵌套
    p7 := PersonWithAddressPtr{
        name: "Alice",
        age: 25,
        gender: "M",
        address: &Address{
            street: "123 Main St",
            city: "New York",
            state: "NY",
            zip: "10001",
        },
    }
    
    // 结构体输出
    fmt.Printf("\n=== 结构体指针嵌套 ===")
    fmt.Printf("Name: %s\n", p7.name)
    fmt.Printf("Age: %d\n", p7.age)
    fmt.Printf("Gender: %s\n", p7.gender)
    fmt.Printf("Address: %s, %s, %s %s\n", p7.address.street, p7.address.city, p7.address.state, p7.address.zip)
}