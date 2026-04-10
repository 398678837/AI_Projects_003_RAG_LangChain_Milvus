<template>
  <div class="style-component">
    <h3>组件样式</h3>
    <p class="text">这是一个使用scoped样式的组件</p>
    <p class="global-text">这是一个使用全局样式的元素</p>
  </div>
</template>

<script>
export default {
  name: 'StyleComponent'
};
</script>

<style scoped>
.style-component {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.text {
  color: blue;
  font-size: 16px;
}
</style>

<style>
.global-text {
  color: red;
  font-size: 14px;
  font-weight: bold;
}
</style>
