<template>
  <div class="temp-card">
    <div class="show-card">
      <img class="tempicon" src="../assets/bed_icon.png" alt="">
      <p class="cur-temp-style">{{BedTemp}}</p>
      <p class="tar-temp-style">/{{BedTargetTemp}}℃</p>
      <!-- <p class="label-hint-style">Bed</p> -->
    </div>
    <div class="show-card">
      <img class="tempicon" src="../assets/nozzle_icon.png" alt="">
      <p class="cur-temp-style">{{NozzleTemp}}</p>
      <p class="tar-temp-style">/{{NozzleTargetTemp}}℃</p>
      <!-- <p class="label-hint-style">Head</p> -->
    </div>
  </div>
  <RequestImp ref="req" />
</template>

<script>
import { mapMutations, mapState } from 'vuex';
import RequestImp from "./RequestImplement.vue";

export default{
  components: {
    RequestImp,
  },
  created() {
    setInterval(this.get_status, 1000);
  },
  data() {
    return {
      NozzleTargetTemp:0,
      NozzleTemp: 0,
      BedTargetTemp:0,
      BedTemp: 0,

      movement_operable:false,
      isRemotePrinting:false,
      isRemotePaused:true,

      nozzle_pos:[],
      print_percent:0,
      fan_speed:[],
    }
  },
  methods: {
    ...mapMutations(["change_printer_status"]),
    ...mapMutations(["change_print_percent"]),
        
    get_status() {
      var retval = this.$refs.req.get_status()

      if(retval[0] == true) {
        this.printer_update_info(retval)
      }else{
        this.webInitFailed();
      }
    },
    updateParems(){
      this.$store.dispatch('update_is_inited', true)
      this.$store.dispatch('update_isRemotePrinting', this.isRemotePrinting)
      this.$store.dispatch('update_movement_operable', this.movement_operable)
      this.$store.dispatch('update_fan_speed', this.fan_speed)
      this.$store.dispatch('update_position', this.nozzle_pos)
      this.$store.dispatch('update_print_percent',  this.print_percent)
    },
    webInitFailed(){
      console.log("inited failed");
      this.$store.dispatch('update_is_inited', false)
    },
    printer_set_paused(status){
      if(status)
        this.isRemotePaused = true
      else
        this.isRemotePaused = false
    },
    update_print_tab(){
      this.$store.dispatch('update_isGcodeInfoGet', true);

      var ret_info = this.$refs.req.preview_last_file();
      console.log(ret_info)
      var info_item = ret_info.split(',')

      this.ui_state.print_filename = info_item[0]
      this.ui_state.print_preview = info_item[1]

      this.$store.dispatch('update_print_preview', this.print_preview)
        this.$store.dispatch('update_print_filename', this.preview_filename)
    },
    printing_info_process(){
      if (this.ui_state.printer_status== "PRINT_STATE_PRINTING"||
        this.ui_state.printer_status== "PRINT_STATE_PAUSE"||
        this.ui_state.printer_status== "PRINT_STATE_FIL_FAULT_PAUSE"||
        this.ui_state.printer_status== "PRINT_STATE_FAULT_PAUSE"||
        this.ui_state.printer_status== "PRINT_STATE_PAUSE") {

          this.movement_operable = false;
          this.isRemotePrinting = true;

        if (this.ui_state.isGcodeInfoGet == false) {
            // 获取一次   打印信息
            this.update_print_tab();
        }

        if (this.ui_state.printer_status== "PRINT_STATE_FIL_FAULT_PAUSE"||
          this.ui_state.printer_status== "PRINT_STATE_FAULT_PAUSE"||
          this.ui_state.printer_status== "PRINT_STATE_PAUSE")  {
            this.printer_set_paused(true);
        }else{
          this.printer_set_paused(false);
        }

        this.$store.dispatch('update_isRemotePaused', this.isRemotePaused);
      }
    },
    idle_info_process(){
      if (this.ui_state.printer_status == "PRINT_STATE_IDLE") {
        this.movement_operable = true; 
        this.isRemotePrinting = false;
      }
    },
    printer_update_info(retval){
      var status_text = retval[1].slice(1,-1)
      console.log(status_text)
      var status_item = status_text.split(',')
      this.NozzleTemp = status_item[1]
      this.NozzleTargetTemp = status_item[2]
      this.BedTemp = status_item[3]
      this.BedTargetTemp = status_item[4]
      this.nozzle_pos = [status_item[5], status_item[6], status_item[7], status_item[8]]
      this.print_percent = Math.round(status_item[9]/10) 
      this.fan_speed = [status_item[10], status_item[11], status_item[12], status_item[13], status_item[14], status_item[15]];

      this.$store.dispatch('update_now_status', status_item[0])

      this.printing_info_process();
        
      this.idle_info_process();

      this.updateParems();
    }
    
  },

  computed:{
    ...mapState(['ui_state'])
  }
}
</script>

<style>
.temp-card{
  width:34rem;
  height:8rem;
  padding-top: 2rem;
  padding-right: 1.2rem;
  margin: 0;
  float: right;
  display:block;
  /* box-shadow: 0 8px 50px #23232333; */
  p{
    display: block;
  }
}
.show-card{
  float:right;
  width: 14rem;
  height: 10rem;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 1.5rem;
  grid-row-gap: 0px;
  margin-right: 1.5rem;
  padding-right: 2rem;
}
.cur-temp-style{
  font-size:28px;
  font-weight: bold;
  margin: 0;
  bottom: 0;
  left: 0;
  grid-area: 1 / 3 / 2 / 5;
  margin-left: -1.2rem;
  padding-top: 0.2rem;
  padding-right: 3rem;
}
.tar-temp-style{
  font-size: large;
  font-weight: normal;
  margin: 0;
  bottom: 0;
  right: 0;
  padding-top: 1.2rem;
  padding-right: 3rem;
  grid-area: 1 / 5 / 2 / 7;
}
.label-hint-style{
  font-size: larger;
  font-weight: bolder;
  margin: 0;
  bottom: 0;
  left: 0;
  text-align: bottom;
  grid-area: 1 / 3 / 2 / 5;
}
.tempicon {
  display: inline-block;
  width: 35px;
  height: 35px;
  top: 0;
  right: 0;
  grid-area: 1 / 1 / 2 / 3;
}


/* Phone */
@media screen and (max-width:600px){


.temp-card{
  width:100%;
  height:4rem;
  margin-top: -1.5rem;
  margin-left: 1.5rem;
  float: left;
  display:block;
  /* box-shadow: 0 8px 50px #23232333; */
  p{
    display: block;
  }
}
.show-card{
  float:right;
  width: 14rem;
  height: 10rem;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 1.5rem;
  grid-row-gap: 0px;
  margin-top: -2rem;
  padding-right: 2rem;
}

.cur-temp-style{
  font-size:28px;
  font-weight: bold;
  margin: 0;
  bottom: 0;
  left: 0;
  text-align: left;
  grid-area: 1 / 3 / 2 / 5;
  margin-left: -1.1rem;
  padding-top: 0.3rem;
  padding-right: 3rem;
}
.tar-temp-style{
  font-size: large;
  font-weight: normal;
  margin: 0;
  bottom: 0;
  right: 0;
  text-align: center;
  padding-top: 1.1rem;
  grid-area: 1 / 5 / 2 / 7;
  margin-left: -0.7rem;
}
.label-hint-style{
  font-size: larger;
  font-weight: bolder;
  margin: 0;
  bottom: 0;
  left: 0;
  text-align: bottom;
  grid-area: 1 / 3 / 2 / 5;
}
.tempicon {
  display: inline-block;
  width: 35px;
  height: 35px;
  top: 0;
  right: 0;
  grid-area: 1 / 1 / 2 / 3;
}

}


</style>