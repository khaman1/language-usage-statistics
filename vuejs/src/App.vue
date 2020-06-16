<template>
  <div id="app">
    <Search />
  </div>
</template>

<script>
import Search from './components/Search.vue'

export default {
  name: 'App',
  components: {
    Search
  },
}
</script>

<style>
@import './assets/static/css/main.css';
@import './assets/static/css/table.css';
</style>
