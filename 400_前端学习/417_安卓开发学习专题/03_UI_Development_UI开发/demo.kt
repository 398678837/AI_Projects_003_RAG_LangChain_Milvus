package com.example.uidevelopment

import android.os.Bundle
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {

    private lateinit var etUsername: EditText
    private lateinit var etPassword: EditText
    private lateinit var btnLogin: Button
    private lateinit var cbRemember: CheckBox
    private lateinit var tvInfo: TextView
    private lateinit var recyclerView: RecyclerView
    private lateinit var adapter: MyAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initViews()
        setupRecyclerView()
        setupListeners()
    }

    private fun initViews() {
        etUsername = findViewById(R.id.et_username)
        etPassword = findViewById(R.id.et_password)
        btnLogin = findViewById(R.id.btn_login)
        cbRemember = findViewById(R.id.cb_remember)
        tvInfo = findViewById(R.id.tv_info)
        recyclerView = findViewById(R.id.recycler_view)
    }

    private fun setupRecyclerView() {
        val dataList = mutableListOf(
            "苹果", "香蕉", "橙子", "葡萄", "西瓜",
            "草莓", "蓝莓", "芒果", "菠萝", "猕猴桃"
        )
        
        adapter = MyAdapter(dataList)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = adapter
    }

    private fun setupListeners() {
        btnLogin.setOnClickListener {
            val username = etUsername.text.toString()
            val password = etPassword.text.toString()
            
            if (username.isEmpty() || password.isEmpty()) {
                Toast.makeText(this, "用户名或密码不能为空", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            
            val remember = cbRemember.isChecked
            tvInfo.text = "登录成功！\n用户名: $username\n记住密码: $remember"
            tvInfo.visibility = View.VISIBLE
        }
    }
}

class MyAdapter(private val dataList: List<String>) :
    RecyclerView.Adapter<MyAdapter.MyViewHolder>() {

    inner class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvItem: TextView = itemView.findViewById(R.id.tv_item)
    }

    override fun onCreateViewHolder(parent: android.view.ViewGroup, viewType: Int): MyViewHolder {
        val view = android.view.LayoutInflater.from(parent.context)
            .inflate(R.layout.item_recycler, parent, false)
        return MyViewHolder(view)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val item = dataList[position]
        holder.tvItem.text = item
        
        holder.itemView.setOnClickListener {
            Toast.makeText(holder.itemView.context, "点击了: $item", Toast.LENGTH_SHORT).show()
        }
    }

    override fun getItemCount(): Int = dataList.size
}
