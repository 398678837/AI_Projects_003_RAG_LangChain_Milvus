// Angular 状态管理示例代码

import { Injectable, Component, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { BehaviorSubject, Observable, combineLatest, map } from 'rxjs';

// 1. Todo 模型
interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

interface AppState {
  todos: Todo[];
  filter: 'all' | 'active' | 'completed';
  user: { name: string; isLoggedIn: boolean } | null;
}

// 2. 使用 RxJS 的状态管理服务
@Injectable({
  providedIn: 'root'
})
export class StateService {
  private initialState: AppState = {
    todos: [],
    filter: 'all',
    user: null
  };

  private stateSubject = new BehaviorSubject<AppState>(this.initialState);
  state$: Observable<AppState> = this.stateSubject.asObservable();

  // 选择器 - 获取 todos
  todos$: Observable<Todo[]> = this.state$.pipe(
    map(state => state.todos)
  );

  // 选择器 - 获取过滤后的 todos
  filteredTodos$: Observable<Todo[]> = combineLatest([
    this.state$.pipe(map(state => state.todos)),
    this.state$.pipe(map(state => state.filter))
  ]).pipe(
    map(([todos, filter]) => {
      switch (filter) {
        case 'active':
          return todos.filter(todo => !todo.completed);
        case 'completed':
          return todos.filter(todo => todo.completed);
        default:
          return todos;
      }
    })
  );

  // 选择器 - 获取统计信息
  todoStats$: Observable<{ total: number; active: number; completed: number }> = this.todos$.pipe(
    map(todos => ({
      total: todos.length,
      active: todos.filter(t => !t.completed).length,
      completed: todos.filter(t => t.completed).length
    }))
  );

  // 选择器 - 获取用户
  user$: Observable<{ name: string; isLoggedIn: boolean } | null> = this.state$.pipe(
    map(state => state.user)
  );

  private get state(): AppState {
    return this.stateSubject.value;
  }

  // 添加 todo
  addTodo(text: string) {
    const newTodo: Todo = {
      id: Date.now(),
      text,
      completed: false
    };
    this.setState({
      todos: [...this.state.todos, newTodo]
    });
  }

  // 切换 todo 完成状态
  toggleTodo(id: number) {
    const todos = this.state.todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    );
    this.setState({ todos });
  }

  // 删除 todo
  deleteTodo(id: number) {
    const todos = this.state.todos.filter(todo => todo.id !== id);
    this.setState({ todos });
  }

  // 清除已完成的 todos
  clearCompleted() {
    const todos = this.state.todos.filter(todo => !todo.completed);
    this.setState({ todos });
  }

  // 设置过滤器
  setFilter(filter: 'all' | 'active' | 'completed') {
    this.setState({ filter });
  }

  // 登录
  login(name: string) {
    this.setState({
      user: { name, isLoggedIn: true }
    });
  }

  // 退出登录
  logout() {
    this.setState({
      user: null
    });
  }

  // 重置状态
  resetState() {
    this.stateSubject.next(this.initialState);
  }

  private setState(partialState: Partial<AppState>) {
    this.stateSubject.next({
      ...this.state,
      ...partialState
    });
  }
}

// 3. Todo 列表组件
@Component({
  selector: 'app-todo-list',
  template: `
    <div class="todo-container">
      <h3>Todo 列表</h3>
      
      <div class="add-todo">
        <input 
          [(ngModel)]="newTodoText" 
          (keyup.enter)="addTodo()"
          placeholder="添加新的 todo..."
          [disabled]="!isLoggedIn">
        <button (click)="addTodo()" [disabled]="!newTodoText || !isLoggedIn">添加</button>
      </div>
      
      <div class="filters">
        <button 
          *ngFor="let f of filters"
          (click)="setFilter(f)"
          [class.active]="filter === f">
          {{ f | uppercase }}
        </button>
      </div>
      
      <ul class="todo-list">
        <li *ngFor="let todo of filteredTodos$ | async" [class.completed]="todo.completed">
          <input 
            type="checkbox" 
            [checked]="todo.completed"
            (change)="toggleTodo(todo.id)"
            [disabled]="!isLoggedIn">
          <span>{{ todo.text }}</span>
          <button (click)="deleteTodo(todo.id)" [disabled]="!isLoggedIn">×</button>
        </li>
      </ul>
      
      <div class="stats" *ngIf="todoStats$ | async as stats">
        <span>总计: {{ stats.total }}</span>
        <span>进行中: {{ stats.active }}</span>
        <span>已完成: {{ stats.completed }}</span>
        <button (click)="clearCompleted()" *ngIf="stats.completed > 0" [disabled]="!isLoggedIn">
          清除已完成
        </button>
      </div>
    </div>
  `,
  styles: [`
    .todo-container { padding: 20px; background: #f5f5f5; border-radius: 5px; }
    .add-todo { margin-bottom: 15px; display: flex; gap: 10px; }
    .add-todo input { flex: 1; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
    .filters { margin-bottom: 15px; display: flex; gap: 10px; }
    .filters button { padding: 5px 15px; border: 1px solid #ddd; background: white; cursor: pointer; }
    .filters button.active { background: #2196f3; color: white; border-color: #2196f3; }
    .todo-list { list-style: none; padding: 0; margin: 0 0 15px 0; }
    .todo-list li { display: flex; align-items: center; padding: 10px; background: white; margin-bottom: 5px; border-radius: 4px; }
    .todo-list li.completed span { text-decoration: line-through; color: #999; }
    .todo-list li span { flex: 1; margin: 0 10px; }
    .todo-list li button { background: #ff5252; color: white; border: none; width: 25px; height: 25px; border-radius: 50%; cursor: pointer; }
    .stats { display: flex; gap: 20px; align-items: center; padding-top: 15px; border-top: 1px solid #ddd; }
    button:disabled { opacity: 0.5; cursor: not-allowed; }
  `]
})
export class TodoListComponent {
  newTodoText = '';
  filters: Array<'all' | 'active' | 'completed'> = ['all', 'active', 'completed'];
  filter: 'all' | 'active' | 'completed' = 'all';
  filteredTodos$ = this.stateService.filteredTodos$;
  todoStats$ = this.stateService.todoStats$;
  isLoggedIn = false;

  constructor(private stateService: StateService) { }

  ngOnInit() {
    this.stateService.user$.subscribe(user => {
      this.isLoggedIn = user?.isLoggedIn || false;
    });
  }

  addTodo() {
    if (this.newTodoText.trim()) {
      this.stateService.addTodo(this.newTodoText.trim());
      this.newTodoText = '';
    }
  }

  toggleTodo(id: number) {
    this.stateService.toggleTodo(id);
  }

  deleteTodo(id: number) {
    this.stateService.deleteTodo(id);
  }

  clearCompleted() {
    this.stateService.clearCompleted();
  }

  setFilter(filter: 'all' | 'active' | 'completed') {
    this.filter = filter;
    this.stateService.setFilter(filter);
  }
}

// 4. 用户认证组件
@Component({
  selector: 'app-auth',
  template: `
    <div class="auth-container">
      <h3>用户认证</h3>
      <div *ngIf="!isLoggedIn">
        <input 
          [(ngModel)]="username" 
          placeholder="输入用户名"
          (keyup.enter)="login()">
        <button (click)="login()" [disabled]="!username">登录</button>
      </div>
      <div *ngIf="isLoggedIn" class="logged-in">
        <p>欢迎, {{ user?.name }}!</p>
        <button (click)="logout()">退出登录</button>
      </div>
    </div>
  `,
  styles: [`
    .auth-container { padding: 20px; background: #e3f2fd; border-radius: 5px; margin-top: 20px; }
    .auth-container input { padding: 8px; margin-right: 10px; border: 1px solid #ddd; border-radius: 4px; }
    .auth-container button { padding: 8px 20px; }
    .logged-in { display: flex; justify-content: space-between; align-items: center; }
  `]
})
export class AuthComponent {
  username = '';
  user: { name: string; isLoggedIn: boolean } | null = null;
  isLoggedIn = false;

  constructor(private stateService: StateService) { }

  ngOnInit() {
    this.stateService.user$.subscribe(user => {
      this.user = user;
      this.isLoggedIn = user?.isLoggedIn || false;
    });
  }

  login() {
    if (this.username.trim()) {
      this.stateService.login(this.username.trim());
      this.username = '';
    }
  }

  logout() {
    this.stateService.logout();
  }
}

// 5. 主组件
@Component({
  selector: 'app-state-management-demo',
  template: `
    <h2>Angular 状态管理示例</h2>
    
    <app-auth></app-auth>
    <app-todo-list></app-todo-list>
    
    <div class="info">
      <h4>状态管理说明:</h4>
      <ul>
        <li>使用 BehaviorSubject 存储状态</li>
        <li>使用 Observable 暴露状态</li>
        <li>使用选择器派生状态</li>
        <li>通过服务方法修改状态</li>
      </ul>
    </div>
  `,
  styles: ['.info { margin-top: 20px; padding: 15px; background: #f5f5f5; border-radius: 5px; }']
})
export class StateManagementDemoComponent { }

// 6. 状态管理模块
@NgModule({
  imports: [
    CommonModule,
    FormsModule
  ],
  declarations: [
    TodoListComponent,
    AuthComponent,
    StateManagementDemoComponent
  ]
})
export class StateManagementDemoModule { }
