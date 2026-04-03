#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <chrono>
#include <cstring>

// 代码规范示例
namespace best_practices {
    // 命名规范
    const int MAX_BUFFER_SIZE = 1024; // 常量使用大写
    
    // 类名使用驼峰命名法
    class FileHandler {
    private:
        // 成员变量使用下划线结尾
        std::string filename_;
        
    public:
        // 构造函数
        FileHandler(const std::string& filename) : filename_(filename) {}
        
        // 成员函数使用驼峰命名法
        bool openFile() {
            std::cout << "打开文件: " << filename_ << std::endl;
            return true;
        }
    };
    
    // 函数使用驼峰命名法
    int calculateSum(const std::vector<int>& numbers) {
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        return sum;
    }
}

// 性能优化示例
class PerformanceOptimization {
public:
    // 避免不必要的复制
    std::string concatenateStrings(const std::vector<std::string>& strings) {
        std::string result;
        // 预分配内存
        size_t totalLength = 0;
        for (const auto& str : strings) {
            totalLength += str.length();
        }
        result.reserve(totalLength);
        
        // 拼接字符串
        for (const auto& str : strings) {
            result += str;
        }
        return result;
    }
    
    // 使用移动语义
    std::vector<int> createLargeVector() {
        std::vector<int> vec(1000000, 42);
        return vec; // 自动移动
    }
    
    // 缓存计算结果
    int fibonacci(int n) {
        static std::vector<int> cache = {0, 1};
        
        if (n < cache.size()) {
            return cache[n];
        }
        
        for (int i = cache.size(); i <= n; i++) {
            cache.push_back(cache[i-1] + cache[i-2]);
        }
        return cache[n];
    }
};

// 安全性示例
class SecurityExample {
public:
    // 安全的字符串复制
    void safeStringCopy(char* dest, const char* src, size_t destSize) {
        if (dest && src && destSize > 0) {
            strncpy(dest, src, destSize - 1);
            dest[destSize - 1] = '\0';
        }
    }
    
    // 空指针检查
    void processPointer(int* ptr) {
        if (ptr) {
            std::cout << "指针值: " << *ptr << std::endl;
        } else {
            std::cout << "空指针" << std::endl;
        }
    }
    
    // 异常安全
    void exceptionSafeOperation() {
        std::unique_ptr<int> resource = std::make_unique<int>(42);
        
        // 即使发生异常，resource也会被自动释放
        if (true) {
            throw std::runtime_error("模拟异常");
        }
    }
};

// 可维护性示例
class MaintainabilityExample {
public:
    // 函数分解
    void processUserData(const std::string& name, int age, const std::string& email) {
        validateUserData(name, age, email);
        saveUserData(name, age, email);
        sendConfirmationEmail(email);
    }
    
    // 私有辅助函数
private:
    void validateUserData(const std::string& name, int age, const std::string& email) {
        // 验证逻辑
        std::cout << "验证用户数据" << std::endl;
    }
    
    void saveUserData(const std::string& name, int age, const std::string& email) {
        // 保存逻辑
        std::cout << "保存用户数据" << std::endl;
    }
    
    void sendConfirmationEmail(const std::string& email) {
        // 发送邮件逻辑
        std::cout << "发送确认邮件到: " << email << std::endl;
    }
};

// 现代C++特性示例
class ModernCppFeatures {
public:
    // 自动类型推断
    void autoTypeDeduction() {
        auto i = 42; // int
        auto d = 3.14; // double
        auto s = "Hello"; // const char*
        auto vec = std::vector<int>{1, 2, 3}; // std::vector<int>
        
        std::cout << "auto类型推断示例" << std::endl;
    }
    
    // 范围for循环
    void rangeBasedFor() {
        std::vector<int> numbers = {1, 2, 3, 4, 5};
        
        std::cout << "范围for循环: ";
        for (auto num : numbers) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
    
    // Lambda表达式
    void lambdaExpressions() {
        std::vector<int> numbers = {5, 2, 8, 1, 9};
        
        // 排序
        std::sort(numbers.begin(), numbers.end(), [](int a, int b) {
            return a < b;
        });
        
        std::cout << "Lambda排序结果: ";
        for (auto num : numbers) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
    
    // 智能指针
    void smartPointers() {
        // unique_ptr
        std::unique_ptr<int> uniquePtr = std::make_unique<int>(42);
        
        // shared_ptr
        std::shared_ptr<int> sharedPtr = std::make_shared<int>(100);
        
        std::cout << "智能指针示例" << std::endl;
    }
};

// 性能测试
void performanceTest() {
    std::cout << "=== 性能测试 ===" << std::endl;
    
    PerformanceOptimization opt;
    
    // 测试字符串拼接
    auto start = std::chrono::high_resolution_clock::now();
    
    std::vector<std::string> strings(1000, "Hello, World! ");
    std::string result = opt.concatenateStrings(strings);
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "字符串拼接耗时: " << duration.count() << " 微秒" << std::endl;
    
    // 测试斐波那契数列
    start = std::chrono::high_resolution_clock::now();
    
    int fib = opt.fibonacci(40);
    std::cout << "斐波那契数列第40项: " << fib << std::endl;
    
    end = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "斐波那契计算耗时: " << duration.count() << " 微秒" << std::endl;
}

int main() {
    // 代码规范
    std::cout << "=== 代码规范 ===" << std::endl;
    best_practices::FileHandler handler("example.txt");
    handler.openFile();
    
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    int sum = best_practices::calculateSum(numbers);
    std::cout << "数字总和: " << sum << std::endl;
    
    // 性能优化
    std::cout << "\n=== 性能优化 ===" << std::endl;
    PerformanceOptimization opt;
    
    std::vector<std::string> strings = {"Hello", " ", "World", "!"};
    std::string concatenated = opt.concatenateStrings(strings);
    std::cout << "拼接结果: " << concatenated << std::endl;
    
    std::vector<int> largeVec = opt.createLargeVector();
    std::cout << "大向量大小: " << largeVec.size() << std::endl;
    
    // 安全性
    std::cout << "\n=== 安全性 ===" << std::endl;
    SecurityExample sec;
    
    char buffer[20];
    sec.safeStringCopy(buffer, "This is a test", sizeof(buffer));
    std::cout << "安全字符串复制: " << buffer << std::endl;
    
    int value = 100;
    sec.processPointer(&value);
    sec.processPointer(nullptr);
    
    // 可维护性
    std::cout << "\n=== 可维护性 ===" << std::endl;
    MaintainabilityExample maintain;
    maintain.processUserData("Alice", 25, "alice@example.com");
    
    // 现代C++特性
    std::cout << "\n=== 现代C++特性 ===" << std::endl;
    ModernCppFeatures modern;
    modern.autoTypeDeduction();
    modern.rangeBasedFor();
    modern.lambdaExpressions();
    modern.smartPointers();
    
    // 性能测试
    performanceTest();
    
    return 0;
}