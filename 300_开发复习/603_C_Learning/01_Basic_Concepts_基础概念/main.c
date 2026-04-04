#include <stdio.h>

int main() {
    // 1. 第一个C程序
    printf("=== 第一个C程序 ===\n");
    printf("Hello, World!\n");
    
    // 2. 变量与常量
    printf("\n=== 变量与常量 ===\n");
    
    int age = 25;
    float height = 1.75;
    char gender = 'M';
    
    printf("Age: %d\n", age);
    printf("Height: %.2f\n", height);
    printf("Gender: %c\n", gender);
    
    const int MAX_AGE = 100;
    printf("Max Age: %d\n", MAX_AGE);
    
    // 3. 数据类型
    printf("\n=== 数据类型 ===\n");
    
    int i = 10;
    short s = 20;
    long l = 30;
    long long ll = 40;
    float f = 3.14;
    double d = 3.14159;
    char c = 'A';
    _Bool b = 1;
    
    printf("int: %d\n", i);
    printf("short: %d\n", s);
    printf("long: %ld\n", l);
    printf("long long: %lld\n", ll);
    printf("float: %.2f\n", f);
    printf("double: %.5f\n", d);
    printf("char: %c\n", c);
    printf("_Bool: %d\n", b);
    
    // 4. 运算符与表达式
    printf("\n=== 运算符与表达式 ===\n");
    
    int a = 10;
    int b1 = 3;
    
    printf("a + b = %d\n", a + b1);
    printf("a - b = %d\n", a - b1);
    printf("a * b = %d\n", a * b1);
    printf("a / b = %d\n", a / b1);
    printf("a %% b = %d\n", a % b1);
    
    // 5. 控制流
    printf("\n=== 控制流 ===\n");
    
    // if语句
    if (a > b1) {
        printf("a is greater than b\n");
    } else {
        printf("a is less than or equal to b\n");
    }
    
    // for循环
    for (int i = 0; i < 5; i++) {
        printf("i = %d\n", i);
    }
    
    // while循环
    int j = 0;
    while (j < 5) {
        printf("j = %d\n", j);
        j++;
    }
    
    // switch语句
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
            printf("Other day\n");
    }
    
    return 0;
}