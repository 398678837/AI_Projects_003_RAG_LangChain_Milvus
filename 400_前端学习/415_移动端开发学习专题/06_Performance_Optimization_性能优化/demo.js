// 移动端性能优化示例代码

// 1. 启动优化
const startupOptimization = `
// 启动优化策略

// 1.1 代码分包/按需加载
const lazyLoading = {
  // React Native 按需加载
  reactNative: \`
    // 使用懒加载组件
    import { lazy, Suspense } from 'react';
    
    const HeavyComponent = lazy(() => import('./HeavyComponent'));
    
    function App() {
      return (
        <Suspense fallback={<Loading />}>
          <HeavyComponent />
        </Suspense>
      );
    }
  \`,
  
  // Flutter 按需加载
  flutter: \`
    // 使用 deferred 加载
    import 'package:flutter/material.dart' deferred as heavy;
    
    class MyApp extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return FutureBuilder(
          future: heavy.loadLibrary(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.done) {
              return heavy.HeavyWidget();
            }
            return LoadingWidget();
          },
        );
      }
    }
  \`,
  
  // uni-app 分包加载
  uniApp: \`
    // pages.json 配置分包
    {
      "pages": [
        "pages/index/index"
      ],
      "subPackages": [
        {
          "root": "packageA",
          "pages": [
            "pages/detail/detail"
          ]
        }
      ],
      "preloadRule": {
        "pages/index/index": {
          "network": "wifi",
          "packages": ["packageA"]
        }
      }
    }
  \`
};

// 1.2 资源预加载
const preloadResources = \`
// 预加载策略

// 预加载图片
function preloadImages(urls) {
  urls.forEach(url => {
    const img = new Image();
    img.src = url;
  });
}

// 预加载数据
async function preloadData() {
  try {
    const [userData, productData] = await Promise.all([
      fetch('/api/user'),
      fetch('/api/products')
    ]);
    
    // 存储到缓存
    localStorage.setItem('user', JSON.stringify(userData));
    localStorage.setItem('products', JSON.stringify(productData));
  } catch (error) {
    console.error('预加载失败:', error);
  }
}

// 应用启动时预加载
document.addEventListener('DOMContentLoaded', () => {
  preloadImages([
    '/images/banner1.jpg',
    '/images/banner2.jpg'
  ]);
  preloadData();
});
\`;

// 1.3 启动时间测量
const measureStartup = \`
// 测量启动时间

// Web 应用
if (window.performance) {
  const timing = performance.timing;
  
  const loadTime = timing.loadEventEnd - timing.navigationStart;
  const domReady = timing.domContentLoadedEventEnd - timing.navigationStart;
  
  console.log('页面加载时间:', loadTime, 'ms');
  console.log('DOM准备时间:', domReady, 'ms');
}

// React Native
import { Platform } from 'react-native';

if (Platform.OS === 'android') {
  console.time('App Startup');
  // 启动逻辑
  console.timeEnd('App Startup');
}

// 上报性能数据
async function reportPerformance(data) {
  await fetch('/api/performance', {
    method: 'POST',
    body: JSON.stringify(data)
  });
}
\`;

console.log('=== 启动优化 ===');
console.log('按需加载:', lazyLoading);
console.log('资源预加载:', preloadResources);
console.log('启动测量:', measureStartup);
`;

console.log('=== 启动优化 ===');
console.log(startupOptimization);

// 2. 渲染优化
const renderingOptimization = `
// 渲染优化策略

// 2.1 虚拟列表
const virtualList = {
  // React Native FlatList
  reactNative: \`
    import { FlatList } from 'react-native';
    
    function VirtualList() {
      const data = Array.from({ length: 1000 }, (_, i) => ({
        id: i,
        name: \`Item \${i}\`
      }));
      
      const renderItem = ({ item }) => (
        <View style={{ height: 50 }}>
          <Text>{item.name}</Text>
        </View>
      );
      
      return (
        <FlatList
          data={data}
          renderItem={renderItem}
          keyExtractor={item => item.id.toString()}
          initialNumToRender={10}
          maxToRenderPerBatch={10}
          windowSize={5}
        />
      );
    }
  \`,
  
  // Flutter ListView.builder
  flutter: \`
    ListView.builder(
      itemCount: 1000,
      itemBuilder: (context, index) {
        return ListTile(
          title: Text('Item \$index'),
        );
      },
    )
  \`,
  
  // Web 虚拟列表
  web: \`
    class VirtualList {
      constructor(container, itemHeight, totalItems) {
        this.container = container;
        this.itemHeight = itemHeight;
        this.totalItems = totalItems;
        this.visibleItems = [];
        this.scrollTop = 0;
        
        this.init();
      }
      
      init() {
        this.container.style.height = \`\${this.totalItems * this.itemHeight}px\`;
        this.container.addEventListener('scroll', this.onScroll.bind(this));
        this.render();
      }
      
      onScroll() {
        this.scrollTop = this.container.scrollTop;
        this.render();
      }
      
      render() {
        const start = Math.floor(this.scrollTop / this.itemHeight);
        const end = start + Math.ceil(this.container.clientHeight / this.itemHeight) + 2;
        
        const fragment = document.createDocumentFragment();
        for (let i = start; i < end && i < this.totalItems; i++) {
          const item = document.createElement('div');
          item.style.height = \`\${this.itemHeight}px\`;
          item.style.transform = \`translateY(\${i * this.itemHeight}px)\`;
          item.textContent = \`Item \${i}\`;
          fragment.appendChild(item);
        }
        
        this.container.innerHTML = '';
        this.container.appendChild(fragment);
      }
    }
  \`
};

// 2.2 减少不必要的重渲染
const reduceRerender = {
  // React 使用 memo
  react: \`
    import { memo, useMemo, useCallback } from 'react';
    
    // 使用 memo 避免不必要的重渲染
    const ExpensiveComponent = memo(({ data }) => {
      return <div>{data}</div>;
    });
    
    // 使用 useMemo 缓存计算结果
    function Parent({ list }) {
      const sortedList = useMemo(() => {
        return list.sort((a, b) => a - b);
      }, [list]);
      
      const handleClick = useCallback((id) => {
        console.log('Clicked:', id);
      }, []);
      
      return (
        <>
          <ExpensiveComponent data={sortedList} />
          <button onClick={() => handleClick(1)}>Click</button>
        </>
      );
    }
  \`,
  
  // Flutter 使用 const 和 const widgets
  flutter: \`
    class MyWidget extends StatelessWidget {
      const MyWidget({super.key});
      
      @override
      Widget build(BuildContext context) {
        return const Column(
          children: [
            Text('Hello'),  // 使用 const
            SizedBox(height: 10),
            Text('World'),
          ],
        );
      }
    }
    
    // 使用 RepaintBoundary 隔离重绘
    RepaintBoundary(
      child: ComplexWidget(),
    )
  \`
};

// 2.3 图片优化
const imageOptimization = \`
// 图片优化策略

// 1. 使用适当尺寸的图片
function getOptimizedImageUrl(baseUrl, width) {
  const devicePixelRatio = window.devicePixelRatio || 1;
  const actualWidth = Math.ceil(width * devicePixelRatio);
  return \`\${baseUrl}?w=\${actualWidth}&q=80\`;
}

// 2. 图片懒加载
const lazyImages = document.querySelectorAll('img[data-src]');
const lazyImageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
      lazyImageObserver.unobserve(img);
    }
  });
});

lazyImages.forEach(img => lazyImageObserver.observe(img));

// 3. 使用 WebP 格式
function supportsWebP() {
  const elem = document.createElement('canvas');
  return elem.toDataURL('image/webp').indexOf('data:image/webp') === 0;
}

// 4. 图片压缩和缓存
const imageCache = new Map();
async function loadImage(url) {
  if (imageCache.has(url)) {
    return imageCache.get(url);
  }
  
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => {
      imageCache.set(url, img);
      resolve(img);
    };
    img.onerror = reject;
    img.src = url;
  });
}
\`;

console.log('=== 渲染优化 ===');
console.log('虚拟列表:', virtualList);
console.log('减少重渲染:', reduceRerender);
console.log('图片优化:', imageOptimization);
`;

console.log('\n=== 渲染优化 ===');
console.log(renderingOptimization);

// 3. 内存优化
const memoryOptimization = `
// 内存优化策略

// 3.1 避免内存泄漏
const avoidMemoryLeaks = {
  // React 清理事件监听器
  react: \`
    import { useEffect } from 'react';
    
    function Component() {
      useEffect(() => {
        const handleScroll = () => {
          console.log('Scrolling');
        };
        
        window.addEventListener('scroll', handleScroll);
        
        // 清理函数
        return () => {
          window.removeEventListener('scroll', handleScroll);
        };
      }, []);
      
      return <div />;
    }
  \`,
  
  // Flutter 取消流订阅
  flutter: \`
    class _MyWidgetState extends State<MyWidget> {
      StreamSubscription? _subscription;
      
      @override
      void initState() {
        super.initState();
        _subscription = myStream.listen((data) {
          print(data);
        });
      }
      
      @override
      void dispose() {
        _subscription?.cancel();
        super.dispose();
      }
    }
  \`,
  
  // 避免闭包引用
  javascript: \`
    // ❌ 错误做法
    function badPractice() {
      const largeData = new Array(1000000).fill(0);
      return function() {
        return largeData.length;
      };
    }
    
    // ✅ 正确做法
    function goodPractice() {
      const largeData = new Array(1000000).fill(0);
      const length = largeData.length;
      largeData.length = 0; // 释放引用
      return function() {
        return length;
      };
    }
  \`
};

// 3.2 图片内存管理
const imageMemoryManagement = \`
// 图片内存管理

// 及时释放图片资源
class ImageManager {
  constructor() {
    this.cache = new Map();
    this.referenceCounts = new Map();
  }
  
  load(url) {
    if (this.cache.has(url)) {
      this.referenceCounts.set(url, (this.referenceCounts.get(url) || 0) + 1);
      return this.cache.get(url);
    }
    
    const img = new Image();
    img.src = url;
    this.cache.set(url, img);
    this.referenceCounts.set(url, 1);
    return img;
  }
  
  release(url) {
    const count = (this.referenceCounts.get(url) || 0) - 1;
    this.referenceCounts.set(url, count);
    
    if (count <= 0) {
      this.cache.delete(url);
      this.referenceCounts.delete(url);
    }
  }
  
  clear() {
    this.cache.clear();
    this.referenceCounts.clear();
  }
}

// 使用
const imageManager = new ImageManager();
const img = imageManager.load('image.jpg');
imageManager.release('image.jpg');
\`;

console.log('=== 内存优化 ===');
console.log('避免内存泄漏:', avoidMemoryLeaks);
console.log('图片内存管理:', imageMemoryManagement);
`;

console.log('\n=== 内存优化 ===');
console.log(memoryOptimization);

// 4. 网络优化
const networkOptimization = `
// 网络优化策略

// 4.1 请求合并和缓存
const requestOptimization = \`
// 请求缓存
class RequestCache {
  constructor(ttl = 5 * 60 * 1000) {
    this.cache = new Map();
    this.ttl = ttl;
  }
  
  async fetch(url, options = {}) {
    const cacheKey = \`\${url}:\${JSON.stringify(options)}\`;
    
    // 检查缓存
    if (this.cache.has(cacheKey)) {
      const cached = this.cache.get(cacheKey);
      if (Date.now() < cached.expireTime) {
        return cached.data;
      }
      this.cache.delete(cacheKey);
    }
    
    // 发起请求
    const response = await fetch(url, options);
    const data = await response.json();
    
    // 缓存结果
    this.cache.set(cacheKey, {
      data,
      expireTime: Date.now() + this.ttl
    });
    
    return data;
  }
  
  clear() {
    this.cache.clear();
  }
}

// 请求合并
class RequestBatcher {
  constructor() {
    this.pending = new Map();
  }
  
  request(key, fetchFn) {
    if (this.pending.has(key)) {
      return this.pending.get(key);
    }
    
    const promise = fetchFn().finally(() => {
      this.pending.delete(key);
    });
    
    this.pending.set(key, promise);
    return promise;
  }
}

// 使用
const cache = new RequestCache();
const batcher = new RequestBatcher();

async function fetchUser(id) {
  return batcher.request(\`user:\${id}\`, async () => {
    return cache.fetch(\`/api/users/\${id}\`);
  });
}
\`;

// 4.2 数据压缩和增量更新
const dataCompression = \`
// 使用 Gzip/Brotli 压缩
// 服务器端配置

// 前端请求压缩的资源
fetch('/api/data', {
  headers: {
    'Accept-Encoding': 'gzip, deflate, br'
  }
});

// 增量更新
async function fetchIncremental(lastModified) {
  const response = await fetch('/api/data', {
    headers: {
      'If-Modified-Since': lastModified
    }
  });
  
  if (response.status === 304) {
    // 数据未修改，使用缓存
    return getCachedData();
  }
  
  // 数据已更新
  const data = await response.json();
  setCachedData(data);
  return data;
}

// 使用 GraphQL 减少请求
const query = \`
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
      email
      posts {
        title
      }
    }
  }
\`;
\`;

console.log('=== 网络优化 ===');
console.log('请求优化:', requestOptimization);
console.log('数据压缩:', dataCompression);
`;

console.log('\n=== 网络优化 ===');
console.log(networkOptimization);

console.log('\n🎉 移动端性能优化学习完成！');
console.log('💡 性能优化是持续的过程，需要不断测量和改进！');
`;

console.log('\n=== 性能优化 ===');
