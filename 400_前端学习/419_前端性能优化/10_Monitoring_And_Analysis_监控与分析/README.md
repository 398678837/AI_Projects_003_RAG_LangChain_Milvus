# 监控与分析

## 什么是监控与分析？

监控与分析是指通过各种工具和技术，实时监测前端应用的性能状态，收集性能数据，分析性能瓶颈，并提供优化建议的过程。监控与分析是前端性能优化的重要组成部分，帮助我们了解应用的实际性能表现，发现并解决性能问题。

## 监控与分析的重要性

1. **实时监测**：实时监测应用性能，及时发现性能问题。
2. **数据驱动**：基于真实数据进行性能优化，提高优化效果。
3. **性能瓶颈定位**：快速定位性能瓶颈，针对性地进行优化。
4. **用户体验改善**：通过分析用户体验数据，改善用户体验。
5. **持续优化**：建立性能监控体系，持续优化应用性能。

## 监控与分析的技术和策略

### 1. 性能指标监控

- **核心Web指标**：LCP（最大内容绘制）、FID（首次输入延迟）、CLS（累积布局偏移）。
- **传统Web指标**：TTFB（首字节时间）、DOMContentLoaded、onload。
- **用户体验指标**：FCP（首次内容绘制）、TTI（可交互时间）、TBT（总阻塞时间）。

### 2. 前端监控

- **错误监控**：捕获和监控JavaScript错误、资源加载错误等。
- **性能监控**：监控页面加载性能、渲染性能、网络性能等。
- **用户行为监控**：监控用户点击、页面浏览、停留时间等。
- **自定义监控**：根据业务需求自定义监控指标。

### 3. 分析工具

- **浏览器开发工具**：Chrome DevTools、Firefox Developer Tools等。
- **性能分析工具**：Lighthouse、WebPageTest、Google PageSpeed Insights等。
- **监控平台**：New Relic、Datadog、Sentry、LogRocket等。
- **自建监控系统**：基于开源工具搭建自定义监控系统。

### 4. 数据收集与分析

- **数据收集**：使用Performance API、Navigation Timing API等收集性能数据。
- **数据存储**：将收集的数据存储到数据库或监控平台。
- **数据分析**：分析性能数据，识别性能瓶颈。
- **可视化**：将分析结果可视化，便于理解和决策。

## 监控与分析的最佳实践

### 1. 建立性能基线

- **定义性能目标**：根据业务需求和用户体验要求，定义性能目标。
- **建立性能基线**：通过监控数据建立性能基线，作为性能优化的参考。
- **定期评估**：定期评估性能指标，确保性能符合预期。

### 2. 实时监控

- **设置监控告警**：当性能指标超过阈值时，及时告警。
- **实时数据**：实时收集和分析性能数据，及时发现问题。
- **多维度监控**：从不同维度监控性能，如网络、渲染、JavaScript执行等。

### 3. 性能分析

- **深入分析**：对性能数据进行深入分析，找出性能瓶颈。
- **根因分析**：分析性能问题的根本原因，而不仅仅是表面现象。
- **对比分析**：对比不同版本、不同环境的性能数据，了解性能变化。

### 4. 持续优化

- **迭代优化**：基于监控和分析结果，持续进行性能优化。
- **验证效果**：优化后验证性能改进效果，确保优化有效。
- **文档记录**：记录性能优化过程和结果，积累经验。

## 示例代码

### 1. 使用Performance API监控性能

```javascript
// 监控页面加载性能
function monitorPageLoad() {
  if (window.performance) {
    window.addEventListener('load', function() {
      const navigationTiming = performance.getEntriesByType('navigation')[0];
      
      console.log('页面加载性能：');
      console.log('DNS解析时间:', navigationTiming.domainLookupEnd - navigationTiming.domainLookupStart);
      console.log('TCP连接时间:', navigationTiming.connectEnd - navigationTiming.connectStart);
      console.log('首字节时间:', navigationTiming.responseStart - navigationTiming.requestStart);
      console.log('内容加载时间:', navigationTiming.responseEnd - navigationTiming.responseStart);
      console.log('DOM加载时间:', navigationTiming.domContentLoadedEventEnd - navigationTiming.navigationStart);
      console.log('页面加载时间:', navigationTiming.loadEventEnd - navigationTiming.navigationStart);
    });
  }
}

// 监控核心Web指标
function monitorCoreWebVitals() {
  // 监控LCP
  new PerformanceObserver((entryList) => {
    const entries = entryList.getEntries();
    const lastEntry = entries[entries.length - 1];
    console.log('LCP:', lastEntry.startTime);
  }).observe({ type: 'largest-contentful-paint', buffered: true });
  
  // 监控FID
  new PerformanceObserver((entryList) => {
    const entries = entryList.getEntries();
    entries.forEach((entry) => {
      console.log('FID:', entry.processingStart - entry.startTime);
    });
  }).observe({ type: 'first-input', buffered: true });
  
  // 监控CLS
  new PerformanceObserver((entryList) => {
    const entries = entryList.getEntries();
    entries.forEach((entry) => {
      console.log('CLS:', entry.value);
    });
  }).observe({ type: 'layout-shift', buffered: true });
}

// 调用监控函数
monitorPageLoad();
monitorCoreWebVitals();
```

### 2. 错误监控

```javascript
// 监控JavaScript错误
window.addEventListener('error', function(event) {
  console.error('JavaScript错误:', event.error);
  console.error('错误位置:', event.filename, ':', event.lineno, ':', event.colno);
  
  // 发送错误数据到监控平台
  // fetch('/api/error', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   body: JSON.stringify({
  //     error: event.error.message,
  //     filename: event.filename,
  //     lineno: event.lineno,
  //     colno: event.colno
  //   })
  // });
});

// 监控未捕获的Promise拒绝
window.addEventListener('unhandledrejection', function(event) {
  console.error('未捕获的Promise拒绝:', event.reason);
  
  // 发送错误数据到监控平台
  // fetch('/api/error', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   body: JSON.stringify({
  //     error: event.reason.message || String(event.reason),
  //     type: 'unhandledrejection'
  //   })
  // });
});
```

### 3. 用户行为监控

```javascript
// 监控用户点击事件
document.addEventListener('click', function(event) {
  console.log('用户点击:', event.target);
  
  // 发送点击数据到监控平台
  // fetch('/api/click', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   body: JSON.stringify({
  //     target: event.target.tagName,
  //     className: event.target.className,
  //     id: event.target.id,
  //     x: event.clientX,
  //     y: event.clientY
  //   })
  // });
});

// 监控页面停留时间
let pageLoadTime = Date.now();

window.addEventListener('beforeunload', function() {
  const stayTime = Date.now() - pageLoadTime;
  console.log('页面停留时间:', stayTime, 'ms');
  
  // 发送停留时间数据到监控平台
  // fetch('/api/staytime', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   body: JSON.stringify({
  //     url: window.location.href,
  //     stayTime: stayTime
  //   })
  // });
});
```

## 监控与分析工具

### 1. 浏览器开发工具

- **Chrome DevTools**：提供网络、性能、内存等分析工具。
- **Firefox Developer Tools**：提供类似的分析工具。
- **Edge DevTools**：基于Chrome DevTools，提供类似的功能。

### 2. 性能分析工具

- **Lighthouse**：分析页面性能，提供优化建议。
- **WebPageTest**：提供详细的性能测试报告。
- **Google PageSpeed Insights**：分析页面性能，提供优化建议。
- **Chrome User Experience Report**：提供真实用户体验数据。

### 3. 监控平台

- **New Relic**：提供应用性能监控、错误监控等。
- **Datadog**：提供应用性能监控、日志管理等。
- **Sentry**：专注于错误监控和异常追踪。
- **LogRocket**：录制用户会话，分析用户行为。
- **Google Analytics**：提供用户行为分析和流量统计。
- **百度统计**：提供用户行为分析和流量统计。

### 4. 自建监控系统

- **Prometheus**：开源的监控系统，用于收集和存储时间序列数据。
- **Grafana**：开源的可视化平台，用于展示监控数据。
- **ELK Stack**：Elasticsearch、Logstash、Kibana的组合，用于日志收集和分析。

## 学习资源

- [Performance API](https://developer.mozilla.org/en-US/docs/Web/API/Performance)
- [Navigation Timing API](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_timing_API)
- [Core Web Vitals](https://web.dev/vitals/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [WebPageTest](https://www.webpagetest.org/)
- [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)
- [Sentry Documentation](https://docs.sentry.io/)
- [New Relic Documentation](https://docs.newrelic.com/)