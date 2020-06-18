import Vue from "vue";
import App from "./App.vue";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
import VueI18n from "vue-i18n";
import VueRouter from "vue-router";
import axios from "axios";
import Vuex from "vuex";

Vue.prototype.axios = axios;

Vue.use(Antd);
Vue.use(VueI18n);
Vue.use(VueRouter);
Vue.use(Vuex);

let HelloWorld = require("./components/HelloWorld.vue").default;
let login = require("./components/login.vue").default;

const routes = [
  {
    path: "/HelloWorld",
    component: HelloWorld,
    meta: {
      requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
    },
  },
  {
    path: "/",
    component: login,
  },
  {
    path: "/Login",
    redirect: "/",
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

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

Vue.config.productionTip = false;

const i18n = new VueI18n({
  locale: localStorage.getItem("language") || "zh", // 语言标识
  //this.$i18n.locale // 通过切换locale的值来实现语言切换
  messages: {
    zh: require("./langs/zh"),
    en: require("./langs/en"),
  },
});

new Vue({
  render: (h) => h(App),
  i18n,
  router,
  store,
}).$mount("#app");
