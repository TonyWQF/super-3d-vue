

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
          <button v-if="isPaused==true" 
            class="print_btn btn_style"
            @click="resumePrint"
            :disabled="!ui_state.isRemotePrinting">Resume</button>
          <button v-if="isPaused==false" 
            class="print_btn btn_style"
            @click="pausePrint"
            :disabled="!ui_state.isRemotePrinting">Pause</button>
          <button 
            class="print_btn btn_style"
            @click="stopPrint">Stop</button>
          <dialog-tab ref="finish_dialog"
            :dialog_type="DialogFinishType"
            :hint="DialogFinishHint"
            :title="DialogFinishTitle"
            @confirm="finished_confirm"
          ></dialog-tab>
          <dialog-tab ref="pause_dialog"
            :dialog_type="DialogPausedType"
            :hint="DialogPausedHint"
            :title="DialogPausedTitle"
            @confirm="filament_confirm"
          ></dialog-tab>
        </div>
      </div>  
  </div>
  <RequestImp ref="req" />
</template>

<script>
import { mapState } from "vuex";
import LineProgress from "./LineProgress.vue"
import DialogTab from "./DialogTab.vue"
import RequestImp from "./RequestImplement.vue";

export default{
  components:{
    LineProgress,
    DialogTab,
    RequestImp,
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

      DialogFinishTitle:"Print Finish",
      DialogFinishHint:"The current gcode has been printed, and after confirmation, select a new file to print.",
      DialogFinishType:"Confirm",

      DialogPausedTitle:"Print Paused",
      DialogPausedHint:"Printer has been paused.",
      DialogPausedType:"Confirm",
    };
  },
  computed:{
    ...mapState(['ui_state']),
    printer_state(){
      return this.ui_state.printer_status
    },

    print_finish(){
      return this.ui_state.print_percent
    },
  },
  watch:{
    printer_state(cur_state, old_state){
      console.log(old_state+"--->"+cur_state);
      if (this.ui_state.isRemotePaused==true) {
        this.$refs.pause_dialog.show();
      }

      if(this.ui_state.printer_status == "PRINT_STATE_PRINTING"){
        this.isPaused = false;
      }
    },
    print_finish(cur_state, old_state){
      console.log(old_state+"--->"+cur_state);
      if (this.ui_state.print_percent=='100') {
        this.$refs.finish_dialog.show();
      }
    },
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
      this.finished_confirm();
      this.$refs.req.stop_print(); 
    },

    finished_confirm(){
      this.$store.dispatch("update_print_filename", "No Gcode is printing");
      this.$store.dispatch("update_print_preview", "data:image/png;base64,");
      this.$store.dispatch("change_print_percent", "0");
    },

    filament_confirm(){
      this.isPaused=true;
    },

  },
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
  width: 60%;
  height: 98%;
  box-shadow: 0 8px 50px #23232333;
  text-align: center;
}

.print_info{
  float: left;
  width: 100%;
  height: fit-content;
  font-size: small;
  font-weight: lighter;
  position: relative;
  text-align: center;
  margin: 0;
  margin-top: 2rem;
  
  .hint_container{
    display: flex;
    align-items: center;
    justify-content: center;
    
  }

  .progress{
    width: 100%;
    margin-top: 2rem;
    padding: 0% 10%;
    height: fit-content;
  }
  .print_btn_container{
    position: relative;
    display: inline-block;
    width: 100%;
    height: fit-content;
    margin-top: 2rem;
  }

    .print_hint{
    width: 50%;
    font-size: large;
    font-weight: normal;
    max-width: 50%;
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
  height: 75%;
  box-shadow: 0 8px 50px #23232333;
  text-align: center;
  margin-top: -6rem;
  margin-left: -2.5rem;
}

}


</style>