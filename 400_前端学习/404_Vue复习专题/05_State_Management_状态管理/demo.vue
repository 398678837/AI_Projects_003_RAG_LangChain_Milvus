<template>
  <div class="state-management">
    <h1>Vue 状态管理示例</h1>
    
    <!-- 1. 组件内部状态 -->
    <div class="section">
      <h2>1. 组件内部状态</h2>
      <p>Count: {{ count }}</p>
      <button @click="increment">增加</button>
      <button @click="decrement">减少</button>
    </div>
    
    <!-- 2. 父组件向子组件传递状态 -->
    <div class="section">
      <h2>2. 父组件向子组件传递状态</h2>
      <p>Parent message: {{ message }}</p>
      <button @click="updateMessage">更新消息</button>
      <child-component :message="message"></child-component>
    </div>
    
    <!-- 3. 子组件向父组件传递状态 -->
    <div class="section">
      <h2>3. 子组件向父组件传递状态</h2>
      <p>Child data: {{ childData }}</p>
      <child-component-with-event @update="handleChildUpdate"></child-component-with-event>
    </div>
    
    <!-- 4. 兄弟组件间状态传递 -->
    <div class="section">
      <h2>4. 兄弟组件间状态传递</h2>
      <sibling-a @update="handleSiblingUpdate"></sibling-a>
      <sibling-b :data="siblingData"></sibling-b>
    </div>
    
    <!-- 5. Vuex 状态管理 -->
    <div class="section">
      <h2>5. Vuex 状态管理</h2>
      <p>Vuex count: {{ $store.state.count }}</p>
      <button @click="incrementVuex">增加</button>
      <button @click="decrementVuex">减少</button>
      <button @click="resetVuex">重置</button>
    </div>
    
    <!-- 6. Composition API 状态管理 -->
    <div class="section">
      <h2>6. Composition API 状态管理</h2>
      <composition-api-demo></composition-api-demo>
    </div>
    
    <!-- 7. Provide/Inject -->
    <div class="section">
      <h2>7. Provide/Inject</h2>
      <provide-demo>
        <inject-demo></inject-demo>
      </provide-demo>
    </div>
  </div>
</template>

<script>
// 导入组件
import ChildComponent from './components/ChildComponent.vue';
import ChildComponentWithEvent from './components/ChildComponentWithEvent.vue';
import SiblingA from './components/SiblingA.vue';
import SiblingB from './components/SiblingB.vue';
import CompositionApiDemo from './components/CompositionApiDemo.vue';
import ProvideDemo from './components/ProvideDemo.vue';
import InjectDemo from './components/InjectDemo.vue';

export default {
  name: 'StateManagementDemo',
  components: {
    ChildComponent,
    ChildComponentWithEvent,
    SiblingA,
    SiblingB,
    CompositionApiDemo,
    ProvideDemo,
    InjectDemo
  },
  data() {
    return {
      count: 0,
      message: 'Hello from parent',
      childData: '',
      siblingData: ''
    };
  },
  methods: {
    increment() {
      this.count++;
    },
    decrement() {
      this.count--;
    },
    updateMessage() {
      this.message = 'Updated message at ' + new Date().toLocaleTimeString();
    },
    handleChildUpdate(data) {
      this.childData = data;
    },
    handleSiblingUpdate(data) {
      this.siblingData = data;
    },
    incrementVuex() {
      this.$store.commit('increment');
    },
    decrementVuex() {
      this.$store.commit('decrement');
    },
    resetVuex() {
      this.$store.commit('reset');
    }
  }
};
</script>

<style scoped>
.state-management {
  padding: 20px;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  margin-right: 10px;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
}

button:hover {
  background-color: #e9e9e9;
}
</style>
