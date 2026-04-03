#include <iostream>
#include <exception>
#include <stdexcept>
#include <string>

// 自定义异常类
class CustomException : public std::exception {
private:
    std::string message;

public:
    CustomException(const std::string& msg) : message(msg) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
};

// 可能抛出异常的函数
int divide(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("除数不能为零");
    }
    return a / b;
}

void checkAge(int age) {
    if (age < 0) {
        throw std::invalid_argument("年龄不能为负数");
    } else if (age > 150) {
        throw CustomException("年龄超出合理范围");
    }
    std::cout << "年龄有效: " << age << std::endl;
}

// 异常安全的类
class Resource {
private:
    int* data;

public:
    Resource(int size) {
        data = new int[size];
        std::cout << "资源分配成功" << std::endl;
    }
    
    ~Resource() {
        if (data) {
            delete[] data;
            std::cout << "资源释放成功" << std::endl;
        }
    }
    
    // 模拟可能抛出异常的操作
    void doSomething(bool throwException) {
        if (throwException) {
            throw std::logic_error("模拟异常");
        }
        std::cout << "操作成功" << std::endl;
    }
};

// 使用RAII确保资源释放
void safeOperation() {
    try {
        Resource res(100);
        // 可能抛出异常
        res.doSomething(true);
    } catch (const std::exception& e) {
        std::cout << "捕获到异常: " << e.what() << std::endl;
        // 即使发生异常，Resource的析构函数也会被调用，资源会被释放
    }
}

int main() {
    // 基本异常处理
    std::cout << "=== 基本异常处理 ===" << std::endl;
    
    try {
        int result = divide(10, 0);
        std::cout << "结果: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cout << "捕获到异常: " << e.what() << std::endl;
    }
    
    // 多个异常类型
    std::cout << "\n=== 多个异常类型 ===" << std::endl;
    
    try {
        checkAge(-5);
    } catch (const std::invalid_argument& e) {
        std::cout << "无效参数异常: " << e.what() << std::endl;
    } catch (const CustomException& e) {
        std::cout << "自定义异常: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cout << "其他异常: " << e.what() << std::endl;
    }
    
    try {
        checkAge(200);
    } catch (const std::invalid_argument& e) {
        std::cout << "无效参数异常: " << e.what() << std::endl;
    } catch (const CustomException& e) {
        std::cout << "自定义异常: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cout << "其他异常: " << e.what() << std::endl;
    }
    
    // 重新抛出异常
    std::cout << "\n=== 重新抛出异常 ===" << std::endl;
    
    try {
        try {
            divide(10, 0);
        } catch (const std::exception& e) {
            std::cout << "内层捕获: " << e.what() << std::endl;
            throw; // 重新抛出异常
        }
    } catch (const std::exception& e) {
        std::cout << "外层捕获: " << e.what() << std::endl;
    }
    
    // 异常安全
    std::cout << "\n=== 异常安全 ===" << std::endl;
    safeOperation();
    
    //  noexcept
    std::cout << "\n=== noexcept ===" << std::endl;
    
    // 声明为noexcept的函数
    auto noThrowFunc = []() noexcept {
        std::cout << "这是一个不会抛出异常的函数" << std::endl;
    };
    
    noThrowFunc();
    
    // 异常规范（C++11前的语法，现在不推荐使用）
    std::cout << "\n=== 异常规范 ===" << std::endl;
    std::cout << "注意：异常规范在C++11中已被弃用，推荐使用noexcept" << std::endl;
    
    return 0;
}