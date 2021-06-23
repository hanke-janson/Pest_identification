<template>
  <div id="centerRight1">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span style="color:#5cd9e8">
          <icon name="chart-line"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2">无人机列表</span>
        </div>
      </div>
      <div class="d-flex jc-center body-box">
        <dv-scroll-board :config="config" style="width:5.375rem;height:4.28rem" />
      </div> 
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      config: {
        header: ["编号", "负责人", "运行情况"],
        data: [
          ["编号1", "admin", "<span  class='colorGrass'>正常</span>"],
          ["编号2", "admin", "<span  class='colorRed'>故障</span>"],
          ["编号3", "admin", "<span  class='colorGrass'>正常</span>"],
          ["编号4", "admin", "<span  class='colorGrass'>正常</span>"],
          ["编号5", "admin", "<span  class='colorGrass'>正常</span>"],
          ["编号6", "admin", "<span  class='colorGrass'>正常</span>"],
          ["编号7", "admin", "<span  class='colorGrass'>正常</span>"],
          ["编号8", "admin", "<span  class='colorRed'>故障</span>"],
          ["编号9", "admin", "<span  class='colorRed'>故障</span></span>"],
          ["编号10", "admin", "<span  class='colorGrass'>正常</span>"]
        ],
        rowNum: 7, //表格行数
        headerHeight: 35,
        headerBGC: "#0f1325", //表头
        oddRowBGC: "#0f1325", //奇数行
        evenRowBGC: "#171c33", //偶数行
        index: true,
        columnWidth: [50],
        align: ["center"]
      }
    };
  },
  components: {},
  mounted() {},
  methods: {}
};
</script>

<style lang="scss">
#centerRight1 {
  
  padding: 0.2rem;
  height: 5.125rem;
  width: 5.75rem;
  border-radius: 0.0625rem;
  .bg-color-black {
    height: 4.8125rem;
    border-radius: 0.125rem;
  }
  .text {
    color: #c3cbde;
  }
  .body-box {
    border-radius: 0.125rem;
    overflow: hidden;
  }
}
</style>