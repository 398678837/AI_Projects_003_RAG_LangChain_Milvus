import java.util.concurrent.*;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

// 1. 线程的创建
class MyThread extends Thread {
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("MyThread: " + i);
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class MyRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("MyRunnable: " + i);
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class MyCallable implements Callable<Integer> {
    @Override
    public Integer call() throws Exception {
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        return sum;
    }
}

// 2. 线程同步
class Counter {
    private int count = 0;
    private Lock lock = new ReentrantLock();
    
    public synchronized void increment() {
        count++;
    }
    
    public void incrementWithLock() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
    }
    
    public int getCount() {
        return count;
    }
}

// 3. 线程通信
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

public class MultithreadingDemo {
    public static void main(String[] args) {
        // 1. 线程的创建
        System.out.println("=== 线程的创建 ===");
        MyThread thread1 = new MyThread();
        thread1.start();
        
        Thread thread2 = new Thread(new MyRunnable());
        thread2.start();
        
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Future<Integer> future = executor.submit(new MyCallable());
        try {
            int result = future.get();
            System.out.println("Callable结果：" + result);
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        executor.shutdown();
        
        // 2. 线程同步
        System.out.println("\n=== 线程同步 ===");
        Counter counter = new Counter();
        for (int i = 0; i < 10; i++) {
            new Thread(() -> {
                for (int j = 0; j < 100; j++) {
                    counter.increment();
                }
            }).start();
        }
        
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Counter结果：" + counter.getCount());
        
        // 3. 线程通信
        System.out.println("\n=== 线程通信 ===");
        Message message = new Message();
        
        new Thread(() -> {
            for (int i = 0; i < 3; i++) {
                message.write("消息" + i);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
        
        new Thread(() -> {
            for (int i = 0; i < 3; i++) {
                String content = message.read();
                System.out.println("收到：" + content);
            }
        }).start();
        
        // 4. 线程池
        System.out.println("\n=== 线程池 ===");
        ExecutorService fixedThreadPool = Executors.newFixedThreadPool(3);
        for (int i = 0; i < 5; i++) {
            int taskNum = i;
            fixedThreadPool.execute(() -> {
                System.out.println("线程池任务" + taskNum + "：" + Thread.currentThread().getName());
            });
        }
        fixedThreadPool.shutdown();
        
        // 5. 并发工具类
        System.out.println("\n=== 并发工具类 ===");
        CountDownLatch latch = new CountDownLatch(3);
        for (int i = 0; i < 3; i++) {
            int taskNum = i;
            new Thread(() -> {
                System.out.println("CountDownLatch任务" + taskNum + "完成");
                latch.countDown();
            }).start();
        }
        try {
            latch.await();
            System.out.println("所有CountDownLatch任务完成");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        // 6. 线程池的自定义
        System.out.println("\n=== 自定义线程池 ===");
        ThreadPoolExecutor customExecutor = new ThreadPoolExecutor(
            2, // 核心线程数
            4, // 最大线程数
            60, // 空闲线程存活时间
            TimeUnit.SECONDS, // 时间单位
            new ArrayBlockingQueue<>(10) // 任务队列
        );
        
        for (int i = 0; i < 10; i++) {
            int taskNum = i;
            customExecutor.execute(() -> {
                System.out.println("自定义线程池任务" + taskNum + "：" + Thread.currentThread().getName());
            });
        }
        customExecutor.shutdown();
    }
}