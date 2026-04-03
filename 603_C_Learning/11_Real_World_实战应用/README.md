# 实战应用

## 1. 系统编程

### 系统调用

C语言是系统编程的首选语言，因为它可以直接调用操作系统的API。在Unix/Linux系统中，系统调用是通过`unistd.h`头文件提供的。

#### 示例：文件操作

```c
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd;
    char buffer[100];
    ssize_t n;
    
    // 打开文件
    fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    
    // 写入数据
    n = write(fd, "Hello, System Call!\n", 18);
    if (n == -1) {
        perror("write");
        close(fd);
        return 1;
    }
    
    // 关闭文件
    if (close(fd) == -1) {
        perror("close");
        return 1;
    }
    
    // 打开文件读取
    fd = open("test.txt", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    
    // 读取数据
    n = read(fd, buffer, sizeof(buffer));
    if (n == -1) {
        perror("read");
        close(fd);
        return 1;
    }
    
    // 输出数据
    write(STDOUT_FILENO, buffer, n);
    
    // 关闭文件
    if (close(fd) == -1) {
        perror("close");
        return 1;
    }
    
    return 0;
}
```

### 进程管理

#### 示例：创建子进程

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int status;
    
    // 创建子进程
    pid = fork();
    if (pid == -1) {
        perror("fork");
        return 1;
    }
    
    if (pid == 0) {
        // 子进程
        printf("Child process: PID = %d\n", getpid());
        execl("/bin/ls", "ls", "-l", NULL);
        perror("execl");
        return 1;
    } else {
        // 父进程
        printf("Parent process: PID = %d, Child PID = %d\n", getpid(), pid);
        wait(&status);
        printf("Child exited with status: %d\n", WEXITSTATUS(status));
    }
    
    return 0;
}
```

## 2. 网络编程

### 套接字编程

C语言是网络编程的基础语言，通过`socket` API可以实现网络通信。

#### 示例：TCP服务器

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    char *hello = "Hello from server";
    
    // 创建套接字文件描述符
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
    
    // 设置套接字选项
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
    
    // 绑定套接字
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    
    // 监听连接
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    
    // 接受连接
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
        perror("accept");
        exit(EXIT_FAILURE);
    }
    
    // 读取客户端消息
    read(new_socket, buffer, BUFFER_SIZE);
    printf("Client: %s\n", buffer);
    
    // 发送消息给客户端
    send(new_socket, hello, strlen(hello), 0);
    printf("Hello message sent\n");
    
    return 0;
}
```

#### 示例：TCP客户端

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char *hello = "Hello from client";
    char buffer[BUFFER_SIZE] = {0};
    
    // 创建套接字文件描述符
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("Socket creation error\n");
        return -1;
    }
    
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    
    // 将IPv4地址从文本转换为二进制
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0) {
        printf("Invalid address\n");
        return -1;
    }
    
    // 连接服务器
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("Connection failed\n");
        return -1;
    }
    
    // 发送消息
    send(sock , hello , strlen(hello) , 0 );
    printf("Hello message sent\n");
    
    // 读取服务器响应
    read( sock , buffer, BUFFER_SIZE);
    printf("Server: %s\n", buffer);
    
    return 0;
}
```

## 3. 嵌入式开发

### 嵌入式C编程

C语言是嵌入式开发的主要语言，因为它可以直接操作硬件，并且生成的代码体积小、执行效率高。

#### 示例：LED闪烁

```c
#include <stdint.h>

// 假设这是一个简单的微控制器平台
#define LED_PORT (*(volatile uint8_t *)0x1000)
#define LED_PIN 0x01

void delay(uint32_t count) {
    while (count--);
}

int main() {
    while (1) {
        // 打开LED
        LED_PORT |= LED_PIN;
        delay(1000000);
        
        // 关闭LED
        LED_PORT &= ~LED_PIN;
        delay(1000000);
    }
    return 0;
}
```

### 硬件操作

#### 示例：UART通信

```c
#include <stdint.h>

// UART寄存器地址
#define UART_BASE 0x10000000
#define UART_DATA (*(volatile uint8_t *)(UART_BASE + 0x00))
#define UART_STATUS (*(volatile uint8_t *)(UART_BASE + 0x04))
#define UART_CTRL (*(volatile uint8_t *)(UART_BASE + 0x08))

// 状态位
#define UART_TX_READY (1 << 0)
#define UART_RX_READY (1 << 1)

void uart_init() {
    // 初始化UART
    UART_CTRL = 0x03; // 启用收发
}

void uart_send(char c) {
    // 等待发送就绪
    while (!(UART_STATUS & UART_TX_READY));
    // 发送数据
    UART_DATA = c;
}

char uart_recv() {
    // 等待接收就绪
    while (!(UART_STATUS & UART_RX_READY));
    // 读取数据
    return UART_DATA;
}

void uart_send_string(const char *str) {
    while (*str) {
        uart_send(*str++);
    }
}

int main() {
    uart_init();
    uart_send_string("Hello, UART!\n");
    
    while (1) {
        char c = uart_recv();
        uart_send(c);
    }
    
    return 0;
}
```

## 4. 数据库编程

### SQLite编程

SQLite是一个轻量级的嵌入式数据库，C语言可以通过SQLite的C API进行操作。

#### 示例：SQLite操作

```c
#include <stdio.h>
#include <sqlite3.h>

static int callback(void *data, int argc, char **argv, char **azColName) {
    int i;
    fprintf(stderr, "%s: ", (const char*)data);
    for (i = 0; i < argc; i++) {
        printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return 0;
}

int main() {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;
    const char* data = "Callback function called";
    
    // 打开数据库
    rc = sqlite3_open("test.db", &db);
    if (rc) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        return 0;
    } else {
        fprintf(stderr, "Opened database successfully\n");
    }
    
    // 创建表
    sql = "CREATE TABLE IF NOT EXISTS USERS (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL);";
    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "Table created successfully\n");
    }
    
    // 插入数据
    sql = "INSERT INTO USERS (ID, NAME, AGE) VALUES (1, 'Alice', 25);";
    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "Records created successfully\n");
    }
    
    // 查询数据
    sql = "SELECT * FROM USERS;";
    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }
    
    // 关闭数据库
    sqlite3_close(db);
    
    return 0;
}
```

## 5. 实用工具开发

### 命令行工具

C语言适合开发命令行工具，因为它可以直接访问系统API，并且生成的可执行文件体积小、运行速度快。

#### 示例：文件复制工具

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    FILE *source, *dest;
    char ch;
    
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
        return 1;
    }
    
    // 打开源文件
    source = fopen(argv[1], "rb");
    if (source == NULL) {
        perror("Error opening source file");
        return 1;
    }
    
    // 打开目标文件
    dest = fopen(argv[2], "wb");
    if (dest == NULL) {
        perror("Error opening destination file");
        fclose(source);
        return 1;
    }
    
    // 复制文件
    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, dest);
    }
    
    // 关闭文件
    fclose(source);
    fclose(dest);
    
    printf("File copied successfully\n");
    
    return 0;
}
```

### 文本处理工具

#### 示例：单词计数工具

```c
#include <stdio.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    FILE *fp;
    int ch;
    int words = 0;
    int in_word = 0;
    
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return 1;
    }
    
    // 打开文件
    fp = fopen(argv[1], "r");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
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
    
    printf("Number of words: %d\n", words);
    
    return 0;
}
```

## 6. 实战项目示例

### 示例：简单的HTTP服务器

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define PORT 8080
#define BUFFER_SIZE 1024

const char *response = "HTTP/1.1 200 OK\r\n" 
                      "Content-Type: text/html\r\n" 
                      "Content-Length: 13\r\n" 
                      "\r\n" 
                      "Hello, World!";

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    
    // 创建套接字文件描述符
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
    
    // 设置套接字选项
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
    
    // 绑定套接字
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    
    // 监听连接
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    
    printf("HTTP server listening on port %d\n", PORT);
    
    while (1) {
        // 接受连接
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
            perror("accept");
            exit(EXIT_FAILURE);
        }
        
        // 读取请求
        read(new_socket, buffer, BUFFER_SIZE);
        printf("Request:\n%s\n", buffer);
        
        // 发送响应
        send(new_socket, response, strlen(response), 0);
        printf("Response sent\n");
        
        // 关闭连接
        close(new_socket);
    }
    
    return 0;
}
```

---

**更新时间：2026-04-04**