#include <stdio.h>

// 1. 常量宏
#define PI 3.14159
#define MAX_SIZE 100
#define MESSAGE "Hello, World!"

// 2. 带参数的宏
#define SQUARE(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

// 3. 多行宏
#define PRINT_NUMBERS(n) \
    do { \
        for (int i = 1; i <= n; i++) { \
            printf("%d ", i); \
        } \
        printf("\n"); \
    } while (0)

// 4. 条件编译
#define DEBUG 1

// 5. 调试宏
#if DEBUG
    #define LOG(fmt, ...) printf("[DEBUG] " fmt "\n", ##__VA_ARGS__)
#else
    #define LOG(fmt, ...) 
#endif

// 6. 平台检测
#ifdef _WIN32
    #define OS_NAME "Windows"
#elif __linux__
    #define OS_NAME "Linux"
#elif __APPLE__
    #define OS_NAME "Mac"
#else
    #define OS_NAME "Unknown"
#endif

// 7. 版本控制
#define VERSION_MAJOR 1
#define VERSION_MINOR 0
#define VERSION_PATCH 0

#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)
#define VERSION STR(VERSION_MAJOR) "." STR(VERSION_MINOR) "." STR(VERSION_PATCH)

int main() {
    // 1. 常量宏
    printf("=== 常量宏 ===\n");
    printf("PI = %f\n", PI);
    printf("MAX_SIZE = %d\n", MAX_SIZE);
    printf("MESSAGE = %s\n", MESSAGE);
    
    // 2. 带参数的宏
    printf("\n=== 带参数的宏 ===\n");
    printf("SQUARE(5) = %d\n", SQUARE(5));
    printf("MAX(10, 20) = %d\n", MAX(10, 20));
    printf("MIN(10, 20) = %d\n", MIN(10, 20));
    
    // 3. 多行宏
    printf("\n=== 多行宏 ===\n");
    PRINT_NUMBERS(5);
    
    // 4. 条件编译
    printf("\n=== 条件编译 ===\n");
    #ifdef DEBUG
        printf("Debug mode is enabled\n");
    #else
        printf("Debug mode is disabled\n");
    #endif
    
    // 条件编译示例
    #ifdef DEBUG
        printf("Debug mode is enabled\n");
    #else
        printf("Debug mode is disabled\n");
    #endif
    
    // 5. 预定义宏
    printf("\n=== 预定义宏 ===\n");
    printf("Line: %d\n", __LINE__);
    printf("File: %s\n", __FILE__);
    printf("Date: %s\n", __DATE__);
    printf("Time: %s\n", __TIME__);
    #ifdef __STDC__
        printf("ANSI C standard\n");
    #endif
    
    // 6. 调试宏
    printf("\n=== 调试宏 ===\n");
    int x = 10;
    LOG("x = %d", x);
    
    // 7. 平台检测
    printf("\n=== 平台检测 ===\n");
    printf("Operating system: %s\n", OS_NAME);
    
    // 8. 版本控制
    printf("\n=== 版本控制 ===\n");
    printf("Version: %s\n", VERSION);
    
    return 0;
}