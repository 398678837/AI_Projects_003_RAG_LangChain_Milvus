// Angular HTTP 网络请求示例代码

import { Injectable, Component, NgModule } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams, HttpErrorResponse, HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Observable, throwError, of } from 'rxjs';
import { catchError, retry, map, tap } from 'rxjs/operators';

// 1. 数据模型
interface User {
  id?: number;
  name: string;
  email: string;
  username?: string;
}

interface Post {
  id?: number;
  title: string;
  body: string;
  userId: number;
}

// 2. HTTP 服务
@Injectable({
  providedIn: 'root'
})
export class DataService {
  private apiUrl = 'https://jsonplaceholder.typicode.com';

  constructor(private http: HttpClient) { }

  // GET 请求 - 获取所有用户
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(`${this.apiUrl}/users`).pipe(
      retry(1),
      catchError(this.handleError<User[]>('getUsers', []))
    );
  }

  // GET 请求 - 获取单个用户
  getUser(id: number): Observable<User> {
    const url = `${this.apiUrl}/users/${id}`;
    return this.http.get<User>(url).pipe(
      catchError(this.handleError<User>(`getUser id=${id}`))
    );
  }

  // GET 请求 - 带查询参数
  getPosts(params?: { userId?: number; _limit?: number }): Observable<Post[]> {
    let httpParams = new HttpParams();
    if (params) {
      if (params.userId) {
        httpParams = httpParams.set('userId', params.userId.toString());
      }
      if (params._limit) {
        httpParams = httpParams.set('_limit', params._limit.toString());
      }
    }

    return this.http.get<Post[]>(`${this.apiUrl}/posts`, { params: httpParams }).pipe(
      catchError(this.handleError<Post[]>('getPosts', []))
    );
  }

  // POST 请求 - 创建用户
  createUser(user: User): Observable<User> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };

    return this.http.post<User>(`${this.apiUrl}/users`, user, httpOptions).pipe(
      catchError(this.handleError<User>('createUser'))
    );
  }

  // PUT 请求 - 更新用户
  updateUser(user: User): Observable<User> {
    const url = `${this.apiUrl}/users/${user.id}`;
    return this.http.put<User>(url, user).pipe(
      catchError(this.handleError<User>('updateUser'))
    );
  }

  // DELETE 请求 - 删除用户
  deleteUser(id: number): Observable<{}> {
    const url = `${this.apiUrl}/users/${id}`;
    return this.http.delete(url).pipe(
      catchError(this.handleError('deleteUser'))
    );
  }

  // 错误处理
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: HttpErrorResponse): Observable<T> => {
      console.error(`${operation} failed: ${error.message}`);
      
      if (error.error instanceof ErrorEvent) {
        console.error('客户端错误:', error.error.message);
      } else {
        console.error(`服务器错误 ${error.status}, 内容: ${error.error}`);
      }
      
      return of(result as T);
    };
  }
}

// 3. HTTP 拦截器
@Injectable()
export class LoggingInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    console.log('请求 URL:', req.url);
    console.log('请求方法:', req.method);
    
    const modifiedReq = req.clone({
      headers: req.headers.set('X-Custom-Header', 'MyCustomValue')
    });
    
    return next.handle(modifiedReq).pipe(
      tap(event => {
        console.log('响应事件:', event);
      })
    );
  }
}

// 4. 用户列表组件
@Component({
  selector: 'app-user-list',
  template: `
    <div class="component">
      <h3>用户列表</h3>
      <button (click)="loadUsers()">刷新用户</button>
      <div *ngIf="loading" class="loading">加载中...</div>
      <ul *ngIf="!loading">
        <li *ngFor="let user of users" (click)="selectUser(user)">
          {{ user.name }} - {{ user.email }}
        </li>
      </ul>
    </div>
  `,
  styles: [`
    .component { padding: 15px; background: #e3f2fd; border-radius: 5px; margin: 10px 0; }
    .loading { color: #666; font-style: italic; }
    ul { list-style: none; padding: 0; }
    li { padding: 8px; border-bottom: 1px solid #ddd; cursor: pointer; }
    li:hover { background: #f5f5f5; }
  `]
})
export class UserListComponent {
  users: User[] = [];
  loading = false;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.loadUsers();
  }

  loadUsers() {
    this.loading = true;
    this.dataService.getUsers().subscribe({
      next: users => {
        this.users = users;
        this.loading = false;
      },
      error: err => {
        console.error('加载用户失败:', err);
        this.loading = false;
      }
    });
  }

  selectUser(user: User) {
    console.log('选中用户:', user);
  }
}

// 5. 用户详情组件
@Component({
  selector: 'app-user-detail',
  template: `
    <div class="component">
      <h3>用户详情</h3>
      <div *ngIf="selectedUser">
        <p><strong>ID:</strong> {{ selectedUser.id }}</p>
        <p><strong>姓名:</strong> {{ selectedUser.name }}</p>
        <p><strong>邮箱:</strong> {{ selectedUser.email }}</p>
        <p><strong>用户名:</strong> {{ selectedUser.username }}</p>
      </div>
      <div *ngIf="!selectedUser">
        <p>请选择一个用户</p>
      </div>
    </div>
  `,
  styles: ['.component { padding: 15px; background: #fff3e0; border-radius: 5px; margin: 10px 0; }']
})
export class UserDetailComponent {
  @Input() selectedUser: User | null = null;
}

// 6. 创建用户组件
@Component({
  selector: 'app-create-user',
  template: `
    <div class="component">
      <h3>创建用户</h3>
      <div class="form-group">
        <label>姓名:</label>
        <input [(ngModel)]="newUser.name" placeholder="输入姓名">
      </div>
      <div class="form-group">
        <label>邮箱:</label>
        <input [(ngModel)]="newUser.email" placeholder="输入邮箱">
      </div>
      <button (click)="createUser()" [disabled]="!newUser.name || !newUser.email">创建</button>
      <div *ngIf="createdUser" class="success">
        用户创建成功！ID: {{ createdUser.id }}
      </div>
    </div>
  `,
  styles: [`
    .component { padding: 15px; background: #e8f5e9; border-radius: 5px; margin: 10px 0; }
    .form-group { margin-bottom: 10px; }
    .form-group label { display: block; margin-bottom: 5px; }
    .form-group input { width: 100%; padding: 8px; box-sizing: border-box; }
    button { padding: 10px 20px; }
    .success { margin-top: 10px; padding: 10px; background: #c8e6c9; border-radius: 4px; }
  `]
})
export class CreateUserComponent {
  newUser: User = { name: '', email: '' };
  createdUser: User | null = null;

  constructor(private dataService: DataService) { }

  createUser() {
    this.dataService.createUser(this.newUser).subscribe({
      next: user => {
        this.createdUser = user;
        this.newUser = { name: '', email: '' };
      },
      error: err => console.error('创建用户失败:', err)
    });
  }
}

// 7. 主组件
@Component({
  selector: 'app-http-demo',
  template: `
    <h2>Angular HTTP 网络请求示例</h2>
    
    <div class="container">
      <app-user-list></app-user-list>
      <app-create-user></app-create-user>
    </div>
    
    <div class="info">
      <h4>说明:</h4>
      <p>本示例使用 JSONPlaceholder API 进行演示</p>
      <p>支持的操作: 获取用户、创建用户、获取帖子</p>
    </div>
  `,
  styles: [`
    .container { display: flex; gap: 20px; flex-wrap: wrap; }
    .container > * { flex: 1; min-width: 300px; }
    .info { margin-top: 20px; padding: 15px; background: #f5f5f5; border-radius: 5px; }
  `]
})
export class HttpDemoComponent { }

// 8. HTTP 模块
@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
    UserListComponent,
    UserDetailComponent,
    CreateUserComponent,
    HttpDemoComponent
  ]
})
export class HttpDemoModule { }
