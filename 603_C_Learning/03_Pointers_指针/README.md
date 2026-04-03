# 指针

## 1. 指针基础

### 指针定义与使用
```c
#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;  // 定义指针并指向a
    
    printf("变量a的值: %d\n", a);
    printf("变量a的地址: %p\n", &a);
    printf("指针p的值: %p\n", p);
    printf("指针p指向的值: %d\n", *p);
    
    *p = 20;  // 通过指针修改a的值
    printf("修改后a的值: %d\n", a);
    
    return 0;
}
```

### 空指针与野指针
```c
#include <stdio.h>

int main() {
    // 空指针
    int *p1 = NULL;
    printf("空指针: %p\n", p1);
    
    // 野指针（危险！）
    int *p2;
    // printf("野指针: %p\n", p2);  // 未初始化，值不确定
    
    return 0;
}
```

### 指针的指针
```c
#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;
    int **pp = &p;
    
    printf("a的值: %d\n", a);
    printf("*p的值: %d\n", *p);
    printf("**pp的值: %d\n", **pp);
    
    return 0;
}
```

## 2. 指针与数组

### 数组名作为指针
```c
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    
    printf("数组名作为指针: %p\n", arr);
    printf("第一个元素的地址: %p\n", &arr[0]);
    printf("第一个元素的值: %d\n", *arr);
    printf("第二个元素的值: %d\n", *(arr + 1));
    
    return 0;
}
```

### 指针算术
```c
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p = arr;
    
    for (int i = 0; i < 5; i++) {
        printf("*(p + %d) = %d\n", i, *(p + i));
    }
    
    return 0;
}
```

### 数组作为函数参数
```c
#include <stdio.h>

// 数组作为参数，实际上传递的是指针
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    print_array(arr, 5);
    return 0;
}
```

## 3. 指针与函数

### 指针作为函数参数
```c
#include <stdio.h>

// 通过指针修改实参的值
void increment(int *p) {
    (*p)++;
}

int main() {
    int a = 10;
    printf("修改前: %d\n", a);
    increment(&a);
    printf("修改后: %d\n", a);
    return 0;
}
```

### 函数返回指针
```c
#include <stdio.h>
#include <stdlib.h>

// 返回动态分配的内存
int *create_array(int size) {
    int *arr = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        arr[i] = i + 1;
    }
    return arr;
}

int main() {
    int *arr = create_array(5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    free(arr);  // 释放内存
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

int main() {
    // 函数指针
    int (*operation)(int, int);
    
    operation = add;
    printf("5 + 3 = %d\n", operation(5, 3));
    
    operation = subtract;
    printf("5 - 3 = %d\n", operation(5, 3));
    
    return 0;
}
```

## 4. 动态内存分配

### malloc与free
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // 分配内存
    int *p = (int *)malloc(5 * sizeof(int));
    if (p == NULL) {
        printf("内存分配失败\n");
        return 1;
    }
    
    // 使用内存
    for (int i = 0; i < 5; i++) {
        p[i] = i + 1;
    }
    
    // 打印值
    for (int i = 0; i < 5; i++) {
        printf("%d ", p[i]);
    }
    printf("\n");
    
    // 释放内存
    free(p);
    p = NULL;  // 避免野指针
    
    return 0;
}
```

### calloc与realloc
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // calloc分配并初始化
    int *p1 = (int *)calloc(5, sizeof(int));
    for (int i = 0; i < 5; i++) {
        printf("%d ", p1[i]);
    }
    printf("\n");
    
    // realloc重新分配
    int *p2 = (int *)realloc(p1, 10 * sizeof(int));
    for (int i = 5; i < 10; i++) {
        p2[i] = i + 1;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", p2[i]);
    }
    printf("\n");
    
    // 释放内存
    free(p2);
    
    return 0;
}
```

---

**更新时间：2026-04-04**