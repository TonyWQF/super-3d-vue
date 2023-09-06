<template>
  <div id="myModal" class="modal" v-if="isDisplay">
    <div class="modal-content">
      <div class="modal-header">
        <span class="close" @click="closeSpan" >&times;</span>
        <h2>Preview</h2>
      </div>
      <div class="modal-body">
        <p id="file_name">{{ preview_filename }}</p>
        <img id="preview_img" :src="icon_data=='data:image/png;base64,'?require('../assets/gcode.svg'):icon_data" alt="">
        <div class="info_con">
          <div class="preview_infolabel">
            <span>Head:</span><span>{{ preview_head }}℃</span>
          </div>
          <div class="preview_infolabel">
            <span>Bed:</span><span>{{ preview_bed }}℃</span>
          </div>
          <div class="preview_infolabel">
            <span>Layer count:</span><span>{{ preview_layercount }}</span>
          </div>
          <div class="preview_infolabel">
            <span>Time:</span><span>{{ preview_time }}</span>
          </div>
        </div>
        <div class="preview_op">
          <button id="go2print" class="preview_btn btn_style" @click="goPrint">Print</button>
          <!-- <button id="downloadfile" class="preview_btn btn_style">Download</button> -->
          <button id="deletefile" class="preview_btn btn_style" @click="deleteFile">Delete</button>
        </div>
      </div>
      <!-- <div class="modal-footer">
        <div class="hint_preview" >You can print, download, delete gcode from remote.</div>
      </div> -->
      <!-- 预览点击删除弹出界面 -->
      <dialog-tab ref="delete_dialog" 
          :dialog_type="deleteDialogType" 
          :title="DeleteFileTitle"
          :hint="deleteHint" 
          @confirm="delete_confirm"
          @cancel="cancel"
        ></dialog-tab>
    </div>
  </div>
  <RequestImp ref="req" />
</template>

<script>
import RequestImp from "./RequestImplement.vue";
import DialogTab from "./DialogTab.vue"
import { mapState } from "vuex";

export default{
  emits:["delete_file"],
  components:{
    DialogTab,
    RequestImp,
  },
  data(){
    return{
      isDisplay:false,
      preview_filename:"xxx",
      preview_time:"24:24:24",
      preview_head:200,
      preview_bed:60,
      preview_layercount:2,
      icon_data:"",

      GoPrintDialogType:"Process",   //YesNo, Confirm, Process
      GoPrintFileTitle:"Parsing File",
      GoPrintHint:"Parsing file, wait a while...",

      deleteDialogType:"YesNo",   //YesNo, Confirm, Process
      DeleteFileTitle:"Delete File",
      deleteHint:"Are you sure to delete the remote file?",
    }
  },
  methods:{
    closeSpan(){
      this.isDisplay = false
    },
    show_preview(fileitem_name){
      this.isDisplay = true;
      // {"estimated_time(s)", "nozzle_temperature(°C)", "build_plate_temperature(°C)", "layer_height", "matierial_weight:", "LAYER_COUNT:", "thumbnail:"}
      
      var retval = this.$refs.req.preview_file(fileitem_name)
      // console.log(retval);

      if(retval[0]==true){
        var res_text = retval[1].split(',')
        this.preview_filename = fileitem_name;
        var puredata = Math.round(res_text[0])
        var min = Math.floor(puredata%3600);
        this.preview_time = Math.floor(puredata/3600)+"h"+ Math.floor(min/60)+"m"+Math.floor(puredata%60)+"s";
        this.preview_head = res_text[1];
        this.preview_bed = res_text[2];
        this.preview_layercount = res_text[5];
        this.icon_data = "data:image/png;base64,"+res_text[6]

      }else{
        this.preview_filename = fileitem_name;
        this.preview_time = 0+"h"+ 0+"m"+0+"s";
        this.preview_head = 0;
        this.preview_bed = 0;
        this.preview_layercount = 0;
        this.icon_data = "data:image/png;base64,"
      }
    },

    goPrint(){
      this.startPrint()
    },

    startPrint(){
      var res=this.$refs.req.start_print(this.preview_filename)
      if(res[0]==true){
        this.closeSpan();
        this.$store.dispatch('update_now_tab', 1)
        this.$store.dispatch('update_print_preview', this.icon_data)
        this.$store.dispatch('update_print_filename', this.preview_filename)
        this.$store.dispatch('update_isGcodeInfoGet', true)
      }
      else{
        alert("error");
      }
    },
    deleteFile(){
      this.$refs.delete_dialog.show();
    },
    delete_confirm(){
      console.log("file_delete send");
      this.$refs.req.delete_file(this.preview_filename);
      this.closeSpan();
      // 刷新列表
      this.$emit('delete_file')
    },
    cancel(){
      console.log("file_delete cancel");
      this.closeSpan();
      // 刷新列表
    },
    
  },
  mounted(){

  },
  computed:{
    ...mapState(['ui_state']),
  }

}
</script>


<style>
/* The Modal (background) */
.modal {
  position: fixed; /* Stay in place */
  z-index: 8; /* Sit on top */
  left: 10%;
  top: 13rem;
  width: 80%; /* Full width */
  height: 35%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
  -webkit-animation-name: fadeIn; /* Fade in the background */
  -webkit-animation-duration: 0.4s;
  animation-name: fadeIn;
  animation-duration: 0.4s;
  text-align:center;
}

/* Modal Content */
.modal-content {
  position: fixed;
  top: 13rem;
  background-color: #fefefe;
  width: 80%;
  height: 70%;
  -webkit-animation-name: slideIn;
  -webkit-animation-duration: 0.4s;
  animation-name: slideIn;
  animation-duration: 0.4s;
  box-shadow: 0 8px 50px #23232333;
  text-align:center;
}

/* The Close Button */
.close {
  color: white;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

.modal-header {
  padding: 2px 16px;
  background-color: #60a4d1f1;
  color: white;
  height: 10%;
}

.modal-body {
  width: 100%;
  height: 70%;
  text-align: center;
  min-height:485px;
  /* max-width:953px; */

}
.modal-footer {
  height: 10%;
  padding: 2px 16px;
  background-color: #60a4d1f1;
  color: white;
}

#file_name{
  font-size: large;
  width: 100%;
  padding: 0% 10%;
  text-overflow: ellipsis;
  overflow: hidden;
  word-break: break-all;
  white-space: nowrap;
  
}
.info_con{
  position:absolute;
  width: 60%;
  height:fit-content;
  position: absolute;
  top: 75%;
  left: 50%;
  transform: translate(-50%, -40%);
}
.preview_infolabel{
  float:left;
  width:50%;
}

.preview_op{
  /* margin-top: 2rem; */
  width:80%;
  position: absolute;
  left: 10%;
  bottom: 10%;
  height: fit-content;
}

.preview_btn{
    max-width: 33.3%;
    margin-left: 1rem;
    margin-right: 1rem;
    padding-top: 1rem;
    padding-bottom: 0;
}

#preview_img{
  /* max-width: 70%; */
  max-height: 50%;
  display: block;
  width: fit-content;
  height:fit-content;
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translate(-50%, -35%);
}

/* Phone */
@media screen and (max-width:600px){


.preview_infolabel{
  float:left;
  width:50%;
  height: 2rem;
}
.hint_preview{
  height:10%;
  font-size:20px;
  margin-top: 0.5rem;
}
.preview_op{
  /* margin-top: 2rem; */
  width:80%;
  position: absolute;
  left: 10%;
  bottom: 10%;
}

.info_con{
  position:absolute;
  width: 100%;
  height:fit-content;
  position: absolute;
  top: 75%;
  left: 50%;
  transform: translate(-50%, -40%);
}

}

</style>