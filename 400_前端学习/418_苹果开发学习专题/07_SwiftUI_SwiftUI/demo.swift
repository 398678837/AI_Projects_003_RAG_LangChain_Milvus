import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            CounterView()
                .tabItem {
                    Label("计数器", systemImage: "number")
                }
            
            TodoListView()
                .tabItem {
                    Label("待办", systemImage: "checklist")
                }
            
            FormView()
                .tabItem {
                    Label("表单", systemImage: "square.and.pencil")
                }
            
            NavigationDemoView()
                .tabItem {
                    Label("导航", systemImage: "arrow.right")
                }
        }
    }
}

struct CounterView: View {
    @State private var count = 0
    @State private var isDarkMode = false
    
    var body: some View {
        VStack(spacing: 20) {
            Text("SwiftUI 示例")
                .font(.largeTitle)
                .fontWeight(.bold)
            
            Text("计数: \(count)")
                .font(.title)
            
            HStack(spacing: 20) {
                Button(action: {
                    count -= 1
                }) {
                    Image(systemName: "minus.circle.fill")
                        .font(.largeTitle)
                }
                
                Button(action: {
                    count += 1
                }) {
                    Image(systemName: "plus.circle.fill")
                        .font(.largeTitle)
                }
            }
            
            Button("重置") {
                count = 0
            }
            .buttonStyle(.borderedProminent)
            
            Toggle(isOn: $isDarkMode) {
                Text("深色模式")
            }
            .padding()
            
            Spacer()
        }
        .padding()
        .preferredColorScheme(isDarkMode ? .dark : .light)
    }
}

struct TodoItem: Identifiable {
    let id = UUID()
    let title: String
    var isCompleted: Bool
}

class TodoViewModel: ObservableObject {
    @Published var items: [TodoItem] = [
        TodoItem(title: "学习SwiftUI", isCompleted: false),
        TodoItem(title: "完成项目", isCompleted: true),
        TodoItem(title: "阅读文档", isCompleted: false)
    ]
    
    func addItem(title: String) {
        items.append(TodoItem(title: title, isCompleted: false))
    }
    
    func toggleItem(id: UUID) {
        if let index = items.firstIndex(where: { $0.id == id }) {
            items[index].isCompleted.toggle()
        }
    }
    
    func deleteItem(id: UUID) {
        items.removeAll { $0.id == id }
    }
}

struct TodoListView: View {
    @StateObject private var viewModel = TodoViewModel()
    @State private var newItemTitle = ""
    
    var body: some View {
        NavigationStack {
            VStack {
                HStack {
                    TextField("添加新待办", text: $newItemTitle)
                        .textFieldStyle(.roundedBorder)
                    
                    Button("添加") {
                        if !newItemTitle.isEmpty {
                            viewModel.addItem(title: newItemTitle)
                            newItemTitle = ""
                        }
                    }
                    .disabled(newItemTitle.isEmpty)
                    .buttonStyle(.borderedProminent)
                }
                .padding()
                
                List {
                    ForEach(viewModel.items) { item in
                        HStack {
                            Button(action: {
                                viewModel.toggleItem(id: item.id)
                            }) {
                                Image(systemName: item.isCompleted ? "checkmark.circle.fill" : "circle")
                                    .foregroundColor(item.isCompleted ? .green : .secondary)
                            }
                            
                            Text(item.title)
                                .strikethrough(item.isCompleted)
                                .foregroundColor(item.isCompleted ? .secondary : .primary)
                        }
                    }
                    .onDelete { indexSet in
                        for index in indexSet {
                            viewModel.deleteItem(id: viewModel.items[index].id)
                        }
                    }
                }
                .navigationTitle("待办列表")
            }
        }
    }
}

struct FormView: View {
    @State private var name = ""
    @State private var email = ""
    @State private var age = 18
    @State private var isStudent = false
    @State private var favoriteColor = Color.blue
    @State private var notificationEnabled = true
    
    var body: some View {
        NavigationStack {
            Form {
                Section("个人信息") {
                    TextField("姓名", text: $name)
                    TextField("邮箱", text: $email)
                        .keyboardType(.emailAddress)
                    
                    Stepper("年龄: \(age)", value: $age, in: 0...120)
                    
                    Toggle("学生", isOn: $isStudent)
                }
                
                Section("偏好设置") {
                    ColorPicker("喜欢的颜色", selection: $favoriteColor)
                    Toggle("通知", isOn: $notificationEnabled)
                }
                
                Section {
                    Button("提交") {
                        print("姓名: \(name), 邮箱: \(email), 年龄: \(age)")
                    }
                }
            }
            .navigationTitle("表单示例")
        }
    }
}

struct DetailView: View {
    let item: String
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        VStack(spacing: 20) {
            Text("详情页")
                .font(.largeTitle)
            
            Text("项目: \(item)")
                .font(.title)
            
            Button("返回") {
                dismiss()
            }
            .buttonStyle(.borderedProminent)
        }
        .navigationTitle("详情")
    }
}

struct NavigationDemoView: View {
    @State private var showSheet = false
    @State private var items = ["项目1", "项目2", "项目3", "项目4", "项目5"]
    
    var body: some View {
        NavigationStack {
            List(items, id: \.self) { item in
                NavigationLink(item) {
                    DetailView(item: item)
                }
            }
            .navigationTitle("导航示例")
            .toolbar {
                Button("Sheet") {
                    showSheet = true
                }
            }
            .sheet(isPresented: $showSheet) {
                SheetView()
            }
        }
    }
}

struct SheetView: View {
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationStack {
            VStack(spacing: 20) {
                Text("这是一个Sheet")
                    .font(.title)
                
                Button("关闭") {
                    dismiss()
                }
                .buttonStyle(.borderedProminent)
            }
            .navigationTitle("Sheet")
        }
    }
}

struct AnimationView: View {
    @State private var scale = 1.0
    @State private var rotation = 0.0
    @State private var opacity = 1.0
    @State private var offset = 0.0
    
    var body: some View {
        VStack(spacing: 30) {
            Text("动画示例")
                .font(.largeTitle)
            
            Circle()
                .fill(.blue)
                .frame(width: 100, height: 100)
                .scaleEffect(scale)
                .rotationEffect(.degrees(rotation))
                .opacity(opacity)
                .offset(y: offset)
            
            HStack(spacing: 20) {
                Button("缩放") {
                    withAnimation(.spring()) {
                        scale = scale == 1.0 ? 1.5 : 1.0
                    }
                }
                
                Button("旋转") {
                    withAnimation(.linear(duration: 1)) {
                        rotation += 360
                    }
                }
                
                Button("淡入淡出") {
                    withAnimation(.easeInOut) {
                        opacity = opacity == 1.0 ? 0.3 : 1.0
                    }
                }
                
                Button("移动") {
                    withAnimation(.easeInOut) {
                        offset = offset == 0.0 ? 50.0 : 0.0
                    }
                }
            }
        }
        .padding()
    }
}

struct UIKitRepresentableView: View {
    var body: some View {
        VStack {
            Text("UIKit集成")
                .font(.title)
            
            UIKitViewRepresentable()
                .frame(height: 100)
        }
    }
}

struct UIKitViewRepresentable: UIViewRepresentable {
    func makeUIView(context: Context) -> UILabel {
        let label = UILabel()
        label.text = "这是UIKit的UILabel"
        label.textAlignment = .center
        label.font = .systemFont(ofSize: 18)
        label.textColor = .systemBlue
        return label
    }
    
    func updateUIView(_ uiView: UILabel, context: Context) {
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
