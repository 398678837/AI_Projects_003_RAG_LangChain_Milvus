# 并发

## 1. 并发基础

### Goroutine
```go
package main

import "fmt"
import "time"

func sayHello() {
    fmt.Println("Hello, World!")
}

func main() {
    // 启动goroutine
    go sayHello()
    
    // 等待goroutine执行完成
    time.Sleep(1 * time.Second)
}
```

### Channel
```go
package main

import "fmt"

func main() {
    // 创建channel
    ch := make(chan string)
    
    // 启动goroutine
    go func() {
        ch <- "Hello, World!"
    }()
    
    // 从channel接收数据
    message := <-ch
    fmt.Println(message)
}
```

### 带缓冲的Channel
```go
package main

import "fmt"

func main() {
    // 创建带缓冲的channel
    ch := make(chan string, 2)
    
    // 向channel发送数据
    ch <- "Hello"
    ch <- "World"
    
    // 从channel接收数据
    fmt.Println(<-ch)
    fmt.Println(<-ch)
}
```

## 2. 并发同步

### Mutex
```go
package main

import "fmt"
import "sync"
import "time"

var (    counter int    mutex   sync.Mutex)

func increment() {
    mutex.Lock()
    defer mutex.Unlock()
    counter++
}

func main() {
    // 启动多个goroutine
    for i := 0; i < 1000; i++ {
        go increment()
    }
    
    // 等待goroutine执行完成
    time.Sleep(1 * time.Second)
    
    fmt.Printf("Counter: %d\n", counter)
}
```

### WaitGroup
```go
package main

import "fmt"
import "sync"

func worker(wg *sync.WaitGroup, id int) {
    defer wg.Done()
    fmt.Printf("Worker %d started\n", id)
    // 模拟工作
    for i := 0; i < 1000000000; i++ {
    }
    fmt.Printf("Worker %d finished\n", id)
}

func main() {
    var wg sync.WaitGroup
    
    // 启动多个goroutine
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go worker(&wg, i)
    }
    
    // 等待所有goroutine执行完成
    wg.Wait()
    fmt.Println("All workers finished")
}
```

## 3. 并发模式

### 生产者-消费者模式
```go
package main

import "fmt"
import "sync"

func producer(ch chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for i := 0; i < 10; i++ {
        ch <- i
        fmt.Printf("Produced: %d\n", i)
    }
    close(ch)
}

func consumer(ch <-chan int, wg *sync.WaitGroup) {
    defer wg.Done()
    for value := range ch {
        fmt.Printf("Consumed: %d\n", value)
    }
}

func main() {
    ch := make(chan int, 5)
    var wg sync.WaitGroup
    
    wg.Add(2)
    go producer(ch, &wg)
    go consumer(ch, &wg)
    
    wg.Wait()
    fmt.Println("All done")
}
```

### 工作池模式
```go
package main

import "fmt"
import "sync"

func worker(jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for job := range jobs {
        results <- job * 2
    }
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)
    var wg sync.WaitGroup
    
    // 启动3个worker
    for w := 1; w <= 3; w++ {
        wg.Add(1)
        go worker(jobs, results, &wg)
    }
    
    // 发送10个任务
    for j := 1; j <= 10; j++ {
        jobs <- j
    }
    close(jobs)
    
    // 等待所有worker完成
    wg.Wait()
    close(results)
    
    // 收集结果
    for result := range results {
        fmt.Printf("Result: %d\n", result)
    }
}
```

---

**更新时间：2026-04-04**