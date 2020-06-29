<template>
  <div>
    <div class="vux-demo">
      <ButtonTab>
        <ButtonTabItem @on-item-click="test" selected>test1</ButtonTabItem>
        <ButtonTabItem>test2</ButtonTabItem>
        <ButtonTabItem>test3</ButtonTabItem>
      </ButtonTab>
      <XHeader title='Xheader'>test</XHeader>
      <tab>
        <tab-item @on-item-click="handler">handler1</tab-item>
        <tab-item @on-item-click="handler">handler2</tab-item>
      </tab>
    </div>
  </div>
</template>

<script>
import {
  ButtonTab,
  ButtonTabItem,
  Tab,
  TabItem,
  XHeader
} from 'vux'

export default {
  components: {
    ButtonTab,
    ButtonTabItem,
    Tab,
    TabItem,
    XHeader
  },
  data () {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      msg: 'Hello World!'
    }
  },
  methods: {
    test () {
      console.log('hello world')
    },
    handler () {
      console.log('handler')
    }
  },
  watch: {
    $route (to, from) {
      if (
        to.path === '/' ||
        to.path === '/Home' ||
        to.path === '/Index'
      ) {
        /**
         * $store来自Store对象
         * dispatch 向 actions 发起请求
         */
        this.$store.dispatch('showTabBar')
      } else {
        this.$store.dispatch('hideTabBar')
      }
    }
  }
}
</script>

<style>
.vux-demo {
  text-align: center;
}
.logo {
  width: 100px;
  height: 100px;
}
.tabbarStyle {
  position: fixed;
}
</style>
