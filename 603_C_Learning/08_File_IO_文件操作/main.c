#include <stdio.h>

// 定义一个结构体
typedef struct {
    char name[50];
    int age;
    float height;
} Person;

// 复制文件
void copy_file(const char *source, const char *dest) {
    FILE *source_fp, *dest_fp;
    char ch;
    
    // 打开源文件
    source_fp = fopen(source, "r");
    if (source_fp == NULL) {
        perror("无法打开源文件");
        return;
    }
    
    // 打开目标文件
    dest_fp = fopen(dest, "w");
    if (dest_fp == NULL) {
        perror("无法打开目标文件");
        fclose(source_fp);
        return;
    }
    
    // 复制内容
    while ((ch = fgetc(source_fp)) != EOF) {
        fputc(ch, dest_fp);
    }
    
    // 关闭文件
    fclose(source_fp);
    fclose(dest_fp);
    
    printf("文件复制成功: %s -> %s\n", source, dest);
}

// 统计文件行数
int count_lines(const char *filename) {
    FILE *fp;
    char ch;
    int count = 0;
    
    // 打开文件
    fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("无法打开文件");
        return -1;
    }
    
    // 统计行数
    while ((ch = fgetc(fp)) != EOF) {
        if (ch == '\n') {
            count++;
        }
    }
    
    // 关闭文件
    fclose(fp);
    
    return count;
}

int main() {
    // 1. 文件打开与关闭
    printf("=== 文件打开与关闭 ===\n");
    
    FILE *fp;
    
    // 打开文件
    fp = fopen("test.txt", "w");
    if (fp == NULL) {
        printf("无法打开文件\n");
        return 1;
    }
    
    // 写入数据
    fprintf(fp, "Hello, File!\n");
    fprintf(fp, "This is a test.\n");
    
    // 关闭文件
    fclose(fp);
    
    printf("文件创建成功\n");
    
    // 2. 文件读写操作
    printf("\n=== 文件读写操作 ===\n");
    
    // 字符读写
    printf("\n=== 字符读写 ===\n");
    char ch;
    
    // 写入文件
    fp = fopen("char_test.txt", "w");
    fputc('H', fp);
    fputc('e', fp);
    fputc('l', fp);
    fputc('l', fp);
    fputc('o', fp);
    fclose(fp);
    
    // 读取文件
    fp = fopen("char_test.txt", "r");
    printf("读取字符: ");
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }
    printf("\n");
    fclose(fp);
    
    // 字符串读写
    printf("\n=== 字符串读写 ===\n");
    char buffer[100];
    
    // 写入文件
    fp = fopen("string_test.txt", "w");
    fputs("Hello, File!\n", fp);
    fputs("This is a test.\n", fp);
    fclose(fp);
    
    // 读取文件
    fp = fopen("string_test.txt", "r");
    printf("读取字符串: \n");
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }
    fclose(fp);
    
    // 格式化读写
    printf("\n=== 格式化读写 ===\n");
    char name[50];
    int age;
    
    // 写入文件
    fp = fopen("format_test.txt", "w");
    fprintf(fp, "Name: %s\nAge: %d\n", "Alice", 25);
    fclose(fp);
    
    // 读取文件
    fp = fopen("format_test.txt", "r");
    fscanf(fp, "Name: %s\nAge: %d\n", name, &age);
    printf("读取格式化数据: \n");
    printf("Name: %s\nAge: %d\n", name, age);
    fclose(fp);
    
    // 3. 文件定位
    printf("\n=== 文件定位 ===\n");
    long position;
    
    // 打开文件
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
    printf("Read all content: \n");
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }
    
    fclose(fp);
    
    // 4. 二进制文件操作
    printf("\n=== 二进制文件操作 ===\n");
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
    printf("读取二进制数据: \n");
    printf("Name: %s\n", p2.name);
    printf("Age: %d\n", p2.age);
    printf("Height: %.2f\n", p2.height);
    
    // 5. 文件操作最佳实践
    printf("\n=== 文件操作最佳实践 ===\n");
    
    // 复制文件
    copy_file("test.txt", "test_copy.txt");
    
    // 统计文件行数
    int lines = count_lines("test.txt");
    if (lines >= 0) {
        printf("文件行数: %d\n", lines);
    }
    
    return 0;
}