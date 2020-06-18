<template>
  <div id="content">
    <router-view></router-view>
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
}
</style>
