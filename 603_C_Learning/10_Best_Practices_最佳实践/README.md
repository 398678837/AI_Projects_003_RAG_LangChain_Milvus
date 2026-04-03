# 最佳实践

## 1. 代码规范

### 命名规范

#### 变量命名
- **局部变量**：使用小写字母和下划线，如 `int counter;`
- **全局变量**：使用大写字母和下划线，如 `int GLOBAL_COUNTER;`
- **常量**：使用大写字母和下划线，如 `#define MAX_SIZE 100`
- **结构体**：使用驼峰命名法，首字母大写，如 `typedef struct { ... } Person;`
- **函数**：使用小写字母和下划线，如 `void print_person(Person p);`

### 代码风格

#### 缩进
- 使用4个空格进行缩进，而不是制表符
- 保持代码块的缩进一致

#### 括号
- 左括号放在行尾，右括号放在单独的一行
- 保持括号的对齐

```c
// 好的风格
if (condition) {
    // 代码
}

// 不好的风格
if (condition)
{
    // 代码
}
```

#### 注释
- 使用 `//` 进行单行注释
- 使用 `/* */` 进行多行注释
- 为函数、复杂逻辑和重要变量添加注释

### 代码组织

#### 文件组织
- 每个文件应该只包含相关的功能
- 头文件应该包含声明，源文件应该包含实现
- 使用 `#ifndef` 防止头文件重复包含

#### 函数组织
- 函数应该短小精悍，只做一件事
- 函数应该有清晰的输入和输出
- 函数应该有适当的注释

## 2. 性能优化

### 内存管理

#### 动态内存分配
- 只在必要时使用动态内存分配
- 及时释放不再使用的内存
- 避免内存泄漏

```c
// 好的实践
void function() {
    int *ptr = (int *)malloc(sizeof(int));
    if (ptr == NULL) {
        // 错误处理
        return;
    }
    // 使用ptr
    free(ptr);
}
```

#### 栈内存使用
- 对于小的、临时的数据，使用栈内存
- 避免在栈上分配大的数组

### 算法优化

#### 时间复杂度
- 选择合适的算法，考虑时间复杂度
- 避免嵌套循环，尤其是深层嵌套

#### 空间复杂度
- 考虑空间复杂度，避免使用过多的内存
- 对于大的数据集，考虑使用流式处理

### 编译器优化

#### 编译选项
- 使用 `-O2` 或 `-O3` 开启编译器优化
- 使用 `-Wall` 开启所有警告
- 使用 `-Werror` 将警告视为错误

## 3. 错误处理

### 错误检测

#### 函数返回值
- 函数应该返回错误码，而不是使用全局变量
- 对于可能失败的操作，检查返回值

```c
// 好的实践
int read_file(const char *filename, char *buffer, size_t size) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        return -1;
    }
    // 读取文件
    fclose(fp);
    return 0;
}
```

#### 错误报告
- 使用 `perror` 或自定义函数报告错误
- 错误消息应该清晰、具体

### 异常处理

#### 断言
- 使用 `assert` 检查程序的假设
- 只在调试时使用断言，生产环境中应该使用错误处理

```c
#include <assert.h>

void function(int x) {
    assert(x > 0);
    // 代码
}
```

## 4. 内存管理

### 内存分配

#### malloc vs calloc
- `malloc`：分配内存但不初始化
- `calloc`：分配内存并初始化为0

```c
// 分配10个整数的内存
int *ptr1 = (int *)malloc(10 * sizeof(int));
int *ptr2 = (int *)calloc(10, sizeof(int));
```

#### realloc
- 使用 `realloc` 调整已分配内存的大小
- 检查 `realloc` 的返回值

```c
int *ptr = (int *)malloc(10 * sizeof(int));
// 使用ptr
ptr = (int *)realloc(ptr, 20 * sizeof(int));
if (ptr == NULL) {
    // 错误处理
}
```

### 内存释放

#### free
- 使用 `free` 释放动态分配的内存
- 释放后将指针设置为 `NULL`，避免野指针

```c
int *ptr = (int *)malloc(sizeof(int));
// 使用ptr
free(ptr);
ptr = NULL; // 避免野指针
```

#### 内存泄漏检测
- 使用工具如 `valgrind` 检测内存泄漏
- 养成良好的内存管理习惯

## 5. 安全性

### 缓冲区溢出

#### 防止缓冲区溢出
- 使用 `strncpy` 而不是 `strcpy`
- 使用 `fgets` 而不是 `gets`
- 检查输入的长度

```c
// 好的实践
char buffer[100];
fgets(buffer, sizeof(buffer), stdin);
```

### 格式化字符串漏洞

#### 防止格式化字符串漏洞
- 不要将用户输入作为格式化字符串
- 使用固定的格式化字符串

```c
// 不好的实践
char user_input[100];
fgets(user_input, sizeof(user_input), stdin);
printf(user_input); // 危险！

// 好的实践
char user_input[100];
fgets(user_input, sizeof(user_input), stdin);
printf("%s", user_input); // 安全
```

### 指针安全

#### 防止野指针
- 初始化指针
- 释放内存后将指针设置为 `NULL`
- 避免使用未初始化的指针

## 6. 可移植性

### 平台差异

#### 数据类型大小
- 使用 `stdint.h` 中的固定大小类型
- 避免假设数据类型的大小

```c
#include <stdint.h>

int32_t x; // 32位整数
uint64_t y; // 64位无符号整数
```

#### 字节序
- 注意不同平台的字节序差异
- 使用 `ntohl` 和 `htonl` 进行网络字节序转换

### 编译器差异

#### 标准合规性
- 遵循C标准，避免使用编译器特定的扩展
- 使用条件编译处理编译器差异

```c
#ifdef _WIN32
    // Windows 特定代码
#elif __linux__
    // Linux 特定代码
#endif
```

## 7. 测试

### 单元测试

#### 测试框架
- 使用测试框架如 `Unity` 进行单元测试
- 为每个函数编写测试用例

#### 测试覆盖
- 确保测试覆盖所有代码路径
- 测试边界条件

### 集成测试

#### 系统测试
- 测试整个系统的功能
- 测试不同组件之间的交互

## 8. 最佳实践示例

### 示例1：安全的字符串复制

```c
#include <string.h>

void safe_strcpy(char *dest, const char *src, size_t dest_size) {
    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';
}
```

### 示例2：内存安全的函数

```c
#include <stdlib.h>

int *create_array(size_t size) {
    int *arr = (int *)malloc(size * sizeof(int));
    if (arr == NULL) {
        return NULL;
    }
    return arr;
}

void free_array(int **arr) {
    if (*arr != NULL) {
        free(*arr);
        *arr = NULL;
    }
}
```

### 示例3：错误处理

```c
#include <stdio.h>

int read_int(const char *prompt, int *value) {
    printf("%s", prompt);
    if (scanf("%d", value) != 1) {
        // 清除输入缓冲区
        int c;
        while ((c = getchar()) != '\n' && c != EOF) {
        }
        return -1;
    }
    return 0;
}
```

---

**更新时间：2026-04-04**