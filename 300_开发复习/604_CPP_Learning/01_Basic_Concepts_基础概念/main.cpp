#include <iostream>
#include <iomanip>

int main() {
    // 基本数据类型
    std::cout << "=== 基本数据类型 ===" << std::endl;
    
    bool b = true;
    char c = 'A';
    int i = 10;
    float f = 3.14f;
    double d = 3.14159;
    
    std::cout << "bool: " << b << std::endl;
    std::cout << "char: " << c << std::endl;
    std::cout << "int: " << i << std::endl;
    std::cout << "float: " << f << std::endl;
    std::cout << "double: " << d << std::endl;
    
    // 变量和常量
    std::cout << "\n=== 变量和常量 ===" << std::endl;
    
    int age = 25;
    const double PI = 3.14159;
    
    std::cout << "age: " << age << std::endl;
    std::cout << "PI: " << PI << std::endl;
    
    // 运算符
    std::cout << "\n=== 运算符 ===" << std::endl;
    
    int a = 10, e = 3;
    std::cout << "a + e: " << a + e << std::endl;
    std::cout << "a - e: " << a - e << std::endl;
    std::cout << "a * e: " << a * e << std::endl;
    std::cout << "a / e: " << a / e << std::endl;
    std::cout << "a % e: " << a % e << std::endl;
    
    // 输入输出
    std::cout << "\n=== 输入输出 ===" << std::endl;
    
    int num;
    std::cout << "请输入一个数字: ";
    std::cin >> num;
    std::cout << "你输入的数字是: " << num << std::endl;
    
    // 格式化输出
    std::cout << "\n=== 格式化输出 ===" << std::endl;
    
    double pi = 3.1415926535;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "PI = " << pi << std::endl;
    
    return 0;
}