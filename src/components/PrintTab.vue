

<template>

<div class="print_process">
  <div class="panel_title">Filename</div>
  <img id="preview_show" src="../assets/Bulbasaur_0.jpg" alt="">

  <div class="print_info">
    <div style="height: 40%;">
      <div class="print_hint">Z_height:200mm</div><div class="print_hint">Print_Speed:100%</div>
      <div class="print_hint">Time:24:24:24</div><div class="print_hint">Print_flowrate:100%</div>
    </div>
    <!-- <div class="loader" style="margin-top: 10px;"></div> -->
    <div style="height: 30%;">
      <button id="btn_pause_resume" class="print_btn btn_style" @Click="toggle_resume_pause">Pause</button>
      <button id="btn_stop_print" class="print_btn btn_style">Stop</button>
    </div>
  </div>
</div>
</template>

<script>

export default{
data(){

}

}
</script>


<style>

#preview_show{
  width: 80%;
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


.loader {
  display: block;
  --height-of-loader: 4px;
  --loader-color: #0071e2;
  left: 20%;
  width: 60%;
  height: var(--height-of-loader);
  border-radius: 30px;
  background-color: rgba(0,0,0,0.2);
  position: relative;
  padding-left: 30%;
}

.loader::before {
  content: "";
  position: absolute;
  background: var(--loader-color);
  top: 0;
  left: 0;
  width: 0%;
  height: 100%;
  border-radius: 30px;
  animation: moving 1s ease-in-out infinite;
}

@keyframes moving {
  50% {
    width: 100%;
  }

  100% {
    width: 0;
    right: 0;
    left: unset;
  }
}


/* Phone */
@media screen and (max-width:600px){
  #preview_show{
  height: 50%;
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
  height: 50%;
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
  }


}


</style>