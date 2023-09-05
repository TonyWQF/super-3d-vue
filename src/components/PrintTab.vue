

<template>
  <div class="print_process">
      <div class="panel_title">{{ ui_state.print_filename }}</div> 
      <img id="preview_show" :src="ui_state.print_preview=='data:image/png;base64,'?require('../assets/gcode.svg'):ui_state.print_preview" alt="">
      <div class="print_info">
        <div class="hint_container">
          <div class="print_hint">
          <span>Height:</span><span>{{ ui_state.nozzle_pos[2] }}mm</span>
          </div>
          <div class="print_hint">
          <span>Fan:</span><span>{{ ui_state.fan[0] }}%</span>
          </div>
          <!-- <div class="print_hint">
          <span>Time:</span><span>{{ print_time }}</span>
          </div>
          <div class="print_hint">
          <span>flowrate:</span><span>{{ print_flowrate }}%</span>
          </div> -->
        </div>
        <line-progress class="progress" :percent="ui_state.print_percent" :show-per-text="true" ></line-progress>
        <div class="print_btn_container" style="height: 30%;">
          <button v-if="isPaused==true" id="btn_resume" class="print_btn btn_style" @click="resumePrint">Resume</button>
          <button v-if="isPaused==false" id="btn_pause" class="print_btn btn_style" @click="pausePrint">Pause</button>
          <button id="btn_stop_print" class="print_btn btn_style" @click="stopPrint">Stop</button>
        </div>
      </div>  
  </div>
  <RequestImp ref="req" />
</template>

<script>
import { mapState } from "vuex";
import LineProgress from "./LineProgress.vue"
import RequestImp from "./RequestImplement.vue";

export default{
  components:{
    LineProgress,
    RequestImp,
  },
  methods:{
    resumePrint(){
      this.isPaused=false;
      this.$refs.req.resume_print();
    },
    pausePrint(){
      this.isPaused=true;
      this.$refs.req.pause_print();
    },
    stopPrint(){
      this.$refs.req.stop_print();
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
  computed:{
    ...mapState(['ui_state']),
  }
}
</script>


<style>

#preview_show{
  display: block;
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
  
  .hint_container{
    position: absolute;
    left: 5%;
    width:90%;
    height: 100%;
  }

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

    .print_hint{
    width: 50%;
    margin-top: 5px;
    float: left;
    font-size: large;
    font-weight: normal;
  }

}


/* Phone */
@media screen and (max-width:600px){
#preview_show{
  display: block;
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
  height: 60%;
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

    .hint_container{
      position: absolute;
      left: 5%;
      width:90%;
    }

    .print_btn_container{
      margin-top: 5%;
      position: relative;
      display: inline-block;
      width: 100%;
      height: 25%;
    }
  }
  
  .print_hint{
    width: 45%;
    max-width: 50%;
    margin-top: 5px;
    float: left;
    font-size: large;
    font-weight: normal;
  }
}


</style>