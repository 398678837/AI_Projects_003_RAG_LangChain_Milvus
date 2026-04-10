// 前端渲染优化示例

// 1. DOM操作优化示例
function domOperationOptimization() {
  console.log('=== DOM操作优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.id = 'container';
  container.style.border = '1px solid #ccc';
  container.style.padding = '10px';
  container.style.margin = '10px 0';
  document.body.appendChild(container);
  
  // 优化前：频繁操作DOM
  function unoptimizedDomOperation() {
    console.time('未优化的DOM操作');
    const container = document.getElementById('container');
    container.innerHTML = ''; // 清空容器
    for (let i = 0; i < 1000; i++) {
      container.innerHTML += `<div>${i}</div>`;
    }
    console.timeEnd('未优化的DOM操作');
  }
  
  // 优化后：使用innerHTML
  function optimizedDomOperationWithInnerHTML() {
    console.time('使用innerHTML的DOM操作');
    const container = document.getElementById('container');
    let html = '';
    for (let i = 0; i < 1000; i++) {
      html += `<div>${i}</div>`;
    }
    container.innerHTML = html;
    console.timeEnd('使用innerHTML的DOM操作');
  }
  
  // 优化后：使用DocumentFragment
  function optimizedDomOperationWithFragment() {
    console.time('使用DocumentFragment的DOM操作');
    const container = document.getElementById('container');
    container.innerHTML = ''; // 清空容器
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
    
    setTimeout(() => {
      optimizedDomOperationWithInnerHTML();
      
      setTimeout(() => {
        optimizedDomOperationWithFragment();
      }, 100);
    }, 100);
  }, 100);
  
  console.log('DOM操作优化示例准备就绪');
}

// 2. 避免重排和重绘示例
function avoidRepaintAndReflow() {
  console.log('\n=== 避免重排和重绘示例 ===');
  
  // 创建测试元素
  const element = document.createElement('div');
  element.id = 'test-element';
  element.style.width = '100px';
  element.style.height = '100px';
  element.style.backgroundColor = 'red';
  element.style.position = 'relative';
  element.style.margin = '10px 0';
  document.body.appendChild(element);
  
  // 优化前：频繁修改样式
  function unoptimizedStyleChanges() {
    console.time('未优化的样式修改');
    const element = document.getElementById('test-element');
    for (let i = 0; i < 100; i++) {
      element.style.left = i + 'px';
      element.style.top = i + 'px';
    }
    console.timeEnd('未优化的样式修改');
  }
  
  // 优化后：批量修改样式
  function optimizedStyleChanges() {
    console.time('优化的样式修改');
    const element = document.getElementById('test-element');
    element.style.cssText = 'left: 100px; top: 100px;';
    console.timeEnd('优化的样式修改');
  }
  
  // 优化后：使用transform
  function optimizedWithTransform() {
    console.time('使用transform的样式修改');
    const element = document.getElementById('test-element');
    element.style.transform = 'translate(150px, 150px)';
    console.timeEnd('使用transform的样式修改');
  }
  
  // 测试样式修改性能
  setTimeout(() => {
    unoptimizedStyleChanges();
    
    setTimeout(() => {
      optimizedStyleChanges();
      
      setTimeout(() => {
        optimizedWithTransform();
      }, 100);
    }, 100);
  }, 100);
  
  console.log('避免重排和重绘示例准备就绪');
}

// 3. CSS优化示例
function cssOptimization() {
  console.log('\n=== CSS优化示例 ===');
  
  // 创建测试元素
  const container = document.createElement('div');
  container.className = 'container';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加子元素
  for (let i = 0; i < 10; i++) {
    const item = document.createElement('div');
    item.className = 'item';
    item.innerHTML = `<a href="#" class="link">Link ${i+1}</a>`;
    container.appendChild(item);
  }
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    /* 优化前：复杂选择器 */
    div.container > div.item > a.link {
      color: blue;
      text-decoration: none;
    }
    
    /* 优化后：简单选择器 */
    .container-link {
      color: red;
      text-decoration: none;
    }
    
    /* 使用CSS变量 */
    :root {
      --primary-color: #3498db;
      --secondary-color: #2ecc71;
    }
    
    .variable-example {
      color: var(--primary-color);
      background-color: var(--secondary-color);
      padding: 10px;
      margin: 10px 0;
    }
    
    /* 优化CSS动画 */
    .animate {
      width: 100px;
      height: 100px;
      background-color: red;
      transition: transform 0.3s ease;
    }
    
    .animate:hover {
      transform: scale(1.1);
    }
  `;
  document.head.appendChild(style);
  
  // 添加CSS变量示例
  const variableExample = document.createElement('div');
  variableExample.className = 'variable-example';
  variableExample.textContent = 'CSS变量示例';
  document.body.appendChild(variableExample);
  
  // 添加动画示例
  const animateExample = document.createElement('div');
  animateExample.className = 'animate';
  document.body.appendChild(animateExample);
  
  console.log('CSS优化示例准备就绪');
  console.log('查看页面中的链接颜色和动画效果');
}

// 4. JavaScript执行优化示例
function javascriptExecutionOptimization() {
  console.log('\n=== JavaScript执行优化示例 ===');
  
  // 优化前：阻塞主线程
  function heavyCalculation() {
    console.time('同步计算');
    let result = 0;
    for (let i = 0; i < 100000000; i++) {
      result += i;
    }
    console.timeEnd('同步计算');
    console.log('计算结果:', result);
  }
  
  // 优化后：使用Web Worker
  function optimizedCalculation() {
    console.time('Web Worker计算');
    
    // 创建Web Worker
    const workerCode = `
      self.onmessage = function(e) {
        let result = 0;
        for (let i = 0; i < 100000000; i++) {
          result += i;
        }
        self.postMessage(result);
      };
    `;
    
    const blob = new Blob([workerCode], { type: 'application/javascript' });
    const worker = new Worker(URL.createObjectURL(blob));
    
    worker.onmessage = function(e) {
      console.timeEnd('Web Worker计算');
      console.log('Web Worker计算结果:', e.data);
      worker.terminate();
    };
    
    worker.postMessage('start');
  }
  
  // 优化前：使用setTimeout进行动画
  function unoptimizedAnimation() {
    const element = document.createElement('div');
    element.id = 'animation-element';
    element.style.width = '50px';
    element.style.height = '50px';
    element.style.backgroundColor = 'blue';
    element.style.position = 'absolute';
    element.style.left = '0';
    element.style.top = '200px';
    document.body.appendChild(element);
    
    console.log('开始setTimeout动画');
    let position = 0;
    function move() {
      position += 1;
      element.style.left = position + 'px';
      if (position < 300) {
        setTimeout(move, 16);
      } else {
        console.log('setTimeout动画结束');
      }
    }
    move();
  }
  
  // 优化后：使用requestAnimationFrame
  function optimizedAnimation() {
    const element = document.createElement('div');
    element.id = 'optimized-animation-element';
    element.style.width = '50px';
    element.style.height = '50px';
    element.style.backgroundColor = 'green';
    element.style.position = 'absolute';
    element.style.left = '0';
    element.style.top = '250px';
    document.body.appendChild(element);
    
    console.log('开始requestAnimationFrame动画');
    let position = 0;
    function move() {
      position += 1;
      element.style.left = position + 'px';
      if (position < 300) {
        requestAnimationFrame(move);
      } else {
        console.log('requestAnimationFrame动画结束');
      }
    }
    move();
  }
  
  // 测试JavaScript执行性能
  setTimeout(() => {
    heavyCalculation();
    
    setTimeout(() => {
      optimizedCalculation();
    }, 100);
  }, 100);
  
  // 测试动画性能
  setTimeout(() => {
    unoptimizedAnimation();
    
    setTimeout(() => {
      optimizedAnimation();
    }, 100);
  }, 1000);
  
  console.log('JavaScript执行优化示例准备就绪');
}

// 5. 事件委托示例
function eventDelegation() {
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
  
  // 优化前：为每个按钮添加事件监听器
  function unoptimizedEventListeners() {
    console.time('为每个按钮添加事件监听器');
    const buttons = document.querySelectorAll('.item-button');
    buttons.forEach((button, index) => {
      button.addEventListener('click', () => {
        console.log(`Button ${index+1} clicked`);
      });
    });
    console.timeEnd('为每个按钮添加事件监听器');
  }
  
  // 优化后：使用事件委托
  function optimizedEventDelegation() {
    console.time('使用事件委托');
    const container = document.getElementById('event-container');
    container.addEventListener('click', (e) => {
      if (e.target.classList.contains('item-button')) {
        console.log(`${e.target.textContent} clicked`);
      }
    });
    console.timeEnd('使用事件委托');
  }
  
  // 测试事件监听器性能
  setTimeout(() => {
    unoptimizedEventListeners();
    
    setTimeout(() => {
      optimizedEventDelegation();
    }, 100);
  }, 100);
  
  console.log('事件委托示例准备就绪');
  console.log('点击按钮查看控制台输出');
}

// 6. 虚拟DOM原理示例
function virtualDomExample() {
  console.log('\n=== 虚拟DOM原理示例 ===');
  
  // 简单的虚拟DOM实现
  function createElement(type, props, ...children) {
    return {
      type,
      props: {
        ...props,
        children: children.map(child => 
          typeof child === 'object' ? child : createTextElement(child)
        )
      }
    };
  }
  
  function createTextElement(text) {
    return {
      type: 'TEXT_ELEMENT',
      props: {
        nodeValue: text,
        children: []
      }
    };
  }
  
  function render(element, container) {
    const dom = element.type === 'TEXT_ELEMENT' 
      ? document.createTextNode('')
      : document.createElement(element.type);
    
    Object.keys(element.props).forEach(key => {
      if (key !== 'children') {
        dom[key] = element.props[key];
      }
    });
    
    element.props.children.forEach(child => {
      render(child, dom);
    });
    
    container.appendChild(dom);
  }
  
  // 测试虚拟DOM
  const element = createElement(
    'div',
    { style: 'padding: 20px; border: 1px solid #ccc;' },
    createElement('h2', null, '虚拟DOM示例'),
    createElement('p', null, '这是一个简单的虚拟DOM实现示例'),
    createElement('button', { onclick: () => console.log('Button clicked') }, 'Click Me')
  );
  
  const container = document.createElement('div');
  container.id = 'virtual-dom-container';
  document.body.appendChild(container);
  
  render(element, container);
  
  console.log('虚拟DOM原理示例准备就绪');
  console.log('查看页面中的虚拟DOM示例');
}

// 7. 渲染性能监控示例
function renderingPerformanceMonitoring() {
  console.log('\n=== 渲染性能监控示例 ===');
  
  // 使用Performance API监控渲染性能
  function monitorRenderingPerformance() {
    // 监控布局和绘制
    const observer = new PerformanceObserver((list) => {
      list.getEntries().forEach((entry) => {
        if (entry.entryType === 'layout-shift') {
          console.log('布局偏移:', entry.value);
        } else if (entry.entryType === 'paint') {
          console.log(`${entry.name}:`, entry.startTime, 'ms');
        }
      });
    });
    
    observer.observe({ entryTypes: ['layout-shift', 'paint'] });
    
    // 监控长任务
    const longTaskObserver = new PerformanceObserver((list) => {
      list.getEntries().forEach((entry) => {
        console.log('长任务:', entry.duration, 'ms');
      });
    });
    
    longTaskObserver.observe({ entryTypes: ['longtask'] });
  }
  
  monitorRenderingPerformance();
  
  // 创建一个长任务
  function createLongTask() {
    console.log('开始长任务');
    let result = 0;
    for (let i = 0; i < 1000000000; i++) {
      result += i;
    }
    console.log('长任务结束');
  }
  
  // 延迟执行长任务
  setTimeout(createLongTask, 2000);
  
  console.log('渲染性能监控示例准备就绪');
  console.log('查看控制台中的性能监控输出');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端渲染优化示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  domOperationOptimization();
  avoidRepaintAndReflow();
  cssOptimization();
  javascriptExecutionOptimization();
  eventDelegation();
  virtualDomExample();
  renderingPerformanceMonitoring();
  
  console.log('前端渲染优化示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}