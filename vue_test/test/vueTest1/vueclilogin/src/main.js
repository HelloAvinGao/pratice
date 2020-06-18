import Vue from "vue";
import App from "./App.vue";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
import VueI18n from "vue-i18n";
import VueRouter from "vue-router";
import axios from "axios";
import Vuex from "vuex";

Vue.prototype.axios = axios;
//挂载Vuex
Vue.use(Vuex);
Vue.use(VueRouter);
Vue.use(Antd);
Vue.use(VueI18n);

Vue.config.productionTip = false;

let hello = require("./components/Hello.vue").default;
let hello1 = require("./components/Hello1.vue").default;
let notFind = require("./components/notFind.vue").default;
let HelloWorld = require("./components/HelloWorld.vue").default;
let index = require("./components/Index.vue").default;
let register = require("./components/register.vue").default;
let login = require("./components/Login.vue").default;

const routes = [
  {
    path: "/",
    component: login,
  },
  {
    path: "/Login",
    redirect: "/",
  },
  {
    path: "/hello",
    name: "hello",
    component: hello,
    meta: {
      requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
    },
  },
  {
    path: "/hello1",
    component: hello1,
    meta: {
      requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
    },
    children: [
      {
        path: "HelloWorld",
        component: HelloWorld,
        meta: {
          requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
        },
      },
    ],
  },
  {
    path: "/h",
    component: notFind,
    meta: {
      requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
    },
  },
  {
    path: "/hello/index",
    component: index,
    meta: {
      requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
    },
  },
  {
    path: "/register",
    component: register,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

router.beforeEach((to, from, next) => {
  let token = localStorage.getItem("Authorization");
  if (to.meta.requireAuth) {  // 判断该路由是否需要登录权限
    if (token === "null" || token === "") {
      next({
        path: '/login',
        query: {redirect: to.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
      })
    } else {
      next();
    }
  }
  else {
      next();
  }
});
// router.beforeEach((to, from, next) => {
//   // let islogin = localStorage.getItem("islogin");
//   // islogin = Boolean(Number(islogin));

//   if (to.meta.requireAuth) {  // 判断该路由是否需要登录权限
//       if (store.state.token) {  // 通过vuex state获取当前的token是否存在
//           next();
//       }
//       else {
//           next({
//               path: '/login',
//               query: {redirect: to.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
//           })
//       }
//   }
//   else {
//       next();
//   }
// })

axios.interceptors.request.use(
  (config) => {
    if (localStorage.getItem("Authorization")) {
      config.headers.Authorization = localStorage.getItem("Authorization");
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);


//创建VueX对象
const store = new Vuex.Store({
  state: {
    // 存储token
    Authorization: localStorage.getItem("Authorization")
      ? localStorage.getItem("Authorization")
      : "",
  },

  mutations: {
    // 修改token，并将token存入localStorage
    changeLogin(state, user) {
      state.Authorization = user.Authorization;
      localStorage.setItem("Authorization", user.Authorization);
    },
  },
});

const i18n = new VueI18n({
  locale: localStorage.getItem("language") || "zh", // 语言标识
  //this.$i18n.locale // 通过切换locale的值来实现语言切换
  messages: {
    zh: require("./theme/zh"),
    en: require("./theme/en"),
  },
});

new Vue({
  render: (h) => h(App),
  i18n, // 不要忘记
  router,
  store,
}).$mount("#app");
