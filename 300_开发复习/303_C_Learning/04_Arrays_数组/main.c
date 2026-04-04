#include <stdio.h>
#include <string.h>

// 数组作为参数
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// 二维数组作为参数
void print_2d_array(int arr[][3], int rows) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

int main() {
    // 1. 一维数组
    printf("=== 一维数组 ===\n");
    
    // 数组定义与初始化
    printf("\n=== 数组定义与初始化 ===\n");
    // 数组定义
    int arr[5];
    
    // 数组初始化
    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 3;
    arr[3] = 4;
    arr[4] = 5;
    
    // 数组初始化（简化）
    int arr2[] = {1, 2, 3, 4, 5};
    
    // 数组初始化（指定大小）
    int arr3[5] = {1, 2, 3};  // 剩余元素自动初始化为0
    
    // 数组访问与遍历
    printf("\n=== 数组访问与遍历 ===\n");
    int arr4[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr4) / sizeof(arr4[0]);
    
    // 数组访问
    printf("第一个元素: %d\n", arr4[0]);
    printf("最后一个元素: %d\n", arr4[size - 1]);
    
    // 数组遍历
    printf("数组元素: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr4[i]);
    }
    printf("\n");
    
    // 数组作为函数参数
    printf("\n=== 数组作为函数参数 ===\n");
    print_array(arr4, size);
    
    // 2. 二维数组
    printf("\n=== 二维数组 ===\n");
    
    // 二维数组定义与初始化
    printf("\n=== 二维数组定义与初始化 ===\n");
    // 二维数组定义
    int arr5[3][3];
    
    // 二维数组初始化
    arr5[0][0] = 1;
    arr5[0][1] = 2;
    arr5[0][2] = 3;
    arr5[1][0] = 4;
    arr5[1][1] = 5;
    arr5[1][2] = 6;
    arr5[2][0] = 7;
    arr5[2][1] = 8;
    arr5[2][2] = 9;
    
    // 二维数组初始化（简化）
    int arr6[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    // 二维数组访问与遍历
    printf("\n=== 二维数组访问与遍历 ===\n");
    // 二维数组访问
    printf("arr6[0][0] = %d\n", arr6[0][0]);
    printf("arr6[2][2] = %d\n", arr6[2][2]);
    
    // 二维数组遍历
    printf("二维数组:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", arr6[i][j]);
        }
        printf("\n");
    }
    
    // 二维数组作为函数参数
    printf("\n=== 二维数组作为函数参数 ===\n");
    print_2d_array(arr6, 3);
    
    // 3. 字符数组
    printf("\n=== 字符数组 ===\n");
    
    // 字符数组定义与初始化
    printf("\n=== 字符数组定义与初始化 ===\n");
    // 字符数组定义
    char str[10];
    
    // 字符数组初始化
    str[0] = 'H';
    str[1] = 'e';
    str[2] = 'l';
    str[3] = 'l';
    str[4] = 'o';
    str[5] = '\0';  // 字符串结束符
    
    // 字符数组初始化（简化）
    char str2[] = "Hello";
    
    // 字符串操作
    printf("\n=== 字符串操作 ===\n");
    char str3[] = "Hello";
    
    // 字符串长度
    printf("字符串长度: %lu\n", strlen(str3));
    
    // 字符串复制
    char str4[20];
    strcpy(str4, str3);
    printf("复制后的字符串: %s\n", str4);
    
    // 字符串连接
    strcat(str4, " World");
    printf("连接后的字符串: %s\n", str4);
    
    // 字符串比较
    char str5[] = "Hello";
    int result = strcmp(str3, str5);
    printf("字符串比较结果: %d\n", result);
    
    // 4. 数组与指针
    printf("\n=== 数组与指针 ===\n");
    
    // 数组名与指针
    printf("\n=== 数组名与指针 ===\n");
    int arr7[] = {1, 2, 3, 4, 5};
    int *p = arr7;  // 数组名就是指向第一个元素的指针
    
    printf("arr7 = %p\n", arr7);
    printf("&arr7[0] = %p\n", &arr7[0]);
    printf("p = %p\n", p);
    
    // 通过指针访问数组元素
    for (int i = 0; i < 5; i++) {
        printf("*(p + %d) = %d\n", i, *(p + i));
    }
    
    // 指针数组
    printf("\n=== 指针数组 ===\n");
    // 指针数组
    char *names[] = {
        "Alice",
        "Bob",
        "Charlie"
    };
    
    // 访问指针数组
    for (int i = 0; i < 3; i++) {
        printf("names[%d] = %s\n", i, names[i]);
    }
    
    return 0;
}