package com.example.corecomponents

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var networkReceiver: NetworkReceiver

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btnGoToSecond = findViewById<Button>(R.id.btn_go_to_second)
        val btnStartService = findViewById<Button>(R.id.btn_start_service)
        val btnStopService = findViewById<Button>(R.id.btn_stop_service)
        val btnSendBroadcast = findViewById<Button>(R.id.btn_send_broadcast)

        btnGoToSecond.setOnClickListener {
            val intent = Intent(this, SecondActivity::class.java)
            intent.putExtra("username", "张三")
            intent.putExtra("age", 25)
            startActivity(intent)
        }

        btnStartService.setOnClickListener {
            val intent = Intent(this, MyService::class.java)
            startService(intent)
            Toast.makeText(this, "服务已启动", Toast.LENGTH_SHORT).show()
        }

        btnStopService.setOnClickListener {
            val intent = Intent(this, MyService::class.java)
            stopService(intent)
            Toast.makeText(this, "服务已停止", Toast.LENGTH_SHORT).show()
        }

        btnSendBroadcast.setOnClickListener {
            val intent = Intent("com.example.MY_BROADCAST")
            intent.putExtra("message", "这是自定义广播消息")
            sendBroadcast(intent)
        }

        networkReceiver = NetworkReceiver()
        val filter = IntentFilter()
        filter.addAction("android.net.conn.CONNECTIVITY_CHANGE")
        registerReceiver(networkReceiver, filter)
    }

    override fun onDestroy() {
        super.onDestroy()
        unregisterReceiver(networkReceiver)
    }
}

class SecondActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        val username = intent.getStringExtra("username")
        val age = intent.getIntExtra("age", 0)

        Toast.makeText(this, "用户名: $username, 年龄: $age", Toast.LENGTH_LONG).show()
    }
}

class MyService : android.app.Service() {
    override fun onCreate() {
        super.onCreate()
        android.util.Log.d("MyService", "onCreate: 服务创建")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        android.util.Log.d("MyService", "onStartCommand: 服务启动, startId: $startId")
        return START_STICKY
    }

    override fun onBind(intent: Intent?): android.os.IBinder? {
        return null
    }

    override fun onDestroy() {
        super.onDestroy()
        android.util.Log.d("MyService", "onDestroy: 服务销毁")
    }
}

class NetworkReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context?, intent: Intent?) {
        Toast.makeText(context, "网络状态发生变化", Toast.LENGTH_SHORT).show()
    }
}

class MyBroadcastReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context?, intent: Intent?) {
        val message = intent?.getStringExtra("message")
        Toast.makeText(context, "收到广播: $message", Toast.LENGTH_LONG).show()
    }
}
