<template>

<div id="print_process"  class="print_tab">
  <!-- <div class="panel_title" style="height: 5%;">Printing</div> -->
  <span id="printing_filename" style="margin-top: 2%;">Filename</span>
  <br>
  <img id="preview_show" src="../assets/Bulbasaur_0.jpg" alt="">
  <div class="loader" style="margin-top: 10px;"></div>
  <div class="print_info">
    <div style="height: 40%;">
      <div class="print_hint">Z_height:200mm</div><div class="print_hint">Print_Speed:100%</div>
      <div class="print_hint">Time:24:24:24</div><div class="print_hint">Print_flowrate:100%</div>
    </div>
    <div style="height: 30%;">
      <button id="btn_pause_resume" class="print_btn button_style" @Click="toggle_resume_pause">Pause</button>
      <button id="btn_stop_print" class="print_btn button_style">Stop</button>
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


</style>