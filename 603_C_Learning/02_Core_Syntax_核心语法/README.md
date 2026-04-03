# 核心语法

## 1. 运算符与表达式

### 算术运算符
```c
#include <stdio.h>

int main() {
    int a = 10, b = 3;
    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    printf("a / b = %d\n", a / b);
    printf("a %% b = %d\n", a % b);
    return 0;
}
```

### 关系运算符
```c
#include <stdio.h>

int main() {
    int a = 10, b = 3;
    printf("a > b: %d\n", a > b);
    printf("a < b: %d\n", a < b);
    printf("a == b: %d\n", a == b);
    printf("a != b: %d\n", a != b);
    printf("a >= b: %d\n", a >= b);
    printf("a <= b: %d\n", a <= b);
    return 0;
}
```

### 逻辑运算符
```c
#include <stdio.h>

int main() {
    int a = 1, b = 0;
    printf("a && b: %d\n", a && b);
    printf("a || b: %d\n", a || b);
    printf("!a: %d\n", !a);
    return 0;
}
```

## 2. 控制流

### if语句
```c
#include <stdio.h>

int main() {
    int age = 18;
    if (age >= 18) {
        printf("You are an adult\n");
    } else {
        printf("You are a minor\n");
    }
    return 0;
}
```

### for循环
```c
#include <stdio.h>

int main() {
    for (int i = 0; i < 5; i++) {
        printf("i = %d\n", i);
    }
    return 0;
}
```

### while循环
```c
#include <stdio.h>

int main() {
    int i = 0;
    while (i < 5) {
        printf("i = %d\n", i);
        i++;
    }
    return 0;
}
```

### switch语句
```c
#include <stdio.h>

int main() {
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
    return 0;
}
```

## 3. 函数

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

### 函数参数
```c
#include <stdio.h>

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
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(x, y);
    printf("After swap (value): x = %d, y = %d\n", x, y);
    swap_ptr(&x, &y);
    printf("After swap (pointer): x = %d, y = %d\n", x, y);
    return 0;
}
```

## 4. 指针

### 指针基础
```c
#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;
    printf("Value of a: %d\n", a);
    printf("Address of a: %p\n", &a);
    printf("Value of p: %p\n", p);
    printf("Value pointed by p: %d\n", *p);
    return 0;
}
```

### 指针与数组
```c
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p = arr;
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d, *(p + %d) = %d\n", i, arr[i], i, *(p + i));
    }
    return 0;
}
```

---

**更新时间：2026-04-04**