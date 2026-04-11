// Kotlin面向对象示例代码

fun main() {
    println("=== Kotlin面向对象 ===")
    println()
    
    // 1. 类和对象
    println("--- 1. 类和对象 ---")
    
    // 简单类
    class Person {
        var name: String = ""
        var age: Int = 0
        
        fun introduce() {
            println("我是$name, 今年$age岁")
        }
    }
    
    val person1 = Person()
    person1.name = "张三"
    person1.age = 18
    person1.introduce()
    
    // 带构造函数的类
    class Student(val name: String, val age: Int, val school: String) {
        fun study() {
            println("$name 在 $school 学习")
        }
    }
    
    val student1 = Student("李四", 20, "北京大学")
    println("name: ${student1.name}, age: ${student1.age}, school: ${student1.school}")
    student1.study()
    
    // 初始化块
    class Rectangle(val width: Int, val height: Int) {
        val area: Int
        
        init {
            area = width * height
            println("矩形创建: $width x $height, 面积: $area")
        }
    }
    
    val rect = Rectangle(5, 3)
    println()
    
    // 2. 数据类
    println("--- 2. 数据类 ---")
    
    data class User(val id: Int, val name: String, val email: String)
    
    val user1 = User(1, "王五", "wangwu@example.com")
    val user2 = User(1, "王五", "wangwu@example.com")
    val user3 = User(2, "赵六", "zhaoliu@example.com")
    
    println("user1: $user1")
    println("user1 == user2: ${user1 == user2}")
    println("user1 == user3: ${user1 == user3}")
    
    // 复制
    val user4 = user1.copy(name = "钱七")
    println("user4: $user4")
    
    // 解构
    val (id, name, email) = user1
    println("id: $id, name: $name, email: $email")
    println()
    
    // 3. 单例对象
    println("--- 3. 单例对象 ---")
    
    object DatabaseConfig {
        val host = "localhost"
        val port = 3306
        val database = "mydb"
        
        fun getUrl(): String {
            return "jdbc:mysql://$host:$port/$database"
        }
    }
    
    println("DatabaseConfig.host: ${DatabaseConfig.host}")
    println("DatabaseConfig.getUrl(): ${DatabaseConfig.getUrl()}")
    
    // 伴生对象
    class MathUtils {
        companion object {
            fun add(a: Int, b: Int) = a + b
            fun multiply(a: Int, b: Int) = a * b
            const val PI = 3.14159
        }
    }
    
    println("MathUtils.add(3, 5): ${MathUtils.add(3, 5)}")
    println("MathUtils.PI: ${MathUtils.PI}")
    println()
    
    // 4. 继承
    println("--- 4. 继承 ---")
    
    open class Animal(val name: String) {
        open fun makeSound() {
            println("$name 发出声音")
        }
        
        fun eat() {
            println("$name 吃东西")
        }
    }
    
    class Dog(name: String) : Animal(name) {
        override fun makeSound() {
            println("$name 汪汪叫")
        }
        
        fun fetch() {
            println("$name 捡东西")
        }
    }
    
    class Cat(name: String) : Animal(name) {
        override fun makeSound() {
            println("$name 喵喵叫")
        }
    }
    
    val dog = Dog("旺财")
    val cat = Cat("咪咪")
    
    dog.makeSound()
    dog.eat()
    dog.fetch()
    
    cat.makeSound()
    cat.eat()
    println()
    
    // 5. 接口
    println("--- 5. 接口 ---")
    
    interface Shape {
        fun area(): Double
        fun perimeter(): Double
        
        fun description() {
            println("这是一个图形")
        }
    }
    
    class Circle(val radius: Double) : Shape {
        override fun area(): Double {
            return Math.PI * radius * radius
        }
        
        override fun perimeter(): Double {
            return 2 * Math.PI * radius
        }
    }
    
    class Square(val side: Double) : Shape {
        override fun area(): Double {
            return side * side
        }
        
        override fun perimeter(): Double {
            return 4 * side
        }
    }
    
    val circle = Circle(5.0)
    val square = Square(4.0)
    
    println("Circle - area: ${circle.area()}, perimeter: ${circle.perimeter()}")
    println("Square - area: ${square.area()}, perimeter: ${square.perimeter()}")
    
    circle.description()
    square.description()
    println()
    
    // 6. 抽象类
    println("--- 6. 抽象类 ---")
    
    abstract class Vehicle(val brand: String) {
        abstract fun start()
        abstract fun stop()
        
        fun honk() {
            println("$brand 鸣笛")
        }
    }
    
    class Car(brand: String) : Vehicle(brand) {
        override fun start() {
            println("$brand 汽车启动")
        }
        
        override fun stop() {
            println("$brand 汽车停止")
        }
    }
    
    class Bike(brand: String) : Vehicle(brand) {
        override fun start() {
            println("$brand 自行车启动")
        }
        
        override fun stop() {
            println("$brand 自行车停止")
        }
    }
    
    val car = Car("特斯拉")
    val bike = Bike("捷安特")
    
    car.start()
    car.honk()
    car.stop()
    
    bike.start()
    bike.stop()
    println()
    
    // 7. 枚举类
    println("--- 7. 枚举类 ---")
    
    enum class Day {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }
    
    enum class Color(val rgb: Int) {
        RED(0xFF0000),
        GREEN(0x00FF00),
        BLUE(0x0000FF);
        
        fun getHex(): String {
            return "#${rgb.toString(16).uppercase()}"
        }
    }
    
    val today = Day.FRIDAY
    println("Today: $today")
    
    val color = Color.BLUE
    println("Color: $color, RGB: ${color.rgb}, Hex: ${color.getHex()}")
    
    // 遍历枚举
    println("所有颜色:")
    for (c in Color.values()) {
        println("  ${c.name}: ${c.getHex()}")
    }
    println()
    
    // 8. 密封类
    println("--- 8. 密封类 ---")
    
    sealed class Result
    data class Success(val data: String) : Result()
    data class Error(val message: String) : Result()
    object Loading : Result()
    
    fun handleResult(result: Result) {
        when (result) {
            is Success -> println("成功: ${result.data}")
            is Error -> println("错误: ${result.message}")
            Loading -> println("加载中...")
        }
    }
    
    handleResult(Success("数据加载完成"))
    handleResult(Error("网络连接失败"))
    handleResult(Loading)
    println()
    
    println("🎉 Kotlin面向对象学习完成！")
    println("💡 数据类、单例、密封类是Kotlin的特色！")
}
