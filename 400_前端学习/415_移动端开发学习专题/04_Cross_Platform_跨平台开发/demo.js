// 跨平台开发示例代码

// 1. React Native项目创建
const reactNativeSetup = `
// React Native项目创建

# 安装React Native CLI
npm install -g react-native-cli

# 创建项目
npx react-native init MyApp
cd MyApp

# 安装依赖
npm install

# 运行Android
npm run android

# 运行iOS
npm run ios

# 或使用Expo
npm install -g expo-cli
expo init MyApp
cd MyApp
npm start
`;

console.log('=== React Native项目创建 ===');
console.log(reactNativeSetup);

// 2. React Native组件示例
const reactNativeComponents = `
// React Native组件示例

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  TextInput,
  FlatList,
  Image,
  ScrollView,
  Alert,
  ToastAndroid
} from 'react-native';

// 基础组件
function HomeScreen() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Hello React Native!</Text>
      
      <View style={styles.counter}>
        <Text>计数: {count}</Text>
        <TouchableOpacity 
          style={styles.button}
          onPress={() => setCount(count + 1)}
        >
          <Text style={styles.buttonText}>+1</Text>
        </TouchableOpacity>
      </View>
      
      <TextInput
        style={styles.input}
        placeholder="请输入文字"
        value={text}
        onChangeText={setText}
      />
      
      <Text>你输入的是: {text}</Text>
    </ScrollView>
  );
}

// 列表组件
function ListScreen() {
  const [data, setData] = useState([
    { id: '1', name: '张三' },
    { id: '2', name: '李四' },
    { id: '3', name: '王五' }
  ]);

  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text style={styles.itemText}>{item.name}</Text>
    </View>
  );

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={item => item.id}
    />
  );
}

// 网络请求
function ApiScreen() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('https://api.example.com/users');
      const json = await response.json();
      setData(json);
    } catch (error) {
      console.error(error);
      Alert.alert('错误', '网络请求失败');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.center}>
        <Text>加载中...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text>数据: {JSON.stringify(data)}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20
  },
  counter: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20
  },
  button: {
    backgroundColor: '#2196F3',
    padding: 10,
    borderRadius: 5,
    marginLeft: 10
  },
  buttonText: {
    color: 'white'
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    paddingLeft: 10
  },
  item: {
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc'
  },
  itemText: {
    fontSize: 18
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  }
});

export default HomeScreen;
`;

console.log('\n=== React Native组件示例 ===');
console.log(reactNativeComponents);

// 3. Flutter项目创建
const flutterSetup = `
// Flutter项目创建

# 安装Flutter SDK
# 下载: https://flutter.dev/docs/get-started/install

# 检查环境
flutter doctor

# 创建项目
flutter create my_app
cd my_app

# 运行
flutter run

# 查看可用设备
flutter devices

# 运行在指定设备
flutter run -d <device_id>

# 构建
flutter build apk       # Android
flutter build ios       # iOS
flutter build appbundle # Android App Bundle
`;

console.log('\n=== Flutter项目创建 ===');
console.log(flutterSetup);

// 4. Flutter组件示例
const flutterComponents = `
// Flutter组件示例

import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

// 基础组件
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _counter = 0;
  String _text = '';

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter Demo'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Hello Flutter!',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            Row(
              children: [
                Text('计数: $_counter'),
                const SizedBox(width: 10),
                ElevatedButton(
                  onPressed: _incrementCounter,
                  child: const Text('+1'),
                ),
              ],
            ),
            const SizedBox(height: 20),
            TextField(
              decoration: const InputDecoration(
                hintText: '请输入文字',
                border: OutlineInputBorder(),
              ),
              onChanged: (value) {
                setState(() {
                  _text = value;
                });
              },
            ),
            const SizedBox(height: 10),
            Text('你输入的是: $_text'),
          ],
        ),
      ),
    );
  }
}

// 列表组件
class ListScreen extends StatelessWidget {
  final List<Map<String, String>> items = [
    {'id': '1', 'name': '张三'},
    {'id': '2', 'name': '李四'},
    {'id': '3', 'name': '王五'},
  ];

  ListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('列表')),
      body: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(items[index]['name']!),
            onTap: () {
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text('点击了 ${items[index]['name']}')),
              );
            },
          );
        },
      ),
    );
  }
}

// 网络请求
class ApiScreen extends StatefulWidget {
  const ApiScreen({super.key});

  @override
  State<ApiScreen> createState() => _ApiScreenState();
}

class _ApiScreenState extends State<ApiScreen> {
  List? _data;
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _fetchData();
  }

  Future<void> _fetchData() async {
    try {
      final response = await http.get(
        Uri.parse('https://api.example.com/users'),
      );
      
      if (response.statusCode == 200) {
        setState(() {
          _data = json.decode(response.body);
          _loading = false;
        });
      }
    } catch (e) {
      setState(() => _loading = false);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('网络请求失败')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('API请求')),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : Center(child: Text('数据: $_data')),
    );
  }
}
`;

console.log('\n=== Flutter组件示例 ===');
console.log(flutterComponents);

// 5. uni-app项目创建
const uniAppSetup = `
// uni-app项目创建

# 使用Vue CLI
npm install -g @vue/cli
vue create -p dcloudio/uni-preset-vue my-project

# 或使用HBuilderX
# 下载: https://www.dcloud.io/hbuilderx.html

# 运行到浏览器
npm run dev:h5

# 运行到微信小程序
npm run dev:mp-weixin

# 运行到App
npm run dev:app

# 构建
npm run build:h5
npm run build:mp-weixin
npm run build:app
`;

console.log('\n=== uni-app项目创建 ===');
console.log(uniAppSetup);

// 6. uni-app组件示例
const uniAppComponents = `
// uni-app组件示例

<template>
  <view class="container">
    <view class="title">Hello uni-app!</view>
    
    <view class="counter">
      <text>计数: {{ count }}</text>
      <button @click="increment">+1</button>
    </view>
    
    <input 
      v-model="text" 
      placeholder="请输入文字" 
    />
    <text>你输入的是: {{ text }}</text>
    
    <view class="list">
      <view 
        v-for="item in list" 
        :key="item.id"
        class="item"
        @click="handleItemClick(item)"
      >
        {{ item.name }}
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      count: 0,
      text: '',
      list: [
        { id: 1, name: '张三' },
        { id: 2, name: '李四' },
        { id: 3, name: '王五' }
      ]
    };
  },
  methods: {
    increment() {
      this.count++;
    },
    handleItemClick(item) {
      uni.showToast({
        title: \`点击了 \${item.name}\`,
        icon: 'none'
      });
    },
    async fetchData() {
      try {
        const res = await uni.request({
          url: 'https://api.example.com/users'
        });
        console.log(res.data);
      } catch (error) {
        uni.showToast({
          title: '请求失败',
          icon: 'none'
        });
      }
    }
  },
  onLoad() {
    this.fetchData();
  }
};
</script>

<style>
.container {
  padding: 20rpx;
}

.title {
  font-size: 48rpx;
  font-weight: bold;
  margin-bottom: 40rpx;
}

.counter {
  display: flex;
  align-items: center;
  margin-bottom: 40rpx;
}

.counter text {
  margin-right: 20rpx;
}

input {
  border: 1rpx solid #ccc;
  padding: 20rpx;
  margin-bottom: 20rpx;
}

.list {
  margin-top: 40rpx;
}

.item {
  padding: 30rpx;
  border-bottom: 1rpx solid #eee;
}
</style>
`;

console.log('\n=== uni-app组件示例 ===');
console.log(uniAppComponents);

// 7. 跨平台开发对比
const crossPlatformComparison = `
// 跨平台开发对比

const comparison = {
  ReactNative: {
    language: 'JavaScript/TypeScript',
    uiFramework: 'React',
    performance: '接近原生',
    learningCurve: '中等',
    ecosystem: '丰富',
    hotReload: true,
    pros: [
      'React生态',
      '热更新',
      '接近原生性能',
      '社区活跃'
    ],
    cons: [
      '部分功能需原生开发',
      'UI一致性一般',
      '包体积较大'
    ]
  },
  Flutter: {
    language: 'Dart',
    uiFramework: 'Flutter Widgets',
    performance: '最佳',
    learningCurve: '较高',
    ecosystem: '快速发展',
    hotReload: true,
    pros: [
      '性能最佳',
      'UI一致性最好',
      '热重载',
      '开发效率高'
    ],
    cons: [
      '需要学习Dart',
      '包体积较大',
      '生态还在发展'
    ]
  },
  uniApp: {
    language: 'Vue.js',
    uiFramework: 'uni-ui',
    performance: '良好',
    learningCurve: '低',
    ecosystem: '国内丰富',
    hotReload: true,
    pros: [
      'Vue技术栈',
      '多端发布',
      '学习成本低',
      '国内生态好'
    ],
    cons: [
      '部分平台受限',
      '国际生态一般',
      '性能一般'
    ]
  }
};

console.log('=== 跨平台开发对比 ===');
console.log('React Native:', comparison.ReactNative);
console.log('Flutter:', comparison.Flutter);
console.log('uni-app:', comparison.uniApp);
`;

console.log('\n=== 跨平台开发对比 ===');
console.log(crossPlatformComparison);

console.log('\n🎉 跨平台开发学习完成！');
console.log('💡 跨平台开发是现代移动端开发的主流选择！');
`;

console.log('\n=== 跨平台开发 ===');
