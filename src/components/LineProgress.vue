<template>
  <div class="c-progress">
    <div class="c-progress-outer" :style="setProgressBgStyle" ref="progress">
      <div class="c-progress-inner" :style="setProgressStyle"></div>
    </div>
    <span class="label_percent" v-if="showPerText">{{percent}}%</span>
  </div>
</template>

<script>
export default {
  name: 'CProgress',
  props: {
    percent: {
      type: Number,
      default: 60
    },
    showPerText: {
      type: Boolean,
      default: true
    },
  },
  data () {
    return {
      progressWidth: 0, // 进度条当前的的宽度
    }
  },
  computed: {
    setProgressStyle () {
      return {
        width: `${this.percent}%`,
      }
    },
  },
  mounted () {

  },
  methods: {
    
  }
}
</script>

<style scoped lang="scss">
  .c-progress {
    width: 100%;
    border-radius: 5px;
    align-items: center;

    .label_percent{
      margin-left: 5px;
      font-size: 16px;
      font-weight: normal;
      color: #666;
      float:left;
      display: block;
      width: 100%;
    }
    
    .c-progress-outer {
      width: 100%;
      height: 10px;
      border-radius: 5px;
      background: #ebeef5;
      position: relative;
      display: flex;
      align-items: center;
      
      .c-progress-inner {
        width: 100px;
        height: 10px;
        background: #409EFF;
        border-radius: 5px;
      }
      
      .c-progress-slider {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #fff;
        border: 1px solid #409EFF;
        position: absolute;
        z-index: 10;
        left: 10px;
      }
    }
  }
</style>

