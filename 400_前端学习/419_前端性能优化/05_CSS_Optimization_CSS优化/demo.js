// 前端CSS优化示例

// 1. CSS选择器优化示例
function cssSelectorOptimization() {
  console.log('=== CSS选择器优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'container';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加子元素
  for (let i = 0; i < 5; i++) {
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
    
    /* 优化前：过度限定 */
    .container .item .link {
      font-size: 14px;
    }
    
    /* 优化后：简化选择器 */
    .item-link {
      font-size: 16px;
    }
    
    /* 直接子选择器示例 */
    .container > .item {
      margin: 10px 0;
    }
  `;
  document.head.appendChild(style);
  
  // 修改链接类名，应用优化后的选择器
  const links = container.querySelectorAll('.link');
  links.forEach((link, index) => {
    link.classList.add('container-link');
    if (index % 2 === 0) {
      link.classList.add('item-link');
    }
  });
  
  console.log('CSS选择器优化示例准备就绪');
  console.log('查看页面中的链接样式');
}

// 2. CSS代码优化示例
function cssCodeOptimization() {
  console.log('\n=== CSS代码优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'code-optimization';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试元素
  const box1 = document.createElement('div');
  box1.className = 'box box1';
  box1.textContent = 'Box 1';
  container.appendChild(box1);
  
  const box2 = document.createElement('div');
  box2.className = 'box box2';
  box2.textContent = 'Box 2';
  container.appendChild(box2);
  
  const box3 = document.createElement('div');
  box3.className = 'box box3';
  box3.textContent = 'Box 3';
  container.appendChild(box3);
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    /* 使用CSS变量 */
    :root {
      --primary-color: #3498db;
      --secondary-color: #2ecc71;
      --margin: 10px;
      --padding: 15px;
      --border-radius: 5px;
    }
    
    /* 优化前：重复代码 */
    .box1 {
      margin-top: 10px;
      margin-right: 10px;
      margin-bottom: 10px;
      margin-left: 10px;
      padding-top: 15px;
      padding-right: 15px;
      padding-bottom: 15px;
      padding-left: 15px;
      border-radius: 5px;
      background-color: #3498db;
      color: white;
    }
    
    /* 优化后：使用简写属性和CSS变量 */
    .box {
      margin: var(--margin);
      padding: var(--padding);
      border-radius: var(--border-radius);
      color: white;
    }
    
    .box2 {
      background-color: var(--primary-color);
    }
    
    .box3 {
      background-color: var(--secondary-color);
    }
  `;
  document.head.appendChild(style);
  
  console.log('CSS代码优化示例准备就绪');
  console.log('查看页面中的盒子样式');
}

// 3. CSS动画优化示例
function cssAnimationOptimization() {
  console.log('\n=== CSS动画优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'animation-container';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  container.style.position = 'relative';
  container.style.height = '200px';
  
  // 添加测试元素
  const box1 = document.createElement('div');
  box1.className = 'animation-box box1';
  box1.textContent = 'Box 1 (position)';
  container.appendChild(box1);
  
  const box2 = document.createElement('div');
  box2.className = 'animation-box box2';
  box2.textContent = 'Box 2 (transform)';
  container.appendChild(box2);
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .animation-box {
      width: 100px;
      height: 100px;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      position: absolute;
      top: 50px;
    }
    
    .box1 {
      background-color: #e74c3c;
      left: 0;
      /* 优化前：使用position进行动画 */
      animation: movePosition 2s ease infinite alternate;
    }
    
    .box2 {
      background-color: #3498db;
      left: 300px;
      /* 优化后：使用transform进行动画 */
      animation: moveTransform 2s ease infinite alternate;
      will-change: transform;
    }
    
    @keyframes movePosition {
      from {
        left: 0;
      }
      to {
        left: 200px;
      }
    }
    
    @keyframes moveTransform {
      from {
        transform: translateX(0);
      }
      to {
        transform: translateX(200px);
      }
    }
  `;
  document.head.appendChild(style);
  
  console.log('CSS动画优化示例准备就绪');
  console.log('查看页面中的动画效果');
  console.log('Box 1 使用position动画，Box 2 使用transform动画，后者性能更好');
}

// 4. CSS加载优化示例
function cssLoadingOptimization() {
  console.log('\n=== CSS加载优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'loading-optimization';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试元素
  const header = document.createElement('div');
  header.className = 'header';
  header.textContent = 'Header (关键CSS)';
  container.appendChild(header);
  
  const content = document.createElement('div');
  content.className = 'content';
  content.textContent = 'Content (非关键CSS)';
  container.appendChild(content);
  
  const footer = document.createElement('div');
  footer.className = 'footer';
  footer.textContent = 'Footer (异步加载CSS)';
  container.appendChild(footer);
  
  document.body.appendChild(container);
  
  // 内联关键CSS
  const criticalStyle = document.createElement('style');
  criticalStyle.textContent = `
    /* 内联关键CSS */
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
    }
    
    .header {
      background-color: #333;
      color: white;
      padding: 20px;
      margin: 10px 0;
    }
  `;
  document.head.appendChild(criticalStyle);
  
  // 异步加载非关键CSS
  const nonCriticalStyle = document.createElement('link');
  nonCriticalStyle.rel = 'stylesheet';
  nonCriticalStyle.href = 'data:text/css, .content { padding: 20px; margin: 10px 0; background-color: #f0f0f0; } .footer { padding: 20px; margin: 10px 0; background-color: #e0e0e0; }';
  nonCriticalStyle.media = 'print';
  nonCriticalStyle.onload = function() {
    this.media = 'all';
    console.log('非关键CSS加载完成');
  };
  document.head.appendChild(nonCriticalStyle);
  
  console.log('CSS加载优化示例准备就绪');
  console.log('查看页面中的样式效果');
  console.log('Header使用内联CSS，Content和Footer使用异步加载的CSS');
}

// 5. CSS架构优化示例
function cssArchitectureOptimization() {
  console.log('\n=== CSS架构优化示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'architecture-optimization';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加BEM命名规范示例
  const header = document.createElement('div');
  header.className = 'header';
  header.innerHTML = `
    <div class="header__logo">Logo</div>
    <nav class="header__nav">
      <ul class="header__nav-list">
        <li class="header__nav-item header__nav-item--active">Home</li>
        <li class="header__nav-item">About</li>
        <li class="header__nav-item">Contact</li>
      </ul>
    </nav>
  `;
  container.appendChild(header);
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    /* BEM命名规范示例 */
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
      background-color: #f8f9fa;
      border-bottom: 1px solid #dee2e6;
    }
    
    .header__logo {
      font-size: 24px;
      font-weight: bold;
      color: #3498db;
    }
    
    .header__nav {
      display: flex;
    }
    
    .header__nav-list {
      display: flex;
      list-style: none;
      margin: 0;
      padding: 0;
    }
    
    .header__nav-item {
      margin: 0 10px;
      padding: 5px 10px;
      cursor: pointer;
    }
    
    .header__nav-item--active {
      color: #3498db;
      border-bottom: 2px solid #3498db;
    }
  `;
  document.head.appendChild(style);
  
  console.log('CSS架构优化示例准备就绪');
  console.log('查看页面中的BEM命名规范示例');
}

// 6. CSS性能监控示例
function cssPerformanceMonitoring() {
  console.log('\n=== CSS性能监控示例 ===');
  
  // 创建测试按钮
  const button = document.createElement('button');
  button.textContent = '测试CSS性能';
  button.style.padding = '10px';
  button.style.margin = '10px';
  document.body.appendChild(button);
  
  // 测试CSS选择器性能
  button.addEventListener('click', () => {
    console.log('测试CSS选择器性能:');
    
    // 创建测试元素
    const container = document.createElement('div');
    container.id = 'test-container';
    
    for (let i = 0; i < 1000; i++) {
      const div = document.createElement('div');
      div.className = 'test-item';
      div.innerHTML = `<span class="test-span">Item ${i+1}</span>`;
      container.appendChild(div);
    }
    
    document.body.appendChild(container);
    
    // 测试不同选择器的性能
    console.time('ID选择器');
    for (let i = 0; i < 10000; i++) {
      document.getElementById('test-container');
    }
    console.timeEnd('ID选择器');
    
    console.time('类选择器');
    for (let i = 0; i < 10000; i++) {
      document.getElementsByClassName('test-item');
    }
    console.timeEnd('类选择器');
    
    console.time('标签选择器');
    for (let i = 0; i < 10000; i++) {
      document.getElementsByTagName('div');
    }
    console.timeEnd('标签选择器');
    
    console.time('后代选择器');
    for (let i = 0; i < 10000; i++) {
      document.querySelectorAll('.test-item .test-span');
    }
    console.timeEnd('后代选择器');
    
    // 清理测试元素
    document.body.removeChild(container);
  });
  
  console.log('CSS性能监控示例准备就绪');
  console.log('点击按钮测试不同CSS选择器的性能');
}

// 7. CSS变量示例
function cssVariablesExample() {
  console.log('\n=== CSS变量示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'variables-example';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试元素
  const box1 = document.createElement('div');
  box1.className = 'variable-box box1';
  box1.textContent = 'Box 1';
  container.appendChild(box1);
  
  const box2 = document.createElement('div');
  box2.className = 'variable-box box2';
  box2.textContent = 'Box 2';
  container.appendChild(box2);
  
  const button = document.createElement('button');
  button.textContent = '切换主题';
  button.style.padding = '10px';
  button.style.margin = '10px 0';
  container.appendChild(button);
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    /* 定义CSS变量 */
    :root {
      --primary-color: #3498db;
      --secondary-color: #2ecc71;
      --background-color: #f8f9fa;
      --text-color: #333;
      --padding: 20px;
      --border-radius: 5px;
    }
    
    /* 深色主题变量 */
    .dark-theme {
      --primary-color: #9b59b6;
      --secondary-color: #1abc9c;
      --background-color: #34495e;
      --text-color: #ecf0f1;
    }
    
    .variable-box {
      padding: var(--padding);
      border-radius: var(--border-radius);
      margin: 10px 0;
      color: var(--text-color);
    }
    
    .box1 {
      background-color: var(--primary-color);
    }
    
    .box2 {
      background-color: var(--secondary-color);
    }
    
    body {
      background-color: var(--background-color);
      color: var(--text-color);
      transition: background-color 0.3s ease, color 0.3s ease;
    }
  `;
  document.head.appendChild(style);
  
  // 切换主题
  button.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    console.log('主题已切换');
  });
  
  console.log('CSS变量示例准备就绪');
  console.log('点击按钮切换主题');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端CSS优化示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  cssSelectorOptimization();
  cssCodeOptimization();
  cssAnimationOptimization();
  cssLoadingOptimization();
  cssArchitectureOptimization();
  cssPerformanceMonitoring();
  cssVariablesExample();
  
  console.log('前端CSS优化示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}