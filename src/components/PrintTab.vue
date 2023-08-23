

<template>

<div class="print_process">
  <div class="panel_title">Filename</div>
  <img id="preview_show" src="../assets/Bulbasaur_0.jpg" alt="">

  <div class="print_info">
    <div class="print-info-con">
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
      </div>
    <!-- <div class="loader" style="margin-top: 10px;"></div> -->
    <div style="height: 30%;">
      <button v-if="isPaused==true" id="btn_resume" class="print_btn btn_style" @click="resumePrint">Resume</button>
      <button v-if="isPaused==false" id="btn_pause" class="print_btn btn_style" @click="pausePrint">Pause</button>
      <button id="btn_stop_print" class="print_btn btn_style">Stop</button>
    </div>
  </div>
</div>
</template>

<script>

export default{
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
    };
  },
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