# Java多线程

## 1. 多线程概述

### 1.1 进程与线程
- **进程**：操作系统分配资源的基本单位
- **线程**：CPU调度的基本单位，一个进程可以包含多个线程

### 1.2 多线程的优势
- 提高程序响应速度
- 提高CPU利用率
- 改善程序结构

### 1.3 多线程的劣势
- 增加系统复杂度
- 可能导致线程安全问题
- 增加调试难度

## 2. 线程的创建

### 2.1 继承Thread类
```java
class MyThread extends Thread {
    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println("Thread: " + i);
        }
    }
}

// 使用
MyThread thread = new MyThread();
thread.start();
```

### 2.2 实现Runnable接口
```java
class MyRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println("Runnable: " + i);
        }
    }
}

// 使用
Thread thread = new Thread(new MyRunnable());
thread.start();
```

### 2.3 实现Callable接口
```java
class MyCallable implements Callable<Integer> {
    @Override
    public Integer call() throws Exception {
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        return sum;
    }
}

// 使用
ExecutorService executor = Executors.newSingleThreadExecutor();
Future<Integer> future = executor.submit(new MyCallable());
int result = future.get();
executor.shutdown();
```

### 2.4 使用线程池
```java
ExecutorService executor = Executors.newFixedThreadPool(5);
for (int i = 0; i < 10; i++) {
    executor.execute(() -> {
        System.out.println("Thread: " + Thread.currentThread().getName());
    });
}
executor.shutdown();
```

## 3. 线程的状态

### 3.1 线程的生命周期
1. **新建状态**（New）：线程对象被创建
2. **就绪状态**（Runnable）：调用start()方法后
3. **运行状态**（Running）：获得CPU时间片
4. **阻塞状态**（Blocked）：等待锁或IO操作
5. **等待状态**（Waiting）：调用wait()、join()等方法
6. **超时等待状态**（Timed Waiting）：调用sleep()、wait(timeout)等方法
7. **终止状态**（Terminated）：run()方法执行完毕

### 3.2 状态转换
```
新建 → 就绪 → 运行 → 终止
     ↓    ↑    ↓    ↑
     阻塞 ←    → 等待
```

## 4. 线程的控制

### 4.1 线程睡眠
```java
Thread.sleep(1000); // 睡眠1秒
```

### 4.2 线程等待
```java
thread.join(); // 等待线程执行完毕
thread.join(1000); // 等待1秒
```

### 4.3 线程让步
```java
Thread.yield(); // 让出CPU时间片
```

### 4.4 线程中断
```java
thread.interrupt(); // 中断线程

// 在run()方法中处理中断
if (Thread.currentThread().isInterrupted()) {
    return;
}
```

### 4.5 线程优先级
```java
thread.setPriority(Thread.MAX_PRIORITY); // 设置最高优先级
thread.setPriority(Thread.MIN_PRIORITY); // 设置最低优先级
thread.setPriority(Thread.NORM_PRIORITY); // 设置默认优先级
```

## 5. 线程同步

### 5.1 线程安全问题
```java
class Counter {
    private int count = 0;
    
    public void increment() {
        count++; // 非原子操作，可能导致线程安全问题
    }
}
```

### 5.2 synchronized关键字

#### 5.2.1 同步方法
```java
class Counter {
    private int count = 0;
    
    public synchronized void increment() {
        count++;
    }
}
```

#### 5.2.2 同步代码块
```java
class Counter {
    private int count = 0;
    private Object lock = new Object();
    
    public void increment() {
        synchronized (lock) {
            count++;
        }
    }
}
```

### 5.3 Lock接口
```java
class Counter {
    private int count = 0;
    private Lock lock = new ReentrantLock();
    
    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
    }
}
```

### 5.4 线程安全的集合
- `ConcurrentHashMap`：线程安全的HashMap
- `CopyOnWriteArrayList`：线程安全的ArrayList
- `CopyOnWriteArraySet`：线程安全的HashSet

## 6. 线程通信

### 6.1 wait()、notify()、notifyAll()
```java
class Message {
    private String content;
    private boolean empty = true;
    
    public synchronized String read() {
        while (empty) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        empty = true;
        notifyAll();
        return content;
    }
    
    public synchronized void write(String content) {
        while (!empty) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        empty = false;
        this.content = content;
        notifyAll();
    }
}
```

### 6.2 Lock与Condition
```java
class Message {
    private String content;
    private boolean empty = true;
    private Lock lock = new ReentrantLock();
    private Condition condition = lock.newCondition();
    
    public String read() {
        lock.lock();
        try {
            while (empty) {
                condition.await();
            }
            empty = true;
            condition.signalAll();
            return content;
        } catch (InterruptedException e) {
            e.printStackTrace();
            return null;
        } finally {
            lock.unlock();
        }
    }
    
    public void write(String content) {
        lock.lock();
        try {
            while (!empty) {
                condition.await();
            }
            empty = false;
            this.content = content;
            condition.signalAll();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }
}
```

## 7. 线程池

### 7.1 线程池的优势
- 降低资源消耗
- 提高响应速度
- 提高线程的可管理性

### 7.2 线程池的创建
```java
// 固定大小线程池
ExecutorService fixedThreadPool = Executors.newFixedThreadPool(5);

// 缓存线程池
ExecutorService cachedThreadPool = Executors.newCachedThreadPool();

// 单线程线程池
ExecutorService singleThreadExecutor = Executors.newSingleThreadExecutor();

// 定时任务线程池
ScheduledExecutorService scheduledThreadPool = Executors.newScheduledThreadPool(5);
```

### 7.3 自定义线程池
```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    5, // 核心线程数
    10, // 最大线程数
    60, // 空闲线程存活时间
    TimeUnit.SECONDS, // 时间单位
    new ArrayBlockingQueue<>(100), // 任务队列
    Executors.defaultThreadFactory(), // 线程工厂
    new ThreadPoolExecutor.AbortPolicy() // 拒绝策略
);
```

### 7.4 拒绝策略
- `AbortPolicy`：直接抛出异常
- `CallerRunsPolicy`：由调用者线程执行任务
- `DiscardPolicy`：直接丢弃任务
- `DiscardOldestPolicy`：丢弃队列中最旧的任务

## 8. 并发工具类

### 8.1 CountDownLatch
```java
CountDownLatch latch = new CountDownLatch(3);

for (int i = 0; i < 3; i++) {
    new Thread(() -> {
        // 执行任务
        latch.countDown();
    }).start();
}

latch.await(); // 等待所有线程完成
```

### 8.2 CyclicBarrier
```java
CyclicBarrier barrier = new CyclicBarrier(3, () -> {
    System.out.println("所有线程都已到达屏障");
});

for (int i = 0; i < 3; i++) {
    new Thread(() -> {
        // 执行任务
        barrier.await(); // 等待其他线程
        // 继续执行
    }).start();
}
```

### 8.3 Semaphore
```java
Semaphore semaphore = new Semaphore(5); // 允许5个线程同时访问

for (int i = 0; i < 10; i++) {
    new Thread(() -> {
        try {
            semaphore.acquire(); // 获取许可
            // 执行任务
            semaphore.release(); // 释放许可
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }).start();
}
```

### 8.4 Exchanger
```java
Exchanger<String> exchanger = new Exchanger<>();

new Thread(() -> {
    String data1 = "数据1";
    try {
        String data2 = exchanger.exchange(data1);
        System.out.println("线程1收到：" + data2);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}).start();

new Thread(() -> {
    String data2 = "数据2";
    try {
        String data1 = exchanger.exchange(data2);
        System.out.println("线程2收到：" + data1);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}).start();
```

## 9. 死锁

### 9.1 死锁的条件
1. **互斥条件**：资源不能被共享，只能被一个线程使用
2. **请求与保持条件**：线程已经获得了一些资源，又请求新的资源
3. **不剥夺条件**：已经分配的资源不能被强制剥夺
4. **循环等待条件**：线程之间形成循环等待资源的关系

### 9.2 死锁的避免
- 破坏死锁的四个条件之一
- 按顺序获取锁
- 使用定时锁
- 避免嵌套锁

## 10. 并发编程的最佳实践

### 10.1 尽量使用并发工具类
- 优先使用`java.util.concurrent`包中的类
- 避免手动实现复杂的同步机制

### 10.2 尽量使用不可变对象
- 不可变对象天生线程安全
- 减少同步的需要

### 10.3 尽量使用局部变量
- 局部变量存储在栈中，线程安全
- 减少共享变量的使用

### 10.4 合理使用线程池
- 避免频繁创建和销毁线程
- 根据任务类型选择合适的线程池

### 10.5 注意线程安全问题
- 对共享变量进行适当的同步
- 使用线程安全的集合

### 10.6 避免死锁
- 按顺序获取锁
- 使用定时锁
- 避免嵌套锁

### 10.7 合理使用volatile关键字
- 保证变量的可见性
- 禁止指令重排序

### 10.8 合理使用原子类
- `AtomicInteger`、`AtomicLong`等
- 提供原子操作，避免使用synchronized

## 11. 性能优化

### 11.1 减少锁的粒度
- 只在必要的地方加锁
- 尽量使用细粒度锁

### 11.2 减少锁的持有时间
- 尽量缩短锁的持有时间
- 避免在锁内执行耗时操作

### 11.3 使用读写锁
- `ReentrantReadWriteLock`
- 读操作共享，写操作互斥

### 11.4 使用非阻塞算法
- `ConcurrentHashMap`等
- 基于CAS操作实现

### 11.5 合理使用并发集合
- 根据场景选择合适的并发集合
- 避免在并发集合上额外加锁