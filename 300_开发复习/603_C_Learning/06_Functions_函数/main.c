#include <stdio.h>
#include <stdarg.h>
#include <stdbool.h>

// 函数声明
int add(int a, int b);
void swap(int a, int b);
void swap_ptr(int *a, int *b);
float divide(int a, int b);
int *create_array(int size);
int factorial(int n);
int fibonacci(int n);
int sum(int count, ...);
void print_array(int arr[], int size);
void square_array(int arr[], int size);
bool is_prime(int n);
int gcd(int a, int b);
int lcm(int a, int b);

// 函数定义
int add(int a, int b) {
    return a + b;
}

// 值传递
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swap: a = %d, b = %d\n", a, b);
}

// 指针传递
void swap_ptr(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 返回浮点数
float divide(int a, int b) {
    return (float)a / b;
}

// 返回指针
int *create_array(int size) {
    static int arr[10];
    for (int i = 0; i < size; i++) {
        arr[i] = i + 1;
    }
    return arr;
}

// 递归函数计算阶乘
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// 递归函数计算斐波那契数列
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// 函数定义
int multiply(int a, int b) {
    return a * b;
}

int divide_int(int a, int b) {
    return a / b;
}

// 可变参数函数
int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }
    
    va_end(args);
    return total;
}

// 数组作为参数
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// 修改数组
void square_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = arr[i] * arr[i];
    }
}

// 检查是否为素数
bool is_prime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

// 计算最大公约数
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// 计算最小公倍数
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    // 1. 函数基础
    printf("=== 函数基础 ===\n");
    
    // 函数定义与调用
    printf("\n=== 函数定义与调用 ===\n");
    int result = add(5, 3);
    printf("5 + 3 = %d\n", result);
    
    // 函数参数
    printf("\n=== 函数参数 ===\n");
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(x, y);
    printf("After swap (value): x = %d, y = %d\n", x, y);
    swap_ptr(&x, &y);
    printf("After swap (pointer): x = %d, y = %d\n", x, y);
    
    // 2. 函数高级特性
    printf("\n=== 函数高级特性 ===\n");
    
    // 函数返回值
    printf("\n=== 函数返回值 ===\n");
    float quotient = divide(5, 2);
    printf("5 / 2 = %f\n", quotient);
    
    int *arr = create_array(5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // 函数递归
    printf("\n=== 函数递归 ===\n");
    printf("5! = %d\n", factorial(5));
    
    printf("Fibonacci sequence: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
    
    // 函数指针
    printf("\n=== 函数指针 ===\n");
    // 函数指针
    int (*operation)(int, int);
    
    operation = add;
    printf("5 + 3 = %d\n", operation(5, 3));
    
    operation = multiply;
    printf("5 * 3 = %d\n", operation(5, 3));
    
    operation = divide_int;
    printf("6 / 3 = %d\n", operation(6, 3));
    
    // 3. 函数参数高级特性
    printf("\n=== 函数参数高级特性 ===\n");
    
    // 可变参数
    printf("\n=== 可变参数 ===\n");
    printf("1 + 2 = %d\n", sum(2, 1, 2));
    printf("1 + 2 + 3 = %d\n", sum(3, 1, 2, 3));
    printf("1 + 2 + 3 + 4 = %d\n", sum(4, 1, 2, 3, 4));
    
    // 数组作为函数参数
    printf("\n=== 数组作为函数参数 ===\n");
    int arr2[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr2) / sizeof(arr2[0]);
    
    printf("原始数组: ");
    print_array(arr2, size);
    
    square_array(arr2, size);
    
    printf("平方后的数组: ");
    print_array(arr2, size);
    
    // 4. 函数最佳实践
    printf("\n=== 函数最佳实践 ===\n");
    
    printf("17 is prime: %d\n", is_prime(17));
    printf("18 is prime: %d\n", is_prime(18));
    
    printf("gcd(12, 18) = %d\n", gcd(12, 18));
    printf("lcm(12, 18) = %d\n", lcm(12, 18));
    
    return 0;
}