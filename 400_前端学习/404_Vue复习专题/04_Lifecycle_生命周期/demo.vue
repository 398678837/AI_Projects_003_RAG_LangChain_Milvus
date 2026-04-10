<template>
  <div class="lifecycle">
    <h1>Vue 生命周期示例</h1>
    
    <div class="section">
      <h2>组件生命周期</h2>
      <p>点击按钮创建或销毁子组件，观察控制台输出的生命周期钩子</p>
      <button @click="toggleComponent">
        {{ showComponent ? '销毁组件' : '创建组件' }}
      </button>
      <child-component v-if="showComponent" :message="message" @update="updateMessage"></child-component>
    </div>
    
    <div class="section">
      <h2>生命周期钩子</h2>
      <ul>
        <li><strong>beforeCreate</strong>: 组件实例创建前</li>
        <li><strong>created</strong>: 组件实例创建后</li>
        <li><strong>beforeMount</strong>: 组件挂载前</li>
        <li><strong>mounted</strong>: 组件挂载后</li>
        <li><strong>beforeUpdate</strong>: 组件更新前</li>
        <li><strong>updated</strong>: 组件更新后</li>
        <li><strong>beforeDestroy</strong>: 组件销毁前</li>
        <li><strong>destroyed</strong>: 组件销毁后</li>
      </ul>
    </div>
    
    <div class="section">
      <h2>生命周期流程图</h2>
      <div class="flowchart">
        <div class="flow-item">beforeCreate</div>
        <div class="flow-arrow">→</div>
        <div class="flow-item">created</div>
        <div class="flow-arrow">→</div>
        <div class="flow-item">beforeMount</div>
        <div class="flow-arrow">→</div>
        <div class="flow-item">mounted</div>
        <div class="flow-arrow">→</div>
        <div class="flow-item">beforeUpdate</div>
        <div class="flow-arrow">→</div>
        <div class="flow-item">updated</div>
        <div class="flow-arrow">→</div>
        <div class="flow-item">beforeDestroy</div>
        <div class="flow-arrow">→</div>
        <div class="flow-item">destroyed</div>
      </div>
    </div>
    
    <div class="section">
      <h2>生命周期的应用场景</h2>
      <ul>
        <li><strong>created</strong>: 初始化数据，发送请求</li>
        <li><strong>mounted</strong>: 操作DOM，绑定事件</li>
        <li><strong>beforeUpdate</strong>: 访问更新前的DOM</li>
        <li><strong>updated</strong>: 操作更新后的DOM</li>
        <li><strong>beforeDestroy</strong>: 清除定时器，解绑事件</li>
      </ul>
    </div>
  </div>
</template>

<script>
import ChildComponent from './ChildComponent.vue';

export default {
  name: 'LifecycleDemo',
  components: {
    ChildComponent
  },
  data() {
    return {
      showComponent: false,
      message: 'Initial message'
    };
  },
  methods: {
    toggleComponent() {
      this.showComponent = !this.showComponent;
    },
    updateMessage() {
      this.message = 'Updated message at ' + new Date().toLocaleTimeString();
    }
  }
};
</script>

<style scoped>
.lifecycle {
  padding: 20px;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #e9e9e9;
}

.flowchart {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
}

.flow-item {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f0f0f0;
  min-width: 120px;
  text-align: center;
}

.flow-arrow {
  font-size: 20px;
  font-weight: bold;
}

ul {
  list-style-type: disc;
  padding-left: 20px;
}

li {
  margin-bottom: 5px;
}
</style>
