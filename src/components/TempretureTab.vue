<template>
  <div>
    <div class="panel_title">Tempreture</div>
    <br>
    <div style="display: flex; justify-content: center; align-items: center;">
      <img class="icon" src="../assets/ext_in_state.png">
      <span>Head:</span><span id="tar_head">{{ TargetHead }}</span><span>℃</span>
    </div>              
    <div class="input-container">
      <input placeholder="Enter Target Tempreture" class="input-field" type="number" onkeyup="set_nozzle_temp(event)" id="targetTemp0">
      <label for="input-field" class="input-label">Enter Tar-Temp.</label>
      <span class="input-highlight"></span>
    </div>
    <br>
    <div style="display: flex; justify-content: center; align-items: center;">
      <img class="icon" src="../assets/bed_in_state.png" >
      <span>Bed:</span><span id="tar_bed">{{ TargetBed }}</span><span>℃</span>
    </div>  
    <div class="input-container">
      <input placeholder="Enter Target Tempreture" class="input-field" type="number"  onkeyup="set_bed_temp(event)" id="targetBedTemp">
      <label for="input-field" class="input-label">Enter Tar-Temp.</label>
      <span class="input-highlight"></span>
    </div>
    <div class="filament_tb">
      <!-- <div class="panel_title">Filament</div> -->
      <button class="button_style"><img src="../assets/load.png" alt=""></button>
      <button class="button_style"><img src="../assets/stop_load.png" alt=""></button>
      <button class="button_style"><img src="../assets/unload.png" alt=""></button>
    </div>
  </div>
</template>

<script>
export default{
  data(){
    return{
      TargetHead:"200",
      TargetBed:"200",
    };
  }
}

</script>

<style>

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

</style>