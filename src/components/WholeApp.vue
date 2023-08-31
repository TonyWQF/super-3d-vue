<template>
  <div class="main_container">
    <div class="content_container">
      <div class="tab">
        <button :class="{active:ui_state.now_tab==1}" @click="openTab(1)" id="1"><i class="iconfont icon-dayinji_o icon-intab"></i>Print</button>
        <button :class="{active:ui_state.now_tab==2}" @click="openTab(2)" id="2"><i class="iconfont icon-shangchuan icon-intab"></i>Upload</button>
        <button :class="{active:ui_state.now_tab==3}" @click="openTab(3)" id="3"><i class="iconfont icon-yuanduanfuzhi icon-intab"></i>Remote</button>
        <button :class="{active:ui_state.now_tab==4}" @click="openTab(4)" id="4"><i class="iconfont icon-xitongkongzhi icon-intab"></i>Control</button>
      </div>
      <div id="Print" class="tabcontent" v-if="ui_state.now_tab==1">
        <camera-tab></camera-tab>
        <print-tab></print-tab>
      </div>
      <div id="Upload" class="tabcontent" v-else-if="ui_state.now_tab==2">
        <upload-tab></upload-tab>
      </div>
      <div id="Remote" class="tabcontent " v-else-if="ui_state.now_tab==3">
        <file-list></file-list>
      </div>
      <div id="Ctrl" class="tabcontent"  v-else-if="ui_state.now_tab==4">
          <tempreture-tab></tempreture-tab>
          <movement-tab></movement-tab>
      </div> 
    </div>
  </div>
</template>

<script>
import CameraTab from './CameraTab.vue'
import PrintTab from './PrintTab.vue'
import UploadTab from './UploadTab.vue';
import FileList from './FileList.vue';
import TempretureTab from './TempretureTab.vue'
import MovementTab from './MovementTab.vue'
import { mapMutations, mapState } from 'vuex';

  export default{
    components:{
      CameraTab,
      PrintTab,
      UploadTab,
      FileList,
      TempretureTab,
      MovementTab,
    },
    data(){
      return{
        activeId:1,
        file_list_page_index: 0,
      };
    },
    methods:{
      ...mapMutations(["change_tab"]),
      openTab(id_NUM) {
        this.change_tab(id_NUM)
        this.activeId = this.$store.getters.get_now_tab;
        // console.log("openTab:"+this.$store.state.ui_state.now_tab);
      },
    },
    mounted(){

    },

    // 专门读取 vuex 数据
    computed:{      
      ...mapState(['ui_state']),
    },
  }
</script>

<style>
*{
  text-align:center;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
       box-sizing: border-box;
}

.main_container{
  float: left;
  top: 15rem;
  left: 2rem;
  position: absolute;
  margin: 0 auto;
  width: 100%; 
  height: 97%;
  color: black;
}

.content_container{
  padding-right: 1%;
  position: relative;
  border: 1px solid #ccc;
  width: 97%;
  height: 70%;
}

/* Style the tab content */
.tabcontent {
  position: absolute;
  right: 0%;
  float: left;
  padding: 0px 12px;
  /* border: 1px solid #ccc; */
  width: 70%;
  border-left: none;
  height: 97%;
}


/* phone */
@media screen and (max-width:600px){
  .content_container{
    padding-right: 1%;
    position: relative;
    border: 1px solid #ccc;
    width: 97%;
    height: 70%;
  }
  .main_container{
    float: left;
    top: 15rem;
    position: absolute;
    margin: 0 auto;
    width: 98%; 
    height: 97%;
    color: black;
  }
}


/* title area loader style */
.typing-indicator {
  width: 60px;
  height: 30px;
  position: relative;
  /* align-items: center; */
  /* z-index: 4; */
}

.typing-circle {
  width: 8px;
  height: 8px;
  position: absolute;
  border-radius: 50%;
  background-color: #000;
  left: 15%;
  transform-origin: 50%;
  animation: typing-circle7124 0.5s alternate infinite ease;
}

@keyframes typing-circle7124 {
  0% {
    top: 20px;
    height: 5px;
    border-radius: 50px 50px 25px 25px;
    transform: scaleX(1.7);
  }

  40% {
    height: 8px;
    border-radius: 50%;
    transform: scaleX(1);
  }

  100% {
    top: 0%;
  }
}

.typing-circle:nth-child(2) {
  left: 45%;
  animation-delay: 0.2s;
}

.typing-circle:nth-child(3) {
  left: auto;
  right: 15%;
  animation-delay: 0.3s;
}

.typing-shadow {
  width: 5px;
  height: 4px;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.2);
  position: absolute;
  top: 30px;
  transform-origin: 50%;
  z-index: 3;
  left: 15%;
  filter: blur(1px);
  animation: typing-shadow046 0.5s alternate infinite ease;
}

@keyframes typing-shadow046 {
  0% {
    transform: scaleX(1.5);
  }

  40% {
    transform: scaleX(1);
    opacity: 0.7;
  }

  100% {
    transform: scaleX(0.2);
    opacity: 0.4;
  }
}

.typing-shadow:nth-child(4) {
  left: 45%;
  animation-delay: 0.2s;
}

.typing-shadow:nth-child(5) {
  left: auto;
  right: 15%;
  animation-delay: 0.3s;
}

/* Style the tab */
.tab {
  position: absolute;
  float: left;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
  width: 30%;
  height: 100%;
}

/* Style the buttons inside the tab */
.tab button {
  display: block;
  background-color: inherit;
  color: black;
  padding: 22px 16px;
  width: 100%;
  border: none;
  outline: none;
  text-align: left;
  cursor: pointer;
  transition: 0.3s;
  font-size: 26px;
}

/* Change background color of buttons on hover */
.tab button:hover {
  background-color: #ddd;
}

/* Create an active/current "tab button" class */
.tab button.active {
  background-color: #ccc;
}

.print_hint{
  width: 50%;
  margin-top: 5px;
  float: left;
  font-size: large;
}


/* Add Animation */
@-webkit-keyframes slideIn {
  from {bottom: -300px; opacity: 0} 
  to {bottom: 0; opacity: 1}
}

@keyframes slideIn {
  from {bottom: -300px; opacity: 0}
  to {bottom: 0; opacity: 1}
}

@-webkit-keyframes fadeIn {
  from {opacity: 0} 
  to {opacity: 1}
}

@keyframes fadeIn {
  from {opacity: 0} 
  to {opacity: 1}
}


/* tempreture area */

.icon {
  display: inline-block;
  width: 35px;
  height: 35px
}

.content_box{
  margin: 1%;
  padding: 1%;
  float: left;
  width: 50%;
  height: 100%;
  box-shadow: 0 8px 50px #23232333;
}

/*  ctrl -> movement area style */
.temp_tb{
  float: left;
  width: 45%;
}


@media screen and (max-width:600px) {
  .content_container{
    position:relative;
    border: none;
    width: 100%;
    float:left;
  }
  .tab {
    position: absolute;
    float: left;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
    width: 100%;
    height: 80px;
    margin-left: -1.7rem;
  }
  .tab button {
    float: left;
    display: block;
    background-color: inherit;
    color: black;
    padding: 22px 16px;
    width: 25%;
    height: 100%;
    border: none;
    outline: none;
    text-align: center;
    cursor: pointer;
    transition: 0.3s;
    font-size: 20px;
  }
  .tabcontent {
    position: absolute;
    top: 80px;
    right: 0%;
    float: left;
    padding: 0px 12px;
    width: 100%;
    height: 100%;
    border-left: none;
    font-size: 20px;
  }
  .content_box{
    float: left;
    width: 98%;
    height: 50%;
  }

  .icon-intab{
    margin-top:-1rem;
    display: inline-flex;
  }
  
}




</style>