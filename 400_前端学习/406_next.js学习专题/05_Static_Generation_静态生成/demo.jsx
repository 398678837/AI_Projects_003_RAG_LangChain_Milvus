// Next.js 静态生成示例

// 1. 基本静态生成
function HomePage({ posts }) {
  return (
    <div>
      <h1>Home Page</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export async function getStaticProps() {
  // 从API获取数据
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await res.json();
  
  return {
    props: {
      posts,
    },
  };
}

export default HomePage;

// 2. 带重新验证的静态生成
function RevalidatePage({ posts }) {
  return (
    <div>
      <h1>Revalidate Page</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
      <p>Last updated: {new Date().toLocaleTimeString()}</p>
    </div>
  );
}

export async function getStaticProps() {
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await res.json();
  
  return {
    props: {
      posts,
    },
    // 每10秒重新验证一次
    revalidate: 10,
  };
}

export default RevalidatePage;

// 3. 动态路由的静态生成
function PostPage({ post }) {
  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      <p>Author: {post.userId}</p>
    </div>
  );
}

export async function getStaticPaths() {
  // 获取所有可能的路径
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await res.json();
  
  // 生成路径参数
  const paths = posts.slice(0, 10).map((post) => ({
    params: { id: post.id.toString() },
  }));
  
  return {
    paths,
    // fallback: false 表示未生成的路径会返回404
    // fallback: true 表示未生成的路径会在请求时生成
    // fallback: 'blocking' 表示未生成的路径会在请求时生成并阻塞
    fallback: false,
  };
}

export async function getStaticProps({ params }) {
  // 根据ID获取单个帖子
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.id}`);
  const post = await res.json();
  
  return {
    props: {
      post,
    },
  };
}

export default PostPage;

// 4. 嵌套动态路由的静态生成
// pages/blog/[category]/[postId].jsx
function BlogPostPage({ post, category }) {
  return (
    <div>
      <h1>{post.title}</h1>
      <p>Category: {category}</p>
      <p>{post.body}</p>
    </div>
  );
}

export async function getStaticPaths() {
  // 模拟获取所有分类和帖子
  const categories = ['tech', 'travel', 'food'];
  const paths = [];
  
  for (const category of categories) {
    // 为每个分类生成3个帖子
    for (let i = 1; i <= 3; i++) {
      paths.push({
        params: {
          category,
          postId: i.toString(),
        },
      });
    }
  }
  
  return {
    paths,
    fallback: false,
  };
}

export async function getStaticProps({ params }) {
  // 模拟获取帖子数据
  const post = {
    id: params.postId,
    title: `Post ${params.postId} in ${params.category}`,
    body: `This is post ${params.postId} in the ${params.category} category`,
  };
  
  return {
    props: {
      post,
      category: params.category,
    },
  };
}

export default BlogPostPage;
