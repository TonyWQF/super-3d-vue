<template>
  <div class="content_box" id="tempreture_tb">
    <div class="panel_title">Tempreture</div>

    <div style="display: flex; justify-content: center; align-items: center;">
      <img class="icon" src="../assets/nozzle_icon.png">
      <span>Nozzle:</span><span id="tar_head">{{ TargetHead }}</span><span>℃</span>
    </div>              
    <div class="input-container">
      <input placeholder="Enter Target Tempreture" class="input-field" type="number" @keyup.enter="set_nozzle_temp(event)" id="targetTemp0" v-model="EnterNozzle">
      <label for="input-field" class="input-label">Enter Tar-Temp.</label>
      <span class="input-highlight"></span>
    </div>

    <div style="display: flex; justify-content: center; align-items: center;">
      <img class="icon" src="../assets/bed_icon.png" >
      <span>Bed:</span><span id="tar_bed">{{ TargetBed }}</span><span>℃</span>
    </div>  
    <div class="input-container">
      <input placeholder="Enter Target Tempreture" class="input-field" type="number"  @keyup.enter="set_bed_temp(event)" id="targetBedTemp" v-model="EnterBed">
      <label for="input-field" class="input-label">Enter Tar-Temp.</label>
      <span class="input-highlight"></span>
    </div>
    <div class="filament_tb">
      <!-- <div class="panel_title">Filament</div> -->
      <button class="btn_style" :disabled="ui_state.isRemotePrinting" @click="extrude()">Load</button>
      <button class="btn_style" :disabled="ui_state.isRemotePrinting" @click="stop()">Stop</button>
      <button class="btn_style" :disabled="ui_state.isRemotePrinting" @click="retract()">Unload</button>
    </div>
  </div>
  <RequestImp ref='req'/>
</template>

<script>
import RequestImp from "./RequestImplement.vue"
import { mapState } from 'vuex';
export default{
  components: {
    RequestImp
  },
  data(){
    return{
      TargetHead:"0",
      TargetBed:"0",
      EnterNozzle:"0",
      EnterBed:"0",
    };
  },
  methods:{
    set_nozzle_temp() {
      var res = this.$refs.req.set_temp(0, this.EnterNozzle)
      this.TargetHead = this.EnterNozzle;
      console.log(res[1])
    },

    set_bed_temp() {
      this.$refs.req.set_temp(1, this.EnterBed)
      this.TargetBed = this.EnterBed;
    },

    extrude() {
      this.$refs.req.extrude(100)
    },

    stop() {
      this.$refs.req.quick_stop()
    },

    retract() {
      this.$refs.req.retract(50)
    },
  },
  computed:{
    ...mapState(['ui_state']),
  }
}

</script>

<style>

.filament_tb{
  margin-top: 1.6rem;
}


#tempreture_tb{
  width: 48%;
}

/* Input container */
.input-container {
  position: relative;
  margin: 20px;
}

/* Input field */
.input-field {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-bottom: 2px solid #ccc;
  outline: none;
  background-color: transparent;
}

/* Input label */
.input-label {
  position: absolute;
  top: 0;
  left: 0;
  font-size: 16px;
  color: rgba(204, 204, 204, 0);
  pointer-events: none;
  transition: all 0.3s ease;
}

/* Input highlight */
.input-highlight {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2px;
  width: 0;
  background-color: gray;
  transition: all 0.3s ease;
}

/* Input field:focus styles */
.input-field:focus + .input-label {
  top: -20px;
  font-size: 12px;
  color: gray;
}

.input-field:focus + .input-label + .input-highlight {
  width: 100%;
}

@media screen and (max-width:600px){
.input-container {
    position: relative;
    margin: 0px;
  }
  #tempreture_tb{
    position: absolute;
    left: 0%;
    top: 0%;
    height: 45%;
    width: 98%;
    margin-left: -1.2rem;
  }
}

</style>