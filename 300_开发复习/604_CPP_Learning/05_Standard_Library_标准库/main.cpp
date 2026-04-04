#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iterator>
#include <memory>
#include <string>
#include <sstream>
#include <fstream>
#include <chrono>

int main() {
    // 序列容器
    std::cout << "=== 序列容器 ===" << std::endl;
    
    // vector
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::cout << "vector: ";
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // list
    std::list<int> lst = {10, 20, 30, 40, 50};
    std::cout << "list: ";
    for (int num : lst) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // 关联容器
    std::cout << "\n=== 关联容器 ===" << std::endl;
    
    // map
    std::map<std::string, int> studentScores;
    studentScores["Alice"] = 95;
    studentScores["Bob"] = 88;
    studentScores["Charlie"] = 92;
    std::cout << "map: " << std::endl;
    for (const auto& pair : studentScores) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    // set
    std::set<int> uniqueNumbers = {1, 2, 2, 3, 4, 4, 5};
    std::cout << "set: ";
    for (int num : uniqueNumbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // 无序容器
    std::cout << "\n=== 无序容器 ===" << std::endl;
    
    // unordered_map
    std::unordered_map<std::string, std::string> capitals;
    capitals["China"] = "Beijing";
    capitals["USA"] = "Washington";
    capitals["Japan"] = "Tokyo";
    std::cout << "unordered_map: " << std::endl;
    for (const auto& pair : capitals) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    // unordered_set
    std::unordered_set<int> hashSet = {10, 20, 30, 40, 50};
    std::cout << "unordered_set: ";
    for (int num : hashSet) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // 算法
    std::cout << "\n=== 算法 ===" << std::endl;
    
    std::vector<int> numbers = {5, 2, 8, 1, 9, 3};
    
    // 排序
    std::sort(numbers.begin(), numbers.end());
    std::cout << "排序后: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // 查找
    int target = 8;
    auto it = std::find(numbers.begin(), numbers.end(), target);
    if (it != numbers.end()) {
        std::cout << "找到 " << target << " 在位置 " << std::distance(numbers.begin(), it) << std::endl;
    } else {
        std::cout << "未找到 " << target << std::endl;
    }
    
    // 计数
    int count = std::count(numbers.begin(), numbers.end(), 3);
    std::cout << "数字3出现的次数: " << count << std::endl;
    
    // 智能指针
    std::cout << "\n=== 智能指针 ===" << std::endl;
    
    // unique_ptr
    std::unique_ptr<int> uniquePtr = std::make_unique<int>(42);
    std::cout << "unique_ptr: " << *uniquePtr << std::endl;
    
    // shared_ptr
    std::shared_ptr<int> sharedPtr1 = std::make_shared<int>(100);
    std::shared_ptr<int> sharedPtr2 = sharedPtr1;
    std::cout << "shared_ptr1: " << *sharedPtr1 << std::endl;
    std::cout << "shared_ptr2: " << *sharedPtr2 << std::endl;
    std::cout << "引用计数: " << sharedPtr1.use_count() << std::endl;
    
    // weak_ptr
    std::weak_ptr<int> weakPtr = sharedPtr1;
    if (auto lockedPtr = weakPtr.lock()) {
        std::cout << "weak_ptr 锁定后: " << *lockedPtr << std::endl;
    }
    
    // 字符串库
    std::cout << "\n=== 字符串库 ===" << std::endl;
    
    std::string str = "Hello, C++ Standard Library!";
    std::cout << "原始字符串: " << str << std::endl;
    std::cout << "字符串长度: " << str.length() << std::endl;
    std::cout << "子字符串: " << str.substr(7, 3) << std::endl;
    
    // 输入输出库
    std::cout << "\n=== 输入输出库 ===" << std::endl;
    
    // 字符串流
    std::stringstream ss;
    ss << "Name: " << "Alice" << ", Age: " << 25;
    std::string result = ss.str();
    std::cout << "字符串流结果: " << result << std::endl;
    
    // 文件操作
    std::ofstream outFile("test.txt");
    if (outFile.is_open()) {
        outFile << "Hello from C++ Standard Library!" << std::endl;
        outFile.close();
        std::cout << "文件写入成功" << std::endl;
    }
    
    std::ifstream inFile("test.txt");
    if (inFile.is_open()) {
        std::string line;
        std::getline(inFile, line);
        std::cout << "文件内容: " << line << std::endl;
        inFile.close();
    }
    
    // 时间库
    std::cout << "\n=== 时间库 ===" << std::endl;
    
    // 获取当前时间
    auto now = std::chrono::system_clock::now();
    std::time_t currentTime = std::chrono::system_clock::to_time_t(now);
    std::cout << "当前时间: " << std::ctime(&currentTime);
    
    // 计时
    auto start = std::chrono::high_resolution_clock::now();
    
    // 模拟一些操作
    for (int i = 0; i < 1000000; i++) {
        // 空循环
    }
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "操作耗时: " << duration.count() << " 微秒" << std::endl;
    
    return 0;
}