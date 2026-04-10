<template>
  <div class="inject-demo">
    <h3>Inject 组件</h3>
    <p>Injected message: {{ providedMessage }}</p>
  </div>
</template>

<script>
export default {
  name: 'InjectDemo',
  inject: ['providedMessage']
};
</script>

<style scoped>
.inject-demo {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}
</style>
