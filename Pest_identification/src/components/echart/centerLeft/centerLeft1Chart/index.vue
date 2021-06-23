<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue';
export default {
  data () {
    return {
      cdata: {
        xData: ["黑蚱蝉", "蟪蛄", "蒙古寒蝉", "茶翅蝽", "菜蝽", "赤条蝽"],
        seriesData: [
          { value: 10, name: "黑蚱蝉" },
          { value: 5, name: "蟪蛄" },
          { value: 15, name: "蒙古寒蝉" },
          { value: 25, name: "茶翅蝽" },
          { value: 20, name: "菜蝽" },
          { value: 35, name: "赤条蝽" }
        ]
      }
    }
  },
  components: {
    Chart,
  },
  mounted () {
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
</style>