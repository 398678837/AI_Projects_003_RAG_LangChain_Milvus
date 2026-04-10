<template>
  <div class="practical-applications">
    <h1>Vue 实战应用示例</h1>
    
    <!-- 1. 待办事项列表 -->
    <div class="section">
      <h2>1. 待办事项列表</h2>
      <div class="todo-app">
        <input v-model="newTodo" @keyup.enter="addTodo" placeholder="添加待办事项">
        <button @click="addTodo">添加</button>
        <ul>
          <li v-for="todo in todos" :key="todo.id" class="todo-item">
            <input type="checkbox" v-model="todo.completed">
            <span :class="{ completed: todo.completed }">{{ todo.text }}</span>
            <button @click="removeTodo(todo.id)">删除</button>
          </li>
        </ul>
        <div class="todo-footer">
          <span>{{ remaining }} 项待完成</span>
          <button @click="clearCompleted">清除已完成</button>
        </div>
      </div>
    </div>
    
    <!-- 2. 计数器应用 -->
    <div class="section">
      <h2>2. 计数器应用</h2>
      <div class="counter-app">
        <h3>计数器: {{ count }}</h3>
        <button @click="increment">增加</button>
        <button @click="decrement">减少</button>
        <button @click="reset">重置</button>
      </div>
    </div>
    
    <!-- 3. 天气应用 -->
    <div class="section">
      <h2>3. 天气应用</h2>
      <div class="weather-app">
        <input v-model="city" placeholder="输入城市名称">
        <button @click="getWeather">获取天气</button>
        <div v-if="weatherData" class="weather-info">
          <h3>{{ weatherData.name }}</h3>
          <p>温度: {{ weatherData.main.temp }}°C</p>
          <p>天气: {{ weatherData.weather[0].description }}</p>
          <p>湿度: {{ weatherData.main.humidity }}%</p>
        </div>
        <div v-if="weatherError" class="error">
          {{ weatherError }}
        </div>
      </div>
    </div>
    
    <!-- 4. 购物车应用 -->
    <div class="section">
      <h2>4. 购物车应用</h2>
      <div class="cart-app">
        <div class="products">
          <div v-for="product in products" :key="product.id" class="product">
            <h4>{{ product.name }}</h4>
            <p>价格: ¥{{ product.price }}</p>
            <button @click="addToCart(product)">加入购物车</button>
          </div>
        </div>
        <div class="cart">
          <h3>购物车</h3>
          <ul>
            <li v-for="item in cart" :key="item.id" class="cart-item">
              <span>{{ item.name }}</span>
              <span>¥{{ item.price }}</span>
              <span>x{{ item.quantity }}</span>
              <button @click="removeFromCart(item.id)">删除</button>
            </li>
          </ul>
          <div class="cart-total">
            <h4>总计: ¥{{ total }}</h4>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 5. 表单验证应用 -->
    <div class="section">
      <h2>5. 表单验证应用</h2>
      <div class="form-validation-app">
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">用户名:</label>
            <input type="text" id="username" v-model="form.username">
            <span v-if="errors.username" class="error">{{ errors.username }}</span>
          </div>
          <div class="form-group">
            <label for="email">邮箱:</label>
            <input type="email" id="email" v-model="form.email">
            <span v-if="errors.email" class="error">{{ errors.email }}</span>
          </div>
          <div class="form-group">
            <label for="password">密码:</label>
            <input type="password" id="password" v-model="form.password">
            <span v-if="errors.password" class="error">{{ errors.password }}</span>
          </div>
          <button type="submit">提交</button>
        </form>
        <div v-if="formSubmitted" class="success">
          表单提交成功！
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PracticalApplicationsDemo',
  data() {
    return {
      // 待办事项
      newTodo: '',
      todos: [
        { id: 1, text: '学习Vue', completed: false },
        { id: 2, text: '完成项目', completed: false },
        { id: 3, text: '锻炼身体', completed: true }
      ],
      nextTodoId: 4,
      
      // 计数器
      count: 0,
      
      // 天气应用
      city: '',
      weatherData: null,
      weatherError: null,
      
      // 购物车
      products: [
        { id: 1, name: 'Vue.js 实战', price: 89.9 },
        { id: 2, name: 'JavaScript 权威指南', price: 129.9 },
        { id: 3, name: 'Node.js 实战', price: 99.9 }
      ],
      cart: [],
      
      // 表单验证
      form: {
        username: '',
        email: '',
        password: ''
      },
      errors: {},
      formSubmitted: false
    };
  },
  computed: {
    remaining() {
      return this.todos.filter(todo => !todo.completed).length;
    },
    total() {
      return this.cart.reduce((sum, item) => sum + item.price * item.quantity, 0).toFixed(2);
    }
  },
  methods: {
    // 待办事项
    addTodo() {
      if (this.newTodo.trim()) {
        this.todos.push({
          id: this.nextTodoId++,
          text: this.newTodo,
          completed: false
        });
        this.newTodo = '';
      }
    },
    removeTodo(id) {
      this.todos = this.todos.filter(todo => todo.id !== id);
    },
    clearCompleted() {
      this.todos = this.todos.filter(todo => !todo.completed);
    },
    
    // 计数器
    increment() {
      this.count++;
    },
    decrement() {
      this.count--;
    },
    reset() {
      this.count = 0;
    },
    
    // 天气应用
    async getWeather() {
      if (!this.city.trim()) {
        this.weatherError = '请输入城市名称';
        return;
      }
      
      try {
        // 这里使用 OpenWeatherMap API，需要替换为真实的 API key
        const apiKey = 'YOUR_API_KEY';
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${this.city}&appid=${apiKey}&units=metric`);
        const data = await response.json();
        
        if (data.cod === 200) {
          this.weatherData = data;
          this.weatherError = null;
        } else {
          this.weatherError = data.message;
          this.weatherData = null;
        }
      } catch (error) {
        this.weatherError = '获取天气信息失败';
        this.weatherData = null;
      }
    },
    
    // 购物车
    addToCart(product) {
      const existingItem = this.cart.find(item => item.id === product.id);
      if (existingItem) {
        existingItem.quantity++;
      } else {
        this.cart.push({
          ...product,
          quantity: 1
        });
      }
    },
    removeFromCart(id) {
      this.cart = this.cart.filter(item => item.id !== id);
    },
    
    // 表单验证
    submitForm() {
      this.errors = {};
      
      if (!this.form.username) {
        this.errors.username = '用户名不能为空';
      }
      
      if (!this.form.email) {
        this.errors.email = '邮箱不能为空';
      } else if (!this.isValidEmail(this.form.email)) {
        this.errors.email = '邮箱格式不正确';
      }
      
      if (!this.form.password) {
        this.errors.password = '密码不能为空';
      } else if (this.form.password.length < 6) {
        this.errors.password = '密码长度不能少于6位';
      }
      
      if (Object.keys(this.errors).length === 0) {
        this.formSubmitted = true;
        // 重置表单
        setTimeout(() => {
          this.form = {
            username: '',
            email: '',
            password: ''
          };
          this.formSubmitted = false;
        }, 3000);
      }
    },
    isValidEmail(email) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    }
  }
};
</script>

<style scoped>
.practical-applications {
  padding: 20px;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

/* 待办事项 */
.todo-app {
  max-width: 400px;
}

.todo-app input {
  width: 250px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 10px;
}

.todo-app button {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
}

.todo-app button:hover {
  background-color: #e9e9e9;
}

.todo-item {
  display: flex;
  align-items: center;
  margin: 10px 0;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.todo-item input {
  margin-right: 10px;
  width: auto;
}

.todo-item span {
  flex: 1;
}

.todo-item .completed {
  text-decoration: line-through;
  color: #999;
}

.todo-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid #ddd;
}

/* 计数器 */
.counter-app {
  text-align: center;
}

.counter-app h3 {
  font-size: 24px;
  margin-bottom: 20px;
}

.counter-app button {
  margin: 0 10px;
  padding: 10px 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
  font-size: 16px;
}

.counter-app button:hover {
  background-color: #e9e9e9;
}

/* 天气应用 */
.weather-app {
  max-width: 400px;
}

.weather-app input {
  width: 250px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 10px;
}

.weather-app button {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
}

.weather-app button:hover {
  background-color: #e9e9e9;
}

.weather-info {
  margin-top: 20px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.error {
  margin-top: 10px;
  color: red;
}

/* 购物车 */
.cart-app {
  display: flex;
  gap: 30px;
}

.products {
  flex: 1;
}

.product {
  padding: 15px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.product button {
  margin-top: 10px;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f0f0f0;
  cursor: pointer;
}

.product button:hover {
  background-color: #e0e0e0;
}

.cart {
  flex: 1;
  padding: 15px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px 0;
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 4px;
}

.cart-total {
  margin-top: 20px;
  padding-top: 10px;
  border-top: 1px solid #ddd;
  text-align: right;
}

/* 表单验证 */
.form-validation-app {
  max-width: 400px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-group .error {
  color: red;
  font-size: 12px;
  margin-top: 5px;
  display: block;
}

.form-validation-app button {
  padding: 10px 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
  font-size: 16px;
}

.form-validation-app button:hover {
  background-color: #e9e9e9;
}

.success {
  margin-top: 20px;
  padding: 10px;
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
  border-radius: 4px;
  text-align: center;
}
</style>
