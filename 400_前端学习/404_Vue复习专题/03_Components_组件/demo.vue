<template>
  <div class="components">
    <h1>Vue 组件示例</h1>
    
    <!-- 1. 基本组件 -->
    <div class="section">
      <h2>1. 基本组件</h2>
      <basic-component></basic-component>
    </div>
    
    <!-- 2. 组件传参 -->
    <div class="section">
      <h2>2. 组件传参</h2>
      <props-component :message="message" :count="count" :user="user"></props-component>
    </div>
    
    <!-- 3. 组件事件 -->
    <div class="section">
      <h2>3. 组件事件</h2>
      <event-component @custom-event="handleCustomEvent"></event-component>
      <p>事件数据: {{ eventData }}</p>
    </div>
    
    <!-- 4. 组件插槽 -->
    <div class="section">
      <h2>4. 组件插槽</h2>
      <slot-component>
        <template v-slot:header>
          <h3>自定义头部</h3>
        </template>
        <p>默认插槽内容</p>
        <template v-slot:footer>
          <p>自定义底部</p>
        </template>
      </slot-component>
    </div>
    
    <!-- 5. 作用域插槽 -->
    <div class="section">
      <h2>5. 作用域插槽</h2>
      <scope-slot-component>
        <template v-slot:default="slotProps">
          <p>作用域插槽数据: {{ slotProps.item }}</p>
        </template>
      </scope-slot-component>
    </div>
    
    <!-- 6. 动态组件 -->
    <div class="section">
      <h2>6. 动态组件</h2>
      <button @click="currentComponent = 'component-a'">组件 A</button>
      <button @click="currentComponent = 'component-b'">组件 B</button>
      <component :is="currentComponent"></component>
    </div>
    
    <!-- 7. 异步组件 -->
    <div class="section">
      <h2>7. 异步组件</h2>
      <async-component></async-component>
    </div>
    
    <!-- 8. 组件通信 -->
    <div class="section">
      <h2>8. 组件通信</h2>
      <parent-component></parent-component>
    </div>
    
    <!-- 9. 组件生命周期 -->
    <div class="section">
      <h2>9. 组件生命周期</h2>
      <lifecycle-component v-if="showLifecycleComponent"></lifecycle-component>
      <button @click="showLifecycleComponent = !showLifecycleComponent">
        {{ showLifecycleComponent ? '销毁组件' : '创建组件' }}
      </button>
    </div>
    
    <!-- 10. 组件样式 -->
    <div class="section">
      <h2>10. 组件样式</h2>
      <style-component></style-component>
    </div>
  </div>
</template>

<script>
// 导入组件
import BasicComponent from './components/BasicComponent.vue';
import PropsComponent from './components/PropsComponent.vue';
import EventComponent from './components/EventComponent.vue';
import SlotComponent from './components/SlotComponent.vue';
import ScopeSlotComponent from './components/ScopeSlotComponent.vue';
import ComponentA from './components/ComponentA.vue';
import ComponentB from './components/ComponentB.vue';
import AsyncComponent from './components/AsyncComponent.vue';
import ParentComponent from './components/ParentComponent.vue';
import LifecycleComponent from './components/LifecycleComponent.vue';
import StyleComponent from './components/StyleComponent.vue';

export default {
  name: 'ComponentsDemo',
  components: {
    BasicComponent,
    PropsComponent,
    EventComponent,
    SlotComponent,
    ScopeSlotComponent,
    ComponentA,
    ComponentB,
    AsyncComponent,
    ParentComponent,
    LifecycleComponent,
    StyleComponent
  },
  data() {
    return {
      message: 'Hello from parent',
      count: 42,
      user: {
        name: 'John',
        age: 30
      },
      eventData: '',
      currentComponent: 'component-a',
      showLifecycleComponent: true
    };
  },
  methods: {
    handleCustomEvent(data) {
      this.eventData = data;
      console.log('Custom event received:', data);
    }
  }
};
</script>

<style scoped>
.components {
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
