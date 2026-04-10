// Next.js 服务端渲染示例

// 1. 基本服务端渲染
function ServerSidePage({ posts, time }) {
  return (
    <div>
      <h1>Server Side Rendering Page</h1>
      <p>Server time: {time}</p>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export async function getServerSideProps() {
  // 从API获取数据
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await res.json();
  
  // 获取服务器时间
  const time = new Date().toLocaleString();
  
  return {
    props: {
      posts,
      time,
    },
  };
}

export default ServerSidePage;

// 2. 带参数的服务端渲染
function DynamicServerPage({ post, params }) {
  return (
    <div>
      <h1>Dynamic Server Page</h1>
      <h2>Post {params.id}</h2>
      <h3>{post.title}</h3>
      <p>{post.body}</p>
      <p>Author: {post.userId}</p>
    </div>
  );
}

export async function getServerSideProps({ params }) {
  // 根据ID获取单个帖子
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.id}`);
  const post = await res.json();
  
  return {
    props: {
      post,
      params,
    },
  };
}

export default DynamicServerPage;

// 3. 带查询参数的服务端渲染
function QueryParamsPage({ data, query }) {
  return (
    <div>
      <h1>Query Params Page</h1>
      <p>Query: {JSON.stringify(query)}</p>
      <div>{data}</div>
    </div>
  );
}

export async function getServerSideProps({ query }) {
  // 使用查询参数获取数据
  const { search, page = 1 } = query;
  
  // 模拟根据查询参数获取数据
  let data = '';
  if (search) {
    data = `Search results for: ${search}, page: ${page}`;
  } else {
    data = `No search query, page: ${page}`;
  }
  
  return {
    props: {
      data,
      query,
    },
  };
}

export default QueryParamsPage;

// 4. 带Cookie的服务端渲染
function CookiePage({ user, cookies }) {
  return (
    <div>
      <h1>Cookie Page</h1>
      <p>User: {user ? user.name : 'Guest'}</p>
      <p>Cookies: {JSON.stringify(cookies)}</p>
    </div>
  );
}

export async function getServerSideProps({ req }) {
  // 从请求中获取Cookie
  const cookies = req.headers.cookie || '';
  let user = null;
  
  // 模拟解析Cookie
  if (cookies.includes('user=')) {
    const userCookie = cookies.split(';').find(cookie => cookie.trim().startsWith('user='));
    if (userCookie) {
      const userData = userCookie.split('=')[1];
      try {
        user = JSON.parse(decodeURIComponent(userData));
      } catch (e) {
        console.error('Error parsing user cookie:', e);
      }
    }
  }
  
  return {
    props: {
      user,
      cookies,
    },
  };
}

export default CookiePage;

// 5. 服务端渲染错误处理
function ErrorPage({ error }) {
  return (
    <div>
      <h1>Error Page</h1>
      <p>Error: {error.message}</p>
    </div>
  );
}

export async function getServerSideProps() {
  try {
    // 模拟错误
    throw new Error('Something went wrong');
  } catch (error) {
    return {
      props: {
        error,
      },
    };
  }
}

export default ErrorPage;
