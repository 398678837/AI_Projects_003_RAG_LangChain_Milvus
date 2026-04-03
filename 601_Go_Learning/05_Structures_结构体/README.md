# 结构体

## 1. 结构体基础

### 结构体定义
```go
package main

import "fmt"

// 结构体定义
type Person struct {
    name string
    age int
    gender string
}

func main() {
    // 结构体初始化
    var p Person
    p.name = "Alice"
    p.age = 25
    p.gender = "M"
    
    // 结构体输出
    fmt.Printf("Name: %s\n", p.name)
    fmt.Printf("Age: %d\n", p.age)
    fmt.Printf("Gender: %s\n", p.gender)
}
```

### 结构体初始化
```go
package main

import "fmt"

// 结构体定义
type Person struct {
    name string
    age int
    gender string
}

func main() {
    // 结构体初始化
    p := Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体输出
    fmt.Printf("Name: %s\n", p.name)
    fmt.Printf("Age: %d\n", p.age)
    fmt.Printf("Gender: %s\n", p.gender)
}
```

### 结构体指针
```go
package main

import "fmt"

// 结构体定义
type Person struct {
    name string
    age int
    gender string
}

func main() {
    // 结构体初始化
    p := &Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体输出
    fmt.Printf("Name: %s\n", p.name)
    fmt.Printf("Age: %d\n", p.age)
    fmt.Printf("Gender: %s\n", p.gender)
}
```

## 2. 结构体方法

### 结构体方法定义
```go
package main

import "fmt"

// 结构体定义
type Person struct {
    name string
    age int
    gender string
}

// 结构体方法定义
func (p Person) GetName() string {
    return p.name
}

func main() {
    // 结构体初始化
    p := Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体方法调用
    fmt.Printf("Name: %s\n", p.GetName())
}
```

### 结构体指针方法
```go
package main

import "fmt"

// 结构体定义
type Person struct {
    name string
    age int
    gender string
}

// 结构体指针方法定义
func (p *Person) SetName(name string) {
    p.name = name
}

func main() {
    // 结构体初始化
    p := &Person{
        name: "Alice",
        age: 25,
        gender: "M",
    }
    
    // 结构体指针方法调用
    p.SetName("Bob")
    fmt.Printf("Name: %s\n", p.name)
}
```

## 3. 结构体嵌套

### 结构体嵌套
```go
package main

import "fmt"

// 结构体定义
type Address struct {
    street string
    city string
    state string
    zip string
}

// 结构体定义
type Person struct {
    name string
    age int
    gender string
    address Address
}

func main() {
    // 结构体初始化
    p := Person{
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
    fmt.Printf("Name: %s\n", p.name)
    fmt.Printf("Age: %d\n", p.age)
    fmt.Printf("Gender: %s\n", p.gender)
    fmt.Printf("Address: %s, %s, %s %s\n", p.address.street, p.address.city, p.address.state, p.address.zip)
}
```

### 结构体指针嵌套
```go
package main

import "fmt"

// 结构体定义
type Address struct {
    street string
    city string
    state string
    zip string
}

// 结构体定义
type Person struct {
    name string
    age int
    gender string
    address *Address
}

func main() {
    // 结构体初始化
    p := Person{
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
    fmt.Printf("Name: %s\n", p.name)
    fmt.Printf("Age: %d\n", p.age)
    fmt.Printf("Gender: %s\n", p.gender)
    fmt.Printf("Address: %s, %s, %s %s\n", p.address.street, p.address.city, p.address.state, p.address.zip)
}
```

---

**更新时间：2026-04-01**