# 03_Components_组件

## 学习目标
- 理解组件的概念和作用
- 掌握组件的创建和使用
- 学会组件之间的通信方式
- 理解组件生命周期钩子
- 掌握内容投影和视图封装

## 知识点总结
1. **组件定义**：使用 @Component 装饰器定义组件
2. **组件元数据**：selector、template、templateUrl、styles、styleUrls
3. **组件通信**：
   - 父传子：@Input()
   - 子传父：@Output() 和 EventEmitter
   - 父子双向绑定：[( )] 语法糖
   - 通过服务通信
4. **组件生命周期**：ngOnChanges、ngOnInit、ngDoCheck、ngAfterContentInit、ngAfterContentChecked、ngAfterViewInit、ngAfterViewChecked、ngOnDestroy
5. **内容投影**：使用 ng-content 实现内容插槽
6. **视图封装**：Emulated、Native、None 三种封装模式

## 参考资料
- [Angular 组件概述](https://angular.cn/guide/component-overview)
- [Angular 组件交互](https://angular.cn/guide/component-interaction)
- [Angular 生命周期钩子](https://angular.cn/guide/lifecycle-hooks)
