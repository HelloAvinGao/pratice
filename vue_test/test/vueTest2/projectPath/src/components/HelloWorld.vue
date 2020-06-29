<template>
  <div class="hello">
    <flow>
      <template v-for="(i, index) in steps">
        <flow-state
          :state="index + 1"
          :title="i.title"
          :is-done="i.isDone"
        ></flow-state>
        <flow-line
          v-if="index != steps.length - 1"
          :is-done="i.lineDone"
          :tip="i.tip ? i.tip : null"
        ></flow-line>
      </template>
    </flow>
    <Panel header="这样写不行吗？"></Panel>
    <marquee class="my-marquee">
      <marquee-item>Lorem dolor doloribus earum error ipsa.</marquee-item>
      <marquee-item>totam vel Dignissimos labore quam voluptatum.</marquee-item>
      <marquee-item>consectetur adipisicing elit. Aperiam culpa.</marquee-item>
      <marquee-item>laudantium nesciunt obcaecati omnis similiqu.</marquee-item>
    </marquee>
    <div>
      <img class="previewer-demo-img" v-for="(item, index) in list" :src="item.src" width="100" @click="show(index)">
      <div>
        <previewer :list="list" ref="previewer" :options="options"></previewer>
      </div>
      <qrcode value="http://dev.cnv8.tv:8900/?nav_source=navbar" type="img"></qrcode>
    </div>
    <div>
      <step v-model="step2" background-color='#fbf9fe' gutter="20px">
        <step-item title="done"></step-item>
        <step-item title="processing"></step-item>
        <step-item title="end"></step-item>
      </step>
      <div class="btn_wrap">
        <x-button type="primary" @click.native="nextStep">next step</x-button>
      </div>
    </div>
    <swiper auto height="30px" direction="vertical" :interval=2000 class="text-scroll" :show-dots="false">
      <SwiperItem><p>义务爱了 完成传奇世界H5-王者归来任务 获得20金币</p></SwiperItem>
      <SwiperItem><p>基本世神 兑换《传奇世界H5》畅玩级礼包 消耗30金币</p></SwiperItem>
      <SwiperItem><p>零哥章魚 完成传奇世界H5-王者归来任务 获得30金币</p></SwiperItem>
      <SwiperItem><p>做迎而為 兑换【饿了么】畅享美食红包 消耗20金币</p></SwiperItem>
      <SwiperItem><p>只知道不知道 兑换【饿了么】畅享美食红包 消耗20金币</p></SwiperItem>
      <SwiperItem><p>基本世神 兑换《传奇世界H5》畅玩级礼包 消耗30金币</p></SwiperItem>
    </swiper>
  </div>
</template>
<script>
import {
  Flow,
  FlowState,
  FlowLine,
  Marquee,
  MarqueeItem,
  Panel,
  Previewer,
  Qrcode,
  Step,
  StepItem,
  XButton,
  Swiper,
  SwiperItem
} from 'vux'
export default {
  name: 'HelloWorld',
  components: {
    Flow,
    FlowState,
    FlowLine,
    Marquee,
    MarqueeItem,
    Panel,
    Previewer,
    Qrcode,
    Step,
    StepItem,
    XButton,
    Swiper,
    SwiperItem
  },
  methods: {
    show (index) {
      this.$refs.previewer.show(index)
    },
    nextStep () {
      this.step2 ++
    },
    demo01_onIndexChange (index) {
      this.demo01_index = index
    }
  },
  data () {
    return {
      steps: [
        {
          title: '已付款',
          isDone: true,
          lineDone: true
        },
        {
          title: '待接单',
          isDone: true,
          lineDone: false,
          tip: '进行中'
        },
        {
          title: '待收货',
          isDone: false,
          lineDone: false
        },
        {
          title: '已完成',
          isDone: false,
          lineDone: false
        }
      ],
      list: [{
        msrc: 'http://ww1.sinaimg.cn/thumbnail/663d3650gy1fplwu9ze86j20m80b40t2.jpg',
        src: 'http://ww1.sinaimg.cn/large/663d3650gy1fplwu9ze86j20m80b40t2.jpg',
        w: 800,
        h: 400
      },
      {
        msrc: 'http://ww1.sinaimg.cn/thumbnail/663d3650gy1fplwvqwuoaj20xc0p0t9s.jpg',
        src: 'http://ww1.sinaimg.cn/large/663d3650gy1fplwvqwuoaj20xc0p0t9s.jpg',
        w: 1200,
        h: 900
      }, {
        msrc: 'http://ww1.sinaimg.cn/thumbnail/663d3650gy1fplwwcynw2j20p00b4js9.jpg',
        src: 'http://ww1.sinaimg.cn/large/663d3650gy1fplwwcynw2j20p00b4js9.jpg'
      }],
      options: {
        getThumbBoundsFn (index) {
          // find thumbnail element
          let thumbnail = document.querySelectorAll('.previewer-demo-img')[index]
          // get window scroll Y
          let pageYScroll = window.pageYOffset || document.documentElement.scrollTop
          // optionally get horizontal scroll
          // get position of element relative to viewport
          let rect = thumbnail.getBoundingClientRect()
          // w = width
          return {x: rect.left, y: rect.top + pageYScroll, w: rect.width}
          // Good guide on how to get element coordinates:
          // http://javascript.info/tutorial/coordinates
        }
      },
      step2: 0
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
