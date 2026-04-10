<template>
  <div class="child-component">
    <h4>子组件</h4>
    <p>从父组件接收的数据: {{ parentData }}</p>
    <button @click="updateParent">更新父组件数据</button>
  </div>
</template>

<script>
export default {
  name: 'ChildComponent',
  props: {
    parentData: {
      type: String,
      default: ''
    }
  },
  methods: {
    updateParent() {
      this.$emit('update-parent', 'Data from child component');
    }
  }
};
</script>

<style scoped>
.child-component {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f0f0f0;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #e0e0e0;
  cursor: pointer;
}

button:hover {
  background-color: #d0d0d0;
}
</style>
