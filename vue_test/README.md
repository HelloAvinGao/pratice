# vueclilogin

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

### ant

npm install --save ant-design-vue

### use ant

## in main.js

```
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
Vue.use(Antd)
```

### switch chinese and english

### source : http://www.luyixian.cn/javascript_show_165783.aspx

npm install vue-i18n --save-dev

### in main.js

```
import Vue from 'vue'
import App from './App.vue'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import VueI18n from 'vue-i18n'


Vue.use(Antd)
Vue.use(VueI18n) // 通过插件的形式挂载

Vue.config.productionTip = false

const i18n = new VueI18n({
  locale: localStorage.getItem('language')||'zh',    // 语言标识
  //this.$i18n.locale // 通过切换locale的值来实现语言切换
  messages: {
    'zh': require('./theme/zh'),
    'en': require('./theme/en')
  }
})

new Vue({
  render: h => h(App),
  i18n,  // 不要忘记
}).$mount('#app')

```

### in ./theme/zh.js

```
module.exports = {
  language: {
    name: "English",
  },
  navbar: {
    home: "首页",
  },
};
```

### in App.vue

```
<template>
  <div id="app" @click="changeLang()">
    <p>{{ $t("language.name") }}</p>
    <p>{{ $t("navbar.home") }}</p>
  </div>
</template>

<script>


export default {
  name: "App",
  components: {

  },
  methods: {
    changeLang: function() {
      let locale = localStorage.getItem("language") || "zh";
      let temp = locale === "zh" ? "en" : "zh";
      this.$i18n.locale = temp; //改变当前语言
      localStorage.language = temp;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

### vue-router
npm install --save vue-router

### in main.js

```
import Vue from 'vue'
import App from './App.vue'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

Vue.config.productionTip = false

let hello = require('./components/Hello.vue').default
let hello1 = require('./components/Hello1.vue').default
let notFind = require('./components/notFind.vue').default

const routes = [{
  path: '/login',
  component: login,
},{
  path: '/',
  redirect: login,
},{
  path:'/h',
  component:notFind,
}
];

const router = new VueRouter
({
    mode: 'history',
    routes
})


new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
```

### in vue file

```
      <div>
        <router-link to="/hello1">点击进入hello1</router-link>
        <br />
        <router-link to="/hello2">点击进入hello2</router-link>
        <br />
        <router-link to="/h">点击进入不存在的路径</router-link>
        <br />
        <router-view></router-view>
      </div>
```

### axios

npm install --save axios

### in main.js

```
import axios from 'axios'
Vue.prototype.axios = axios
```

### in login.vue

```
          this.axios({
            url: "http://127.0.0.1:5000/login",
            method: "POST",
            crossdomain: true,
            params: {
              userName:"gao",
              password:"qiang",
            },
          }).then((res) => {
            console.log(res.data);
          });
```
### vuex 
npm install --save vuex

### in main.js
```
import Vuex from 'vuex'

Vue.use(Vuex)

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    // 判断该路由是否需要登录权限
    if (store.state.token) {
      // 通过vuex state获取当前的token是否存在
      next();
    } else {
      next({
        path: "/login",
        query: { redirect: to.fullPath }, // 将跳转的路由path作为参数，登录成功后跳转到该路由
      });
    }
  } else {
    next();
  }
});
// http request 拦截器
axios.interceptors.request.use(
  (config) => {
    if (store.state.token) {
      // 判断是否存在token，如果存在的话，则每个http header都加上token
      config.headers.Authorization = `token ${store.state.token}`;
    }
    return config;
  },
  (err) => {
    return Promise.reject(err);
  }
);

// http response 拦截器
axios.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // 返回 401 清除token信息并跳转到登录页面
          // store.commit(types.LOGOUT);
          router.replace({
            path: "login",
            query: { redirect: router.currentRoute.fullPath },
          });
      }
    }
    return Promise.reject(error.response.data); // 返回接口返回的错误信息
  }
);

//创建VueX对象
const store = new Vuex.Store({
  state: {
    // 存储token
    token: localStorage.getItem("token")
      ? localStorage.getItem("token")
      : "",
  },
  mutations: {
    set_token(state, token) {
      state.token = token;
      sessionStorage.token = token;
      localStorage.token = token;
    },
    del_token(state) {
      state.token = "";
      sessionStorage.removeItem("token");
      localStorage.removeItem('token');
    },
  },
});



```
### in login.vue
```
import { mapMutations } from 'vuex';
...

   methods: {
    changeLang: function() {
      let locale = localStorage.getItem("language") || "zh";
      let temp = locale === "zh" ? "en" : "zh";
      this.$i18n.locale = temp; //改变当前语言
      localStorage.language = temp;
      location.reload();
    },
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
          this.axios({
            url: "http://127.0.0.1:5000/login",
            method: "POST",
            crossdomain: true,
            params: values,
          }).then((res) => {
            this.token = res.data.token;
            if (this.token) {
              this.$store.commit("set_token", this.token); //调用store中的获取token方法，并将token存在store中
              this.$router.push("/HelloWorld");
            } else {
              this.$router.replace("/login");
            }
          });
        }
      });
    },
  },
```

