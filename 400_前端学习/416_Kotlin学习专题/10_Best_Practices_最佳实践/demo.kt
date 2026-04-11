// Kotlin最佳实践示例代码

fun main() {
    println("=== Kotlin最佳实践 ===")
    println()
    
    // 1. 命名规范
    println("--- 1. 命名规范 ---")
    
    val namingConventions = """
        // ✅ 好的命名
        class UserService
        class OrderRepository
        class ApiClient
        
        fun calculateTotalPrice(): Double
        fun getUserById(id: Long): User?
        fun isValidEmail(email: String): Boolean
        
        val maxRetryCount = 3
        val defaultTimeout = 5000
        val isNetworkAvailable: Boolean
        
        // ❌ 不好的命名
        class usrSvc
        class ord_repo
        class APICLIENT
        
        fun calc(): Double
        fun getu(id: Long): User?
        fun checkemail(email: String): Boolean
        
        val mrc = 3
        val to = 5000
        val net: Boolean
        
        // 常量命名
        const val MAX_RETRY_COUNT = 3
        const val DEFAULT_TIMEOUT = 5000
        const val API_BASE_URL = "https://api.example.com"
        
        // 包名
        package com.example.project.service
        package com.example.project.repository
        package com.example.project.util
        
        // 私有属性
        class UserManager {
            private val users = mutableListOf<User>()
            private var currentUser: User? = null
            
            fun addUser(user: User) {
                users.add(user)
            }
        }
    """.trimIndent()
    
    println(namingConventions)
    println()
    
    // 2. 空安全最佳实践
    println("--- 2. 空安全最佳实践 ---")
    
    val nullSafety = """
        // ✅ 优先使用非空类型
        class User(
            val id: Long,
            val name: String,
            val email: String
        )
        
        // ✅ 只在确实需要时使用可空类型
        class UserProfile(
            val user: User,
            val avatarUrl: String?,
            val bio: String?
        )
        
        // ✅ 使用 ?. 和 ?: 安全处理
        fun getAvatarUrl(profile: UserProfile?): String {
            return profile?.avatarUrl ?: DEFAULT_AVATAR
        }
        
        // ✅ 使用 let 处理可空值
        fun processUser(user: User?) {
            user?.let {
                // 这里 user 是非空的
                println("Processing user: ${it.name}")
                sendNotification(it)
            } ?: run {
                println("User is null")
            }
        }
        
        // ✅ 使用 require 或 check 进行参数校验
        fun createUser(name: String, email: String): User {
            require(name.isNotBlank()) { "Name cannot be blank" }
            require(email.isNotBlank()) { "Email cannot be blank" }
            require(email.contains("@")) { "Invalid email format" }
            
            return User(1, name, email)
        }
        
        // ❌ 避免过度使用 !!
        fun badPractice(user: User?) {
            // 可能抛出 NullPointerException
            val name = user!!.name
        }
        
        // ✅ 更好的做法
        fun goodPractice(user: User?) {
            val name = user?.name ?: return
            println(name)
        }
        
        // ✅ 使用 early return
        fun validateUser(user: User?): Boolean {
            user ?: return false
            if (user.name.isBlank()) return false
            if (user.email.isBlank()) return false
            return true
        }
    """.trimIndent()
    
    println(nullSafety)
    println()
    
    // 3. 函数设计最佳实践
    println("--- 3. 函数设计最佳实践 ---")
    
    val functionDesign = """
        // ✅ 函数应该短小精悍，单一职责
        fun calculateTotalPrice(
            items: List<Item>,
            discount: Discount?
        ): Double {
            val subtotal = calculateSubtotal(items)
            val discountAmount = calculateDiscount(subtotal, discount)
            val tax = calculateTax(subtotal - discountAmount)
            return subtotal - discountAmount + tax
        }
        
        private fun calculateSubtotal(items: List<Item>): Double {
            return items.sumOf { it.price * it.quantity }
        }
        
        private fun calculateDiscount(
            subtotal: Double,
            discount: Discount?
        ): Double {
            return discount?.let {
                when (it.type) {
                    Discount.Type.PERCENTAGE -> subtotal * it.value / 100
                    Discount.Type.FIXED -> it.value
                }
            } ?: 0.0
        }
        
        private fun calculateTax(amount: Double): Double {
            return amount * TAX_RATE
        }
        
        // ✅ 使用默认参数
        fun createUser(
            name: String,
            email: String,
            age: Int? = null,
            role: Role = Role.USER
        ): User {
            return User(
                id = generateId(),
                name = name,
                email = email,
                age = age,
                role = role
            )
        }
        
        // 使用
        val user1 = createUser("张三", "zhangsan@example.com")
        val user2 = createUser("李四", "lisi@example.com", age = 20)
        val user3 = createUser("王五", "wangwu@example.com", role = Role.ADMIN)
        
        // ✅ 使用命名参数提高可读性
        val user = createUser(
            name = "张三",
            email = "zhangsan@example.com",
            age = 18,
            role = Role.USER
        )
        
        // ✅ 使用扩展函数
        fun String.isValidEmail(): Boolean {
            return matches(EMAIL_REGEX.toRegex())
        }
        
        fun String.capitalizeFirst(): String {
            return if (isNotEmpty()) {
                substring(0, 1).uppercase() + substring(1).lowercase()
            } else {
                this
            }
        }
        
        // 使用
        val email = "test@example.com"
        if (email.isValidEmail()) {
            println("有效邮箱")
        }
        
        val name = "john doe"
        println(name.capitalizeFirst()) // John Doe
        
        // ✅ 顶层函数 vs 成员函数
        // 工具函数使用顶层函数
        fun formatDate(date: LocalDate): String {
            return date.format(DateTimeFormatter.ISO_LOCAL_DATE)
        }
        
        // 与类紧密相关的使用成员函数
        class User {
            fun getFullName(): String {
                return "$firstName $lastName"
            }
        }
    """.trimIndent()
    
    println(functionDesign)
    println()
    
    // 4. 类设计最佳实践
    println("--- 4. 类设计最佳实践 ---")
    
    val classDesign = """
        // ✅ 优先使用 data class 用于数据承载
        data class User(
            val id: Long,
            val name: String,
            val email: String,
            val age: Int? = null,
            val createdAt: LocalDateTime = LocalDateTime.now()
        )
        
        // ✅ 使用密封类表示受限的类层次结构
        sealed class Result<out T> {
            data class Success<out T>(val data: T) : Result<T>()
            data class Error(val message: String) : Result<Nothing>()
            object Loading : Result<Nothing>()
        }
        
        // 使用
        fun processResult(result: Result<User>) {
            when (result) {
                is Result.Success -> println("成功: ${result.data}")
                is Result.Error -> println("失败: ${result.message}")
                Result.Loading -> println("加载中...")
            }
        }
        
        // ✅ 使用 object 实现单例
        object DatabaseConfig {
            const val URL = "jdbc:mysql://localhost:3306/db"
            const val USERNAME = "root"
            const val PASSWORD = "password"
        }
        
        // ✅ 使用伴生对象
        class User private constructor(
            val id: Long,
            val name: String
        ) {
            companion object {
                fun create(name: String): User {
                    return User(generateId(), name)
                }
                
                private fun generateId(): Long {
                    return System.currentTimeMillis()
                }
            }
        }
        
        // ✅ 优先使用不可变性
        // ✅ val 而不是 var
        data class Order(
            val id: Long,
            val items: List<OrderItem>,
            val status: OrderStatus
        ) {
            // 返回新的实例而不是修改
            fun updateStatus(newStatus: OrderStatus): Order {
                return copy(status = newStatus)
            }
            
            fun addItem(item: OrderItem): Order {
                return copy(items = items + item)
            }
        }
        
        // ✅ 使用接口定义契约
        interface Repository<T, ID> {
            fun findById(id: ID): T?
            fun findAll(): List<T>
            fun save(entity: T): T
            fun deleteById(id: ID)
        }
        
        class UserRepository : Repository<User, Long> {
            override fun findById(id: Long): User? { /* ... */ }
            override fun findAll(): List<User> { /* ... */ }
            override fun save(entity: User): User { /* ... */ }
            override fun deleteById(id: Long) { /* ... */ }
        }
    """.trimIndent()
    
    println(classDesign)
    println()
    
    // 5. 集合操作最佳实践
    println("--- 5. 集合操作最佳实践 ---")
    
    val collectionBestPractices = """
        // ✅ 使用不可变集合
        val users = listOf(user1, user2, user3)
        val products = setOf(product1, product2)
        val userMap = mapOf(1 to user1, 2 to user2)
        
        // ✅ 需要修改时使用可变集合
        val mutableUsers = users.toMutableList()
        mutableUsers.add(user4)
        
        // ✅ 使用序列处理大数据集
        // ❌ List - 中间结果都会创建新集合
        val resultList = users
            .filter { it.age > 18 }
            .map { it.name }
            .take(10)
        
        // ✅ Sequence - 惰性求值
        val resultSequence = users.asSequence()
            .filter { it.age > 18 }
            .map { it.name }
            .take(10)
            .toList()
        
        // ✅ 使用合适的集合函数
        val adults = users.filter { it.age >= 18 }
        val names = users.map { it.name }
        val totalAge = users.sumOf { it.age ?: 0 }
        val firstAdult = users.find { it.age >= 18 }
        val allAdults = users.all { it.age >= 18 }
        val anyAdult = users.any { it.age >= 18 }
        val groupedByAge = users.groupBy { it.age ?: 0 }
        
        // ✅ 避免嵌套集合操作
        // ❌ 性能差
        val ordersWithUser = orders.map { order ->
            val user = users.find { it.id == order.userId }
            order to user
        }
        
        // ✅ 先创建索引
        val userById = users.associateBy { it.id }
        val ordersWithUser2 = orders.map { order ->
            order to userById[order.userId]
        }
        
        // ✅ 使用 withIndex 获取索引
        users.withIndex().forEach { (index, user) ->
            println("$index: ${user.name}")
        }
        
        // ✅ 使用 partition 分割集合
        val (adults, minors) = users.partition { it.age >= 18 }
        
        // ✅ 使用 zip 配对两个集合
        val names = listOf("张三", "李四", "王五")
        val emails = listOf("a@a.com", "b@b.com", "c@c.com")
        val users = names.zip(emails) { name, email ->
            User(name, email)
        }
    """.trimIndent()
    
    println(collectionBestPractices)
    println()
    
    // 6. 协程最佳实践
    println("--- 6. 协程最佳实践 ---")
    
    val coroutinesBestPractices = """
        // ✅ 使用合适的作用域
        class MyViewModel : ViewModel() {
            // ViewModel 使用 viewModelScope
            fun loadData() {
                viewModelScope.launch {
                    // 会在 ViewModel 销毁时自动取消
                }
            }
        }
        
        class MyFragment : Fragment() {
            // Lifecycle 使用 lifecycleScope
            override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
                viewLifecycleOwner.lifecycleScope.launch {
                    repeatOnLifecycle(Lifecycle.State.STARTED) {
                        // 只会在 STARTED 状态时执行
                    }
                }
            }
        }
        
        // ✅ 使用合适的调度器
        suspend fun loadData() {
            // 默认在 Dispatchers.Default
            val result = withContext(Dispatchers.IO) {
                // IO 操作
            }
            withContext(Dispatchers.Main) {
                // 更新 UI
            }
        }
        
        // ✅ 使用 async 并发执行
        suspend fun fetchMultipleData() {
            val userDeferred = async { fetchUser() }
            val productsDeferred = async { fetchProducts() }
            
            val user = userDeferred.await()
            val products = productsDeferred.await()
        }
        
        // ✅ 正确处理取消
        suspend fun doWork() {
            try {
                while (isActive) {
                    // 检查是否被取消
                    doSomeWork()
                    yield() // 让出执行权
                }
            } catch (e: CancellationException) {
                // 清理资源
                cleanup()
                throw e // 重新抛出
            }
        }
        
        // ✅ 使用 coroutineScope 结构化并发
        suspend fun parentTask() = coroutineScope {
            launch { childTask1() }
            launch { childTask2() }
            // 等待所有子协程完成
        }
        
        // ✅ 使用 supervisorScope 避免一个失败影响全部
        suspend fun loadAllData() = supervisorScope {
            val userDeferred = async { fetchUser() }
            val productsDeferred = async { fetchProducts() }
            
            try {
                val user = userDeferred.await()
            } catch (e: Exception) {
                println("获取用户失败")
            }
            
            try {
                val products = productsDeferred.await()
            } catch (e: Exception) {
                println("获取产品失败")
            }
        }
        
        // ✅ 使用 Flow 处理数据流
        fun getUpdates(): Flow<Update> = callbackFlow {
            val listener = object : UpdateListener {
                override fun onUpdate(update: Update) {
                    trySend(update)
                }
            }
            api.registerListener(listener)
            awaitClose {
                api.unregisterListener(listener)
            }
        }
        
        // ✅ Flow 操作符
        updates
            .filter { it.isImportant() }
            .map { it.transform() }
            .debounce(300)
            .distinctUntilChanged()
            .catch { e -> emit(ErrorUpdate(e)) }
            .collect { update -> handleUpdate(update) }
    """.trimIndent()
    
    println(coroutinesBestPractices)
    println()
    
    // 7. 错误处理最佳实践
    println("--- 7. 错误处理最佳实践 ---")
    
    val errorHandling = """
        // ✅ 使用 Result 类型
        sealed class Result<out T> {
            data class Success<out T>(val data: T) : Result<T>()
            data class Failure(val error: Throwable) : Result<Nothing>()
        }
        
        suspend fun fetchUser(id: Long): Result<User> {
            return try {
                val user = api.getUser(id)
                Result.Success(user)
            } catch (e: Exception) {
                Result.Failure(e)
            }
        }
        
        // 使用
        when (val result = fetchUser(1)) {
            is Result.Success -> showUser(result.data)
            is Result.Failure -> showError(result.error)
        }
        
        // ✅ 使用 runCatching
        fun parseNumber(str: String): Int? {
            return runCatching {
                str.toInt()
            }.getOrNull()
        }
        
        val number = runCatching {
            str.toInt()
        }.fold(
            onSuccess = { it },
            onFailure = { 0 }
        )
        
        // ✅ 自定义异常
        class UserNotFoundException(userId: Long) :
            RuntimeException("User not found: $userId")
        
        class InvalidEmailException(email: String) :
            RuntimeException("Invalid email: $email")
        
        // ✅ 使用 require/check/assert
        fun createUser(name: String, email: String): User {
            require(name.isNotBlank()) {
                "Name cannot be blank"
            }
            require(email.isValidEmail()) {
                "Invalid email: $email"
            }
            
            val user = User(name, email)
            check(user.id > 0) {
                "Invalid user ID"
            }
            
            return user
        }
        
        // ✅ 不要捕获太宽泛的异常
        // ❌
        try {
            doSomething()
        } catch (e: Exception) {
            // 隐藏所有异常
        }
        
        // ✅
        try {
            doSomething()
        } catch (e: IOException) {
            handleIOException(e)
        } catch (e: SQLException) {
            handleSQLException(e)
        }
        
        // ✅ 记录异常
        try {
            doSomething()
        } catch (e: Exception) {
            logger.error("Operation failed", e)
            throw e
        }
        
        // ✅ 使用 Either 类型（Arrow库）
        fun fetchUserEither(id: Long): Either<Error, User> {
            return try {
                val user = api.getUser(id)
                user.right()
            } catch (e: Exception) {
                Error(e.message).left()
            }
        }
        
        fetchUserEither(1).fold(
            ifLeft = { error -> showError(error) },
            ifRight = { user -> showUser(user) }
        )
    """.trimIndent()
    
    println(errorHandling)
    println()
    
    // 8. 测试最佳实践
    println("--- 8. 测试最佳实践 ---")
    
    val testingBestPractices = """
        // ✅ 测试命名应该描述行为
        class UserServiceTest {
            
            @Test
            fun `getUserById should return user when exists`() { }
            
            @Test
            fun `getUserById should throw when not exists`() { }
            
            @Test
            fun `createUser should save user with valid data`() { }
            
            @Test
            fun `createUser should fail when email is duplicate`() { }
        }
        
        // ✅ 使用 Given-When-Then 结构
        @Test
        fun `calculateTotal should return correct sum`() {
            // Given
            val items = listOf(
                Item(price = 10.0, quantity = 2),
                Item(price = 20.0, quantity = 1)
            )
            
            // When
            val total = calculateTotal(items)
            
            // Then
            assertThat(total).isEqualTo(40.0)
        }
        
        // ✅ 使用数据驱动测试
        @ParameterizedTest
        @CsvSource(
            "10, 20, 30",
            "0, 0, 0",
            "-5, 10, 5"
        )
        fun `add should return correct sum`(a: Int, b: Int, expected: Int) {
            assertThat(add(a, b)).isEqualTo(expected)
        }
        
        // ✅ 使用 Mock
        class UserServiceTest {
            
            @Mock
            private lateinit var userRepository: UserRepository
            
            @InjectMocks
            private lateinit var userService: UserService
            
            @Test
            fun `getUser should call repository`() {
                // Given
                val user = User(1, "张三")
                given(userRepository.findById(1)).willReturn(user)
                
                // When
                val result = userService.getUser(1)
                
                // Then
                assertThat(result).isEqualTo(user)
                verify(userRepository).findById(1)
            }
        }
        
        // ✅ 测试行为而不是实现
        // ❌ 测试实现细节
        @Test
        fun `bad test`() {
            service.doSomething()
            verify(service).internalMethod() // 依赖内部实现
        }
        
        // ✅ 测试行为
        @Test
        fun `good test`() {
            val result = service.doSomething()
            assertThat(result).isCorrect()
        }
        
        // ✅ 保持测试独立
        @BeforeEach
        fun setup() {
            userRepository.deleteAll()
        }
        
        @Test
        fun test1() { }
        
        @Test
        fun test2() { } // 不依赖 test1
        
        // ✅ 使用断言库
        // AssertJ
        assertThat(user)
            .isNotNull()
            .hasFieldOrPropertyWithValue("name", "张三")
            .hasFieldOrPropertyWithValue("age", 18)
        
        assertThat(users)
            .hasSize(3)
            .extracting("name")
            .containsExactly("张三", "李四", "王五")
        
        // ✅ 测试异常
        @Test
        fun `should throw when user not found`() {
            given(userRepository.findById(1)).willReturn(null)
            
            assertThatThrownBy {
                userService.getUser(1)
            }.isInstanceOf(UserNotFoundException::class.java)
        }
        
        // ✅ 使用 JUnit 5 扩展
        @ExtendWith(MockKExtension::class)
        class UserServiceTest {
            
            @MockK
            private lateinit var userRepository: UserRepository
            
            @InjectMockKs
            private lateinit var userService: UserService
        }
    """.trimIndent()
    
    println(testingBestPractices)
    println()
    
    // 9. 性能优化最佳实践
    println("--- 9. 性能优化最佳实践 ---")
    
    val performanceBestPractices = """
        // ✅ 避免在循环中创建对象
        // ❌
        for (i in 1..1000) {
            val list = mutableListOf<Int>() // 每次都创建新对象
            list.add(i)
        }
        
        // ✅
        val list = mutableListOf<Int>()
        for (i in 1..1000) {
            list.add(i)
        }
        
        // ✅ 使用序列处理大数据
        // ❌
        val result = bigList
            .filter { it.active }
            .map { it.name }
            .take(10)
        
        // ✅
        val result = bigList.asSequence()
            .filter { it.active }
            .map { it.name }
            .take(10)
            .toList()
        
        // ✅ 使用 lazy 延迟初始化
        class UserManager {
            // 只在第一次访问时初始化
            private val heavyObject by lazy {
                HeavyObject() // 昂贵的初始化
            }
        }
        
        // ✅ 避免不必要的装箱
        // ❌
        fun sum(numbers: List<Int?>): Int {
            var total = 0
            for (num in numbers) {
                if (num != null) {
                    total += num
                }
            }
            return total
        }
        
        // ✅
        fun sum(numbers: List<Int>): Int {
            return numbers.sum()
        }
        
        // ✅ 使用 inline 函数
        inline fun measureTime(block: () -> Unit): Long {
            val start = System.currentTimeMillis()
            block()
            return System.currentTimeMillis() - start
        }
        
        // ✅ 使用 const 编译时常量
        class Constants {
            companion object {
                const val API_URL = "https://api.example.com"
                const val TIMEOUT = 5000
                const val MAX_RETRY = 3
            }
        }
        
        // ✅ 缓存频繁访问的数据
        class UserCache {
            private val cache = mutableMapOf<Long, User>()
            
            fun getUser(id: Long): User? {
                return cache[id] ?: run {
                    val user = database.getUser(id)
                    if (user != null) {
                        cache[id] = user
                    }
                    user
                }
            }
        }
        
        // ✅ 避免深拷贝
        // ❌
        val newList = oldList.map { it.copy() }
        
        // ✅
        val newList = oldList.toList() // 只在需要时才拷贝
        
        // ✅ 使用原始类型数组
        // ❌
        val intList = listOf(1, 2, 3) // 装箱
        
        // ✅
        val intArray = intArrayOf(1, 2, 3) // 原始类型
    """.trimIndent()
    
    println(performanceBestPractices)
    println()
    
    // 10. 安全最佳实践
    println("--- 10. 安全最佳实践 ---")
    
    val securityBestPractices = """
        // ✅ 不要在日志中记录敏感信息
        // ❌
        logger.info("User created: $user") // 可能包含密码
        
        // ✅
        logger.info("User created: ${user.id}")
        
        // ✅ 验证输入
        fun createUser(email: String, password: String) {
            require(email.matches(EMAIL_REGEX)) {
                "Invalid email format"
            }
            require(password.length >= 8) {
                "Password must be at least 8 characters"
            }
            require(password.contains(Regex("[A-Z]"))) {
                "Password must contain uppercase letter"
            }
        }
        
        // ✅ 使用安全的加密
        import javax.crypto.Cipher
        import javax.crypto.KeyGenerator
        import javax.crypto.SecretKey
        import javax.crypto.spec.GCMParameterSpec
        
        object EncryptionUtils {
            private const val ALGORITHM = "AES/GCM/NoPadding"
            private const val TAG_LENGTH = 128
            
            fun encrypt(data: ByteArray, key: SecretKey): ByteArray {
                val cipher = Cipher.getInstance(ALGORITHM)
                val iv = ByteArray(12)
                SecureRandom().nextBytes(iv)
                val spec = GCMParameterSpec(TAG_LENGTH, iv)
                cipher.init(Cipher.ENCRYPT_MODE, key, spec)
                val encrypted = cipher.doFinal(data)
                return iv + encrypted
            }
        }
        
        // ✅ 安全地处理密码
        import org.mindrot.jbcrypt.BCrypt
        
        object PasswordUtils {
            fun hashPassword(password: String): String {
                return BCrypt.hashpw(password, BCrypt.gensalt())
            }
            
            fun checkPassword(password: String, hashed: String): Boolean {
                return BCrypt.checkpw(password, hashed)
            }
        }
        
        // ✅ 不要硬编码密钥
        // ❌
        const val API_KEY = "secret123456" // 硬编码
        
        // ✅
        object Config {
            val apiKey: String by lazy {
                System.getenv("API_KEY") 
                    ?: throw IllegalStateException("API_KEY not set")
            }
        }
        
        // ✅ 使用 HTTPS
        // ❌
        val url = "http://api.example.com"
        
        // ✅
        val url = "https://api.example.com"
        
        // ✅ 验证 SSL 证书
        val okHttpClient = OkHttpClient.Builder()
            .certificatePinner(
                CertificatePinner.Builder()
                    .add("example.com", "sha256/abc123...")
                    .build()
            )
            .build()
        
        // ✅ 及时释放资源
        fun processFile(file: File) {
            file.inputStream().use { input ->
                input.readBytes()
            } // 自动关闭
        }
        
        // ✅ 防止 SQL 注入
        // ❌
        fun getUser(id: String): User? {
            val sql = "SELECT * FROM users WHERE id = $id" // 危险！
            return jdbcTemplate.queryForObject(sql, UserRowMapper())
        }
        
        // ✅
        fun getUser(id: Long): User? {
            val sql = "SELECT * FROM users WHERE id = ?"
            return jdbcTemplate.queryForObject(sql, UserRowMapper(), id)
        }
        
        // ✅ 使用 PreparedStatement
        fun getUser(id: Long): User? {
            return jdbcTemplate.queryForObject(
                "SELECT * FROM users WHERE id = ?",
                UserRowMapper(),
                id
            )
        }
    """.trimIndent()
    
    println(securityBestPractices)
    println()
    
    println("🎉🎉🎉 Kotlin最佳实践学习完成！")
    println("💡 遵循最佳实践能让你的代码更优雅、更健壮！")
}
