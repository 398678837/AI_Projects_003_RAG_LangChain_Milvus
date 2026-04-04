# 并发编程

## 1. 并发编程基础

### 1.1 并发的概念

并发是指两个或多个任务同时执行的能力。在C++中，我们可以通过多种方式实现并发：

- **多线程**：在同一进程内创建多个线程
- **多进程**：创建多个进程
- **异步编程**：使用异步操作

### 1.2 并发的优势

- **提高性能**：充分利用多核处理器
- **改善响应性**：避免主线程阻塞
- **资源共享**：方便线程间通信
- **模块化**：将不同任务分离到不同线程

### 1.3 并发的挑战

- **竞争条件**：多个线程同时访问共享资源
- **死锁**：线程相互等待对方释放资源
- **活锁**：线程不断尝试但无法进展
- **资源耗尽**：创建过多线程导致系统资源耗尽

## 2. 多线程编程

### 2.1 线程的创建和管理

C++11引入了`std::thread`类，用于创建和管理线程：

```cpp
#include <thread>
#include <iostream>

void function() {
    std::cout << "Hello from thread!" << std::endl;
}

int main() {
    // 创建线程
    std::thread t(function);
    
    // 等待线程完成
    t.join();
    
    std::cout << "Hello from main!" << std::endl;
    return 0;
}
```

### 2.2 线程参数

线程函数可以接受参数：

```cpp
#include <thread>
#include <iostream>

void function(int x, const std::string& message) {
    std::cout << "x: " << x << ", message: " << message << std::endl;
}

int main() {
    std::thread t(function, 42, "Hello");
    t.join();
    return 0;
}
```

### 2.3 线程移动

线程可以移动但不能复制：

```cpp
#include <thread>

void function() {
    // 线程函数
}

int main() {
    std::thread t1(function);
    std::thread t2 = std::move(t1);  // 移动线程
    
    t2.join();
    // t1现在是无效的
    return 0;
}
```

## 3. 互斥锁

### 3.1 互斥锁的概念

互斥锁（mutex）用于保护共享资源，确保同一时间只有一个线程可以访问：

```cpp
#include <thread>
#include <mutex>
#include <iostream>

std::mutex mtx;
int shared_data = 0;

void increment() {
    for (int i = 0; i < 1000; i++) {
        std::lock_guard<std::mutex> lock(mtx);  // 自动加锁和解锁
        shared_data++;
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);
    
    t1.join();
    t2.join();
    
    std::cout << "shared_data: " << shared_data << std::endl;
    return 0;
}
```

### 3.2 递归互斥锁

递归互斥锁（recursive_mutex）允许同一线程多次获取锁：

```cpp
#include <thread>
#include <mutex>

std::recursive_mutex rmtx;

void function1() {
    std::lock_guard<std::recursive_mutex> lock(rmtx);
    // 做一些事情
    function2();
}

void function2() {
    std::lock_guard<std::recursive_mutex> lock(rmtx);
    // 做一些事情
}
```

### 3.3 时间互斥锁

时间互斥锁（timed_mutex）允许尝试获取锁一段时间：

```cpp
#include <thread>
#include <mutex>
#include <chrono>

std::timed_mutex tmtx;

void function() {
    if (tmtx.try_lock_for(std::chrono::seconds(1))) {
        // 获取锁成功
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        tmtx.unlock();
    } else {
        // 获取锁失败
    }
}
```

## 4. 条件变量

### 4.1 条件变量的概念

条件变量用于线程间的通信，允许线程等待特定条件：

```cpp
#include <thread>
#include <mutex>
#include <condition_variable>
#include <iostream>

std::mutex mtx;
std::condition_variable cv;
bool ready = false;

void producer() {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    
    {
        std::lock_guard<std::mutex> lock(mtx);
        ready = true;
        std::cout << "Producer: Data is ready" << std::endl;
    }
    
    cv.notify_one();  // 通知一个等待的线程
}

void consumer() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, []{ return ready; });  // 等待条件满足
    
    std::cout << "Consumer: Data is received" << std::endl;
}

int main() {
    std::thread t1(producer);
    std::thread t2(consumer);
    
    t1.join();
    t2.join();
    return 0;
}
```

### 4.2 条件变量的使用

条件变量通常与互斥锁一起使用：

- 使用`wait()`等待条件满足
- 使用`notify_one()`通知一个等待的线程
- 使用`notify_all()`通知所有等待的线程

## 5. 原子操作

### 5.1 原子类型

C++11引入了原子类型，用于无锁的线程安全操作：

```cpp
#include <thread>
#include <atomic>
#include <iostream>

std::atomic<int> shared_data(0);

void increment() {
    for (int i = 0; i < 1000; i++) {
        shared_data++;
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);
    
    t1.join();
    t2.join();
    
    std::cout << "shared_data: " << shared_data << std::endl;
    return 0;
}
```

### 5.2 原子操作

原子操作包括：

- 基本算术操作：`++`, `--`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`
- 比较交换操作：`compare_exchange_weak()`, `compare_exchange_strong()`
- 加载和存储操作：`load()`, `store()`
- 交换操作：`exchange()`

## 6. 线程局部存储

### 6.1 线程局部存储的概念

线程局部存储（Thread Local Storage, TLS）允许每个线程拥有变量的独立副本：

```cpp
#include <thread>
#include <iostream>

thread_local int counter = 0;

void function() {
    counter++;
    std::cout << "Thread ID: " << std::this_thread::get_id() 
              << ", counter: " << counter << std::endl;
}

int main() {
    std::thread t1(function);
    std::thread t2(function);
    
    t1.join();
    t2.join();
    
    function();  // 主线程
    return 0;
}
```

### 6.2 线程局部存储的应用

线程局部存储适用于：

- 线程特定的状态
- 避免参数传递
- 提高性能（避免锁）

## 7. 异步编程

### 7.1  futures和promises

C++11引入了`std::future`和`std::promise`，用于异步任务的结果传递：

```cpp
#include <future>
#include <iostream>

int compute() {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return 42;
}

int main() {
    // 启动异步任务
    std::future<int> future = std::async(std::launch::async, compute);
    
    // 做一些其他事情
    std::cout << "Waiting for result..." << std::endl;
    
    // 获取结果
    int result = future.get();
    std::cout << "Result: " << result << std::endl;
    
    return 0;
}
```

### 7.2 异步任务的启动策略

`std::async`支持两种启动策略：

- `std::launch::async`：立即启动新线程
- `std::launch::deferred`：延迟执行，直到调用`get()`或`wait()`

```cpp
// 立即启动新线程
std::future<int> future1 = std::async(std::launch::async, compute);

// 延迟执行
std::future<int> future2 = std::async(std::launch::deferred, compute);
```

## 8. 线程池

### 8.1 线程池的概念

线程池是一组预先创建的线程，用于执行任务：

### 8.2 线程池的实现

```cpp
#include <vector>
#include <queue>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <functional>

class ThreadPool {
private:
    std::vector<std::thread> workers;
    std::queue<std::function<void()>> tasks;
    
    std::mutex mtx;
    std::condition_variable cv;
    bool stop;

public:
    ThreadPool(size_t threads) : stop(false) {
        for (size_t i = 0; i < threads; i++) {
            workers.emplace_back([this] {
                while (true) {
                    std::function<void()> task;
                    
                    { 
                        std::unique_lock<std::mutex> lock(this->mtx);
                        this->cv.wait(lock, [this] { 
                            return this->stop || !this->tasks.empty(); 
                        });
                        
                        if (this->stop && this->tasks.empty()) {
                            return;
                        }
                        
                        task = std::move(this->tasks.front());
                        this->tasks.pop();
                    }
                    
                    task();
                }
            });
        }
    }
    
    template<class F>
    void enqueue(F&& f) {
        { 
            std::unique_lock<std::mutex> lock(mtx);
            tasks.emplace(std::forward<F>(f));
        }
        cv.notify_one();
    }
    
    ~ThreadPool() {
        { 
            std::unique_lock<std::mutex> lock(mtx);
            stop = true;
        }
        cv.notify_all();
        
        for (std::thread &worker : workers) {
            worker.join();
        }
    }
};
```

### 8.3 线程池的应用

```cpp
int main() {
    ThreadPool pool(4);
    
    for (int i = 0; i < 8; i++) {
        pool.enqueue([i] {
            std::cout << "Task " << i << " executed by thread " 
                      << std::this_thread::get_id() << std::endl;
            std::this_thread::sleep_for(std::chrono::seconds(1));
        });
    }
    
    // 主线程等待
    std::this_thread::sleep_for(std::chrono::seconds(3));
    
    return 0;
}
```

## 9. 同步原语

### 9.1 信号量

信号量用于控制对资源的访问：

```cpp
#include <mutex>
#include <condition_variable>

class Semaphore {
private:
    std::mutex mtx;
    std::condition_variable cv;
    int count;

public:
    Semaphore(int count = 0) : count(count) {}
    
    void acquire() {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [this] { return count > 0; });
        count--;
    }
    
    void release() {
        std::unique_lock<std::mutex> lock(mtx);
        count++;
        cv.notify_one();
    }
};
```

### 9.2 读写锁

读写锁允许多个线程同时读取，但只允许一个线程写入：

```cpp
#include <mutex>
#include <condition_variable>

class ReadWriteLock {
private:
    std::mutex mtx;
    std::condition_variable cv_read;
    std::condition_variable cv_write;
    int readers;
    int writers;
    int write_requests;

public:
    ReadWriteLock() : readers(0), writers(0), write_requests(0) {}
    
    void read_lock() {
        std::unique_lock<std::mutex> lock(mtx);
        cv_read.wait(lock, [this] { return writers == 0 && write_requests == 0; });
        readers++;
    }
    
    void read_unlock() {
        std::unique_lock<std::mutex> lock(mtx);
        readers--;
        if (readers == 0) {
            cv_write.notify_one();
        }
    }
    
    void write_lock() {
        std::unique_lock<std::mutex> lock(mtx);
        write_requests++;
        cv_write.wait(lock, [this] { return readers == 0 && writers == 0; });
        write_requests--;
        writers++;
    }
    
    void write_unlock() {
        std::unique_lock<std::mutex> lock(mtx);
        writers--;
        cv_read.notify_all();
        cv_write.notify_one();
    }
};
```

## 10. 并发编程的最佳实践

### 10.1 并发编程的准则

- **最小化共享资源**：减少线程间的共享数据
- **使用原子操作**：对于简单的计数器等操作
- **使用互斥锁**：对于复杂的共享资源
- **使用条件变量**：用于线程间通信
- **避免死锁**：使用锁的顺序一致
- **使用RAII**：管理锁和其他资源

### 10.2 并发编程的性能优化

- **减少锁的范围**：只在必要时持有锁
- **使用无锁数据结构**：减少锁的竞争
- **使用线程池**：避免频繁创建和销毁线程
- **避免过度同步**：只在必要时同步

### 10.3 并发编程的调试

- **使用线程安全的日志**：避免日志操作的竞争
- **使用调试工具**：如Valgrind的Helgrind工具
- **重现问题**：尝试重现并发问题
- **使用断言**：检查不变量

---

**更新时间：2026-04-04**