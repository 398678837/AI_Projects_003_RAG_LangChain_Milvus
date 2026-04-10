<template>
  <div class="composition-api-demo">
    <h3>Composition API 状态管理</h3>
    <p>Count: {{ count }}</p>
    <button @click="increment">增加</button>
    <button @click="decrement">减少</button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'CompositionApiDemo',
  setup() {
    const count = ref(0);
    
    const increment = () => {
      count.value++;
    };
    
    const decrement = () => {
      count.value--;
    };
    
    return {
      count,
      increment,
      decrement
    };
  }
};
</script>

<style scoped>
.composition-api-demo {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

button {
  margin-right: 10px;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f0f0f0;
  cursor: pointer;
}

button:hover {
  background-color: #e0e0e0;
}
</style>
