<template>
  <section class="amount-total">
    <div class="amount-total-container" id="amount-total-container"></div>
  </section>
</template>

<script>
import Http from '../../../dependencies/modules/Http.class.js'
import Highcharts from 'highcharts/highstock';
export default {
  name: 'AmountTotalComponent',
  data() {
    return {
      highCharts: null
    }
  },
  methods: {
    initHighcharts () {
      this.highCharts = Highcharts.chart('amount-total-container', {
        title: {
          text: '各货物近10年出货量'
        },
        yAxis: {
          title: {
            text: '出货量'
          },
          ceiling: 3000
        },
        legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
        },
        xAxis: {
          title: {
            text: '年份'
          },
          categories: []
        },
        plotOptions: {
          series: {
            label: {
              connectorAllowed: false
            }
          }
        },
        series: (function () {
          let series = []
          for (let i = 0; i < 10; i++) {
            series.push({
              name: '',
              data: []
            })
          }
          return series
        })()
      });
    },
    updateChart (data) {
      let yearSet = new Set();
      let series = {}
      data.forEach(item => {
        yearSet.add(item.year.toString())
        if (item.kind in series) {
          series[item.kind].data.push([item.year.toString(), item.amount])
        } else {
          series[item.kind] = {
            name: `货物${item.kind}`,
            data: [[item.year.toString(), item.amount]]
          }
        }
      })
      this.highCharts.xAxis[0].update({
        categories: Array.from(yearSet).sort()
      });
      this.highCharts.update({
        series: Object.values(series)
      })
    },
    getChartData () {
      Http.send({
        url: 'AmountTotal',
        method: 'get'
      })
      .success(data => {
        this.updateChart(data)
      })
      .default(() => {
      })
    }
  },
  mounted() {
    this.initHighcharts()
    this.getChartData()
  }
}
</script>

<style lang="sass" scoped>
@import "./amount-total.scss";
</style>
