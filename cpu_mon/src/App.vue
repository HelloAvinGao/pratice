<template>
  <div id="app">
    <heads />
    <echarts />
    <tables />
  </div>
</template>

<script>
import echarts from './components/echarts'
import heads from './components/head'
import tables from './components/table'
export default {
  name: 'App',
  components: {
    heads,
    echarts,
    tables
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin:auto;
  font-size: 1rem;
}
</style>
