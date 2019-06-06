<template>
  <section class="amount-detail">
    <div class="amount-detail-container" id="amount-detail-container"></div>
    <button class="amount-detail-btn" :disabled="btnDisabled" @click="saveCurrentData">保存当前数据</button>
  </section>
</template>

<script>
import Http from '../../../dependencies/modules/Http.class.js'
import Highcharts from 'highcharts/highstock';
export default {
  name: 'AmountDetailComponent',
  data() {
    return {
      highCharts: null,
      btnDisabled: false
    }
  },
  methods: {
    initHighcharts () {
      this.highCharts = Highcharts.chart('amount-detail-container', {
        chart: {
          type: 'column'
        },
        title: {
          text: '每年各货物出货量'
        },
        xAxis: {
          title: {
            text: '货物种类'
          },
          categories: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        },
        yAxis: {
          title: {
            text: '出货量'
          },
          ceiling: 3000
        },
        series: [{
          name: ``,
          data: [],
        }]
      })
    },
    updateChart (data) {
      let series = []
      data.forEach(item => {
        series.push([item.kind, item.amount])
      })
      this.highCharts.update({
        series: [{
          name: `year ${data[0].year}`,
          data: series
        }]
      })
    },
    getChartData () {
      Http.send({
        url: 'AmountDetail',
        method: 'get'
      })
      .success(data => {
        this.updateChart(data)
      })
    },
    saveCurrentData () {
      Http.send({
        url: 'AmountTotal',
        method: 'post'
      })
      .before(() => {
        this.btnDisabled = true
      })
      .default(() => {
        this.btnDisabled = false
      })
    }
  },
  mounted() {
    this.initHighcharts()
    this.getChartData()
    setInterval(this.getChartData, 10000)
  }
}
</script>

<style lang="sass" scoped>
@import "./amount-detail.scss";
</style>
