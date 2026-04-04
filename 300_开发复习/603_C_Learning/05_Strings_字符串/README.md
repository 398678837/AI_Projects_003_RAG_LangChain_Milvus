# 字符串

## 1. 字符串基础

### 字符串定义与初始化
```c
#include <stdio.h>

int main() {
    // 字符数组定义
    char str1[10];
    
    // 字符数组初始化
    str1[0] = 'H';
    str1[1] = 'e';
    str1[2] = 'l';
    str1[3] = 'l';
    str1[4] = 'o';
    str1[5] = '\0';  // 字符串结束符
    
    // 字符串字面量初始化
    char str2[] = "Hello";
    
    // 指针指向字符串字面量
    char *str3 = "Hello";
    
    return 0;
}
```

### 字符串输入与输出
```c
#include <stdio.h>

int main() {
    // 字符串输出
    char str[] = "Hello, World!";
    printf("%s\n", str);
    
    // 字符串输入
    char name[50];
    printf("Enter your name: ");
    scanf("%s", name);  // 注意：scanf会在空格处停止
    printf("Hello, %s!\n", name);
    
    // 使用fgets读取带空格的字符串
    char fullname[50];
    printf("Enter your full name: ");
    fgets(fullname, sizeof(fullname), stdin);
    printf("Hello, %s!\n", fullname);
    
    return 0;
}
```

## 2. 字符串操作函数

### 字符串长度
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World!";
    int length = strlen(str);
    printf("字符串长度: %d\n", length);
    return 0;
}
```

### 字符串复制
```c
#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Hello";
    char destination[20];
    
    strcpy(destination, source);
    printf("复制后的字符串: %s\n", destination);
    
    // 安全的字符串复制
    strncpy(destination, source, sizeof(destination) - 1);
    destination[sizeof(destination) - 1] = '\0';
    printf("安全复制后的字符串: %s\n", destination);
    
    return 0;
}
```

### 字符串连接
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello";
    char str2[] = " World!";
    
    strcat(str1, str2);
    printf("连接后的字符串: %s\n", str1);
    
    // 安全的字符串连接
    char str3[20] = "Hello";
    strncat(str3, str2, sizeof(str3) - strlen(str3) - 1);
    printf("安全连接后的字符串: %s\n", str3);
    
    return 0;
}
```

### 字符串比较
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "Hello";
    char str3[] = "World";
    
    int result1 = strcmp(str1, str2);
    int result2 = strcmp(str1, str3);
    int result3 = strcmp(str3, str1);
    
    printf("strcmp(\"Hello\", \"Hello\") = %d\n", result1);
    printf("strcmp(\"Hello\", \"World\") = %d\n", result2);
    printf("strcmp(\"World\", \"Hello\") = %d\n", result3);
    
    // 字符串比较（指定长度）
    int result4 = strncmp(str1, "Hel", 3);
    printf("strncmp(\"Hello\", \"Hel\", 3) = %d\n", result4);
    
    return 0;
}
```

## 3. 字符串与指针

### 指针与字符串
```c
#include <stdio.h>

int main() {
    // 指针指向字符串字面量
    char *str = "Hello, World!";
    
    // 通过指针访问字符串
    printf("字符串: %s\n", str);
    
    // 通过指针遍历字符串
    char *p = str;
    while (*p != '\0') {
        printf("%c", *p);
        p++;
    }
    printf("\n");
    
    return 0;
}
```

### 字符串数组
```c
#include <stdio.h>

int main() {
    // 字符串数组
    char *names[] = {
        "Alice",
        "Bob",
        "Charlie",
        "David"
    };
    
    // 遍历字符串数组
    for (int i = 0; i < 4; i++) {
        printf("names[%d] = %s\n", i, names[i]);
    }
    
    return 0;
}
```

## 4. 字符串格式化

### sprintf函数
```c
#include <stdio.h>

int main() {
    char buffer[100];
    int age = 25;
    char name[] = "Alice";
    
    // 格式化字符串
    sprintf(buffer, "Name: %s, Age: %d", name, age);
    printf("格式化后的字符串: %s\n", buffer);
    
    return 0;
}
```

### sscanf函数
```c
#include <stdio.h>

int main() {
    char buffer[] = "Alice 25";
    char name[50];
    int age;
    
    // 从字符串中读取格式化数据
    sscanf(buffer, "%s %d", name, &age);
    printf("Name: %s, Age: %d\n", name, age);
    
    return 0;
}
```

## 5. 字符串处理实例

### 字符串反转
```c
#include <stdio.h>
#include <string.h>

void reverse_string(char *str) {
    int length = strlen(str);
    int i, j;
    char temp;
    
    for (i = 0, j = length - 1; i < j; i++, j--) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

int main() {
    char str[] = "Hello, World!";
    printf("原始字符串: %s\n", str);
    reverse_string(str);
    printf("反转后的字符串: %s\n", str);
    return 0;
}
```

### 字符串查找
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World!";
    char *ptr;
    
    // 查找字符
    ptr = strchr(str, 'W');
    if (ptr != NULL) {
        printf("找到字符 'W' 在位置: %ld\n", ptr - str);
    }
    
    // 查找子字符串
    ptr = strstr(str, "World");
    if (ptr != NULL) {
        printf("找到子字符串 'World' 在位置: %ld\n", ptr - str);
    }
    
    return 0;
}
```

---

**更新时间：2026-04-04**