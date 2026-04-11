// 原生开发示例代码

// 1. Swift基础语法
const swiftBasics = `
// Swift基础语法

// 变量和常量
var name = "张三"  // 变量
let pi = 3.14159    // 常量

// 类型注解
var age: Int = 18
var height: Double = 175.5
var isStudent: Bool = true

// 字符串
let greeting = "Hello, \\(name)!"
let multiLine = """
这是多行
字符串
"""

// 数组
var numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers[0] = 0

// 字典
var user = [
    "name": "张三",
    "age": 18
]
user["email"] = "zhangsan@example.com"

// 控制流
for i in 1...5 {
    print(i)
}

if age >= 18 {
    print("成年")
} else {
    print("未成年")
}

// 函数
func greet(name: String) -> String {
    return "Hello, \\(name)!"
}
let message = greet(name: "World")

// 结构体
struct Person {
    var name: String
    var age: Int
    
    func sayHello() {
        print("Hello, I'm \\(name)")
    }
}
let person = Person(name: "张三", age: 18)
person.sayHello()

// 类
class Animal {
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    func makeSound() {
        print("...")
    }
}
class Dog: Animal {
    override func makeSound() {
        print("汪汪!")
    }
}
let dog = Dog(name: "旺财")
dog.makeSound()
`;

console.log('=== Swift基础语法 ===');
console.log(swiftBasics);

// 2. SwiftUI示例
const swiftUIExample = `
// SwiftUI示例

import SwiftUI

// 基础视图
struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            Text("Hello, SwiftUI!")
                .font(.title)
                .foregroundColor(.blue)
            
            Button("点击我") {
                print("按钮被点击了")
            }
            .padding()
            .background(Color.green)
            .foregroundColor(.white)
            .cornerRadius(10)
        }
        .padding()
    }
}

// 状态管理
struct CounterView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("计数: \\(count)")
                .font(.largeTitle)
            
            HStack(spacing: 20) {
                Button("-") { count -= 1 }
                Button("+") { count += 1 }
            }
            .font(.title)
        }
    }
}

// 列表
struct ListView: View {
    let items = ["苹果", "香蕉", "橙子"]
    
    var body: some View {
        NavigationView {
            List(items, id: \\.self) { item in
                Text(item)
            }
            .navigationTitle("水果列表")
        }
    }
}

// 表单
struct FormView: View {
    @State private var name = ""
    @State private var email = ""
    @State private var agree = false
    
    var body: some View {
        NavigationView {
            Form {
                Section("个人信息") {
                    TextField("姓名", text: $name)
                    TextField("邮箱", text: $email)
                }
                
                Section {
                    Toggle("同意协议", isOn: $agree)
                }
                
                Section {
                    Button("提交") {
                        print("姓名: \\(name), 邮箱: \\(email)")
                    }
                    .disabled(!agree)
                }
            }
            .navigationTitle("注册")
        }
    }
}
`;

console.log('\n=== SwiftUI示例 ===');
console.log(swiftUIExample);

// 3. Kotlin基础语法
const kotlinBasics = `
// Kotlin基础语法

// 变量和常量
var name = "张三"  // 变量
val pi = 3.14159    // 只读变量

// 类型声明
var age: Int = 18
var height: Double = 175.5
var isStudent: Boolean = true

// 字符串
val greeting = "Hello, $name!"
val multiLine = """
    这是多行
    字符串
""".trimIndent()

// 数组
val numbers = arrayOf(1, 2, 3, 4, 5)
val mutableNumbers = mutableListOf(1, 2, 3)
mutableNumbers.add(4)

// 字典
val user = mutableMapOf(
    "name" to "张三",
    "age" to 18
)
user["email"] = "zhangsan@example.com"

// 控制流
for (i in 1..5) {
    println(i)
}

when {
    age >= 18 -> println("成年")
    else -> println("未成年")
}

// 函数
fun greet(name: String): String {
    return "Hello, $name!"
}
val message = greet("World")

// 数据类
data class Person(
    val name: String,
    val age: Int
) {
    fun sayHello() {
        println("Hello, I'm $name")
    }
}
val person = Person("张三", 18)
person.sayHello()

// 类
open class Animal(val name: String) {
    open fun makeSound() {
        println("...")
    }
}
class Dog(name: String) : Animal(name) {
    override fun makeSound() {
        println("汪汪!")
    }
}
val dog = Dog("旺财")
dog.makeSound()
`;

console.log('\n=== Kotlin基础语法 ===');
console.log(kotlinBasics);

// 4. Jetpack Compose示例
const composeExample = `
// Jetpack Compose示例

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

// 基础视图
@Composable
fun ContentView() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            text = "Hello, Compose!",
            style = MaterialTheme.typography.headlineMedium,
            color = MaterialTheme.colorScheme.primary
        )
        
        Button(onClick = { println("按钮被点击了") }) {
            Text("点击我")
        }
    }
}

// 状态管理
@Composable
fun CounterView() {
    var count by remember { mutableStateOf(0) }
    
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {
        Text(
            text = "计数: $count",
            style = MaterialTheme.typography.headlineLarge
        )
        
        Row(
            horizontalArrangement = Arrangement.spacedBy(20.dp)
        ) {
            Button(onClick = { count-- }) {
                Text("-")
            }
            Button(onClick = { count++ }) {
                Text("+")
            }
        }
    }
}

// 列表
@Composable
fun ListView() {
    val items = listOf("苹果", "香蕉", "橙子")
    
    Column {
        Text(
            text = "水果列表",
            style = MaterialTheme.typography.titleLarge,
            modifier = Modifier.padding(16.dp)
        )
        
        items.forEach { item ->
            ListItem(
                headlineContent = { Text(item) }
            )
            Divider()
        }
    }
}

// 表单
@Composable
fun FormView() {
    var name by remember { mutableStateOf("") }
    var email by remember { mutableStateOf("") }
    var agree by remember { mutableStateOf(false) }
    
    Column(
        modifier = Modifier.padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Text(
            text = "注册",
            style = MaterialTheme.typography.headlineMedium
        )
        
        OutlinedTextField(
            value = name,
            onValueChange = { name = it },
            label = { Text("姓名") }
        )
        
        OutlinedTextField(
            value = email,
            onValueChange = { email = it },
            label = { Text("邮箱") }
        )
        
        Row(
            verticalAlignment = Alignment.CenterVertically
        ) {
            Checkbox(
                checked = agree,
                onCheckedChange = { agree = it }
            )
            Text("同意协议")
        }
        
        Button(
            onClick = { println("姓名: $name, 邮箱: $email") },
            enabled = agree
        ) {
            Text("提交")
        }
    }
}
`;

console.log('\n=== Jetpack Compose示例 ===');
console.log(composeExample);

// 5. 原生开发优缺点对比
const nativeProsCons = `
// 原生开发优缺点

const nativePros = [
    '性能最佳 - 充分利用硬件',
    '用户体验最好 - 符合平台设计规范',
    '可访问全部原生API和功能',
    '应用商店审核更容易通过',
    '系统级优化支持更好',
    '离线体验优秀',
    '长期维护性好'
];

const nativeCons = [
    '需要维护两套代码（iOS + Android）',
    '开发成本高 - 需要两个开发团队',
    '开发周期长',
    '需要学习新的编程语言',
    '更新需要重新提交审核',
    '无法热更新',
    '包体积相对较大'
];

// 适用场景
const nativeUseCases = [
    '游戏应用 - 需要最佳性能',
    '图像处理/视频应用',
    'AR/VR应用',
    '系统级工具应用',
    '对性能要求极高的应用',
    '需要深度硬件集成的应用'
];

console.log('=== 原生开发优缺点 ===');
console.log('优点:', nativePros);
console.log('缺点:', nativeCons);
console.log('适用场景:', nativeUseCases);
`;

console.log('\n=== 原生开发优缺点 ===');
console.log(nativeProsCons);

console.log('\n🎉 原生开发学习完成！');
console.log('💡 原生开发适合追求最佳性能和体验的应用！');
`;

console.log('\n=== 原生开发 ===');
