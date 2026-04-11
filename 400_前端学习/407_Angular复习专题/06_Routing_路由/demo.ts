// Angular 路由示例代码

import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes, Router, ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

// 1. 页面组件
@Component({
  template: `
    <div class="page">
      <h2>首页</h2>
      <p>欢迎来到首页！</p>
    </div>
  `,
  styles: ['.page { padding: 20px; }']
})
export class HomeComponent { }

@Component({
  template: `
    <div class="page">
      <h2>关于我们</h2>
      <p>这是关于页面。</p>
    </div>
  `,
  styles: ['.page { padding: 20px; }']
})
export class AboutComponent { }

@Component({
  template: `
    <div class="page">
      <h2>用户详情</h2>
      <p>用户ID: {{ userId }}</p>
      <p>用户名: {{ userName }}</p>
      <button (click)="goBack()">返回</button>
    </div>
  `,
  styles: ['.page { padding: 20px; }']
})
export class UserDetailComponent {
  userId: string = '';
  userName: string = '';

  constructor(private route: ActivatedRoute, private router: Router) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.userId = params['id'];
      this.userName = this.getUserName(this.userId);
    });
    
    this.route.queryParams.subscribe(queryParams => {
      console.log('查询参数:', queryParams);
    });
  }

  getUserName(id: string): string {
    const users: { [key: string]: string } = {
      '1': '张三',
      '2': '李四',
      '3': '王五'
    };
    return users[id] || '未知用户';
  }

  goBack() {
    this.router.navigate(['/users']);
  }
}

@Component({
  template: `
    <div class="page">
      <h2>用户列表</h2>
      <ul>
        <li *ngFor="let user of users">
          <a [routerLink]="['/users', user.id]" [queryParams]="{ ref: 'list' }">
            {{ user.name }}
          </a>
        </li>
      </ul>
    </div>
  `,
  styles: ['.page { padding: 20px; }']
})
export class UsersComponent {
  users = [
    { id: '1', name: '张三' },
    { id: '2', name: '李四' },
    { id: '3', name: '王五' }
  ];
}

@Component({
  template: `
    <div class="page">
      <h2>产品中心</h2>
      <nav>
        <a routerLink="./list" routerLinkActive="active">产品列表</a>
        <a routerLink="./detail" routerLinkActive="active">产品详情</a>
      </nav>
      <router-outlet></router-outlet>
    </div>
  `,
  styles: ['.page { padding: 20px; } nav a { margin-right: 15px; } .active { color: blue; font-weight: bold; }']
})
export class ProductsComponent { }

@Component({
  template: `
    <div class="sub-page">
      <h3>产品列表</h3>
      <ul>
        <li>产品A</li>
        <li>产品B</li>
        <li>产品C</li>
      </ul>
    </div>
  `,
  styles: ['.sub-page { padding: 15px; background: #f5f5f5; margin-top: 10px; }']
})
export class ProductListComponent { }

@Component({
  template: `
    <div class="sub-page">
      <h3>产品详情</h3>
      <p>这是产品详情页面</p>
    </div>
  `,
  styles: ['.sub-page { padding: 15px; background: #f5f5f5; margin-top: 10px; }']
})
export class ProductDetailComponent { }

@Component({
  template: `
    <div class="page">
      <h2>404 - 页面未找到</h2>
      <p>抱歉，您访问的页面不存在。</p>
      <a routerLink="/">返回首页</a>
    </div>
  `,
  styles: ['.page { padding: 20px; }']
})
export class NotFoundComponent { }

// 2. 路由配置
const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'users', component: UsersComponent },
  { path: 'users/:id', component: UserDetailComponent },
  { 
    path: 'products', 
    component: ProductsComponent,
    children: [
      { path: '', redirectTo: 'list', pathMatch: 'full' },
      { path: 'list', component: ProductListComponent },
      { path: 'detail', component: ProductDetailComponent }
    ]
  },
  { path: '**', component: NotFoundComponent }
];

// 3. 导航组件
@Component({
  selector: 'app-nav',
  template: `
    <nav class="navbar">
      <a routerLink="/" routerLinkActive="active" [routerLinkActiveOptions]="{ exact: true }">首页</a>
      <a routerLink="/about" routerLinkActive="active">关于</a>
      <a routerLink="/users" routerLinkActive="active">用户</a>
      <a routerLink="/products" routerLinkActive="active">产品</a>
    </nav>
  `,
  styles: [`
    .navbar { padding: 15px; background: #333; margin-bottom: 20px; }
    .navbar a { color: white; text-decoration: none; margin-right: 20px; }
    .navbar a:hover { text-decoration: underline; }
    .navbar a.active { color: #4CAF50; font-weight: bold; }
  `]
})
export class NavComponent { }

// 4. 编程导航组件
@Component({
  selector: 'app-programmatic-nav',
  template: `
    <div class="section">
      <h3>编程式导航</h3>
      <button (click)="goHome()">去首页</button>
      <button (click)="goToAbout()">去关于</button>
      <button (click)="goToUser(1)">去用户1</button>
      <button (click)="goToUser(2)">去用户2</button>
    </div>
  `,
  styles: ['.section { padding: 15px; background: #f5f5f5; margin: 20px 0; } button { margin: 5px; }']
})
export class ProgrammaticNavComponent {
  constructor(private router: Router) { }

  goHome() {
    this.router.navigate(['/home']);
  }

  goToAbout() {
    this.router.navigate(['/about']);
  }

  goToUser(id: number) {
    this.router.navigate(['/users', id], { queryParams: { source: 'button' } });
  }
}

// 5. 主组件
@Component({
  selector: 'app-routing-demo',
  template: `
    <h2>Angular 路由示例</h2>
    <app-nav></app-nav>
    <app-programmatic-nav></app-programmatic-nav>
    <router-outlet></router-outlet>
  `
})
export class RoutingDemoComponent { }

// 6. 路由模块
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    RouterModule.forChild(routes)
  ],
  declarations: [
    HomeComponent,
    AboutComponent,
    UserDetailComponent,
    UsersComponent,
    ProductsComponent,
    ProductListComponent,
    ProductDetailComponent,
    NotFoundComponent,
    NavComponent,
    ProgrammaticNavComponent,
    RoutingDemoComponent
  ]
})
export class RoutingDemoModule { }
