// 移动端UI设计示例代码

// 1. 色彩系统
const colorSystem = `
// Material Design 色彩系统

const materialColors = {
  primary: {
    50: '#e3f2fd',
    100: '#bbdefb',
    200: '#90caf9',
    300: '#64b5f6',
    400: '#42a5f5',
    500: '#2196f3',
    600: '#1e88e5',
    700: '#1976d2',
    800: '#1565c0',
    900: '#0d47a1'
  },
  secondary: {
    50: '#fce4ec',
    100: '#f8bbd9',
    200: '#f48fb1',
    300: '#f06292',
    400: '#ec407a',
    500: '#e91e63',
    600: '#d81b60',
    700: '#c2185b',
    800: '#ad1457',
    900: '#880e4f'
  },
  neutral: {
    50: '#fafafa',
    100: '#f5f5f5',
    200: '#eeeeee',
    300: '#e0e0e0',
    400: '#bdbdbd',
    500: '#9e9e9e',
    600: '#757575',
    700: '#616161',
    800: '#424242',
    900: '#212121'
  },
  success: '#4caf50',
  warning: '#ff9800',
  error: '#f44336',
  info: '#2196f3'
};

// iOS 色彩系统
const iosColors = {
  system: {
    blue: '#007aff',
    green: '#34c759',
    indigo: '#5856d6',
    orange: '#ff9500',
    pink: '#ff2d55',
    purple: '#af52de',
    red: '#ff3b30',
    teal: '#5ac8fa',
    yellow: '#ffcc00'
  },
  gray: {
    systemGray: '#8e8e93',
    systemGray2: '#aeaeb2',
    systemGray3: '#c7c7cc',
    systemGray4: '#d1d1d6',
    systemGray5: '#e5e5ea',
    systemGray6: '#f2f2f7'
  },
  label: {
    primary: '#000000',
    secondary: '#3c3c4399',
    tertiary: '#3c3c434d',
    quaternary: '#3c3c432e'
  },
  background: {
    primary: '#ffffff',
    secondary: '#f2f2f7',
    tertiary: '#ffffff'
  },
  grouped: {
    primary: '#f2f2f7',
    secondary: '#ffffff',
    tertiary: '#f2f2f7'
  },
  filled: {
    primary: '#78788033',
    secondary: '#78788029',
    tertiary: '#7676801f',
    quaternary: '#74748014'
  }
};

console.log('=== 色彩系统 ===');
console.log('Material Design:', materialColors);
console.log('iOS:', iosColors);
`;

console.log('=== 色彩系统 ===');
console.log(colorSystem);

// 2. 间距系统
const spacingSystem = `
// 间距系统 - 8pt栅格

const spacing = {
  xs: 4,    // 4px - 极小间距
  sm: 8,    // 8px - 小间距
  md: 16,   // 16px - 中间距
  lg: 24,   // 24px - 大间距
  xl: 32,   // 32px - 超大间距
  '2xl': 48, // 48px
  '3xl': 64  // 64px
};

// 字体大小
const typography = {
  xs: 12,    // 12px - 极小文字
  sm: 14,    // 14px - 小文字
  base: 16,  // 16px - 正文
  lg: 18,    // 18px - 大文字
  xl: 20,    // 20px - 超大文字
  '2xl': 24, // 24px - 标题
  '3xl': 30, // 30px - 大标题
  '4xl': 36, // 36px - 超大标题
  '5xl': 48  // 48px
};

// 圆角
const borderRadius = {
  none: 0,
  sm: 4,     // 4px - 小圆角
  md: 8,     // 8px - 中圆角
  lg: 12,    // 12px - 大圆角
  xl: 16,    // 16px - 超大圆角
  '2xl': 24, // 24px
  full: 9999 // 完全圆角
};

// 阴影
const shadows = {
  none: 'none',
  sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
  md: '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
  lg: '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
  xl: '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)'
};

// 安全区域
const safeArea = {
  top: 44,    // 顶部安全区域
  bottom: 34,  // 底部安全区域
  left: 0,
  right: 0
};

console.log('=== 间距系统 ===');
console.log('间距:', spacing);
console.log('字体:', typography);
console.log('圆角:', borderRadius);
console.log('阴影:', shadows);
`;

console.log('\n=== 间距系统 ===');
console.log(spacingSystem);

// 3. 按钮设计
const buttonDesign = `
// 按钮设计

const buttonVariants = {
  primary: {
    background: '#2196f3',
    color: '#ffffff',
    border: 'none',
    hoverBackground: '#1976d2',
    activeBackground: '#1565c0'
  },
  secondary: {
    background: '#ffffff',
    color: '#2196f3',
    border: '1px solid #2196f3',
    hoverBackground: '#e3f2fd',
    activeBackground: '#bbdefb'
  },
  outline: {
    background: 'transparent',
    color: '#2196f3',
    border: '1px solid #2196f3',
    hoverBackground: '#e3f2fd',
    activeBackground: '#bbdefb'
  },
  text: {
    background: 'transparent',
    color: '#2196f3',
    border: 'none',
    hoverBackground: '#e3f2fd',
    activeBackground: '#bbdefb'
  },
  danger: {
    background: '#f44336',
    color: '#ffffff',
    border: 'none',
    hoverBackground: '#d32f2f',
    activeBackground: '#b71c1c'
  }
};

const buttonSizes = {
  sm: {
    padding: '6px 12px',
    fontSize: '14px',
    borderRadius: '4px'
  },
  md: {
    padding: '10px 20px',
    fontSize: '16px',
    borderRadius: '8px'
  },
  lg: {
    padding: '14px 28px',
    fontSize: '18px',
    borderRadius: '12px'
  }
};

const buttonStates = {
  normal: {},
  hover: { transform: 'translateY(-1px)' },
  active: { transform: 'translateY(0)' },
  disabled: {
    opacity: 0.5,
    cursor: 'not-allowed'
  },
  loading: {
    opacity: 0.7,
    cursor: 'wait'
  }
};

// CSS示例
const buttonCSS = \`
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s;
  user-select: none;
}

.btn-primary {
  background-color: #2196f3;
  color: #ffffff;
  border: none;
}

.btn-primary:hover {
  background-color: #1976d2;
}

.btn-primary:active {
  background-color: #1565c0;
}

.btn-secondary {
  background-color: #ffffff;
  color: #2196f3;
  border: 1px solid #2196f3;
}

.btn-lg {
  padding: 14px 28px;
  font-size: 18px;
  border-radius: 12px;
}

.btn-md {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 8px;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
\`;

console.log('=== 按钮设计 ===');
console.log('变体:', buttonVariants);
console.log('尺寸:', buttonSizes);
console.log('状态:', buttonStates);
`;

console.log('\n=== 按钮设计 ===');
console.log(buttonDesign);

// 4. 卡片设计
const cardDesign = `
// 卡片设计

const cardVariants = {
  default: {
    background: '#ffffff',
    borderRadius: '12px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    padding: '20px'
  },
  outlined: {
    background: '#ffffff',
    borderRadius: '12px',
    boxShadow: 'none',
    border: '1px solid #e0e0e0',
    padding: '20px'
  },
  elevated: {
    background: '#ffffff',
    borderRadius: '16px',
    boxShadow: '0 8px 24px rgba(0,0,0,0.12)',
    padding: '24px'
  }
};

const cardComponents = {
  header: {
    marginBottom: '16px'
  },
  title: {
    fontSize: '18px',
    fontWeight: '600',
    color: '#212121',
    marginBottom: '4px'
  },
  subtitle: {
    fontSize: '14px',
    color: '#757575'
  },
  content: {
    fontSize: '16px',
    color: '#424242',
    lineHeight: '1.6'
  },
  footer: {
    marginTop: '16px',
    paddingTop: '16px',
    borderTop: '1px solid #f0f0f0'
  },
  actions: {
    display: 'flex',
    gap: '8px'
  },
  media: {
    width: '100%',
    height: '200px',
    objectFit: 'cover',
    borderRadius: '8px',
    marginBottom: '16px'
  }
};

// 卡片HTML结构
const cardHTML = \`
<div class="card">
  <div class="card-media">
    <img src="image.jpg" alt="Card image">
  </div>
  <div class="card-header">
    <h3 class="card-title">卡片标题</h3>
    <p class="card-subtitle">卡片副标题</p>
  </div>
  <div class="card-content">
    <p>这是卡片的内容区域，可以放置任意内容。</p>
  </div>
  <div class="card-footer">
    <div class="card-actions">
      <button class="btn btn-secondary">取消</button>
      <button class="btn btn-primary">确定</button>
    </div>
  </div>
</div>
\`;

// 卡片CSS
const cardCSS = \`
.card {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  overflow: hidden;
}

.card-media {
  width: 100%;
  height: 200px;
}

.card-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-header {
  padding: 20px 20px 0;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #212121;
  margin: 0 0 4px;
}

.card-subtitle {
  font-size: 14px;
  color: #757575;
  margin: 0;
}

.card-content {
  padding: 16px 20px;
  font-size: 16px;
  color: #424242;
  line-height: 1.6;
}

.card-footer {
  padding: 16px 20px 20px;
  border-top: 1px solid #f0f0f0;
}

.card-actions {
  display: flex;
  gap: 8px;
  justify-content: flex-end;
}
\`;

console.log('=== 卡片设计 ===');
console.log('变体:', cardVariants);
console.log('组件:', cardComponents);
`;

console.log('\n=== 卡片设计 ===');
console.log(cardDesign);

console.log('\n🎉 移动端UI设计学习完成！');
console.log('💡 好的UI设计能大大提升用户体验！');
`;

console.log('\n=== UI设计 ===');
