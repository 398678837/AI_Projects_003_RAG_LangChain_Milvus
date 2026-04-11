// Angular 表示例代码

import { Component, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, NgForm } from '@angular/forms';
import { ReactiveFormsModule, FormBuilder, FormGroup, FormControl, Validators, AbstractControl, ValidationErrors } from '@angular/forms';

// 1. 自定义验证器
export function forbiddenNameValidator(nameRe: RegExp): (control: AbstractControl) => ValidationErrors | null {
  return (control: AbstractControl): ValidationErrors | null => {
    const forbidden = nameRe.test(control.value);
    return forbidden ? { forbiddenName: { value: control.value } } : null;
  };
}

// 2. 模板驱动表单组件
@Component({
  selector: 'app-template-driven-form',
  template: `
    <div class="form-container">
      <h3>模板驱动表单</h3>
      <form #userForm="ngForm" (ngSubmit)="onSubmit(userForm)">
        <div class="form-group">
          <label>姓名:</label>
          <input 
            type="text" 
            name="name" 
            [(ngModel)]="user.name"
            required
            minlength="2"
            maxlength="20"
            #name="ngModel">
          <div *ngIf="name.invalid && (name.dirty || name.touched)" class="error">
            <div *ngIf="name.errors?.['required']">姓名是必填的</div>
            <div *ngIf="name.errors?.['minlength']">姓名至少2个字符</div>
            <div *ngIf="name.errors?.['maxlength']">姓名最多20个字符</div>
          </div>
        </div>
        
        <div class="form-group">
          <label>邮箱:</label>
          <input 
            type="email" 
            name="email" 
            [(ngModel)]="user.email"
            required
            email
            #email="ngModel">
          <div *ngIf="email.invalid && (email.dirty || email.touched)" class="error">
            <div *ngIf="email.errors?.['required']">邮箱是必填的</div>
            <div *ngIf="email.errors?.['email']">请输入有效的邮箱地址</div>
          </div>
        </div>
        
        <div class="form-group">
          <label>年龄:</label>
          <input 
            type="number" 
            name="age" 
            [(ngModel)]="user.age"
            required
            min="1"
            max="120"
            #age="ngModel">
          <div *ngIf="age.invalid && (age.dirty || age.touched)" class="error">
            <div *ngIf="age.errors?.['required']">年龄是必填的</div>
            <div *ngIf="age.errors?.['min']">年龄至少1岁</div>
            <div *ngIf="age.errors?.['max']">年龄最多120岁</div>
          </div>
        </div>
        
        <div class="form-group">
          <label>性别:</label>
          <select name="gender" [(ngModel)]="user.gender" required #gender="ngModel">
            <option value="">请选择</option>
            <option value="male">男</option>
            <option value="female">女</option>
          </select>
        </div>
        
        <div class="form-group">
          <label>订阅通知:</label>
          <input type="checkbox" name="subscribe" [(ngModel)]="user.subscribe">
        </div>
        
        <div class="form-group">
          <label>简介:</label>
          <textarea name="bio" [(ngModel)]="user.bio" rows="3"></textarea>
        </div>
        
        <button type="submit" [disabled]="userForm.invalid">提交</button>
        <button type="button" (click)="resetForm(userForm)">重置</button>
      </form>
      
      <div *ngIf="submitted" class="result">
        <h4>提交的数据:</h4>
        <pre>{{ submittedData | json }}</pre>
      </div>
    </div>
  `,
  styles: [`
    .form-container { padding: 20px; background: #f5f5f5; border-radius: 5px; }
    .form-group { margin-bottom: 15px; }
    .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
    .form-group input, .form-group select, .form-group textarea { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
    .error { color: red; font-size: 12px; margin-top: 5px; }
    button { padding: 10px 20px; margin-right: 10px; cursor: pointer; }
    button:disabled { background: #ccc; cursor: not-allowed; }
    .result { margin-top: 20px; padding: 15px; background: #e8f5e9; border-radius: 5px; }
  `]
})
export class TemplateDrivenFormComponent {
  user = {
    name: '',
    email: '',
    age: null,
    gender: '',
    subscribe: false,
    bio: ''
  };
  submitted = false;
  submittedData: any = null;

  onSubmit(form: NgForm) {
    if (form.valid) {
      this.submitted = true;
      this.submittedData = { ...this.user };
      console.log('表单提交:', this.user);
    }
  }

  resetForm(form: NgForm) {
    form.resetForm();
    this.user = {
      name: '',
      email: '',
      age: null,
      gender: '',
      subscribe: false,
      bio: ''
    };
    this.submitted = false;
    this.submittedData = null;
  }
}

// 3. 响应式表单组件
@Component({
  selector: 'app-reactive-form',
  template: `
    <div class="form-container">
      <h3>响应式表单</h3>
      <form [formGroup]="profileForm" (ngSubmit)="onSubmitReactive()">
        <div class="form-group">
          <label>姓名:</label>
          <input type="text" formControlName="name">
          <div *ngIf="name?.invalid && (name?.dirty || name?.touched)" class="error">
            <div *ngIf="name?.errors?.['required']">姓名是必填的</div>
            <div *ngIf="name?.errors?.['minlength']">姓名至少2个字符</div>
            <div *ngIf="name?.errors?.['forbiddenName']">姓名不能是admin</div>
          </div>
        </div>
        
        <div formGroupName="emailGroup">
          <div class="form-group">
            <label>邮箱:</label>
            <input type="email" formControlName="email">
            <div *ngIf="email?.invalid && (email?.dirty || email?.touched)" class="error">
              <div *ngIf="email?.errors?.['required']">邮箱是必填的</div>
              <div *ngIf="email?.errors?.['email']">请输入有效的邮箱地址</div>
            </div>
          </div>
          
          <div class="form-group">
            <label>确认邮箱:</label>
            <input type="email" formControlName="confirmEmail">
            <div *ngIf="confirmEmail?.invalid && (confirmEmail?.dirty || confirmEmail?.touched)" class="error">
              <div *ngIf="confirmEmail?.errors?.['required']">请确认邮箱</div>
            </div>
            <div *ngIf="emailGroup?.errors?.['emailMismatch'] && emailGroup?.touched" class="error">
              两次输入的邮箱不一致
            </div>
          </div>
        </div>
        
        <div class="form-group">
          <label>密码:</label>
          <input type="password" formControlName="password">
          <div *ngIf="password?.invalid && (password?.dirty || password?.touched)" class="error">
            <div *ngIf="password?.errors?.['required']">密码是必填的</div>
            <div *ngIf="password?.errors?.['minlength']">密码至少6个字符</div>
          </div>
        </div>
        
        <div class="form-group">
          <label>技能:</label>
          <div formArrayName="skills">
            <div *ngFor="let skill of skills.controls; let i = index" class="skill-item">
              <input [formControlName]="i" placeholder="技能 {{i + 1}}">
              <button type="button" (click)="removeSkill(i)" *ngIf="i > 0">删除</button>
            </div>
          </div>
          <button type="button" (click)="addSkill()">添加技能</button>
        </div>
        
        <button type="submit" [disabled]="profileForm.invalid">提交</button>
        <button type="button" (click)="resetReactiveForm()">重置</button>
        <button type="button" (click)="patchValue()">部分填充</button>
      </form>
      
      <div class="form-status">
        <h4>表单状态:</h4>
        <p>有效: {{ profileForm.valid }}</p>
        <p>脏: {{ profileForm.dirty }}</p>
        <p>已触碰: {{ profileForm.touched }}</p>
      </div>
      
      <div *ngIf="reactiveSubmitted" class="result">
        <h4>提交的数据:</h4>
        <pre>{{ reactiveSubmittedData | json }}</pre>
      </div>
    </div>
  `,
  styles: [`
    .form-container { padding: 20px; background: #fff3e0; border-radius: 5px; margin-top: 20px; }
    .form-group { margin-bottom: 15px; }
    .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
    .form-group input { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
    .error { color: red; font-size: 12px; margin-top: 5px; }
    button { padding: 10px 20px; margin-right: 10px; cursor: pointer; }
    button:disabled { background: #ccc; cursor: not-allowed; }
    .skill-item { display: flex; gap: 10px; margin-bottom: 10px; }
    .skill-item input { flex: 1; }
    .form-status { margin-top: 15px; padding: 10px; background: #e3f2fd; border-radius: 5px; }
    .result { margin-top: 20px; padding: 15px; background: #e8f5e9; border-radius: 5px; }
  `]
})
export class ReactiveFormComponent {
  profileForm: FormGroup;
  reactiveSubmitted = false;
  reactiveSubmittedData: any = null;

  constructor(private fb: FormBuilder) {
    this.profileForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2), forbiddenNameValidator(/admin/i)]],
      emailGroup: this.fb.group({
        email: ['', [Validators.required, Validators.email]],
        confirmEmail: ['', Validators.required]
      }, { validators: this.emailMatchValidator }),
      password: ['', [Validators.required, Validators.minLength(6)]],
      skills: this.fb.array([''])
    });
  }

  get name() { return this.profileForm.get('name'); }
  get emailGroup() { return this.profileForm.get('emailGroup'); }
  get email() { return this.profileForm.get('emailGroup.email'); }
  get confirmEmail() { return this.profileForm.get('emailGroup.confirmEmail'); }
  get password() { return this.profileForm.get('password'); }
  get skills() { return this.profileForm.get('skills') as any; }

  emailMatchValidator(group: FormGroup): ValidationErrors | null {
    const email = group.get('email')?.value;
    const confirmEmail = group.get('confirmEmail')?.value;
    return email === confirmEmail ? null : { emailMismatch: true };
  }

  addSkill() {
    this.skills.push(this.fb.control(''));
  }

  removeSkill(index: number) {
    this.skills.removeAt(index);
  }

  onSubmitReactive() {
    if (this.profileForm.valid) {
      this.reactiveSubmitted = true;
      this.reactiveSubmittedData = this.profileForm.value;
      console.log('响应式表单提交:', this.profileForm.value);
    }
  }

  resetReactiveForm() {
    this.profileForm.reset();
    this.skills.clear();
    this.skills.push(this.fb.control(''));
    this.reactiveSubmitted = false;
    this.reactiveSubmittedData = null;
  }

  patchValue() {
    this.profileForm.patchValue({
      name: '张三',
      emailGroup: {
        email: 'zhangsan@example.com',
        confirmEmail: 'zhangsan@example.com'
      },
      password: '123456'
    });
  }
}

// 4. 主组件
@Component({
  selector: 'app-forms-demo',
  template: `
    <h2>Angular 表示例</h2>
    <app-template-driven-form></app-template-driven-form>
    <app-reactive-form></app-reactive-form>
  `
})
export class FormsDemoComponent { }

// 5. 表单模块
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule
  ],
  declarations: [
    TemplateDrivenFormComponent,
    ReactiveFormComponent,
    FormsDemoComponent
  ]
})
export class FormsDemoModule { }
