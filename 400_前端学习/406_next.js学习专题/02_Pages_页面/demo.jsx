// Next.js 页面示例

// 1. 基本页面
function HomePage() {
  return (
    <div>
      <h1>Home Page</h1>
      <p>Welcome to the home page</p>
    </div>
  );
}

export default HomePage;

// 2. 带参数的页面
// pages/posts/[id].jsx
function PostPage({ params }) {
  const { id } = params;
  
  return (
    <div>
      <h1>Post {id}</h1>
      <p>This is post {id}</p>
    </div>
  );
}

export default PostPage;

// 3. 动态路由页面
// pages/[...slug].jsx
function CatchAllPage({ params }) {
  const { slug } = params;
  
  return (
    <div>
      <h1>Catch All Page</h1>
      <p>Slug: {slug.join('/')}</p>
    </div>
  );
}

export default CatchAllPage;

// 4. 可选的动态路由页面
// pages/[[...slug]].jsx
function OptionalCatchAllPage({ params }) {
  const { slug } = params || { slug: [] };
  
  return (
    <div>
      <h1>Optional Catch All Page</h1>
      <p>Slug: {slug.join('/')}</p>
    </div>
  );
}

export default OptionalCatchAllPage;

// 5. 嵌套路由
// pages/dashboard/index.jsx
function DashboardPage() {
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome to the dashboard</p>
    </div>
  );
}

export default DashboardPage;

// pages/dashboard/settings.jsx
function SettingsPage() {
  return (
    <div>
      <h1>Settings</h1>
      <p>Edit your settings</p>
    </div>
  );
}

export default SettingsPage;

// 6. 404页面
// pages/404.jsx
function Custom404() {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for does not exist</p>
    </div>
  );
}

export default Custom404;

// 7. 错误页面
// pages/_error.jsx
function Error({ statusCode }) {
  return (
    <div>
      <h1>Error {statusCode}</h1>
      <p>An error occurred</p>
    </div>
  );
}

Error.getInitialProps = ({ res, err }) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode : 404;
  return { statusCode };
};

export default Error;
