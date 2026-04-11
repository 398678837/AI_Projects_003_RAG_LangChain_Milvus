// Kotlin集合示例代码

fun main() {
    println("=== Kotlin集合 ===")
    println()
    
    // 1. List
    println("--- 1. List ---")
    
    // 不可变List
    val list1 = listOf(1, 2, 3, 4, 5)
    println("不可变List: $list1")
    println("list1[0]: ${list1[0]}")
    println("list1.size: ${list1.size}")
    
    // 可变List
    val mutableList = mutableListOf("A", "B", "C")
    mutableList.add("D")
    mutableList.add(0, "X")
    mutableList.remove("B")
    mutableList[1] = "Y"
    println("可变List: $mutableList")
    
    // List常用操作
    println("list1.first(): ${list1.first()}")
    println("list1.last(): ${list1.last()}")
    println("list1.indexOf(3): ${list1.indexOf(3)}")
    println("list1.contains(4): ${list1.contains(4)}")
    println("list1.take(3): ${list1.take(3)}")
    println("list1.drop(2): ${list1.drop(2)}")
    println()
    
    // 2. Set
    println("--- 2. Set ---")
    
    // 不可变Set
    val set1 = setOf(1, 2, 3, 2, 1)
    println("不可变Set: $set1")
    
    // 可变Set
    val mutableSet = mutableSetOf("苹果", "香蕉", "橙子")
    mutableSet.add("葡萄")
    mutableSet.add("苹果")
    mutableSet.remove("香蕉")
    println("可变Set: $mutableSet")
    
    // Set操作
    val set2 = setOf(3, 4, 5, 6)
    println("set1 union set2: ${set1 union set2}")
    println("set1 intersect set2: ${set1 intersect set2}")
    println("set1 subtract set2: ${set1 subtract set2}")
    println()
    
    // 3. Map
    println("--- 3. Map ---")
    
    // 不可变Map
    val map1 = mapOf(
        "name" to "张三",
        "age" to 18,
        "city" to "北京"
    )
    println("不可变Map: $map1")
    println("map1[\"name\"]: ${map1["name"]}")
    println("map1.keys: ${map1.keys}")
    println("map1.values: ${map1.values}")
    
    // 可变Map
    val mutableMap = mutableMapOf<String, Int>()
    mutableMap["a"] = 1
    mutableMap["b"] = 2
    mutableMap["c"] = 3
    mutableMap["b"] = 20
    mutableMap.remove("c")
    println("可变Map: $mutableMap")
    
    // 遍历Map
    println("遍历Map:")
    for ((key, value) in map1) {
        println("  $key -> $value")
    }
    println()
    
    // 4. 集合操作
    println("--- 4. 集合操作 ---")
    
    val numbers = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    // filter - 过滤
    val evens = numbers.filter { it % 2 == 0 }
    println("filter(偶数): $evens")
    
    val greaterThan5 = numbers.filter { it > 5 }
    println("filter(>5): $greaterThan5")
    
    // map - 映射
    val doubled = numbers.map { it * 2 }
    println("map(*2): $doubled")
    
    val strings = numbers.map { "Number: $it" }
    println("map(字符串): $strings")
    
    // flatMap - 扁平化映射
    val nestedList = listOf(listOf(1, 2), listOf(3, 4), listOf(5, 6))
    val flattened = nestedList.flatMap { it }
    println("flatMap: $flattened")
    
    // reduce - 归约
    val sum = numbers.reduce { acc, num -> acc + num }
    println("reduce(sum): $sum")
    
    val product = numbers.reduce { acc, num -> acc * num }
    println("reduce(product): $product")
    
    // fold - 带初始值的归约
    val sumWithInit = numbers.fold(100) { acc, num -> acc + num }
    println("fold(100 + sum): $sumWithInit")
    
    // forEach - 遍历
    println("forEach:")
    numbers.take(3).forEach { print("$it ") }
    println()
    
    // groupBy - 分组
    val grouped = numbers.groupBy { if (it % 2 == 0) "偶数" else "奇数" }
    println("groupBy: $grouped")
    
    // sorted - 排序
    val unsorted = listOf(5, 2, 8, 1, 9, 3)
    val sorted = unsorted.sorted()
    val sortedDesc = unsorted.sortedDescending()
    println("sorted: $sorted")
    println("sortedDesc: $sortedDesc")
    
    // distinct - 去重
    val duplicates = listOf(1, 2, 2, 3, 3, 3, 4)
    val distinct = duplicates.distinct()
    println("distinct: $distinct")
    
    // any/all/none - 检查
    println("any(>5): ${numbers.any { it > 5 }}")
    println("all(<20): ${numbers.all { it < 20 }}")
    println("none(>10): ${numbers.none { it > 10 }}")
    
    // firstOrNull/find - 查找
    val firstEven = numbers.find { it % 2 == 0 }
    val firstGreaterThan10 = numbers.firstOrNull { it > 10 }
    println("find(偶数): $firstEven")
    println("firstOrNull(>10): $firstGreaterThan10")
    println()
    
    // 5. 序列(Sequence)
    println("--- 5. 序列(Sequence) ---")
    
    // List操作（立即执行）
    println("List操作（立即执行）:")
    val listResult = numbers
        .filter {
            println("  filter: $it")
            it % 2 == 0
        }
        .map {
            println("  map: $it")
            it * 2
        }
        .first()
    println("  结果: $listResult")
    
    // Sequence操作（惰性执行）
    println("Sequence操作（惰性执行）:")
    val seqResult = numbers.asSequence()
        .filter {
            println("  filter: $it")
            it % 2 == 0
        }
        .map {
            println("  map: $it")
            it * 2
        }
        .first()
    println("  结果: $seqResult")
    
    // 生成序列
    println("生成序列:")
    val seq1 = generateSequence(1) { it + 2 }
        .take(5)
        .toList()
    println("  奇数序列: $seq1")
    
    val seq2 = sequence {
        yield(1)
        yield(2)
        yieldAll(listOf(3, 4, 5))
    }.toList()
    println("  sequence: $seq2")
    println()
    
    // 6. 数组和集合转换
    println("--- 6. 数组和集合转换 ---")
    
    // Array转List
    val array = arrayOf(1, 2, 3)
    val listFromArray = array.toList()
    println("Array转List: $listFromArray")
    
    // List转Array
    val list = listOf(4, 5, 6)
    val arrayFromList = list.toTypedArray()
    println("List转Array: ${arrayFromList.contentToString()}")
    
    // List转Set
    val list2 = listOf(1, 2, 2, 3)
    val setFromList = list2.toSet()
    println("List转Set: $setFromList")
    
    // Pair列表转Map
    val pairs = listOf("a" to 1, "b" to 2, "c" to 3)
    val mapFromPairs = pairs.toMap()
    println("Pair列表转Map: $mapFromPairs")
    println()
    
    println("🎉 Kotlin集合学习完成！")
    println("💡 Kotlin集合操作函数非常强大！")
}
