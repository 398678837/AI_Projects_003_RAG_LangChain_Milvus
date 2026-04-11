// Kotlin Android开发示例代码

fun main() {
    println("=== Kotlin Android开发 ===")
    println()
    
    // 1. Activity基础
    println("--- 1. Activity基础 ---")
    
    val activityCode = """
        // MainActivity.kt
        class MainActivity : AppCompatActivity() {
            
            override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState)
                setContentView(R.layout.activity_main)
                
                // 初始化UI
                initViews()
                
                // 设置点击事件
                setupClickListeners()
            }
            
            private fun initViews() {
                val textView = findViewById<TextView>(R.id.textView)
                textView.text = "Hello Kotlin!"
            }
            
            private fun setupClickListeners() {
                val button = findViewById<Button>(R.id.button)
                button.setOnClickListener {
                    Toast.makeText(this, "按钮被点击了", Toast.LENGTH_SHORT).show()
                }
            }
            
            override fun onStart() {
                super.onStart()
                Log.d("MainActivity", "onStart")
            }
            
            override fun onResume() {
                super.onResume()
                Log.d("MainActivity", "onResume")
            }
            
            override fun onPause() {
                super.onPause()
                Log.d("MainActivity", "onPause")
            }
            
            override fun onStop() {
                super.onStop()
                Log.d("MainActivity", "onStop")
            }
            
            override fun onDestroy() {
                super.onDestroy()
                Log.d("MainActivity", "onDestroy")
            }
        }
    """.trimIndent()
    
    println(activityCode)
    println()
    
    // 2. ViewBinding
    println("--- 2. ViewBinding ---")
    
    val viewBindingCode = """
        // build.gradle (Module)
        android {
            buildFeatures {
                viewBinding true
            }
        }
        
        // MainActivity.kt
        class MainActivity : AppCompatActivity() {
            
            private lateinit var binding: ActivityMainBinding
            
            override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState)
                binding = ActivityMainBinding.inflate(layoutInflater)
                setContentView(binding.root)
                
                // 使用binding访问视图
                binding.textView.text = "Hello ViewBinding!"
                
                binding.button.setOnClickListener {
                    binding.textView.text = "按钮被点击了!"
                }
            }
        }
    """.trimIndent()
    
    println(viewBindingCode)
    println()
    
    // 3. ViewModel和LiveData
    println("--- 3. ViewModel和LiveData ---")
    
    val viewModelCode = """
        // MainViewModel.kt
        class MainViewModel : ViewModel() {
            
            private val _count = MutableLiveData(0)
            val count: LiveData<Int> = _count
            
            private val _userName = MutableLiveData("")
            val userName: LiveData<String> = _userName
            
            fun increment() {
                _count.value = (_count.value ?: 0) + 1
            }
            
            fun decrement() {
                _count.value = (_count.value ?: 0) - 1
            }
            
            fun setUserName(name: String) {
                _userName.value = name
            }
            
            // 模拟网络请求
            fun fetchData() {
                viewModelScope.launch {
                    try {
                        val result = apiService.getData()
                        _data.value = result
                    } catch (e: Exception) {
                        _error.value = e.message
                    }
                }
            }
        }
        
        // MainActivity.kt
        class MainActivity : AppCompatActivity() {
            
            private val viewModel: MainViewModel by viewModels()
            
            override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState)
                val binding = ActivityMainBinding.inflate(layoutInflater)
                setContentView(binding.root)
                
                // 观察LiveData
                viewModel.count.observe(this) { count ->
                    binding.countText.text = count.toString()
                }
                
                viewModel.userName.observe(this) { name ->
                    binding.nameText.text = name
                }
                
                // 按钮点击
                binding.incrementBtn.setOnClickListener {
                    viewModel.increment()
                }
                
                binding.decrementBtn.setOnClickListener {
                    viewModel.decrement()
                }
            }
        }
    """.trimIndent()
    
    println(viewModelCode)
    println()
    
    // 4. Room数据库
    println("--- 4. Room数据库 ---")
    
    val roomCode = """
        // User.kt - Entity
        @Entity(tableName = "users")
        data class User(
            @PrimaryKey(autoGenerate = true)
            val id: Int = 0,
            val name: String,
            val email: String,
            val age: Int
        )
        
        // UserDao.kt - DAO
        @Dao
        interface UserDao {
            
            @Query("SELECT * FROM users")
            fun getAllUsers(): Flow<List<User>>
            
            @Query("SELECT * FROM users WHERE id = :id")
            suspend fun getUserById(id: Int): User?
            
            @Insert(onConflict = OnConflictStrategy.REPLACE)
            suspend fun insertUser(user: User)
            
            @Update
            suspend fun updateUser(user: User)
            
            @Delete
            suspend fun deleteUser(user: User)
            
            @Query("DELETE FROM users")
            suspend fun deleteAllUsers()
        }
        
        // AppDatabase.kt - Database
        @Database(entities = [User::class], version = 1)
        abstract class AppDatabase : RoomDatabase() {
            abstract fun userDao(): UserDao
            
            companion object {
                @Volatile
                private var INSTANCE: AppDatabase? = null
                
                fun getDatabase(context: Context): AppDatabase {
                    return INSTANCE ?: synchronized(this) {
                        val instance = Room.databaseBuilder(
                            context.applicationContext,
                            AppDatabase::class.java,
                            "app_database"
                        ).build()
                        INSTANCE = instance
                        instance
                    }
                }
            }
        }
        
        // UserRepository.kt - Repository
        class UserRepository(private val userDao: UserDao) {
            
            val allUsers: Flow<List<User>> = userDao.getAllUsers()
            
            suspend fun insert(user: User) {
                userDao.insertUser(user)
            }
            
            suspend fun update(user: User) {
                userDao.updateUser(user)
            }
            
            suspend fun delete(user: User) {
                userDao.deleteUser(user)
            }
            
            suspend fun getUserById(id: Int): User? {
                return userDao.getUserById(id)
            }
        }
    """.trimIndent()
    
    println(roomCode)
    println()
    
    // 5. Retrofit网络请求
    println("--- 5. Retrofit网络请求 ---")
    
    val retrofitCode = """
        // ApiService.kt
        interface ApiService {
            
            @GET("users")
            suspend fun getUsers(): Response<List<User>>
            
            @GET("users/{id}")
            suspend fun getUser(@Path("id") id: Int): Response<User>
            
            @POST("users")
            suspend fun createUser(@Body user: User): Response<User>
            
            @PUT("users/{id}")
            suspend fun updateUser(
                @Path("id") id: Int,
                @Body user: User
            ): Response<User>
            
            @DELETE("users/{id}")
            suspend fun deleteUser(@Path("id") id: Int): Response<Unit>
        }
        
        // RetrofitClient.kt
        object RetrofitClient {
            
            private const val BASE_URL = "https://api.example.com/"
            
            private val okHttpClient = OkHttpClient.Builder()
                .addInterceptor(HttpLoggingInterceptor().apply {
                    level = HttpLoggingInterceptor.Level.BODY
                })
                .connectTimeout(30, TimeUnit.SECONDS)
                .readTimeout(30, TimeUnit.SECONDS)
                .build()
            
            private val retrofit = Retrofit.Builder()
                .baseUrl(BASE_URL)
                .client(okHttpClient)
                .addConverterFactory(GsonConverterFactory.create())
                .build()
            
            val apiService: ApiService = retrofit.create(ApiService::class.java)
        }
        
        // UserRepository.kt
        class UserRepository {
            
            private val apiService = RetrofitClient.apiService
            
            suspend fun getUsers(): Result<List<User>> {
                return try {
                    val response = apiService.getUsers()
                    if (response.isSuccessful) {
                        Result.success(response.body() ?: emptyList())
                    } else {
                        Result.failure(Exception("请求失败"))
                    }
                } catch (e: Exception) {
                    Result.failure(e)
                }
            }
            
            suspend fun createUser(user: User): Result<User> {
                return try {
                    val response = apiService.createUser(user)
                    if (response.isSuccessful) {
                        Result.success(response.body()!!)
                    } else {
                        Result.failure(Exception("创建失败"))
                    }
                } catch (e: Exception) {
                    Result.failure(e)
                }
            }
        }
        
        // UserViewModel.kt
        class UserViewModel(private val repository: UserRepository) : ViewModel() {
            
            private val _users = MutableStateFlow<List<User>>(emptyList())
            val users: StateFlow<List<User>> = _users
            
            private val _isLoading = MutableStateFlow(false)
            val isLoading: StateFlow<Boolean> = _isLoading
            
            private val _error = MutableStateFlow<String?>(null)
            val error: StateFlow<String?> = _error
            
            fun loadUsers() {
                viewModelScope.launch {
                    _isLoading.value = true
                    _error.value = null
                    
                    repository.getUsers().fold(
                        onSuccess = { users ->
                            _users.value = users
                        },
                        onFailure = { e ->
                            _error.value = e.message
                        }
                    )
                    
                    _isLoading.value = false
                }
            }
        }
    """.trimIndent()
    
    println(retrofitCode)
    println()
    
    // 6. Jetpack Compose
    println("--- 6. Jetpack Compose ---")
    
    val composeCode = """
        // MainActivity.kt
        class MainActivity : ComponentActivity() {
            override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState)
                setContent {
                    MyApplicationTheme {
                        Surface(
                            modifier = Modifier.fillMaxSize(),
                            color = MaterialTheme.colorScheme.background
                        ) {
                            MainScreen()
                        }
                    }
                }
            }
        }
        
        // MainScreen.kt
        @Composable
        fun MainScreen(viewModel: MainViewModel = viewModel()) {
            val count by viewModel.count.observeAsState(0)
            val isLoading by viewModel.isLoading.observeAsState(false)
            
            Scaffold(
                topBar = {
                    TopAppBar(
                        title = { Text("Compose Demo") }
                    )
                }
            ) { padding ->
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(padding)
                        .padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.Center
                ) {
                    Text(
                        text = "Count: $count",
                        style = MaterialTheme.typography.headlineMedium
                    )
                    
                    Spacer(modifier = Modifier.height(16.dp))
                    
                    Row(
                        horizontalArrangement = Arrangement.spacedBy(16.dp)
                    ) {
                        Button(onClick = { viewModel.decrement() }) {
                            Text("-")
                        }
                        Button(onClick = { viewModel.increment() }) {
                            Text("+")
                        }
                    }
                    
                    Spacer(modifier = Modifier.height(16.dp))
                    
                    if (isLoading) {
                        CircularProgressIndicator()
                    } else {
                        Button(onClick = { viewModel.loadData() }) {
                            Text("Load Data")
                        }
                    }
                }
            }
        }
        
        // ListScreen.kt
        @Composable
        fun ListScreen(users: List<User>) {
            LazyColumn {
                items(users) { user ->
                    UserItem(user = user)
                }
            }
        }
        
        @Composable
        fun UserItem(user: User) {
            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp),
                elevation = CardDefaults.cardElevation(4.dp)
            ) {
                Column(
                    modifier = Modifier.padding(16.dp)
                ) {
                    Text(
                        text = user.name,
                        style = MaterialTheme.typography.titleLarge
                    )
                    Text(
                        text = user.email,
                        style = MaterialTheme.typography.bodyMedium
                    )
                    Text(
                        text = "年龄: ${user.age}",
                        style = MaterialTheme.typography.bodySmall
                    )
                }
            }
        }
        
        // ViewModel with StateFlow
        class MainViewModel : ViewModel() {
            
            private val _count = MutableStateFlow(0)
            val count: StateFlow<Int> = _count.asStateFlow()
            
            private val _isLoading = MutableStateFlow(false)
            val isLoading: StateFlow<Boolean> = _isLoading.asStateFlow()
            
            fun increment() {
                _count.update { it + 1 }
            }
            
            fun decrement() {
                _count.update { it - 1 }
            }
            
            fun loadData() {
                viewModelScope.launch {
                    _isLoading.value = true
                    delay(2000) // 模拟网络请求
                    _isLoading.value = false
                }
            }
        }
    """.trimIndent()
    
    println(composeCode)
    println()
    
    // 7. Kotlin Coroutines in Android
    println("--- 7. Kotlin Coroutines in Android ---")
    
    val coroutinesAndroidCode = """
        // ViewModelScope
        class MyViewModel : ViewModel() {
            
            fun fetchData() {
                viewModelScope.launch {
                    try {
                        val result = apiService.getData()
                        _data.value = result
                    } catch (e: Exception) {
                        _error.value = e.message
                    }
                }
            }
        }
        
        // LifecycleScope
        class MyFragment : Fragment() {
            
            override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
                super.onViewCreated(view, savedInstanceState)
                
                viewLifecycleOwner.lifecycleScope.launch {
                    repeatOnLifecycle(Lifecycle.State.STARTED) {
                        viewModel.data.collect { data ->
                            updateUI(data)
                        }
                    }
                }
            }
        }
        
        // withContext切换线程
        suspend fun loadData(): Data {
            return withContext(Dispatchers.IO) {
                val response = apiService.getData()
                response.body()!!
            }
        }
        
        // async并发请求
        suspend fun fetchMultipleData() {
            val userDeferred = async { apiService.getUser() }
            val productsDeferred = async { apiService.getProducts() }
            
            val user = userDeferred.await()
            val products = productsDeferred.await()
            
            updateUI(user, products)
        }
        
        // StateFlow
        class MyViewModel : ViewModel() {
            
            private val _uiState = MutableStateFlow(UiState())
            val uiState: StateFlow<UiState> = _uiState.asStateFlow()
            
            fun loadData() {
                viewModelScope.launch {
                    _uiState.update { it.copy(isLoading = true) }
                    
                    try {
                        val data = apiService.getData()
                        _uiState.update { 
                            it.copy(
                                isLoading = false,
                                data = data
                            )
                        }
                    } catch (e: Exception) {
                        _uiState.update { 
                            it.copy(
                                isLoading = false,
                                error = e.message
                            )
                        }
                    }
                }
            }
        }
        
        data class UiState(
            val isLoading: Boolean = false,
            val data: Data? = null,
            val error: String? = null
        )
    """.trimIndent()
    
    println(coroutinesAndroidCode)
    println()
    
    println("🎉 Kotlin Android开发学习完成！")
    println("💡 Kotlin是Android开发的首选语言！")
}
