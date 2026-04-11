# 缓存策略

## 什么是缓存策略？

缓存策略是指通过各种技术和策略，将频繁访问的资源存储起来，减少重复请求，提高页面加载速度的过程。缓存策略是前端性能优化的重要组成部分，直接影响应用的响应速度和用户体验。

## 缓存策略的重要性

1. **加载速度**：缓存的资源加载速度更快，提高页面加载速度。
2. **带宽成本**：缓存减少了重复请求，降低了带宽使用，节省服务器成本。
3. **用户体验**：更快的加载速度提供更好的用户体验。
4. **离线访问**：适当的缓存策略可以提供离线访问能力。

## 缓存策略的类型

### 1. 浏览器缓存

- **强缓存**：使用Cache-Control和Expires头控制，浏览器直接从缓存中获取资源，不发送请求。
- **协商缓存**：使用ETag和Last-Modified头控制，浏览器发送请求验证资源是否过期，过期则重新获取。

### 2. Service Worker缓存

- **离线缓存**：使用Service Worker缓存静态资源，提供离线访问能力。
- **自定义缓存策略**：根据资源类型和使用场景，自定义缓存策略。

### 3. 本地存储

- **localStorage**：存储持久化数据，容量约5MB。
- **sessionStorage**：存储会话数据，页面关闭后清除。
- **IndexedDB**：存储结构化数据，容量更大。

### 4. CDN缓存

- **边缘缓存**：将资源缓存在CDN边缘节点，减少网络延迟。
- **缓存刷新**：通过版本号或路径变化刷新CDN缓存。

## 缓存策略的最佳实践

### 1. 浏览器缓存策略

- **静态资源**：设置较长的缓存时间（如1年），使用版本化URL。
- **动态资源**：使用协商缓存，设置较短的缓存时间。
- **HTML文件**：通常不缓存或设置较短的缓存时间，确保用户获取最新内容。

### 2. Service Worker缓存策略

- **预缓存**：在Service Worker安装时预缓存关键资源。
- **运行时缓存**：在运行时缓存动态资源。
- **缓存策略**：根据资源类型选择不同的缓存策略，如网络优先、缓存优先等。

### 3. 本地存储策略

- **数据存储**：存储用户偏好设置、表单数据等。
- **状态管理**：存储应用状态，提高页面恢复速度。
- **注意事项**：避免存储敏感数据，定期清理过期数据。

### 4. CDN缓存策略

- **缓存配置**：合理配置CDN缓存时间，根据资源变化频率调整。
- **缓存刷新**：使用版本化URL或缓存刷新API更新缓存。
- **回源策略**：配置合理的回源策略，确保资源更新及时。

## 缓存策略的实现

### 1. 浏览器缓存实现

#### 强缓存

```nginx
# Nginx配置
location ~* \.(css|js|jpg|jpeg|png|gif|ico|svg)$ {
  expires 1y;
  add_header Cache-Control "public, max-age=31536000";
  try_files $uri =404;
}
```

#### 协商缓存

```nginx
# Nginx配置
location ~* \.(php|html)$ {
  add_header Cache-Control "no-cache";
  try_files $uri =404;
}
```

### 2. Service Worker缓存实现

```javascript
// service-worker.js
const CACHE_NAME = 'my-app-cache-v1';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/css/main.css',
  '/js/main.js',
  '/images/logo.png'
];

// 安装事件，预缓存静态资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('缓存已打开');
        return cache.addAll(STATIC_ASSETS);
      })
  );
});

// 激活事件，清理旧缓存
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('清理旧缓存:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

//  fetch事件，处理网络请求
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // 如果缓存中有响应，则返回缓存
        if (response) {
          return response;
        }
        
        // 否则发起网络请求
        return fetch(event.request)
          .then((response) => {
            // 检查响应是否有效
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            
            // 克隆响应，因为响应流只能使用一次
            const responseToCache = response.clone();
            
            // 将响应添加到缓存
            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(event.request, responseToCache);
              });
            
            return response;
          });
      })
  );
});
```

### 3. 本地存储实现

#### localStorage

```javascript
// 存储数据
localStorage.setItem('user', JSON.stringify({ name: 'John', age: 30 }));

// 获取数据
const user = JSON.parse(localStorage.getItem('user'));

// 删除数据
localStorage.removeItem('user');

// 清空所有数据
localStorage.clear();
```

#### IndexedDB

```javascript
// 打开数据库
const request = indexedDB.open('my-db', 1);

// 创建对象存储
request.onupgradeneeded = (event) => {
  const db = event.target.result;
  if (!db.objectStoreNames.contains('users')) {
    db.createObjectStore('users', { keyPath: 'id' });
  }
};

// 存储数据
request.onsuccess = (event) => {
  const db = event.target.result;
  const transaction = db.transaction(['users'], 'readwrite');
  const store = transaction.objectStore('users');
  
  store.add({ id: 1, name: 'John', age: 30 });
  
  transaction.oncomplete = () => {
    console.log('数据存储成功');
  };
};

// 获取数据
request.onsuccess = (event) => {
  const db = event.target.result;
  const transaction = db.transaction(['users'], 'readonly');
  const store = transaction.objectStore('users');
  const getRequest = store.get(1);
  
  getRequest.onsuccess = () => {
    console.log('获取的数据:', getRequest.result);
  };
};
```

### 4. CDN缓存实现

```html
<!-- 使用版本化URL -->
<link rel="stylesheet" href="/css/main.css?v=1.0.0">
<script src="/js/main.js?v=1.0.0"></script>

<!-- 使用内容哈希 -->
<link rel="stylesheet" href="/css/main.5e7f9a.css">
<script src="/js/main.8d3f2b.js"></script>
```

## 缓存策略的问题与解决方案

### 1. 缓存更新问题

- **问题**：缓存的资源无法及时更新。
- **解决方案**：使用版本化URL或内容哈希，确保资源更新时URL变化。

### 2. 缓存一致性问题

- **问题**：不同用户获取到的资源版本不一致。
- **解决方案**：使用CDN缓存刷新API，确保所有边缘节点的缓存一致。

### 3. 缓存大小问题

- **问题**：缓存过大导致存储不足。
- **解决方案**：设置合理的缓存时间，定期清理过期缓存。

### 4. 缓存穿透问题

- **问题**：恶意请求导致缓存失效，直接访问服务器。
- **解决方案**：使用缓存预热，设置合理的缓存策略。

## 缓存策略的工具

### 1. 浏览器开发工具

- **Chrome DevTools**：网络面板可以查看缓存状态和资源加载情况。
- **Firefox Developer Tools**：网络面板可以查看缓存状态和资源加载情况。

### 2. 缓存分析工具

- **Lighthouse**：分析页面性能，包括缓存策略建议。
- **Google PageSpeed Insights**：分析页面性能，包括缓存策略建议。

### 3. Service Worker工具

- **Workbox**：Google开发的Service Worker工具库，简化Service Worker的使用。
- **sw-precache**：生成Service Worker代码，预缓存静态资源。

### 4. 本地存储工具

- **localForage**：增强的本地存储库，支持IndexedDB、WebSQL和localStorage。
- **Dexie.js**：IndexedDB的包装库，提供更简洁的API。

## 学习资源

- [HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
- [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
- [Workbox](https://developers.google.com/web/tools/workbox)
- [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache)