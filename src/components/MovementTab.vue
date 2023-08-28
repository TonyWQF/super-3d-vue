<template>
  <div class="content_box"   id="movement_tb">
    <div class="panel_title">Movement</div>
    <br>
    <div class="move_btn_wrapper"> 
      <button class="btn_style move_btn" style="width: 98%;" onclick="move_left()">X+</button>
      <button class="btn_style move_btn" style="width: 98%;" onclick="move_back()">Y+</button>
      <button class="btn_style move_btn" style="width: 98%;" onclick="move_up()">Z+</button>

      <button class="btn_style move_btn" style="width: 98%;" onclick="move_right()">X-</button> 
      <button class="btn_style move_btn" style="width: 98%;" onclick="move_front()">Y-</button> 
      <button class="btn_style move_btn" style="width: 98%;" onclick="move_down()">Z-</button>

      <button class="btn_style move_btn" style="width: 98%;">HomeXY</button>
      <button class="btn_style move_btn" style="width: 98%;">HomeZ</button>
      <button class="btn_style move_btn" style="width: 98%;">HomeAll</button>
    </div>
    <div class="radio-inputs" align="center" style="width: 100%; display:flex;justify-content: center; align-items:center;">
      <label class="radio">
        <input type="radio" name="radio" id="radio_1mm" checked="" v-model="distance" value="1">
        <span class="name">1mm</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" id="radio_10mm" v-model="distance" value="10">
        <span class="name">10mm</span>
      </label>                      
      <label class="radio">
        <input type="radio" name="radio" id="radio_50mm" v-model="distance" value="50">
        <span class="name">50mm</span>
      </label>
    </div>
  </div> 
</template>


<script>
export default{
  data(){
    return{
      distance:10,
    }
  },
  methods:{
     move_axis(axis, distance) {
      var xhr = new XMLHttpRequest();
      var form_data = new FormData();

      xhr.open("POST", "api/ctrl/move")
      form_data.append('axis', axis)
      form_data.append('this.distance', distance)
      xhr.onload = function() {
        if(xhr.status == 200) {
          console.log("move success")
        }
      }
      xhr.send(form_data)
    },
    get_move_distance()
    {
      return this.distance;
    },
    move_left() {
      this.distance = this.get_move_distance();
      this.move_axis('X', this.distance);
    },
    move_right() {
      this.distance = this.get_move_distance();
      this.move_axis('X', -this.distance);
    },
    move_front() {
      this.distance = this.get_move_distance();
      this.move_axis('Y', this.distance);
    },
    move_back() {
      this.distance = this.get_move_distance();
      this.move_axis('Y', -this.distance);
    },
    move_up() {
      this.distance = this.get_move_distance();
      this.move_axis('Z', this.distance);
    },
    move_down() {
      this.distance = this.get_move_distance();
      this.move_axis('Z', -this.distance);
    },
  }
}

</script>

<style>


  
.radio-inputs {
  margin-top: 5px;
  position: relative;
  display: flex;text-align: center;
  flex-wrap: wrap;
  border-radius: 0.1rem;
  background-color: #EEE;
  box-sizing: border-box;
  box-shadow: 0 0 0px 1px rgba(0, 0, 0, 0.06);
  padding: 0.25rem;
  width: 300px;
  font-size: 14px;

}

.radio-inputs .radio {
  flex: 1 1 auto;
  text-align: center;
}

.radio-inputs .radio input {
  display: none;
}

.radio-inputs .radio .name {
  display: flex;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  border-radius: 0.1rem;
  border: none;
  padding: .5rem 0;
  color: rgba(51, 65, 85, 1);
  transition: all .15s ease-in-out;
}

.radio-inputs .radio input:checked + .name {
  background-color: #fff;
  font-weight: 600;
}

#movement_tb{
    margin: 1%;
    width: 48%;
    height: 100%;
    box-shadow: 0 8px 50px #23232333;
  }

  .move_btn_wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr;
  }


/* Phone */
@media screen and (max-width:600px){
#movement_tb{
    margin: 1%;
    width: 98%;
    height: 40%;
    box-shadow: 0 8px 50px #23232333;
    margin-left: -1.2rem;
  }



}

</style>