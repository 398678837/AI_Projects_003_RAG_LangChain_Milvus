# 基础概念

## 1. Go语言简介

Go语言（又称Golang）是Google开发的一种静态强类型、编译型、并发型，并具有垃圾回收功能的编程语言。

### 特点
- 简洁、快速、安全
- 并行、有趣、开源
- 内存管理、数组安全、编译迅速

## 2. 开发环境搭建

### 安装Go
- 官方网站：https://golang.org/dl/
- 版本选择：建议使用最新稳定版

### 配置环境变量
```bash
# Linux/macOS
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin

# Windows
set GOPATH=%USERPROFILE%\go
set PATH=%PATH%;%GOPATH%\bin
```

### 验证安装
```bash
go version
go env
```

## 3. 第一个Go程序

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### 编译运行
```bash
go run hello.go
go build hello.go
./hello
```

## 4. 变量与常量

### 变量声明
```go
var name string = "Go"
var age int = 10
var isGood bool = true

// 类型推断
var name = "Go"

// 短变量声明
name := "Go"
```

### 常量声明
```go
const PI = 3.14159
const MAX_SIZE = 1024
```

## 5. 数据类型

### 基本类型
- 布尔型：bool
- 数值型：int, int8, int16, int32, int64, uint, uint8, uint16, uint32, uint64, uintptr, float32, float64, complex64, complex128
- 字符串：string

### 复合类型
- 数组：[n]T
- 切片：[]T
- 字典：map[K]V
- 结构体：struct
- 接口：interface

---

**更新时间：2026-04-01**