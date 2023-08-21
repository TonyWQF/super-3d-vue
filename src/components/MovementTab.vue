<template>
  <div>
    <div class="panel_title">Movement</div>
    <div> 
      <table style="width: 100%;height: 100%;">
        <tr>
          <td><button class="button_style" onclick="move_left()">X+</button></td>
          <td><button class="button_style" onclick="move_back()">Y+</button></td>
          <td><button class="button_style" onclick="move_up()">Z+</button></td>
        </tr>
        <tr>
          <td><button class="button_style" onclick="move_right()">X-</button></td> 
          <td><button class="button_style" onclick="move_front()">Y-</button></td> 
          <td><button class="button_style" onclick="move_down()">Z-</button></td>
        </tr>
        <tr>
          <td><button class="button_style">HomeXY</button></td>
          <td><button class="button_style">HomeZ</button></td>
          <td><button class="button_style">HomeAll</button></td>
        </tr>
      </table>
    </div>
    <div class="radio-inputs" align="center" style="width: 100%; display:flex;justify-content: center; align-items:center;">
      <label class="radio">
        <input type="radio" name="radio" id="radio_1mm" checked="">
        <span class="name">1mm</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" id="radio_10mm">
        <span class="name">10mm</span>
      </label>                      
      <label class="radio">
        <input type="radio" name="radio" id="radio_50mm">
        <span class="name">50mm</span>
      </label>
    </div>
  </div> 
</template>


<script>
export default{
  data(){

  },
  methods:{

  },
}

</script>