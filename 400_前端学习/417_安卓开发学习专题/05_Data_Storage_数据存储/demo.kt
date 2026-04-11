package com.example.datastorage

import android.content.ContentValues
import android.content.Context
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.room.*
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    private lateinit var etKey: EditText
    private lateinit var etValue: EditText
    private lateinit var tvResult: TextView
    private lateinit var dbHelper: MyDatabaseHelper
    private lateinit var appDatabase: AppDatabase

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        etKey = findViewById(R.id.et_key)
        etValue = findViewById(R.id.et_value)
        tvResult = findViewById(R.id.tv_result)

        val btnSaveSp = findViewById<Button>(R.id.btn_save_sp)
        val btnLoadSp = findViewById<Button>(R.id.btn_load_sp)
        val btnSaveFile = findViewById<Button>(R.id.btn_save_file)
        val btnLoadFile = findViewById<Button>(R.id.btn_load_file)
        val btnInsertDb = findViewById<Button>(R.id.btn_insert_db)
        val btnQueryDb = findViewById<Button>(R.id.btn_query_db)
        val btnInsertRoom = findViewById<Button>(R.id.btn_insert_room)
        val btnQueryRoom = findViewById<Button>(R.id.btn_query_room)

        dbHelper = MyDatabaseHelper(this, "BookStore.db", 1)
        appDatabase = AppDatabase.getDatabase(this)

        btnSaveSp.setOnClickListener { saveToSharedPreferences() }
        btnLoadSp.setOnClickListener { loadFromSharedPreferences() }
        btnSaveFile.setOnClickListener { saveToFile() }
        btnLoadFile.setOnClickListener { loadFromFile() }
        btnInsertDb.setOnClickListener { insertToDb() }
        btnQueryDb.setOnClickListener { queryFromDb() }
        btnInsertRoom.setOnClickListener { insertToRoom() }
        btnQueryRoom.setOnClickListener { queryFromRoom() }
    }

    private fun saveToSharedPreferences() {
        val key = etKey.text.toString()
        val value = etValue.text.toString()
        if (key.isEmpty() || value.isEmpty()) {
            Toast.makeText(this, "请输入key和value", Toast.LENGTH_SHORT).show()
            return
        }
        val sp = getSharedPreferences("my_sp", Context.MODE_PRIVATE)
        sp.edit().putString(key, value).apply()
        Toast.makeText(this, "已保存到SharedPreferences", Toast.LENGTH_SHORT).show()
    }

    private fun loadFromSharedPreferences() {
        val key = etKey.text.toString()
        if (key.isEmpty()) {
            Toast.makeText(this, "请输入key", Toast.LENGTH_SHORT).show()
            return
        }
        val sp = getSharedPreferences("my_sp", Context.MODE_PRIVATE)
        val value = sp.getString(key, "未找到")
        tvResult.text = "SharedPreferences:\n$key = $value"
    }

    private fun saveToFile() {
        val content = etValue.text.toString()
        if (content.isEmpty()) {
            Toast.makeText(this, "请输入内容", Toast.LENGTH_SHORT).show()
            return
        }
        try {
            val output = openFileOutput("data.txt", Context.MODE_PRIVATE)
            output.write(content.toByteArray())
            output.close()
            Toast.makeText(this, "已保存到文件", Toast.LENGTH_SHORT).show()
        } catch (e: Exception) {
            e.printStackTrace()
            Toast.makeText(this, "保存失败", Toast.LENGTH_SHORT).show()
        }
    }

    private fun loadFromFile() {
        try {
            val input = openFileInput("data.txt")
            val content = input.readBytes().toString(Charsets.UTF_8)
            input.close()
            tvResult.text = "文件内容:\n$content"
        } catch (e: Exception) {
            e.printStackTrace()
            tvResult.text = "读取文件失败"
        }
    }

    private fun insertToDb() {
        val db = dbHelper.writableDatabase
        val values = ContentValues().apply {
            put("name", "第一行代码")
            put("author", "郭霖")
            put("pages", 570)
            put("price", 79.00)
        }
        db.insert("Book", null, values)
        Toast.makeText(this, "已插入数据库", Toast.LENGTH_SHORT).show()
    }

    private fun queryFromDb() {
        val db = dbHelper.readableDatabase
        val cursor = db.query("Book", null, null, null, null, null, null)
        val result = StringBuilder("SQLite查询结果:\n")
        if (cursor.moveToFirst()) {
            do {
                val name = cursor.getString(cursor.getColumnIndexOrThrow("name"))
                val author = cursor.getString(cursor.getColumnIndexOrThrow("author"))
                val pages = cursor.getInt(cursor.getColumnIndexOrThrow("pages"))
                val price = cursor.getDouble(cursor.getColumnIndexOrThrow("price"))
                result.append("书名: $name, 作者: $author, 页数: $pages, 价格: $price\n")
            } while (cursor.moveToNext())
        }
        cursor.close()
        tvResult.text = result.toString()
    }

    private fun insertToRoom() {
        GlobalScope.launch {
            val book = BookEntity(0, "Kotlin实战", "Dmitry Jemerov", 450, 89.00)
            appDatabase.bookDao().insert(book)
            runOnUiThread {
                Toast.makeText(this@MainActivity, "已插入Room", Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun queryFromRoom() {
        GlobalScope.launch {
            val books = appDatabase.bookDao().getAllBooks()
            val result = StringBuilder("Room查询结果:\n")
            books.forEach {
                result.append("书名: ${it.name}, 作者: ${it.author}, 页数: ${it.pages}, 价格: ${it.price}\n")
            }
            runOnUiThread {
                tvResult.text = result.toString()
            }
        }
    }
}

class MyDatabaseHelper(context: Context, name: String, version: Int) :
    SQLiteOpenHelper(context, name, null, version) {
    
    private val createBook = """
        create table Book (
            id integer primary key autoincrement,
            author text,
            price real,
            pages integer,
            name text
        )
    """.trimIndent()

    override fun onCreate(db: SQLiteDatabase?) {
        db?.execSQL(createBook)
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
    }
}

@Entity(tableName = "books")
data class BookEntity(
    @PrimaryKey(autoGenerate = true) val id: Int,
    val name: String,
    val author: String,
    val pages: Int,
    val price: Double
)

@Dao
interface BookDao {
    @Insert
    suspend fun insert(book: BookEntity)

    @Query("SELECT * FROM books")
    suspend fun getAllBooks(): List<BookEntity>
}

@Database(entities = [BookEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun bookDao(): BookDao

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
