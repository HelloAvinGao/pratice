# gwtv

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

### router params

# js

this.\$router.push({name:"nav1",params:{"username":values.userName}}); // params 和 query

# vue

<router-link v-bind:to="{name:'nav3',params:{username:this.$route.params.username}}">nav 3</router-link>

{{ $route.params.username }}

### cookie

npm install --save vue-cookie

### main.js

// 配置 cookie
import cookie from 'vue-cookie'
Vue.prototype.$cookie = cookie;  //配置时候prototype.$这里的名字自己定义不是固定是 cookie

### 使用

created() {//创建时间节点
console.log('组件创建成功');
let token = 'asd1d5.0o9utrf7.12jjkht';
// 设置 cookie 默认过期时间单位是 1d(1 天)
this.$cookie.set('token', token, 1);
},
mounted() {//创建渲染节点
    console.log('组件渲染成功');
    let token = this.$cookie.get('token');
console.log(token);
},
destroyed() {//组件销毁节点
console.log('组件销毁成功');
this.\$cookie.delete('token')
}

### log out

```
    logoutFun: function(){
      this.$router.push({path: "/login"});
      this.$cookie.delete("username");
      this.$cookie.delete("password");
      this.$store.commit("del_token");
    }
```
