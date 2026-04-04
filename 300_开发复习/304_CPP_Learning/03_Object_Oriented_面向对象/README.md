# 面向对象编程

## 1. 类和对象

### 1.1 类的定义

类是C++中面向对象编程的基本单位，它封装了数据和操作数据的方法：

```cpp
class ClassName {
private:
    // 私有成员变量
public:
    // 公共成员变量和方法
protected:
    // 保护成员变量和方法
};
```

示例：

```cpp
class Person {
private:
    std::string name;
    int age;
public:
    // 构造函数
    Person(std::string n, int a) : name(n), age(a) {}
    
    // 成员方法
    void setName(std::string n) {
        name = n;
    }
    
    std::string getName() {
        return name;
    }
    
    void setAge(int a) {
        age = a;
    }
    
    int getAge() {
        return age;
    }
};
```

### 1.2 对象的创建和使用

对象是类的实例：

```cpp
// 创建对象
ClassName objectName(arguments);

// 访问对象的成员
objectName.memberVariable;
objectName.memberFunction(arguments);
```

示例：

```cpp
Person person("Alice", 25);
std::cout << "Name: " << person.getName() << std::endl;
std::cout << "Age: " << person.getAge() << std::endl;
person.setAge(26);
std::cout << "Updated age: " << person.getAge() << std::endl;
```

## 2. 构造函数和析构函数

### 2.1 构造函数

构造函数是在创建对象时自动调用的特殊方法，用于初始化对象：

```cpp
class ClassName {
public:
    // 默认构造函数
    ClassName() {
        // 初始化代码
    }
    
    // 带参数的构造函数
    ClassName(parameters) {
        // 初始化代码
    }
    
    // 复制构造函数
    ClassName(const ClassName &other) {
        // 复制代码
    }
};
```

示例：

```cpp
class Person {
private:
    std::string name;
    int age;
public:
    // 默认构造函数
    Person() : name(""), age(0) {}
    
    // 带参数的构造函数
    Person(std::string n, int a) : name(n), age(a) {}
    
    // 复制构造函数
    Person(const Person &other) : name(other.name), age(other.age) {}
};
```

### 2.2 析构函数

析构函数是在对象销毁时自动调用的特殊方法，用于清理资源：

```cpp
class ClassName {
public:
    // 析构函数
    ~ClassName() {
        // 清理代码
    }
};
```

示例：

```cpp
class Resource {
private:
    int *data;
public:
    Resource(int size) {
        data = new int[size];
    }
    
    ~Resource() {
        delete[] data;
    }
};
```

## 3. 继承

### 3.1 继承的概念

继承是面向对象编程的重要特性，它允许一个类（子类）继承另一个类（父类）的属性和方法：

```cpp
class DerivedClass : accessSpecifier BaseClass {
    // 子类成员
};
```

其中，`accessSpecifier`可以是：
- `public`：公共继承
- `protected`：保护继承
- `private`：私有继承

示例：

```cpp
class Animal {
public:
    void eat() {
        std::cout << "Animal is eating" << std::endl;
    }
};

class Dog : public Animal {
public:
    void bark() {
        std::cout << "Dog is barking" << std::endl;
    }
};
```

### 3.2 继承的访问控制

| 父类成员访问级别 | 公共继承 | 保护继承 | 私有继承 |
|------------------|----------|----------|----------|
| public           | public   | protected | private  |
| protected        | protected | protected | private  |
| private          | 不可访问  | 不可访问  | 不可访问  |

### 3.3 构造函数和析构函数的继承

- 子类构造函数会调用父类的构造函数
- 子类析构函数会调用父类的析构函数

```cpp
class Base {
public:
    Base() {
        std::cout << "Base constructor" << std::endl;
    }
    
    ~Base() {
        std::cout << "Base destructor" << std::endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        std::cout << "Derived constructor" << std::endl;
    }
    
    ~Derived() {
        std::cout << "Derived destructor" << std::endl;
    }
};
```

## 4. 多态

### 4.1 多态的概念

多态是面向对象编程的重要特性，它允许不同类型的对象对相同的消息做出不同的响应：

### 4.2 虚函数

虚函数是在基类中声明的，允许在派生类中重写的函数：

```cpp
class Base {
public:
    virtual void function() {
        std::cout << "Base function" << std::endl;
    }
};

class Derived : public Base {
public:
    void function() override {
        std::cout << "Derived function" << std::endl;
    }
};
```

### 4.3 纯虚函数和抽象类

纯虚函数是没有实现的虚函数，包含纯虚函数的类称为抽象类：

```cpp
class AbstractClass {
public:
    virtual void pureVirtualFunction() = 0;  // 纯虚函数
};
```

### 4.4 多态的应用

```cpp
void printFunction(Base *obj) {
    obj->function();  // 多态调用
}

int main() {
    Base base;
    Derived derived;
    
    printFunction(&base);  // 输出：Base function
    printFunction(&derived);  // 输出：Derived function
    
    return 0;
}
```

## 5. 封装

### 5.1 封装的概念

封装是面向对象编程的重要特性，它将数据和操作数据的方法封装在一起，对外部隐藏实现细节：

### 5.2 访问控制

C++提供了三种访问控制修饰符：
- `public`：公共成员，可以被任何代码访问
- `protected`：保护成员，只能被类本身和派生类访问
- `private`：私有成员，只能被类本身访问

示例：

```cpp
class Person {
private:
    std::string name;  // 私有成员，只能被类本身访问
protected:
    int age;  // 保护成员，只能被类本身和派生类访问
public:
    void setName(std::string n) {  // 公共成员，可以被任何代码访问
        name = n;
    }
    
    std::string getName() {
        return name;
    }
};
```

## 6. 抽象

### 6.1 抽象的概念

抽象是面向对象编程的重要特性，它允许我们关注对象的本质特征，忽略非本质细节：

### 6.2 抽象类和接口

- **抽象类**：包含至少一个纯虚函数的类，不能实例化
- **接口**：只包含纯虚函数的抽象类

示例：

```cpp
// 接口
class Shape {
public:
    virtual double area() = 0;
    virtual double perimeter() = 0;
};

// 实现接口的类
class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    
    double area() override {
        return 3.14159 * radius * radius;
    }
    
    double perimeter() override {
        return 2 * 3.14159 * radius;
    }
};
```

## 7. 静态成员

### 7.1 静态成员变量

静态成员变量是属于类的变量，而不是属于对象的变量：

```cpp
class ClassName {
public:
    static type staticVariable;
};

// 在类外部初始化静态成员变量
type ClassName::staticVariable = value;
```

示例：

```cpp
class Counter {
public:
    static int count;
    
    Counter() {
        count++;
    }
};

int Counter::count = 0;
```

### 7.2 静态成员函数

静态成员函数是属于类的函数，而不是属于对象的函数：

```cpp
class ClassName {
public:
    static returnType staticFunction(parameters) {
        // 函数体
    }
};
```

示例：

```cpp
class Math {
public:
    static int add(int a, int b) {
        return a + b;
    }
    
    static int multiply(int a, int b) {
        return a * b;
    }
};
```

## 8. 友元

### 8.1 友元函数

友元函数是可以访问类的私有成员的非成员函数：

```cpp
class ClassName {
    friend returnType friendFunction(parameters);
};
```

示例：

```cpp
class Rectangle {
private:
    int width;
    int height;
public:
    Rectangle(int w, int h) : width(w), height(h) {}
    
    friend int area(Rectangle r);
};

int area(Rectangle r) {
    return r.width * r.height;
}
```

### 8.2 友元类

友元类是可以访问另一个类的私有成员的类：

```cpp
class ClassName {
    friend class FriendClass;
};
```

示例：

```cpp
class A {
private:
    int value;
public:
    A(int v) : value(v) {}
    
    friend class B;
};

class B {
public:
    void printValue(A a) {
        std::cout << "A's value: " << a.value << std::endl;
    }
};
```

## 9. 运算符重载

### 9.1 运算符重载的概念

运算符重载允许我们为自定义类型定义运算符的行为：

```cpp
class ClassName {
public:
    returnType operator op(parameters) {
        // 运算符实现
    }
};
```

### 9.2 重载常见运算符

#### 算术运算符

```cpp
class Vector {
private:
    int x;
    int y;
public:
    Vector(int x, int y) : x(x), y(y) {}
    
    Vector operator+(const Vector &other) {
        return Vector(x + other.x, y + other.y);
    }
    
    Vector operator-(const Vector &other) {
        return Vector(x - other.x, y - other.y);
    }
};
```

#### 关系运算符

```cpp
class Person {
private:
    std::string name;
    int age;
public:
    Person(std::string name, int age) : name(name), age(age) {}
    
    bool operator==(const Person &other) {
        return name == other.name && age == other.age;
    }
    
    bool operator<(const Person &other) {
        return age < other.age;
    }
};
```

## 10. 特殊成员函数

### 10.1 移动构造函数和移动赋值运算符（C++11）

移动构造函数和移动赋值运算符用于高效地转移资源：

```cpp
class ClassName {
public:
    // 移动构造函数
    ClassName(ClassName &&other) noexcept {
        // 转移资源
    }
    
    // 移动赋值运算符
    ClassName &operator=(ClassName &&other) noexcept {
        if (this != &other) {
            // 释放当前资源
            // 转移资源
        }
        return *this;
    }
};
```

### 10.2 复制省略和返回值优化

C++11引入了复制省略和返回值优化，减少不必要的复制操作：

```cpp
class ClassName {
public:
    ClassName() {
        std::cout << "Constructor" << std::endl;
    }
    
    ClassName(const ClassName &) {
        std::cout << "Copy constructor" << std::endl;
    }
    
    ClassName(ClassName &&) {
        std::cout << "Move constructor" << std::endl;
    }
};

ClassName createObject() {
    return ClassName();  // 返回值优化，不会调用复制或移动构造函数
}
```

---

**更新时间：2026-04-04**