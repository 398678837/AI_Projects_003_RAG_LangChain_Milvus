# 基础概念

## 1. C语言简介

C语言是一种通用的、过程式的计算机编程语言，广泛用于系统软件和应用软件的开发。C语言的设计目标是提供一种能以简易的方式编译、处理低级存储器、产生少量的机器码以及不需要任何运行环境支持便能运行的编程语言。

### 特点
- 高效、灵活
- 可移植性强
- 功能丰富
- 表达能力强

## 2. 开发环境搭建

### 安装GCC
```bash
# Ubuntu/Debian
sudo apt-get install gcc

# CentOS/RHEL
sudo yum install gcc

# macOS
brew install gcc
```

### 验证安装
```bash
gcc --version
```

## 3. 第一个C程序

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### 编译运行
```bash
gcc hello.c -o hello
./hello
```

## 4. 变量与常量

### 变量声明
```c
int age = 25;
float height = 1.75;
char gender = 'M';
```

### 常量声明
```c
const int MAX_AGE = 100;
#define PI 3.14159
```

## 5. 数据类型

### 基本类型
- 整型：int, short, long, long long
- 浮点型：float, double
- 字符型：char
- 布尔型：_Bool

### 复合类型
- 数组：int arr[10];
- 结构体：struct Person { ... };
- 共用体：union Data { ... };
- 枚举：enum Color { ... };

---

**更新时间：2026-04-01**