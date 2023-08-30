<template>
  <teleport class="container_dialog" to="body">
    <transition name="confirm-fade">
      <div class="confirm" v-show="visible">
        <div class="confirm-wrapper">
          <div class="confirm-content">
            <p class="title_text">{{ title }}</p>
            <p class="text">{{ hint }}</p>
            <br>
            <div class="operate" v-if="dialog_type=='YesNo'">
              <div class="operate-btn" @click="confirm">
                OK
              </div>
              <div class="operate-btn" @click="cancel">
                Cancel
              </div>
            </div>
            <div class=operate v-if="dialog_type=='Confirm'">
              <div class="operate_con" @click="confirm">
                OK
              </div>
            </div>
            <div class=operate v-if="dialog_type=='Process'">
              <div class="operate_spin">
                <circle-spinner-tab></circle-spinner-tab>
              </div>              
            </div>
          </div>
        </div>
      </div>
    </transition>
  </teleport>
</template>

<script>
import { mapState } from "vuex"
import CircleSpinnerTab from "./CircleSpinnerTab.vue"
 
export default{
  props:{
    title:{ required:true, type:String},
    hint:{required:true, type:String},
    dialog_type:{default:"YesNo", type:String},
    waitStatus:{default:"PRINT_STATE_MAX", type:String},
    waitSTick:{default:"5", type:String},
  },
  components:{
    CircleSpinnerTab,
  },
  data(){
    return{
      visible:false,
      timer:"",
      tick:0,
    }
  },
  methods:{
    confirm () {
      this.hide()
      this.$emit('confirm')
    },
    cancel () {
      this.hide()
      this.$emit('cancel')
    },
    hide () {
      this.visible = false
    },
    show () {
      this.tick = 0;
      this.timer = setInterval(this.checkStatus, 1000); // 注意: 第一个参数为方法名的时候不要加括号;
      this.visible = true
    },
    checkStatus(){
      this.tick++;

      console.log("this.tick"+this.tick);
      if(this.waitStatus == this.$store.getters.get_now_printer_status){
        this.visible = false;
        this.tick = 0;
        clearInterval(this.timer);
      }
      if(this.waitSTick > this.tick){
        this.visible = false;
        this.tick = 0;
        clearInterval(this.timer);
      }
    }
  },
  computed:{
    ...mapState["ui_state"],
  },
  emits:['confirm', 'cancel'],
}
</script>
<style>
  .confirm {
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: 996;
    background-color: rgba(0, 0, 0, 0.2);
    &.confirm-fade-enter-active {
      animation: confirm-fadein .3s;
      .confirm-content {
        animation: confirm-zoom-in .3s;
      }
    }
    &.confirm-fade-leave-active {
      animation: confirm-fadeout .3s;
      .confirm-content {
        animation: confirm-zoom-out .3s;
      }
    }
    .confirm-wrapper {
      position: absolute;
      top: 50%;
      left: 50%;
      box-shadow: 0 8px 50px #23232333;
      background-color:whitesmoke;
      transform: translate(-50%, -50%);
      z-index: 997;
      .confirm-content {
        text-align: center;
        width: 100%;
        border-radius: 2px;

        .title_text{
          width: 100%;
          line-height: 22px;
          text-align: center;
          font-size: larger;
        }
        .text {
          padding: 19px 15px;
          width: 100%;
          line-height: 22px;
          text-align: center;
          font-size: large;
          color: #4d4d4d;
        }
        .operate {
          width: 100%;
          z-index: 998;
          display: flex;
          align-items: center;
          font-size: normal;

          .operate-btn {
            width: 50%;
            line-height: 4.5rem;
            color: #4d4d4d;
            margin: 2rem;
            box-shadow: 0 8px 50px #23232333;
            
          }
          .operate_con{
            width: 50%;
            line-height: 4.5rem;
            margin-left: 25%;
            margin-right: 25%;
            margin-bottom: 2rem;
            color: #4d4d4d;
            /* border:1px solid #23232333; */
            box-shadow: 0 8px 50px #23232333;
          }
          .operate_spin{
            width: 50%;
            margin-left: 25%;
            margin-right: 25%;
          }

          .operate_con:hover,.operate-btn:hover,
          .operate_con:hover,.operate-btn:focus {
            border-color: rgba(0, 0, 0, 0.15);
            box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
            color: rgba(0, 0, 0, 0.65);
          }

          .operate_con:hover.operate-btn:focus {
          transform: translateY(-1px);
          }

          .operate_con:active, .operate-btn:active {
            background-color: #F0F0F1;
            border-color: rgba(0, 0, 0, 0.15);
            box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
            color: rgba(0, 0, 0, 0.65);
            transform: translateY(0);
          }
        }

      }
    }

    @keyframes confirm-fadein {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 1;
      }
    }

    @keyframes confirm-fadeout {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 1;
      }
    }

    @keyframes confirm-zoom-in {
      0% {
        transform: scale(0);
      }
      50% {
        transform: scale(1.1);
      }
      100% {
        transform: scale(1);
      }
    }

    @keyframes confirm-zoom-out {
      0% {
        transform: scale(1);
      }
      100% {
        transform: scale(0);
      }
    }
  }
</style>