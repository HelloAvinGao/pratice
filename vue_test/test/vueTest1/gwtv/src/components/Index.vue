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
            <span><router-link to="/nav1">nav 1</router-link></span>
          </a-menu-item>
          <a-menu-item key="2">
            <a-icon type="video-camera" />
            <span><router-link to="/nav2">nav 2</router-link></span>
          </a-menu-item>
          <a-menu-item key="3">
            <a-icon type="upload" />
            <span><router-link to="/nav3">nav 3</router-link></span>
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
                {{ userName }}
                <img src="../assets/logo.png" width="30px" height=" 30px" style="margin-right:30px;"/>
                
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
      userName: 'gao'
    };
  },
  methods: {

  }, 
  mounted(){
			// 在挂载时接收到参数并且赋值
			this.userName = this.$route.query.username;
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
