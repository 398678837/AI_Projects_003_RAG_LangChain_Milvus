<template>
  <div class="sibling-b">
    <h3>兄弟组件 B</h3>
    <p>Received data: {{ data }}</p>
  </div>
</template>

<script>
export default {
  name: 'SiblingB',
  props: {
    data: {
      type: String,
      default: ''
    }
  }
};
</script>

<style scoped>
.sibling-b {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}
</style>
