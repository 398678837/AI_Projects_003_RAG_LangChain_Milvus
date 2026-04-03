# 数组

## 1. 一维数组

### 数组定义与初始化
```c
#include <stdio.h>

int main() {
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
    
    return 0;
}
```

### 数组访问与遍历
```c
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // 数组访问
    printf("第一个元素: %d\n", arr[0]);
    printf("最后一个元素: %d\n", arr[size - 1]);
    
    // 数组遍历
    printf("数组元素: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
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

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    print_array(arr, size);
    return 0;
}
```

## 2. 二维数组

### 二维数组定义与初始化
```c
#include <stdio.h>

int main() {
    // 二维数组定义
    int arr[3][3];
    
    // 二维数组初始化
    arr[0][0] = 1;
    arr[0][1] = 2;
    arr[0][2] = 3;
    arr[1][0] = 4;
    arr[1][1] = 5;
    arr[1][2] = 6;
    arr[2][0] = 7;
    arr[2][1] = 8;
    arr[2][2] = 9;
    
    // 二维数组初始化（简化）
    int arr2[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    return 0;
}
```

### 二维数组访问与遍历
```c
#include <stdio.h>

int main() {
    int arr[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    // 二维数组访问
    printf("arr[0][0] = %d\n", arr[0][0]);
    printf("arr[2][2] = %d\n", arr[2][2]);
    
    // 二维数组遍历
    printf("二维数组:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

### 二维数组作为函数参数
```c
#include <stdio.h>

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
    int arr[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    print_2d_array(arr, 3);
    return 0;
}
```

## 3. 字符数组

### 字符数组定义与初始化
```c
#include <stdio.h>

int main() {
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
    
    return 0;
}
```

### 字符串操作
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello";
    
    // 字符串长度
    printf("字符串长度: %lu\n", strlen(str));
    
    // 字符串复制
    char str2[10];
    strcpy(str2, str);
    printf("复制后的字符串: %s\n", str2);
    
    // 字符串连接
    strcat(str2, " World");
    printf("连接后的字符串: %s\n", str2);
    
    // 字符串比较
    char str3[] = "Hello";
    int result = strcmp(str, str3);
    printf("字符串比较结果: %d\n", result);
    
    return 0;
}
```

## 4. 数组与指针

### 数组名与指针
```c
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p = arr;  // 数组名就是指向第一个元素的指针
    
    printf("arr = %p\n", arr);
    printf("&arr[0] = %p\n", &arr[0]);
    printf("p = %p\n", p);
    
    // 通过指针访问数组元素
    for (int i = 0; i < 5; i++) {
        printf("*(p + %d) = %d\n", i, *(p + i));
    }
    
    return 0;
}
```

### 指针数组
```c
#include <stdio.h>

int main() {
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
```

---

**更新时间：2026-04-04**