<template>
  <div id="app">
    <aside class="app-menu">
      <div class="menu-item" v-for="(item, index) in menu" :class="{'selected': item.page == current}" :key="index" @click="showContent(item.page)">{{item.name}}</div>
    </aside>
    <section class="app-content">
      <router-view/>
    </section>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      current: '',
      menu: [
        {
          name: 'detail',
          page: 'amount-detail'
        },
        {
          name: 'total',
          page: 'amount-total'
        }
      ]
    }
  },
  methods: {
    showContent (page) {
      this.current = page
      this.$router.push({name: page})
    }
  },
}
</script>

<style lang="sass" scoped>
@import "./app.scss";
</style>