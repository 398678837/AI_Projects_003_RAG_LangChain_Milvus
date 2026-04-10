<template>
  <div class="my-component">
    <h3>子组件</h3>
    <p>{{ message }}</p>
    <button @click="emitEvent">触发事件</button>
  </div>
</template>

<script>
export default {
  name: 'MyComponent',
  props: {
    message: {
      type: String,
      default: 'Hello from component'
    }
  },
  methods: {
    emitEvent() {
      this.$emit('custom-event', { data: 'Event data' });
    }
  }
};
</script>

<style scoped>
.my-component {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}
</style>
