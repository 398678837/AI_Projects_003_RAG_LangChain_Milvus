package main

import (
    "fmt"
    "time"
    "sync"
)

func sayHello() {
    fmt.Println("Hello, World!")
}

var (
    counter int
    mutex   sync.Mutex
)

func increment() {
    mutex.Lock()
    defer mutex.Unlock()
    counter++
}

func worker(wg *sync.WaitGroup, id int) {
    defer wg.Done()
    fmt.Printf("Worker %d started\n", id)
    // 模拟工作
    time.Sleep(100 * time.Millisecond)
    fmt.Printf("Worker %d finished\n", id)
}

func producer(ch chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for i := 0; i < 10; i++ {
        ch <- i
        fmt.Printf("Produced: %d\n", i)
        time.Sleep(50 * time.Millisecond)
    }
    close(ch)
}

func consumer(ch <-chan int, wg *sync.WaitGroup) {
    defer wg.Done()
    for value := range ch {
        fmt.Printf("Consumed: %d\n", value)
        time.Sleep(100 * time.Millisecond)
    }
}

func workerPool(jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for job := range jobs {
        results <- job * 2
        time.Sleep(50 * time.Millisecond)
    }
}

func main() {
    // 1. Goroutine
    fmt.Println("=== Goroutine ===")
    
    // 启动goroutine
    go sayHello()
    
    // 等待goroutine执行完成
    time.Sleep(1 * time.Second)
    
    // 2. Channel
    fmt.Println("\n=== Channel ===")
    
    // 创建channel
    ch := make(chan string)
    
    // 启动goroutine
    go func() {
        ch <- "Hello, World!"
    }()
    
    // 从channel接收数据
    message := <-ch
    fmt.Println(message)
    
    // 3. 带缓冲的Channel
    fmt.Println("\n=== 带缓冲的Channel ===")
    
    // 创建带缓冲的channel
    ch2 := make(chan string, 2)
    
    // 向channel发送数据
    ch2 <- "Hello"
    ch2 <- "World"
    
    // 从channel接收数据
    fmt.Println(<-ch2)
    fmt.Println(<-ch2)
    
    // 4. Mutex
    fmt.Println("\n=== Mutex ===")
    
    // 启动多个goroutine
    for i := 0; i < 1000; i++ {
        go increment()
    }
    
    // 等待goroutine执行完成
    time.Sleep(1 * time.Second)
    
    fmt.Printf("Counter: %d\n", counter)
    
    // 5. WaitGroup
    fmt.Println("\n=== WaitGroup ===")
    
    var wg sync.WaitGroup
    
    // 启动多个goroutine
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go worker(&wg, i)
    }
    
    // 等待所有goroutine执行完成
    wg.Wait()
    fmt.Println("All workers finished")
    
    // 6. 生产者-消费者模式
    fmt.Println("\n=== 生产者-消费者模式 ===")
    
    ch3 := make(chan int, 5)
    var wg2 sync.WaitGroup
    
    wg2.Add(2)
    go producer(ch3, &wg2)
    go consumer(ch3, &wg2)
    
    wg2.Wait()
    fmt.Println("All done")
    
    // 7. 工作池模式
    fmt.Println("\n=== 工作池模式 ===")
    
    jobs := make(chan int, 100)
    results := make(chan int, 100)
    var wg3 sync.WaitGroup
    
    // 启动3个worker
    for w := 1; w <= 3; w++ {
        wg3.Add(1)
        go workerPool(jobs, results, &wg3)
    }
    
    // 发送10个任务
    for j := 1; j <= 10; j++ {
        jobs <- j
    }
    close(jobs)
    
    // 等待所有worker完成
    wg3.Wait()
    close(results)
    
    // 收集结果
    for result := range results {
        fmt.Printf("Result: %d\n", result)
    }
}