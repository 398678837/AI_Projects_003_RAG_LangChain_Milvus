package com.example.notification

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.graphics.BitmapFactory
import android.os.Build
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat

class MainActivity : AppCompatActivity() {

    companion object {
        const val CHANNEL_ID_NORMAL = "normal_channel"
        const val CHANNEL_ID_IMPORTANT = "important_channel"
        const val NOTIFICATION_ID_BASIC = 1
        const val NOTIFICATION_ID_BIG_TEXT = 2
        const val NOTIFICATION_ID_BIG_PICTURE = 3
        const val NOTIFICATION_ID_ACTION = 4
        const val NOTIFICATION_ID_PROGRESS = 5
    }

    private lateinit var notificationManager: NotificationManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        createNotificationChannels()

        val btnBasicNotification = findViewById<Button>(R.id.btn_basic_notification)
        val btnBigTextNotification = findViewById<Button>(R.id.btn_big_text_notification)
        val btnBigPictureNotification = findViewById<Button>(R.id.btn_big_picture_notification)
        val btnActionNotification = findViewById<Button>(R.id.btn_action_notification)
        val btnProgressNotification = findViewById<Button>(R.id.btn_progress_notification)

        btnBasicNotification.setOnClickListener { sendBasicNotification() }
        btnBigTextNotification.setOnClickListener { sendBigTextNotification() }
        btnBigPictureNotification.setOnClickListener { sendBigPictureNotification() }
        btnActionNotification.setOnClickListener { sendActionNotification() }
        btnProgressNotification.setOnClickListener { sendProgressNotification() }
    }

    private fun createNotificationChannels() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val normalChannel = NotificationChannel(
                CHANNEL_ID_NORMAL,
                "普通通知",
                NotificationManager.IMPORTANCE_DEFAULT
            ).apply {
                description = "普通通知渠道"
                enableVibration(true)
                enableLights(true)
            }

            val importantChannel = NotificationChannel(
                CHANNEL_ID_IMPORTANT,
                "重要通知",
                NotificationManager.IMPORTANCE_HIGH
            ).apply {
                description = "重要通知渠道"
                enableVibration(true)
                enableLights(true)
                setShowBadge(true)
            }

            notificationManager.createNotificationChannel(normalChannel)
            notificationManager.createNotificationChannel(importantChannel)
        }
    }

    private fun sendBasicNotification() {
        val intent = Intent(this, MainActivity::class.java)
        val pendingIntent = PendingIntent.getActivity(
            this,
            0,
            intent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        val notification = NotificationCompat.Builder(this, CHANNEL_ID_NORMAL)
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle("基本通知")
            .setContentText("这是一条基本通知")
            .setContentIntent(pendingIntent)
            .setAutoCancel(true)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .build()

        notificationManager.notify(NOTIFICATION_ID_BASIC, notification)
    }

    private fun sendBigTextNotification() {
        val longText = """
            这是一段很长的文本内容，使用BigTextStyle可以在通知中显示更多内容。
            当用户下拉通知时，可以看到完整的文本。
            这种样式适用于需要展示较多文字信息的场景，
            比如邮件内容、新闻摘要、消息详情等。
        """.trimIndent()

        val notification = NotificationCompat.Builder(this, CHANNEL_ID_IMPORTANT)
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle("大文本通知")
            .setContentText("点击展开查看更多内容")
            .setStyle(NotificationCompat.BigTextStyle().bigText(longText))
            .setAutoCancel(true)
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            .build()

        notificationManager.notify(NOTIFICATION_ID_BIG_TEXT, notification)
    }

    private fun sendBigPictureNotification() {
        val bitmap = BitmapFactory.decodeResource(resources, R.drawable.ic_launcher_foreground)

        val notification = NotificationCompat.Builder(this, CHANNEL_ID_IMPORTANT)
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle("大图片通知")
            .setContentText("点击展开查看图片")
            .setStyle(NotificationCompat.BigPictureStyle()
                .bigPicture(bitmap)
                .setBigContentTitle("图片标题")
                .setSummaryText("图片描述"))
            .setAutoCancel(true)
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            .build()

        notificationManager.notify(NOTIFICATION_ID_BIG_PICTURE, notification)
    }

    private fun sendActionNotification() {
        val replyIntent = Intent(this, MainActivity::class.java).apply {
            action = "ACTION_REPLY"
        }
        val replyPendingIntent = PendingIntent.getActivity(
            this,
            1,
            replyIntent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        val deleteIntent = Intent(this, MainActivity::class.java).apply {
            action = "ACTION_DELETE"
        }
        val deletePendingIntent = PendingIntent.getActivity(
            this,
            2,
            deleteIntent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        val notification = NotificationCompat.Builder(this, CHANNEL_ID_IMPORTANT)
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle("带操作按钮的通知")
            .setContentText("您可以选择回复或删除")
            .addAction(R.drawable.ic_reply, "回复", replyPendingIntent)
            .addAction(R.drawable.ic_delete, "删除", deletePendingIntent)
            .setAutoCancel(true)
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            .build()

        notificationManager.notify(NOTIFICATION_ID_ACTION, notification)
    }

    private fun sendProgressNotification() {
        val maxProgress = 100
        val notificationBuilder = NotificationCompat.Builder(this, CHANNEL_ID_NORMAL)
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle("下载中...")
            .setContentText("正在下载文件")
            .setPriority(NotificationCompat.PRIORITY_LOW)
            .setOngoing(true)

        Thread {
            var progress = 0
            while (progress <= maxProgress) {
                notificationBuilder.setProgress(maxProgress, progress, false)
                notificationManager.notify(NOTIFICATION_ID_PROGRESS, notificationBuilder.build())
                progress += 10
                Thread.sleep(500)
            }
            notificationBuilder
                .setContentText("下载完成")
                .setProgress(0, 0, false)
                .setOngoing(false)
                .setAutoCancel(true)
            notificationManager.notify(NOTIFICATION_ID_PROGRESS, notificationBuilder.build())
        }.start()
    }
}
