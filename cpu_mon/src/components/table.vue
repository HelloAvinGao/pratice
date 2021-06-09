<template>
  <div class="tables">
    <a-row>
      <a-col
        :xs="{ span: 24}"
        :sm="{ span: 24}"
        :md="{ span: 12}"
        :lg="{ span: 12}"
        v-for="item in pieitems"
        :key="item .str"
      >
        <div :id="`${item}`" :style="{width: 'auto', height: '15rem'}"></div>
      </a-col>
    </a-row>
    <a-row>
      <a-col
        :xs="{ span: 24}"
        :sm="{ span: 24}"
        :md="{ span: 12}"
        :lg="{ span: 12}"
        v-for="item in lineitems"
        :key="item .str"
      >
        <div :id="`${item}`" :style="{width: 'auto', height: '15rem'}"></div>
      </a-col>
    </a-row>
    <a-table :columns="columnsDF" :data-source="dataDF" :pagination="false" :scroll="{ y: 240 }" />
  </div>
</template>
<script>
const columnsDF = [
  {
    title: "Filesystem",
    dataIndex: "Filesystem",
    key: "Filesystem",
    sorter: (a, b) => a.Filesystem.length - b.Filesystem.length,
    sortDirections: ["descend", "ascend"]
  },
  {
    title: "Size",
    dataIndex: "Size",
    key: "Size",
    sorter: (a, b) => a.Size.length - b.Size.length,
    sortDirections: ["descend", "ascend"]
  },
  {
    title: "Avail",
    dataIndex: "Avail",
    key: "Avail",
    sorter: (a, b) => a.Avail.length - b.Avail.length,
    sortDirections: ["descend", "ascend"]
  },
  {
    title: "Used",
    dataIndex: "Used",
    key: "Used",
    sorter: (a, b) => a.Filesystem.length - b.Filesystem.length,
    sortDirections: ["descend", "ascend"]
  },
  {
    title: "Use%",
    dataIndex: "Use%",
    key: "Use%",
    sorter: (a, b) => a.Used.length - b.Used.length,
    sortDirections: ["descend", "ascend"]
  },
  {
    title: "Mounted on",
    dataIndex: "Mountedon",
    key: "Mountedon",
    sorter: (a, b) => a.Mountedon.length - b.Mountedon.length,
    sortDirections: ["descend", "ascend"]
  }
];
const dataDF = [];
const pieitems = ["KiB Mem ", "KiB Swap"];
const lineitems = ["%Cpu(s)", "load_aver"];
export default {
  name: "tables",
  props: {},
  mounted: function() {
    this.loadData();
  },
  methods: {
    loadData: function() {
      this.axios({
        url: "sys_mon.json",
        method: "GET",
        crossdomain: true
      }).then(res => {
        let dataobj = res.data;
        let maxDate = 0;
        let timeData = [];
        for (let key in dataobj) {
          let num = parseInt(key);
          timeData.push(num);
          if (num > maxDate) {
            maxDate = num;
          } else {
            continue;
          }
        }

        console.log(timeData);
        console.log(timeData.sort());
        console.log(timeData.sort().slice(0, 1));

        maxDate = maxDate.toString();
        let dfData = dataobj[maxDate]["df_h"];
        let topData = dataobj[maxDate]["top"];

        // df data to table
        for (let keys in dfData) {
          if (keys == "Filesystem") {
            continue;
          } else {
            let keyList = {};
            for (let key in dfData[keys]) {
              if (key == "Mounted on") {
                keyList["Mountedon"] = dfData[keys][key];
              } else {
                keyList[key] = dfData[keys][key];
              }
            }
            dataDF.push(keyList);
          }
        }

        let legendDataCPU = ["hi", "id", "ni", "si", "st", "sy", "us", "wa"];
        let legendDataLoadAverage = ["1min", "5min", "15min"];
        let xaxisData = [];

        for (let i in topData) {
          let dataArr = [];
          let name = "";
          let ids = "";
          let seriesDatas = [];
          if (i == "KiB Mem " || i == "KiB Swap") {
            for (let topkeys in topData[i]) {
              if (topkeys == "total") {
                continue;
              } else {
                dataArr.push({
                  name: topkeys,
                  value: topData[i][topkeys]
                });
              }
            }
            let title = {
              text: i,
              // subtext: "纯属虚构",
              left: "center"
            };
            let series = {
              name: i
            };
            this.loadPIE(i, title, series, dataArr);
          } else if (i == "running_time") {
            continue;
          } else {
            // top 折线图
            name = i;
            ids = i;
            if (timeData.length < 24) {
              xaxisData = timeData.sort();
            } else {
              xaxisData = timeData
                .sort()
                .slice(timeData.length - 24, timeData.length);
            }
            if (i == "%Cpu(s)") {
              for (let n = 0; n < legendDataCPU.length; n++) {
                let seriesData = [];
                for (let k = 0; k < xaxisData.length; k++) {
                  seriesData.push(
                    dataobj[xaxisData[k].toString()]["top"][i][legendDataCPU[n]]
                  );
                }
                seriesDatas.push({
                  name: legendDataCPU[n],
                  type: "line",
                  stack: "总量",
                  data: seriesData
                });
              }
              this.loadLine(ids, name, legendDataCPU, xaxisData, seriesDatas);
            } else if (i == "load_aver") {
              for (let l = 0; l < legendDataLoadAverage.length; l++) {
                let seriesData = [];
                for (let m = 0; m < xaxisData.length; m++) {
                  seriesData.push(
                    dataobj[xaxisData[m].toString()]["top"][i][l]
                  );
                }
                seriesDatas.push({
                  name: legendDataLoadAverage[l],
                  type: "line",
                  stack: "总量",
                  data: seriesData
                });
              }
              this.loadLine(
                ids,
                name,
                legendDataLoadAverage,
                xaxisData,
                seriesDatas
              );
            }
          }
        }

        // title = 'hello'  string.
        // legendData = ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"]   array.
        // xaxis = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]   x轴数据  array.
        // series = [{name: "邮件营销",type: "line",stack: "总量",data: [120, 132, 101, 134, 90, 230, 210]},]
        // this.loadLine(ids,linetitle,legendData,xaxisData,seriesDatas);
      });
    },
    loadPIE: function(id, title, series, memArr) {
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById(id));
      // 绘制图表配置
      let option = {
        title: {
          text: title["text"],
          subtext: title["subtext"],
          left: title["left"]
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        series: [
          {
            name: series["name"],
            type: "pie",
            redius: "55%",
            center: ["50%", "60%"],
            data: memArr
          }
        ]
      };
      // 窗口大小自适应方案
      myChart.setOption(option);
      setTimeout(function() {
        window.onresize = function() {
          myChart.resize();
        };
      }, 200);
    },
    loadLine: function(id, title, legendData, xaxisData, seriesData) {
      let myChart = this.$echarts.init(document.getElementById(id));
      let option = {
        title: {
          text: title,
          left: "10%"
        },
        tooltip: {
          trigger: "axis"
        },
        legend: {
          data: legendData,
          top: "10%"
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true
        },
        toolbox: {
          feature: {
            top: "10%",
            mark: {
              // '辅助线开关'
              show: true
            },
            dataView: {
              //数据视图工具，可以展现当前图表所用的数据，编辑后可以动态更新
              show: true, //是否显示该工具。
              title: "数据视图",
              readOnly: false, //是否不可编辑（只读）
              lang: ["数据视图", "关闭", "刷新"], //数据视图上有三个话术，默认是['数据视图', '关闭', '刷新']
              backgroundColor: "#fff", //数据视图浮层背景色。
              textareaColor: "#fff", //数据视图浮层文本输入区背景色
              textareaBorderColor: "#333", //数据视图浮层文本输入区边框颜色
              textColor: "#000", //文本颜色。
              buttonColor: "#c23531", //按钮颜色。
              buttonTextColor: "#fff" //按钮文本颜色。
            },
            magicType: {
              //动态类型切换
              show: true,
              title: "切换", //各个类型的标题文本，可以分别配置。
              type: ["line", "bar", "stack", "tiled"] //启用的动态类型，包括'line'（切换为折线图）, 'bar'（切换为柱状图）, 'stack'（切换为堆叠模式）, 'tiled'（切换为平铺模式）
            },
            restore: {
              //配置项还原。
              show: true, //是否显示该工具。
              title: "还原"
            },
            saveAsImage: {
              //保存为图片。
              show: true, //是否显示该工具。
              type: "png", //保存的图片格式。支持 'png' 和 'jpeg'。
              name: "", //保存的文件名称，默认使用 title.text 作为名称
              backgroundColor: "#ffffff", //保存的图片背景色，默认使用 backgroundColor，如果backgroundColor不存在的话会取白色
              title: "保存为图片",
              pixelRatio: 1 //保存图片的分辨率比例，默认跟容器相同大小，如果需要保存更高分辨率的，可以设置为大于 1 的值，例如 2
            },
            dataZoom: {
              //数据区域缩放。目前只支持直角坐标系的缩放
              show: true, //是否显示该工具。
              title: "缩放", //缩放和还原的标题文本
              xAxisIndex: 0, //指定哪些 xAxis 被控制。如果缺省则控制所有的x轴。如果设置为 false 则不控制任何x轴。如果设置成 3 则控制 axisIndex 为 3 的x轴。如果设置为 [0, 3] 则控制 axisIndex 为 0 和 3 的x轴
              yAxisIndex: false //指定哪些 yAxis 被控制。如果缺省则控制所有的y轴。如果设置为 false 则不控制任何y轴。如果设置成 3 则控制 axisIndex 为 3 的y轴。如果设置为 [0, 3] 则控制 axisIndex 为 0 和 3 的y轴
            }
          }
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: xaxisData
        },
        yAxis: {
          type: "value"
        },
        series: seriesData
      };

      myChart.setOption(option);
    }
  },
  data() {
    return {
      dataDF,
      columnsDF,
      pieitems,
      lineitems
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
