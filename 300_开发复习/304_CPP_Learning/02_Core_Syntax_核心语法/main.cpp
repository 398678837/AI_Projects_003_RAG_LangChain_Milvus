#include <iostream>
#include <string>

// 函数声明
int add(int a, int b);
double calculate_area(double radius);
void print_array(int arr[], int size);

int main() {
    // 控制流 - 条件语句
    std::cout << "=== 条件语句 ===" << std::endl;
    
    int score = 85;
    if (score >= 90) {
        std::cout << "优秀" << std::endl;
    } else if (score >= 80) {
        std::cout << "良好" << std::endl;
    } else if (score >= 60) {
        std::cout << "及格" << std::endl;
    } else {
        std::cout << "不及格" << std::endl;
    }
    
    // 控制流 - 循环语句
    std::cout << "\n=== 循环语句 ===" << std::endl;
    
    // for循环
    std::cout << "for循环: " << std::endl;
    for (int i = 1; i <= 5; i++) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    
    // while循环
    std::cout << "while循环: " << std::endl;
    int j = 1;
    while (j <= 5) {
        std::cout << j << " ";
        j++;
    }
    std::cout << std::endl;
    
    // do-while循环
    std::cout << "do-while循环: " << std::endl;
    int k = 1;
    do {
        std::cout << k << " ";
        k++;
    } while (k <= 5);
    std::cout << std::endl;
    
    // 函数调用
    std::cout << "\n=== 函数调用 ===" << std::endl;
    
    int sum = add(10, 20);
    std::cout << "10 + 20 = " << sum << std::endl;
    
    double area = calculate_area(5.0);
    std::cout << "半径为5的圆面积: " << area << std::endl;
    
    // 数组
    std::cout << "\n=== 数组 ===" << std::endl;
    
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    std::cout << "数组元素: " << std::endl;
    print_array(numbers, size);
    
    // 字符串
    std::cout << "\n=== 字符串 ===" << std::endl;
    
    // C风格字符串
    char c_string[] = "Hello, C string!";
    std::cout << "C风格字符串: " << c_string << std::endl;
    
    // C++字符串
    std::string cpp_string = "Hello, C++ string!";
    std::cout << "C++字符串: " << cpp_string << std::endl;
    
    // 字符串操作
    cpp_string += " Welcome!";
    std::cout << "字符串连接: " << cpp_string << std::endl;
    std::cout << "字符串长度: " << cpp_string.length() << std::endl;
    
    // 指针
    std::cout << "\n=== 指针 ===" << std::endl;
    
    int x = 100;
    int* ptr = &x;
    
    std::cout << "x的值: " << x << std::endl;
    std::cout << "x的地址: " << &x << std::endl;
    std::cout << "指针ptr的值: " << ptr << std::endl;
    std::cout << "指针ptr指向的值: " << *ptr << std::endl;
    
    // 修改指针指向的值
    *ptr = 200;
    std::cout << "修改后x的值: " << x << std::endl;
    
    // 引用
    std::cout << "\n=== 引用 ===" << std::endl;
    
    int y = 50;
    int& ref = y;
    
    std::cout << "y的值: " << y << std::endl;
    std::cout << "引用ref的值: " << ref << std::endl;
    
    // 通过引用修改值
    ref = 150;
    std::cout << "修改后y的值: " << y << std::endl;
    
    return 0;
}

// 函数定义
int add(int a, int b) {
    return a + b;
}

double calculate_area(double radius) {
    const double PI = 3.14159;
    return PI * radius * radius;
}

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}