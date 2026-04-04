# 函数

## 1. 函数基础

### 函数定义与调用
```c
#include <stdio.h>

// 函数定义
int add(int a, int b) {
    return a + b;
}

int main() {
    // 函数调用
    int result = add(5, 3);
    printf("5 + 3 = %d\n", result);
    return 0;
}
```

### 函数声明
```c
#include <stdio.h>

// 函数声明
int add(int a, int b);

int main() {
    // 函数调用
    int result = add(5, 3);
    printf("5 + 3 = %d\n", result);
    return 0;
}

// 函数定义
int add(int a, int b) {
    return a + b;
}
```

### 函数参数
```c
#include <stdio.h>

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

int main() {
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(x, y);
    printf("After swap (value): x = %d, y = %d\n", x, y);
    swap_ptr(&x, &y);
    printf("After swap (pointer): x = %d, y = %d\n", x, y);
    return 0;
}
```

## 2. 函数高级特性

### 函数返回值
```c
#include <stdio.h>

// 返回整数
int add(int a, int b) {
    return a + b;
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

int main() {
    int result = add(5, 3);
    printf("5 + 3 = %d\n", result);
    
    float quotient = divide(5, 2);
    printf("5 / 2 = %f\n", quotient);
    
    int *arr = create_array(5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}
```

### 函数递归
```c
#include <stdio.h>

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

int main() {
    printf("5! = %d\n", factorial(5));
    
    printf("Fibonacci sequence: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
    
    return 0;
}
```

### 函数指针
```c
#include <stdio.h>

// 函数定义
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    return a / b;
}

int main() {
    // 函数指针
    int (*operation)(int, int);
    
    operation = add;
    printf("5 + 3 = %d\n", operation(5, 3));
    
    operation = subtract;
    printf("5 - 3 = %d\n", operation(5, 3));
    
    operation = multiply;
    printf("5 * 3 = %d\n", operation(5, 3));
    
    operation = divide;
    printf("6 / 3 = %d\n", operation(6, 3));
    
    return 0;
}
```

## 3. 函数参数高级特性

### 可变参数
```c
#include <stdio.h>
#include <stdarg.h>

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

int main() {
    printf("1 + 2 = %d\n", sum(2, 1, 2));
    printf("1 + 2 + 3 = %d\n", sum(3, 1, 2, 3));
    printf("1 + 2 + 3 + 4 = %d\n", sum(4, 1, 2, 3, 4));
    return 0;
}
```

### 数组作为函数参数
```c
#include <stdio.h>

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

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    printf("原始数组: ");
    print_array(arr, size);
    
    square_array(arr, size);
    
    printf("平方后的数组: ");
    print_array(arr, size);
    
    return 0;
}
```

## 4. 函数最佳实践

### 函数设计原则
```c
// 1. 函数应该只做一件事
// 2. 函数名应该清晰表达其功能
// 3. 函数参数应该尽可能少
// 4. 函数应该返回有意义的值
// 5. 函数应该处理错误情况
```

### 函数示例
```c
#include <stdio.h>
#include <stdbool.h>

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
    printf("17 is prime: %d\n", is_prime(17));
    printf("18 is prime: %d\n", is_prime(18));
    
    printf("gcd(12, 18) = %d\n", gcd(12, 18));
    printf("lcm(12, 18) = %d\n", lcm(12, 18));
    
    return 0;
}
```

---

**更新时间：2026-04-04**