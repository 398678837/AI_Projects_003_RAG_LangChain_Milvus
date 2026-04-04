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
    // 1. 字符串基础
    printf("=== 字符串基础 ===\n");
    
    // 字符串定义与初始化
    printf("\n=== 字符串定义与初始化 ===\n");
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
    
    // 字符串输入与输出
    printf("\n=== 字符串输入与输出 ===\n");
    // 字符串输出
    char str4[] = "Hello, World!";
    printf("%s\n", str4);
    
    // 2. 字符串操作函数
    printf("\n=== 字符串操作函数 ===\n");
    
    // 字符串长度
    printf("\n=== 字符串长度 ===\n");
    char str5[] = "Hello, World!";
    int length = strlen(str5);
    printf("字符串长度: %d\n", length);
    
    // 字符串复制
    printf("\n=== 字符串复制 ===\n");
    char source[] = "Hello";
    char destination[20];
    
    strcpy(destination, source);
    printf("复制后的字符串: %s\n", destination);
    
    // 安全的字符串复制
    strncpy(destination, source, sizeof(destination) - 1);
    destination[sizeof(destination) - 1] = '\0';
    printf("安全复制后的字符串: %s\n", destination);
    
    // 字符串连接
    printf("\n=== 字符串连接 ===\n");
    char str6[20] = "Hello";
    char str7[] = " World!";
    
    strcat(str6, str7);
    printf("连接后的字符串: %s\n", str6);
    
    // 安全的字符串连接
    char str8[20] = "Hello";
    strncat(str8, str7, sizeof(str8) - strlen(str8) - 1);
    printf("安全连接后的字符串: %s\n", str8);
    
    // 字符串比较
    printf("\n=== 字符串比较 ===\n");
    char str9[] = "Hello";
    char str10[] = "Hello";
    char str11[] = "World";
    
    int result1 = strcmp(str9, str10);
    int result2 = strcmp(str9, str11);
    int result3 = strcmp(str11, str9);
    
    printf("strcmp(\"Hello\", \"Hello\") = %d\n", result1);
    printf("strcmp(\"Hello\", \"World\") = %d\n", result2);
    printf("strcmp(\"World\", \"Hello\") = %d\n", result3);
    
    // 字符串比较（指定长度）
    int result4 = strncmp(str9, "Hel", 3);
    printf("strncmp(\"Hello\", \"Hel\", 3) = %d\n", result4);
    
    // 3. 字符串与指针
    printf("\n=== 字符串与指针 ===\n");
    
    // 指针与字符串
    printf("\n=== 指针与字符串 ===\n");
    // 指针指向字符串字面量
    char *str12 = "Hello, World!";
    
    // 通过指针访问字符串
    printf("字符串: %s\n", str12);
    
    // 通过指针遍历字符串
    char *p = str12;
    while (*p != '\0') {
        printf("%c", *p);
        p++;
    }
    printf("\n");
    
    // 字符串数组
    printf("\n=== 字符串数组 ===\n");
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
    
    // 4. 字符串格式化
    printf("\n=== 字符串格式化 ===\n");
    
    // sprintf函数
    printf("\n=== sprintf函数 ===\n");
    char buffer[100];
    int age = 25;
    char name[] = "Alice";
    
    // 格式化字符串
    sprintf(buffer, "Name: %s, Age: %d", name, age);
    printf("格式化后的字符串: %s\n", buffer);
    
    // sscanf函数
    printf("\n=== sscanf函数 ===\n");
    char buffer2[] = "Alice 25";
    char name2[50];
    int age2;
    
    // 从字符串中读取格式化数据
    sscanf(buffer2, "%s %d", name2, &age2);
    printf("Name: %s, Age: %d\n", name2, age2);
    
    // 5. 字符串处理实例
    printf("\n=== 字符串处理实例 ===\n");
    
    // 字符串反转
    printf("\n=== 字符串反转 ===\n");
    char str13[] = "Hello, World!";
    printf("原始字符串: %s\n", str13);
    reverse_string(str13);
    printf("反转后的字符串: %s\n", str13);
    
    // 字符串查找
    printf("\n=== 字符串查找 ===\n");
    char str14[] = "Hello, World!";
    char *ptr;
    
    // 查找字符
    ptr = strchr(str14, 'W');
    if (ptr != NULL) {
        printf("找到字符 'W' 在位置: %ld\n", ptr - str14);
    }
    
    // 查找子字符串
    ptr = strstr(str14, "World");
    if (ptr != NULL) {
        printf("找到子字符串 'World' 在位置: %ld\n", ptr - str14);
    }
    
    return 0;
}