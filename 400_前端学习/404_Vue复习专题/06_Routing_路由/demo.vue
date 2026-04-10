<template>
  <div class="routing">
    <h1>Vue 路由示例</h1>
    
    <!-- 1. 路由配置 -->
    <div class="section">
      <h2>1. 路由配置</h2>
      <pre><code>// router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/user/:id',
    name: 'User',
    component: () => import('../views/User.vue')
  },
  {
    path: '*',
    name: '404',
    component: () => import('../views/404.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router</code></pre>
    </div>
    
    <!-- 2. 路由导航 -->
    <div class="section">
      <h2>2. 路由导航</h2>
      <div class="navigation">
        <router-link to="/">首页</router-link>
        <router-link to="/about">关于</router-link>
        <router-link to="/user/1">用户 1</router-link>
        <router-link to="/user/2">用户 2</router-link>
        <router-link to="/not-found">404 页面</router-link>
      </div>
    </div>
    
    <!-- 3. 路由视图 -->
    <div class="section">
      <h2>3. 路由视图</h2>
      <router-view></router-view>
    </div>
    
    <!-- 4. 编程式导航 -->
    <div class="section">
      <h2>4. 编程式导航</h2>
      <button @click="navigateToHome">跳转到首页</button>
      <button @click="navigateToAbout">跳转到关于</button>
      <button @click="navigateToUser">跳转到用户</button>
      <button @click="goBack">返回</button>
    </div>
    
    <!-- 5. 路由参数 -->
    <div class="section">
      <h2>5. 路由参数</h2>
      <p>当前路由: {{ $route.path }}</p>
      <p>当前路由参数: {{ $route.params }}</p>
      <p>当前路由查询: {{ $route.query }}</p>
    </div>
    
    <!-- 6. 路由守卫 -->
    <div class="section">
      <h2>6. 路由守卫</h2>
      <pre><code>// 全局前置守卫
router.beforeEach((to, from, next) => {
  console.log('Global before guard');
  next();
});

// 全局后置守卫
router.afterEach((to, from) => {
  console.log('Global after guard');
});

// 路由独享守卫
const router = new VueRouter({
  routes: [
    {
      path: '/user/:id',
      component: User,
      beforeEnter: (to, from, next) => {
        console.log('Route before enter');
        next();
      }
    }
  ]
});

// 组件内守卫
export default {
  beforeRouteEnter(to, from, next) {
    console.log('Component before route enter');
    next();
  },
  beforeRouteUpdate(to, from, next) {
    console.log('Component before route update');
    next();
  },
  beforeRouteLeave(to, from, next) {
    console.log('Component before route leave');
    next();
  }
}</code></pre>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RoutingDemo',
  methods: {
    navigateToHome() {
      this.$router.push('/');
    },
    navigateToAbout() {
      this.$router.push('/about');
    },
    navigateToUser() {
      this.$router.push('/user/3');
    },
    goBack() {
      this.$router.back();
    }
  }
};
</script>

<style scoped>
.routing {
  padding: 20px;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.navigation {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.router-link {
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  text-decoration: none;
  color: #333;
}

.router-link:hover {
  background-color: #e9e9e9;
}

.router-link-active {
  background-color: #007bff;
  color: white;
  border-color: #007bff;
}

button {
  margin-right: 10px;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
  cursor: pointer;
}

button:hover {
  background-color: #e9e9e9;
}

pre {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 4px;
  overflow-x: auto;
}

code {
  font-family: 'Courier New', Courier, monospace;
}
</style>
