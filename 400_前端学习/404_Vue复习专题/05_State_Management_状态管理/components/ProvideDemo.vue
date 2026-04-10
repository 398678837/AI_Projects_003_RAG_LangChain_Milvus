<template>
  <div class="provide-demo">
    <h3>Provide 组件</h3>
    <p>Provided message: {{ message }}</p>
    <button @click="updateMessage">更新消息</button>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'ProvideDemo',
  data() {
    return {
      message: 'Hello from provide'
    };
  },
  provide() {
    return {
      providedMessage: this.message
    };
  },
  methods: {
    updateMessage() {
      this.message = 'Updated message at ' + new Date().toLocaleTimeString();
    }
  }
};
</script>

<style scoped>
.provide-demo {
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
