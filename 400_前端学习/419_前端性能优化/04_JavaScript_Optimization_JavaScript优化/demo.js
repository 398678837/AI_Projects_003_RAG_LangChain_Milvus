// 前端JavaScript优化示例

// 1. Web Workers示例
function webWorkersExample() {
  console.log('=== Web Workers示例 ===');
  
  // 创建测试按钮
  const button = document.createElement('button');
  button.textContent = '使用Web Worker计算';
  button.style.padding = '10px';
  button.style.margin = '10px';
  document.body.appendChild(button);
  
  // 主线程代码
  button.addEventListener('click', () => {
    console.log('开始计算...');
    
    // 创建Web Worker
    const workerCode = `
      self.onmessage = function(e) {
        const { data } = e.data;
        console.log('Worker开始计算:', data);
        
        let result = 0;
        for (let i = 0; i < data; i++) {
          result += i;
        }
        
        console.log('Worker计算完成');
        self.postMessage(result);
      };
    `;
    
    const blob = new Blob([workerCode], { type: 'application/javascript' });
    const worker = new Worker(URL.createObjectURL(blob));
    
    worker.onmessage = function(e) {
      console.log('主线程收到结果:', e.data);
      worker.terminate();
    };
    
    worker.onerror = function(error) {
      console.error('Worker错误:', error);
      worker.terminate();
    };
    
    // 发送数据给Worker
    worker.postMessage({ data: 1000000000 });
    
    // 主线程继续执行
    console.log('主线程继续执行其他任务');
  });
  
  console.log('Web Workers示例准备就绪');
  console.log('点击按钮查看Web Worker计算效果');
}

// 2. 函数节流和防抖示例
function debounceAndThrottleExample() {
  console.log('\n=== 函数节流和防抖示例 ===');
  
  // 创建测试输入框
  const input = document.createElement('input');
  input.type = 'text';
  input.placeholder = '输入内容测试防抖';
  input.style.padding = '10px';
  input.style.margin = '10px';
  input.style.width = '300px';
  document.body.appendChild(input);
  
  // 创建测试按钮
  const button = document.createElement('button');
  button.textContent = '测试节流';
  button.style.padding = '10px';
  button.style.margin = '10px';
  document.body.appendChild(button);
  
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
  const debouncedSearch = debounce((query) => {
    console.log('防抖搜索:', query);
  }, 500);
  
  input.addEventListener('input', (e) => {
    debouncedSearch(e.target.value);
  });
  
  // 测试节流
  let clickCount = 0;
  const throttledClick = throttle(() => {
    clickCount++;
    console.log('节流点击:', clickCount);
  }, 1000);
  
  button.addEventListener('click', throttledClick);
  
  console.log('函数节流和防抖示例准备就绪');
  console.log('在输入框中输入内容测试防抖，快速点击按钮测试节流');
}

// 3. 内存管理示例
function memoryManagementExample() {
  console.log('\n=== 内存管理示例 ===');
  
  // 创建测试按钮
  const button1 = document.createElement('button');
  button1.textContent = '创建按钮（可能内存泄漏）';
  button1.style.padding = '10px';
  button1.style.margin = '10px';
  document.body.appendChild(button1);
  
  const button2 = document.createElement('button');
  button2.textContent = '创建按钮（优化内存）';
  button2.style.padding = '10px';
  button2.style.margin = '10px';
  document.body.appendChild(button2);
  
  const button3 = document.createElement('button');
  button3.textContent = '清理按钮';
  button3.style.padding = '10px';
  button3.style.margin = '10px';
  document.body.appendChild(button3);
  
  const buttons = [];
  
  // 优化前：可能导致内存泄漏
  button1.addEventListener('click', () => {
    const button = document.createElement('button');
    button.textContent = '测试按钮（可能内存泄漏）';
    button.style.padding = '5px';
    button.style.margin = '5px';
    
    // 闭包可能导致内存泄漏
    button.addEventListener('click', function() {
      console.log('按钮点击');
    });
    
    document.body.appendChild(button);
    buttons.push(button);
    console.log('创建了可能内存泄漏的按钮');
  });
  
  // 优化后：正确管理内存
  button2.addEventListener('click', () => {
    const button = document.createElement('button');
    button.textContent = '测试按钮（优化内存）';
    button.style.padding = '5px';
    button.style.margin = '5px';
    
    // 分离事件处理函数
    const handleClick = function() {
      console.log('按钮点击');
    };
    
    button.addEventListener('click', handleClick);
    button._handleClick = handleClick; // 存储事件处理函数引用
    
    document.body.appendChild(button);
    buttons.push(button);
    console.log('创建了优化内存的按钮');
  });
  
  // 清理按钮
  button3.addEventListener('click', () => {
    buttons.forEach(button => {
      // 移除事件监听器
      if (button._handleClick) {
        button.removeEventListener('click', button._handleClick);
      }
      // 从DOM中移除
      if (button.parentNode) {
        button.parentNode.removeChild(button);
      }
    });
    buttons.length = 0;
    console.log('清理了所有按钮');
  });
  
  // 使用WeakMap存储临时数据
  console.log('\n使用WeakMap存储临时数据:');
  const weakMap = new WeakMap();
  
  const obj1 = { id: 1 };
  const obj2 = { id: 2 };
  
  weakMap.set(obj1, '临时数据1');
  weakMap.set(obj2, '临时数据2');
  
  console.log('WeakMap中的数据:', weakMap.get(obj1), weakMap.get(obj2));
  
  // 当对象被垃圾回收时，WeakMap中的数据也会被自动清理
  obj1 = null;
  console.log('obj1设置为null后，WeakMap中的数据:', weakMap.get(obj1), weakMap.get(obj2));
  
  console.log('内存管理示例准备就绪');
  console.log('点击按钮创建测试按钮，然后点击清理按钮清理内存');
}

// 4. 代码优化示例
function codeOptimizationExample() {
  console.log('\n=== 代码优化示例 ===');
  
  // 创建测试按钮
  const button1 = document.createElement('button');
  button1.textContent = '测试循环优化';
  button1.style.padding = '10px';
  button1.style.margin = '10px';
  document.body.appendChild(button1);
  
  const button2 = document.createElement('button');
  button2.textContent = '测试数据结构优化';
  button2.style.padding = '10px';
  button2.style.margin = '10px';
  document.body.appendChild(button2);
  
  const button3 = document.createElement('button');
  button3.textContent = '测试缓存优化';
  button3.style.padding = '10px';
  button3.style.margin = '10px';
  document.body.appendChild(button3);
  
  // 测试循环优化
  button1.addEventListener('click', () => {
    console.log('测试循环优化:');
    
    const items = Array.from({ length: 1000000 }, (_, i) => i);
    
    // 优化前：普通for循环
    console.time('普通for循环');
    let sum1 = 0;
    for (let i = 0; i < items.length; i++) {
      sum1 += items[i];
    }
    console.timeEnd('普通for循环');
    
    // 优化后：缓存长度的for循环
    console.time('缓存长度的for循环');
    let sum2 = 0;
    const length = items.length;
    for (let i = 0; i < length; i++) {
      sum2 += items[i];
    }
    console.timeEnd('缓存长度的for循环');
    
    // 优化后：forEach循环
    console.time('forEach循环');
    let sum3 = 0;
    items.forEach(item => {
      sum3 += item;
    });
    console.timeEnd('forEach循环');
    
    // 优化后：reduce方法
    console.time('reduce方法');
    const sum4 = items.reduce((acc, item) => acc + item, 0);
    console.timeEnd('reduce方法');
  });
  
  // 测试数据结构优化
  button2.addEventListener('click', () => {
    console.log('测试数据结构优化:');
    
    // 创建测试数据
    const items = Array.from({ length: 1000000 }, (_, i) => ({
      id: i,
      name: `Item ${i}`
    }));
    
    // 测试1：使用数组查找
    console.time('使用数组查找');
    function findItemById(items, id) {
      for (let i = 0; i < items.length; i++) {
        if (items[i].id === id) {
          return items[i];
        }
      }
      return null;
    }
    findItemById(items, 999999);
    console.timeEnd('使用数组查找');
    
    // 测试2：使用Map查找
    console.time('使用Map查找');
    const itemMap = new Map();
    items.forEach(item => itemMap.set(item.id, item));
    
    function findItemByIdWithMap(id) {
      return itemMap.get(id);
    }
    findItemByIdWithMap(999999);
    console.timeEnd('使用Map查找');
  });
  
  // 测试缓存优化
  button3.addEventListener('click', () => {
    console.log('测试缓存优化:');
    
    // 模拟复杂计算
    function expensiveCalculation(a, b) {
      console.log('执行复杂计算');
      let result = 0;
      for (let i = 0; i < 1000000; i++) {
        result += Math.sin(a) * Math.cos(b);
      }
      return result;
    }
    
    // 优化前：每次都执行计算
    console.time('未缓存的计算');
    expensiveCalculation(1, 2);
    expensiveCalculation(1, 2); // 重复计算
    console.timeEnd('未缓存的计算');
    
    // 优化后：使用缓存
    console.time('缓存的计算');
    const cache = new Map();
    
    function cachedCalculation(a, b) {
      const key = `${a},${b}`;
      if (cache.has(key)) {
        console.log('从缓存获取结果');
        return cache.get(key);
      }
      
      const result = expensiveCalculation(a, b);
      cache.set(key, result);
      return result;
    }
    
    cachedCalculation(1, 2);
    cachedCalculation(1, 2); // 从缓存获取
    console.timeEnd('缓存的计算');
  });
  
  console.log('代码优化示例准备就绪');
  console.log('点击按钮测试不同的代码优化效果');
}

// 5. 模块优化示例
function moduleOptimizationExample() {
  console.log('\n=== 模块优化示例 ===');
  
  // 创建测试按钮
  const button = document.createElement('button');
  button.textContent = '加载模块';
  button.style.padding = '10px';
  button.style.margin = '10px';
  document.body.appendChild(button);
  
  // 动态导入模块
  button.addEventListener('click', () => {
    console.log('开始加载模块...');
    
    // 模拟动态导入
    const moduleCode = `
      export default function() {
        return '模块加载成功！';
      }
    `;
    
    // 创建一个Blob URL
    const blob = new Blob([moduleCode], { type: 'application/javascript' });
    const url = URL.createObjectURL(blob);
    
    // 动态导入
    import(url)
      .then(module => {
        console.log('模块加载完成:', module.default());
        URL.revokeObjectURL(url);
      })
      .catch(error => {
        console.error('模块加载失败:', error);
      });
  });
  
  // 代码分割示例
  console.log('代码分割示例:');
  console.log(`
// 使用动态导入进行代码分割
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <div>
      <h1>主应用</h1>
      <React.Suspense fallback={<div>加载中...</div>}>
        <LazyComponent />
      </React.Suspense>
    </div>
  );
}
  `);
  
  console.log('模块优化示例准备就绪');
  console.log('点击按钮测试动态导入模块');
}

// 6. 事件委托示例
function eventDelegationExample() {
  console.log('\n=== 事件委托示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.id = 'event-container';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加多个按钮
  for (let i = 0; i < 100; i++) {
    const button = document.createElement('button');
    button.className = 'item-button';
    button.textContent = `Button ${i+1}`;
    button.style.margin = '5px';
    button.style.padding = '5px 10px';
    container.appendChild(button);
  }
  
  document.body.appendChild(container);
  
  // 使用事件委托
  container.addEventListener('click', (e) => {
    if (e.target.classList.contains('item-button')) {
      console.log(`${e.target.textContent} clicked`);
    }
  });
  
  console.log('事件委托示例准备就绪');
  console.log('点击按钮查看控制台输出');
  console.log('事件委托可以减少事件监听器数量，提高性能');
}

// 7. requestAnimationFrame和requestIdleCallback示例
function requestAnimationFrameExample() {
  console.log('\n=== requestAnimationFrame和requestIdleCallback示例 ===');
  
  // 创建测试元素
  const element = document.createElement('div');
  element.id = 'animate-element';
  element.style.width = '50px';
  element.style.height = '50px';
  element.style.backgroundColor = 'red';
  element.style.position = 'absolute';
  element.style.left = '0';
  element.style.top = '400px';
  document.body.appendChild(element);
  
  // 使用requestAnimationFrame进行动画
  let position = 0;
  function animate() {
    position += 1;
    element.style.left = position + 'px';
    
    if (position < 300) {
      requestAnimationFrame(animate);
    } else {
      console.log('动画完成');
      
      // 使用requestIdleCallback执行非关键任务
      requestIdleCallback(() => {
        console.log('在浏览器空闲时执行非关键任务');
        // 这里可以执行一些非关键的计算或操作
      });
    }
  }
  
  // 开始动画
  setTimeout(() => {
    console.log('开始动画');
    animate();
  }, 1000);
  
  console.log('requestAnimationFrame和requestIdleCallback示例准备就绪');
  console.log('查看页面中的动画效果');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端JavaScript优化示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  webWorkersExample();
  debounceAndThrottleExample();
  memoryManagementExample();
  codeOptimizationExample();
  moduleOptimizationExample();
  eventDelegationExample();
  requestAnimationFrameExample();
  
  console.log('前端JavaScript优化示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}