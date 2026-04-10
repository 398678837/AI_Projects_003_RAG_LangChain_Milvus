<template>
  <div class="child-component">
    <h3>子组件</h3>
    <p>Received message: {{ message }}</p>
  </div>
</template>

<script>
export default {
  name: 'ChildComponent',
  props: {
    message: {
      type: String,
      default: ''
    }
  }
};
</script>

<style scoped>
.child-component {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}
</style>
