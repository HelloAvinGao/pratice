<template>
  <div>
    <!-- rourer-view 作为默认插槽内容 -->
    <div>
      <router-view></router-view>
    </div>
    <Tabbar>
        <TabbarItem link='/Home'
          ><span slot="label">TabbarItem1</span></TabbarItem
        >
        <TabbarItem link='/Index'
          ><span slot="label">TabbarItem2</span></TabbarItem
        >
    </Tabbar>
  </div>
</template>

<script>
import {
  Tabbar,
  TabbarItem
} from 'vux'
export default {
  name: 'app',
  components: {
    Tabbar,
    TabbarItem
  },
  methods: {

  }
}
</script>

<style lang="less">
@import "~vux/src/styles/reset.less";

body {
  background-color: #fbf9fe;
}
</style>
