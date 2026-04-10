// Next.js 中间件示例

// 1. 基本中间件
// middleware.js
export function middleware(request) {
  console.log('Middleware executed for:', request.nextUrl.pathname);
  return NextResponse.next();
}

// 2. 路径匹配
// middleware.js
export const config = {
  matcher: ['/api/:path*', '/dashboard/:path*'],
};

// 3. 重定向
// middleware.js
export function middleware(request) {
  if (request.nextUrl.pathname === '/old-path') {
    return NextResponse.redirect(new URL('/new-path', request.url));
  }
  return NextResponse.next();
}

// 4. 认证中间件
// middleware.js
export function middleware(request) {
  const token = request.cookies.get('token')?.value;
  
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};

// 5. 地域检测
// middleware.js
export function middleware(request) {
  const country = request.geo?.country || 'US';
  
  if (country === 'CN') {
    return NextResponse.redirect(new URL('/cn', request.url));
  }
  
  return NextResponse.next();
}

// 6. 响应修改
// middleware.js
export function middleware(request) {
  const response = NextResponse.next();
  
  // 设置自定义头部
  response.headers.set('X-Custom-Header', 'Hello from middleware');
  
  return response;
}

// 7. 限流中间件
// middleware.js
import { NextResponse } from 'next/server';

// 简单的内存限流实现
const rateLimit = {
  tokens: {},
  windowMs: 60 * 1000, // 1分钟
  max: 10, // 最大请求数
};

export function middleware(request) {
  const ip = request.ip || request.headers.get('x-forwarded-for') || 'unknown';
  
  if (!rateLimit.tokens[ip]) {
    rateLimit.tokens[ip] = {
      count: 0,
      lastReset: Date.now(),
    };
  }
  
  const now = Date.now();
  
  // 重置计数器
  if (now - rateLimit.tokens[ip].lastReset > rateLimit.windowMs) {
    rateLimit.tokens[ip] = {
      count: 0,
      lastReset: now,
    };
  }
  
  rateLimit.tokens[ip].count++;
  
  if (rateLimit.tokens[ip].count > rateLimit.max) {
    return new NextResponse('Too many requests', {
      status: 429,
    });
  }
  
  return NextResponse.next();
}

// 8. 内容安全策略
// middleware.js
export function middleware(request) {
  const response = NextResponse.next();
  
  response.headers.set(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' https://trusted-cdn.com; style-src 'self' 'unsafe-inline'"
  );
  
  return response;
}

// 9. 缓存控制
// middleware.js
export function middleware(request) {
  const response = NextResponse.next();
  
  // 设置缓存控制头部
  response.headers.set('Cache-Control', 's-maxage=86400, stale-while-revalidate');
  
  return response;
}

// 10. 多中间件组合
// middleware.js
import { NextResponse } from 'next/server';

// 认证中间件
function authMiddleware(request) {
  const token = request.cookies.get('token')?.value;
  
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  return NextResponse.next();
}

// 日志中间件
function loggerMiddleware(request) {
  console.log(`${new Date().toISOString()} - ${request.method} ${request.nextUrl.pathname}`);
  return NextResponse.next();
}

export function middleware(request) {
  // 应用日志中间件
  loggerMiddleware(request);
  
  // 对特定路径应用认证中间件
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    return authMiddleware(request);
  }
  
  return NextResponse.next();
}

export const config = {
  matcher: ['/api/:path*', '/dashboard/:path*', '/profile'],
};
