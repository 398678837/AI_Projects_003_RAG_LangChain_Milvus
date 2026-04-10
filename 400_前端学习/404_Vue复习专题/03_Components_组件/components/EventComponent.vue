<template>
  <div class="event-component">
    <h3>组件事件</h3>
    <button @click="emitEvent">触发自定义事件</button>
  </div>
</template>

<script>
export default {
  name: 'EventComponent',
  methods: {
    emitEvent() {
      this.$emit('custom-event', {
        message: 'Hello from child component',
        timestamp: new Date().toISOString()
      });
    }
  }
};
</script>

<style scoped>
.event-component {
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
