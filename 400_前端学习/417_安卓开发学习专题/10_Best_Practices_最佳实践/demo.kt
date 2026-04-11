package com.example.bestpractices

import android.content.Context
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.os.Message
import android.widget.Button
import android.widget.TextView
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.*
import kotlinx.coroutines.*
import java.lang.ref.WeakReference

class MainActivity : AppCompatActivity() {

    private val viewModel: MyViewModel by viewModels()
    private lateinit var tvData: TextView
    private lateinit var tvCounter: TextView
    private lateinit var btnStart: Button
    private lateinit var btnStop: Button
    private lateinit var btnLoad: Button

    private val safeHandler = SafeHandler(this)

    companion object {
        private const val MSG_UPDATE_COUNTER = 1
        private const val TAG = "MainActivity"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initViews()
        setupObservers()
        setupListeners()
    }

    private fun initViews() {
        tvData = findViewById(R.id.tv_data)
        tvCounter = findViewById(R.id.tv_counter)
        btnStart = findViewById(R.id.btn_start)
        btnStop = findViewById(R.id.btn_stop)
        btnLoad = findViewById(R.id.btn_load)
    }

    private fun setupObservers() {
        viewModel.data.observe(this) { data ->
            tvData.text = data
        }

        viewModel.isLoading.observe(this) { isLoading ->
            btnLoad.isEnabled = !isLoading
            btnLoad.text = if (isLoading) "加载中..." else "加载数据"
        }
    }

    private fun setupListeners() {
        btnStart.setOnClickListener {
            viewModel.startCounter()
        }

        btnStop.setOnClickListener {
            viewModel.stopCounter()
        }

        btnLoad.setOnClickListener {
            viewModel.loadData()
        }
    }

    fun updateCounter(counter: Int) {
        tvCounter.text = "计数器: $counter"
    }

    override fun onDestroy() {
        super.onDestroy()
        safeHandler.removeCallbacksAndMessages(null)
    }

    class SafeHandler(activity: MainActivity) : Handler(Looper.getMainLooper()) {
        private val activityRef = WeakReference(activity)

        override fun handleMessage(msg: Message) {
            val activity = activityRef.get() ?: return
            when (msg.what) {
                MSG_UPDATE_COUNTER -> {
                    activity.updateCounter(msg.arg1)
                }
            }
        }
    }
}

class MyViewModel : ViewModel() {

    private val _data = MutableLiveData<String>()
    val data: LiveData<String> = _data

    private val _isLoading = MutableLiveData<Boolean>(false)
    val isLoading: LiveData<Boolean> = _isLoading

    private var counterJob: Job? = null
    private var counter = 0

    private val repository = DataRepository()

    fun loadData() {
        viewModelScope.launch {
            _isLoading.value = true
            try {
                val result = repository.fetchData()
                _data.value = result
            } catch (e: Exception) {
                _data.value = "加载失败: ${e.message}"
            } finally {
                _isLoading.value = false
            }
        }
    }

    fun startCounter() {
        if (counterJob?.isActive == true) return
        counterJob = viewModelScope.launch {
            while (isActive) {
                counter++
                delay(1000)
            }
        }
    }

    fun stopCounter() {
        counterJob?.cancel()
        counterJob = null
    }

    override fun onCleared() {
        super.onCleared()
        counterJob?.cancel()
    }
}

class DataRepository {
    suspend fun fetchData(): String {
        return withContext(Dispatchers.IO) {
            delay(2000)
            "这是从服务器加载的数据\n时间: ${System.currentTimeMillis()}"
        }
    }
}

object SingletonManager {
    private var context: WeakReference<Context>? = null

    fun init(context: Context) {
        this.context = WeakReference(context.applicationContext)
    }

    fun getContext(): Context? {
        return context?.get()
    }
}

sealed class UiState<out T> {
    object Loading : UiState<Nothing>()
    data class Success<out T>(val data: T) : UiState<T>()
    data class Error(val message: String) : UiState<Nothing>()
}

data class User(
    val id: Long,
    val name: String,
    val email: String
)

interface UserRepository {
    suspend fun getUser(id: Long): User
    suspend fun saveUser(user: User)
    suspend fun deleteUser(id: Long)
}

class UserRepositoryImpl(
    private val localDataSource: UserLocalDataSource,
    private val remoteDataSource: UserRemoteDataSource
) : UserRepository {

    override suspend fun getUser(id: Long): User {
        return try {
            val remoteUser = remoteDataSource.getUser(id)
            localDataSource.saveUser(remoteUser)
            remoteUser
        } catch (e: Exception) {
            localDataSource.getUser(id)
        }
    }

    override suspend fun saveUser(user: User) {
        localDataSource.saveUser(user)
        try {
            remoteDataSource.saveUser(user)
        } catch (e: Exception) {
        }
    }

    override suspend fun deleteUser(id: Long) {
        localDataSource.deleteUser(id)
        try {
            remoteDataSource.deleteUser(id)
        } catch (e: Exception) {
        }
    }
}

interface UserLocalDataSource {
    suspend fun getUser(id: Long): User
    suspend fun saveUser(user: User)
    suspend fun deleteUser(id: Long)
}

interface UserRemoteDataSource {
    suspend fun getUser(id: Long): User
    suspend fun saveUser(user: User)
    suspend fun deleteUser(id: Long)
}

class MemoryLeakExample {
    private var context: Context? = null

    fun setContext(context: Context) {
        this.context = context
    }

    fun doSomething() {
    }
}

class MemorySafeExample {
    private var context: WeakReference<Context>? = null

    fun setContext(context: Context) {
        this.context = WeakReference(context)
    }

    fun doSomething() {
        context?.get()?.let {
        }
    }
}

class ResourceManager {
    private var resources: MutableList<Any> = mutableListOf()

    fun addResource(resource: Any) {
        resources.add(resource)
    }

    fun release() {
        resources.clear()
    }
}

fun <T> T?.orElse(default: T): T {
    return this ?: default
}

inline fun <T> measureTimeMillis(block: () -> T): Pair<T, Long> {
    val startTime = System.currentTimeMillis()
    val result = block()
    val endTime = System.currentTimeMillis()
    return result to (endTime - startTime)
}

class PerformanceOptimization {
    fun avoidCreatingObjectsInLoop(list: List<String>) {
        val stringBuilder = StringBuilder()
        for (item in list) {
            stringBuilder.append(item)
        }
    }

    fun useSparseArrayInsteadOfHashMap(map: Map<Int, String>) {
        val sparseArray = android.util.SparseArray<String>()
        for ((key, value) in map) {
            sparseArray.put(key, value)
        }
    }
}

class NetworkCacheManager {
    private val cache = mutableMapOf<String, CacheEntry>()

    fun put(key: String, data: String, expiryTime: Long = 300000) {
        cache[key] = CacheEntry(data, System.currentTimeMillis() + expiryTime)
    }

    fun get(key: String): String? {
        val entry = cache[key] ?: return null
        if (System.currentTimeMillis() > entry.expiryTime) {
            cache.remove(key)
            return null
        }
        return entry.data
    }

    fun clear() {
        cache.clear()
    }

    private data class CacheEntry(
        val data: String,
        val expiryTime: Long
    )
}

class Constants {
    companion object {
        const val BASE_URL = "https://api.example.com"
        const val TIMEOUT = 30
        const val MAX_RETRY_COUNT = 3
        const val CACHE_SIZE = 10 * 1024 * 1024
    }
}

enum class Status {
    LOADING, SUCCESS, ERROR, EMPTY
}
