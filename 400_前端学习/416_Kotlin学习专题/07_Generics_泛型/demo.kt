// Kotlin泛型示例代码

fun main() {
    println("=== Kotlin泛型 ===")
    println()
    
    // 1. 泛型类
    println("--- 1. 泛型类 ---")
    
    class Box<T>(val item: T) {
        fun getItem(): T = item
        fun printItem() {
            println("Box contains: $item")
        }
    }
    
    val intBox = Box(100)
    val stringBox = Box("Hello Kotlin")
    
    intBox.printItem()
    stringBox.printItem()
    println("intBox.getItem(): ${intBox.getItem()}")
    println("stringBox.getItem(): ${stringBox.getItem()}")
    
    // 多个类型参数
    class Pair<K, V>(val key: K, val value: V) {
        override fun toString(): String {
            return "($key, $value)"
        }
    }
    
    val pair1 = Pair("name", "张三")
    val pair2 = Pair(1, "One")
    println("pair1: $pair1")
    println("pair2: $pair2")
    println()
    
    // 2. 泛型函数
    println("--- 2. 泛型函数 ---")
    
    fun <T> printItem(item: T) {
        println("Item: $item")
    }
    
    printItem(123)
    printItem("Hello")
    printItem(3.14)
    
    fun <T> createList(vararg items: T): List<T> {
        return items.toList()
    }
    
    val list1 = createList(1, 2, 3, 4, 5)
    val list2 = createList("A", "B", "C")
    println("list1: $list1")
    println("list2: $list2")
    
    // 带返回值的泛型函数
    fun <T> firstOrNull(list: List<T>): T? {
        return if (list.isNotEmpty()) list[0] else null
    }
    
    println("firstOrNull(list1): ${firstOrNull(list1)}")
    println("firstOrNull(emptyList()): ${firstOrNull(emptyList<Int>())}")
    println()
    
    // 3. 泛型约束
    println("--- 3. 泛型约束 ---")
    
    // 上界约束
    fun <T : Number> doubleValue(value: T): Double {
        return value.toDouble() * 2
    }
    
    println("doubleValue(5): ${doubleValue(5)}")
    println("doubleValue(3.14): ${doubleValue(3.14)}")
    
    // 可空上界约束
    fun <T : CharSequence?> printLength(value: T) {
        println("Length: ${value?.length ?: 0}")
    }
    
    printLength("Hello")
    printLength(null)
    
    // 多重约束
    interface Loggable {
        fun log(): String
    }
    
    interface Serializable {
        fun serialize(): String
    }
    
    fun <T> processItem(item: T) where T : Loggable, T : Serializable {
        println("Log: ${item.log()}")
        println("Serialized: ${item.serialize()}")
    }
    
    class Data(val id: Int, val name: String) : Loggable, Serializable {
        override fun log(): String = "Data(id=$id, name=$name)"
        override fun serialize(): String = "{\"id\":$id,\"name\":\"$name\"}"
    }
    
    val data = Data(1, "Test")
    processItem(data)
    println()
    
    // 4. 型变 - 协变(out)
    println("--- 4. 型变 - 协变(out) ---")
    
    interface Producer<out T> {
        fun produce(): T
    }
    
    class AnimalProducer : Producer<Animal> {
        override fun produce(): Animal = Animal()
    }
    
    class DogProducer : Producer<Dog> {
        override fun produce(): Dog = Dog()
    }
    
    open class Animal
    class Dog : Animal()
    
    fun useProducer(producer: Producer<Animal>) {
        val animal = producer.produce()
        println("Produced: $animal")
    }
    
    val animalProducer = AnimalProducer()
    val dogProducer = DogProducer()
    
    useProducer(animalProducer)
    useProducer(dogProducer)
    
    // 5. 型变 - 逆变(in)
    println("\n--- 5. 型变 - 逆变(in) ---")
    
    interface Consumer<in T> {
        fun consume(item: T)
    }
    
    class AnimalConsumer : Consumer<Animal> {
        override fun consume(item: Animal) {
            println("Consumed animal: $item")
        }
    }
    
    class DogConsumer : Consumer<Dog> {
        override fun consume(item: Dog) {
            println("Consumed dog: $item")
        }
    }
    
    fun feedDog(consumer: Consumer<Dog>) {
        consumer.consume(Dog())
    }
    
    val animalConsumer = AnimalConsumer()
    val dogConsumer2 = DogConsumer()
    
    feedDog(dogConsumer2)
    feedDog(animalConsumer)
    
    // 6. 使用点型变
    println("\n--- 6. 使用点型变 ---")
    
    class MutableBox<T>(var item: T)
    
    fun copyFrom(source: MutableBox<out Animal>, dest: MutableBox<in Dog>) {
        dest.item = source.item as Dog
    }
    
    val sourceBox = MutableBox(Dog())
    val destBox = MutableBox<Animal>(Animal())
    copyFrom(sourceBox, destBox)
    println("destBox.item: ${destBox.item}")
    
    // 7. 星投影
    println("\n--- 7. 星投影 ---")
    
    class SimpleBox<T>(val item: T) {
        fun getItem(): T = item
        override fun toString(): String = "SimpleBox($item)"
    }
    
    fun printBox(box: SimpleBox<*>) {
        println("Box: $box")
    }
    
    val intBox2 = SimpleBox(100)
    val stringBox2 = SimpleBox("Hello")
    printBox(intBox2)
    printBox(stringBox2)
    
    // List<*>
    fun printList(list: List<*>) {
        println("List size: ${list.size}")
        list.forEach { println("  Item: $it") }
    }
    
    val mixedList = listOf(1, "Hello", 3.14, true)
    printList(mixedList)
    println()
    
    // 8. 具体化类型参数(reified)
    println("--- 8. 具体化类型参数(reified) ---")
    
    inline fun <reified T> isOfType(value: Any): Boolean {
        return value is T
    }
    
    println("isOfType<String>(\"Hello\"): ${isOfType<String>("Hello")}")
    println("isOfType<Int>(123): ${isOfType<Int>(123)}")
    println("isOfType<Double>(123): ${isOfType<Double>(123)}")
    
    inline fun <reified T> filterByType(list: List<*>): List<T> {
        return list.filterIsInstance<T>()
    }
    
    val mixed = listOf(1, "A", 2, "B", 3, "C")
    val ints = filterByType<Int>(mixed)
    val strings = filterByType<String>(mixed)
    println("ints: $ints")
    println("strings: $strings")
    println()
    
    // 9. 泛型与数组
    println("--- 9. 泛型与数组 ---")
    
    // 创建泛型数组
    inline fun <reified T> createArray(size: Int, init: (Int) -> T): Array<T> {
        return Array(size, init)
    }
    
    val intArray = createArray(5) { it * 2 }
    val stringArray = createArray(3) { "Item $it" }
    println("intArray: ${intArray.contentToString()}")
    println("stringArray: ${stringArray.contentToString()}")
    
    // 10. 实际应用示例
    println("\n--- 10. 实际应用示例 ---")
    
    // 泛型栈
    class Stack<T> {
        private val items = mutableListOf<T>()
        
        fun push(item: T) = items.add(item)
        fun pop(): T? = if (items.isNotEmpty()) items.removeLast() else null
        fun peek(): T? = items.lastOrNull()
        fun isEmpty(): Boolean = items.isEmpty()
        fun size(): Int = items.size
        
        override fun toString(): String = items.toString()
    }
    
    val stack = Stack<String>()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    println("Stack: $stack")
    println("pop(): ${stack.pop()}")
    println("Stack: $stack")
    println("peek(): ${stack.peek()}")
    
    // 泛型Result
    sealed class Result<out T> {
        data class Success<out T>(val data: T) : Result<T>()
        data class Error(val message: String) : Result<Nothing>()
    }
    
    fun <T> processResult(result: Result<T>) {
        when (result) {
            is Result.Success -> println("成功: ${result.data}")
            is Result.Error -> println("失败: ${result.message}")
        }
    }
    
    val successResult = Result.Success("数据加载成功")
    val errorResult = Result.Error("网络连接失败")
    processResult(successResult)
    processResult(errorResult)
    println()
    
    println("🎉 Kotlin泛型学习完成！")
    println("💡 协变和逆变是Kotlin泛型的特色！")
}
