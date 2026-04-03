# 字符串

## 1. 字符串基础

### 字符串声明
```go
package main

import "fmt"

func main() {
    // 字符串声明
    var str string
    
    // 字符串初始化
    str = "Hello, World!"
    
    // 字符串输出
    fmt.Printf("String: %s\n", str)
}
```

### 字符串初始化
```go
package main

import "fmt"

func main() {
    // 字符串初始化
    str := "Hello, World!"
    
    // 字符串输出
    fmt.Printf("String: %s\n", str)
}
```

### 字符串长度
```go
package main

import "fmt"

func main() {
    // 字符串初始化
    str := "Hello, World!"
    
    // 字符串长度
    fmt.Printf("String length: %d\n", len(str))
}
```

## 2. 字符串操作

### 字符串拼接
```go
package main

import "fmt"

func main() {
    // 字符串初始化
    str1 := "Hello, "
    str2 := "World!"
    
    // 字符串拼接
    str3 := str1 + str2
    
    // 字符串输出
    fmt.Printf("String: %s\n", str3)
}
```

### 字符串截取
```go
package main

import "fmt"

func main() {
    // 字符串初始化
    str := "Hello, World!"
    
    // 字符串截取
    substr := str[0:5]
    
    // 字符串输出
    fmt.Printf("Substring: %s\n", substr)
}
```

### 字符串查找
```go
package main

import "fmt"
import "strings"

func main() {
    // 字符串初始化
    str := "Hello, World!"
    
    // 字符串查找
    index := strings.Index(str, "World")
    
    // 字符串输出
    fmt.Printf("Index: %d\n", index)
}
```

### 字符串替换
```go
package main

import "fmt"
import "strings"

func main() {
    // 字符串初始化
    str := "Hello, World!"
    
    // 字符串替换
    newStr := strings.Replace(str, "World", "Go", -1)
    
    // 字符串输出
    fmt.Printf("New string: %s\n", newStr)
}
```

### 字符串分割
```go
package main

import "fmt"
import "strings"

func main() {
    // 字符串初始化
    str := "Hello, World!"
    
    // 字符串分割
    parts := strings.Split(str, ", ")
    
    // 字符串输出
    for i := 0; i < len(parts); i++ {
        fmt.Printf("Part %d: %s\n", i, parts[i])
    }
}
```

## 3. 字符串格式化

### 格式化输出
```go
package main

import "fmt"

func main() {
    // 字符串初始化
    str := "Hello, World!"
    
    // 格式化输出
    fmt.Printf("String: %s\n", str)
    fmt.Printf("String length: %d\n", len(str))
    fmt.Printf("First character: %c\n", str[0])
}
```

### 格式化输入
```go
package main

import "fmt"

func main() {
    // 字符串初始化
    var str string
    
    // 格式化输入
    fmt.Scanf("%s", &str)
    
    // 字符串输出
    fmt.Printf("String: %s\n", str)
}
```

---

**更新时间：2026-04-01**