// 前端性能优化基础概念示例

// 1. 性能监控示例
function monitorPerformance() {
  console.log('=== 性能监控示例 ===');
  
  // 页面加载完成后监控性能指标
  window.addEventListener('load', () => {
    const performance = window.performance;
    
    // 获取导航时序数据
    const navigationTiming = performance.getEntriesByType('navigation')[0];
    console.log('导航时序数据:', navigationTiming);
    
    // 计算页面加载时间
    const loadTime = navigationTiming.loadEventEnd - navigationTiming.navigationStart;
    console.log('页面加载时间:', loadTime, 'ms');
    
    // 计算DOM加载完成时间
    const domContentLoadedTime = navigationTiming.domContentLoadedEventEnd - navigationTiming.navigationStart;
    console.log('DOM加载完成时间:', domContentLoadedTime, 'ms');
    
    // 计算首字节时间
    const timeToFirstByte = navigationTiming.responseStart - navigationTiming.navigationStart;
    console.log('首字节时间:', timeToFirstByte, 'ms');
  });
  
  // 监控FCP和LCP
  const observer = new PerformanceObserver((list) => {
    list.getEntries().forEach((entry) => {
      if (entry.name === 'first-contentful-paint') {
        console.log('首次内容绘制(FCP):', entry.startTime, 'ms');
      } else if (entry.name === 'largest-contentful-paint') {
        console.log('最大内容绘制(LCP):', entry.startTime, 'ms');
      }
    });
  });
  
  observer.observe({ entryTypes: ['paint'] });
  
  // 监控CLS
  const clsObserver = new PerformanceObserver((list) => {
    list.getEntries().forEach((entry) => {
      if (entry.name === 'layout-shift') {
        console.log('布局偏移(CLS):', entry.value);
      }
    });
  });
  
  clsObserver.observe({ entryTypes: ['layout-shift'] });
}

// 2. DOM操作优化示例
function domOptimization() {
  console.log('\n=== DOM操作优化示例 ===');
  
  // 优化前：频繁操作DOM
  function unoptimizedDomOperation() {
    console.time('未优化的DOM操作');
    const container = document.getElementById('container');
    for (let i = 0; i < 1000; i++) {
      container.innerHTML += `<div>${i}</div>`;
    }
    console.timeEnd('未优化的DOM操作');
  }
  
  // 优化后：批量操作DOM
  function optimizedDomOperation() {
    console.time('优化的DOM操作');
    const container = document.getElementById('container');
    let html = '';
    for (let i = 0; i < 1000; i++) {
      html += `<div>${i}</div>`;
    }
    container.innerHTML = html;
    console.timeEnd('优化的DOM操作');
  }
  
  // 优化后：使用DocumentFragment
  function optimizedDomOperationWithFragment() {
    console.time('使用DocumentFragment的DOM操作');
    const container = document.getElementById('container');
    const fragment = document.createDocumentFragment();
    for (let i = 0; i < 1000; i++) {
      const div = document.createElement('div');
      div.textContent = i;
      fragment.appendChild(div);
    }
    container.appendChild(fragment);
    console.timeEnd('使用DocumentFragment的DOM操作');
  }
  
  // 测试DOM操作性能
  setTimeout(() => {
    unoptimizedDomOperation();
    // 清空容器
    document.getElementById('container').innerHTML = '';
    
    setTimeout(() => {
      optimizedDomOperation();
      // 清空容器
      document.getElementById('container').innerHTML = '';
      
      setTimeout(() => {
        optimizedDomOperationWithFragment();
      }, 100);
    }, 100);
  }, 100);
}

// 3. 防抖和节流示例
function debounceAndThrottle() {
  console.log('\n=== 防抖和节流示例 ===');
  
  // 防抖函数
  function debounce(func, wait) {
    let timeout;
    return function() {
      const context = this;
      const args = arguments;
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        func.apply(context, args);
      }, wait);
    };
  }
  
  // 节流函数
  function throttle(func, limit) {
    let inThrottle;
    return function() {
      const context = this;
      const args = arguments;
      if (!inThrottle) {
        func.apply(context, args);
        inThrottle = true;
        setTimeout(() => {
          inThrottle = false;
        }, limit);
      }
    };
  }
  
  // 测试防抖
  const debouncedFunction = debounce(() => {
    console.log('防抖函数执行');
  }, 1000);
  
  // 测试节流
  const throttledFunction = throttle(() => {
    console.log('节流函数执行');
  }, 1000);
  
  console.log('连续调用防抖函数...');
  for (let i = 0; i < 5; i++) {
    debouncedFunction();
  }
  
  console.log('连续调用节流函数...');
  for (let i = 0; i < 5; i++) {
    throttledFunction();
  }
}

// 4. 内存优化示例
function memoryOptimization() {
  console.log('\n=== 内存优化示例 ===');
  
  // 优化前：可能导致内存泄漏
  function memoryLeakExample() {
    const element = document.getElementById('memory-test');
    element.addEventListener('click', function() {
      console.log('点击事件处理');
      // 这里可能存在闭包导致的内存泄漏
    });
    // 没有移除事件监听器
  }
  
  // 优化后：正确管理事件监听器
  function memoryOptimizationExample() {
    const element = document.getElementById('memory-test');
    const handleClick = function() {
      console.log('点击事件处理');
    };
    
    element.addEventListener('click', handleClick);
    
    // 当元素不再需要时，移除事件监听器
    // element.removeEventListener('click', handleClick);
  }
  
  // 测试内存优化
  memoryLeakExample();
  memoryOptimizationExample();
  console.log('内存优化示例完成');
}

// 5. 图片优化示例
function imageOptimization() {
  console.log('\n=== 图片优化示例 ===');
  
  // 懒加载图片
  function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.classList.remove('lazy');
          imageObserver.unobserve(img);
          console.log('图片懒加载完成:', img.src);
        }
      });
    });
    
    images.forEach(img => {
      imageObserver.observe(img);
    });
  }
  
  // 响应式图片
  function responsiveImages() {
    console.log('响应式图片示例:');
    console.log('<picture>');
    console.log('  <source media="(max-width: 768px)" srcset="small.jpg">');
    console.log('  <source media="(max-width: 1200px)" srcset="medium.jpg">');
    console.log('  <img src="large.jpg" alt="示例图片">');
    console.log('</picture>');
  }
  
  lazyLoadImages();
  responsiveImages();
}

// 6. 网络请求优化示例
function networkOptimization() {
  console.log('\n=== 网络请求优化示例 ===');
  
  // 优化前：多个独立请求
  function multipleRequests() {
    console.log('多个独立请求:');
    fetch('/api/data1')
      .then(response => response.json())
      .then(data => console.log('数据1:', data));
    
    fetch('/api/data2')
      .then(response => response.json())
      .then(data => console.log('数据2:', data));
    
    fetch('/api/data3')
      .then(response => response.json())
      .then(data => console.log('数据3:', data));
  }
  
  // 优化后：并行请求
  function parallelRequests() {
    console.log('并行请求:');
    Promise.all([
      fetch('/api/data1').then(response => response.json()),
      fetch('/api/data2').then(response => response.json()),
      fetch('/api/data3').then(response => response.json())
    ]).then(([data1, data2, data3]) => {
      console.log('数据1:', data1);
      console.log('数据2:', data2);
      console.log('数据3:', data3);
    });
  }
  
  // 缓存请求结果
  function cachedRequests() {
    console.log('缓存请求结果:');
    const cache = new Map();
    
    function fetchWithCache(url) {
      if (cache.has(url)) {
        console.log('从缓存获取数据:', url);
        return Promise.resolve(cache.get(url));
      }
      
      return fetch(url)
        .then(response => response.json())
        .then(data => {
          cache.set(url, data);
          console.log('从网络获取数据并缓存:', url);
          return data;
        });
    }
    
    fetchWithCache('/api/data1');
    // 第二次调用会从缓存获取
    setTimeout(() => {
      fetchWithCache('/api/data1');
    }, 1000);
  }
  
  multipleRequests();
  parallelRequests();
  cachedRequests();
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端性能优化示例...');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.id = 'container';
  container.style.height = '200px';
  container.style.border = '1px solid #ccc';
  container.style.padding = '10px';
  document.body.appendChild(container);
  
  const memoryTest = document.createElement('div');
  memoryTest.id = 'memory-test';
  memoryTest.textContent = '点击测试内存优化';
  memoryTest.style.padding = '10px';
  memoryTest.style.backgroundColor = '#f0f0f0';
  memoryTest.style.cursor = 'pointer';
  document.body.appendChild(memoryTest);
  
  // 创建懒加载图片示例
  for (let i = 0; i < 5; i++) {
    const img = document.createElement('img');
    img.dataset.src = `https://picsum.photos/200/300?random=${i}`;
    img.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="200" height="300"%3E%3C/svg%3E';
    img.className = 'lazy';
    img.style.width = '200px';
    img.style.height = '300px';
    img.style.margin = '10px';
    img.alt = `示例图片 ${i+1}`;
    document.body.appendChild(img);
  }
  
  // 执行示例
  monitorPerformance();
  domOptimization();
  debounceAndThrottle();
  memoryOptimization();
  imageOptimization();
  networkOptimization();
  
  console.log('前端性能优化示例执行完成！');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}