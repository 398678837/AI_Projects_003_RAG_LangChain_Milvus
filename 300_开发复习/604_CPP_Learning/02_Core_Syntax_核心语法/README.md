# 核心语法

## 1. 控制流

### 1.1 条件语句

#### if语句

`if`语句用于根据条件执行不同的代码块：

```cpp
if (condition) {
    // 条件为真时执行的代码
}
```

#### if-else语句

`if-else`语句在条件为真时执行一个代码块，在条件为假时执行另一个代码块：

```cpp
if (condition) {
    // 条件为真时执行的代码
} else {
    // 条件为假时执行的代码
}
```

#### if-else if-else语句

用于处理多个条件：

```cpp
if (condition1) {
    // 条件1为真时执行的代码
} else if (condition2) {
    // 条件2为真时执行的代码
} else {
    // 所有条件都为假时执行的代码
}
```

### 1.2 循环语句

#### for循环

`for`循环用于重复执行一段代码固定次数：

```cpp
for (initialization; condition; increment) {
    // 循环体
}
```

示例：

```cpp
for (int i = 0; i < 10; i++) {
    std::cout << i << " ";
}
```

#### while循环

`while`循环在条件为真时重复执行代码块：

```cpp
while (condition) {
    // 循环体
}
```

示例：

```cpp
int i = 0;
while (i < 10) {
    std::cout << i << " ";
    i++;
}
```

#### do-while循环

`do-while`循环先执行一次循环体，然后在条件为真时继续执行：

```cpp
do {
    // 循环体
} while (condition);
```

示例：

```cpp
int i = 0;
do {
    std::cout << i << " ";
    i++;
} while (i < 10);
```

### 1.3 跳转语句

#### break语句

`break`语句用于跳出循环或switch语句：

```cpp
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break;  // 跳出循环
    }
    std::cout << i << " ";
}
```

#### continue语句

`continue`语句用于跳过当前循环的剩余部分，开始下一次循环：

```cpp
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        continue;  // 跳过偶数
    }
    std::cout << i << " ";
}
```

#### return语句

`return`语句用于从函数中返回值：

```cpp
int add(int a, int b) {
    return a + b;
}
```

## 2. 函数

### 2.1 函数定义

函数定义包括返回类型、函数名、参数列表和函数体：

```cpp
return_type function_name(parameter_list) {
    // 函数体
    return value;  // 可选
}
```

示例：

```cpp
int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}
```

### 2.2 函数声明

函数声明告诉编译器函数的存在，包括返回类型、函数名和参数列表：

```cpp
return_type function_name(parameter_list);
```

示例：

```cpp
int max(int a, int b);
```

### 2.3 函数调用

函数调用通过函数名和实际参数来执行函数：

```cpp
result = function_name(arguments);
```

示例：

```cpp
int result = max(10, 20);
std::cout << "最大值是：" << result << std::endl;
```

### 2.4 函数重载

函数重载允许使用相同的函数名但不同的参数列表：

```cpp
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}
```

### 2.5 内联函数

内联函数通过`inline`关键字声明，编译器会尝试将函数体直接插入到调用点：

```cpp
inline int square(int x) {
    return x * x;
}
```

## 3. 数组

### 3.1 一维数组

一维数组是相同类型元素的集合：

```cpp
// 声明数组
type array_name[size];

// 初始化数组
type array_name[size] = {value1, value2, ...};
```

示例：

```cpp
int numbers[5] = {1, 2, 3, 4, 5};
```

### 3.2 二维数组

二维数组是数组的数组：

```cpp
// 声明二维数组
type array_name[rows][columns];

// 初始化二维数组
type array_name[rows][columns] = {
    {value1, value2, ...},
    {value3, value4, ...},
    ...
};
```

示例：

```cpp
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

### 3.3 数组操作

#### 访问数组元素

使用索引访问数组元素：

```cpp
array_name[index];
```

示例：

```cpp
int x = numbers[2];  // 访问第三个元素（索引从0开始）
```

#### 遍历数组

使用循环遍历数组：

```cpp
for (int i = 0; i < size; i++) {
    std::cout << array_name[i] << " ";
}
```

## 4. 字符串

### 4.1 C风格字符串

C风格字符串是字符数组，以空字符`'\0'`结尾：

```cpp
char str[] = "Hello";
char str2[10] = "World";
```

### 4.2 C++字符串

C++提供了`string`类，更加方便使用：

```cpp
#include <string>

std::string str = "Hello";
std::string str2 = "World";
```

### 4.3 字符串操作

#### 字符串连接

```cpp
std::string str1 = "Hello";
std::string str2 = "World";
std::string result = str1 + " " + str2;  // 结果："Hello World"
```

#### 字符串长度

```cpp
std::string str = "Hello";
int length = str.length();  // 结果：5
```

#### 字符串比较

```cpp
std::string str1 = "Hello";
std::string str2 = "World";
if (str1 == str2) {
    // 字符串相等
} else if (str1 < str2) {
    // str1小于str2
} else {
    // str1大于str2
}
```

## 5. 指针

### 5.1 指针基础

指针是存储内存地址的变量：

```cpp
type *pointer_name;
```

示例：

```cpp
int x = 10;
int *ptr = &x;  // ptr存储x的地址
```

### 5.2 指针操作

#### 解引用

使用`*`运算符访问指针指向的值：

```cpp
int x = 10;
int *ptr = &x;
std::cout << *ptr << std::endl;  // 输出：10
```

#### 指针算术

指针可以进行算术运算：

```cpp
int arr[] = {1, 2, 3, 4, 5};
int *ptr = arr;  // 指向数组的第一个元素
ptr++;  // 指向下一个元素
```

### 5.3 空指针和野指针

- **空指针**：指向nullptr的指针
- **野指针**：指向无效内存地址的指针

```cpp
int *ptr = nullptr;  // 空指针
```

## 6. 引用

### 6.1 引用基础

引用是变量的别名，使用`&`符号声明：

```cpp
type &reference_name = variable;
```

示例：

```cpp
int x = 10;
int &ref = x;  // ref是x的别名
ref = 20;  // 修改ref会同时修改x
```

### 6.2 引用的特点

- 引用必须在声明时初始化
- 引用一旦初始化，就不能再指向其他变量
- 引用不能为null

### 6.3 引用的应用

#### 引用作为函数参数

```cpp
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}
```

#### 引用作为函数返回值

```cpp
int &getElement(int arr[], int index) {
    return arr[index];
}
```

## 7. 命名空间

### 7.1 命名空间定义

命名空间用于组织代码，避免命名冲突：

```cpp
namespace namespace_name {
    // 代码
}
```

示例：

```cpp
namespace math {
    int add(int a, int b) {
        return a + b;
    }
}
```

### 7.2 命名空间使用

#### 使用作用域解析运算符

```cpp
int result = math::add(10, 20);
```

#### 使用using声明

```cpp
using math::add;
int result = add(10, 20);
```

#### 使用using namespace

```cpp
using namespace math;
int result = add(10, 20);
```

## 8. 类型定义

### 8.1 typedef

`typedef`用于为现有类型创建别名：

```cpp
typedef type new_name;
```

示例：

```cpp
typedef int integer;
integer x = 10;
```

### 8.2 using（C++11）

C++11引入了`using`关键字来创建类型别名：

```cpp
using new_name = type;
```

示例：

```cpp
using integer = int;
integer x = 10;
```

## 9. 类型推断

### 9.1 auto关键字（C++11）

`auto`关键字让编译器自动推断变量类型：

```cpp
auto x = 10;  // x被推断为int类型
auto y = 3.14;  // y被推断为double类型
auto z = "Hello";  // z被推断为const char*类型
```

### 9.2 decltype关键字（C++11）

`decltype`关键字用于获取表达式的类型：

```cpp
decltype(expression) variable;
```

示例：

```cpp
int x = 10;
decltype(x) y = 20;  // y被声明为int类型
```

## 10. 初始化

### 10.1 列表初始化

C++11引入了列表初始化，可以使用花括号进行初始化：

```cpp
int x{10};
int arr[]{1, 2, 3, 4, 5};
std::string str{"Hello"};
```

### 10.2 统一初始化

列表初始化可以用于任何类型的初始化：

```cpp
class Person {
public:
    Person(std::string name, int age) : name(name), age(age) {}
private:
    std::string name;
    int age;
};

Person p{"Alice", 25};  // 统一初始化
```

---

**更新时间：2026-04-04**