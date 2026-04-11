# 07_Forms_表单

## 学习目标
- 理解模板驱动表单和响应式表单的区别
- 掌握模板驱动表单的使用
- 掌握响应式表单的使用
- 学会表单验证
- 理解表单状态管理

## 知识点总结
1. **表单类型**：
   - 模板驱动表单：使用 ngModel，适合简单表单
   - 响应式表单：使用 FormGroup、FormControl，适合复杂表单
2. **模板驱动表单**：
   - 导入 FormsModule
   - 使用 ngModel 进行双向绑定
   - 使用 name 属性标识表单控件
3. **响应式表单**：
   - 导入 ReactiveFormsModule
   - 使用 FormBuilder 创建表单
   - 使用 formGroup、formControlName 绑定
4. **表单验证**：
   - 内置验证器：required、minLength、maxLength、pattern、email
   - 自定义验证器
   - 异步验证器
5. **表单状态**：
   - touched、untouched
   - dirty、pristine
   - valid、invalid
   - errors

## 参考资料
- [Angular 表单](https://angular.cn/guide/forms-overview)
- [Angular 模板驱动表单](https://angular.cn/guide/forms)
- [Angular 响应式表单](https://angular.cn/guide/reactive-forms)
