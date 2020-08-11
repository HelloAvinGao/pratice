import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import echarts from 'echarts' //引入echarts


Vue.use(Antd)
Vue.config.productionTip = false

Vue.prototype.axios = axios
Vue.prototype.$echarts = echarts //挂载在原型，组件内使用直接this.$echarts调用

new Vue({
  render: h => h(App),
}).$mount('#app')
