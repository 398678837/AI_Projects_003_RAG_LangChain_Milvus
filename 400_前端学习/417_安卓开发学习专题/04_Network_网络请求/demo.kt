package com.example.network

import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.gson.Gson
import com.google.gson.annotations.SerializedName
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Path
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL

class MainActivity : AppCompatActivity() {

    private lateinit var tvResult: TextView
    private val gson = Gson()
    private val okHttpClient = OkHttpClient()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        tvResult = findViewById(R.id.tv_result)
        val btnHttpUrlConnection = findViewById<Button>(R.id.btn_http_url_connection)
        val btnOkHttpGet = findViewById<Button>(R.id.btn_okhttp_get)
        val btnOkHttpPost = findViewById<Button>(R.id.btn_okhttp_post)
        val btnRetrofit = findViewById<Button>(R.id.btn_retrofit)

        btnHttpUrlConnection.setOnClickListener {
            requestWithHttpUrlConnection()
        }

        btnOkHttpGet.setOnClickListener {
            requestWithOkHttpGet()
        }

        btnOkHttpPost.setOnClickListener {
            requestWithOkHttpPost()
        }

        btnRetrofit.setOnClickListener {
            requestWithRetrofit()
        }
    }

    private fun requestWithHttpUrlConnection() {
        GlobalScope.launch(Dispatchers.IO) {
            var connection: HttpURLConnection? = null
            try {
                val url = URL("https://api.github.com/users/octocat")
                connection = url.openConnection() as HttpURLConnection
                connection.requestMethod = "GET"
                connection.connectTimeout = 5000
                connection.readTimeout = 5000

                val responseCode = connection.responseCode
                if (responseCode == HttpURLConnection.HTTP_OK) {
                    val reader = BufferedReader(InputStreamReader(connection.inputStream))
                    val response = StringBuilder()
                    var line: String?
                    while (reader.readLine().also { line = it } != null) {
                        response.append(line)
                    }
                    reader.close()

                    val user = gson.fromJson(response.toString(), GithubUser::class.java)
                    updateResult("HttpURLConnection:\n${user.name}\n${user.bio}")
                }
            } catch (e: Exception) {
                Log.e("Network", "Error", e)
                updateResult("HttpURLConnection Error: ${e.message}")
            } finally {
                connection?.disconnect()
            }
        }
    }

    private fun requestWithOkHttpGet() {
        GlobalScope.launch(Dispatchers.IO) {
            try {
                val request = Request.Builder()
                    .url("https://api.github.com/users/octocat")
                    .build()

                val response = okHttpClient.newCall(request).execute()
                if (response.isSuccessful) {
                    val responseBody = response.body?.string()
                    val user = gson.fromJson(responseBody, GithubUser::class.java)
                    updateResult("OkHttp GET:\n${user.name}\n${user.bio}")
                }
            } catch (e: Exception) {
                Log.e("Network", "Error", e)
                updateResult("OkHttp GET Error: ${e.message}")
            }
        }
    }

    private fun requestWithOkHttpPost() {
        GlobalScope.launch(Dispatchers.IO) {
            try {
                val json = """{"name":"test","value":123}"""
                val requestBody = json.toRequestBody(okhttp3.MediaType.parse("application/json"))
                
                val request = Request.Builder()
                    .url("https://httpbin.org/post")
                    .post(requestBody)
                    .build()

                val response = okHttpClient.newCall(request).execute()
                if (response.isSuccessful) {
                    updateResult("OkHttp POST:\n${response.body?.string()}")
                }
            } catch (e: Exception) {
                Log.e("Network", "Error", e)
                updateResult("OkHttp POST Error: ${e.message}")
            }
        }
    }

    private fun requestWithRetrofit() {
        GlobalScope.launch(Dispatchers.IO) {
            try {
                val retrofit = Retrofit.Builder()
                    .baseUrl("https://api.github.com/")
                    .addConverterFactory(GsonConverterFactory.create())
                    .build()

                val service = retrofit.create(GithubService::class.java)
                val user = service.getUser("octocat")
                updateResult("Retrofit:\n${user.name}\n${user.bio}")
            } catch (e: Exception) {
                Log.e("Network", "Error", e)
                updateResult("Retrofit Error: ${e.message}")
            }
        }
    }

    private suspend fun updateResult(text: String) {
        withContext(Dispatchers.Main) {
            tvResult.text = text
        }
    }
}

data class GithubUser(
    val name: String?,
    val bio: String?,
    @SerializedName("avatar_url") val avatarUrl: String?
)

interface GithubService {
    @GET("users/{username}")
    suspend fun getUser(@Path("username") username: String): GithubUser
}
