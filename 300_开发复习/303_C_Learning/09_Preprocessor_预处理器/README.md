# 预处理器

## 1. 预处理器基础

### 预处理器简介

C预处理器是在编译之前运行的程序，它处理以`#`开头的指令。预处理器的主要功能包括：

1. **文件包含**：将其他文件的内容包含到当前文件中
2. **宏定义**：定义常量和宏函数
3. **条件编译**：根据条件决定哪些代码被编译
4. **行控制**：控制源代码的行号和文件名

### 预处理器指令

预处理器指令以`#`开头，并且必须是一行的第一个非空白字符。常见的预处理器指令包括：

| 指令 | 描述 |
|------|------|
| `#include` | 包含头文件 |
| `#define` | 定义宏 |
| `#undef` | 取消宏定义 |
| `#if` | 条件编译开始 |
| `#ifdef` | 如果宏已定义则编译 |
| `#ifndef` | 如果宏未定义则编译 |
| `#else` | 条件编译的否则部分 |
| `#elif` | 条件编译的 else if 部分 |
| `#endif` | 条件编译结束 |
| `#pragma` | 特定于编译器的指令 |

## 2. 宏定义

### 常量宏

常量宏用于定义常量值，通常使用大写字母表示。

```c
#include <stdio.h>

// 定义常量宏
#define PI 3.14159
#define MAX_SIZE 100
#define MESSAGE "Hello, World!"

int main() {
    printf("PI = %f\n", PI);
    printf("MAX_SIZE = %d\n", MAX_SIZE);
    printf("MESSAGE = %s\n", MESSAGE);
    return 0;
}
```

### 带参数的宏

带参数的宏类似于函数，但在编译前被展开。

```c
#include <stdio.h>

// 定义带参数的宏
#define SQUARE(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int main() {
    printf("SQUARE(5) = %d\n", SQUARE(5));
    printf("MAX(10, 20) = %d\n", MAX(10, 20));
    printf("MIN(10, 20) = %d\n", MIN(10, 20));
    return 0;
}
```

### 多行宏

多行宏使用反斜杠`\`来表示续行。

```c
#include <stdio.h>

// 定义多行宏
#define PRINT_NUMBERS(n) \
    do { \
        for (int i = 1; i <= n; i++) { \
            printf("%d ", i); \
        } \
        printf("\n"); \
    } while (0)

int main() {
    PRINT_NUMBERS(5);
    return 0;
}
```

## 3. 条件编译

### 基本条件编译

条件编译允许根据条件决定哪些代码被编译。

```c
#include <stdio.h>

#define DEBUG 1

int main() {
    #ifdef DEBUG
        printf("Debug mode is enabled\n");
    #else
        printf("Debug mode is disabled\n");
    #endif
    return 0;
}
```

### 多条件编译

使用`#elif`可以实现多条件编译。

```c
#include <stdio.h>

#define OS "Windows"

int main() {
    #if defined(OS) && OS == "Windows"
        printf("Windows operating system\n");
    #elif defined(OS) && OS == "Linux"
        printf("Linux operating system\n");
    #elif defined(OS) && OS == "Mac"
        printf("Mac operating system\n");
    #else
        printf("Unknown operating system\n");
    #endif
    return 0;
}
```

### 防止头文件重复包含

使用`#ifndef`和`#define`可以防止头文件被重复包含。

```c
// header.h
#ifndef HEADER_H
#define HEADER_H

void function();

#endif // HEADER_H
```

## 4. 文件包含

### 包含标准库头文件

使用尖括号`<>`包含标准库头文件。

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```

### 包含用户头文件

使用双引号`""`包含用户头文件。

```c
#include "header.h"
#include "utils.h"
```

## 5. 预定义宏

C语言提供了一些预定义宏，它们在编译时被自动定义。

| 宏 | 描述 |
|------|------|
| `__LINE__` | 当前源文件的行号 |
| `__FILE__` | 当前源文件的文件名 |
| `__DATE__` | 编译日期 |
| `__TIME__` | 编译时间 |
| `__STDC__` | 如果编译器符合ANSI C标准，则为1 |

```c
#include <stdio.h>

int main() {
    printf("Line: %d\n", __LINE__);
    printf("File: %s\n", __FILE__);
    printf("Date: %s\n", __DATE__);
    printf("Time: %s\n", __TIME__);
    #ifdef __STDC__
        printf("ANSI C standard\n");
    #endif
    return 0;
}
```

## 6. 预处理器最佳实践

### 宏命名规范

- 常量宏使用大写字母和下划线
- 带参数的宏应该使用括号包围参数和整个表达式
- 复杂的宏应该使用`do-while(0)`结构

### 避免宏的副作用

```c
// 不好的宏定义
#define SQUARE(x) x * x

// 好的宏定义
#define SQUARE(x) ((x) * (x))
```

### 条件编译的使用

- 使用条件编译来处理不同平台的差异
- 使用条件编译来启用或禁用调试代码
- 使用条件编译来处理不同编译器的特性

## 7. 预处理器示例

### 调试宏

```c
#include <stdio.h>

#define DEBUG 1

#if DEBUG
    #define LOG(fmt, ...) printf("[DEBUG] " fmt "\n", ##__VA_ARGS__)
#else
    #define LOG(fmt, ...) 
#endif

int main() {
    int x = 10;
    LOG("x = %d", x);
    return 0;
}
```

### 平台检测

```c
#include <stdio.h>

#ifdef _WIN32
    #define OS_NAME "Windows"
#elif __linux__
    #define OS_NAME "Linux"
#elif __APPLE__
    #define OS_NAME "Mac"
#else
    #define OS_NAME "Unknown"
#endif

int main() {
    printf("Operating system: %s\n", OS_NAME);
    return 0;
}
```

### 版本控制

```c
#include <stdio.h>

#define VERSION_MAJOR 1
#define VERSION_MINOR 0
#define VERSION_PATCH 0

#define VERSION_STR(major, minor, patch) #major "." #minor "." #patch
#define VERSION VERSION_STR(VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)

int main() {
    printf("Version: %s\n", VERSION);
    return 0;
}
```

---

**更新时间：2026-04-04**