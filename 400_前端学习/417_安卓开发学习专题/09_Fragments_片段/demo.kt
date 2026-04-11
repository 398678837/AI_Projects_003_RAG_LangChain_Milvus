package com.example.fragments

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment

class MainActivity : AppCompatActivity(), FirstFragment.OnFragmentInteractionListener {

    companion object {
        private const val TAG = "MainActivity"
    }

    private var isSecondFragmentAdded = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d(TAG, "Activity onCreate")

        val btnAddFragment = findViewById<Button>(R.id.btn_add_fragment)
        val btnReplaceFragment = findViewById<Button>(R.id.btn_replace_fragment)
        val btnRemoveFragment = findViewById<Button>(R.id.btn_remove_fragment)
        val btnSendMessage = findViewById<Button>(R.id.btn_send_message)
        val etMessage = findViewById<EditText>(R.id.et_message)

        btnAddFragment.setOnClickListener {
            if (!isSecondFragmentAdded) {
                val fragment = SecondFragment.newInstance("这是SecondFragment")
                supportFragmentManager.beginTransaction()
                    .add(R.id.fragment_container, fragment, "SecondFragment")
                    .addToBackStack(null)
                    .commit()
                isSecondFragmentAdded = true
                Toast.makeText(this, "已添加SecondFragment", Toast.LENGTH_SHORT).show()
            }
        }

        btnReplaceFragment.setOnClickListener {
            val fragment = ThirdFragment.newInstance("这是ThirdFragment")
            supportFragmentManager.beginTransaction()
                .replace(R.id.fragment_container, fragment, "ThirdFragment")
                .addToBackStack(null)
                .commit()
            Toast.makeText(this, "已替换为ThirdFragment", Toast.LENGTH_SHORT).show()
        }

        btnRemoveFragment.setOnClickListener {
            val fragment = supportFragmentManager.findFragmentByTag("SecondFragment")
            if (fragment != null) {
                supportFragmentManager.beginTransaction()
                    .remove(fragment)
                    .commit()
                isSecondFragmentAdded = false
                Toast.makeText(this, "已移除SecondFragment", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "SecondFragment不存在", Toast.LENGTH_SHORT).show()
            }
        }

        btnSendMessage.setOnClickListener {
            val message = etMessage.text.toString()
            if (message.isNotEmpty()) {
                val firstFragment = supportFragmentManager.findFragmentById(R.id.first_fragment) as? FirstFragment
                firstFragment?.updateMessage(message)
                Toast.makeText(this, "消息已发送到FirstFragment", Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onFragmentInteraction(message: String) {
        Toast.makeText(this, "从FirstFragment收到: $message", Toast.LENGTH_SHORT).show()
        val secondFragment = supportFragmentManager.findFragmentByTag("SecondFragment") as? SecondFragment
        secondFragment?.updateMessage(message)
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, "Activity onStart")
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, "Activity onResume")
    }

    override fun onPause() {
        super.onPause()
        Log.d(TAG, "Activity onPause")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "Activity onStop")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "Activity onDestroy")
    }
}

class FirstFragment : Fragment() {

    companion object {
        private const val TAG = "FirstFragment"
    }

    private var listener: OnFragmentInteractionListener? = null
    private lateinit var tvMessage: TextView

    interface OnFragmentInteractionListener {
        fun onFragmentInteraction(message: String)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        Log.d(TAG, "onAttach")
        if (context is OnFragmentInteractionListener) {
            listener = context
        } else {
            throw RuntimeException("$context must implement OnFragmentInteractionListener")
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d(TAG, "onCreate")
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        Log.d(TAG, "onCreateView")
        return inflater.inflate(R.layout.fragment_first, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        Log.d(TAG, "onViewCreated")

        tvMessage = view.findViewById(R.id.tv_first_message)
        val btnSendToActivity = view.findViewById<Button>(R.id.btn_send_to_activity)

        btnSendToActivity.setOnClickListener {
            listener?.onFragmentInteraction("Hello from FirstFragment!")
        }
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        Log.d(TAG, "onActivityCreated")
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, "onStart")
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, "onResume")
    }

    override fun onPause() {
        super.onPause()
        Log.d(TAG, "onPause")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "onStop")
    }

    override fun onDestroyView() {
        super.onDestroyView()
        Log.d(TAG, "onDestroyView")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "onDestroy")
    }

    override fun onDetach() {
        super.onDetach()
        Log.d(TAG, "onDetach")
        listener = null
    }

    fun updateMessage(message: String) {
        tvMessage.text = message
    }
}

class SecondFragment : Fragment() {

    companion object {
        private const val ARG_PARAM = "param"
        private const val TAG = "SecondFragment"

        fun newInstance(param: String): SecondFragment {
            val fragment = SecondFragment()
            val args = Bundle()
            args.putString(ARG_PARAM, param)
            fragment.arguments = args
            return fragment
        }
    }

    private var param: String? = null
    private lateinit var tvMessage: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d(TAG, "onCreate")
        arguments?.let {
            param = it.getString(ARG_PARAM)
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        Log.d(TAG, "onCreateView")
        return inflater.inflate(R.layout.fragment_second, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        Log.d(TAG, "onViewCreated")

        tvMessage = view.findViewById(R.id.tv_second_message)
        tvMessage.text = param ?: "SecondFragment"
    }

    fun updateMessage(message: String) {
        tvMessage.text = message
    }
}

class ThirdFragment : Fragment() {

    companion object {
        private const val ARG_PARAM = "param"

        fun newInstance(param: String): ThirdFragment {
            val fragment = ThirdFragment()
            val args = Bundle()
            args.putString(ARG_PARAM, param)
            fragment.arguments = args
            return fragment
        }
    }

    private var param: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        arguments?.let {
            param = it.getString(ARG_PARAM)
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_third, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val tvMessage = view.findViewById<TextView>(R.id.tv_third_message)
        tvMessage.text = param ?: "ThirdFragment"
    }
}
