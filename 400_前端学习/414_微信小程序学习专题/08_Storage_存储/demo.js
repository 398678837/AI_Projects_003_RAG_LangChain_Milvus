// 微信小程序存储示例代码

// 1. 同步存储
const syncStorage = `
// 存储数据
wx.setStorageSync('username', '张三');
wx.setStorageSync('age', 18);
wx.setStorageSync('isLogin', true);

// 存储对象
const userInfo = {
  id: 1,
  name: '张三',
  age: 18,
  avatar: 'https://example.com/avatar.jpg'
};
wx.setStorageSync('userInfo', userInfo);

// 存储数组
const list = [
  { id: 1, name: '商品1' },
  { id: 2, name: '商品2' },
  { id: 3, name: '商品3' }
];
wx.setStorageSync('cartList', list);

// 读取数据
const username = wx.getStorageSync('username');
const age = wx.getStorageSync('age');
const isLogin = wx.getStorageSync('isLogin');
const userInfo = wx.getStorageSync('userInfo');
const cartList = wx.getStorageSync('cartList');

console.log(username, age, isLogin);
console.log(userInfo);
console.log(cartList);

// 读取不存在的key，返回空字符串
const notExist = wx.getStorageSync('notExist');
console.log(notExist); // ''

// 删除数据
wx.removeStorageSync('username');

// 清空所有数据
wx.clearStorageSync();
`;

console.log('=== 同步存储 ===');
console.log(syncStorage);

// 2. 异步存储
const asyncStorage = `
// 异步存储数据
wx.setStorage({
  key: 'username',
  data: '张三',
  success() {
    console.log('存储成功');
  },
  fail(err) {
    console.error('存储失败', err);
  }
});

// Promise封装
function setStorage(key, data) {
  return new Promise((resolve, reject) => {
    wx.setStorage({
      key,
      data,
      success: resolve,
      fail: reject
    });
  });
}

function getStorage(key) {
  return new Promise((resolve, reject) => {
    wx.getStorage({
      key,
      success: res => resolve(res.data),
      fail: reject
    });
  });
}

function removeStorage(key) {
  return new Promise((resolve, reject) => {
    wx.removeStorage({
      key,
      success: resolve,
      fail: reject
    });
  });
}

// 使用async/await
async function example() {
  try {
    await setStorage('username', '张三');
    console.log('存储成功');
    
    const username = await getStorage('username');
    console.log('读取成功:', username);
    
    await removeStorage('username');
    console.log('删除成功');
  } catch (err) {
    console.error('操作失败', err);
  }
}
`;

console.log('\n=== 异步存储 ===');
console.log(asyncStorage);

// 3. 存储信息
const storageInfo = `
// 获取存储信息
wx.getStorageInfo({
  success(res) {
    console.log('所有key:', res.keys);
    console.log('已用空间:', res.currentSize, 'KB');
    console.log('限制空间:', res.limitSize, 'KB');
  }
});

// 同步获取
const info = wx.getStorageInfoSync();
console.log('所有key:', info.keys);
console.log('已用空间:', info.currentSize, 'KB');
console.log('限制空间:', info.limitSize, 'KB');

// 检查key是否存在
function hasKey(key) {
  const info = wx.getStorageInfoSync();
  return info.keys.includes(key);
}

console.log('是否存在username:', hasKey('username'));
`;

console.log('\n=== 存储信息 ===');
console.log(storageInfo);

// 4. 封装存储工具
const storageUtil = `
// utils/storage.js

const STORAGE_PREFIX = 'myapp_';

class Storage {
  constructor() {
    this.prefix = STORAGE_PREFIX;
  }

  getKey(key) {
    return this.prefix + key;
  }

  set(key, value) {
    try {
      const data = JSON.stringify(value);
      wx.setStorageSync(this.getKey(key), data);
      return true;
    } catch (err) {
      console.error('存储失败', err);
      return false;
    }
  }

  get(key, defaultValue = null) {
    try {
      const data = wx.getStorageSync(this.getKey(key));
      if (!data) return defaultValue;
      return JSON.parse(data);
    } catch (err) {
      console.error('读取失败', err);
      return defaultValue;
    }
  }

  remove(key) {
    try {
      wx.removeStorageSync(this.getKey(key));
      return true;
    } catch (err) {
      console.error('删除失败', err);
      return false;
    }
  }

  clear() {
    try {
      const info = wx.getStorageInfoSync();
      info.keys.forEach(key => {
        if (key.startsWith(this.prefix)) {
          wx.removeStorageSync(key);
        }
      });
      return true;
    } catch (err) {
      console.error('清空失败', err);
      return false;
    }
  }

  has(key) {
    const info = wx.getStorageInfoSync();
    return info.keys.includes(this.getKey(key));
  }

  getInfo() {
    const info = wx.getStorageInfoSync();
    const myKeys = info.keys.filter(key => key.startsWith(this.prefix));
    return {
      keys: myKeys,
      currentSize: info.currentSize,
      limitSize: info.limitSize
    };
  }
}

module.exports = new Storage();

// 使用示例
const storage = require('@/utils/storage');

// 存储
storage.set('userInfo', { id: 1, name: '张三' });

// 读取
const userInfo = storage.get('userInfo');
console.log(userInfo);

// 删除
storage.remove('userInfo');

// 检查
console.log(storage.has('userInfo'));

// 清空
storage.clear();
`;

console.log('\n=== 封装存储工具 ===');
console.log(storageUtil);

// 5. 缓存策略
const cacheStrategy = `
// 带过期时间的缓存
class Cache {
  constructor(prefix = 'cache_') {
    this.prefix = prefix;
  }

  set(key, value, ttl = 300000) { // 默认5分钟
    const data = {
      value,
      expireTime: Date.now() + ttl
    };
    wx.setStorageSync(this.prefix + key, JSON.stringify(data));
  }

  get(key) {
    const dataStr = wx.getStorageSync(this.prefix + key);
    if (!dataStr) return null;
    
    try {
      const data = JSON.parse(dataStr);
      if (Date.now() > data.expireTime) {
        this.remove(key);
        return null;
      }
      return data.value;
    } catch (err) {
      this.remove(key);
      return null;
    }
  }

  remove(key) {
    wx.removeStorageSync(this.prefix + key);
  }

  clear() {
    const info = wx.getStorageInfoSync();
    info.keys.forEach(key => {
      if (key.startsWith(this.prefix)) {
        wx.removeStorageSync(key);
      }
    });
  }
}

const cache = new Cache();

// 使用示例
cache.set('userList', [
  { id: 1, name: '张三' },
  { id: 2, name: '李四' }
], 60000); // 1分钟过期

const list = cache.get('userList');
if (list) {
  console.log('使用缓存:', list);
} else {
  console.log('缓存过期，重新获取');
}
`;

console.log('\n=== 缓存策略 ===');
console.log(cacheStrategy);

// 6. 购物车示例
const cartExample = `
// 购物车存储
const CART_KEY = 'cart';

function getCart() {
  return wx.getStorageSync(CART_KEY) || [];
}

function saveCart(cart) {
  wx.setStorageSync(CART_KEY, cart);
}

function addToCart(product) {
  const cart = getCart();
  const existItem = cart.find(item => item.id === product.id);
  
  if (existItem) {
    existItem.quantity += 1;
  } else {
    cart.push({
      ...product,
      quantity: 1,
      selected: true
    });
  }
  
  saveCart(cart);
  return cart;
}

function updateCartQuantity(id, quantity) {
  const cart = getCart();
  const item = cart.find(item => item.id === id);
  
  if (item) {
    if (quantity <= 0) {
      return removeFromCart(id);
    }
    item.quantity = quantity;
    saveCart(cart);
  }
  
  return cart;
}

function removeFromCart(id) {
  const cart = getCart().filter(item => item.id !== id);
  saveCart(cart);
  return cart;
}

function toggleCartItem(id) {
  const cart = getCart();
  const item = cart.find(item => item.id === id);
  
  if (item) {
    item.selected = !item.selected;
    saveCart(cart);
  }
  
  return cart;
}

function toggleAllCart(selected) {
  const cart = getCart();
  cart.forEach(item => {
    item.selected = selected;
  });
  saveCart(cart);
  return cart;
}

function clearCart() {
  saveCart([]);
}

function getCartTotal() {
  const cart = getCart();
  return cart
    .filter(item => item.selected)
    .reduce((total, item) => total + item.price * item.quantity, 0);
}

function getCartCount() {
  const cart = getCart();
  return cart.reduce((count, item) => count + item.quantity, 0);
}

// 使用
addToCart({ id: 1, name: '商品1', price: 100 });
addToCart({ id: 2, name: '商品2', price: 200 });

console.log(getCart());
console.log('总数:', getCartCount());
console.log('总价:', getCartTotal());
`;

console.log('\n=== 购物车示例 ===');
console.log(cartExample);

console.log('=== 微信小程序存储 ===');
