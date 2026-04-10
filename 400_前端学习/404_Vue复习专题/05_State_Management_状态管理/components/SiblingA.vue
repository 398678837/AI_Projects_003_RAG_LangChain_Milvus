<template>
  <div class="sibling-a">
    <h3>兄弟组件 A</h3>
    <button @click="sendData">向兄弟组件 B 传递数据</button>
  </div>
</template>

<script>
export default {
  name: 'SiblingA',
  methods: {
    sendData() {
      const data = 'Data from Sibling A at ' + new Date().toLocaleTimeString();
      this.$emit('update', data);
    }
  }
};
</script>

<style scoped>
.sibling-a {
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
