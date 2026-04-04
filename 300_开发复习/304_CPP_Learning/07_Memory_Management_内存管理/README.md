# 内存管理

## 1. 内存管理基础

### 1.1 内存布局

C++程序的内存布局通常分为以下几个部分：

- **代码区**：存储程序的可执行代码
- **全局/静态区**：存储全局变量和静态变量
- **常量区**：存储常量
- **堆区**：存储动态分配的内存
- **栈区**：存储函数的局部变量和函数参数

### 1.2 内存分配方式

C++中有三种内存分配方式：

- **静态分配**：在编译时分配内存，如全局变量和静态变量
- **栈分配**：在函数调用时自动分配内存，函数返回时自动释放
- **堆分配**：在运行时动态分配内存，需要手动释放

## 2. 动态内存分配

### 2.1 new和delete操作符

C++使用`new`和`delete`操作符进行动态内存分配和释放：

```cpp
// 分配单个对象
int* p = new int(10);

// 使用指针
std::cout << *p << std::endl;

// 释放内存
delete p;
p = nullptr;  // 避免野指针

// 分配数组
int* arr = new int[5];

// 使用数组
for (int i = 0; i < 5; i++) {
    arr[i] = i;
}

// 释放数组
delete[] arr;
arr = nullptr;  // 避免野指针
```

### 2.2 new[]和delete[]

使用`new[]`分配数组，必须使用`delete[]`释放：

```cpp
// 错误的做法
int* arr = new int[5];
delete arr;  // 只释放第一个元素，导致内存泄漏

// 正确的做法
int* arr = new int[5];
delete[] arr;  // 释放整个数组
```

### 2.3 定位new（placement new）

定位new允许在已分配的内存上构造对象：

```cpp
#include <new>

// 分配内存
char buffer[sizeof(int)];

// 在指定内存上构造对象
int* p = new (buffer) int(42);

// 使用对象
std::cout << *p << std::endl;

// 手动调用析构函数
p->~int();
```

## 3. 智能指针

### 3.1 unique_ptr

`unique_ptr`是一个独占所有权的智能指针：

```cpp
#include <memory>

// 创建unique_ptr
std::unique_ptr<int> p1(new int(10));

// 使用make_unique（C++14）
auto p2 = std::make_unique<int>(20);

// 转移所有权
std::unique_ptr<int> p3 = std::move(p1);

// 检查指针是否为空
if (p1) {
    std::cout << "p1 is not null" << std::endl;
} else {
    std::cout << "p1 is null" << std::endl;
}

if (p3) {
    std::cout << "p3 is not null" << std::endl;
    std::cout << *p3 << std::endl;
}
```

### 3.2 shared_ptr

`shared_ptr`是一个共享所有权的智能指针：

```cpp
#include <memory>

// 创建shared_ptr
std::shared_ptr<int> p1(new int(10));

// 使用make_shared
auto p2 = std::make_shared<int>(20);

// 共享所有权
std::shared_ptr<int> p3 = p1;

// 检查引用计数
std::cout << "p1 use count: " << p1.use_count() << std::endl;
std::cout << "p3 use count: " << p3.use_count() << std::endl;

// 释放一个指针
p1.reset();
std::cout << "p3 use count after p1 reset: " << p3.use_count() << std::endl;
```

### 3.3 weak_ptr

`weak_ptr`是一个不增加引用计数的智能指针：

```cpp
#include <memory>

// 创建shared_ptr
auto p1 = std::make_shared<int>(10);

// 创建weak_ptr
std::weak_ptr<int> wp = p1;

// 检查weak_ptr是否有效
if (auto p2 = wp.lock()) {
    std::cout << "wp is valid: " << *p2 << std::endl;
} else {
    std::cout << "wp is invalid" << std::endl;
}

// 释放shared_ptr
p1.reset();

// 再次检查weak_ptr
if (auto p2 = wp.lock()) {
    std::cout << "wp is valid: " << *p2 << std::endl;
} else {
    std::cout << "wp is invalid" << std::endl;
}
```

## 4. RAII（资源获取即初始化）

### 4.1 RAII的概念

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
    
    // 禁止复制
    File(const File&) = delete;
    File& operator=(const File&) = delete;
    
    // 允许移动
    File(File&& other) noexcept : fp(other.fp) {
        other.fp = nullptr;
    }
    
    File& operator=(File&& other) noexcept {
        if (this != &other) {
            if (fp) {
                fclose(fp);
            }
            fp = other.fp;
            other.fp = nullptr;
        }
        return *this;
    }
};
```

### 4.2 RAII的应用

RAII可以用于管理各种资源：

- 文件句柄
- 网络连接
- 互斥锁
- 内存

```cpp
void processFile(const char* filename) {
    File file(filename, "r");
    // 使用文件
    // 如果发生异常，file的析构函数会自动关闭文件
}
```

## 5. 内存池

### 5.1 内存池的概念

内存池是一种预分配内存的技术，用于减少内存分配和释放的开销：

### 5.2 内存池的实现

```cpp
class MemoryPool {
private:
    char* pool;
    size_t size;
    size_t used;
public:
    MemoryPool(size_t size) : size(size), used(0) {
        pool = new char[size];
    }
    
    ~MemoryPool() {
        delete[] pool;
    }
    
    void* allocate(size_t bytes) {
        if (used + bytes > size) {
            return nullptr;
        }
        void* ptr = pool + used;
        used += bytes;
        return ptr;
    }
    
    void reset() {
        used = 0;
    }
};
```

### 5.3 内存池的应用

内存池适用于频繁分配和释放小内存的场景：

```cpp
void process() {
    MemoryPool pool(1024);
    
    // 分配内存
    int* p1 = static_cast<int*>(pool.allocate(sizeof(int)));
    *p1 = 10;
    
    double* p2 = static_cast<double*>(pool.allocate(sizeof(double)));
    *p2 = 3.14;
    
    // 使用内存
    std::cout << *p1 << " " << *p2 << std::endl;
    
    // 重置内存池
    pool.reset();
    
    // 重新分配内存
    int* p3 = static_cast<int*>(pool.allocate(sizeof(int)));
    *p3 = 20;
    std::cout << *p3 << std::endl;
}
```

## 6. 内存泄漏

### 6.1 内存泄漏的原因

内存泄漏是指程序未能正确释放已经不再使用的内存，常见原因包括：

- 忘记释放动态分配的内存
- 释放内存后未将指针设置为nullptr
- 异常导致的内存泄漏
- 循环引用导致的内存泄漏

### 6.2 内存泄漏的检测

可以使用工具来检测内存泄漏：

- **Valgrind**：Linux平台的内存检测工具
- **Dr. Memory**：Windows平台的内存检测工具
- **AddressSanitizer**：编译器内置的内存检测工具

### 6.3 内存泄漏的避免

- 使用智能指针管理内存
- 使用RAII管理资源
- 避免循环引用
- 定期检查内存使用情况

## 7. 内存优化

### 7.1 内存使用优化

- **减少内存分配**：使用对象池或内存池
- **优化数据结构**：选择合适的数据结构
- **减少内存碎片**：合理分配内存
- **使用移动语义**：减少不必要的复制

### 7.2 内存访问优化

- **局部性原理**：优化数据访问模式
- **缓存友好**：按顺序访问数据
- **避免频繁的内存分配和释放**：使用预分配

## 8. 现代C++中的内存管理

### 8.1 移动语义（C++11）

移动语义允许我们将资源从一个对象转移到另一个对象，而不是复制：

```cpp
class MyString {
private:
    char* data;
    size_t length;
public:
    // 构造函数
    MyString(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
    }
    
    // 移动构造函数
    MyString(MyString&& other) noexcept : data(other.data), length(other.length) {
        other.data = nullptr;
        other.length = 0;
    }
    
    // 移动赋值运算符
    MyString& operator=(MyString&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            length = other.length;
            other.data = nullptr;
            other.length = 0;
        }
        return *this;
    }
    
    // 析构函数
    ~MyString() {
        delete[] data;
    }
};
```

### 8.2 右值引用（C++11）

右值引用是一种新的引用类型，用于支持移动语义：

```cpp
void process(int& lvalue) {
    std::cout << "Processing lvalue" << std::endl;
}

void process(int&& rvalue) {
    std::cout << "Processing rvalue" << std::endl;
}

int main() {
    int x = 10;
    process(x);  // 调用第一个函数
    process(20);  // 调用第二个函数
    process(std::move(x));  // 调用第二个函数
    return 0;
}
```

### 8.3 智能指针的最佳实践

- **优先使用unique_ptr**：当所有权独占时
- **使用shared_ptr**：当所有权需要共享时
- **使用weak_ptr**：当需要避免循环引用时
- **使用make_shared**：创建shared_ptr时
- **使用make_unique**：创建unique_ptr时（C++14）

## 9. 内存管理的最佳实践

### 9.1 通用准则

- **使用智能指针**：避免手动内存管理
- **使用RAII**：确保资源正确释放
- **避免裸指针**：尽量使用智能指针或引用
- **注意内存对齐**：提高内存访问效率
- **定期检查内存使用**：避免内存泄漏

### 9.2 性能优化

- **预分配内存**：避免频繁的内存分配
- **使用内存池**：减少内存分配开销
- **优化数据结构**：减少内存使用
- **使用移动语义**：减少不必要的复制

### 9.3 安全性

- **避免野指针**：释放内存后将指针设置为nullptr
- **避免悬空指针**：不要使用已释放的内存
- **避免内存溢出**：检查数组边界
- **避免缓冲区溢出**：使用安全的字符串操作

## 10. 内存管理的实际应用

### 10.1 自定义内存分配器

我们可以自定义内存分配器，以满足特定的需求：

```cpp
template <typename T>
class MyAllocator {
public:
    using value_type = T;
    
    MyAllocator() = default;
    
    template <typename U>
    MyAllocator(const MyAllocator<U>&) noexcept {
    }
    
    T* allocate(std::size_t n) {
        if (n > std::numeric_limits<std::size_t>::max() / sizeof(T)) {
            throw std::bad_alloc();
        }
        if (auto p = static_cast<T*>(std::malloc(n * sizeof(T)))) {
            return p;
        }
        throw std::bad_alloc();
    }
    
    void deallocate(T* p, std::size_t) noexcept {
        std::free(p);
    }
};

// 使用自定义分配器
std::vector<int, MyAllocator<int>> v;
v.push_back(10);
v.push_back(20);
```

### 10.2 内存管理在大型项目中的应用

在大型项目中，内存管理是一个重要的考虑因素：

- **内存预算**：为不同的组件分配内存预算
- **内存监控**：监控内存使用情况
- **内存泄漏检测**：定期检测内存泄漏
- **内存优化**：根据实际情况优化内存使用

---

**更新时间：2026-04-04**