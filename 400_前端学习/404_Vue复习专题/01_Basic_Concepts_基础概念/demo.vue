<template>
  <div class="basic-concepts">
    <h1>Vue 基础概念示例</h1>
    
    <!-- 1. 插值表达式 -->
    <div class="section">
      <h2>1. 插值表达式</h2>
      <p>{{ message }}</p>
      <p>{{ 1 + 1 }}</p>
      <p>{{ user.name }}</p>
    </div>
    
    <!-- 2. 指令 -->
    <div class="section">
      <h2>2. 指令</h2>
      <!-- v-bind -->
      <div v-bind:class="{ active: isActive }">
        v-bind:class 示例
      </div>
      <!-- v-if -->
      <div v-if="showMessage">
        条件渲染：显示消息
      </div>
      <!-- v-for -->
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }}
        </li>
      </ul>
      <!-- v-on -->
      <button v-on:click="handleClick">
        点击我
      </button>
    </div>
    
    <!-- 3. 计算属性 -->
    <div class="section">
      <h2>3. 计算属性</h2>
      <p>原始消息: {{ message }}</p>
      <p>反转消息: {{ reversedMessage }}</p>
    </div>
    
    <!-- 4. 监听属性 -->
    <div class="section">
      <h2>4. 监听属性</h2>
      <input v-model="message" placeholder="输入消息">
      <p>消息长度: {{ messageLength }}</p>
    </div>
    
    <!-- 5. 方法 -->
    <div class="section">
      <h2>5. 方法</h2>
      <button @click="sayHello">
        打招呼
      </button>
      <p>{{ greeting }}</p>
    </div>
    
    <!-- 6. 过滤器 -->
    <div class="section">
      <h2>6. 过滤器</h2>
      <p>{{ date | formatDate }}</p>
    </div>
    
    <!-- 7. 修饰符 -->
    <div class="section">
      <h2>7. 修饰符</h2>
      <form @submit.prevent="handleSubmit">
        <input type="text" v-model="formData.name">
        <button type="submit">提交</button>
      </form>
    </div>
    
    <!-- 8. 组件 -->
    <div class="section">
      <h2>8. 组件</h2>
      <my-component :message="message" @custom-event="handleCustomEvent"></my-component>
    </div>
    
    <!-- 9. 生命周期钩子 -->
    <div class="section">
      <h2>9. 生命周期钩子</h2>
      <p>组件已创建: {{ created }}</p>
      <p>组件已挂载: {{ mounted }}</p>
    </div>
    
    <!-- 10. 响应式数据 -->
    <div class="section">
      <h2>10. 响应式数据</h2>
      <button @click="updateUser">更新用户</button>
      <p>用户信息: {{ user }}</p>
    </div>
  </div>
</template>

<script>
// 导入组件
import MyComponent from './MyComponent.vue';

export default {
  name: 'BasicConcepts',
  components: {
    MyComponent
  },
  data() {
    return {
      message: 'Hello Vue!',
      user: {
        name: 'John',
        age: 30
      },
      items: [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' },
        { id: 3, name: 'Item 3' }
      ],
      isActive: true,
      showMessage: true,
      greeting: '',
      formData: {
        name: ''
      },
      date: new Date(),
      created: false,
      mounted: false,
      messageLength: 0
    };
  },
  computed: {
    reversedMessage() {
      return this.message.split('').reverse().join('');
    }
  },
  watch: {
    message(newValue) {
      this.messageLength = newValue.length;
    }
  },
  methods: {
    handleClick() {
      console.log('Button clicked!');
    },
    sayHello() {
      this.greeting = `Hello, ${this.user.name}!`;
    },
    handleSubmit() {
      console.log('Form submitted:', this.formData);
    },
    handleCustomEvent(data) {
      console.log('Custom event received:', data);
    },
    updateUser() {
      this.user = {
        name: 'Jane',
        age: 25
      };
    }
  },
  filters: {
    formatDate(value) {
      return new Date(value).toLocaleDateString();
    }
  },
  created() {
    this.created = true;
    console.log('Component created');
  },
  mounted() {
    this.mounted = true;
    console.log('Component mounted');
  }
};
</script>

<style scoped>
.basic-concepts {
  padding: 20px;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.active {
  color: red;
  font-weight: bold;
}
</style>
