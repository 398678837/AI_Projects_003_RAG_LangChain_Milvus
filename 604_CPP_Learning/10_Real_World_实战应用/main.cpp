#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <filesystem>
#include <cstdlib>
#include <chrono>

// 系统编程示例
void systemProgramming() {
    std::cout << "=== 系统编程 ===" << std::endl;
    
    // 文件系统操作
    std::cout << "\n文件系统操作: " << std::endl;
    
    // 创建目录
    std::filesystem::create_directory("test_dir");
    std::cout << "创建目录: test_dir" << std::endl;
    
    // 创建文件
    std::ofstream file("test_dir/example.txt");
    file << "Hello, System Programming!" << std::endl;
    file.close();
    std::cout << "创建文件: test_dir/example.txt" << std::endl;
    
    // 遍历目录
    std::cout << "目录内容: " << std::endl;
    for (const auto& entry : std::filesystem::directory_iterator("test_dir")) {
        std::cout << entry.path() << std::endl;
    }
    
    // 删除文件
    std::filesystem::remove("test_dir/example.txt");
    std::cout << "删除文件: test_dir/example.txt" << std::endl;
    
    // 删除目录
    std::filesystem::remove_all("test_dir");
    std::cout << "删除目录: test_dir" << std::endl;
    
    // 执行系统命令
    std::cout << "\n执行系统命令: " << std::endl;
    int result = system("echo Hello from system command");
    std::cout << "系统命令返回值: " << result << std::endl;
}

// 网络编程示例（简化版）
void networkProgramming() {
    std::cout << "\n=== 网络编程 ===" << std::endl;
    std::cout << "注意：完整的网络编程示例需要使用套接字API或网络库" << std::endl;
    std::cout << "这里仅展示基本概念" << std::endl;
    
    // 提示如何使用Boost.Asio等库
    std::cout << "\n推荐使用Boost.Asio、libcurl等库进行网络编程" << std::endl;
    std::cout << "例如，使用Boost.Asio创建HTTP服务器或客户端" << std::endl;
}

// 图形界面编程示例（简化版）
void guiProgramming() {
    std::cout << "\n=== 图形界面编程 ===" << std::endl;
    std::cout << "注意：完整的图形界面编程需要使用GUI库" << std::endl;
    std::cout << "这里仅展示基本概念" << std::endl;
    
    // 提示如何使用Qt、GTK+等库
    std::cout << "\n推荐使用Qt、GTK+、SFML等库进行图形界面编程" << std::endl;
    std::cout << "例如，使用Qt创建窗口和按钮" << std::endl;
}

// 数据库编程示例（简化版）
void databaseProgramming() {
    std::cout << "\n=== 数据库编程 ===" << std::endl;
    std::cout << "注意：完整的数据库编程需要使用数据库API或库" << std::endl;
    std::cout << "这里仅展示基本概念" << std::endl;
    
    // 提示如何使用SQLite、MySQL等库
    std::cout << "\n推荐使用SQLite、MySQL Connector/C++等库进行数据库编程" << std::endl;
    std::cout << "例如，使用SQLite创建表和执行查询" << std::endl;
}

// 游戏开发示例（简化版）
void gameDevelopment() {
    std::cout << "\n=== 游戏开发 ===" << std::endl;
    std::cout << "注意：完整的游戏开发需要使用游戏引擎或图形库" << std::endl;
    std::cout << "这里仅展示基本概念" << std::endl;
    
    // 提示如何使用SDL、SFML等库
    std::cout << "\n推荐使用SDL、SFML、Unity等库或引擎进行游戏开发" << std::endl;
    std::cout << "例如，使用SDL创建窗口和绘制图形" << std::endl;
}

// 嵌入式开发示例（简化版）
void embeddedDevelopment() {
    std::cout << "\n=== 嵌入式开发 ===" << std::endl;
    std::cout << "注意：嵌入式开发通常需要特定的硬件和工具链" << std::endl;
    std::cout << "这里仅展示基本概念" << std::endl;
    
    // 提示如何在Arduino、树莓派等平台上开发
    std::cout << "\n在Arduino上，可以使用C++编写嵌入式代码" << std::endl;
    std::cout << "例如，控制LED闪烁" << std::endl;
    
    std::cout << "\n在树莓派上，可以使用wiringPi库控制GPIO" << std::endl;
    std::cout << "例如，控制LED和读取传感器数据" << std::endl;
}

// 高性能计算示例
void highPerformanceComputing() {
    std::cout << "\n=== 高性能计算 ===" << std::endl;
    
    // 多线程计算
    std::cout << "多线程计算: " << std::endl;
    
    const int size = 10000000;
    std::vector<double> data(size);
    
    // 初始化数据
    for (int i = 0; i < size; i++) {
        data[i] = i * 0.1;
    }
    
    // 计算平方和
    double sum = 0.0;
    auto start = std::chrono::high_resolution_clock::now();
    
    for (double value : data) {
        sum += value * value;
    }
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    std::cout << "平方和: " << sum << std::endl;
    std::cout << "计算耗时: " << duration.count() << " 毫秒" << std::endl;
}

// 网络应用示例（简化版）
void webApplication() {
    std::cout << "\n=== 网络应用 ===" << std::endl;
    std::cout << "注意：完整的网络应用需要使用Web框架" << std::endl;
    std::cout << "这里仅展示基本概念" << std::endl;
    
    // 提示如何使用CppCMS、Wt等Web框架
    std::cout << "\n推荐使用CppCMS、Wt等C++ Web框架" << std::endl;
    std::cout << "例如，创建HTTP服务器和处理请求" << std::endl;
}

// 工具开发示例
void toolDevelopment() {
    std::cout << "\n=== 工具开发 ===" << std::endl;
    
    // 命令行工具示例
    std::cout << "命令行工具示例: " << std::endl;
    std::cout << "例如，创建一个简单的文本处理工具" << std::endl;
    
    // 文本处理示例
    std::string text = "Hello, C++ Tool Development!";
    std::cout << "原始文本: " << text << std::endl;
    
    // 转换为大写
    std::string upperText = text;
    for (char& c : upperText) {
        c = std::toupper(c);
    }
    std::cout << "大写文本: " << upperText << std::endl;
}

// 项目实战示例
void projectExample() {
    std::cout << "\n=== 项目实战 ===" << std::endl;
    
    // 简单的文本编辑器
    std::cout << "简单的文本编辑器: " << std::endl;
    
    // 创建临时文件
    std::ofstream tempFile("temp.txt");
    tempFile << "Hello, Project Example!" << std::endl;
    tempFile.close();
    
    // 读取文件内容
    std::ifstream inFile("temp.txt");
    std::string line;
    std::cout << "文件内容: " << std::endl;
    while (std::getline(inFile, line)) {
        std::cout << line << std::endl;
    }
    inFile.close();
    
    // 追加内容
    std::ofstream appendFile("temp.txt", std::ios::app);
    appendFile << "This is an appended line." << std::endl;
    appendFile.close();
    
    // 再次读取文件内容
    inFile.open("temp.txt");
    std::cout << "\n追加后文件内容: " << std::endl;
    while (std::getline(inFile, line)) {
        std::cout << line << std::endl;
    }
    inFile.close();
    
    // 删除临时文件
    std::filesystem::remove("temp.txt");
    std::cout << "\n临时文件已删除" << std::endl;
}

int main() {
    systemProgramming();
    networkProgramming();
    guiProgramming();
    databaseProgramming();
    gameDevelopment();
    embeddedDevelopment();
    highPerformanceComputing();
    webApplication();
    toolDevelopment();
    projectExample();
    
    return 0;
}