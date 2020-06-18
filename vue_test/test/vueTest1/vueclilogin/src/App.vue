<template>
  <div id="content">
    <div>
      <div>

        <router-link to="/register">点击进入register</router-link>
        <br />
        <router-link to="/hello1">点击进入hello1</router-link>
        <br />
        <router-link to="/hello1/HelloWorld">点击进入HelloWorld</router-link>
        <br />
        <router-link to="/hello">点击进入hello</router-link>
        <br />
        <router-link to="/h">点击进入不存在的路径</router-link>
        <br />
        <router-link to="/hello/index">点击进入/index/index</router-link>
        <br />
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "App",
  components: {
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style>
#content {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: url("./assets/background.svg");
}
</style>
