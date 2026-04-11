package com.example.permissions

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.Settings
import android.widget.Button
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity() {

    private lateinit var btnCamera: Button
    private lateinit var btnStorage: Button
    private lateinit var btnLocation: Button
    private lateinit var btnCallPhone: Button

    private val cameraPermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        if (isGranted) {
            openCamera()
        } else {
            handlePermissionDenied(Manifest.permission.CAMERA, "相机")
        }
    }

    private val multiplePermissionsLauncher = registerForActivityResult(
        ActivityResultContracts.RequestMultiplePermissions()
    ) { permissions ->
        val allGranted = permissions.entries.all { it.value }
        if (allGranted) {
            Toast.makeText(this, "所有权限已授予", Toast.LENGTH_SHORT).show()
        } else {
            val deniedPermissions = permissions.filter { !it.value }.keys
            Toast.makeText(this, "部分权限被拒绝: $deniedPermissions", Toast.LENGTH_SHORT).show()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnCamera = findViewById(R.id.btn_camera)
        btnStorage = findViewById(R.id.btn_storage)
        btnLocation = findViewById(R.id.btn_location)
        btnCallPhone = findViewById(R.id.btn_call_phone)

        btnCamera.setOnClickListener {
            checkAndRequestPermission(Manifest.permission.CAMERA, "相机") {
                openCamera()
            }
        }

        btnStorage.setOnClickListener {
            requestMultiplePermissions()
        }

        btnLocation.setOnClickListener {
            checkAndRequestPermission(Manifest.permission.ACCESS_FINE_LOCATION, "位置") {
                getLocation()
            }
        }

        btnCallPhone.setOnClickListener {
            checkAndRequestPermission(Manifest.permission.CALL_PHONE, "电话") {
                makeCall()
            }
        }
    }

    private fun checkAndRequestPermission(permission: String, permissionName: String, onGranted: () -> Unit) {
        when {
            ContextCompat.checkSelfPermission(this, permission) == PackageManager.PERMISSION_GRANTED -> {
                onGranted()
            }
            shouldShowRequestPermissionRationale(permission) -> {
                showPermissionRationale(permission, permissionName, onGranted)
            }
            else -> {
                cameraPermissionLauncher.launch(permission)
            }
        }
    }

    private fun showPermissionRationale(permission: String, permissionName: String, onGranted: () -> Unit) {
        AlertDialog.Builder(this)
            .setTitle("需要权限")
            .setMessage("此功能需要$permissionName权限才能正常使用，请授予权限。")
            .setPositiveButton("确定") { _, _ ->
                cameraPermissionLauncher.launch(permission)
            }
            .setNegativeButton("取消", null)
            .show()
    }

    private fun handlePermissionDenied(permission: String, permissionName: String) {
        if (!shouldShowRequestPermissionRationale(permission)) {
            AlertDialog.Builder(this)
                .setTitle("权限被拒绝")
                .setMessage("您已永久拒绝$permissionName权限，请前往设置中开启。")
                .setPositiveButton("去设置") { _, _ ->
                    openAppSettings()
                }
                .setNegativeButton("取消", null)
                .show()
        } else {
            Toast.makeText(this, "$permissionName权限被拒绝", Toast.LENGTH_SHORT).show()
        }
    }

    private fun requestMultiplePermissions() {
        val permissions = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            arrayOf(
                Manifest.permission.READ_MEDIA_IMAGES,
                Manifest.permission.READ_MEDIA_VIDEO
            )
        } else {
            arrayOf(
                Manifest.permission.READ_EXTERNAL_STORAGE,
                Manifest.permission.WRITE_EXTERNAL_STORAGE
            )
        }
        
        multiplePermissionsLauncher.launch(permissions)
    }

    private fun openCamera() {
        Toast.makeText(this, "相机已打开", Toast.LENGTH_SHORT).show()
    }

    private fun getLocation() {
        Toast.makeText(this, "正在获取位置...", Toast.LENGTH_SHORT).show()
    }

    private fun makeCall() {
        val intent = Intent(Intent.ACTION_CALL)
        intent.data = Uri.parse("tel:10086")
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CALL_PHONE) == PackageManager.PERMISSION_GRANTED) {
            startActivity(intent)
        }
    }

    private fun openAppSettings() {
        val intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
        val uri = Uri.fromParts("package", packageName, null)
        intent.data = uri
        startActivity(intent)
    }
}
