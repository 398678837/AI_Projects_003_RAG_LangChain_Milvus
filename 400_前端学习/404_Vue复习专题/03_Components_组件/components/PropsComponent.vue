<template>
  <div class="props-component">
    <h3>组件传参</h3>
    <p>Message: {{ message }}</p>
    <p>Count: {{ count }}</p>
    <p>User: {{ user.name }}, {{ user.age }} years old</p>
  </div>
</template>

<script>
export default {
  name: 'PropsComponent',
  props: {
    message: {
      type: String,
      default: 'Default message'
    },
    count: {
      type: Number,
      required: true
    },
    user: {
      type: Object,
      default: () => ({})
    }
  }
};
</script>

<style scoped>
.props-component {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}
</style>
