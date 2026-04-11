// Kotlin扩展示例代码

fun main() {
    println("=== Kotlin扩展 ===")
    println()
    
    // 1. 扩展函数
    println("--- 1. 扩展函数 ---")
    
    // String扩展
    fun String.addExclamation(): String {
        return "$this!"
    }
    
    val greeting = "Hello"
    println("greeting.addExclamation(): ${greeting.addExclamation()}")
    
    // Int扩展
    fun Int.square(): Int = this * this
    
    val num = 5
    println("$num.square(): ${num.square()}")
    
    // List扩展
    fun <T> List<T>.second(): T? {
        return if (size >= 2) this[1] else null
    }
    
    val list = listOf(1, 2, 3, 4, 5)
    println("list.second(): ${list.second()}")
    
    // MutableList扩展
    fun MutableList<Int>.swap(i: Int, j: Int) {
        val temp = this[i]
        this[i] = this[j]
        this[j] = temp
    }
    
    val mutableList = mutableListOf(1, 2, 3)
    mutableList.swap(0, 2)
    println("swap后: $mutableList")
    
    // 可空类型扩展
    fun String?.isNullOrEmptyOrBlank(): Boolean {
        return this == null || this.isEmpty() || this.isBlank()
    }
    
    val nullStr: String? = null
    val emptyStr = ""
    val blankStr = "   "
    val normalStr = "Hello"
    println("nullStr.isNullOrEmptyOrBlank(): ${nullStr.isNullOrEmptyOrBlank()}")
    println("emptyStr.isNullOrEmptyOrBlank(): ${emptyStr.isNullOrEmptyOrBlank()}")
    println("blankStr.isNullOrEmptyOrBlank(): ${blankStr.isNullOrEmptyOrBlank()}")
    println("normalStr.isNullOrEmptyOrBlank(): ${normalStr.isNullOrEmptyOrBlank()}")
    println()
    
    // 2. 扩展属性
    println("--- 2. 扩展属性 ---")
    
    // String扩展属性
    val String.isEmail: Boolean
        get() = contains("@") && contains(".")
    
    val email1 = "test@example.com"
    val email2 = "invalid-email"
    println("email1.isEmail: ${email1.isEmail}")
    println("email2.isEmail: ${email2.isEmail}")
    
    // List扩展属性
    val <T> List<T>.middleIndex: Int
        get() = size / 2
    
    val <T> List<T>.middleElement: T?
        get() = if (isNotEmpty()) this[middleIndex] else null
    
    val numbers = listOf(1, 2, 3, 4, 5)
    println("numbers.middleIndex: ${numbers.middleIndex}")
    println("numbers.middleElement: ${numbers.middleElement}")
    
    // 可变扩展属性（需要 backing field）
    var StringBuilder.lastChar: Char
        get() = if (isNotEmpty()) this[length - 1] else '\u0000'
        set(value) {
            if (isNotEmpty()) {
                this.setCharAt(length - 1, value)
            }
        }
    
    val sb = StringBuilder("Hello")
    println("sb.lastChar: ${sb.lastChar}")
    sb.lastChar = '!'
    println("sb: $sb")
    println()
    
    // 3. 作用域函数
    println("--- 3. 作用域函数 ---")
    
    // let - 上下文对象是it, 返回最后一个表达式
    println("let:")
    val str: String? = "Hello Kotlin"
    val length = str?.let {
        println("  字符串: $it")
        it.length
    }
    println("  长度: $length")
    
    // run - 上下文对象是this, 返回最后一个表达式
    println("run:")
    val result = "Hello".run {
        println("  字符串: $this")
        uppercase()
    }
    println("  结果: $result")
    
    // with - 非扩展函数, 上下文对象是this, 返回最后一个表达式
    println("with:")
    val list2 = mutableListOf<String>()
    val size = with(list2) {
        add("A")
        add("B")
        add("C")
        size
    }
    println("  list: $list2, size: $size")
    
    // apply - 上下文对象是this, 返回对象本身
    println("apply:")
    val person = Person().apply {
        name = "张三"
        age = 18
        city = "北京"
    }
    println("  person: $person")
    
    // also - 上下文对象是it, 返回对象本身
    println("also:")
    val numbers2 = mutableListOf(1, 2, 3).also {
        println("  添加前: $it")
        it.add(4)
        println("  添加后: $it")
    }
    println("  numbers2: $numbers2")
    
    // 作用域函数选择
    println("作用域函数选择:")
    println("  let: 对非空对象操作, 转换结果")
    println("  run: 配置对象并计算结果")
    println("  with: 对对象进行一组操作")
    println("  apply: 配置对象")
    println("  also: 额外的副作用操作")
    println()
    
    // 4. 伴生对象扩展
    println("--- 4. 伴生对象扩展 ---")
    
    class MyClass {
        companion object
    }
    
    fun MyClass.Companion.sayHello() {
        println("Hello from companion extension!")
    }
    
    fun MyClass.Companion.create(name: String): MyClass {
        println("Creating $name")
        return MyClass()
    }
    
    MyClass.sayHello()
    val obj = MyClass.create("test")
    println()
    
    // 5. 常用标准库扩展
    println("--- 5. 常用标准库扩展 ---")
    
    // String扩展
    val s = "  Hello World  "
    println("String扩展:")
    println("  s.trim(): '${s.trim()}'")
    println("  s.uppercase(): '${s.uppercase()}'")
    println("  s.lowercase(): '${s.lowercase()}'")
    println("  s.capitalize(): '${s.trim().replaceFirstChar { it.uppercase() }}'")
    println("  s.startsWith(\"  He\"): ${s.startsWith("  He")}")
    println("  s.endsWith(\"d  \"): ${s.endsWith("d  ")}")
    println("  s.contains(\"World\"): ${s.contains("World")}")
    println("  s.substring(2, 7): '${s.substring(2, 7)}'")
    println("  s.split(\" \"): ${s.trim().split(" ")}")
    println("  s.repeat(2): '${s.trim().repeat(2)}'")
    
    // Collection扩展
    val nums = listOf(1, 2, 3, 4, 5)
    println("\nCollection扩展:")
    println("  nums.sum(): ${nums.sum()}")
    println("  nums.average(): ${nums.average()}")
    println("  nums.maxOrNull(): ${nums.maxOrNull()}")
    println("  nums.minOrNull(): ${nums.minOrNull()}")
    println("  nums.count(): ${nums.count()}")
    println("  nums.any { it > 3 }: ${nums.any { it > 3 }}")
    println("  nums.all { it < 10 }: ${nums.all { it < 10 }}")
    println("  nums.none { it > 10 }: ${nums.none { it > 10 }}")
    println("  nums.firstOrNull(): ${nums.firstOrNull()}")
    println("  nums.lastOrNull(): ${nums.lastOrNull()}")
    println("  nums.find { it > 3 }: ${nums.find { it > 3 }}")
    println("  nums.indexOf(3): ${nums.indexOf(3)}")
    println("  nums.take(3): ${nums.take(3)}")
    println("  nums.drop(2): ${nums.drop(2)}")
    println("  nums.sorted(): ${nums.sorted()}")
    println("  nums.sortedDescending(): ${nums.sortedDescending()}")
    println("  nums.reversed(): ${nums.reversed()}")
    println("  nums.shuffled(): ${nums.shuffled()}")
    println("  nums.distinct(): ${nums.distinct()}")
    println("  nums.joinToString(): ${nums.joinToString()}")
    println("  nums.joinToString(separator = \", \", prefix = \"[\", suffix = \"]\"): ${nums.joinToString(separator = ", ", prefix = "[", suffix = "]")}")
    println()
    
    println("🎉 Kotlin扩展学习完成！")
    println("💡 扩展函数和作用域函数让代码更简洁！")
}

class Person {
    var name: String = ""
    var age: Int = 0
    var city: String = ""
    
    override fun toString(): String {
        return "Person(name='$name', age=$age, city='$city')"
    }
}
