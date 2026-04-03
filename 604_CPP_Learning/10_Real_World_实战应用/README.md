# 实战应用

## 1. 系统编程

### 1.1 文件系统操作

C++可以使用标准库和系统API进行文件系统操作：

```cpp
#include <iostream>
#include <fstream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    // 创建目录
    fs::create_directory("test");
    
    // 创建文件
    std::ofstream file("test/example.txt");
    file << "Hello, World!" << std::endl;
    file.close();
    
    // 遍历目录
    std::cout << "Directory contents:" << std::endl;
    for (const auto& entry : fs::directory_iterator("test")) {
        std::cout << entry.path() << std::endl;
    }
    
    // 删除文件
    fs::remove("test/example.txt");
    
    // 删除目录
    fs::remove_all("test");
    
    return 0;
}
```

### 1.2 进程管理

C++可以使用系统API创建和管理进程：

```cpp
#include <iostream>
#include <cstdlib>

int main() {
    // 创建子进程
    int result = system("echo Hello from child process");
    std::cout << "System call result: " << result << std::endl;
    
    return 0;
}
```

## 2. 网络编程

### 2.1 套接字编程

C++可以使用系统API进行套接字编程：

```cpp
#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    // 创建套接字
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        std::cerr << "Failed to create socket" << std::endl;
        return 1;
    }
    
    // 设置套接字选项
    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt));
    
    // 绑定地址
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);
    
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        std::cerr << "Failed to bind" << std::endl;
        return 1;
    }
    
    // 监听连接
    if (listen(server_fd, 3) < 0) {
        std::cerr << "Failed to listen" << std::endl;
        return 1;
    }
    
    std::cout << "Server listening on port 8080" << std::endl;
    
    // 接受连接
    int new_socket;
    socklen_t addrlen = sizeof(address);
    new_socket = accept(server_fd, (struct sockaddr*)&address, &addrlen);
    if (new_socket < 0) {
        std::cerr << "Failed to accept" << std::endl;
        return 1;
    }
    
    // 发送数据
    const char* message = "Hello from server";
    send(new_socket, message, strlen(message), 0);
    std::cout << "Message sent" << std::endl;
    
    // 关闭套接字
    close(new_socket);
    close(server_fd);
    
    return 0;
}
```

### 2.2 网络库

可以使用第三方网络库如Boost.Asio进行网络编程：

```cpp
#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

int main() {
    try {
        boost::asio::io_context io_context;
        
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 8080));
        
        std::cout << "Server listening on port 8080" << std::endl;
        
        tcp::socket socket(io_context);
        acceptor.accept(socket);
        
        std::string message = "Hello from server\n";
        boost::asio::write(socket, boost::asio::buffer(message));
        
        std::cout << "Message sent" << std::endl;
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## 3. 图形界面编程

### 3.1 Qt框架

Qt是一个跨平台的C++图形界面框架：

```cpp
#include <QApplication>
#include <QMainWindow>
#include <QPushButton>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    
    QMainWindow window;
    window.setWindowTitle("Qt Application");
    window.resize(400, 300);
    
    QPushButton *button = new QPushButton("Hello, Qt!", &window);
    button->setGeometry(150, 120, 100, 30);
    
    QObject::connect(button, &QPushButton::clicked, []() {
        qDebug() << "Button clicked!";
    });
    
    window.show();
    
    return app.exec();
}
```

### 3.2 GTK+框架

GTK+是另一个跨平台的图形界面框架：

```cpp
#include <gtk/gtk.h>

static void on_button_clicked(GtkWidget *widget, gpointer data) {
    g_print("Button clicked!\n");
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);
    
    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "GTK+ Application");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 300);
    
    GtkWidget *button = gtk_button_new_with_label("Hello, GTK!");
    g_signal_connect(button, "clicked", G_CALLBACK(on_button_clicked), NULL);
    
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_box_pack_start(GTK_BOX(box), button, TRUE, TRUE, 0);
    
    gtk_container_add(GTK_CONTAINER(window), box);
    
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
    
    gtk_widget_show_all(window);
    
    gtk_main();
    
    return 0;
}
```

## 4. 数据库编程

### 4.1 SQLite

SQLite是一个轻量级的嵌入式数据库：

```cpp
#include <iostream>
#include <sqlite3.h>

static int callback(void *data, int argc, char **argv, char **azColName) {
    for (int i = 0; i < argc; i++) {
        std::cout << azColName[i] << " = " << (argv[i] ? argv[i] : "NULL") << std::endl;
    }
    std::cout << std::endl;
    return 0;
}

int main() {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    
    // 打开数据库
    rc = sqlite3_open("test.db", &db);
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return 1;
    }
    
    // 创建表
    const char *sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);";
    rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << zErrMsg << std::endl;
        sqlite3_free(zErrMsg);
    }
    
    // 插入数据
    sql = "INSERT INTO users (name, age) VALUES ('Alice', 25);";
    rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << zErrMsg << std::endl;
        sqlite3_free(zErrMsg);
    }
    
    // 查询数据
    sql = "SELECT * FROM users;";
    rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << zErrMsg << std::endl;
        sqlite3_free(zErrMsg);
    }
    
    // 关闭数据库
    sqlite3_close(db);
    
    return 0;
}
```

### 4.2 MySQL

可以使用MySQL Connector/C++连接MySQL数据库：

```cpp
#include <iostream>
#include <mysqlx/xdevapi.h>

using namespace mysqlx;

int main() {
    try {
        // 连接数据库
        Session session("localhost", 33060, "root", "password");
        
        // 创建模式
        Schema schema = session.createSchema("test", true);
        
        // 创建表
        Table table = schema.createTable("users", true)
            .addColumn("id", mysqlx::Type::INT).setNotNull().setPrimaryKey()
            .addColumn("name", mysqlx::Type::VARCHAR, 50)
            .addColumn("age", mysqlx::Type::INT)
            .execute();
        
        // 插入数据
        table.insert("id", "name", "age")
            .values(1, "Alice", 25)
            .values(2, "Bob", 30)
            .execute();
        
        // 查询数据
        Result result = table.select("*").execute();
        for (auto row : result) {
            std::cout << "ID: " << row[0] << ", Name: " << row[1] << ", Age: " << row[2] << std::endl;
        }
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    
    return 0;
}
```

## 5. 游戏开发

### 5.1 SDL库

SDL（Simple DirectMedia Layer）是一个跨平台的游戏开发库：

```cpp
#include <SDL2/SDL.h>
#include <iostream>

int main() {
    // 初始化SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL initialization failed: " << SDL_GetError() << std::endl;
        return 1;
    }
    
    // 创建窗口
    SDL_Window *window = SDL_CreateWindow("SDL Application",
                                          SDL_WINDOWPOS_UNDEFINED,
                                          SDL_WINDOWPOS_UNDEFINED,
                                          800, 600,
                                          SDL_WINDOW_SHOWN);
    if (!window) {
        std::cerr << "Window creation failed: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }
    
    // 创建渲染器
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        std::cerr << "Renderer creation failed: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }
    
    // 主循环
    bool running = true;
    SDL_Event event;
    
    while (running) {
        // 处理事件
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }
        
        // 清除屏幕
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        
        // 绘制矩形
        SDL_Rect rect = { 350, 250, 100, 100 };
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderFillRect(renderer, &rect);
        
        // 更新屏幕
        SDL_RenderPresent(renderer);
    }
    
    // 清理资源
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    
    return 0;
}
```

### 5.2 SFML库

SFML（Simple and Fast Multimedia Library）是另一个跨平台的游戏开发库：

```cpp
#include <SFML/Graphics.hpp>

int main() {
    // 创建窗口
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Application");
    
    // 创建矩形
    sf::RectangleShape rectangle(sf::Vector2f(100.f, 100.f));
    rectangle.setPosition(350.f, 250.f);
    rectangle.setFillColor(sf::Color::Red);
    
    // 主循环
    while (window.isOpen()) {
        // 处理事件
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }
        
        // 清除屏幕
        window.clear();
        
        // 绘制矩形
        window.draw(rectangle);
        
        // 更新屏幕
        window.display();
    }
    
    return 0;
}
```

## 6. 嵌入式开发

### 6.1 Arduino

C++可以用于Arduino开发：

```cpp
// Arduino代码
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
```

### 6.2 树莓派

C++可以用于树莓派开发：

```cpp
#include <wiringPi.h>
#include <iostream>

int main() {
    // 初始化wiringPi
    if (wiringPiSetup() == -1) {
        std::cerr << "Failed to initialize wiringPi" << std::endl;
        return 1;
    }
    
    // 设置引脚模式
    pinMode(0, OUTPUT);
    
    // 主循环
    while (true) {
        digitalWrite(0, HIGH);
        delay(1000);
        digitalWrite(0, LOW);
        delay(1000);
    }
    
    return 0;
}
```

## 7. 高性能计算

### 7.1 多线程计算

C++可以使用多线程进行高性能计算：

```cpp
#include <iostream>
#include <vector>
#include <thread>
#include <numeric>

void compute(std::vector<double>& data, int start, int end, double& result) {
    double sum = 0.0;
    for (int i = start; i < end; i++) {
        sum += data[i] * data[i];
    }
    result = sum;
}

int main() {
    const int size = 10000000;
    std::vector<double> data(size);
    
    // 初始化数据
    for (int i = 0; i < size; i++) {
        data[i] = i * 0.1;
    }
    
    // 分块计算
    const int num_threads = 4;
    const int block_size = size / num_threads;
    std::vector<double> results(num_threads);
    std::vector<std::thread> threads;
    
    for (int i = 0; i < num_threads; i++) {
        int start = i * block_size;
        int end = (i == num_threads - 1) ? size : (i + 1) * block_size;
        threads.emplace_back(compute, std::ref(data), start, end, std::ref(results[i]));
    }
    
    // 等待线程完成
    for (auto& thread : threads) {
        thread.join();
    }
    
    // 汇总结果
    double total = std::accumulate(results.begin(), results.end(), 0.0);
    std::cout << "Total: " << total << std::endl;
    
    return 0;
}
```

### 7.2 SIMD指令

C++可以使用SIMD（Single Instruction Multiple Data）指令进行向量计算：

```cpp
#include <iostream>
#include <immintrin.h>

int main() {
    // 16个32位浮点数
    float a[16] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0};
    float b[16] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0};
    float c[16];
    
    // 使用AVX2指令集
    __m256 avx_a, avx_b, avx_c;
    
    for (int i = 0; i < 16; i += 8) {
        // 加载数据
        avx_a = _mm256_loadu_ps(&a[i]);
        avx_b = _mm256_loadu_ps(&b[i]);
        
        // 执行加法
        avx_c = _mm256_add_ps(avx_a, avx_b);
        
        // 存储结果
        _mm256_storeu_ps(&c[i], avx_c);
    }
    
    // 输出结果
    for (int i = 0; i < 16; i++) {
        std::cout << c[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## 8. 网络应用

### 8.1 HTTP服务器

C++可以使用Boost.Asio创建HTTP服务器：

```cpp
#include <iostream>
#include <string>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

int main() {
    try {
        boost::asio::io_context io_context;
        
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 8080));
        
        std::cout << "HTTP server listening on port 8080" << std::endl;
        
        while (true) {
            tcp::socket socket(io_context);
            acceptor.accept(socket);
            
            // 读取请求
            boost::asio::streambuf request;
            boost::asio::read_until(socket, request, "\r\n\r\n");
            
            // 发送响应
            std::string response = "HTTP/1.1 200 OK\r\n";
            response += "Content-Type: text/html\r\n";
            response += "Content-Length: 13\r\n";
            response += "\r\n";
            response += "Hello, World!";
            
            boost::asio::write(socket, boost::asio::buffer(response));
        }
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    
    return 0;
}
```

### 8.2 WebSocket客户端

C++可以使用WebSocket库创建WebSocket客户端：

```cpp
#include <iostream>
#include <websocketpp/client.hpp>
#include <websocketpp/config/asio_no_tls.hpp>

typedef websocketpp::client<websocketpp::config::asio> client;

int main() {
    client c;
    
    // 初始化客户端
    c.init_asio();
    
    // 连接处理
    c.set_open_handler([&](websocketpp::connection_hdl hdl) {
        std::cout << "Connected" << std::endl;
        c.send(hdl, "Hello, WebSocket!", websocketpp::frame::opcode::text);
    });
    
    // 消息处理
    c.set_message_handler([&](websocketpp::connection_hdl hdl, client::message_ptr msg) {
        std::cout << "Received: " << msg->get_payload() << std::endl;
    });
    
    // 连接到服务器
    websocketpp::lib::error_code ec;
    client::connection_ptr con = c.get_connection("ws://echo.websocket.org", ec);
    if (ec) {
        std::cerr << "Connection error: " << ec.message() << std::endl;
        return 1;
    }
    
    c.connect(con);
    
    // 运行事件循环
    c.run();
    
    return 0;
}
```

## 9. 工具开发

### 9.1 命令行工具

C++可以开发命令行工具：

```cpp
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char *argv[]) {
    // 解析命令行参数
    std::vector<std::string> args(argv + 1, argv + argc);
    
    if (args.empty()) {
        std::cout << "Usage: " << argv[0] << " <command> [args]" << std::endl;
        return 1;
    }
    
    std::string command = args[0];
    
    if (command == "hello") {
        std::cout << "Hello, World!" << std::endl;
    } else if (command == "add") {
        if (args.size() < 3) {
            std::cout << "Usage: " << argv[0] << " add <num1> <num2>" << std::endl;
            return 1;
        }
        int num1 = std::stoi(args[1]);
        int num2 = std::stoi(args[2]);
        std::cout << num1 << " + " << num2 << " = " << num1 + num2 << std::endl;
    } else {
        std::cout << "Unknown command: " << command << std::endl;
        return 1;
    }
    
    return 0;
}
```

### 9.2 文本处理工具

C++可以开发文本处理工具：

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Usage: " << argv[0] << " <file>" << std::endl;
        return 1;
    }
    
    std::string filename = argv[1];
    std::ifstream file(filename);
    
    if (!file) {
        std::cerr << "Failed to open file: " << filename << std::endl;
        return 1;
    }
    
    int line_count = 0;
    int word_count = 0;
    int char_count = 0;
    std::string line;
    
    while (std::getline(file, line)) {
        line_count++;
        char_count += line.size() + 1;  // +1 for newline
        
        // 统计单词数
        bool in_word = false;
        for (char c : line) {
            if (std::isspace(c)) {
                in_word = false;
            } else if (!in_word) {
                in_word = true;
                word_count++;
            }
        }
    }
    
    std::cout << "Lines: " << line_count << std::endl;
    std::cout << "Words: " << word_count << std::endl;
    std::cout << "Characters: " << char_count << std::endl;
    
    return 0;
}
```

## 10. 项目实战

### 10.1 项目规划

一个完整的C++项目通常包括：

- **需求分析**：明确项目的功能和目标
- **设计**：设计系统架构和数据结构
- **实现**：编写代码
- **测试**：测试功能和性能
- **部署**：部署和维护

### 10.2 项目结构

一个典型的C++项目结构：

```
project/
├── include/          # 头文件
├── src/              # 源文件
├── tests/            # 测试文件
├── examples/         # 示例代码
├── CMakeLists.txt    # CMake配置文件
└── README.md         # 项目说明
```

### 10.3 项目示例

#### 简单的文本编辑器

```cpp
// 主文件
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class TextEditor {
private:
    std::vector<std::string> lines;
    std::string filename;

public:
    TextEditor(const std::string& fname) : filename(fname) {
        load();
    }
    
    void load() {
        std::ifstream file(filename);
        if (file) {
            std::string line;
            while (std::getline(file, line)) {
                lines.push_back(line);
            }
        }
    }
    
    void save() {
        std::ofstream file(filename);
        for (const auto& line : lines) {
            file << line << std::endl;
        }
    }
    
    void addLine(const std::string& line) {
        lines.push_back(line);
    }
    
    void insertLine(int index, const std::string& line) {
        if (index >= 0 && index <= lines.size()) {
            lines.insert(lines.begin() + index, line);
        }
    }
    
    void deleteLine(int index) {
        if (index >= 0 && index < lines.size()) {
            lines.erase(lines.begin() + index);
        }
    }
    
    void print() {
        for (int i = 0; i < lines.size(); i++) {
            std::cout << i + 1 << ": " << lines[i] << std::endl;
        }
    }
};

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Usage: " << argv[0] << " <file>" << std::endl;
        return 1;
    }
    
    TextEditor editor(argv[1]);
    editor.print();
    
    // 示例操作
    editor.addLine("New line");
    editor.insertLine(0, "First line");
    editor.deleteLine(1);
    editor.print();
    editor.save();
    
    return 0;
}
```

---

**更新时间：2026-04-04**