# 图片优化

## 什么是图片优化？

图片优化是指通过各种技术和策略，减少图片文件大小，提高图片加载速度，同时保持图片质量的过程。图片优化是前端性能优化的重要组成部分，直接影响页面的加载速度和用户体验。

## 图片优化的重要性

1. **加载速度**：优化的图片加载速度更快，提高页面加载速度。
2. **带宽成本**：优化的图片文件大小更小，减少带宽使用，降低服务器成本。
3. **用户体验**：更快的图片加载速度提供更好的用户体验。
4. **SEO**：页面加载速度是SEO的重要因素，图片优化有助于提高网站排名。

## 图片优化的技术和策略

### 1. 选择合适的图片格式

- **JPEG**：适用于照片和复杂图像，支持有损压缩。
- **PNG**：适用于图标和简单图像，支持无损压缩和透明背景。
- **WebP**：谷歌开发的现代图片格式，提供更好的压缩率。
- **SVG**：适用于矢量图形，支持无损缩放。
- **AVIF**：新一代图片格式，提供比WebP更好的压缩率。

### 2. 图片压缩

- **有损压缩**：通过减少图片质量来减少文件大小，适用于照片。
- **无损压缩**：在不影响图片质量的情况下减少文件大小，适用于图标和简单图像。
- **工具推荐**：TinyPNG、ImageOptim、Squoosh等。

### 3. 响应式图片

- **使用srcset**：根据设备像素密度和屏幕尺寸提供不同大小的图片。
- **使用picture元素**：根据设备特性提供不同格式和大小的图片。
- **使用sizes属性**：指定图片在不同屏幕尺寸下的显示大小。

### 4. 图片懒加载

- **传统懒加载**：使用JavaScript监听滚动事件，当图片进入视口时加载。
- **原生懒加载**：使用loading="lazy"属性实现图片懒加载。
- **Intersection Observer API**：使用Intersection Observer API实现更高效的懒加载。

### 5. 图片CDN

- **使用CDN**：将图片存储在CDN上，减少网络延迟。
- **CDN图片处理**：使用CDN的图片处理服务，如调整大小、裁剪、格式转换等。

### 6. 图片预加载

- **预加载关键图片**：使用preload或prefetch预加载关键图片。
- **预连接CDN**：使用preconnect预连接到图片CDN，减少DNS解析时间。

### 7. 图片占位符

- **低质量占位符**：使用低质量的图片作为占位符，提高用户体验。
- **SVG占位符**：使用SVG作为占位符，减少占位符大小。
- **骨架屏**：使用骨架屏作为占位符，提供更好的用户体验。

## 图片优化的最佳实践

### 1. 选择合适的图片格式

- **照片**：使用JPEG或WebP格式，适当调整压缩质量。
- **图标和简单图像**：使用PNG或SVG格式。
- **需要透明背景的图像**：使用PNG或WebP格式。
- **矢量图形**：使用SVG格式。

### 2. 压缩图片

- **使用工具压缩**：使用TinyPNG、ImageOptim等工具压缩图片。
- **调整压缩质量**：根据图片用途调整压缩质量，平衡文件大小和图片质量。
- **批量压缩**：批量压缩多张图片，提高效率。

### 3. 使用响应式图片

- **使用srcset和sizes**：为不同设备提供合适大小的图片。
- **使用picture元素**：为不同设备提供不同格式的图片。
- **测试不同设备**：在不同设备上测试图片显示效果。

### 4. 实现图片懒加载

- **使用原生懒加载**：在支持的浏览器中使用loading="lazy"属性。
- **使用Intersection Observer**：在不支持原生懒加载的浏览器中使用Intersection Observer API。
- **设置合适的占位符**：使用低质量图片或SVG作为占位符。

### 5. 使用图片CDN

- **选择合适的CDN**：根据目标用户分布选择合适的CDN。
- **使用CDN图片处理**：利用CDN的图片处理服务，如调整大小、裁剪等。
- **配置CDN缓存**：合理配置CDN缓存策略，提高缓存命中率。

### 6. 优化图片加载顺序

- **预加载关键图片**：使用preload预加载首屏所需的图片。
- **延迟加载非关键图片**：使用懒加载延迟加载非首屏图片。
- **合理安排图片请求**：避免同时请求过多图片，影响页面加载速度。

## 示例代码

### 1. 响应式图片示例

```html
<!-- 使用srcset和sizes -->
<img 
  src="small.jpg" 
  srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w" 
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px" 
  alt="Example image"
>

<!-- 使用picture元素 -->
<picture>
  <source media="(max-width: 600px)" srcset="small.webp" type="image/webp">
  <source media="(max-width: 600px)" srcset="small.jpg" type="image/jpeg">
  <source media="(max-width: 1200px)" srcset="medium.webp" type="image/webp">
  <source media="(max-width: 1200px)" srcset="medium.jpg" type="image/jpeg">
  <source srcset="large.webp" type="image/webp">
  <img src="large.jpg" alt="Example image">
</picture>
```

### 2. 图片懒加载示例

```html
<!-- 原生懒加载 -->
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="Lazy loaded image">

<!-- 使用Intersection Observer的懒加载 -->
<img src="placeholder.jpg" data-src="actual-image.jpg" class="lazy" alt="Lazy loaded image">

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const lazyImages = document.querySelectorAll('.lazy');
    
    if ('IntersectionObserver' in window) {
      const imageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            const image = entry.target;
            image.src = image.dataset.src;
            image.classList.remove('lazy');
            imageObserver.unobserve(image);
          }
        });
      });
      
      lazyImages.forEach(function(image) {
        imageObserver.observe(image);
      });
    } else {
      // 回退方案
      let lazyImageCount = lazyImages.length;
      
      if (lazyImageCount > 0) {
        const lazyLoad = function() {
          if (window.pageYOffset + window.innerHeight > lazyImages[0].offsetTop) {
            let image = lazyImages[0];
            image.src = image.dataset.src;
            image.classList.remove('lazy');
            
            lazyImages = Array.prototype.slice.call(lazyImages, 1);
            
            if (lazyImages.length === 0) {
              document.removeEventListener('scroll', lazyLoad);
              window.removeEventListener('resize', lazyLoad);
              window.removeEventListener('orientationchange', lazyLoad);
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
  });
</script>
```

### 3. 图片预加载示例

```html
<!-- 预加载关键图片 -->
<link rel="preload" href="hero.jpg" as="image">

<!-- 预连接到图片CDN -->
<link rel="preconnect" href="https://cdn.example.com" crossorigin>

<!-- 预获取可能需要的图片 -->
<link rel="prefetch" href="next-page-image.jpg" as="image">
```

### 4. 图片CDN示例

```html
<!-- 使用CDN加载图片 -->
<img src="https://cdn.example.com/images/image.jpg" alt="CDN image">

<!-- 使用CDN图片处理 -->
<img src="https://cdn.example.com/images/image.jpg?w=800&h=600&format=webp" alt="Processed CDN image">
```

### 5. 图片占位符示例

```html
<!-- 低质量占位符 -->
<img 
  src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAA..." 
  data-src="actual-image.jpg" 
  class="lazy" 
  alt="Image with placeholder"
>

<!-- SVG占位符 -->
<img 
  src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'/%3E" 
  data-src="actual-image.jpg" 
  class="lazy" 
  alt="Image with SVG placeholder"
>

<!-- 骨架屏 -->
<div class="image-skeleton">
  <img src="actual-image.jpg" data-src="actual-image.jpg" class="lazy" alt="Image with skeleton">
</div>

<style>
  .image-skeleton {
    width: 400px;
    height: 300px;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: skeleton-loading 1.5s infinite;
  }
  
  @keyframes skeleton-loading {
    0% {
      background-position: 200% 0;
    }
    100% {
      background-position: -200% 0;
    }
  }
  
  .image-skeleton img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>
```

## 图片优化工具

### 1. 图片压缩工具

- **TinyPNG**：在线压缩PNG和JPEG图片。
- **ImageOptim**：Mac上的图片压缩工具。
- **Squoosh**：谷歌开发的在线图片压缩工具，支持多种格式。
- **imagemin**：Node.js图片压缩库，可集成到构建流程中。
- **Sharp**：Node.js图片处理库，支持调整大小、格式转换等。

### 2. 图片CDN服务

- **Cloudinary**：提供图片处理和CDN服务。
- **Imgix**：提供图片处理和CDN服务。
- **AWS CloudFront**：亚马逊提供的CDN服务。
- **Cloudflare**：提供CDN服务，支持图片优化。
- **七牛云**：国内的图片CDN服务。

### 3. 图片格式转换工具

- **Squoosh**：在线图片格式转换工具。
- **cwebp**：Google提供的WebP转换工具。
- **avifenc**：AVIF格式转换工具。

### 4. 性能分析工具

- **Lighthouse**：分析页面性能，包括图片优化建议。
- **Google PageSpeed Insights**：分析页面性能，包括图片优化建议。
- **WebPageTest**：提供详细的性能测试报告，包括图片加载时间。

## 学习资源

- [Responsive Images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
- [Lazy Loading](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API/Lazy_loading_images)
- [WebP](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types#webp)
- [AVIF](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types#avif)
- [Image Optimization](https://web.dev/optimize-images/)
- [Preload Critical Assets](https://web.dev/preload-critical-assets/)