// Next.js 数据获取示例

// 1. getStaticProps - 静态生成
function StaticPropsPage({ posts }) {
  return (
    <div>
      <h1>Static Props Page</h1>
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
    // 重新验证时间（秒）
    revalidate: 10,
  };
}

export default StaticPropsPage;

// 2. getServerSideProps - 服务端渲染
function ServerSidePropsPage({ posts }) {
  return (
    <div>
      <h1>Server Side Props Page</h1>
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
  
  return {
    props: {
      posts,
    },
  };
}

export default ServerSidePropsPage;

// 3. getStaticPaths - 动态路由的静态生成
function DynamicStaticPage({ post }) {
  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}

export async function getStaticPaths() {
  // 获取所有可能的路径
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await res.json();
  
  const paths = posts.slice(0, 5).map((post) => ({
    params: { id: post.id.toString() },
  }));
  
  return {
    paths,
    fallback: false,
  };
}

export async function getStaticProps({ params }) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.id}`);
  const post = await res.json();
  
  return {
    props: {
      post,
    },
  };
}

export default DynamicStaticPage;

// 4. 客户端数据获取 - useEffect
import { useState, useEffect } from 'react';

function ClientSideFetching() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    async function fetchPosts() {
      const res = await fetch('https://jsonplaceholder.typicode.com/posts');
      const data = await res.json();
      setPosts(data);
      setLoading(false);
    }
    
    fetchPosts();
  }, []);
  
  if (loading) {
    return <div>Loading...</div>;
  }
  
  return (
    <div>
      <h1>Client Side Fetching</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export { ClientSideFetching };

// 5. SWR - 数据获取库
// 首先安装 SWR
// npm install swr

// import useSWR from 'swr';

// function SWRFetching() {
//   const fetcher = (...args) => fetch(...args).then((res) => res.json());
//   const { data, error, isLoading } = useSWR('https://jsonplaceholder.typicode.com/posts', fetcher);
//   
//   if (error) {
//     return <div>Error: {error.message}</div>;
//   }
//   
//   if (isLoading) {
//     return <div>Loading...</div>;
//   }
//   
//   return (
//     <div>
//       <h1>SWR Fetching</h1>
//       <ul>
//         {data.map((post) => (
//           <li key={post.id}>{post.title}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export { SWRFetching };
