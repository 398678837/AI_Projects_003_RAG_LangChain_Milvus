// 前端图片优化示例

// 1. 响应式图片示例
function responsiveImagesExample() {
  console.log('=== 响应式图片示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'responsive-images';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>响应式图片示例</h2>
    <p>响应式图片可以根据设备像素密度和屏幕尺寸提供不同大小的图片，提高加载速度和用户体验。</p>
    
    <div class="image-container">
      <h3>使用srcset和sizes</h3>
      <img 
        src="https://picsum.photos/id/237/400/300" 
        srcset="https://picsum.photos/id/237/400/300 400w, https://picsum.photos/id/237/800/600 800w, https://picsum.photos/id/237/1200/900 1200w" 
        sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px" 
        alt="Responsive image"
        style="max-width: 100%; height: auto;"
      >
    </div>
    
    <div class="image-container">
      <h3>使用picture元素</h3>
      <picture>
        <source media="(max-width: 600px)" srcset="https://picsum.photos/id/238/400/300" type="image/jpeg">
        <source media="(max-width: 1200px)" srcset="https://picsum.photos/id/238/800/600" type="image/jpeg">
        <img src="https://picsum.photos/id/238/1200/900" alt="Picture element image" style="max-width: 100%; height: auto;">
      </picture>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .responsive-images {
      font-family: Arial, sans-serif;
    }
    
    .image-container {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .image-container h3 {
      margin-top: 0;
      color: #3498db;
    }
  `;
  document.head.appendChild(style);
  
  console.log('响应式图片示例准备就绪');
  console.log('查看页面中的响应式图片效果');
}

// 2. 图片懒加载示例
function lazyLoadingExample() {
  console.log('\n=== 图片懒加载示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'lazy-loading';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>图片懒加载示例</h2>
    <p>图片懒加载可以延迟加载非首屏图片，提高页面加载速度。</p>
    
    <div class="scroll-container" style="height: 400px; overflow-y: scroll; border: 1px solid #ddd; padding: 10px;">
      <div style="height: 1000px; padding: 20px;">
        <p>向下滚动查看懒加载图片...</p>
        
        <div class="image-container">
          <h3>原生懒加载</h3>
          <img 
            src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'/%3E" 
            data-src="https://picsum.photos/id/239/400/300" 
            loading="lazy" 
            alt="Native lazy loaded image"
            style="max-width: 100%; height: auto;"
          >
        </div>
        
        <div class="image-container">
          <h3>Intersection Observer懒加载</h3>
          <img 
            src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'/%3E" 
            data-src="https://picsum.photos/id/240/400/300" 
            class="lazy" 
            alt="Intersection Observer lazy loaded image"
            style="max-width: 100%; height: auto;"
          >
        </div>
        
        <div class="image-container">
          <h3>带占位符的懒加载</h3>
          <div class="image-skeleton">
            <img 
              src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'/%3E" 
              data-src="https://picsum.photos/id/241/400/300" 
              class="lazy" 
              alt="Lazy loaded image with placeholder"
              style="max-width: 100%; height: 100%; object-fit: cover;"
            >
          </div>
        </div>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .lazy-loading {
      font-family: Arial, sans-serif;
    }
    
    .image-container {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .image-container h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .image-skeleton {
      width: 400px;
      height: 300px;
      background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
      background-size: 200% 100%;
      animation: skeleton-loading 1.5s infinite;
      position: relative;
      overflow: hidden;
    }
    
    @keyframes skeleton-loading {
      0% {
        background-position: 200% 0;
      }
      100% {
        background-position: -200% 0;
      }
    }
  `;
  document.head.appendChild(style);
  
  // 实现Intersection Observer懒加载
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          const image = entry.target;
          image.src = image.dataset.src;
          image.classList.remove('lazy');
          imageObserver.unobserve(image);
          console.log('懒加载图片已加载:', image.dataset.src);
        }
      });
    });
    
    const lazyImages = document.querySelectorAll('.lazy');
    lazyImages.forEach(function(image) {
      imageObserver.observe(image);
    });
  } else {
    // 回退方案
    let lazyImageCount = document.querySelectorAll('.lazy').length;
    
    if (lazyImageCount > 0) {
      const lazyLoad = function() {
        const lazyImages = document.querySelectorAll('.lazy');
        if (lazyImages.length > 0) {
          for (let i = 0; i < lazyImages.length; i++) {
            if (window.pageYOffset + window.innerHeight > lazyImages[i].offsetTop) {
              let image = lazyImages[i];
              image.src = image.dataset.src;
              image.classList.remove('lazy');
              console.log('懒加载图片已加载:', image.dataset.src);
            }
          }
        }
      };
      
      document.addEventListener('scroll', lazyLoad);
      window.addEventListener('resize', lazyLoad);
      window.addEventListener('orientationchange', lazyLoad);
      
      // 初始检查
      lazyLoad();
    }
  }
  
  console.log('图片懒加载示例准备就绪');
  console.log('向下滚动查看懒加载图片效果');
}

// 3. 图片压缩示例
function imageCompressionExample() {
  console.log('\n=== 图片压缩示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'image-compression';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>图片压缩示例</h2>
    <p>图片压缩可以减少图片文件大小，提高加载速度，同时保持图片质量。</p>
    
    <div class="compression-types">
      <div class="compression-type">
        <h3>原始图片</h3>
        <canvas id="original-image" width="400" height="300"></canvas>
        <p id="original-size">大小: 计算中...</p>
      </div>
      <div class="compression-type">
        <h3>压缩后图片</h3>
        <canvas id="compressed-image" width="400" height="300"></canvas>
        <p id="compressed-size">大小: 计算中...</p>
        <p id="compression-ratio">压缩率: 计算中...</p>
      </div>
    </div>
    
    <div class="compression-controls">
      <h3>压缩控制</h3>
      <label for="quality">压缩质量:</label>
      <input type="range" id="quality" min="0" max="1" step="0.1" value="0.5">
      <span id="quality-value">0.5</span>
      <button id="compress-btn">压缩图片</button>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .image-compression {
      font-family: Arial, sans-serif;
    }
    
    .compression-types {
      display: flex;
      gap: 20px;
      margin: 20px 0;
    }
    
    .compression-type {
      flex: 1;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
      text-align: center;
    }
    
    .compression-type h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    canvas {
      border: 1px solid #ddd;
      margin: 10px 0;
      max-width: 100%;
    }
    
    .compression-controls {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .compression-controls h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    #compress-btn {
      padding: 8px 16px;
      margin-top: 10px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #compress-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 绘制测试图片
  const originalCanvas = document.getElementById('original-image');
  const compressedCanvas = document.getElementById('compressed-image');
  const originalCtx = originalCanvas.getContext('2d');
  const compressedCtx = compressedCanvas.getContext('2d');
  
  // 绘制原图
  originalCtx.fillStyle = '#3498db';
  originalCtx.fillRect(0, 0, 400, 300);
  originalCtx.fillStyle = 'white';
  originalCtx.font = '24px Arial';
  originalCtx.textAlign = 'center';
  originalCtx.textBaseline = 'middle';
  originalCtx.fillText('Original Image', 200, 150);
  
  // 压缩图片
  const qualityInput = document.getElementById('quality');
  const qualityValue = document.getElementById('quality-value');
  const compressBtn = document.getElementById('compress-btn');
  const originalSizeEl = document.getElementById('original-size');
  const compressedSizeEl = document.getElementById('compressed-size');
  const compressionRatioEl = document.getElementById('compression-ratio');
  
  // 更新质量值
  qualityInput.addEventListener('input', () => {
    qualityValue.textContent = qualityInput.value;
  });
  
  // 压缩按钮点击事件
  compressBtn.addEventListener('click', () => {
    const quality = parseFloat(qualityInput.value);
    
    // 转换为base64
    const originalDataUrl = originalCanvas.toDataURL('image/png');
    const compressedDataUrl = originalCanvas.toDataURL('image/jpeg', quality);
    
    // 计算大小
    const originalSize = Math.round((originalDataUrl.length - 22) * 3 / 4); // 估算原始大小
    const compressedSize = Math.round((compressedDataUrl.length - 22) * 3 / 4); // 估算压缩后大小
    const compressionRatio = Math.round((1 - compressedSize / originalSize) * 100);
    
    // 显示大小信息
    originalSizeEl.textContent = `大小: ${originalSize} bytes`;
    compressedSizeEl.textContent = `大小: ${compressedSize} bytes`;
    compressionRatioEl.textContent = `压缩率: ${compressionRatio}%`;
    
    // 显示压缩后的图片
    const img = new Image();
    img.onload = () => {
      compressedCtx.drawImage(img, 0, 0, 400, 300);
    };
    img.src = compressedDataUrl;
    
    console.log('图片压缩测试：原始大小', originalSize, '压缩后大小', compressedSize, '压缩率', compressionRatio);
  });
  
  console.log('图片压缩示例准备就绪');
  console.log('调整压缩质量并点击压缩按钮查看效果');
}

// 4. 图片CDN示例
function imageCdnExample() {
  console.log('\n=== 图片CDN示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'image-cdn';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>图片CDN示例</h2>
    <p>图片CDN可以将图片存储在全球各地的边缘节点，减少网络延迟，提高加载速度。</p>
    
    <div class="cdn-examples">
      <div class="cdn-example">
        <h3>基础CDN图片</h3>
        <img src="https://picsum.photos/id/242/400/300" alt="CDN image" style="max-width: 100%; height: auto;">
        <p>https://picsum.photos/id/242/400/300</p>
      </div>
      
      <div class="cdn-example">
        <h3>CDN图片处理</h3>
        <img src="https://picsum.photos/id/243/400/300?blur=5" alt="CDN processed image" style="max-width: 100%; height: auto;">
        <p>https://picsum.photos/id/243/400/300?blur=5</p>
      </div>
      
      <div class="cdn-example">
        <h3>不同尺寸的CDN图片</h3>
        <div class="image-sizes">
          <img src="https://picsum.photos/id/244/100/75" alt="Small CDN image" style="margin: 5px;">
          <img src="https://picsum.photos/id/244/200/150" alt="Medium CDN image" style="margin: 5px;">
          <img src="https://picsum.photos/id/244/300/225" alt="Large CDN image" style="margin: 5px;">
        </div>
        <p>不同尺寸的图片</p>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .image-cdn {
      font-family: Arial, sans-serif;
    }
    
    .cdn-examples {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }
    
    .cdn-example {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .cdn-example h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    .cdn-example p {
      font-size: 12px;
      color: #666;
      word-break: break-all;
    }
    
    .image-sizes {
      display: flex;
      flex-wrap: wrap;
      margin: 10px 0;
    }
  `;
  document.head.appendChild(style);
  
  console.log('图片CDN示例准备就绪');
  console.log('查看页面中的CDN图片效果');
}

// 5. 图片预加载示例
function imagePreloadingExample() {
  console.log('\n=== 图片预加载示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'image-preloading';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>图片预加载示例</h2>
    <p>图片预加载可以提前加载关键图片，提高用户体验。</p>
    
    <div class="preload-examples">
      <div class="preload-example">
        <h3>预加载关键图片</h3>
        <img id="preloaded-image" src="https://picsum.photos/id/245/400/300" alt="Preloaded image" style="max-width: 100%; height: auto;">
        <p>使用link rel="preload"预加载</p>
      </div>
      
      <div class="preload-example">
        <h3>动态预加载</h3>
        <button id="preload-btn">预加载图片</button>
        <div id="preload-status" style="margin-top: 10px;">点击按钮预加载图片</div>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .image-preloading {
      font-family: Arial, sans-serif;
    }
    
    .preload-examples {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }
    
    .preload-example {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .preload-example h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    #preload-btn {
      padding: 8px 16px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #preload-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 添加预加载链接
  const preloadLink = document.createElement('link');
  preloadLink.rel = 'preload';
  preloadLink.href = 'https://picsum.photos/id/245/400/300';
  preloadLink.as = 'image';
  document.head.appendChild(preloadLink);
  
  // 动态预加载
  const preloadBtn = document.getElementById('preload-btn');
  const preloadStatus = document.getElementById('preload-status');
  
  preloadBtn.addEventListener('click', () => {
    preloadStatus.textContent = '正在预加载图片...';
    
    // 创建图片对象进行预加载
    const image = new Image();
    image.src = 'https://picsum.photos/id/246/400/300';
    
    image.onload = () => {
      preloadStatus.textContent = '图片预加载完成！';
      console.log('图片预加载完成');
    };
    
    image.onerror = () => {
      preloadStatus.textContent = '图片预加载失败';
      console.error('图片预加载失败');
    };
  });
  
  console.log('图片预加载示例准备就绪');
  console.log('查看页面中的图片预加载效果');
}

// 6. 图片格式示例
function imageFormatsExample() {
  console.log('\n=== 图片格式示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'image-formats';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>图片格式示例</h2>
    <p>不同的图片格式有不同的特点和适用场景。</p>
    
    <div class="format-examples">
      <div class="format-example">
        <h3>JPEG</h3>
        <p>适用于照片和复杂图像，支持有损压缩</p>
        <img src="https://picsum.photos/id/247/400/300" alt="JPEG image" style="max-width: 100%; height: auto;">
      </div>
      
      <div class="format-example">
        <h3>PNG</h3>
        <p>适用于图标和简单图像，支持无损压缩和透明背景</p>
        <img src="https://picsum.photos/id/248/400/300" alt="PNG image" style="max-width: 100%; height: auto;">
      </div>
      
      <div class="format-example">
        <h3>SVG</h3>
        <p>适用于矢量图形，支持无损缩放</p>
        <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
          <rect width="400" height="300" fill="#3498db"/>
          <text x="200" y="150" font-size="24" fill="white" text-anchor="middle" dominant-baseline="middle">SVG Example</text>
        </svg>
      </div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .image-formats {
      font-family: Arial, sans-serif;
    }
    
    .format-examples {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }
    
    .format-example {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .format-example h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    svg {
      margin: 10px 0;
      border: 1px solid #ddd;
    }
  `;
  document.head.appendChild(style);
  
  console.log('图片格式示例准备就绪');
  console.log('查看页面中的不同图片格式效果');
}

// 7. 图片性能监控示例
function imagePerformanceMonitoringExample() {
  console.log('\n=== 图片性能监控示例 ===');
  
  // 创建测试容器
  const container = document.createElement('div');
  container.className = 'image-performance';
  container.style.padding = '20px';
  container.style.margin = '10px 0';
  container.style.border = '1px solid #ccc';
  
  // 添加测试内容
  container.innerHTML = `
    <h2>图片性能监控示例</h2>
    <p>图片性能监控可以帮助我们了解图片加载的性能指标。</p>
    
    <div class="performance-test">
      <h3>测试图片加载性能</h3>
      <button id="performance-btn">测试图片加载性能</button>
      <div id="performance-result" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9;"></div>
    </div>
  `;
  
  document.body.appendChild(container);
  
  // 添加CSS样式
  const style = document.createElement('style');
  style.textContent = `
    .image-performance {
      font-family: Arial, sans-serif;
    }
    
    .performance-test {
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    
    .performance-test h3 {
      margin-top: 0;
      color: #3498db;
    }
    
    #performance-btn {
      padding: 8px 16px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #performance-btn:hover {
      background-color: #2980b9;
    }
  `;
  document.head.appendChild(style);
  
  // 测试图片加载性能
  const performanceBtn = document.getElementById('performance-btn');
  const performanceResult = document.getElementById('performance-result');
  
  performanceBtn.addEventListener('click', () => {
    console.log('测试图片加载性能');
    performanceResult.innerHTML = '<p>正在测试图片加载性能...</p>';
    
    // 清除之前的性能条目
    if (performance.clearResourceTimings) {
      performance.clearResourceTimings();
    }
    
    // 创建测试图片
    const testImages = [
      'https://picsum.photos/id/249/400/300',
      'https://picsum.photos/id/250/400/300',
      'https://picsum.photos/id/251/400/300'
    ];
    
    let loadedCount = 0;
    
    testImages.forEach((src, index) => {
      const img = new Image();
      img.src = src;
      
      img.onload = () => {
        loadedCount++;
        if (loadedCount === testImages.length) {
          // 所有图片加载完成，分析性能
          analyzeImagePerformance();
        }
      };
      
      img.onerror = () => {
        loadedCount++;
        if (loadedCount === testImages.length) {
          analyzeImagePerformance();
        }
      };
    });
    
    function analyzeImagePerformance() {
      if (performance.getEntriesByType) {
        const resourceEntries = performance.getEntriesByType('resource');
        const imageEntries = resourceEntries.filter(entry => entry.initiatorType === 'img');
        
        let html = '<h3>图片加载性能指标：</h3><ul>';
        
        imageEntries.forEach((entry, index) => {
          html += `
            <li>
              <strong>图片 ${index + 1}:</strong> ${entry.name}<br>
              加载时间: ${(entry.duration).toFixed(2)}ms<br>
              开始时间: ${(entry.startTime).toFixed(2)}ms<br>
              响应时间: ${(entry.responseEnd - entry.requestStart).toFixed(2)}ms
            </li>
          `;
        });
        
        html += '</ul>';
        performanceResult.innerHTML = html;
        console.log('图片性能测试：', imageEntries);
      } else {
        performanceResult.innerHTML = '<p>浏览器不支持Performance API</p>';
      }
    }
  });
  
  console.log('图片性能监控示例准备就绪');
  console.log('点击按钮测试图片加载性能');
}

// 执行所有示例
function runAllExamples() {
  console.log('开始执行前端图片优化示例...');
  
  // 创建示例容器
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  document.body.appendChild(container);
  
  // 执行示例
  responsiveImagesExample();
  lazyLoadingExample();
  imageCompressionExample();
  imageCdnExample();
  imagePreloadingExample();
  imageFormatsExample();
  imagePerformanceMonitoringExample();
  
  console.log('前端图片优化示例执行完成！');
  console.log('请查看控制台输出和页面效果。');
}

// 页面加载完成后执行示例
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', runAllExamples);
} else {
  runAllExamples();
}