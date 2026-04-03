# 文件操作

## 1. 文件操作基础

### 文件打开与关闭

在C语言中，文件操作是通过文件指针来实现的。文件指针是一个指向`FILE`类型的指针，用于表示一个打开的文件。

#### 文件打开

使用`fopen`函数打开文件，函数原型为：

```c
FILE *fopen(const char *filename, const char *mode);
```

其中，`filename`是文件名，`mode`是打开模式，常见的打开模式有：

| 模式 | 描述 |
|------|------|
| "r" | 只读模式，文件必须存在 |
| "w" | 只写模式，如果文件存在则截断为0长度，否则创建新文件 |
| "a" | 追加模式，在文件末尾写入，文件不存在则创建 |
| "r+" | 读写模式，文件必须存在 |
| "w+" | 读写模式，如果文件存在则截断为0长度，否则创建新文件 |
| "a+" | 读写模式，在文件末尾写入，文件不存在则创建 |

#### 文件关闭

使用`fclose`函数关闭文件，函数原型为：

```c
int fclose(FILE *stream);
```

### 示例代码

```c
#include <stdio.h>

int main() {
    FILE *fp;
    
    // 打开文件
    fp = fopen("test.txt", "w");
    if (fp == NULL) {
        printf("无法打开文件\n");
        return 1;
    }
    
    // 写入数据
    fprintf(fp, "Hello, File!\n");
    
    // 关闭文件
    fclose(fp);
    
    return 0;
}
```

## 2. 文件读写操作

### 字符读写

#### 单字符读写

- `fgetc`：从文件中读取一个字符
- `fputc`：向文件中写入一个字符

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char ch;
    
    // 写入文件
    fp = fopen("test.txt", "w");
    fputc('H', fp);
    fputc('e', fp);
    fputc('l', fp);
    fputc('l', fp);
    fputc('o', fp);
    fclose(fp);
    
    // 读取文件
    fp = fopen("test.txt", "r");
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }
    fclose(fp);
    
    return 0;
}
```

### 字符串读写

#### 字符串读写

- `fgets`：从文件中读取一个字符串
- `fputs`：向文件中写入一个字符串

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[100];
    
    // 写入文件
    fp = fopen("test.txt", "w");
    fputs("Hello, File!\n", fp);
    fputs("This is a test.\n", fp);
    fclose(fp);
    
    // 读取文件
    fp = fopen("test.txt", "r");
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }
    fclose(fp);
    
    return 0;
}
```

### 格式化读写

#### 格式化读写

- `fprintf`：向文件中写入格式化数据
- `fscanf`：从文件中读取格式化数据

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char name[50];
    int age;
    
    // 写入文件
    fp = fopen("test.txt", "w");
    fprintf(fp, "Name: %s\nAge: %d\n", "Alice", 25);
    fclose(fp);
    
    // 读取文件
    fp = fopen("test.txt", "r");
    fscanf(fp, "Name: %s\nAge: %d\n", name, &age);
    printf("Name: %s\nAge: %d\n", name, age);
    fclose(fp);
    
    return 0;
}
```

## 3. 文件定位

### 文件指针定位

- `ftell`：获取当前文件指针位置
- `fseek`：设置文件指针位置
- `rewind`：将文件指针重置到文件开头

```c
#include <stdio.h>

int main() {
    FILE *fp;
    long position;
    char buffer[100];
    
    // 写入文件
    fp = fopen("test.txt", "w");
    fprintf(fp, "Hello, File!\n");
    fclose(fp);
    
    // 读取文件
    fp = fopen("test.txt", "r");
    
    // 获取当前位置
    position = ftell(fp);
    printf("Current position: %ld\n", position);
    
    // 读取一些数据
    fgets(buffer, 6, fp);
    printf("Read: %s\n", buffer);
    
    // 获取当前位置
    position = ftell(fp);
    printf("Current position: %ld\n", position);
    
    // 重置到文件开头
    rewind(fp);
    position = ftell(fp);
    printf("Position after rewind: %ld\n", position);
    
    // 读取全部内容
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }
    
    fclose(fp);
    
    return 0;
}
```

## 4. 二进制文件操作

### 二进制文件读写

- `fread`：从文件中读取二进制数据
- `fwrite`：向文件中写入二进制数据

```c
#include <stdio.h>

// 定义一个结构体
typedef struct {
    char name[50];
    int age;
    float height;
} Person;

int main() {
    FILE *fp;
    Person p1 = {"Alice", 25, 1.65};
    Person p2;
    
    // 写入二进制文件
    fp = fopen("person.bin", "wb");
    fwrite(&p1, sizeof(Person), 1, fp);
    fclose(fp);
    
    // 读取二进制文件
    fp = fopen("person.bin", "rb");
    fread(&p2, sizeof(Person), 1, fp);
    fclose(fp);
    
    // 输出读取的数据
    printf("Name: %s\n", p2.name);
    printf("Age: %d\n", p2.age);
    printf("Height: %.2f\n", p2.height);
    
    return 0;
}
```

## 5. 文件操作最佳实践

### 错误处理

在文件操作中，应该始终检查函数返回值，以确保操作成功。

```c
#include <stdio.h>

int main() {
    FILE *fp;
    
    // 打开文件
    fp = fopen("test.txt", "w");
    if (fp == NULL) {
        perror("无法打开文件");
        return 1;
    }
    
    // 写入数据
    if (fprintf(fp, "Hello, File!\n") < 0) {
        perror("写入失败");
        fclose(fp);
        return 1;
    }
    
    // 关闭文件
    if (fclose(fp) != 0) {
        perror("关闭文件失败");
        return 1;
    }
    
    return 0;
}
```

### 文件操作示例

#### 复制文件

```c
#include <stdio.h>

int main() {
    FILE *source, *dest;
    char ch;
    
    // 打开源文件
    source = fopen("source.txt", "r");
    if (source == NULL) {
        perror("无法打开源文件");
        return 1;
    }
    
    // 打开目标文件
    dest = fopen("dest.txt", "w");
    if (dest == NULL) {
        perror("无法打开目标文件");
        fclose(source);
        return 1;
    }
    
    // 复制内容
    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, dest);
    }
    
    // 关闭文件
    fclose(source);
    fclose(dest);
    
    printf("文件复制成功\n");
    
    return 0;
}
```

#### 统计文件行数

```c
#include <stdio.h>

int main() {
    FILE *fp;
    char ch;
    int count = 0;
    
    // 打开文件
    fp = fopen("test.txt", "r");
    if (fp == NULL) {
        perror("无法打开文件");
        return 1;
    }
    
    // 统计行数
    while ((ch = fgetc(fp)) != EOF) {
        if (ch == '\n') {
            count++;
        }
    }
    
    // 关闭文件
    fclose(fp);
    
    printf("文件行数: %d\n", count);
    
    return 0;
}
```

---

**更新时间：2026-04-04**