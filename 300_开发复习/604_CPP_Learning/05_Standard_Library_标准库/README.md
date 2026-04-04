# 标准库

## 1. 标准库概述

C++标准库是C++语言的重要组成部分，提供了大量的工具和组件，包括：

- **容器**：用于存储和管理数据
- **算法**：用于处理数据
- **迭代器**：用于遍历容器
- **函数对象**：用于封装函数
- **适配器**：用于修改其他组件的行为
- **流**：用于输入输出操作
- **工具类**：如智能指针、时间工具等

## 2. 容器库

### 2.1 序列容器

序列容器按照线性顺序存储元素：

#### vector

`vector`是最常用的序列容器，它是一个动态数组：

```cpp
#include <vector>

std::vector<int> v;
v.push_back(10);
v.push_back(20);
v.push_back(30);

for (size_t i = 0; i < v.size(); i++) {
    std::cout << v[i] << " ";
}
```

#### list

`list`是一个双向链表：

```cpp
#include <list>

std::list<int> l;
l.push_back(10);
l.push_front(5);
l.push_back(15);

for (auto it = l.begin(); it != l.end(); ++it) {
    std::cout << *it << " ";
}
```

#### deque

`deque`是一个双端队列：

```cpp
#include <deque>

std::deque<int> d;
d.push_back(10);
d.push_front(5);
d.push_back(15);

for (auto it = d.begin(); it != d.end(); ++it) {
    std::cout << *it << " ";
}
```

### 2.2 关联容器

关联容器按照键值对存储元素：

#### map

`map`是一个有序的键值对容器：

```cpp
#include <map>

std::map<std::string, int> m;
m["Alice"] = 25;
m["Bob"] = 30;
m["Charlie"] = 35;

for (auto it = m.begin(); it != m.end(); ++it) {
    std::cout << it->first << ": " << it->second << std::endl;
}
```

#### set

`set`是一个有序的集合：

```cpp
#include <set>

std::set<int> s;
s.insert(10);
s.insert(20);
s.insert(30);

for (auto it = s.begin(); it != s.end(); ++it) {
    std::cout << *it << " ";
}
```

### 2.3 无序容器

无序容器使用哈希表实现：

#### unordered_map

`unordered_map`是一个无序的键值对容器：

```cpp
#include <unordered_map>

std::unordered_map<std::string, int> um;
um["Alice"] = 25;
um["Bob"] = 30;
um["Charlie"] = 35;

for (auto it = um.begin(); it != um.end(); ++it) {
    std::cout << it->first << ": " << it->second << std::endl;
}
```

#### unordered_set

`unordered_set`是一个无序的集合：

```cpp
#include <unordered_set>

std::unordered_set<int> us;
us.insert(10);
us.insert(20);
us.insert(30);

for (auto it = us.begin(); it != us.end(); ++it) {
    std::cout << *it << " ";
}
```

## 3. 算法库

### 3.1 非修改性算法

非修改性算法不会修改容器中的元素：

#### find

查找元素：

```cpp
#include <algorithm>
#include <vector>

std::vector<int> v = {1, 2, 3, 4, 5};
auto it = std::find(v.begin(), v.end(), 3);
if (it != v.end()) {
    std::cout << "Found: " << *it << std::endl;
} else {
    std::cout << "Not found" << std::endl;
}
```

#### count

统计元素出现的次数：

```cpp
#include <algorithm>
#include <vector>

std::vector<int> v = {1, 2, 3, 2, 1};
int count = std::count(v.begin(), v.end(), 2);
std::cout << "Count: " << count << std::endl;
```

### 3.2 修改性算法

修改性算法会修改容器中的元素：

#### sort

排序元素：

```cpp
#include <algorithm>
#include <vector>

std::vector<int> v = {5, 2, 8, 1, 9};
std::sort(v.begin(), v.end());

for (auto i : v) {
    std::cout << i << " ";
}
```

#### transform

转换元素：

```cpp
#include <algorithm>
#include <vector>

std::vector<int> v = {1, 2, 3, 4, 5};
std::vector<int> result(v.size());
std::transform(v.begin(), v.end(), result.begin(), [](int x) { return x * 2; });

for (auto i : result) {
    std::cout << i << " ";
}
```

### 3.3 数值算法

数值算法用于数值计算：

#### accumulate

累加元素：

```cpp
#include <numeric>
#include <vector>

std::vector<int> v = {1, 2, 3, 4, 5};
int sum = std::accumulate(v.begin(), v.end(), 0);
std::cout << "Sum: " << sum << std::endl;
```

#### inner_product

计算内积：

```cpp
#include <numeric>
#include <vector>

std::vector<int> a = {1, 2, 3};
std::vector<int> b = {4, 5, 6};
int product = std::inner_product(a.begin(), a.end(), b.begin(), 0);
std::cout << "Inner product: " << product << std::endl;
```

## 4. 迭代器

### 4.1 迭代器类别

C++标准库定义了五种迭代器类别：

- **输入迭代器**：只读，只能单向移动
- **输出迭代器**：只写，只能单向移动
- **前向迭代器**：可读写，只能单向移动
- **双向迭代器**：可读写，可双向移动
- **随机访问迭代器**：可读写，可随机访问

### 4.2 迭代器适配器

迭代器适配器修改迭代器的行为：

#### reverse_iterator

反向迭代器：

```cpp
#include <vector>

std::vector<int> v = {1, 2, 3, 4, 5};
for (auto it = v.rbegin(); it != v.rend(); ++it) {
    std::cout << *it << " ";
}
```

#### back_insert_iterator

后插入迭代器：

```cpp
#include <vector>
#include <iterator>

std::vector<int> v;
std::back_insert_iterator<std::vector<int>> it(v);
*it = 10;
++it;
*it = 20;

for (auto i : v) {
    std::cout << i << " ";
}
```

## 5. 函数对象

### 5.1 预定义函数对象

C++标准库提供了一些预定义的函数对象：

```cpp
#include <functional>

std::plus<int> add;
std::minus<int> subtract;
std::multiplies<int> multiply;
std::divides<int> divide;
std::modulus<int> modulus;
std::negate<int> negate;

std::cout << add(10, 20) << std::endl;  // 30
std::cout << subtract(20, 10) << std::endl;  // 10
```

### 5.2 函数适配器

函数适配器修改函数对象的行为：

```cpp
#include <functional>

std::bind(std::plus<int>(), 10, std::placeholders::_1)(20);  // 30
std::bind(std::minus<int>(), std::placeholders::_1, 10)(20);  // 10
```

## 6. 智能指针

### 6.1 unique_ptr

`unique_ptr`是一个独占所有权的智能指针：

```cpp
#include <memory>

std::unique_ptr<int> p1(new int(10));
std::unique_ptr<int> p2 = std::move(p1);  // 转移所有权

if (p1) {
    std::cout << "p1 is not null" << std::endl;
} else {
    std::cout << "p1 is null" << std::endl;
}

if (p2) {
    std::cout << "p2 is not null" << std::endl;
    std::cout << *p2 << std::endl;  // 10
}
```

### 6.2 shared_ptr

`shared_ptr`是一个共享所有权的智能指针：

```cpp
#include <memory>

std::shared_ptr<int> p1(new int(10));
std::shared_ptr<int> p2 = p1;  // 共享所有权

std::cout << "p1 use count: " << p1.use_count() << std::endl;  // 2
std::cout << "p2 use count: " << p2.use_count() << std::endl;  // 2

p1.reset();
std::cout << "p1 use count: " << p1.use_count() << std::endl;  // 0
std::cout << "p2 use count: " << p2.use_count() << std::endl;  // 1
```

### 6.3 weak_ptr

`weak_ptr`是一个不增加引用计数的智能指针：

```cpp
#include <memory>

std::shared_ptr<int> p1(new int(10));
std::weak_ptr<int> wp = p1;

std::cout << "wp use count: " << wp.use_count() << std::endl;  // 1

if (auto p2 = wp.lock()) {
    std::cout << "wp is valid" << std::endl;
    std::cout << *p2 << std::endl;  // 10
} else {
    std::cout << "wp is invalid" << std::endl;
}

p1.reset();

if (auto p2 = wp.lock()) {
    std::cout << "wp is valid" << std::endl;
} else {
    std::cout << "wp is invalid" << std::endl;
}
```

## 7. 字符串库

### 7.1 string类

`string`类提供了字符串操作的功能：

```cpp
#include <string>

std::string s1 = "Hello";
std::string s2 = "World";
std::string s3 = s1 + " " + s2;

std::cout << s3 << std::endl;  // Hello World
std::cout << s3.length() << std::endl;  // 11
std::cout << s3.substr(0, 5) << std::endl;  // Hello
```

### 7.2 字符串视图（C++17）

`string_view`提供了对字符串的非拥有视图：

```cpp
#include <string_view>

std::string s = "Hello, World!";
std::string_view sv = s;

std::cout << sv << std::endl;  // Hello, World!
std::cout << sv.substr(0, 5) << std::endl;  // Hello
```

## 8. 输入输出库

### 8.1 标准输入输出

```cpp
#include <iostream>

// 标准输出
std::cout << "Hello, World!" << std::endl;

// 标准输入
int x;
std::cin >> x;
std::cout << "You entered: " << x << std::endl;
```

### 8.2 文件输入输出

```cpp
#include <fstream>

// 写入文件
std::ofstream outfile("example.txt");
outfile << "Hello, File!" << std::endl;
outfile.close();

// 读取文件
std::ifstream infile("example.txt");
std::string line;
while (std::getline(infile, line)) {
    std::cout << line << std::endl;
}
infile.close();
```

### 8.3 字符串流

```cpp
#include <sstream>

// 字符串输出流
std::ostringstream oss;
oss << "Name: " << "Alice" << ", Age: " << 25;
std::string s = oss.str();
std::cout << s << std::endl;  // Name: Alice, Age: 25

// 字符串输入流
std::istringstream iss("10 20 30");
int a, b, c;
iss >> a >> b >> c;
std::cout << a << " " << b << " " << c << std::endl;  // 10 20 30
```

## 9. 时间库

### 9.1 系统时钟

```cpp
#include <chrono>
#include <iostream>

// 获取当前时间
auto now = std::chrono::system_clock::now();

// 转换为时间_t
time_t now_time = std::chrono::system_clock::to_time_t(now);
std::cout << std::ctime(&now_time);
```

### 9.2 时间间隔

```cpp
#include <chrono>
#include <iostream>

// 测量代码执行时间
auto start = std::chrono::high_resolution_clock::now();

// 执行一些操作
for (int i = 0; i < 1000000; i++) {
    // 空循环
}

auto end = std::chrono::high_resolution_clock::now();
auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
std::cout << "Execution time: " << duration.count() << " microseconds" << std::endl;
```

## 10. 工具库

### 10.1 类型特性

```cpp
#include <type_traits>

std::cout << std::is_integral<int>::value << std::endl;  // 1
std::cout << std::is_floating_point<double>::value << std::endl;  // 1
std::cout << std::is_array<int[]>::value << std::endl;  // 1
std::cout << std::is_pointer<int*>::value << std::endl;  // 1
```

### 10.2 数值极限

```cpp
#include <limits>

std::cout << std::numeric_limits<int>::min() << std::endl;
std::cout << std::numeric_limits<int>::max() << std::endl;
std::cout << std::numeric_limits<double>::epsilon() << std::endl;
```

### 10.3 随机数生成

```cpp
#include <random>

std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<int> dist(1, 100);

for (int i = 0; i < 10; i++) {
    std::cout << dist(gen) << " ";
}
```

---

**更新时间：2026-04-04**