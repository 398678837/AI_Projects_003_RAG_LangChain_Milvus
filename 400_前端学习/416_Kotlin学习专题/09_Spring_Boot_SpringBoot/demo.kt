// Kotlin Spring Boot示例代码

fun main() {
    println("=== Kotlin Spring Boot ===")
    println()
    
    // 1. Spring Boot基础
    println("--- 1. Spring Boot基础 ---")
    
    val springBootCode = """
        // 1. 主应用类
        @SpringBootApplication
        class DemoApplication
        
        fun main(args: Array<String>) {
            runApplication<DemoApplication>(*args)
        }
        
        // 2. application.properties
        server.port=8080
        spring.application.name=demo-app
        
        # 数据库配置
        spring.datasource.url=jdbc:mysql://localhost:3306/demo
        spring.datasource.username=root
        spring.datasource.password=password
        spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
        
        # JPA配置
        spring.jpa.hibernate.ddl-auto=update
        spring.jpa.show-sql=true
        spring.jpa.properties.hibernate.format_sql=true
        
        # application.yml
        server:
          port: 8080
        
        spring:
          application:
            name: demo-app
          datasource:
            url: jdbc:mysql://localhost:3306/demo
            username: root
            password: password
            driver-class-name: com.mysql.cj.jdbc.Driver
          jpa:
            hibernate:
              ddl-auto: update
            show-sql: true
            properties:
              hibernate:
                format_sql: true
        
        // 3. build.gradle.kts
        plugins {
            id("org.springframework.boot") version "3.2.0"
            id("io.spring.dependency-management") version "1.1.4"
            kotlin("jvm") version "1.9.20"
            kotlin("plugin.spring") version "1.9.20"
            kotlin("plugin.jpa") version "1.9.20"
        }
        
        group = "com.example"
        version = "0.0.1-SNAPSHOT"
        
        java {
            sourceCompatibility = JavaVersion.VERSION_17
        }
        
        repositories {
            mavenCentral()
        }
        
        dependencies {
            implementation("org.springframework.boot:spring-boot-starter-web")
            implementation("org.springframework.boot:spring-boot-starter-data-jpa")
            implementation("com.fasterxml.jackson.module:jackson-module-kotlin")
            implementation("org.jetbrains.kotlin:kotlin-reflect")
            runtimeOnly("com.mysql:mysql-connector-j")
            testImplementation("org.springframework.boot:spring-boot-starter-test")
        }
        
        tasks.withType<Test> {
            useJUnitPlatform()
        }
    """.trimIndent()
    
    println(springBootCode)
    println()
    
    // 2. Controller
    println("--- 2. Controller ---")
    
    val controllerCode = """
        // 简单的Controller
        @RestController
        @RequestMapping("/api")
        class HelloController {
            
            @GetMapping("/hello")
            fun hello(): String {
                return "Hello, Spring Boot with Kotlin!"
            }
            
            @GetMapping("/greet/{name}")
            fun greet(@PathVariable name: String): String {
                return "Hello, $name!"
            }
            
            @GetMapping("/add")
            fun add(
                @RequestParam a: Int,
                @RequestParam b: Int
            ): Int {
                return a + b
            }
        }
        
        // 返回JSON
        data class User(
            val id: Long,
            val name: String,
            val email: String,
            val age: Int
        )
        
        @RestController
        @RequestMapping("/api/users")
        class UserController {
            
            private val users = mutableListOf(
                User(1, "张三", "zhangsan@example.com", 18),
                User(2, "李四", "lisi@example.com", 20)
            )
            
            @GetMapping
            fun getAllUsers(): List<User> {
                return users
            }
            
            @GetMapping("/{id}")
            fun getUserById(@PathVariable id: Long): ResponseEntity<User> {
                val user = users.find { it.id == id }
                return if (user != null) {
                    ResponseEntity.ok(user)
                } else {
                    ResponseEntity.notFound().build()
                }
            }
            
            @PostMapping
            fun createUser(@RequestBody user: User): ResponseEntity<User> {
                val newUser = user.copy(id = users.size.toLong() + 1)
                users.add(newUser)
                return ResponseEntity.status(HttpStatus.CREATED).body(newUser)
            }
            
            @PutMapping("/{id}")
            fun updateUser(
                @PathVariable id: Long,
                @RequestBody updatedUser: User
            ): ResponseEntity<User> {
                val index = users.indexOfFirst { it.id == id }
                return if (index != -1) {
                    users[index] = updatedUser.copy(id = id)
                    ResponseEntity.ok(users[index])
                } else {
                    ResponseEntity.notFound().build()
                }
            }
            
            @DeleteMapping("/{id}")
            fun deleteUser(@PathVariable id: Long): ResponseEntity<Void> {
                val removed = users.removeIf { it.id == id }
                return if (removed) {
                    ResponseEntity.noContent().build()
                } else {
                    ResponseEntity.notFound().build()
                }
            }
        }
    """.trimIndent()
    
    println(controllerCode)
    println()
    
    // 3. Spring Data JPA
    println("--- 3. Spring Data JPA ---")
    
    val jpaCode = """
        // Entity
        @Entity
        @Table(name = "users")
        class User(
            @Id
            @GeneratedValue(strategy = GenerationType.IDENTITY)
            val id: Long? = null,
            
            @Column(nullable = false)
            val name: String,
            
            @Column(nullable = false, unique = true)
            val email: String,
            
            val age: Int? = null,
            
            @Column(name = "created_at")
            val createdAt: LocalDateTime = LocalDateTime.now()
        )
        
        // Repository
        interface UserRepository : JpaRepository<User, Long> {
            
            // 按名称查询
            fun findByName(name: String): List<User>
            
            // 按邮箱查询
            fun findByEmail(email: String): User?
            
            // 按年龄范围查询
            fun findByAgeBetween(minAge: Int, maxAge: Int): List<User>
            
            // 按名称模糊查询
            fun findByNameContaining(name: String): List<User>
            
            // 自定义查询
            @Query("SELECT u FROM User u WHERE u.age > :minAge ORDER BY u.name ASC")
            fun findUsersOlderThan(@Param("minAge") minAge: Int): List<User>
            
            // 计数查询
            fun countByAgeGreaterThan(age: Int): Long
            
            // 删除查询
            fun deleteByEmail(email: String)
        }
        
        // Service
        @Service
        class UserService(
            private val userRepository: UserRepository
        ) {
            
            fun getAllUsers(): List<User> {
                return userRepository.findAll()
            }
            
            fun getUserById(id: Long): User? {
                return userRepository.findById(id).orElse(null)
            }
            
            fun createUser(user: User): User {
                return userRepository.save(user)
            }
            
            fun updateUser(id: Long, user: User): User? {
                if (!userRepository.existsById(id)) {
                    return null
                }
                return userRepository.save(user.copy(id = id))
            }
            
            fun deleteUser(id: Long): Boolean {
                if (!userRepository.existsById(id)) {
                    return false
                }
                userRepository.deleteById(id)
                return true
            }
            
            fun getUsersByName(name: String): List<User> {
                return userRepository.findByName(name)
            }
            
            fun getUserByEmail(email: String): User? {
                return userRepository.findByEmail(email)
            }
        }
        
        // Controller with Service
        @RestController
        @RequestMapping("/api/users")
        class UserController(
            private val userService: UserService
        ) {
            
            @GetMapping
            fun getAllUsers(): ResponseEntity<List<User>> {
                return ResponseEntity.ok(userService.getAllUsers())
            }
            
            @GetMapping("/{id}")
            fun getUserById(@PathVariable id: Long): ResponseEntity<User> {
                val user = userService.getUserById(id)
                return if (user != null) {
                    ResponseEntity.ok(user)
                } else {
                    ResponseEntity.notFound().build()
                }
            }
            
            @PostMapping
            fun createUser(@RequestBody user: User): ResponseEntity<User> {
                val createdUser = userService.createUser(user)
                return ResponseEntity.status(HttpStatus.CREATED).body(createdUser)
            }
            
            @PutMapping("/{id}")
            fun updateUser(
                @PathVariable id: Long,
                @RequestBody user: User
            ): ResponseEntity<User> {
                val updatedUser = userService.updateUser(id, user)
                return if (updatedUser != null) {
                    ResponseEntity.ok(updatedUser)
                } else {
                    ResponseEntity.notFound().build()
                }
            }
            
            @DeleteMapping("/{id}")
            fun deleteUser(@PathVariable id: Long): ResponseEntity<Void> {
                val deleted = userService.deleteUser(id)
                return if (deleted) {
                    ResponseEntity.noContent().build()
                } else {
                    ResponseEntity.notFound().build()
                }
            }
        }
    """.trimIndent()
    
    println(jpaCode)
    println()
    
    // 4. 依赖注入和配置
    println("--- 4. 依赖注入和配置 ---")
    
    val diConfigCode = """
        // Configuration
        @Configuration
        class AppConfig {
            
            @Bean
            fun dateFormatter(): DateTimeFormatter {
                return DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
            }
            
            @Bean
            fun restTemplate(): RestTemplate {
                return RestTemplate()
            }
        }
        
        // 配置属性类
        @ConfigurationProperties(prefix = "app")
        data class AppProperties(
            val name: String = "demo-app",
            val version: String = "1.0.0",
            val api: ApiConfig = ApiConfig()
        ) {
            data class ApiConfig(
                val url: String = "https://api.example.com",
                val timeout: Int = 5000,
                val key: String = ""
            )
        }
        
        @EnableConfigurationProperties(AppProperties::class)
        @SpringBootApplication
        class DemoApplication
        
        // 使用配置属性
        @Service
        class ApiService(
            private val appProperties: AppProperties
        ) {
            
            fun callApi(): String {
                val url = appProperties.api.url
                val timeout = appProperties.api.timeout
                return "Calling API at $url with timeout $timeout ms"
            }
        }
        
        // 构造函数注入
        @Service
        class UserService(
            private val userRepository: UserRepository,
            private val emailService: EmailService
        ) {
            // ...
        }
        
        // Setter注入
        @Service
        class PaymentService {
            
            private lateinit var userService: UserService
            
            @Autowired
            fun setUserService(userService: UserService) {
                this.userService = userService
            }
        }
        
        // 字段注入（不推荐）
        @Service
        class OrderService {
            
            @Autowired
            private lateinit var userService: UserService
        }
    """.trimIndent()
    
    println(diConfigCode)
    println()
    
    // 5. 异常处理
    println("--- 5. 异常处理 ---")
    
    val exceptionCode = """
        // 自定义异常
        class ResourceNotFoundException(message: String) : RuntimeException(message)
        
        class BusinessException(message: String) : RuntimeException(message)
        
        class ValidationException(message: String) : RuntimeException(message)
        
        // 全局异常处理
        @RestControllerAdvice
        class GlobalExceptionHandler {
            
            @ExceptionHandler(ResourceNotFoundException::class)
            fun handleNotFound(ex: ResourceNotFoundException): ResponseEntity<ErrorResponse> {
                val error = ErrorResponse(
                    status = HttpStatus.NOT_FOUND.value(),
                    message = ex.message ?: "Resource not found",
                    timestamp = LocalDateTime.now()
                )
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error)
            }
            
            @ExceptionHandler(BusinessException::class)
            fun handleBusinessException(ex: BusinessException): ResponseEntity<ErrorResponse> {
                val error = ErrorResponse(
                    status = HttpStatus.BAD_REQUEST.value(),
                    message = ex.message ?: "Business error",
                    timestamp = LocalDateTime.now()
                )
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error)
            }
            
            @ExceptionHandler(ValidationException::class)
            fun handleValidationException(ex: ValidationException): ResponseEntity<ErrorResponse> {
                val error = ErrorResponse(
                    status = HttpStatus.BAD_REQUEST.value(),
                    message = ex.message ?: "Validation error",
                    timestamp = LocalDateTime.now()
                )
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error)
            }
            
            @ExceptionHandler(Exception::class)
            fun handleGenericException(ex: Exception): ResponseEntity<ErrorResponse> {
                val error = ErrorResponse(
                    status = HttpStatus.INTERNAL_SERVER_ERROR.value(),
                    message = "Internal server error",
                    timestamp = LocalDateTime.now()
                )
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error)
            }
        }
        
        data class ErrorResponse(
            val status: Int,
            val message: String,
            val timestamp: LocalDateTime
        )
        
        // 使用异常
        @Service
        class UserService(
            private val userRepository: UserRepository
        ) {
            
            fun getUserById(id: Long): User {
                return userRepository.findById(id)
                    .orElseThrow { ResourceNotFoundException("User not found with id: $id") }
            }
            
            fun createUser(user: User): User {
                if (userRepository.findByEmail(user.email) != null) {
                    throw BusinessException("Email already exists")
                }
                if (user.age != null && user.age < 0) {
                    throw ValidationException("Age cannot be negative")
                }
                return userRepository.save(user)
            }
        }
    """.trimIndent()
    
    println(exceptionCode)
    println()
    
    // 6. 测试
    println("--- 6. 测试 ---")
    
    val testCode = """
        // 单元测试
        @SpringBootTest
        class UserServiceTest {
            
            @MockBean
            private lateinit var userRepository: UserRepository
            
            @Autowired
            private lateinit var userService: UserService
            
            @Test
            fun `getUserById should return user when exists`() {
                // given
                val user = User(1, "张三", "zhangsan@example.com", 18)
                given(userRepository.findById(1)).willReturn(Optional.of(user))
                
                // when
                val result = userService.getUserById(1)
                
                // then
                assertThat(result).isNotNull
                assertThat(result?.name).isEqualTo("张三")
            }
            
            @Test
            fun `getUserById should return null when not exists`() {
                // given
                given(userRepository.findById(1)).willReturn(Optional.empty())
                
                // when
                val result = userService.getUserById(1)
                
                // then
                assertThat(result).isNull()
            }
        }
        
        // 集成测试
        @SpringBootTest
        @AutoConfigureMockMvc
        class UserControllerTest {
            
            @Autowired
            private lateinit var mockMvc: MockMvc
            
            @Autowired
            private lateinit var userRepository: UserRepository
            
            @BeforeEach
            fun setup() {
                userRepository.deleteAll()
            }
            
            @Test
            fun `getAllUsers should return empty list`() {
                mockMvc.get("/api/users")
                    .andExpect {
                        status { isOk() }
                        content { jsonArray().isEmpty() }
                    }
            }
            
            @Test
            fun `createUser should create user`() {
                val userJson = """{
                    "name": "张三",
                    "email": "zhangsan@example.com",
                    "age": 18
                }""".trimIndent()
                
                mockMvc.post("/api/users") {
                    contentType = MediaType.APPLICATION_JSON
                    content = userJson
                }.andExpect {
                    status { isCreated() }
                    jsonPath("$.name") { value("张三") }
                    jsonPath("$.email") { value("zhangsan@example.com") }
                }
            }
        }
        
        // 使用MockK
        class UserServiceMockKTest {
            
            private val userRepository = mockk<UserRepository>()
            private val userService = UserService(userRepository)
            
            @Test
            fun `getUserById test`() {
                // given
                val user = User(1, "张三", "zhangsan@example.com", 18)
                every { userRepository.findById(1) } returns Optional.of(user)
                
                // when
                val result = userService.getUserById(1)
                
                // then
                assertThat(result?.name).isEqualTo("张三")
                verify(exactly = 1) { userRepository.findById(1) }
            }
        }
    """.trimIndent()
    
    println(testCode)
    println()
    
    // 7. Kotlin Coroutines with Spring
    println("--- 7. Kotlin Coroutines with Spring ---")
    
    val coroutinesCode = """
        // Coroutine Controller
        @RestController
        @RequestMapping("/api/coroutines")
        class CoroutineController {
            
            @GetMapping("/simple")
            suspend fun simple(): String {
                delay(1000)
                return "Hello from coroutine!"
            }
            
            @GetMapping("/data")
            suspend fun getData(): ResponseEntity<User> {
                val user = withContext(Dispatchers.IO) {
                    // 模拟数据库查询
                    delay(500)
                    User(1, "张三", "zhangsan@example.com", 18)
                }
                return ResponseEntity.ok(user)
            }
            
            @GetMapping("/concurrent")
            suspend fun concurrent(): Map<String, Any> = coroutineScope {
                val userDeferred = async { fetchUser() }
                val productsDeferred = async { fetchProducts() }
                
                mapOf(
                    "user" to userDeferred.await(),
                    "products" to productsDeferred.await()
                )
            }
            
            private suspend fun fetchUser(): User {
                delay(500)
                return User(1, "张三", "zhangsan@example.com", 18)
            }
            
            private suspend fun fetchProducts(): List<String> {
                delay(300)
                return listOf("产品1", "产品2", "产品3")
            }
        }
        
        // Coroutine Repository
        interface CoroutineUserRepository : CoroutineCrudRepository<User, Long> {
            
            suspend fun findByName(name: String): List<User>
            
            suspend fun findByEmail(email: String): User?
        }
        
        // Coroutine Service
        @Service
        class CoroutineUserService(
            private val userRepository: CoroutineUserRepository
        ) {
            
            suspend fun getAllUsers(): List<User> {
                return userRepository.findAll().toList()
            }
            
            suspend fun getUserById(id: Long): User? {
                return userRepository.findById(id)
            }
            
            suspend fun createUser(user: User): User {
                return userRepository.save(user)
            }
        }
        
        // Flow
        @RestController
        @RequestMapping("/api/flow")
        class FlowController {
            
            @GetMapping("/stream", produces = [MediaType.TEXT_EVENT_STREAM_VALUE])
            fun streamNumbers(): Flow<Int> = flow {
                for (i in 1..10) {
                    delay(500)
                    emit(i)
                }
            }
            
            @GetMapping("/users/stream")
            fun streamUsers(): Flow<User> = flow {
                val users = listOf(
                    User(1, "张三", "zhangsan@example.com", 18),
                    User(2, "李四", "lisi@example.com", 20),
                    User(3, "王五", "wangwu@example.com", 22)
                )
                users.forEach { user ->
                    delay(300)
                    emit(user)
                }
            }
        }
    """.trimIndent()
    
    println(coroutinesCode)
    println()
    
    println("🎉 Kotlin Spring Boot学习完成！")
    println("💡 Kotlin和Spring Boot配合非常完美！")
}
