<template>
  <div class="li_vessel" data-type="0">
    <div class="upload_item c-progress-outer" :style="setProgressBgStyle" ref="progress" 
      @touchstart.capture="touchStart" @touchend.capture="touchEnd" @click="oneself">
        <div class="c-progress-inner" :style="setProgressStyle"></div>
        <img class="upload_gcode_icon" :src="icon_data?icon_data:require('../assets/Bulbasaur_0.jpg')">
        <span class="upload_gcode_name">{{upload_filename}}</span>
        <span class="upload_gcode_percent">{{ upload_percentage }}%</span>
        <!-- <upload-item-option ref="option"></upload-item-option> -->
    </div>
    <div class="drawer_op">
      <div class="iconfont icon-trash1 icon—size"></div>
    </div>
  </div>
</template>

<script>
// import UploadItemOption from "./UploadItemOption.vue"

export default{
  
  components:{
    // UploadItemOption,
  },
  data(){
    return{
      icon_data:"",
      upload_filename:"filename.gcode",
      upload_percentage:45,

      startX: 0, //滑动开始
      endX:0, //滑动结束
    }    
  },
  methods:{
    // 向左滑动出现删除按钮时，点击区域取消
    oneself(e) {
      if (this.checkSlide()) {
        this.restSlide();
      } else {
        let parentElement = e.currentTarget.parentElement;
        this.restSlide();
        parentElement.dataset.type = 1;
      }
    },
    //滑动开始
    touchStart(e) {
      // 记录初始位置
      this.startX = e.touches[0].clientX;
    },
    //滑动结束
    touchEnd(e) {
      // 当前滑动的父级元素
      let parentElement = e.currentTarget.parentElement;
      // 记录结束位置
      this.endX = e.changedTouches[0].clientX;
      // 左滑大于30距离出现
      if (parentElement.dataset.type == 0 && this.startX - this.endX > 30) {
        this.restSlide();
        parentElement.dataset.type = 1;
        console.log("左滑");
      }
      // 右滑
      if (parentElement.dataset.type == 1 && this.startX - this.endX < -30) {
        this.restSlide();
        parentElement.dataset.type = 0;
        console.log("右滑");
      }
        this.startX = 0;
        this.endX = 0;
    },
    //判断当前是否有滑块处于滑动状态
    checkSlide() {
      let listItems = document.querySelectorAll(".li_vessel");
      console.log(listItems);
      for (let i = 0; i < listItems.length; i++) {
        if (listItems[i].dataset.type == 1) {
          return true;
        }
      }
      return false;
    },
    //复位滑动状态
    restSlide() {
      let listItems = document.querySelectorAll(".li_vessel");
      // 复位
      for (let i = 0; i < listItems.length; i++) {
        listItems[i].dataset.type = 0;
      }
    },
    //删除数据信息
    remove(e) {
      // 当前索引值
      let index = e.currentTarget.dataset.index;
      // 复位
      this.restSlide();
      // 删除数组lists中一个数据
      this.lists.splice(index, 1);
    },

  },
  computed:{
    setProgressStyle () {
      return {
        width: `${this.upload_percentage}%`,
      }
    },
  },
}
</script>


<style>
.icon—size{
  font-family: "iconfont" !important;
  font-size: 24px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.li_vessel {
  /* 全部样式 0.2秒 缓动*/
  transition: all 0.2s;
}
/* =0隐藏 */
.li_vessel[data-type="0"] {
  transform: translate3d(0, 0, 0);
}
/* =1显示 */
.li_vessel[data-type="1"] {
  /* -64px 设置的越大可以左滑的距离越远，最好与下面删除按钮的宽度以及定位的距离设置一样的值*/
  transform: translate3d(-64px, 0, 0);
}
/* 删除按钮 */
.li_vessel .drawer_op {
  width: 64px;
  height: 9rem;
  position: absolute;
  top: 0px;
  right: -64px;
  background: #232323;
  font-size: 16px;
  color: #fff;
  text-align: center;
  line-height: 9rem;
  text-align: center;
  border-radius: 2px;
}

.upload_item{
  width: 95%;
  height: 9rem;
  margin:1rem;
  border-radius: 5px;
  border: 1px solid #23232333;
  background: #ebeef5;
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden; /*消除图片带来的浮动*/

  .c-progress-inner {
    width: 100px;
    height: 9rem;
    background: #409EFF20;
    border-radius: 5px;
  }

  .upload_gcode_icon{
    position: absolute;
    display: block;
    width: 9rem;
    height: 9rem;
    left: 0;
    top: 0;
    padding: 1rem;
  }
  .upload_gcode_name{
    position: absolute;
    left: 10rem;
    line-height: 9rem;
    vertical-align: middle;
    float: left;
    font-size:medium;
    font-weight: normal;
  }
  .upload_gcode_percent{
    position: absolute;
    right: 1rem;
    margin-right: 1rem;
    line-height: 9rem;
    vertical-align: middle;
    font-size: large;
    font-weight: bold;
  }
}


</style>