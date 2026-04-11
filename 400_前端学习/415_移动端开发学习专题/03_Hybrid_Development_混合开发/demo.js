// 混合开发示例代码

// 1. Cordova项目创建
const cordovaSetup = `
// Cordova项目创建

# 安装Cordova CLI
npm install -g cordova

# 创建项目
cordova create MyApp com.example.myapp MyApp
cd MyApp

# 添加平台
cordova platform add ios
cordova platform add android

# 添加插件
cordova plugin add cordova-plugin-camera
cordova plugin add cordova-plugin-geolocation
cordova plugin add cordova-plugin-network-information

# 运行
cordova run ios
cordova run android

# 构建
cordova build ios --release
cordova build android --release
`;

console.log('=== Cordova项目创建 ===');
console.log(cordovaSetup);

// 2. Capacitor项目创建
const capacitorSetup = `
// Capacitor项目创建

# 安装Capacitor CLI
npm install -g @capacitor/cli

# 创建项目
npm init @capacitor/app MyApp
cd MyApp

# 初始化Capacitor
npm install @capacitor/core @capacitor/cli
npx cap init

# 添加平台
npm install @capacitor/android @capacitor/ios
npx cap add android
npx cap add ios

# 构建Web应用
npm run build

# 同步到原生平台
npx cap sync

# 打开原生IDE
npx cap open ios
npx cap open android

# 运行
npx cap run android
npx cap run ios
`;

console.log('\n=== Capacitor项目创建 ===');
console.log(capacitorSetup);

// 3. Capacitor API使用
const capacitorAPI = `
// Capacitor API使用

import { Camera, CameraResultType } from '@capacitor/camera';
import { Geolocation } from '@capacitor/geolocation';
import { Network } from '@capacitor/network';
import { Storage } from '@capacitor/storage';
import { Device } from '@capacitor/device';

// 相机
async function takePhoto() {
  const image = await Camera.getPhoto({
    quality: 90,
    allowEditing: true,
    resultType: CameraResultType.Uri
  });
  
  console.log('照片路径:', image.webPath);
  return image.webPath;
}

// 地理位置
async function getCurrentLocation() {
  const position = await Geolocation.getCurrentPosition();
  
  console.log('纬度:', position.coords.latitude);
  console.log('经度:', position.coords.longitude);
  
  return position;
}

// 网络状态
async function getNetworkStatus() {
  const status = await Network.getStatus();
  
  console.log('已连接:', status.connected);
  console.log('连接类型:', status.connectionType);
  
  return status;
}

// 监听网络变化
function listenNetworkChanges() {
  Network.addListener('networkStatusChange', (status) => {
    console.log('网络变化:', status);
  });
}

// 本地存储
async function storageDemo() {
  await Storage.set({
    key: 'user',
    value: JSON.stringify({ name: '张三', age: 18 })
  });
  
  const { value } = await Storage.get({ key: 'user' });
  const user = JSON.parse(value);
  console.log('用户:', user);
  
  await Storage.remove({ key: 'user' });
  await Storage.clear();
}

// 设备信息
async function getDeviceInfo() {
  const info = await Device.getInfo();
  
  console.log('平台:', info.platform);
  console.log('系统版本:', info.osVersion);
  console.log('设备型号:', info.model);
  
  return info;
}

// 振动
async function vibrate() {
  await Device.vibrate();
}

// 手电筒
async function toggleTorch(on: boolean) {
  await Device.setTorch({ on });
}
`;

console.log('\n=== Capacitor API使用 ===');
console.log(capacitorAPI);

// 4. Ionic项目创建
const ionicSetup = `
// Ionic项目创建

# 安装Ionic CLI
npm install -g @ionic/cli

# 创建项目
ionic start MyApp tabs --type=react
# 或
ionic start MyApp blank --type=angular
# 或
ionic start MyApp sidemenu --type=vue

cd MyApp

# 添加Capacitor
ionic integrations enable capacitor

# 构建
ionic build

# 添加平台
npx cap add ios
npx cap add android

# 同步
npx cap sync

# 运行
ionic serve          # 浏览器
ionic cap run ios    # iOS
ionic cap run android # Android

# 生成页面
ionic generate page User
ionic generate component MyButton
ionic generate service Api
`;

console.log('\n=== Ionic项目创建 ===');
console.log(ionicSetup);

// 5. Ionic组件使用
const ionicComponents = `
// Ionic组件使用

// Ionic + React
import { 
  IonContent, 
  IonHeader, 
  IonTitle, 
  IonToolbar,
  IonButton,
  IonInput,
  IonList,
  IonItem,
  IonLabel,
  IonCard,
  IonCardHeader,
  IonCardTitle,
  IonCardContent,
  IonToast
} from '@ionic/react';

function HomePage() {
  const [name, setName] = useState('');
  const [showToast, setShowToast] = useState(false);

  return (
    <>
      <IonHeader>
        <IonToolbar>
          <IonTitle>首页</IonTitle>
        </IonToolbar>
      </IonHeader>
      
      <IonContent className="ion-padding">
        <IonCard>
          <IonCardHeader>
            <IonCardTitle>欢迎使用Ionic</IonCardTitle>
          </IonCardHeader>
          <IonCardContent>
            <IonInput
              value={name}
              placeholder="请输入姓名"
              onIonChange={(e) => setName(e.detail.value!)}
            />
            
            <IonButton 
              expand="block" 
              onClick={() => setShowToast(true)}
            >
              点击我
            </IonButton>
          </IonCardContent>
        </IonCard>
        
        <IonList>
          <IonItem>
            <IonLabel>列表项 1</IonLabel>
          </IonItem>
          <IonItem>
            <IonLabel>列表项 2</IonLabel>
          </IonItem>
          <IonItem>
            <IonLabel>列表项 3</IonLabel>
          </IonItem>
        </IonList>
        
        <IonToast
          isOpen={showToast}
          message={\`你好, \${name}!\`}
          duration={2000}
          onDidDismiss={() => setShowToast(false)}
        />
      </IonContent>
    </>
  );
}

// Ionic + Angular
import { Component } from '@angular/core';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-home',
  template: \`
    <ion-header>
      <ion-toolbar>
        <ion-title>首页</ion-title>
      </ion-toolbar>
    </ion-header>
    
    <ion-content class="ion-padding">
      <ion-card>
        <ion-card-header>
          <ion-card-title>欢迎使用Ionic</ion-card-title>
        </ion-card-header>
        <ion-card-content>
          <ion-input 
            [(ngModel)]="name" 
            placeholder="请输入姓名"
          ></ion-input>
          
          <ion-button 
            expand="block" 
            (click)="showToast()"
          >
            点击我
          </ion-button>
        </ion-card-content>
      </ion-card>
    </ion-content>
  \`
})
export class HomePage {
  name = '';

  constructor(private toastCtrl: ToastController) {}

  async showToast() {
    const toast = await this.toastCtrl.create({
      message: \`你好, \${this.name}!\`,
      duration: 2000
    });
    toast.present();
  }
}
`;

console.log('\n=== Ionic组件使用 ===');
console.log(ionicComponents);

// 6. 混合开发优缺点
const hybridProsCons = `
// 混合开发优缺点

const hybridPros = [
    '开发速度快 - 一套代码多端运行',
    '成本低 - 使用Web技术栈',
    '维护简单 - 只需维护一套代码',
    '可以热更新 - 无需重新提交审核',
    '现有Web团队可直接上手',
    '迭代速度快',
    '包体积相对较小'
];

const hybridCons = [
    '性能一般 - WebView渲染',
    '体验不如原生',
    '部分原生API受限',
    '深度硬件集成困难',
    '复杂动画效果较差',
    '大型应用性能问题明显',
    '应用商店审核可能有问题'
];

// 适用场景
const hybridUseCases = [
    '内容展示类应用',
    '企业内部应用',
    '快速原型验证',
    '中小型应用',
    '更新频繁的应用',
    '对性能要求不高的应用',
    '预算有限的项目'
];

console.log('=== 混合开发优缺点 ===');
console.log('优点:', hybridPros);
console.log('缺点:', hybridCons);
console.log('适用场景:', hybridUseCases);
`;

console.log('\n=== 混合开发优缺点 ===');
console.log(hybridProsCons);

console.log('\n🎉 混合开发学习完成！');
console.log('💡 混合开发适合快速开发、预算有限的项目！');
`;

console.log('\n=== 混合开发 ===');
