<template>
  <a-layout id="components-layout-all">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
        <div class="logo" />
        <a-menu
          theme="dark"
          mode="inline"
          class="menuStyle"
          :default-selected-keys="['1']"
        >
          <a-menu-item key="1">
            <a-icon type="user" />
            <span
              ><router-link
                v-bind:to="{
                  name: 'nav1',
                  params: { username: this.$route.params.username },
                }"
                >nav 1</router-link
              ></span
            >
          </a-menu-item>
          <a-menu-item key="2">
            <a-icon type="video-camera" />
            <span
              ><router-link
                v-bind:to="{
                  name: 'nav2',
                  params: { username: this.$route.params.username },
                }"
                >nav 2</router-link
              ></span
            >
          </a-menu-item>
          <a-menu-item key="3">
            <a-icon type="upload" />
            <span
              ><router-link
                v-bind:to="{
                  name: 'nav3',
                  params: { username: this.$route.params.username },
                }"
                >nav 3</router-link
              ></span
            >
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout style="background: #fff;">
        <a-layout-header style="background: #fff; padding: 0">
          <a-layout>
            <a-row>
              <a-col :span="12" style="text-align:left;">
                <a-icon
                  class="trigger"
                  :type="collapsed ? 'menu-unfold' : 'menu-fold'"
                  @click="() => (collapsed = !collapsed)"
                />
              </a-col>
              <a-col :span="12" style="text-align:right;" v-model="userName">
                {{ userName || $route.params.username }}
                <a-tooltip placement="bottom">
                  <template slot="title">
                    <a-button @click="logoutFun">prompt text</a-button>
                  </template>
                  <img
                  src="../assets/logo.png"
                  width="30px"
                  height=" 30px"
                  style="margin-right:30px;"
                />
                </a-tooltip>
              </a-col>
            </a-row>
          </a-layout>
        </a-layout-header>
        <a-layout-content
          :style="{
            margin: '24px 16px',
            padding: '24px',
          }"
        >
          <router-view></router-view>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script>
export default {
  data() {
    return {
      collapsed: false,
      userName: null,
    };
  },
  methods: {
    logoutFun: function(){
      this.$router.push({path: "/login"}); 
      this.$cookie.delete("username");
      this.$cookie.delete("password");
      this.$store.commit("del_token");
    }
  },
  mounted() {
    let username = this.$cookie.get("username");
    if(username){
      this.userName = username;
      console.log(this.$cookie.get("password"));
    }else{
      // 在挂载时接收到参数并且赋值
      this.userName = this.$route.params.username;
      console.log('params');
    }
  },
};
</script>
<style scoped>
a {
  color: #ffffff;
}
#components-layout-all {
  width: 100vw;
  height: 100vh;
}
#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1806fe;
}

#components-layout-demo-custom-trigger .logo {
  height: 32px;
  background: rgba(255, 255, 255, 1);
  margin: 16px;
}
</style>
