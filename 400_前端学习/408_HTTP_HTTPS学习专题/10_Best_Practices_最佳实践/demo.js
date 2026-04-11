// HTTP/HTTPS 最佳实践示例代码

// 1. 性能优化最佳实践
const performanceOptimizations = {
  减少HTTP请求: {
    方法: '合并CSS/JS、使用CSS精灵图',
    效果: '减少网络往返'
  },
  使用CDN: {
    方法: '静态资源使用CDN分发',
    效果: '就近访问，加快速度'
  },
  启用压缩: {
    方法: 'Gzip/Brotli压缩文本资源',
    效果: '减少传输大小'
  },
  缓存策略: {
    方法: 'Cache-Control、ETag、Last-Modified',
    效果: '减少重复请求'
  },
  使用HTTP2: {
    方法: '启用HTTP/2多路复用',
    效果: '并行传输，提高效率'
  },
  懒加载: {
    方法: '图片、组件按需加载',
    效果: '减少初始加载'
  },
  预加载: {
    方法: 'link rel="preload"',
    效果: '提前加载关键资源'
  }
};

console.log('性能优化最佳实践:', performanceOptimizations);

// 2. 安全最佳实践
const securityBestPractices = {
  使用HTTPS: {
    说明: '全站HTTPS，HSTS强制',
    配置: 'Strict-Transport-Security: max-age=31536000'
  },
  安全响应头: {
    说明: '设置CSP、X-Frame-Options等',
    配置: {
      'Content-Security-Policy': "default-src 'self'",
      'X-Frame-Options': 'DENY',
      'X-Content-Type-Options': 'nosniff',
      'X-XSS-Protection': '1; mode=block'
    }
  },
  输入验证: {
    说明: '验证和清理所有输入',
    做法: '白名单验证，类型检查'
  },
  防止注入: {
    说明: '防止SQL注入、XSS、CSRF',
    做法: '参数化查询、输出编码、CSRF Token'
  },
  认证授权: {
    说明: '安全的会话管理',
    做法: 'JWT、Session、HttpOnly Cookie'
  },
  错误处理: {
    说明: '不要泄露敏感信息',
    做法: '通用错误消息，记录详细日志'
  },
  依赖管理: {
    说明: '定期更新依赖',
    做法: 'npm audit、安全扫描'
  }
};

console.log('\n安全最佳实践:', securityBestPractices);

// 3. 缓存策略示例
const cacheStrategies = {
  HTML: {
    'Cache-Control': 'no-cache',
    说明: '每次验证，可快速更新'
  },
  CSS_JS: {
    'Cache-Control': 'public, max-age=31536000',
    说明: '长期缓存，用hash版本号'
  },
  图片: {
    'Cache-Control': 'public, max-age=86400',
    说明: '缓存一天'
  },
  API数据: {
    'Cache-Control': 'private, max-age=300',
    说明: '私有缓存5分钟'
  },
  不缓存: {
    'Cache-Control': 'no-store, no-cache, must-revalidate',
    说明: '完全不缓存'
  }
};

console.log('\n缓存策略:', cacheStrategies);

// 4. 生成带版本的静态资源URL
function versionedAsset(filename, hash) {
  const ext = filename.lastIndexOf('.');
  const name = filename.substring(0, ext);
  const extension = filename.substring(ext);
  return `${name}.${hash}${extension}`;
}

console.log('\n版本化资源:', versionedAsset('app.js', 'abc123'));
console.log('版本化资源:', versionedAsset('style.css', 'def456'));

// 5. HTTP 请求重试逻辑
async function fetchWithRetry(url, options = {}, retries = 3, delay = 1000) {
  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    if (retries > 0) {
      console.log(`请求失败，${delay/1000}秒后重试... (剩余${retries}次)`);
      await new Promise(resolve => setTimeout(resolve, delay));
      return fetchWithRetry(url, options, retries - 1, delay * 2);
    }
    throw error;
  }
}

console.log('\n请求重试函数已定义');

// 6. 请求超时处理
function fetchWithTimeout(url, options = {}, timeout = 5000) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);
  
  return fetch(url, {
    ...options,
    signal: controller.signal
  }).then(response => {
    clearTimeout(id);
    return response;
  }).catch(error => {
    clearTimeout(id);
    if (error.name === 'AbortError') {
      throw new Error('请求超时');
    }
    throw error;
  });
}

console.log('请求超时函数已定义');

// 7. 请求日志记录
function createLoggedFetch() {
  return async function loggedFetch(url, options = {}) {
    const startTime = Date.now();
    const method = options.method || 'GET';
    
    console.log(`[REQUEST] ${method} ${url}`);
    
    try {
      const response = await fetch(url, options);
      const duration = Date.now() - startTime;
      
      console.log(`[RESPONSE] ${method} ${url} - ${response.status} (${duration}ms)`);
      
      return response;
    } catch (error) {
      const duration = Date.now() - startTime;
      console.error(`[ERROR] ${method} ${url} - ${error.message} (${duration}ms)`);
      throw error;
    }
  };
}

const loggedFetch = createLoggedFetch();
console.log('日志记录Fetch已定义');

// 8. API 响应验证
function validateResponse(data, schema) {
  for (const key in schema) {
    const expectedType = schema[key];
    const actualValue = data[key];
    const actualType = Array.isArray(actualValue) ? 'array' : typeof actualValue;
    
    if (actualType !== expectedType) {
      throw new Error(`字段 ${key} 类型错误，期望 ${expectedType}，实际 ${actualType}`);
    }
  }
  return true;
}

const userSchema = {
  id: 'number',
  name: 'string',
  email: 'string',
  isActive: 'boolean'
};

const validUser = { id: 1, name: '张三', email: 'test@example.com', isActive: true };
console.log('\n响应验证:', validateResponse(validUser, userSchema));

// 9. 健康检查端点
async function healthCheck(url) {
  try {
    const response = await fetchWithTimeout(url, {}, 3000);
    if (response.ok) {
      return { status: 'healthy', code: response.status };
    }
    return { status: 'unhealthy', code: response.status };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}

console.log('健康检查函数已定义');

// 10. 调试工具和技巧
const debuggingTools = {
  浏览器DevTools: {
    Network: '查看请求响应',
    Console: '查看日志和错误',
    Application: '查看Cookie、Storage'
  },
  抓包工具: {
    Charles: 'HTTP/HTTPS代理',
    Fiddler: 'Web调试代理',
    Wireshark: '网络包分析'
  },
  命令行工具: {
    curl: '发送HTTP请求',
    'HTTPie': '更友好的curl替代',
    Postman: 'API测试工具'
  }
};

console.log('\n调试工具:', debuggingTools);

// 11. 常见问题排查
const troubleshooting = {
  CORS错误: {
    原因: '跨域访问限制',
    解决: '服务器配置CORS头'
  },
  304未修改: {
    原因: '缓存有效',
    解决: '正常行为，使用缓存'
  },
  401未授权: {
    原因: '未登录或token过期',
    解决: '重新登录'
  },
  403禁止: {
    原因: '权限不足',
    解决: '检查用户权限'
  },
  404未找到: {
    原因: 'URL错误或资源不存在',
    解决: '检查URL'
  },
  500服务器错误: {
    原因: '服务器端问题',
    解决: '联系后端或查看日志'
  },
  网络超时: {
    原因: '网络慢或服务器无响应',
    解决: '重试或检查网络'
  }
};

console.log('\n常见问题排查:', troubleshooting);

// 12. 性能指标监控
class PerformanceMonitor {
  constructor() {
    this.metrics = [];
  }

  start(name) {
    return {
      name,
      startTime: performance.now()
    };
  }

  end(marker) {
    const duration = performance.now() - marker.startTime;
    this.metrics.push({
      name: marker.name,
      duration: duration.toFixed(2) + 'ms'
    });
    console.log(`[PERF] ${marker.name}: ${duration.toFixed(2)}ms`);
    return duration;
  }

  async measure(name, fn) {
    const marker = this.start(name);
    try {
      const result = await fn();
      this.end(marker);
      return result;
    } catch (error) {
      this.end(marker);
      throw error;
    }
  }

  getMetrics() {
    return this.metrics;
  }
}

// 使用示例
const monitor = new PerformanceMonitor();
console.log('\n性能监控器已创建');

// 13. 完整的最佳实践检查清单
const checklist = {
  性能: [
    '启用Gzip/Brotli压缩',
    '使用CDN分发静态资源',
    '配置合适的缓存策略',
    '使用HTTP/2或HTTP/3',
    '减少HTTP请求数量',
    '图片优化和懒加载'
  ],
  安全: [
    '全站HTTPS + HSTS',
    '设置安全响应头',
    '验证和清理所有输入',
    '防止XSS、CSRF、SQL注入',
    'HttpOnly和Secure Cookie',
    '定期更新依赖'
  ],
  可靠性: [
    '请求超时和重试',
    '优雅降级',
    '错误边界',
    '日志记录',
    '监控和告警',
    '健康检查'
  ],
  可维护性: [
    '统一响应格式',
    'API版本管理',
    '完善的文档',
    '代码注释',
    '类型检查',
    '测试覆盖'
  ]
};

console.log('\n最佳实践检查清单:', checklist);
