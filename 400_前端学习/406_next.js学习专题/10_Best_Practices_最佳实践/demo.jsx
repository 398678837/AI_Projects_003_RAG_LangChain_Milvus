// Next.js 最佳实践示例

// 1. 组件结构
// components/Button.jsx
function Button({ children, variant = 'primary', size = 'medium', onClick }) {
  const variants = {
    primary: 'bg-blue-500 text-white',
    secondary: 'bg-gray-500 text-white',
    danger: 'bg-red-500 text-white',
  };
  
  const sizes = {
    small: 'px-3 py-1 text-sm',
    medium: 'px-4 py-2',
    large: 'px-6 py-3 text-lg',
  };
  
  return (
    <button
      className={`${variants[variant]} ${sizes[size]} rounded-md hover:opacity-90 transition-opacity`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}

export default Button;

// 2. 布局组件
// components/Layout.jsx
import Header from './Header';
import Footer from './Footer';

function Layout({ children }) {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow">{children}</main>
      <Footer />
    </div>
  );
}

export default Layout;

// 3. 数据获取
// pages/index.jsx
import { useSWR } from 'swr';

function HomePage() {
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error, isLoading } = useSWR('https://api.example.com/posts', fetcher);
  
  if (error) {
    return <div>Error: {error.message}</div>;
  }
  
  if (isLoading) {
    return <div>Loading...</div>;
  }
  
  return (
    <div>
      <h1>Posts</h1>
      <ul>
        {data.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;

// 4. 静态生成
// pages/blog/[slug].jsx
export async function getStaticPaths() {
  const res = await fetch('https://api.example.com/posts');
  const posts = await res.json();
  
  const paths = posts.map((post) => ({
    params: { slug: post.slug },
  }));
  
  return {
    paths,
    fallback: 'blocking',
  };
}

export async function getStaticProps({ params }) {
  const res = await fetch(`https://api.example.com/posts/${params.slug}`);
  const post = await res.json();
  
  return {
    props: {
      post,
    },
    revalidate: 60,
  };
}

function BlogPost({ post }) {
  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </div>
  );
}

export default BlogPost;

// 5. 图片优化
// components/OptimizedImage.jsx
import Image from 'next/image';

function OptimizedImage({ src, alt, width, height, className }) {
  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height}
      className={className}
      priority={false}
      loading="lazy"
    />
  );
}

export default OptimizedImage;

// 6. 字体优化
// pages/_app.jsx
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

function MyApp({ Component, pageProps }) {
  return (
    <div className={inter.className}>
      <Component {...pageProps} />
    </div>
  );
}

export default MyApp;

// 7. 错误边界
// components/ErrorBoundary.jsx
import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h1>Something went wrong</h1>
          <p>{this.state.error?.message}</p>
        </div>
      );
    }
    
    return this.props.children;
  }
}

export default ErrorBoundary;

// 8. 路由预加载
// components/LinkWithPrefetch.jsx
import Link from 'next/link';

function LinkWithPrefetch({ href, children }) {
  return (
    <Link href={href} prefetch>
      <a className="hover:underline">{children}</a>
    </Link>
  );
}

export default LinkWithPrefetch;

// 9. 环境变量
// utils/api.js
const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function fetchAPI(endpoint) {
  const res = await fetch(`${API_URL}${endpoint}`);
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  return res.json();
}

// 10. 性能优化
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['example.com', 'cdn.example.com'],
  },
  optimizeFonts: true,
  compress: true,
  output: 'standalone',
};

module.exports = nextConfig;
