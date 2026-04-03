#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <vector>
#include <chrono>
#include <future>

// 全局变量
int sharedData = 0;
std::mutex mtx;
std::condition_variable cv;
bool dataReady = false;
std::atomic<int> atomicCounter(0);

// 线程函数
void incrementData(int iterations) {
    for (int i = 0; i < iterations; i++) {
        // 使用互斥锁保护共享数据
        std::lock_guard<std::mutex> lock(mtx);
        sharedData++;
    }
}

// 生产者线程
void producer() {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    
    { 
        std::lock_guard<std::mutex> lock(mtx);
        sharedData = 42;
        dataReady = true;
        std::cout << "生产者: 数据已准备好" << std::endl;
    }
    
    cv.notify_one(); // 通知消费者
}

// 消费者线程
void consumer() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, []{ return dataReady; }); // 等待数据准备好
    
    std::cout << "消费者: 接收到数据: " << sharedData << std::endl;
}

// 原子操作示例
void atomicIncrement(int iterations) {
    for (int i = 0; i < iterations; i++) {
        atomicCounter++;
    }
}

// 线程局部存储
thread_local int threadId = 0;

void threadFunction(int id) {
    threadId = id; // 每个线程有自己的threadId副本
    
    for (int i = 0; i < 3; i++) {
        std::cout << "线程 " << threadId << " 执行迭代 " << i << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
}

// 异步任务
int compute(int x, int y) {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return x + y;
}

// 线程池
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

int main() {
    // 基本线程创建
    std::cout << "=== 基本线程创建 ===" << std::endl;
    
    std::thread t1(incrementData, 1000);
    std::thread t2(incrementData, 1000);
    
    t1.join();
    t2.join();
    
    std::cout << "共享数据值: " << sharedData << std::endl;
    
    // 条件变量
    std::cout << "\n=== 条件变量 ===" << std::endl;
    
    std::thread producerThread(producer);
    std::thread consumerThread(consumer);
    
    producerThread.join();
    consumerThread.join();
    
    // 原子操作
    std::cout << "\n=== 原子操作 ===" << std::endl;
    
    std::thread t3(atomicIncrement, 1000);
    std::thread t4(atomicIncrement, 1000);
    
    t3.join();
    t4.join();
    
    std::cout << "原子计数器值: " << atomicCounter << std::endl;
    
    // 线程局部存储
    std::cout << "\n=== 线程局部存储 ===" << std::endl;
    
    std::thread t5(threadFunction, 1);
    std::thread t6(threadFunction, 2);
    
    t5.join();
    t6.join();
    
    // 异步任务
    std::cout << "\n=== 异步任务 ===" << std::endl;
    
    std::future<int> future = std::async(std::launch::async, compute, 10, 20);
    std::cout << "等待计算结果..." << std::endl;
    
    int result = future.get();
    std::cout << "计算结果: " << result << std::endl;
    
    // 线程池
    std::cout << "\n=== 线程池 ===" << std::endl;
    
    ThreadPool pool(4);
    
    for (int i = 0; i < 8; i++) {
        pool.enqueue([i] {
            std::cout << "任务 " << i << " 由线程 " 
                      << std::this_thread::get_id() << " 执行" << std::endl;
            std::this_thread::sleep_for(std::chrono::milliseconds(200));
        });
    }
    
    // 主线程等待
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    std::cout << "所有任务执行完成" << std::endl;
    
    return 0;
}