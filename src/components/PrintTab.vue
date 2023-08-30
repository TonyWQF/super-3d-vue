

<template>
  <div class="print_process">
      <div class="panel_title">Filename</div>
      <img id="preview_show" :src="preview_img_data?preview_img_data:require('../assets/Bulbasaur_0.jpg')" alt="">
      <div class="print_info">
        <div class="print_hint">
        <span>Z-Height:</span><span>{{ z_height }}mm</span>
        </div>
        <div class="print_hint">
        <span>Speed:</span><span>{{ print_speed }}%</span>
        </div>
        <div class="print_hint">
        <span>Time:</span><span>{{ print_time }}</span>
        </div>
        <div class="print_hint">
        <span>flowrate:</span><span>{{ print_flowrate }}%</span>
        </div>
        <line-progress class="progress" :percent="print_percentage" :show-per-text="true" ></line-progress>
        <div class="print_btn_container" style="height: 30%;">
          <button v-if="isPaused==true" id="btn_resume" class="print_btn btn_style" @click="resumePrint">Resume</button>
          <button v-if="isPaused==false" id="btn_pause" class="print_btn btn_style" @click="pausePrint">Pause</button>
          <button id="btn_stop_print" class="print_btn btn_style">Stop</button>
        </div>
      </div>  
  </div>
</template>

<script>
import LineProgress from "./LineProgress.vue"

export default{
  components:{
    LineProgress,
  },
  methods:{
    resumePrint(){
      this.isPaused=false;
    },
    pausePrint(){
      this.isPaused=true;
    },
  },
  data(){
    return{
      z_height:200,
      print_speed:100,
      print_time:"24:24:24",
      print_flowrate:100,
      isPaused:false,

      print_percentage:45,
      preview_img_data:"",
    };
  },
}
</script>


<style>

#preview_show{
  width: 80%;
  max-height: 50%;
  margin-top: 2%;
  margin-bottom: 2%;
  margin-left: 10%;
  margin-right: 10%;
}

.print_process{
  float:left;
  margin: 1%;
  width: 48%;
  height: 98%;
  box-shadow: 0 8px 50px #23232333;
  text-align: center;
}

.print_info{
  float: left;
  width: 100%;
  height: 20%;
  font-size: small;
  font-weight: lighter;
  position: relative;
  text-align: center;
  margin: 0;

  .progress{
    width: 80%;
    margin-top: 20%;
    margin-left: 10%;
  }
  .print_btn_container{
    margin-top: 5%;
    position: relative;
    display: inline-block;
    width: 100%;
    height: 25%;
  }
}


/* Phone */
@media screen and (max-width:600px){
#preview_show{
  height: 42%;
  width: 50%;
  margin-top: 0.5%;
  margin-bottom: 0.5%;
  margin-left: 25%;
  margin-right: 25%;
}

.print_process{
  float:left;
  margin: 1%;
  width: 100%;
  height: 55%;
  box-shadow: 0 8px 50px #23232333;
  text-align: center;
  margin-left: -1.5rem;
}

.print_info{
    float: left;
    width: 100%;
    height: 27%;
    font-size: small;
    font-weight: lighter;
    position: relative;
    text-align: center;
    margin: 0;
    .print_btn_container{
      margin-top: 1%;
      position: relative;
      display: inline-block;
      width: 100%;
      height: 25%;
    }
  }


}


</style>