# 04_Lifecycle_生命周期

## 学习目标
- 理解Vue组件的生命周期
- 掌握生命周期钩子的使用方法
- 熟悉生命周期的应用场景
- 学会在不同生命周期阶段执行相应的操作

## 知识点总结
1. **beforeCreate**：组件实例创建前，数据观测和事件配置之前
2. **created**：组件实例创建后，数据观测和事件配置完成
3. **beforeMount**：组件挂载前，模板编译完成
4. **mounted**：组件挂载后，可以操作DOM
5. **beforeUpdate**：组件更新前，数据更新但DOM未更新
6. **updated**：组件更新后，DOM已更新
7. **beforeDestroy**：组件销毁前，清理工作
8. **destroyed**：组件销毁后，实例完全销毁

## 参考资料
- [Vue 生命周期](https://cn.vuejs.org/v2/guide/instance.html#%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90)
- [Vue 生命周期图解](https://cn.vuejs.org/v2/guide/instance.html#%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%9B%BE%E8%A7%A3)
