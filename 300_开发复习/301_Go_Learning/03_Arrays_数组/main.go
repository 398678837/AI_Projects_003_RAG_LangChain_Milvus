package main

import "fmt"

func main() {
    // 1. 数组基础
    fmt.Println("=== 数组基础 ===")
    
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
    
    // 数组初始化
    arr2 := [5]int{1, 2, 3, 4, 5}
    
    // 数组遍历
    fmt.Printf("\n=== 数组初始化 ===")
    for i := 0; i < len(arr2); i++ {
        fmt.Printf("arr2[%d] = %d\n", i, arr2[i])
    }
    
    // 数组长度
    fmt.Printf("\n=== 数组长度 ===")
    fmt.Printf("Array length: %d\n", len(arr2))
    
    // 2. 多维数组
    fmt.Println("\n=== 多维数组 ===")
    
    // 二维数组初始化
    arr3 := [3][3]int{
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    }
    
    // 二维数组遍历
    fmt.Printf("\n=== 二维数组 ===")
    for i := 0; i < len(arr3); i++ {
        for j := 0; j < len(arr3[i]); j++ {
            fmt.Printf("arr3[%d][%d] = %d\n", i, j, arr3[i][j])
        }
    }
    
    // 三维数组初始化
    arr4 := [2][2][2]int{
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
    fmt.Printf("\n=== 三维数组 ===")
    for i := 0; i < len(arr4); i++ {
        for j := 0; j < len(arr4[i]); j++ {
            for k := 0; k < len(arr4[i][j]); k++ {
                fmt.Printf("arr4[%d][%d][%d] = %d\n", i, j, k, arr4[i][j][k])
            }
        }
    }
    
    // 3. 数组方法
    fmt.Println("\n=== 数组方法 ===")
    
    // 数组切片
    arr5 := [5]int{1, 2, 3, 4, 5}
    
    // 数组切片
    slice := arr5[1:3]
    
    // 数组切片遍历
    fmt.Printf("\n=== 数组切片 ===")
    for i := 0; i < len(slice); i++ {
        fmt.Printf("slice[%d] = %d\n", i, slice[i])
    }
    
    // 数组拷贝
    var arr6 [5]int
    copy(arr6[:], arr5[:])
    
    // 数组拷贝遍历
    fmt.Printf("\n=== 数组拷贝 ===")
    for i := 0; i < len(arr6); i++ {
        fmt.Printf("arr6[%d] = %d\n", i, arr6[i])
    }
}