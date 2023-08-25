import { createApp } from 'vue'
import App from './App.vue'
import "./assets/reset.css";
import "./assets/icon/iconfont.css"
import router from './router'
import store from './store'


createApp(App).use(store).use(router).mount('#app')
