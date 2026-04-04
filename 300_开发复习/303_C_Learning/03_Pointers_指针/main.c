#include <stdio.h>
#include <stdlib.h>

// 数组作为参数，实际上传递的是指针
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// 通过指针修改实参的值
void increment(int *p) {
    (*p)++;
}

// 返回动态分配的内存
int *create_array(int size) {
    int *arr = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        arr[i] = i + 1;
    }
    return arr;
}

// 函数定义
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    // 1. 指针基础
    printf("=== 指针基础 ===\n");
    
    // 指针定义与使用
    printf("\n=== 指针定义与使用 ===\n");
    int a = 10;
    int *p = &a;  // 定义指针并指向a
    
    printf("变量a的值: %d\n", a);
    printf("变量a的地址: %p\n", &a);
    printf("指针p的值: %p\n", p);
    printf("指针p指向的值: %d\n", *p);
    
    *p = 20;  // 通过指针修改a的值
    printf("修改后a的值: %d\n", a);
    
    // 空指针与野指针
    printf("\n=== 空指针与野指针 ===\n");
    // 空指针
    int *p1 = NULL;
    printf("空指针: %p\n", p1);
    
    // 野指针（危险！）
    int *p2;
    // printf("野指针: %p\n", p2);  // 未初始化，值不确定
    
    // 指针的指针
    printf("\n=== 指针的指针 ===\n");
    int b = 10;
    int *p3 = &b;
    int **pp = &p3;
    
    printf("b的值: %d\n", b);
    printf("*p3的值: %d\n", *p3);
    printf("**pp的值: %d\n", **pp);
    
    // 2. 指针与数组
    printf("\n=== 指针与数组 ===\n");
    
    // 数组名作为指针
    printf("\n=== 数组名作为指针 ===\n");
    int arr[] = {1, 2, 3, 4, 5};
    
    printf("数组名作为指针: %p\n", arr);
    printf("第一个元素的地址: %p\n", &arr[0]);
    printf("第一个元素的值: %d\n", *arr);
    printf("第二个元素的值: %d\n", *(arr + 1));
    
    // 指针算术
    printf("\n=== 指针算术 ===\n");
    int *p_arr = arr;
    for (int i = 0; i < 5; i++) {
        printf("*(p_arr + %d) = %d\n", i, *(p_arr + i));
    }
    
    // 数组作为函数参数
    printf("\n=== 数组作为函数参数 ===\n");
    print_array(arr, 5);
    
    // 3. 指针与函数
    printf("\n=== 指针与函数 ===\n");
    
    // 指针作为函数参数
    printf("\n=== 指针作为函数参数 ===\n");
    int c = 10;
    printf("修改前: %d\n", c);
    increment(&c);
    printf("修改后: %d\n", c);
    
    // 函数返回指针
    printf("\n=== 函数返回指针 ===\n");
    int *arr2 = create_array(5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");
    free(arr2);  // 释放内存
    
    // 函数指针
    printf("\n=== 函数指针 ===\n");
    // 函数指针
    int (*operation)(int, int);
    
    operation = add;
    printf("5 + 3 = %d\n", operation(5, 3));
    
    operation = subtract;
    printf("5 - 3 = %d\n", operation(5, 3));
    
    // 4. 动态内存分配
    printf("\n=== 动态内存分配 ===\n");
    
    // malloc与free
    printf("\n=== malloc与free ===\n");
    // 分配内存
    int *p4 = (int *)malloc(5 * sizeof(int));
    if (p4 == NULL) {
        printf("内存分配失败\n");
        return 1;
    }
    
    // 使用内存
    for (int i = 0; i < 5; i++) {
        p4[i] = i + 1;
    }
    
    // 打印值
    for (int i = 0; i < 5; i++) {
        printf("%d ", p4[i]);
    }
    printf("\n");
    
    // 释放内存
    free(p4);
    p4 = NULL;  // 避免野指针
    
    // calloc与realloc
    printf("\n=== calloc与realloc ===\n");
    // calloc分配并初始化
    int *p5 = (int *)calloc(5, sizeof(int));
    for (int i = 0; i < 5; i++) {
        printf("%d ", p5[i]);
    }
    printf("\n");
    
    // realloc重新分配
    int *p6 = (int *)realloc(p5, 10 * sizeof(int));
    for (int i = 5; i < 10; i++) {
        p6[i] = i + 1;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", p6[i]);
    }
    printf("\n");
    
    // 释放内存
    free(p6);
    
    return 0;
}