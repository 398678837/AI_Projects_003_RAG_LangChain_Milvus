<template>
  <div class="child-component-with-event">
    <h3>子组件（带事件）</h3>
    <button @click="sendData">向父组件传递数据</button>
  </div>
</template>

<script>
export default {
  name: 'ChildComponentWithEvent',
  methods: {
    sendData() {
      const data = 'Data from child at ' + new Date().toLocaleTimeString();
      this.$emit('update', data);
    }
  }
};
</script>

<style scoped>
.child-component-with-event {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

button {
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
