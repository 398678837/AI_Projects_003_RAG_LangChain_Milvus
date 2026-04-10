// Next.js 路由示例

// 1. 使用 Link 组件
import Link from 'next/link';

function Navigation() {
  return (
    <nav>
      <ul>
        <li>
          <Link href="/">Home</Link>
        </li>
        <li>
          <Link href="/about">About</Link>
        </li>
        <li>
          <Link href="/posts/1">Post 1</Link>
        </li>
      </ul>
    </nav>
  );
}

export { Navigation };

// 2. 使用 useRouter 钩子
import { useRouter } from 'next/router';

function DynamicPage() {
  const router = useRouter();
  const { id } = router.query;
  
  return (
    <div>
      <h1>Dynamic Page {id}</h1>
      <button onClick={() => router.push('/')}>Go Home</button>
      <button onClick={() => router.back()}>Go Back</button>
      <button onClick={() => router.reload()}>Reload</button>
    </div>
  );
}

export { DynamicPage };

// 3. 编程式导航
function NavigationButtons() {
  const router = useRouter();
  
  const handleNavigation = () => {
    router.push('/about');
  };
  
  const handleNavigationWithState = () => {
    router.push({
      pathname: '/about',
      query: { name: 'John' }
    });
  };
  
  return (
    <div>
      <button onClick={handleNavigation}>Go to About</button>
      <button onClick={handleNavigationWithState}>Go to About with State</button>
    </div>
  );
}

export { NavigationButtons };

// 4. 路由事件
function RouteEvents() {
  const router = useRouter();
  
  useEffect(() => {
    const handleRouteChange = (url, { shallow }) => {
      console.log('App is changing to: ', url, shallow);
    };
    
    const handleRouteChangeStart = (url) => {
      console.log('Route is starting to change to: ', url);
    };
    
    const handleRouteChangeComplete = (url) => {
      console.log('Route change is complete: ', url);
    };
    
    const handleRouteChangeError = (err, url) => {
      console.error('Route change error: ', err, url);
    };
    
    router.events.on('routeChangeStart', handleRouteChangeStart);
    router.events.on('routeChangeComplete', handleRouteChangeComplete);
    router.events.on('routeChangeError', handleRouteChangeError);
    router.events.on('routeChange', handleRouteChange);
    
    return () => {
      router.events.off('routeChangeStart', handleRouteChangeStart);
      router.events.off('routeChangeComplete', handleRouteChangeComplete);
      router.events.off('routeChangeError', handleRouteChangeError);
      router.events.off('routeChange', handleRouteChange);
    };
  }, [router.events]);
  
  return (
    <div>
      <h1>Route Events</h1>
      <p>Check the console for route events</p>
    </div>
  );
}

export { RouteEvents };

// 5. 浅路由
function ShallowRouting() {
  const router = useRouter();
  
  const handleShallowNavigation = () => {
    router.push('/?counter=1', undefined, { shallow: true });
  };
  
  return (
    <div>
      <h1>Shallow Routing</h1>
      <button onClick={handleShallowNavigation}>Update Query</button>
      <p>Counter: {router.query.counter}</p>
    </div>
  );
}

export { ShallowRouting };

// 6. 路由预加载
function LinkWithPrefetch() {
  return (
    <Link href="/about" prefetch>
      <a>About (with prefetch)</a>
    </Link>
  );
}

export { LinkWithPrefetch };
