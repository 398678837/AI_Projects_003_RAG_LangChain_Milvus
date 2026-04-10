<template>
  <div class="scope-slot-component">
    <h3>作用域插槽</h3>
    <div v-for="item in items" :key="item.id">
      <slot :item="item"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ScopeSlotComponent',
  data() {
    return {
      items: [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' },
        { id: 3, name: 'Item 3' }
      ]
    };
  }
};
</script>

<style scoped>
.scope-slot-component {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

div {
  margin-bottom: 5px;
}
</style>
