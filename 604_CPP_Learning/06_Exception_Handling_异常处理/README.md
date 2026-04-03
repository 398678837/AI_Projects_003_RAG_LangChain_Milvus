# 异常处理

## 1. 异常处理基础

### 1.1 异常的概念

异常是程序运行过程中发生的特殊情况，如除以零、数组越界、内存分配失败等。C++提供了异常处理机制，允许程序在发生异常时进行适当的处理，而不是直接崩溃。

### 1.2 异常处理的语法

C++的异常处理使用三个关键字：`try`、`catch`和`throw`：

- `try`：包含可能抛出异常的代码块
- `catch`：捕获并处理异常
- `throw`：抛出异常

```cpp
try {
    // 可能抛出异常的代码
    if (condition) {
        throw exception;
    }
} catch (exception_type1 e) {
    // 处理异常类型1
} catch (exception_type2 e) {
    // 处理异常类型2
} catch (...) {
    // 处理所有其他类型的异常
}
```

## 2. 异常的抛出和捕获

### 2.1 抛出异常

使用`throw`关键字抛出异常：

```cpp
void divide(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("Division by zero");
    }
    std::cout << "Result: " << a / b << std::endl;
}
```

### 2.2 捕获异常

使用`catch`关键字捕获异常：

```cpp
try {
    divide(10, 0);
} catch (const std::runtime_error& e) {
    std::cout << "Error: " << e.what() << std::endl;
}
```

### 2.3 异常的传递

如果异常在函数中被抛出但没有被捕获，它会传递给调用函数：

```cpp
void function1() {
    function2();
}

void function2() {
    function3();
}

void function3() {
    throw std::runtime_error("Error");
}

int main() {
    try {
        function1();
    } catch (const std::runtime_error& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## 3. 标准异常

### 3.1 标准异常层次结构

C++标准库提供了一系列标准异常类，它们都派生自`std::exception`：

- `std::exception`：所有标准异常的基类
- `std::bad_alloc`：内存分配失败
- `std::bad_cast`：类型转换失败
- `std::bad_typeid`：`typeid`操作失败
- `std::logic_error`：逻辑错误
  - `std::domain_error`：域错误
  - `std::invalid_argument`：无效参数
  - `std::length_error`：长度错误
  - `std::out_of_range`：超出范围
- `std::runtime_error`：运行时错误
  - `std::range_error`：范围错误
  - `std::overflow_error`：溢出错误
  - `std::underflow_error`：下溢错误

### 3.2 使用标准异常

```cpp
#include <stdexcept>

void checkAge(int age) {
    if (age < 0) {
        throw std::invalid_argument("Age cannot be negative");
    } else if (age > 150) {
        throw std::out_of_range("Age is too large");
    }
    std::cout << "Age is valid: " << age << std::endl;
}

int main() {
    try {
        checkAge(-10);
    } catch (const std::invalid_argument& e) {
        std::cout << "Invalid argument: " << e.what() << std::endl;
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << std::endl;
    }
    return 0;
}
```

## 4. 自定义异常

### 4.1 自定义异常类

我们可以通过继承`std::exception`或其派生类来创建自定义异常：

```cpp
class MyException : public std::exception {
private:
    std::string message;
public:
    MyException(const std::string& msg) : message(msg) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
};
```

### 4.2 使用自定义异常

```cpp
void process(int value) {
    if (value < 0) {
        throw MyException("Value cannot be negative");
    }
    std::cout << "Processing value: " << value << std::endl;
}

int main() {
    try {
        process(-5);
    } catch (const MyException& e) {
        std::cout << "MyException: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Standard exception: " << e.what() << std::endl;
    }
    return 0;
}
```

## 5. 异常安全

### 5.1 异常安全级别

异常安全是指程序在发生异常时保持一致性的能力，C++定义了三个异常安全级别：

- **无抛出保证**：函数不会抛出任何异常
- **基本异常安全**：函数抛出异常时，程序状态保持一致，但资源可能泄漏
- **强异常安全**：函数抛出异常时，程序状态完全回滚到调用前的状态

### 5.2 异常安全的实现

#### RAII（资源获取即初始化）

RAII是一种管理资源的技术，确保资源在对象创建时获取，在对象销毁时释放：

```cpp
class File {
private:
    FILE* fp;
public:
    File(const char* filename, const char* mode) {
        fp = fopen(filename, mode);
        if (fp == nullptr) {
            throw std::runtime_error("Failed to open file");
        }
    }
    
    ~File() {
        if (fp) {
            fclose(fp);
        }
    }
    
    FILE* get() {
        return fp;
    }
};

void processFile(const char* filename) {
    File file(filename, "r");
    // 使用文件
    // 如果发生异常，file的析构函数会自动关闭文件
}
```

#### 智能指针

智能指针是RAII的一种实现，确保内存资源的正确释放：

```cpp
void process() {
    std::unique_ptr<int> ptr(new int(10));
    // 使用ptr
    // 如果发生异常，ptr的析构函数会自动释放内存
}
```

## 6. 异常处理的最佳实践

### 6.1 何时使用异常

- **使用异常处理**：处理程序逻辑之外的错误，如资源分配失败、无效的输入等
- **不使用异常处理**：处理程序逻辑之内的错误，如用户输入验证等

### 6.2 异常处理的准则

- **只抛出有意义的异常**：异常应该包含足够的信息，以便调用者能够理解错误
- **捕获具体的异常**：优先捕获具体的异常类型，而不是使用通用的`catch(...)`
- **不要在析构函数中抛出异常**：析构函数应该是无抛出的
- **使用RAII管理资源**：确保资源在异常发生时能够正确释放
- **保持异常的层次结构**：创建有意义的异常层次结构

### 6.3 异常处理的性能考虑

- **异常处理会增加运行时开销**：只有在真正需要时才使用异常
- **异常应该用于特殊情况**：不要将异常用于常规的控制流
- **避免在性能关键代码中使用异常**：如循环内部

## 7. 异常与构造函数和析构函数

### 7.1 构造函数中的异常

构造函数可以抛出异常，但如果构造函数抛出异常，析构函数不会被调用：

```cpp
class Resource {
private:
    int* data;
public:
    Resource(int size) {
        data = new int[size];
        // 如果这里抛出异常，data不会被释放
        // 会导致内存泄漏
    }
    
    ~Resource() {
        delete[] data;
    }
};
```

为了避免内存泄漏，应该使用RAII或智能指针：

```cpp
class Resource {
private:
    std::unique_ptr<int[]> data;
public:
    Resource(int size) : data(new int[size]) {
        // 如果这里抛出异常，data的析构函数会自动释放内存
    }
};
```

### 7.2 析构函数中的异常

析构函数不应该抛出异常，因为如果析构函数在处理另一个异常时抛出异常，程序会终止：

```cpp
class BadClass {
public:
    ~BadClass() {
        throw std::runtime_error("Error in destructor");
    }
};

int main() {
    try {
        BadClass obj;
        throw std::runtime_error("Error in main");
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;
    }
    return 0;
}
```

## 8. 异常与函数声明

### 8.1 异常规范（C++11前）

在C++11之前，可以使用异常规范来指定函数可能抛出的异常：

```cpp
void function() throw(std::runtime_error, std::logic_error) {
    // 函数可能抛出std::runtime_error或std::logic_error
}
```

### 8.2 noexcept（C++11）

C++11引入了`noexcept`关键字，用于指定函数不会抛出异常：

```cpp
void function() noexcept {
    // 函数不会抛出异常
}

void function() noexcept(false) {
    // 函数可能抛出异常
}
```

### 8.3 noexcept操作符（C++11）

`noexcept`操作符用于检查表达式是否会抛出异常：

```cpp
template <typename T>
void swap(T& a, T& b) noexcept(noexcept(std::declval<T&>() = std::declval<T&>())) {
    T temp = std::move(a);
    a = std::move(b);
    b = std::move(temp);
}
```

## 9. 异常处理的高级特性

### 9.1 重新抛出异常

我们可以在catch块中重新抛出异常：

```cpp
try {
    // 可能抛出异常的代码
} catch (const std::exception& e) {
    // 处理异常
    std::cout << "Caught: " << e.what() << std::endl;
    // 重新抛出异常
    throw;
}
```

### 9.2 异常指针（C++11）

C++11引入了`std::exception_ptr`，用于存储异常的指针：

```cpp
std::exception_ptr eptr;

try {
    throw std::runtime_error("Error");
} catch (...) {
    eptr = std::current_exception();
}

if (eptr) {
    try {
        std::rethrow_exception(eptr);
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;
    }
}
```

### 9.3 嵌套异常（C++11）

C++11引入了`std::nested_exception`，用于嵌套异常：

```cpp
void function1() {
    try {
        throw std::runtime_error("Error in function1");
    } catch (...) {
        std::throw_with_nested(std::runtime_error("Error in function2"));
    }
}

void print_exception(const std::exception& e, int level = 0) {
    std::cout << std::string(level, ' ') << "Exception: " << e.what() << std::endl;
    try {
        std::rethrow_if_nested(e);
    } catch (const std::exception& nested) {
        print_exception(nested, level + 1);
    } catch (...) {
    }
}

int main() {
    try {
        function1();
    } catch (const std::exception& e) {
        print_exception(e);
    }
    return 0;
}
```

## 10. 异常处理的实际应用

### 10.1 异常处理在库设计中的应用

在库设计中，异常处理是一种重要的错误处理机制：

```cpp
class Database {
private:
    std::string connectionString;
public:
    Database(const std::string& connStr) : connectionString(connStr) {
        // 连接数据库
        if (!connect()) {
            throw DatabaseException("Failed to connect to database");
        }
    }
    
    std::vector<Record> query(const std::string& sql) {
        if (sql.empty()) {
            throw InvalidQueryException("Empty query");
        }
        // 执行查询
        // 如果查询失败，抛出异常
        return results;
    }
};
```

### 10.2 异常处理在大型项目中的应用

在大型项目中，异常处理可以帮助我们更好地管理错误：

- **集中错误处理**：在顶层捕获异常，统一处理
- **错误传播**：通过异常将错误从底层传播到顶层
- **资源管理**：使用RAII确保资源在异常发生时正确释放
- **错误恢复**：在适当的地方捕获异常，尝试恢复操作

---

**更新时间：2026-04-04**