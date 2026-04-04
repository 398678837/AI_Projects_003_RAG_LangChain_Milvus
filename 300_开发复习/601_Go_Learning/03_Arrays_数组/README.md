# 数组

## 1. 数组基础

### 数组声明
```go
package main

import "fmt"

func main() {
    // 数组声明
    var arr [5]int
    
    // 数组初始化
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    arr[3] = 4
    arr[4] = 5
    
    // 数组遍历
    for i := 0; i < len(arr); i++ {
        fmt.Printf("arr[%d] = %d\n", i, arr[i])
    }
}
```

### 数组初始化
```go
package main

import "fmt"

func main() {
    // 数组初始化
    arr := [5]int{1, 2, 3, 4, 5}
    
    // 数组遍历
    for i := 0; i < len(arr); i++ {
        fmt.Printf("arr[%d] = %d\n", i, arr[i])
    }
}
```

### 数组长度
```go
package main

import "fmt"

func main() {
    // 数组初始化
    arr := [5]int{1, 2, 3, 4, 5}
    
    // 数组长度
    fmt.Printf("Array length: %d\n", len(arr))
}
```

## 2. 多维数组

### 二维数组
```go
package main

import "fmt"

func main() {
    // 二维数组初始化
    arr := [3][3]int{
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    }
    
    // 二维数组遍历
    for i := 0; i < len(arr); i++ {
        for j := 0; j < len(arr[i]); j++ {
            fmt.Printf("arr[%d][%d] = %d\n", i, j, arr[i][j])
        }
    }
}
```

### 三维数组
```go
package main

import "fmt"

func main() {
    // 三维数组初始化
    arr := [2][2][2]int{
        {
            {1, 2},
            {3, 4},
        },
        {
            {5, 6},
            {7, 8},
        },
    }
    
    // 三维数组遍历
    for i := 0; i < len(arr); i++ {
        for j := 0; j < len(arr[i]); j++ {
            for k := 0; k < len(arr[i][j]); k++ {
                fmt.Printf("arr[%d][%d][%d] = %d\n", i, j, k, arr[i][j][k])
            }
        }
    }
}
```

## 3. 数组方法

### 数组切片
```go
package main

import "fmt"

func main() {
    // 数组初始化
    arr := [5]int{1, 2, 3, 4, 5}
    
    // 数组切片
    slice := arr[1:3]
    
    // 数组切片遍历
    for i := 0; i < len(slice); i++ {
        fmt.Printf("slice[%d] = %d\n", i, slice[i])
    }
}
```

### 数组拷贝
```go
package main

import "fmt"

func main() {
    // 数组初始化
    arr := [5]int{1, 2, 3, 4, 5}
    
    // 数组拷贝
    var arr2 [5]int
    copy(arr2[:], arr[:])
    
    // 数组拷贝遍历
    for i := 0; i < len(arr2); i++ {
        fmt.Printf("arr2[%d] = %d\n", i, arr2[i])
    }
}
```

---

**更新时间：2026-04-01**