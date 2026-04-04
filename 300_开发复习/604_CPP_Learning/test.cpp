#include <iostream>
#include <vector>
#include <string>

int main() {
    std::cout << "=== C++环境测试 ===" << std::endl;
    
    // 测试基本输入输出
    std::cout << "Hello, C++!" << std::endl;
    
    // 测试向量容器
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    std::cout << "Vector size: " << numbers.size() << std::endl;
    
    // 测试字符串
    std::string str = "C++ is powerful!";
    std::cout << "String: " << str << std::endl;
    
    // 测试循环
    std::cout << "Numbers: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    std::cout << "=== 测试成功! ===" << std::endl;
    
    return 0;
}