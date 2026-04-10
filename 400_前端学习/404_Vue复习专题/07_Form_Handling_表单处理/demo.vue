<template>
  <div class="form-handling">
    <h1>Vue 表单处理示例</h1>
    
    <!-- 1. 基本表单 -->
    <div class="section">
      <h2>1. 基本表单</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="name">姓名:</label>
          <input type="text" id="name" v-model="form.name" placeholder="请输入姓名">
        </div>
        <div class="form-group">
          <label for="email">邮箱:</label>
          <input type="email" id="email" v-model="form.email" placeholder="请输入邮箱">
        </div>
        <div class="form-group">
          <label for="age">年龄:</label>
          <input type="number" id="age" v-model="form.age" placeholder="请输入年龄">
        </div>
        <button type="submit">提交</button>
      </form>
      <p>表单数据: {{ form }}</p>
    </div>
    
    <!-- 2. 表单验证 -->
    <div class="section">
      <h2>2. 表单验证</h2>
      <form @submit.prevent="handleValidationSubmit">
        <div class="form-group">
          <label for="validation-name">姓名:</label>
          <input type="text" id="validation-name" v-model="validationForm.name" placeholder="请输入姓名">
          <span v-if="errors.name" class="error">{{ errors.name }}</span>
        </div>
        <div class="form-group">
          <label for="validation-email">邮箱:</label>
          <input type="email" id="validation-email" v-model="validationForm.email" placeholder="请输入邮箱">
          <span v-if="errors.email" class="error">{{ errors.email }}</span>
        </div>
        <div class="form-group">
          <label for="validation-age">年龄:</label>
          <input type="number" id="validation-age" v-model="validationForm.age" placeholder="请输入年龄">
          <span v-if="errors.age" class="error">{{ errors.age }}</span>
        </div>
        <button type="submit">提交</button>
      </form>
      <p>验证错误: {{ errors }}</p>
    </div>
    
    <!-- 3. 单选框和复选框 -->
    <div class="section">
      <h2>3. 单选框和复选框</h2>
      <div class="form-group">
        <label>性别:</label>
        <div class="radio-group">
          <label>
            <input type="radio" v-model="form.gender" value="male"> 男
          </label>
          <label>
            <input type="radio" v-model="form.gender" value="female"> 女
          </label>
        </div>
      </div>
      <div class="form-group">
        <label>爱好:</label>
        <div class="checkbox-group">
          <label>
            <input type="checkbox" v-model="form.hobbies" value="reading"> 阅读
          </label>
          <label>
            <input type="checkbox" v-model="form.hobbies" value="sports"> 运动
          </label>
          <label>
            <input type="checkbox" v-model="form.hobbies" value="music"> 音乐
          </label>
        </div>
      </div>
      <p>性别: {{ form.gender }}</p>
      <p>爱好: {{ form.hobbies }}</p>
    </div>
    
    <!-- 4. 下拉选择框 -->
    <div class="section">
      <h2>4. 下拉选择框</h2>
      <div class="form-group">
        <label for="city">城市:</label>
        <select id="city" v-model="form.city">
          <option value="">请选择城市</option>
          <option value="beijing">北京</option>
          <option value="shanghai">上海</option>
          <option value="guangzhou">广州</option>
          <option value="shenzhen">深圳</option>
        </select>
      </div>
      <div class="form-group">
        <label for="skills">技能:</label>
        <select id="skills" v-model="form.skills" multiple>
          <option value="javascript">JavaScript</option>
          <option value="vue">Vue</option>
          <option value="react">React</option>
          <option value="angular">Angular</option>
        </select>
      </div>
      <p>城市: {{ form.city }}</p>
      <p>技能: {{ form.skills }}</p>
    </div>
    
    <!-- 5. 文本域 -->
    <div class="section">
      <h2>5. 文本域</h2>
      <div class="form-group">
        <label for="description">描述:</label>
        <textarea id="description" v-model="form.description" rows="4" placeholder="请输入描述"></textarea>
      </div>
      <p>描述: {{ form.description }}</p>
    </div>
    
    <!-- 6. 修饰符 -->
    <div class="section">
      <h2>6. 修饰符</h2>
      <div class="form-group">
        <label for="lazy">lazy 修饰符:</label>
        <input type="text" id="lazy" v-model.lazy="form.lazyValue" placeholder="输入后失去焦点才更新">
        <p>值: {{ form.lazyValue }}</p>
      </div>
      <div class="form-group">
        <label for="number">number 修饰符:</label>
        <input type="text" id="number" v-model.number="form.numberValue" placeholder="输入数字">
        <p>值: {{ form.numberValue }}, 类型: {{ typeof form.numberValue }}</p>
      </div>
      <div class="form-group">
        <label for="trim">trim 修饰符:</label>
        <input type="text" id="trim" v-model.trim="form.trimValue" placeholder="输入带空格的文本">
        <p>值: '{{ form.trimValue }}', 长度: {{ form.trimValue.length }}</p>
      </div>
    </div>
    
    <!-- 7. 自定义表单组件 -->
    <div class="section">
      <h2>7. 自定义表单组件</h2>
      <custom-input v-model="customValue" label="自定义输入"></custom-input>
      <p>自定义输入值: {{ customValue }}</p>
    </div>
  </div>
</template>

<script>
import CustomInput from './CustomInput.vue';

export default {
  name: 'FormHandlingDemo',
  components: {
    CustomInput
  },
  data() {
    return {
      form: {
        name: '',
        email: '',
        age: '',
        gender: '',
        hobbies: [],
        city: '',
        skills: [],
        description: '',
        lazyValue: '',
        numberValue: '',
        trimValue: ''
      },
      validationForm: {
        name: '',
        email: '',
        age: ''
      },
      errors: {},
      customValue: ''
    };
  },
  methods: {
    handleSubmit() {
      console.log('Form submitted:', this.form);
    },
    handleValidationSubmit() {
      this.errors = {};
      
      if (!this.validationForm.name) {
        this.errors.name = '姓名不能为空';
      }
      
      if (!this.validationForm.email) {
        this.errors.email = '邮箱不能为空';
      } else if (!this.isValidEmail(this.validationForm.email)) {
        this.errors.email = '邮箱格式不正确';
      }
      
      if (!this.validationForm.age) {
        this.errors.age = '年龄不能为空';
      } else if (this.validationForm.age < 18) {
        this.errors.age = '年龄必须大于等于18';
      }
      
      if (Object.keys(this.errors).length === 0) {
        console.log('Validation form submitted:', this.validationForm);
      }
    },
    isValidEmail(email) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    }
  }
};
</script>

<style scoped>
.form-handling {
  padding: 20px;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="number"],
select,
textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

textarea {
  resize: vertical;
}

.radio-group,
.checkbox-group {
  display: flex;
  gap: 15px;
}

.radio-group label,
.checkbox-group label {
  font-weight: normal;
  cursor: pointer;
}

button {
  padding: 10px 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #e9e9e9;
}

.error {
  color: red;
  font-size: 12px;
  margin-top: 5px;
  display: block;
}

p {
  margin-top: 10px;
}
</style>
