# 模板与泛型编程

## 1. 模板基础

### 1.1 函数模板

函数模板允许我们编写通用的函数，可以处理不同类型的参数：

```cpp
template <typename T>
T max(T a, T b) {
    return a > b ? a : b;
}
```

使用函数模板：

```cpp
int main() {
    int a = 10, b = 20;
    std::cout << max(a, b) << std::endl;  // 调用int版本
    
    double c = 3.14, d = 2.71;
    std::cout << max(c, d) << std::endl;  // 调用double版本
    
    return 0;
}
```

### 1.2 类模板

类模板允许我们编写通用的类，可以处理不同类型的成员：

```cpp
template <typename T>
class Stack {
private:
    std::vector<T> elements;
public:
    void push(T const& item) {
        elements.push_back(item);
    }
    
    void pop() {
        if (elements.empty()) {
            throw std::out_of_range("Stack<>::pop(): empty stack");
        }
        elements.pop_back();
    }
    
    T const& top() const {
        if (elements.empty()) {
            throw std::out_of_range("Stack<>::top(): empty stack");
        }
        return elements.back();
    }
    
    bool empty() const {
        return elements.empty();
    }
};
```

使用类模板：

```cpp
int main() {
    Stack<int> intStack;
    intStack.push(10);
    intStack.push(20);
    std::cout << intStack.top() << std::endl;
    
    Stack<std::string> stringStack;
    stringStack.push("Hello");
    stringStack.push("World");
    std::cout << stringStack.top() << std::endl;
    
    return 0;
}
```

## 2. 模板特化

### 2.1 函数模板特化

函数模板特化允许我们为特定类型提供专门的实现：

```cpp
// 主模板
template <typename T>
T max(T a, T b) {
    return a > b ? a : b;
}

// 特化版本
template <>
const char* max<const char*>(const char* a, const char* b) {
    return std::strcmp(a, b) > 0 ? a : b;
}
```

### 2.2 类模板特化

类模板特化允许我们为特定类型提供专门的类实现：

```cpp
// 主模板
template <typename T>
class MyClass {
public:
    void print() {
        std::cout << "General template" << std::endl;
    }
};

// 特化版本
template <>
class MyClass<int> {
public:
    void print() {
        std::cout << "Specialized for int" << std::endl;
    }
};
```

## 3. 模板参数

### 3.1 类型参数

类型参数是最常见的模板参数：

```cpp
template <typename T, typename U>
class Pair {
private:
    T first;
    U second;
public:
    Pair(T f, U s) : first(f), second(s) {}
    
    T getFirst() const {
        return first;
    }
    
    U getSecond() const {
        return second;
    }
};
```

### 3.2 非类型参数

非类型参数允许我们传递常量值作为模板参数：

```cpp
template <typename T, int Size>
class Array {
private:
    T data[Size];
public:
    T& operator[](int index) {
        return data[index];
    }
    
    const T& operator[](int index) const {
        return data[index];
    }
    
    int size() const {
        return Size;
    }
};
```

使用非类型模板参数：

```cpp
Array<int, 5> arr;
for (int i = 0; i < arr.size(); i++) {
    arr[i] = i;
}
```

## 4. 可变参数模板

### 4.1 可变参数函数模板

C++11引入了可变参数模板，允许我们处理任意数量的参数：

```cpp
template <typename... Args>
void print(Args... args) {
    // 实现
}
```

### 4.2 递归展开参数包

我们可以使用递归来展开参数包：

```cpp
// 基本情况
void print() {
    std::cout << std::endl;
}

// 递归情况
template <typename T, typename... Args>
void print(T first, Args... rest) {
    std::cout << first << " ";
    print(rest...);
}
```

### 4.3 折叠表达式（C++17）

C++17引入了折叠表达式，简化了参数包的处理：

```cpp
template <typename... Args>
auto sum(Args... args) {
    return (args + ...);
}
```

## 5. 模板元编程

### 5.1 编译时计算

模板元编程允许我们在编译时进行计算：

```cpp
template <int N>
struct Factorial {
    static const int value = N * Factorial<N - 1>::value;
};

// 特化基本情况
template <>
struct Factorial<0> {
    static const int value = 1;
};
```

使用模板元编程：

```cpp
int main() {
    constexpr int fact5 = Factorial<5>::value;  // 编译时计算
    std::cout << "5! = " << fact5 << std::endl;  // 输出：120
    return 0;
}
```

### 5.2 类型特性

我们可以使用模板元编程来检查类型特性：

```cpp
template <typename T>
struct is_integral {
    static const bool value = false;
};

template <>
struct is_integral<int> {
    static const bool value = true;
};

template <>
struct is_integral<long> {
    static const bool value = true;
};
```

## 6. 标准库中的模板

### 6.1 容器

标准库中的容器都是模板类：

- `std::vector<T>`：动态数组
- `std::list<T>`：双向链表
- `std::map<K, V>`：键值对映射
- `std::set<T>`：有序集合
- `std::unordered_map<K, V>`：哈希表
- `std::unordered_set<T>`：哈希集合

### 6.2 算法

标准库中的算法都是模板函数：

- `std::sort`：排序
- `std::find`：查找
- `std::for_each`：遍历
- `std::transform`：转换
- `std::accumulate`：累加

### 6.3 迭代器

迭代器是一种抽象，允许我们遍历容器中的元素：

- `std::begin`：获取容器的起始迭代器
- `std::end`：获取容器的结束迭代器

## 7. 模板的编译模型

### 7.1 包含模型

在包含模型中，模板的定义必须在使用模板的地方可见：

```cpp
// header.h
template <typename T>
class MyClass {
public:
    void doSomething();
};

// 模板定义也需要在头文件中
template <typename T>
void MyClass<T>::doSomething() {
    // 实现
}
```

### 7.2 显式实例化

我们可以显式实例化模板，避免在每个使用点都实例化：

```cpp
// 显式实例化
template class MyClass<int>;
template class MyClass<double>;
```

## 8. 模板的最佳实践

### 8.1 模板设计原则

- **简单性**：保持模板接口简单
- **通用性**：设计通用的模板，能够处理各种类型
- **效率**：确保模板生成的代码高效
- **可维护性**：编写清晰、可维护的模板代码

### 8.2 常见陷阱

- **模板代码膨胀**：过度使用模板可能导致代码膨胀
- **编译时间**：模板会增加编译时间
- **错误信息**：模板错误信息通常比较复杂
- **依赖关系**：模板的依赖关系可能很复杂

## 9. 泛型编程技术

### 9.1 类型擦除

类型擦除允许我们在运行时处理不同类型的对象：

```cpp
class Any {
private:
    struct Base {
        virtual ~Base() {}
        virtual Base* clone() const = 0;
    };
    
    template <typename T>
    struct Derived : Base {
        T value;
        Derived(T v) : value(v) {}
        Base* clone() const override {
            return new Derived(value);
        }
    };
    
    Base* ptr;
public:
    template <typename T>
    Any(T value) : ptr(new Derived<T>(value)) {}
    
    Any(const Any& other) : ptr(other.ptr->clone()) {}
    
    ~Any() {
        delete ptr;
    }
    
    template <typename T>
    T cast() const {
        Derived<T>* d = dynamic_cast<Derived<T>*>(ptr);
        if (!d) {
            throw std::bad_cast();
        }
        return d->value;
    }
};
```

### 9.2 策略模式

策略模式允许我们在运行时选择算法：

```cpp
template <typename SortStrategy>
class Sorter {
private:
    SortStrategy strategy;
public:
    Sorter(SortStrategy s) : strategy(s) {}
    
    template <typename Container>
    void sort(Container& container) {
        strategy.sort(container);
    }
};

struct BubbleSort {
    template <typename Container>
    void sort(Container& container) {
        // 冒泡排序实现
    }
};

struct QuickSort {
    template <typename Container>
    void sort(Container& container) {
        // 快速排序实现
    }
};
```

## 10. 现代C++中的模板特性

### 10.1 别名模板（C++11）

别名模板允许我们为模板创建别名：

```cpp
template <typename T>
using Vec = std::vector<T>;

Vec<int> v;  // 等价于 std::vector<int> v;
```

### 10.2 变量模板（C++14）

变量模板允许我们定义模板变量：

```cpp
template <typename T>
constexpr T pi = T(3.14159265358979323846);

int main() {
    std::cout << pi<double> << std::endl;
    return 0;
}
```

### 10.3 模板模板参数（C++17）

模板模板参数允许我们传递模板作为模板参数：

```cpp
template <template <typename> class Container, typename T>
Container<T> createContainer(T value) {
    Container<T> container;
    container.push_back(value);
    return container;
}

int main() {
    auto v = createContainer<std::vector>(42);
    return 0;
}
```

---

**更新时间：2026-04-04**