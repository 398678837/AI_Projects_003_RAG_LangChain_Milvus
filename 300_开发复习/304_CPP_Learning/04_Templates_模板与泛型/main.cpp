#include <iostream>
#include <string>
#include <vector>

// 函数模板 - 最大值
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// 函数模板 - 打印数组
template <typename T>
void printArray(const T* array, int size) {
    for (int i = 0; i < size; i++) {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
}

// 类模板 - 栈
template <typename T>
class Stack {
private:
    std::vector<T> elements;

public:
    // 压栈
    void push(const T& item) {
        elements.push_back(item);
    }
    
    // 出栈
    void pop() {
        if (!empty()) {
            elements.pop_back();
        }
    }
    
    // 获取栈顶元素
    T top() const {
        if (!empty()) {
            return elements.back();
        }
        throw std::out_of_range("Stack is empty");
    }
    
    // 检查是否为空
    bool empty() const {
        return elements.empty();
    }
    
    // 获取大小
    size_t size() const {
        return elements.size();
    }
};

// 类模板特化 - 针对字符串的栈
template <>
class Stack<std::string> {
private:
    std::vector<std::string> elements;

public:
    // 压栈
    void push(const std::string& item) {
        elements.push_back(item);
        std::cout << "Pushed string: " << item << std::endl;
    }
    
    // 出栈
    void pop() {
        if (!empty()) {
            std::cout << "Popped string: " << elements.back() << std::endl;
            elements.pop_back();
        }
    }
    
    // 获取栈顶元素
    std::string top() const {
        if (!empty()) {
            return elements.back();
        }
        throw std::out_of_range("Stack is empty");
    }
    
    // 检查是否为空
    bool empty() const {
        return elements.empty();
    }
    
    // 获取大小
    size_t size() const {
        return elements.size();
    }
};

// 可变参数模板 - 打印多个值
void print() {
    std::cout << std::endl;
}

template <typename T, typename... Args>
void print(T first, Args... rest) {
    std::cout << first << " ";
    print(rest...);
}

// 可变参数模板 - 计算总和
template <typename T>
T sum(T value) {
    return value;
}

template <typename T, typename... Args>
T sum(T first, Args... rest) {
    return first + sum(rest...);
}

int main() {
    // 测试函数模板
    std::cout << "=== 函数模板测试 ===" << std::endl;
    
    // 测试max函数
    int a = 10, b = 20;
    std::cout << "max(" << a << ", " << b << ") = " << max(a, b) << std::endl;
    
    double x = 3.14, y = 2.71;
    std::cout << "max(" << x << ", " << y << ") = " << max(x, y) << std::endl;
    
    std::string s1 = "hello", s2 = "world";
    std::cout << "max(\"" << s1 << "\", \"" << s2 << "\") = " << max(s1, s2) << std::endl;
    
    // 测试printArray函数
    int intArray[] = {1, 2, 3, 4, 5};
    std::cout << "int数组: ";
    printArray(intArray, 5);
    
    double doubleArray[] = {1.1, 2.2, 3.3, 4.4, 5.5};
    std::cout << "double数组: ";
    printArray(doubleArray, 5);
    
    // 测试类模板
    std::cout << "\n=== 类模板测试 ===" << std::endl;
    
    // 测试整数栈
    Stack<int> intStack;
    intStack.push(10);
    intStack.push(20);
    intStack.push(30);
    std::cout << "整数栈大小: " << intStack.size() << std::endl;
    std::cout << "栈顶元素: " << intStack.top() << std::endl;
    intStack.pop();
    std::cout << "弹出后栈顶元素: " << intStack.top() << std::endl;
    
    // 测试字符串栈（特化版本）
    Stack<std::string> stringStack;
    stringStack.push("Hello");
    stringStack.push("World");
    stringStack.push("C++");
    std::cout << "字符串栈大小: " << stringStack.size() << std::endl;
    std::cout << "栈顶元素: " << stringStack.top() << std::endl;
    stringStack.pop();
    std::cout << "弹出后栈顶元素: " << stringStack.top() << std::endl;
    
    // 测试可变参数模板
    std::cout << "\n=== 可变参数模板测试 ===" << std::endl;
    
    // 测试print函数
    std::cout << "打印多个值: ";
    print(1, 2.5, "Hello", true);
    
    // 测试sum函数
    std::cout << "sum(1, 2, 3, 4, 5) = " << sum(1, 2, 3, 4, 5) << std::endl;
    std::cout << "sum(1.1, 2.2, 3.3) = " << sum(1.1, 2.2, 3.3) << std::endl;
    
    return 0;
}