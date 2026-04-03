#include <iostream>
#include <memory>
#include <vector>
#include <string>

// 内存布局示例
void memoryLayout() {
    std::cout << "=== 内存布局 ===" << std::endl;
    
    // 全局变量 - 静态存储区
    static int globalVar = 100;
    std::cout << "全局变量地址: " << &globalVar << std::endl;
    
    // 局部变量 - 栈区
    int localVar = 200;
    std::cout << "局部变量地址: " << &localVar << std::endl;
    
    // 动态分配 - 堆区
    int* heapVar = new int(300);
    std::cout << "堆变量地址: " << heapVar << std::endl;
    std::cout << "堆变量值: " << *heapVar << std::endl;
    
    // 释放堆内存
    delete heapVar;
}

// 动态内存分配
void dynamicMemory() {
    std::cout << "\n=== 动态内存分配 ===" << std::endl;
    
    // 分配单个对象
    int* single = new int(42);
    std::cout << "单个对象: " << *single << std::endl;
    delete single;
    
    // 分配数组
    int* array = new int[5];
    for (int i = 0; i < 5; i++) {
        array[i] = i * 10;
    }
    std::cout << "数组元素: ";
    for (int i = 0; i < 5; i++) {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
    delete[] array;
    
    // 分配失败
    try {
        // 尝试分配非常大的内存
        int* largeArray = new int[1000000000000];
        delete[] largeArray;
    } catch (const std::bad_alloc& e) {
        std::cout << "内存分配失败: " << e.what() << std::endl;
    }
}

// 智能指针
void smartPointers() {
    std::cout << "\n=== 智能指针 ===" << std::endl;
    
    // unique_ptr
    std::cout << "unique_ptr: " << std::endl;
    std::unique_ptr<int> uniquePtr = std::make_unique<int>(100);
    std::cout << "值: " << *uniquePtr << std::endl;
    // 转移所有权
    std::unique_ptr<int> anotherPtr = std::move(uniquePtr);
    if (!uniquePtr) {
        std::cout << "uniquePtr 已转移所有权" << std::endl;
    }
    std::cout << "anotherPtr 值: " << *anotherPtr << std::endl;
    
    // shared_ptr
    std::cout << "\nshared_ptr: " << std::endl;
    std::shared_ptr<int> sharedPtr1 = std::make_shared<int>(200);
    std::cout << "sharedPtr1 值: " << *sharedPtr1 << std::endl;
    std::cout << "引用计数: " << sharedPtr1.use_count() << std::endl;
    
    { 
        std::shared_ptr<int> sharedPtr2 = sharedPtr1;
        std::cout << "sharedPtr2 值: " << *sharedPtr2 << std::endl;
        std::cout << "引用计数: " << sharedPtr1.use_count() << std::endl;
    } // sharedPtr2 超出作用域
    
    std::cout << "引用计数: " << sharedPtr1.use_count() << std::endl;
    
    // weak_ptr
    std::cout << "\nweak_ptr: " << std::endl;
    std::weak_ptr<int> weakPtr = sharedPtr1;
    if (auto lockedPtr = weakPtr.lock()) {
        std::cout << "weak_ptr 锁定后值: " << *lockedPtr << std::endl;
        std::cout << "引用计数: " << lockedPtr.use_count() << std::endl;
    }
    
    // 重置 shared_ptr
    sharedPtr1.reset();
    if (auto lockedPtr = weakPtr.lock()) {
        std::cout << "weak_ptr 仍然有效" << std::endl;
    } else {
        std::cout << "weak_ptr 已过期" << std::endl;
    }
}

// RAII示例
class FileHandler {
private:
    FILE* file;

public:
    FileHandler(const char* filename, const char* mode) {
        file = fopen(filename, mode);
        if (file) {
            std::cout << "文件打开成功" << std::endl;
        } else {
            std::cout << "文件打开失败" << std::endl;
        }
    }
    
    ~FileHandler() {
        if (file) {
            fclose(file);
            std::cout << "文件关闭成功" << std::endl;
        }
    }
    
    // 禁止拷贝
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
    
    // 允许移动
    FileHandler(FileHandler&& other) noexcept : file(other.file) {
        other.file = nullptr;
        std::cout << "文件处理器移动构造" << std::endl;
    }
    
    FileHandler& operator=(FileHandler&& other) noexcept {
        if (this != &other) {
            if (file) {
                fclose(file);
            }
            file = other.file;
            other.file = nullptr;
            std::cout << "文件处理器移动赋值" << std::endl;
        }
        return *this;
    }
    
    // 写入数据
    void write(const char* data) {
        if (file) {
            fprintf(file, "%s", data);
        }
    }
};

void raiiExample() {
    std::cout << "\n=== RAII示例 ===" << std::endl;
    
    { 
        FileHandler file("test.txt", "w");
        file.write("Hello RAII!\n");
        // 文件会在作用域结束时自动关闭
    }
    
    // 移动语义
    FileHandler file1("test1.txt", "w");
    file1.write("Hello Move!\n");
    
    FileHandler file2 = std::move(file1);
    file2.write("More data\n");
}

// 简单的内存池
class MemoryPool {
private:
    struct Block {
        Block* next;
    };
    
    Block* freeList;
    size_t blockSize;
    size_t poolSize;
    char* pool;

public:
    MemoryPool(size_t blockSize, size_t numBlocks) : blockSize(blockSize), poolSize(numBlocks) {
        // 分配内存池
        pool = new char[blockSize * numBlocks];
        
        // 初始化自由链表
        freeList = nullptr;
        for (size_t i = 0; i < numBlocks; i++) {
            Block* block = reinterpret_cast<Block*>(&pool[i * blockSize]);
            block->next = freeList;
            freeList = block;
        }
        
        std::cout << "内存池初始化成功，块大小: " << blockSize << ", 块数量: " << numBlocks << std::endl;
    }
    
    ~MemoryPool() {
        delete[] pool;
        std::cout << "内存池销毁" << std::endl;
    }
    
    // 分配内存
    void* allocate() {
        if (freeList) {
            Block* block = freeList;
            freeList = freeList->next;
            return block;
        }
        return nullptr; // 内存池已满
    }
    
    // 释放内存
    void deallocate(void* ptr) {
        if (ptr) {
            Block* block = reinterpret_cast<Block*>(ptr);
            block->next = freeList;
            freeList = block;
        }
    }
};

void memoryPoolExample() {
    std::cout << "\n=== 内存池示例 ===" << std::endl;
    
    MemoryPool pool(sizeof(int), 10);
    
    // 分配内存
    int* p1 = static_cast<int*>(pool.allocate());
    int* p2 = static_cast<int*>(pool.allocate());
    int* p3 = static_cast<int*>(pool.allocate());
    
    *p1 = 10;
    *p2 = 20;
    *p3 = 30;
    
    std::cout << "p1: " << *p1 << ", p2: " << *p2 << ", p3: " << *p3 << std::endl;
    
    // 释放内存
    pool.deallocate(p2);
    
    // 重新分配
    int* p4 = static_cast<int*>(pool.allocate());
    *p4 = 40;
    std::cout << "p4: " << *p4 << std::endl;
}

int main() {
    memoryLayout();
    dynamicMemory();
    smartPointers();
    raiiExample();
    memoryPoolExample();
    
    return 0;
}