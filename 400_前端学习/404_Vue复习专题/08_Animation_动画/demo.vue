<template>
  <div class="animation">
    <h1>Vue 动画示例</h1>
    
    <!-- 1. 过渡动画 -->
    <div class="section">
      <h2>1. 过渡动画</h2>
      <button @click="show = !show">切换显示</button>
      <transition name="fade">
        <div v-if="show" class="box">
          这是一个过渡动画示例
        </div>
      </transition>
    </div>
    
    <!-- 2. 过渡组动画 -->
    <div class="section">
      <h2>2. 过渡组动画</h2>
      <button @click="addItem">添加项</button>
      <button @click="removeItem">移除项</button>
      <transition-group name="list" tag="ul">
        <li v-for="item in items" :key="item.id" class="list-item">
          {{ item.text }}
        </li>
      </transition-group>
    </div>
    
    <!-- 3. 自定义过渡类名 -->
    <div class="section">
      <h2>3. 自定义过渡类名</h2>
      <button @click="showCustom = !showCustom">切换显示</button>
      <transition
        enter-active-class="custom-enter-active"
        leave-active-class="custom-leave-active"
        enter-class="custom-enter"
        leave-class="custom-leave"
      >
        <div v-if="showCustom" class="box custom-box">
          这是一个自定义过渡动画示例
        </div>
      </transition>
    </div>
    
    <!-- 4. 动态过渡 -->
    <div class="section">
      <h2>4. 动态过渡</h2>
      <button @click="showDynamic = !showDynamic">切换显示</button>
      <select v-model="transitionName">
        <option value="fade">淡入淡出</option>
        <option value="slide">滑动</option>
        <option value="scale">缩放</option>
      </select>
      <transition :name="transitionName">
        <div v-if="showDynamic" class="box">
          这是一个动态过渡动画示例
        </div>
      </transition>
    </div>
    
    <!-- 5. 交错过渡 -->
    <div class="section">
      <h2>5. 交错过渡</h2>
      <button @click="showStaggered = !showStaggered">切换显示</button>
      <transition-group
        name="staggered-fade"
        tag="div"
        class="staggered-list"
        v-on:enter="enter"
        v-on:leave="leave"
      >
        <div
          v-for="(item, index) in staggeredItems"
          :key="item"
          class="staggered-item"
          :data-index="index"
        >
          {{ item }}
        </div>
      </transition-group>
    </div>
    
    <!-- 6. CSS 动画 -->
    <div class="section">
      <h2>6. CSS 动画</h2>
      <button @click="showAnimation = !showAnimation">切换显示</button>
      <transition name="bounce">
        <div v-if="showAnimation" class="box">
          这是一个 CSS 动画示例
        </div>
      </transition>
    </div>
    
    <!-- 7. 列表动画 -->
    <div class="section">
      <h2>7. 列表动画</h2>
      <button @click="shuffleItems">打乱列表</button>
      <transition-group name="flip-list" tag="ul">
        <li v-for="item in shuffleItemsList" :key="item.id" class="flip-item">
          {{ item.text }}
        </li>
      </transition-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnimationDemo',
  data() {
    return {
      show: false,
      showCustom: false,
      showDynamic: false,
      showStaggered: false,
      showAnimation: false,
      transitionName: 'fade',
      items: [
        { id: 1, text: 'Item 1' },
        { id: 2, text: 'Item 2' },
        { id: 3, text: 'Item 3' }
      ],
      nextId: 4,
      staggeredItems: ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'],
      shuffleItemsList: [
        { id: 1, text: 'Item 1' },
        { id: 2, text: 'Item 2' },
        { id: 3, text: 'Item 3' },
        { id: 4, text: 'Item 4' },
        { id: 5, text: 'Item 5' }
      ]
    };
  },
  methods: {
    addItem() {
      this.items.push({ id: this.nextId++, text: `Item ${this.nextId - 1}` });
    },
    removeItem() {
      this.items.pop();
    },
    shuffleItems() {
      this.shuffleItemsList = this.shuffleArray([...this.shuffleItemsList]);
    },
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    },
    enter(el, done) {
      const delay = el.dataset.index * 150;
      setTimeout(() => {
        done();
      }, delay);
    },
    leave(el, done) {
      const delay = el.dataset.index * 150;
      setTimeout(() => {
        done();
      }, delay);
    }
  }
};
</script>

<style scoped>
.animation {
  padding: 20px;
}

.section {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
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

.box {
  width: 300px;
  height: 100px;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
  border-radius: 4px;
}

/* 1. 淡入淡出动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

/* 2. 列表动画 */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s;
}

.list-enter,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.list-item {
  list-style: none;
  padding: 10px;
  margin: 5px 0;
  background-color: #f0f0f0;
  border-radius: 4px;
}

/* 3. 自定义过渡 */
.custom-enter-active,
.custom-leave-active {
  transition: all 0.5s;
}

.custom-enter,
.custom-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.custom-box {
  background-color: #e3f2fd;
  border: 1px solid #2196f3;
}

/* 4. 滑动动画 */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter,
.slide-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* 5. 缩放动画 */
.scale-enter-active,
.scale-leave-active {
  transition: all 0.5s;
}

.scale-enter,
.scale-leave-to {
  opacity: 0;
  transform: scale(0.8);
}

/* 6. 交错过渡 */
.staggered-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}

.staggered-item {
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 4px;
}

.staggered-fade-enter-active,
.staggered-fade-leave-active {
  transition: all 0.5s;
}

.staggered-fade-enter,
.staggered-fade-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* 7. CSS 动画 */
.bounce-enter-active {
  animation: bounce-in 0.5s;
}

.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}

@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

/* 8. 列表翻转动画 */
.flip-list {
  list-style: none;
  padding: 0;
  margin-top: 10px;
}

.flip-item {
  padding: 10px;
  margin: 5px 0;
  background-color: #f0f0f0;
  border-radius: 4px;
  transition: all 0.5s;
}

.flip-list-move {
  transition: transform 0.5s;
}

.flip-list-enter-active,
.flip-list-leave-active {
  transition: all 0.5s;
}

.flip-list-enter,
.flip-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.flip-list-leave-active {
  position: absolute;
}
</style>
