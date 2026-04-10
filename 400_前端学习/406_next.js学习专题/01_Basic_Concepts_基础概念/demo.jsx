// Next.js 基础概念示例

// 1. 页面组件
function HomePage() {
  return (
    <div>
      <h1>Welcome to Next.js</h1>
      <p>This is a basic Next.js page</p>
    </div>
  );
}

export default HomePage;

// 2. 布局组件
function Layout({ children }) {
  return (
    <div>
      <header>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
          </ul>
        </nav>
      </header>
      <main>{children}</main>
      <footer>
        <p>© 2024 Next.js App</p>
      </footer>
    </div>
  );
}

export { Layout };

// 3. 组件
function Button({ children, onClick }) {
  return (
    <button onClick={onClick}>
      {children}
    </button>
  );
}

export { Button };

// 4. 样式
// 使用 CSS 模块
/*
// styles/Home.module.css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}
*/

// 5. 环境变量
// 创建 .env.local 文件
/*
NEXT_PUBLIC_API_URL=https://api.example.com
*/

// 使用环境变量
// const apiUrl = process.env.NEXT_PUBLIC_API_URL;

// 6. 图片优化
// import Image from 'next/image';

// function ImageExample() {
//   return (
//     <Image
//       src="/logo.png"
//       alt="Logo"
//       width={100}
//       height={100}
//     />
//   );
// }

// 7. 字体优化
// import { Inter } from 'next/font/google';

// const inter = Inter({ subsets: ['latin'] });

// function FontExample() {
//   return (
//     <div className={inter.className}>
//       <p>Hello with Inter font</p>
//     </div>
//   );
// }
