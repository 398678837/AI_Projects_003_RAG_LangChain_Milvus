// Kotlin核心语法示例代码

fun main() {
    println("=== Kotlin核心语法 ===")
    println()
    
    // 1. 函数进阶
    println("--- 1. 函数进阶 ---")
    
    // 单表达式函数
    fun square(x: Int) = x * x
    println("square(5) = ${square(5)}")
    
    // 本地函数（函数内定义函数）
    fun calculate(x: Int, y: Int): Int {
        fun add(a: Int, b: Int) = a + b
        fun multiply(a: Int, b: Int) = a * b
        return add(multiply(x, x), multiply(y, y))
    }
    println("calculate(3, 4) = ${calculate(3, 4)}")
    
    // 可变参数
    fun printAll(vararg messages: String) {
        for (msg in messages) {
            println("  $msg")
        }
    }
    println("可变参数:")
    printAll("Hello", "Kotlin", "World")
    
    // 使用展开运算符
    val msgArray = arrayOf("A", "B", "C")
    println("展开运算符:")
    printAll(*msgArray)
    println()
    
    // 2. Lambda表达式
    println("--- 2. Lambda表达式 ---")
    
    // 基本Lambda
    val sum = { a: Int, b: Int -> a + b }
    println("sum(3, 5) = ${sum(3, 5)}")
    
    // 高阶函数
    fun operate(a: Int, b: Int, operation: (Int, Int) -> Int): Int {
        return operation(a, b)
    }
    
    val result1 = operate(10, 5) { x, y -> x + y }
    val result2 = operate(10, 5) { x, y -> x * y }
    println("operate(10, 5, +) = $result1")
    println("operate(10, 5, *) = $result2")
    
    // it关键字（单个参数）
    val numbers = listOf(1, 2, 3, 4, 5)
    val doubled = numbers.map { it * 2 }
    println("doubled: $doubled")
    
    // 函数引用
    fun isEven(n: Int) = n % 2 == 0
    val evens = numbers.filter(::isEven)
    println("evens: $evens")
    println()
    
    // 3. 数组
    println("--- 3. 数组 ---")
    
    // 创建数组
    val arr1 = arrayOf(1, 2, 3, 4, 5)
    val arr2 = IntArray(5) { it * 2 }
    val arr3 = Array(3) { "Item $it" }
    
    println("arr1: ${arr1.contentToString()}")
    println("arr2: ${arr2.contentToString()}")
    println("arr3: ${arr3.contentToString()}")
    
    // 访问元素
    println("arr1[0]: ${arr1[0]}")
    println("arr1[2]: ${arr1[2]}")
    
    // 修改元素
    arr1[0] = 100
    println("修改后arr1: ${arr1.contentToString()}")
    
    // 数组遍历
    println("数组遍历:")
    for (num in arr2) {
        print("$num ")
    }
    println()
    
    // 数组常用操作
    println("arr2.size: ${arr2.size}")
    println("arr2.sum(): ${arr2.sum()}")
    println("arr2.average(): ${arr2.average()}")
    println("arr2.contains(4): ${arr2.contains(4)}")
    println()
    
    // 4. 范围
    println("--- 4. 范围 ---")
    
    // 递增范围
    val range1 = 1..5
    println("1..5:")
    for (i in range1) print("$i ")
    println()
    
    // 递减范围
    val range2 = 5 downTo 1
    println("5 downTo 1:")
    for (i in range2) print("$i ")
    println()
    
    // 带步长的范围
    val range3 = 1..10 step 2
    println("1..10 step 2:")
    for (i in range3) print("$i ")
    println()
    
    // 半开范围
    val range4 = 1 until 5
    println("1 until 5:")
    for (i in range4) print("$i ")
    println()
    
    // 范围检查
    val x = 3
    println("$x in 1..5: ${x in 1..5}")
    println("$x !in 6..10: ${x !in 6..10}")
    println()
    
    // 5. 字符串操作
    println("--- 5. 字符串操作 ---")
    
    val str = "Hello Kotlin World"
    
    // 字符串遍历
    println("字符串遍历:")
    for (char in str) {
        print("$char ")
    }
    println()
    
    // 字符串索引
    println("str[0]: ${str[0]}")
    println("str[6]: ${str[6]}")
    println("str.last(): ${str.last()}")
    
    // 子字符串
    println("str.substring(6, 12): ${str.substring(6, 12)}")
    
    // 分割
    val words = str.split(" ")
    println("split: $words")
    
    // 替换
    val replaced = str.replace("World", "Kotlin")
    println("replaced: $replaced")
    
    // 去除空白
    val messyStr = "  Hello  Kotlin  "
    println("trim: '${messyStr.trim()}'")
    println()
    
    // 6. 解构声明
    println("--- 6. 解构声明 ---")
    
    // 数据类解构
    data class Person(val name: String, val age: Int)
    val person = Person("张三", 18)
    val (name, age) = person
    println("name: $name, age: $age")
    
    // 忽略某个值
    val (name2, _) = person
    println("name2: $name2")
    
    // 遍历Map时解构
    val map = mapOf("a" to 1, "b" to 2, "c" to 3)
    println("Map遍历:")
    for ((key, value) in map) {
        println("  $key -> $value")
    }
    println()
    
    // 7. 运算符重载
    println("--- 7. 运算符重载 ---")
    
    data class Point(val x: Int, val y: Int) {
        operator fun plus(other: Point): Point {
            return Point(x + other.x, y + other.y)
        }
        
        operator fun times(n: Int): Point {
            return Point(x * n, y * n)
        }
    }
    
    val p1 = Point(1, 2)
    val p2 = Point(3, 4)
    val p3 = p1 + p2
    val p4 = p1 * 3
    
    println("p1: (${p1.x}, ${p1.y})")
    println("p2: (${p2.x}, ${p2.y})")
    println("p1 + p2: (${p3.x}, ${p3.y})")
    println("p1 * 3: (${p4.x}, ${p4.y})")
    println()
    
    // 8. 空安全进阶
    println("--- 8. 空安全进阶 ---")
    
    // let函数
    fun processString(str: String?) {
        str?.let {
            println("处理字符串: $it")
            println("长度: ${it.length}")
        } ?: run {
            println("字符串为空")
        }
    }
    
    processString("Hello")
    processString(null)
    
    // also函数
    var strVar: String? = "Kotlin"
    strVar?.also {
        println("also: $it")
    }
    
    // apply函数
    val sb = StringBuilder().apply {
        append("Hello")
        append(" ")
        append("Kotlin")
    }
    println("apply: $sb")
    
    // with函数
    val list = mutableListOf<String>()
    val result = with(list) {
        add("A")
        add("B")
        add("C")
        size
    }
    println("with: $list, size: $result")
    println()
    
    println("🎉 Kotlin核心语法学习完成！")
    println("💡 Lambda和高阶函数是Kotlin的强大特性！")
}
