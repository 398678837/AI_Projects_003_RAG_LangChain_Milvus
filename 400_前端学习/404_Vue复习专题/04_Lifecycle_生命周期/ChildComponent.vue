<template>
  <div class="child-component">
    <h3>子组件</h3>
    <p>Message: {{ message }}</p>
    <button @click="updateMessage">更新消息</button>
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
  },
  data() {
    return {
      internalMessage: 'Internal message'
    };
  },
  methods: {
    updateMessage() {
      this.internalMessage = 'Updated internal message at ' + new Date().toLocaleTimeString();
      this.$emit('update');
    }
  },
  beforeCreate() {
    console.log('ChildComponent: beforeCreate');
  },
  created() {
    console.log('ChildComponent: created');
  },
  beforeMount() {
    console.log('ChildComponent: beforeMount');
  },
  mounted() {
    console.log('ChildComponent: mounted');
  },
  beforeUpdate() {
    console.log('ChildComponent: beforeUpdate');
  },
  updated() {
    console.log('ChildComponent: updated');
  },
  beforeDestroy() {
    console.log('ChildComponent: beforeDestroy');
  },
  destroyed() {
    console.log('ChildComponent: destroyed');
  }
};
</script>

<style scoped>
.child-component {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

button {
  margin-top: 10px;
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
