// Kotlin协程示例代码

import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*
import kotlin.system.measureTimeMillis

fun main() = runBlocking {
    println("=== Kotlin协程 ===")
    println()
    
    // 1. 协程基础
    println("--- 1. 协程基础 ---")
    
    // launch - 启动协程
    println("launch启动协程:")
    val job = launch {
        delay(1000)
        println("  协程1执行完成")
    }
    println("  主程序继续执行")
    job.join()
    println()
    
    // async - 异步获取结果
    println("async异步获取结果:")
    val deferred = async {
        delay(1000)
        "Hello from async"
    }
    val result = deferred.await()
    println("  async结果: $result")
    println()
    
    // 2. 挂起函数
    println("--- 2. 挂起函数 ---")
    
    suspend fun doSomething(): String {
        delay(500)
        return "任务完成"
    }
    
    println("调用挂起函数:")
    val result2 = doSomething()
    println("  结果: $result2")
    println()
    
    // 3. 并发执行
    println("--- 3. 并发执行 ---")
    
    suspend fun fetchUser(): String {
        delay(1000)
        return "张三"
    }
    
    suspend fun fetchProducts(): List<String> {
        delay(800)
        return listOf("产品1", "产品2", "产品3")
    }
    
    val time = measureTimeMillis {
        val userDeferred = async { fetchUser() }
        val productsDeferred = async { fetchProducts() }
        
        val user = userDeferred.await()
        val products = productsDeferred.await()
        
        println("  用户: $user")
        println("  产品: $products")
    }
    println("  总耗时: ${time}ms")
    println()
    
    // 4. 协程作用域
    println("--- 4. 协程作用域 ---")
    
    // GlobalScope - 全局作用域（不推荐）
    println("GlobalScope:")
    GlobalScope.launch {
        delay(100)
        println("  GlobalScope协程")
    }
    delay(200)
    
    // 自定义作用域
    println("自定义作用域:")
    val scope = CoroutineScope(Dispatchers.Default)
    val job2 = scope.launch {
        delay(100)
        println("  自定义作用域协程")
    }
    job2.join()
    scope.cancel()
    println()
    
    // 5. 协程上下文和Dispatchers
    println("--- 5. 协程上下文和Dispatchers ---")
    
    // Dispatchers.Default - CPU密集型
    println("Dispatchers.Default:")
    launch(Dispatchers.Default) {
        println("  运行在Default调度器")
        println("  线程: ${Thread.currentThread().name}")
    }.join()
    
    // Dispatchers.IO - IO密集型
    println("Dispatchers.IO:")
    launch(Dispatchers.IO) {
        println("  运行在IO调度器")
        println("  线程: ${Thread.currentThread().name}")
    }.join()
    
    // Dispatchers.Main - 主线程（Android/UI）
    println("Dispatchers.Main:")
    println("  用于UI更新（需要UI环境）")
    
    // withContext - 切换上下文
    println("withContext:")
    val result3 = withContext(Dispatchers.IO) {
        println("  IO操作...")
        delay(100)
        "IO结果"
    }
    println("  切换回原上下文: $result3")
    println()
    
    // 6. Job管理
    println("--- 6. Job管理 ---")
    
    val parentJob = Job()
    val childScope = CoroutineScope(Dispatchers.Default + parentJob)
    
    val childJob1 = childScope.launch {
        delay(1000)
        println("  子协程1完成")
    }
    
    val childJob2 = childScope.launch {
        delay(500)
        println("  子协程2完成")
    }
    
    println("取消父Job:")
    delay(200)
    parentJob.cancel()
    println("  父Job已取消")
    delay(100)
    println()
    
    // 7. 超时
    println("--- 7. 超时 ---")
    
    try {
        withTimeout(500) {
            delay(1000)
            println("  这个不会执行")
        }
    } catch (e: TimeoutCancellationException) {
        println("  超时异常捕获")
    }
    
    val result4 = withTimeoutOrNull(500) {
        delay(1000)
        "结果"
    }
    println("  withTimeoutOrNull结果: $result4")
    println()
    
    // 8. Flow - 异步流
    println("--- 8. Flow - 异步流 ---")
    
    // 创建Flow
    fun simpleFlow(): Flow<Int> = flow {
        for (i in 1..3) {
            delay(100)
            emit(i)
        }
    }
    
    println("Flow基础:")
    simpleFlow().collect { value ->
        println("  收到: $value")
    }
    
    // Flow操作符
    println("Flow操作符:")
    (1..5).asFlow()
        .filter { it % 2 == 0 }
        .map { it * it }
        .collect { println("  处理后: $it") }
    
    // 转换Flow
    println("Flow转换:")
    fun strings(): Flow<String> = flow {
        emit("Hello")
        emit("Kotlin")
        emit("Flow")
    }
    
    strings()
        .map { it.uppercase() }
        .collect { println("  大写: $it") }
    
    // 组合Flow
    println("Flow组合:")
    val nums = (1..3).asFlow()
    val strs = flowOf("A", "B", "C")
    
    nums.zip(strs) { a, b -> "$a$b" }
        .collect { println("  组合: $it") }
    
    // 限流
    println("Flow限流:")
    flow {
        emit(1)
        delay(50)
        emit(2)
        delay(50)
        emit(3)
    }
        .conflate()
        .collect { value ->
            println("  收到: $value")
            delay(100)
        }
    println()
    
    println("🎉 Kotlin协程学习完成！")
    println("💡 协程让异步编程变得简单！")
}
