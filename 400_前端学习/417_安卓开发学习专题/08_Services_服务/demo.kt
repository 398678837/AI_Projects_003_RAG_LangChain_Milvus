package com.example.services

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.os.*
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat

class MainActivity : AppCompatActivity() {

    private lateinit var tvServiceStatus: TextView
    private var myBoundService: MyBoundService? = null
    private var isBound = false

    private val serviceConnection = object : ServiceConnection {
        override fun onServiceConnected(name: ComponentName?, service: IBinder?) {
            val binder = service as MyBoundService.LocalBinder
            myBoundService = binder.getService()
            isBound = true
            tvServiceStatus.text = "服务已绑定"
        }

        override fun onServiceDisconnected(name: ComponentName?) {
            isBound = false
            myBoundService = null
            tvServiceStatus.text = "服务已解绑"
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        tvServiceStatus = findViewById(R.id.tv_service_status)
        val btnStartService = findViewById<Button>(R.id.btn_start_service)
        val btnStopService = findViewById<Button>(R.id.btn_stop_service)
        val btnBindService = findViewById<Button>(R.id.btn_bind_service)
        val btnUnbindService = findViewById<Button>(R.id.btn_unbind_service)
        val btnGetRandomNumber = findViewById<Button>(R.id.btn_get_random_number)
        val btnStartForegroundService = findViewById<Button>(R.id.btn_start_foreground_service)
        val btnStopForegroundService = findViewById<Button>(R.id.btn_stop_foreground_service)
        val btnStartIntentService = findViewById<Button>(R.id.btn_start_intent_service)

        btnStartService.setOnClickListener { startMyService() }
        btnStopService.setOnClickListener { stopMyService() }
        btnBindService.setOnClickListener { bindMyService() }
        btnUnbindService.setOnClickListener { unbindMyService() }
        btnGetRandomNumber.setOnClickListener { getRandomNumber() }
        btnStartForegroundService.setOnClickListener { startForegroundService() }
        btnStopForegroundService.setOnClickListener { stopForegroundService() }
        btnStartIntentService.setOnClickListener { startIntentService() }
    }

    private fun startMyService() {
        val intent = Intent(this, MyStartedService::class.java)
        intent.putExtra("data", "Hello from Activity")
        startService(intent)
        Toast.makeText(this, "服务已启动", Toast.LENGTH_SHORT).show()
    }

    private fun stopMyService() {
        val intent = Intent(this, MyStartedService::class.java)
        stopService(intent)
        Toast.makeText(this, "服务已停止", Toast.LENGTH_SHORT).show()
    }

    private fun bindMyService() {
        val intent = Intent(this, MyBoundService::class.java)
        bindService(intent, serviceConnection, Context.BIND_AUTO_CREATE)
        Toast.makeText(this, "正在绑定服务...", Toast.LENGTH_SHORT).show()
    }

    private fun unbindMyService() {
        if (isBound) {
            unbindService(serviceConnection)
            isBound = false
            Toast.makeText(this, "服务已解绑", Toast.LENGTH_SHORT).show()
        }
    }

    private fun getRandomNumber() {
        if (isBound) {
            val num = myBoundService?.getRandomNumber()
            Toast.makeText(this, "随机数: $num", Toast.LENGTH_SHORT).show()
        } else {
            Toast.makeText(this, "请先绑定服务", Toast.LENGTH_SHORT).show()
        }
    }

    private fun startForegroundService() {
        val intent = Intent(this, MyForegroundService::class.java)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            startForegroundService(intent)
        } else {
            startService(intent)
        }
        Toast.makeText(this, "前台服务已启动", Toast.LENGTH_SHORT).show()
    }

    private fun stopForegroundService() {
        val intent = Intent(this, MyForegroundService::class.java)
        stopService(intent)
        Toast.makeText(this, "前台服务已停止", Toast.LENGTH_SHORT).show()
    }

    private fun startIntentService() {
        val intent = Intent(this, MyIntentService::class.java)
        intent.putExtra("task1", "下载文件")
        intent.putExtra("task2", "处理数据")
        intent.putExtra("task3", "上传结果")
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            startForegroundService(intent)
        } else {
            startService(intent)
        }
        Toast.makeText(this, "IntentService已启动", Toast.LENGTH_SHORT).show()
    }

    override fun onDestroy() {
        super.onDestroy()
        if (isBound) {
            unbindService(serviceConnection)
            isBound = false
        }
    }
}

class MyStartedService : Service() {
    override fun onCreate() {
        super.onCreate()
        android.util.Log.d("MyStartedService", "onCreate")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        android.util.Log.d("MyStartedService", "onStartCommand, startId: $startId")
        val data = intent?.getStringExtra("data")
        android.util.Log.d("MyStartedService", "接收到数据: $data")
        
        Thread {
            for (i in 1..5) {
                Thread.sleep(1000)
                android.util.Log.d("MyStartedService", "任务执行中: $i")
            }
            android.util.Log.d("MyStartedService", "任务执行完成")
        }.start()

        return START_STICKY
    }

    override fun onBind(intent: Intent?): IBinder? {
        return null
    }

    override fun onDestroy() {
        super.onDestroy()
        android.util.Log.d("MyStartedService", "onDestroy")
    }
}

class MyBoundService : Service() {
    private val binder = LocalBinder()
    private val random = java.util.Random()

    inner class LocalBinder : Binder() {
        fun getService(): MyBoundService = this@MyBoundService
    }

    override fun onCreate() {
        super.onCreate()
        android.util.Log.d("MyBoundService", "onCreate")
    }

    override fun onBind(intent: Intent?): IBinder? {
        android.util.Log.d("MyBoundService", "onBind")
        return binder
    }

    override fun onUnbind(intent: Intent?): Boolean {
        android.util.Log.d("MyBoundService", "onUnbind")
        return super.onUnbind(intent)
    }

    override fun onDestroy() {
        super.onDestroy()
        android.util.Log.d("MyBoundService", "onDestroy")
    }

    fun getRandomNumber(): Int = random.nextInt(100)
}

class MyForegroundService : Service() {
    companion object {
        const val CHANNEL_ID = "foreground_service_channel"
        const val NOTIFICATION_ID = 1001
    }

    override fun onCreate() {
        super.onCreate()
        createNotificationChannel()
        startForeground(NOTIFICATION_ID, createNotification())
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID,
                "前台服务通知",
                NotificationManager.IMPORTANCE_LOW
            )
            val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
            notificationManager.createNotificationChannel(channel)
        }
    }

    private fun createNotification(): Notification {
        return NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("前台服务")
            .setContentText("服务正在运行中...")
            .setSmallIcon(R.drawable.ic_notification)
            .build()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        android.util.Log.d("MyForegroundService", "前台服务运行中")
        return START_STICKY
    }

    override fun onBind(intent: Intent?): IBinder? {
        return null
    }
}

class MyIntentService : Service() {
    private val handlerThread = HandlerThread("IntentServiceThread").apply { start() }
    private val handler = Handler(handlerThread.looper)

    override fun onCreate() {
        super.onCreate()
        android.util.Log.d("MyIntentService", "onCreate")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        android.util.Log.d("MyIntentService", "onStartCommand")
        handler.post {
            intent?.let {
                val task1 = it.getStringExtra("task1")
                val task2 = it.getStringExtra("task2")
                val task3 = it.getStringExtra("task3")

                task1?.let { task ->
                    android.util.Log.d("MyIntentService", "开始执行: $task")
                    Thread.sleep(2000)
                    android.util.Log.d("MyIntentService", "完成: $task")
                }
                task2?.let { task ->
                    android.util.Log.d("MyIntentService", "开始执行: $task")
                    Thread.sleep(2000)
                    android.util.Log.d("MyIntentService", "完成: $task")
                }
                task3?.let { task ->
                    android.util.Log.d("MyIntentService", "开始执行: $task")
                    Thread.sleep(2000)
                    android.util.Log.d("MyIntentService", "完成: $task")
                }
            }
            stopSelf(startId)
        }
        return START_NOT_STICKY
    }

    override fun onBind(intent: Intent?): IBinder? {
        return null
    }

    override fun onDestroy() {
        super.onDestroy()
        handlerThread.quit()
        android.util.Log.d("MyIntentService", "onDestroy")
    }
}
