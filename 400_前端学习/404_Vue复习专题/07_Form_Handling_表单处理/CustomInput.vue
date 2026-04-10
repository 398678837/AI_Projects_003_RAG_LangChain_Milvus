<template>
  <div class="custom-input">
    <label v-if="label">{{ label }}</label>
    <input
      type="text"
      :value="value"
      @input="$emit('input', $event.target.value)"
      placeholder="请输入内容"
    >
  </div>
</template>

<script>
export default {
  name: 'CustomInput',
  props: {
    value: {
      type: String,
      default: ''
    },
    label: {
      type: String,
      default: ''
    }
  },
  model: {
    prop: 'value',
    event: 'input'
  }
};
</script>

<style scoped>
.custom-input {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}
</style>
