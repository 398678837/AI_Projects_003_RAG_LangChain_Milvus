// 移动端用户体验示例代码

// 1. 加载状态设计
const loadingStates = `
// 加载状态设计

// 1.1 骨架屏
const skeletonScreen = {
  // CSS 骨架屏
  css: \`
    .skeleton {
      background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
      background-size: 200% 100%;
      animation: shimmer 1.5s infinite;
    }
    
    @keyframes shimmer {
      0% { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }
    
    .skeleton-text {
      height: 16px;
      margin-bottom: 8px;
      border-radius: 4px;
    }
    
    .skeleton-avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
    }
    
    .skeleton-image {
      width: 100%;
      height: 200px;
      border-radius: 8px;
    }
  \`,
  
  // React 骨架屏组件
  react: \`
    function SkeletonCard() {
      return (
        <div className="card">
          <div className="skeleton skeleton-image" />
          <div className="card-content">
            <div className="skeleton skeleton-text" style={{ width: '60%' }} />
            <div className="skeleton skeleton-text" style={{ width: '80%' }} />
            <div className="skeleton skeleton-text" style={{ width: '40%' }} />
          </div>
        </div>
      );
    }
    
    function Card({ data, loading }) {
      if (loading) {
        return <SkeletonCard />;
      }
      
      return (
        <div className="card">
          <img src={data.image} alt={data.title} />
          <div className="card-content">
            <h3>{data.title}</h3>
            <p>{data.description}</p>
          </div>
        </div>
      );
    }
  \`
};

// 1.2 加载指示器
const loadingIndicators = {
  // 多种加载样式
  styles: \`
    /* 旋转加载 */
    .spinner {
      width: 40px;
      height: 40px;
      border: 3px solid #f3f3f3;
      border-top: 3px solid #2196f3;
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    
    /* 脉冲加载 */
    .pulse {
      width: 40px;
      height: 40px;
      background: #2196f3;
      border-radius: 50%;
      animation: pulse 1.5s ease-in-out infinite;
    }
    
    @keyframes pulse {
      0%, 100% { transform: scale(0.8); opacity: 0.5; }
      50% { transform: scale(1); opacity: 1; }
    }
    
    /* 弹跳加载 */
    .bounce {
      display: flex;
      gap: 8px;
    }
    
    .bounce-dot {
      width: 12px;
      height: 12px;
      background: #2196f3;
      border-radius: 50%;
      animation: bounce 1.4s ease-in-out infinite both;
    }
    
    .bounce-dot:nth-child(1) { animation-delay: -0.32s; }
    .bounce-dot:nth-child(2) { animation-delay: -0.16s; }
    
    @keyframes bounce {
      0%, 80%, 100% { transform: scale(0); }
      40% { transform: scale(1); }
    }
  \`,
  
  // 进度条
  progressBar: \`
    .progress-bar {
      width: 100%;
      height: 4px;
      background: #e0e0e0;
      border-radius: 2px;
      overflow: hidden;
    }
    
    .progress-bar-fill {
      height: 100%;
      background: #2196f3;
      transition: width 0.3s ease;
    }
    
    // 不确定进度条
    .progress-bar-indeterminate .progress-bar-fill {
      width: 30%;
      animation: indeterminate 1.5s linear infinite;
    }
    
    @keyframes indeterminate {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(400%); }
    }
  \`
};

// 1.3 加载策略
const loadingStrategies = \`
// 不同场景的加载策略

// 1. 首次加载 - 全屏加载
function FullPageLoading() {
  return (
    <div className="full-page-loading">
      <div className="spinner" />
      <p>加载中...</p>
    </div>
  );
}

// 2. 局部加载 - 按钮加载
function Button({ loading, onClick, children }) {
  return (
    <button onClick={onClick} disabled={loading}>
      {loading ? (
        <>
          <div className="spinner-small" />
          加载中...
        </>
      ) : children}
    </button>
  );
}

// 3. 下拉刷新
function PullToRefresh() {
  const [refreshing, setRefreshing] = useState(false);
  
  const onRefresh = async () => {
    setRefreshing(true);
    await fetchData();
    setRefreshing(false);
  };
  
  return (
    <RefreshControl refreshing={refreshing} onRefresh={onRefresh}>
      <List />
    </RefreshControl>
  );
}

// 4. 上拉加载更多
function InfiniteScroll() {
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);
  
  const loadMore = async () => {
    if (loading || !hasMore) return;
    
    setLoading(true);
    const data = await fetchMoreData();
    setHasMore(data.length > 0);
    setLoading(false);
  };
  
  return (
    <ScrollView onScrollToBottom={loadMore}>
      <List />
      {loading && <LoadingIndicator />}
      {!hasMore && <NoMoreData />}
    </ScrollView>
  );
}
\`;

console.log('=== 加载状态设计 ===');
console.log('骨架屏:', skeletonScreen);
console.log('加载指示器:', loadingIndicators);
console.log('加载策略:', loadingStrategies);
`;

console.log('=== 加载状态设计 ===');
console.log(loadingStates);

// 2. 空状态和错误状态
const emptyErrorStates = `
// 空状态和错误状态设计

// 2.1 空状态设计
const emptyStates = {
  // 无数据
  noData: {
    icon: '📭',
    title: '暂无数据',
    description: '这里还没有内容哦',
    action: {
      text: '刷新一下',
      onClick: () => refresh()
    }
  },
  
  // 搜索无结果
  noSearchResults: {
    icon: '🔍',
    title: '未找到结果',
    description: '试试其他关键词吧',
    action: {
      text: '清除搜索',
      onClick: () => clearSearch()
    }
  },
  
  // 无网络
  noNetwork: {
    icon: '📡',
    title: '网络连接失败',
    description: '请检查您的网络设置',
    action: {
      text: '重试',
      onClick: () => retry()
    }
  },
  
  // 空购物车
  emptyCart: {
    icon: '🛒',
    title: '购物车是空的',
    description: '快去挑选心仪的商品吧',
    action: {
      text: '去逛逛',
      onClick: () => navigateToShop()
    }
  }
};

// 空状态组件
const emptyStateComponent = \`
function EmptyState({ icon, title, description, action }) {
  return (
    <div className="empty-state">
      <div className="empty-state-icon">{icon}</div>
      <h3 className="empty-state-title">{title}</h3>
      <p className="empty-state-description">{description}</p>
      {action && (
        <button className="empty-state-action" onClick={action.onClick}>
          {action.text}
        </button>
      )}
    </div>
  );
}

// 使用
function UserList({ users, loading }) {
  if (loading) {
    return <Loading />;
  }
  
  if (!users || users.length === 0) {
    return (
      <EmptyState
        icon="👥"
        title="暂无用户"
        description="还没有添加任何用户"
        action={{
          text: '添加用户',
          onClick: () => navigateToAddUser()
        }}
      />
    );
  }
  
  return <List data={users} />;
}
\`;

// 2.2 错误状态设计
const errorStates = {
  // 通用错误
  genericError: {
    icon: '❌',
    title: '出错了',
    description: '发生了一些意外，请稍后重试',
    action: {
      text: '重试',
      onClick: () => retry()
    }
  },
  
  // 网络错误
  networkError: {
    icon: '📡',
    title: '网络错误',
    description: '无法连接到服务器',
    action: {
      text: '检查网络',
      onClick: () => openNetworkSettings()
    }
  },
  
  // 服务器错误
  serverError: {
    icon: '⚠️',
    title: '服务器错误',
    description: '服务器暂时无法响应',
    action: {
      text: '稍后重试',
      onClick: () => retry()
    }
  },
  
  // 权限错误
  permissionError: {
    icon: '🔒',
    title: '权限不足',
    description: '您没有权限访问此内容',
    action: {
      text: '联系管理员',
      onClick: () => contactAdmin()
    }
  }
};

// 错误边界组件
const errorBoundary = \`
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
    logError(error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <ErrorState
          icon="💥"
          title="页面崩溃了"
          description="不要担心，我们已经记录了这个错误"
          action={{
            text: '刷新页面',
            onClick: () => window.location.reload()
          }}
        />
      );
    }
    
    return this.props.children;
  }
}

// 使用
<ErrorBoundary>
  <App />
</ErrorBoundary>
\`;

console.log('=== 空状态和错误状态 ===');
console.log('空状态:', emptyStates);
console.log('空状态组件:', emptyStateComponent);
console.log('错误状态:', errorStates);
console.log('错误边界:', errorBoundary);
`;

console.log('\n=== 空状态和错误状态 ===');
console.log(emptyErrorStates);

// 3. 手势和动画
const gesturesAnimations = `
// 手势和动画设计

// 3.1 常用手势
const gestures = {
  // 点击
  tap: {
    description: '轻触',
    useCases: ['按钮点击', '列表项选择', '链接跳转'],
    duration: '< 300ms'
  },
  
  // 双击
  doubleTap: {
    description: '双击',
    useCases: ['图片放大', '点赞', '全屏切换'],
    duration: '两次点击间隔 < 300ms'
  },
  
  // 长按
  longPress: {
    description: '长按',
    useCases: ['显示菜单', '多选', '拖动排序'],
    duration: '> 500ms'
  },
  
  // 滑动
  swipe: {
    description: '滑动',
    useCases: ['删除', '归档', '查看详情', '切换页面'],
    directions: ['left', 'right', 'up', 'down'],
    distance: '> 50px'
  },
  
  // 拖动
  drag: {
    description: '拖动',
    useCases: ['排序', '调整大小', '移动位置'],
    duration: '持续触摸并移动'
  },
  
  // 捏合
  pinch: {
    description: '捏合',
    useCases: ['缩放图片', '缩放地图'],
    fingers: 2
  }
};

// 手势库使用示例
const gestureLibrary = \`
// 使用 Hammer.js
import Hammer from 'hammerjs';

const element = document.getElementById('my-element');
const hammer = new Hammer(element);

// 单击
hammer.on('tap', (e) => {
  console.log('单击');
});

// 双击
hammer.on('doubletap', (e) => {
  console.log('双击');
});

// 长按
hammer.on('press', (e) => {
  console.log('长按');
});

// 滑动
hammer.on('swipeleft', (e) => {
  console.log('左滑');
});

hammer.on('swiperight', (e) => {
  console.log('右滑');
});

// 拖动
hammer.on('pan', (e) => {
  console.log('拖动', e.deltaX, e.deltaY);
});

// React Native 手势
import { GestureResponderEvent, PanGestureHandler } from 'react-native';

function Draggable() {
  const [translateX, setTranslateX] = useState(0);
  const [translateY, setTranslateY] = useState(0);
  
  const onGestureEvent = (event) => {
    setTranslateX(event.nativeEvent.translationX);
    setTranslateY(event.nativeEvent.translationY);
  };
  
  return (
    <PanGestureHandler onGestureEvent={onGestureEvent}>
      <Animated.View 
        style={{
          transform: [
            { translateX },
            { translateY }
          ]
        }}
      >
        <Content />
      </Animated.View>
    </PanGestureHandler>
  );
}
\`;

// 3.2 动画设计
const animations = {
  // 动画原则
  principles: [
    '持续时间: 200-500ms',
    '缓动函数: ease-in-out',
    '一致性: 相同操作相同动画',
    '目的性: 动画要有意义',
    '克制: 不要过度使用动画'
  ],
  
  // 常用动画
  types: {
    fade: {
      property: 'opacity',
      duration: '300ms',
      easing: 'ease-out'
    },
    slide: {
      property: 'transform',
      duration: '300ms',
      easing: 'ease-out'
    },
    scale: {
      property: 'transform',
      duration: '200ms',
      easing: 'ease-out'
    },
    rotate: {
      property: 'transform',
      duration: '300ms',
      easing: 'ease-in-out'
    }
  }
};

// CSS 动画示例
const cssAnimations = \`
/* 淡入 */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  animation: fadeIn 0.3s ease-out;
}

/* 滑入 */
@keyframes slideInUp {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.slide-in-up {
  animation: slideInUp 0.3s ease-out;
}

/* 缩放 */
@keyframes scaleIn {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

.scale-in {
  animation: scaleIn 0.2s ease-out;
}

/* 弹性动画 */
@keyframes bounceIn {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.05); }
  70% { transform: scale(0.9); }
  100% { transform: scale(1); opacity: 1; }
}

.bounce-in {
  animation: bounceIn 0.6s ease-out;
}

/* 过渡 */
.transition {
  transition: all 0.3s ease;
}

.transition-fast {
  transition: all 0.15s ease;
}

.transition-slow {
  transition: all 0.5s ease;
}
\`;

console.log('=== 手势和动画 ===');
console.log('手势:', gestures);
console.log('手势库使用:', gestureLibrary);
console.log('动画:', animations);
console.log('CSS动画:', cssAnimations);
`;

console.log('\n=== 手势和动画 ===');
console.log(gesturesAnimations);

console.log('\n🎉 移动端用户体验学习完成！');
console.log('💡 好的用户体验能让用户爱上你的应用！');
`;

console.log('\n=== 用户体验 ===');
