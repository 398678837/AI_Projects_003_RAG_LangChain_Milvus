#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <ctype.h>
#include <netinet/in.h>
#include <sys/socket.h>

// 1. 系统调用示例

void system_call_example() {
    printf("=== 系统调用示例 ===\n");
    
    int fd;
    char buffer[100];
    ssize_t n;
    
    // 打开文件
    fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open");
        return;
    }
    
    // 写入数据
    n = write(fd, "Hello, System Call!\n", 18);
    if (n == -1) {
        perror("write");
        close(fd);
        return;
    }
    
    // 关闭文件
    if (close(fd) == -1) {
        perror("close");
        return;
    }
    
    // 打开文件读取
    fd = open("test.txt", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return;
    }
    
    // 读取数据
    n = read(fd, buffer, sizeof(buffer));
    if (n == -1) {
        perror("read");
        close(fd);
        return;
    }
    
    // 输出数据
    write(STDOUT_FILENO, buffer, n);
    
    // 关闭文件
    if (close(fd) == -1) {
        perror("close");
        return;
    }
    
    printf("\n");
}

// 2. 网络编程示例 - 简单的HTTP服务器

void http_server_example() {
    printf("=== HTTP服务器示例 ===\n");
    
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};
    
    const char *response = "HTTP/1.1 200 OK\r\n" 
                          "Content-Type: text/html\r\n" 
                          "Content-Length: 13\r\n" 
                          "\r\n" 
                          "Hello, World!";
    
    // 创建套接字文件描述符
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        return;
    }
    
    // 设置套接字选项
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("setsockopt");
        close(server_fd);
        return;
    }
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);
    
    // 绑定套接字
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        close(server_fd);
        return;
    }
    
    // 监听连接
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        close(server_fd);
        return;
    }
    
    printf("HTTP server listening on port 8080\n");
    printf("请在浏览器中访问 http://localhost:8080\n");
    printf("按 Ctrl+C 退出\n");
    
    // 只处理一个连接
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
        perror("accept");
        close(server_fd);
        return;
    }
    
    // 读取请求
    read(new_socket, buffer, 1024);
    printf("Request:\n%s\n", buffer);
    
    // 发送响应
    send(new_socket, response, strlen(response), 0);
    printf("Response sent\n");
    
    // 关闭连接
    close(new_socket);
    close(server_fd);
    
    printf("\n");
}

// 3. 实用工具 - 文件复制工具

void file_copy_tool(int argc, char *argv[]) {
    printf("=== 文件复制工具 ===\n");
    
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
        return;
    }
    
    FILE *source, *dest;
    char ch;
    
    // 打开源文件
    source = fopen(argv[1], "rb");
    if (source == NULL) {
        perror("Error opening source file");
        return;
    }
    
    // 打开目标文件
    dest = fopen(argv[2], "wb");
    if (dest == NULL) {
        perror("Error opening destination file");
        fclose(source);
        return;
    }
    
    // 复制文件
    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, dest);
    }
    
    // 关闭文件
    fclose(source);
    fclose(dest);
    
    printf("文件复制成功: %s -> %s\n\n", argv[1], argv[2]);
}

// 4. 实用工具 - 单词计数工具

void word_count_tool(int argc, char *argv[]) {
    printf("=== 单词计数工具 ===\n");
    
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return;
    }
    
    FILE *fp;
    int ch;
    int words = 0;
    int in_word = 0;
    
    // 打开文件
    fp = fopen(argv[1], "r");
    if (fp == NULL) {
        perror("Error opening file");
        return;
    }
    
    // 统计单词数
    while ((ch = fgetc(fp)) != EOF) {
        if (isspace(ch)) {
            in_word = 0;
        } else if (!in_word) {
            in_word = 1;
            words++;
        }
    }
    
    // 关闭文件
    fclose(fp);
    
    printf("文件 %s 中的单词数: %d\n\n", argv[1], words);
}

int main(int argc, char *argv[]) {
    // 运行系统调用示例
    system_call_example();
    
    // 运行HTTP服务器示例
    // http_server_example(); // 注释掉，避免阻塞
    
    // 运行文件复制工具
    if (argc >= 3) {
        file_copy_tool(argc, argv);
    }
    
    // 运行单词计数工具
    if (argc >= 2) {
        word_count_tool(argc, argv);
    }
    
    // 显示帮助信息
    if (argc == 1) {
        printf("=== 实战应用示例 ===\n");
        printf("用法:\n");
        printf("  %s <source> <destination>  - 复制文件\n", argv[0]);
        printf("  %s <file>               - 统计文件中的单词数\n", argv[0]);
        printf("  %s                    - 运行系统调用示例\n", argv[0]);
    }
    
    return 0;
}