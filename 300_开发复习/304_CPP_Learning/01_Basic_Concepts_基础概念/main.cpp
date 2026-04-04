#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    cout << "=== 基本数据类型 ===" << endl;
    
    // 基本数据类型
    bool b = true;
    char c = 'A';
    int i = 10;
    float f = 3.14f;
    double d = 3.14159;
    string s = "Hello, C++!";
    
    cout << "bool: " << b << endl;
    cout << "char: " << c << endl;
    cout << "int: " << i << endl;
    cout << "float: " << f << endl;
    cout << "double: " << d << endl;
    cout << "string: " << s << endl;
    
    cout << "\n=== 变量和常量 ===" << endl;
    
    // 变量和常量
    int age = 25;
    const double PI = 3.14159;
    
    cout << "age: " << age << endl;
    cout << "PI: " << PI << endl;
    
    cout << "\n=== 运算符 ===" << endl;
    
    // 运算符
    int a = 10, e = 3;
    cout << "a + e: " << a + e << endl;
    cout << "a - e: " << a - e << endl;
    cout << "a * e: " << a * e << endl;
    cout << "a / e: " << a / e << endl;
    cout << "a % e: " << a % e << endl;
    
    cout << "\n=== 类型转换 ===" << endl;
    
    // 类型转换
    int intValue = 100;
    double doubleValue = intValue; // 隐式转换
    intValue = static_cast<int>(doubleValue); // 显式转换
    
    cout << "intValue: " << intValue << endl;
    cout << "doubleValue: " << doubleValue << endl;
    
    cout << "\n=== 字符串操作 ===" << endl;
    
    // 字符串操作
    string str1 = "Hello";
    string str2 = "World";
    string str3 = str1 + " " + str2;
    
    cout << "str3: " << str3 << endl;
    cout << "str3.length(): " << str3.length() << endl;
    cout << "str3.substr(0, 5): " << str3.substr(0, 5) << endl;
    
    cout << "\n=== 格式化输出 ===" << endl;
    
    // 格式化输出
    cout << fixed << setprecision(2);
    cout << "PI = " << PI << endl;
    
    cout << "\n=== 结束 ===" << endl;
    cout << "程序运行完成！" << endl;
    
    return 0;
}