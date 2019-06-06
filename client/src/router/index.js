import Vue from 'vue'
import Router from 'vue-router'
import AmountDetailComponent from '../components/amount-detail/amount-detail.vue'
import AmountTotalComponent from '../components/amount-total/amount-total.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/amount'
    },
    {
      path: '/amount',
      name: 'amount'
    },
    {
      path: '/amount/detail',
      name: 'amount-detail',
      component: AmountDetailComponent
    },
    {
      path: '/amount/total',
      name: 'amount-total',
      component: AmountTotalComponent
    },
    {
      path: '*',
      redirect: '/amount'
    }
  ]
})
