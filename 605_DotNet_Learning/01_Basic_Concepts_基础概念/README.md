# 基础概念

## 1. .NET语言简介

.NET是一种通用的、面向对象的编程语言，是C语言的扩展。.NET支持多种编程范式，包括面向过程、面向对象和泛型编程。.NET的设计目标是提供一种能以简易的方式编译、处理低级存储器、产生少量的机器码以及不需要任何运行环境支持便能运行的编程语言。

### 特点
- 高效、灵活
- 可移植性强
- 功能丰富
- 表达能力强
- 面向对象

## 2. 开发环境搭建

### 安装.NET SDK
```bash
# Ubuntu/Debian
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install -y apt-transport-https
sudo apt-get update
sudo apt-get install -y dotnet-sdk-5.0

# CentOS/RHEL
sudo dnf install dotnet-sdk-5.0

# macOS
brew install dotnet-sdk
```

### 验证安装
```bash
dotnet --version
```

## 3. 第一个.NET程序

```csharp
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
```

### 编译运行
```bash
dotnet new console -o hello
cd hello
dotnet run
```

## 4. 变量与常量

### 变量声明
```csharp
int age = 25;
float height = 1.75f;
char gender = 'M';
```

### 常量声明
```csharp
const int MAX_AGE = 100;
#define PI 3.14159
```

## 5. 数据类型

### 基本类型
- 整型：int, short, long, long long
- 浮点型：float, double, long double
- 字符型：char, wchar_t
- 布尔型：bool

### 复合类型
- 数组：int[] arr = new int[10];
- 结构体：struct Person { ... };
- 共用体：union Data { ... };
- 枚举：enum Color { ... };
- 类：class Person { ... };

---

**更新时间：2026-04-01**