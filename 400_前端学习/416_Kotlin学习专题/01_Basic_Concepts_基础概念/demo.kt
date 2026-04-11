// Kotlin基础概念示例代码

fun main() {
    println("=== Kotlin基础概念 ===")
    println()
    
    // 1. 变量和常量
    println("--- 1. 变量和常量 ---")
    
    // var - 可变变量
    var name = "张三"
    println("初始name: $name")
    name = "李四"
    println("修改后name: $name")
    
    // val - 只读变量（类似Java的final）
    val PI = 3.14159
    println("PI: $PI")
    // PI = 3.14 // 错误：val不能重新赋值
    
    // 显式类型声明
    var age: Int = 18
    var height: Double = 175.5
    var isStudent: Boolean = true
    var grade: Char = 'A'
    
    println("age: $age, height: $height, isStudent: $isStudent, grade: $grade")
    println()
    
    // 2. 基本数据类型
    println("--- 2. 基本数据类型 ---")
    
    // 整数类型
    val byteValue: Byte = 127
    val shortValue: Short = 32767
    val intValue: Int = 2147483647
    val longValue: Long = 9223372036854775807L
    println("Byte: $byteValue, Short: $shortValue, Int: $intValue, Long: $longValue")
    
    // 浮点数类型
    val floatValue: Float = 3.14f
    val doubleValue: Double = 3.14159265359
    println("Float: $floatValue, Double: $doubleValue")
    
    // 布尔类型
    val isTrue: Boolean = true
    val isFalse: Boolean = false
    println("Boolean: true=$isTrue, false=$isFalse")
    
    // 字符类型
    val charA: Char = 'A'
    val charChinese: Char = '中'
    println("Char: $charA, $charChinese")
    println()
    
    // 3. 字符串
    println("--- 3. 字符串 ---")
    
    // 普通字符串
    val str1 = "Hello, Kotlin!"
    println(str1)
    
    // 字符串模板
    val userName = "张三"
    val greeting = "你好, $userName!"
    println(greeting)
    
    // 表达式模板
    val a = 10
    val b = 20
    val sumStr = "$a + $b = ${a + b}"
    println(sumStr)
    
    // 多行字符串
    val multiLineStr = """
        这是第一行
        这是第二行
        这是第三行
    """.trimIndent()
    println(multiLineStr)
    
    // 字符串常用方法
    val text = "Hello Kotlin"
    println("长度: ${text.length}")
    println("大写: ${text.uppercase()}")
    println("小写: ${text.lowercase()}")
    println("是否包含Kotlin: ${text.contains("Kotlin")}")
    println("截取0-5: ${text.substring(0, 5)}")
    println()
    
    // 4. 类型转换
    println("--- 4. 类型转换 ---")
    
    val intNum = 100
    val longNum: Long = intNum.toLong()
    val doubleNum: Double = intNum.toDouble()
    val stringNum: String = intNum.toString()
    
    println("Int $intNum -> Long: $longNum")
    println("Int $intNum -> Double: $doubleNum")
    println("Int $intNum -> String: $stringNum")
    
    // 字符串转数字
    val strNum = "123"
    val parsedInt: Int? = strNum.toIntOrNull()
    val parsedDouble: Double? = "3.14".toDoubleOrNull()
    println("String '$strNum' -> Int: $parsedInt")
    println("String '3.14' -> Double: $parsedDouble")
    println()
    
    // 5. 运算符
    println("--- 5. 运算符 ---")
    
    val x = 15
    val y = 4
    
    println("$x + $y = ${x + y}")
    println("$x - $y = ${x - y}")
    println("$x * $y = ${x * y}")
    println("$x / $y = ${x / y}")
    println("$x % $y = ${x % y}")
    
    // 比较运算符
    println("$x > $y: ${x > y}")
    println("$x < $y: ${x < y}")
    println("$x == 15: ${x == 15}")
    println("$x != 15: ${x != 15}")
    
    // 逻辑运算符
    val condition1 = true
    val condition2 = false
    println("$condition1 && $condition2: ${condition1 && condition2}")
    println("$condition1 || $condition2: ${condition1 || condition2}")
    println("!$condition1: ${!condition1}")
    println()
    
    // 6. 空安全
    println("--- 6. 空安全 ---")
    
    // 非空类型（默认）
    var nonNullStr: String = "Hello"
    // nonNullStr = null // 错误：不能赋值null
    
    // 可空类型
    var nullableStr: String? = "Hello"
    nullableStr = null // 正确
    println("nullableStr: $nullableStr")
    
    // 安全调用运算符 ?.
    var nullableName: String? = "张三"
    val length1 = nullableName?.length
    println("nullableName?.length: $length1")
    
    nullableName = null
    val length2 = nullableName?.length
    println("nullableName?.length (null): $length2")
    
    // Elvis运算符 ?:
    val nameLength = nullableName?.length ?: 0
    println("nameLength (Elvis): $nameLength")
    
    // 非空断言 !!（慎用）
    val safeName: String? = "李四"
    val safeLength = safeName!!.length
    println("safeName!!.length: $safeLength")
    
    // 安全转换 as?
    val obj: Any = "Hello"
    val str: String? = obj as? String
    val int: Int? = obj as? Int
    println("obj as? String: $str")
    println("obj as? Int: $int")
    println()
    
    // 7. 控制流
    println("--- 7. 控制流 ---")
    
    // if表达式
    val num = 18
    val result = if (num >= 18) {
        "成年"
    } else {
        "未成年"
    }
    println("$num 岁: $result")
    
    // when表达式（类似switch）
    val score = 85
    val gradeLevel = when {
        score >= 90 -> "优秀"
        score >= 80 -> "良好"
        score >= 60 -> "及格"
        else -> "不及格"
    }
    println("$score 分: $gradeLevel")
    
    // for循环
    println("for循环 1-5:")
    for (i in 1..5) {
        println("  $i")
    }
    
    // 遍历数组
    val fruits = arrayOf("苹果", "香蕉", "橙子")
    println("遍历数组:")
    for (fruit in fruits) {
        println("  $fruit")
    }
    
    // while循环
    println("while循环 1-3:")
    var count = 1
    while (count <= 3) {
        println("  $count")
        count++
    }
    println()
    
    // 8. 函数基础
    println("--- 8. 函数基础 ---")
    
    // 简单函数
    fun greet(name: String): String {
        return "你好, $name!"
    }
    println(greet("王五"))
    
    // 表达式函数体
    fun add(a: Int, b: Int): Int = a + b
    println("3 + 5 = ${add(3, 5)}")
    
    // 默认参数
    fun introduce(name: String, age: Int = 18) {
        println("我是$name, 今年$age岁")
    }
    introduce("赵六")
    introduce("钱七", 25)
    
    // 可变参数
    fun sum(vararg numbers: Int): Int {
        var total = 0
        for (num in numbers) {
            total += num
        }
        return total
    }
    println("sum(1, 2, 3, 4, 5) = ${sum(1, 2, 3, 4, 5)}")
    println()
    
    println("🎉 Kotlin基础概念学习完成！")
    println("💡 Kotlin是一门简洁、安全、现代的编程语言！")
}
