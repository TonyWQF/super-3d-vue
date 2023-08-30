<template>
  <div class="upload_item c-progress-outer" :style="setProgressBgStyle" ref="progress" @click="openOp">
    <div class="c-progress-inner" :style="setProgressStyle">
    </div>
    <img class="upload_gcode_icon" :src="icon_data?icon_data:require('../assets/Bulbasaur_0.jpg')">
    <span class="upload_gcode_name">{{upload_filename}}</span>
    <span class="upload_gcode_percent">{{ upload_percentage }}%</span>
    <upload-item-option ref="option"></upload-item-option>
  </div>
</template>

<script>
import UploadItemOption from "./UploadItemOption.vue"

export default{
  
  components:{
    UploadItemOption,
  },
  data(){
    return{
      icon_data:"",
      upload_filename:"filename.gcode",
      upload_percentage:72,
    }    
  },
  methods:{
    openOp(){
      console.log("xxxx");
      this.$refs.option.openOption();
    }
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
.upload_item{
  width: 95%;
  height: 9rem;
  margin:1rem;
  border-radius: 5px;
  border: 1px solid #23232333;

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

.c-progress-outer {
  height: 9rem;
  border-radius: 5px;
  background: #ebeef5;
  position: relative;
  display: flex;
  align-items: center;
  
  .c-progress-inner {
    width: 100px;
    height: 9rem;
    background: #409EFF20;
    border-radius: 5px;
  }
}

</style>