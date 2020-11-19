import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue' //added by me
//src/main.js
import 'bootstrap/dist/css/bootstrap.css' //added by me
import 'bootstrap-vue/dist/bootstrap-vue.css' //added by me

Vue.use(BootstrapVue) //added by me
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
