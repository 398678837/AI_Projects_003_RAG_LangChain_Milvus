<template>
  <div class="slot-component">
    <h3>组件插槽</h3>
    <div class="header">
      <slot name="header">默认头部</slot>
    </div>
    <div class="content">
      <slot>默认内容</slot>
    </div>
    <div class="footer">
      <slot name="footer">默认底部</slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SlotComponent'
};
</script>

<style scoped>
.slot-component {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.header {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #e9e9e9;
  border-radius: 4px;
}

.content {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 4px;
}

.footer {
  padding: 10px;
  background-color: #e9e9e9;
  border-radius: 4px;
}
</style>
