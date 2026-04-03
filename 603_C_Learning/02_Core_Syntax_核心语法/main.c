#include <stdio.h>

// 函数定义
int add(int a, int b) {
    return a + b;
}

// 值传递
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

// 指针传递
void swap_ptr(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    // 1. 运算符与表达式
    printf("=== 运算符与表达式 ===\n");
    
    // 算术运算符
    int a = 10, b = 3;
    printf("\n=== 算术运算符 ===\n");
    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    printf("a / b = %d\n", a / b);
    printf("a %% b = %d\n", a % b);
    
    // 关系运算符
    printf("\n=== 关系运算符 ===\n");
    printf("a > b: %d\n", a > b);
    printf("a < b: %d\n", a < b);
    printf("a == b: %d\n", a == b);
    printf("a != b: %d\n", a != b);
    printf("a >= b: %d\n", a >= b);
    printf("a <= b: %d\n", a <= b);
    
    // 逻辑运算符
    printf("\n=== 逻辑运算符 ===\n");
    int c = 1, d = 0;
    printf("c && d: %d\n", c && d);
    printf("c || d: %d\n", c || d);
    printf("!c: %d\n", !c);
    
    // 2. 控制流
    printf("\n=== 控制流 ===\n");
    
    // if语句
    printf("\n=== if语句 ===\n");
    int age = 18;
    if (age >= 18) {
        printf("You are an adult\n");
    } else {
        printf("You are a minor\n");
    }
    
    // for循环
    printf("\n=== for循环 ===\n");
    for (int i = 0; i < 5; i++) {
        printf("i = %d\n", i);
    }
    
    // while循环
    printf("\n=== while循环 ===\n");
    int i = 0;
    while (i < 5) {
        printf("i = %d\n", i);
        i++;
    }
    
    // switch语句
    printf("\n=== switch语句 ===\n");
    int day = 3;
    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        default:
            printf("Invalid day\n");
    }
    
    // 3. 函数
    printf("\n=== 函数 ===\n");
    
    // 函数调用
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
    
    // 4. 指针
    printf("\n=== 指针 ===\n");
    
    // 指针基础
    printf("\n=== 指针基础 ===\n");
    int num = 10;
    int *p = &num;
    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", &num);
    printf("Value of p: %p\n", p);
    printf("Value pointed by p: %d\n", *p);
    
    // 指针与数组
    printf("\n=== 指针与数组 ===\n");
    int arr[] = {1, 2, 3, 4, 5};
    int *p_arr = arr;
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d, *(p_arr + %d) = %d\n", i, arr[i], i, *(p_arr + i));
    }
    
    return 0;
}