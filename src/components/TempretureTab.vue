<template>
  <div class="content_box" id="tempreture_tb">
    <div class="panel_title">Tempreture</div>
    <br>
    <div style="display: flex; justify-content: center; align-items: center;">
      <img class="icon" src="../assets/ext_in_state.png">
      <span>Head:</span><span id="tar_head">{{ TargetHead }}</span><span>℃</span>
    </div>              
    <div class="input-container">
      <input placeholder="Enter Target Tempreture" class="input-field" type="number" @keyup.enter="set_nozzle_temp(event)" id="targetTemp0">
      <label for="input-field" class="input-label">Enter Tar-Temp.</label>
      <span class="input-highlight"></span>
    </div>
    <br>
    <div style="display: flex; justify-content: center; align-items: center;">
      <img class="icon" src="../assets/bed_in_state.png" >
      <span>Bed:</span><span id="tar_bed">{{ TargetBed }}</span><span>℃</span>
    </div>  
    <div class="input-container">
      <input placeholder="Enter Target Tempreture" class="input-field" type="number"  @keyup.enter="set_bed_temp(event)" id="targetBedTemp">
      <label for="input-field" class="input-label">Enter Tar-Temp.</label>
      <span class="input-highlight"></span>
    </div>
    <div class="filament_tb">
      <!-- <div class="panel_title">Filament</div> -->
      <button class="btn_style">Load</button>
      <button class="btn_style">Stop</button>
      <button class="btn_style">Unload</button>
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
  },
  methods:{
    set_nozzle_temp(){
      var xhr = new XMLHttpRequest();
      var form_data = new FormData();
      xhr.open("POST", "api/ctrl/heat");
      form_data.append("target", "0");
      form_data.append("temp", document.getElementById('targetTemp0').value);
      xhr.onload = function() {
        console.log("heat success");
      }
      xhr.send(form_data);

      var tar_head = document.getElementById("tar_head");
      tar_head.innerHTML = document.getElementById('targetTemp0').value;
    },
    set_bed_temp() {
        var xhr = new XMLHttpRequest();
        var form_data = new FormData();
        xhr.open("POST", "api/ctrl/heat");
        form_data.append("target", "2");
        form_data.append("temp", document.getElementById('targetBedTemp').value);
        xhr.onload = function() {
          console.log("heat success");
        }
        xhr.send(form_data);

        var tar_bed = document.getElementById("tar_bed");
        tar_bed.innerHTML = document.getElementById('targetBedTemp').value;
      }
    }
}

</script>

<style>

.filament_tb{

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
  height: 60%;
  width: 98%;
  margin-left: -1.2rem;
  }
}

</style>