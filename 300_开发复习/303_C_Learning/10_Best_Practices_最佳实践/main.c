#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdint.h>

// 1. 代码规范示例

// 常量定义
#define MAX_SIZE 100

// 结构体定义
typedef struct {
    char name[50];
    int age;
    float height;
} Person;

// 函数声明
void print_person(Person p);
void safe_strcpy(char *dest, const char *src, size_t dest_size);
int *create_array(size_t size);
void free_array(int **arr);
int read_int(const char *prompt, int *value);

// 2. 内存管理示例

// 安全的字符串复制
void safe_strcpy(char *dest, const char *src, size_t dest_size) {
    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';
}

// 创建数组
int *create_array(size_t size) {
    int *arr = (int *)malloc(size * sizeof(int));
    if (arr == NULL) {
        return NULL;
    }
    return arr;
}

// 释放数组
void free_array(int **arr) {
    if (*arr != NULL) {
        free(*arr);
        *arr = NULL;
    }
}

// 3. 错误处理示例

// 读取整数
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

// 4. 性能优化示例

// 计算斐波那契数列（递归）
int fibonacci_recursive(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

// 计算斐波那契数列（迭代）
int fibonacci_iterative(int n) {
    if (n <= 1) {
        return n;
    }
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

// 5. 安全性示例

// 安全的格式化输出
void safe_printf(const char *format, ...) {
    // 这里只是一个示例，实际实现需要使用va_list
    printf("[SAFE] ");
    printf(format);
}

// 6. 可移植性示例

// 字节序检测
void check_endianness() {
    union {
        uint32_t i;
        char c[4];
    } u;
    u.i = 0x12345678;
    if (u.c[0] == 0x78) {
        printf("Little-endian\n");
    } else {
        printf("Big-endian\n");
    }
}

// 7. 测试示例

// 测试函数
void test_safe_strcpy() {
    char dest[10];
    safe_strcpy(dest, "Hello, World!", sizeof(dest));
    printf("safe_strcpy test: %s\n", dest);
}

void test_create_array() {
    int *arr = create_array(5);
    if (arr != NULL) {
        for (int i = 0; i < 5; i++) {
            arr[i] = i + 1;
        }
        printf("create_array test: ");
        for (int i = 0; i < 5; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
        free_array(&arr);
        assert(arr == NULL);
    }
}

int main() {
    // 1. 代码规范
    printf("=== 代码规范 ===\n");
    
    Person p = {"Alice", 25, 1.65};
    print_person(p);
    
    // 2. 内存管理
    printf("\n=== 内存管理 ===\n");
    
    test_safe_strcpy();
    test_create_array();
    
    // 3. 错误处理
    printf("\n=== 错误处理 ===\n");
    
    int value;
    if (read_int("Enter a number: ", &value) == 0) {
        printf("You entered: %d\n", value);
    } else {
        printf("Invalid input\n");
    }
    
    // 4. 性能优化
    printf("\n=== 性能优化 ===\n");
    
    printf("Fibonacci(10) recursive: %d\n", fibonacci_recursive(10));
    printf("Fibonacci(10) iterative: %d\n", fibonacci_iterative(10));
    
    // 5. 安全性
    printf("\n=== 安全性 ===\n");
    
    safe_printf("Hello, %s!\n", "World");
    
    // 6. 可移植性
    printf("\n=== 可移植性 ===\n");
    
    check_endianness();
    
    // 7. 最佳实践总结
    printf("\n=== 最佳实践总结 ===\n");
    printf("1. 遵循命名规范\n");
    printf("2. 合理使用内存\n");
    printf("3. 正确处理错误\n");
    printf("4. 优化性能\n");
    printf("5. 确保安全性\n");
    printf("6. 考虑可移植性\n");
    printf("7. 编写测试\n");
    
    return 0;
}

// 函数定义
void print_person(Person p) {
    printf("Name: %s\n", p.name);
    printf("Age: %d\n", p.age);
    printf("Height: %.2f\n", p.height);
}