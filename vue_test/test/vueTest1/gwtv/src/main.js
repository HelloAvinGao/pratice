import Vue from "vue";
import App from "./App.vue";
import Antd from "ant-design-vue"; //引用ant前端插件
import "ant-design-vue/dist/antd.css"; //引用ant样式
import VueI18n from "vue-i18n"; //引用多语言设置插件
import VueRouter from "vue-router"; //引用router
import axios from "axios";
import Vuex from "vuex";

Vue.prototype.axios = axios;

Vue.config.productionTip = false;

Vue.use(Antd); //注册ant
Vue.use(VueI18n); //注册vue-i18n
Vue.use(VueRouter); //注册vue-router
Vue.use(Vuex);

let Index = require("./components/Index.vue").default;
let Login = require("./components/Login.vue").default;
let Register = require("./components/Register.vue").default;
let Nav1 = require("./components/Nav1.vue").default;
let Nav2 = require("./components/Nav2.vue").default;
let Nav3 = require("./components/Nav3.vue").default;

//设置vue-i18n语言环境调用文件
const i18n = new VueI18n({
  locale: localStorage.getItem("language") || "zh", // 语言标识
  //this.$i18n.locale // 通过切换locale的值来实现语言切换
  messages: {
    zh: require("./langs/zh"),
    en: require("./langs/en"),
  },
});

const routes = [
  {
    path: "/index",
    component: Index,
    meta: {
      requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
    },
    children: [
      {
        path: "/nav1",
        component: Nav1,
        meta: {
          requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
        },
      },
      {
        path: "/nav2",
        component: Nav2,
        meta: {
          requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
        },
      },
      {
        path: "/nav3",
        component: Nav3,
        meta: {
          requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
        },
      },
    ],
  },
  {
    path: "/index",
    redirect: "/nav1",
  },
  {
    path: "/",
    component: Login,
  },
  {
    path: "/login",
    redirect: "/",
  },
  {
    path: "/register",
    component: Register,
  },
];

//设置vue-router
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
    token: localStorage.getItem("token") ? localStorage.getItem("token") : "",
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
      localStorage.removeItem("token");
    },
  },
});

new Vue({
  render: (h) => h(App),
  i18n, //调用vue-i18n
  router, //调用vue-router
  store, //调用vuex => store
}).$mount("#app");
