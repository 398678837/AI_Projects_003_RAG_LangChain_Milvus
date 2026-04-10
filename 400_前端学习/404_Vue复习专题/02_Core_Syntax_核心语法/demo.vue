<template>
  <div class="core-syntax">
    <h1>Vue 核心语法示例</h1>
    
    <!-- 1. 模板语法 -->
    <div class="section">
      <h2>1. 模板语法</h2>
      <!-- 文本插值 -->
      <p>文本插值: {{ message }}</p>
      <!-- 原始 HTML -->
      <p v-html="rawHtml"></p>
      <!-- 属性绑定 -->
      <div v-bind:id="dynamicId">动态 ID</div>
      <!-- 简写形式 -->
      <div :class="{ active: isActive }">动态类</div>
    </div>
    
    <!-- 2. 指令 -->
    <div class="section">
      <h2>2. 指令</h2>
      <!-- v-if -->
      <div v-if="showContent">
        <p>条件渲染内容</p>
      </div>
      <div v-else>
        <p>条件渲染的其他内容</p>
      </div>
      
      <!-- v-for -->
      <ul>
        <li v-for="(item, index) in items" :key="item.id">
          {{ index }}: {{ item.name }}
        </li>
      </ul>
      
      <!-- v-on -->
      <button v-on:click="increment">
        点击次数: {{ count }}
      </button>
      <!-- 简写形式 -->
      <button @click="decrement">
        减少
      </button>
      
      <!-- v-model -->
      <input v-model="inputValue" placeholder="输入内容">
      <p>输入内容: {{ inputValue }}</p>
    </div>
    
    <!-- 3. 计算属性 -->
    <div class="section">
      <h2>3. 计算属性</h2>
      <p>原始消息: {{ message }}</p>
      <p>反转消息: {{ reversedMessage }}</p>
      <p>消息长度: {{ messageLength }}</p>
    </div>
    
    <!-- 4. 监听属性 -->
    <div class="section">
      <h2>4. 监听属性</h2>
      <input v-model="watchValue" placeholder="输入内容">
      <p>监听值: {{ watchValue }}</p>
      <p>监听次数: {{ watchCount }}</p>
    </div>
    
    <!-- 5. 方法 -->
    <div class="section">
      <h2>5. 方法</h2>
      <button @click="sayHello">打招呼</button>
      <button @click="toggleActive">切换激活状态</button>
      <p>{{ greeting }}</p>
      <p :class="{ active: isActive }">激活状态: {{ isActive }}</p>
    </div>
    
    <!-- 6. 修饰符 -->
    <div class="section">
      <h2>6. 修饰符</h2>
      <!-- 事件修饰符 -->
      <button @click.stop="handleClick">阻止冒泡</button>
      <button @click.prevent="handleSubmit">阻止默认行为</button>
      
      <!-- 按键修饰符 -->
      <input @keyup.enter="handleEnter">
      
      <!-- 系统修饰符 -->
      <button @click.ctrl="handleCtrlClick">Ctrl + 点击</button>
      
      <!-- v-model 修饰符 -->
      <input v-model.lazy="lazyValue">
      <p>延迟绑定: {{ lazyValue }}</p>
    </div>
    
    <!-- 7. 过滤器 -->
    <div class="section">
      <h2>7. 过滤器</h2>
      <p>日期: {{ date | formatDate }}</p>
      <p>大写: {{ message | uppercase }}</p>
      <p>自定义: {{ message | customFilter('后缀') }}</p>
    </div>
    
    <!-- 8. 计算属性 vs 方法 -->
    <div class="section">
      <h2>8. 计算属性 vs 方法</h2>
      <p>计算属性: {{ computedValue }}</p>
      <p>方法: {{ methodValue() }}</p>
      <button @click="updateValue">更新值</button>
    </div>
    
    <!-- 9. 响应式原理 -->
    <div class="section">
      <h2>9. 响应式原理</h2>
      <button @click="addProperty">添加属性</button>
      <button @click="updateArray">更新数组</button>
      <p>对象: {{ reactiveObject }}</p>
      <p>数组: {{ reactiveArray }}</p>
    </div>
    
    <!-- 10. 生命周期 -->
    <div class="section">
      <h2>10. 生命周期</h2>
      <p>created: {{ lifecycle.created }}</p>
      <p>mounted: {{ lifecycle.mounted }}</p>
      <p>updated: {{ lifecycle.updated }}</p>
      <button @click="updateMessage">更新消息</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CoreSyntax',
  data() {
    return {
      message: 'Hello Vue!',
      rawHtml: '<strong>粗体文本</strong>',
      dynamicId: 'dynamic-id',
      isActive: false,
      showContent: true,
      items: [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' },
        { id: 3, name: 'Item 3' }
      ],
      count: 0,
      inputValue: '',
      watchValue: '',
      watchCount: 0,
      greeting: '',
      lazyValue: '',
      date: new Date(),
      value: 10,
      reactiveObject: { name: 'John' },
      reactiveArray: [1, 2, 3],
      lifecycle: {
        created: false,
        mounted: false,
        updated: false
      }
    };
  },
  computed: {
    reversedMessage() {
      return this.message.split('').reverse().join('');
    },
    messageLength() {
      return this.message.length;
    },
    computedValue() {
      console.log('Computed value computed');
      return this.value * 2;
    }
  },
  watch: {
    watchValue(newValue, oldValue) {
      this.watchCount++;
      console.log(`Value changed from ${oldValue} to ${newValue}`);
    },
    message() {
      this.lifecycle.updated = true;
    }
  },
  methods: {
    increment() {
      this.count++;
    },
    decrement() {
      this.count--;
    },
    sayHello() {
      this.greeting = `Hello, ${this.reactiveObject.name}!`;
    },
    toggleActive() {
      this.isActive = !this.isActive;
    },
    handleClick() {
      console.log('Click handled');
    },
    handleSubmit() {
      console.log('Submit handled');
    },
    handleEnter() {
      console.log('Enter key pressed');
    },
    handleCtrlClick() {
      console.log('Ctrl + Click');
    },
    methodValue() {
      console.log('Method called');
      return this.value * 2;
    },
    updateValue() {
      this.value++;
    },
    addProperty() {
      // Vue 无法检测到对象属性的添加
      // this.reactiveObject.age = 30; // 不会触发响应
      this.$set(this.reactiveObject, 'age', 30); // 会触发响应
    },
    updateArray() {
      // Vue 无法检测到数组索引的直接修改
      // this.reactiveArray[0] = 10; // 不会触发响应
      this.reactiveArray.push(4); // 会触发响应
    },
    updateMessage() {
      this.message = 'Updated message!';
    }
  },
  filters: {
    formatDate(value) {
      return new Date(value).toLocaleDateString();
    },
    uppercase(value) {
      return value.toUpperCase();
    },
    customFilter(value, suffix) {
      return `${value} ${suffix}`;
    }
  },
  created() {
    this.lifecycle.created = true;
    console.log('Component created');
  },
  mounted() {
    this.lifecycle.mounted = true;
    console.log('Component mounted');
  },
  updated() {
    console.log('Component updated');
  }
};
</script>

<style scoped>
.core-syntax {
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
