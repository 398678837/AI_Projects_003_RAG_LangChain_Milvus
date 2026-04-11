package com.example.basicconcepts

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    companion object {
        private const val TAG = "MainActivity"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        Log.d(TAG, "onCreate: Activity被创建")
        initViews()
    }

    private fun initViews() {
        Log.d(TAG, "initViews: 初始化视图")
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, "onStart: Activity变得可见")
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, "onResume: Activity获得焦点，可以与用户交互")
    }

    override fun onPause() {
        super.onPause()
        Log.d(TAG, "onPause: Activity失去焦点")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "onStop: Activity变得不可见")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d(TAG, "onRestart: Activity从停止状态重新启动")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "onDestroy: Activity被销毁")
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        Log.d(TAG, "onSaveInstanceState: 保存Activity状态")
        outState.putString("key", "value")
    }

    override fun onRestoreInstanceState(savedInstanceState: Bundle) {
        super.onRestoreInstanceState(savedInstanceState)
        Log.d(TAG, "onRestoreInstanceState: 恢复Activity状态")
        val value = savedInstanceState.getString("key")
        Log.d(TAG, "恢复的值: $value")
    }
}
