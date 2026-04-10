<template>
  <div class="parent-component">
    <h3>父组件</h3>
    <p>父组件数据: {{ parentData }}</p>
    <button @click="updateChildData">更新子组件数据</button>
    <child-component :parent-data="parentData" @update-parent="updateParentData"></child-component>
  </div>
</template>

<script>
import ChildComponent from './ChildComponent.vue';

export default {
  name: 'ParentComponent',
  components: {
    ChildComponent
  },
  data() {
    return {
      parentData: 'Parent data'
    };
  },
  methods: {
    updateChildData() {
      this.parentData = 'Updated parent data';
    },
    updateParentData(data) {
      this.parentData = data;
    }
  }
};
</script>

<style scoped>
.parent-component {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

button {
  margin: 10px 0;
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
