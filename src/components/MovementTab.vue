<template>
  <div class="content_box"   id="movement_tb">
    <div class="panel_title">Movement</div>
    <div class="move_btn_wrapper"> 
      <button class="btn_style move_btn"  @click="move_left()">X+</button>
      <button class="btn_style move_btn"  @click="move_back()">Y+</button>
      <button class="btn_style move_btn"  @click="move_up()">Z+</button>

      <button class="btn_style move_btn"  @click="move_right()">X-</button> 
      <button class="btn_style move_btn"  @click="move_front()">Y-</button> 
      <button class="btn_style move_btn"  @click="move_down()">Z-</button>

      <button class="btn_style move_btn"  @click="home_xy()">HomeXY</button>
      <button class="btn_style move_btn"  @click="home_z()">HomeZ</button>
      <button class="btn_style move_btn"  @click="home_all()">HomeAll</button>
    </div>
    <div class="radio-inputs" align="center" style="width: 100%; display:flex;justify-content: center; align-items:center;">
      <label class="radio">
        <input type="radio" name="radio" id="radio_1mm" value=1 checked="" v-model=Distance>
        <span class="name">1mm</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" value=10 id="radio_10mm" v-model=Distance>
        <span class="name">10mm</span>
      </label>                      
      <label class="radio">
        <input type="radio" name="radio" value=50 id="radio_50mm" v-model=Distance>
        <span class="name">50mm</span>
      </label>
    </div>
    <!-- 点击归零弹出界面 -->
    <dialog-tab ref="home_dialog" 
      :dialog_type="DialogType" 
      :title="HomeTitle"
      :hint="HomeHint" 
      :waitStatus="HomeWaitStatus"
      :waitSTick="HomeWaitStick"
    ></dialog-tab>
  </div> 
  <RequestImp ref="req" />
</template>


<script>
import DialogTab from "./DialogTab.vue"
import RequestImp from "./RequestImplement.vue"

export default{
  components: {
    DialogTab,
    RequestImp,
  },
  data() {
    return {
      Distance: 1,

      DialogType:"Process",
      HomeTitle:"Home Aixs",
      HomeHint:"Homing axis, wait a while...",

      HomeWaitStatus:"PRINT_STATE_IDLE",
      HomeWaitStick:5,

    }
  },
  methods: {
    move_left() {
      this.$refs.req.move_axis(0, -this.Distance)
    },

    move_right() {
      this.$refs.req.move_axis(0, this.Distance)
    },

    move_back() {
      this.$refs.req.move_axis(1, -this.Distance)
    },

    move_front() {
      this.$refs.req.move_axis(1, this.Distance)
    },

    move_up() {
      this.$refs.req.move_axis(2, this.Distance)
    },

    move_down() {
      this.$refs.req.move_axis(2, -this.Distance)
    },

    home_xy() {
      this.$refs.req.home_axis((1<<0) | (1<<1));
      this.$refs.home_dialog.show();
    },

    home_z() {
      this.$refs.req.home_axis(1<<2);
      this.$refs.home_dialog.show();
    },

    home_all() {
      this.$refs.req.home_all();
      this.$refs.home_dialog.show();
    },

  }
}

</script>

<style>


  
.radio-inputs {
  margin-top: 1.6rem;
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
    margin-top: 1.6rem;

    .move_btn{
      width:30%;
      margin:0.3rem;
    }
  }

/* Phone */
@media screen and (max-width:600px){
#movement_tb{
    margin: 1%;
    width: 98%;
    height: 40%;
    box-shadow: 0 8px 50px #23232333;
    margin-left: -1.2rem;
    position: absolute;
    left: 0%;
    top: 47%;
  }



}

</style>