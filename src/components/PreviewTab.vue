<template>
  <div id="myModal" class="modal" v-if="isDisplay">
    <div class="modal-content">
      <div class="modal-header">
        <span class="close" @click="closeSpan" >&times;</span>
        <h2>Preview</h2>
      </div>
      <div class="modal-body">
        <img id="preview_img" src="../assets/Bulbasaur_0.jpg" alt="">
        <p id="file_name">{{ preview_filename }}</p>
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
          <br>
          <button id="go2print" class="preview_btn btn_style" @click="goPrint()">Print</button>
          <button id="downloadfile" class="preview_btn btn_style">Download</button>
          <button id="deletefile" class="preview_btn btn_style" @click="deleteFile()">Delete</button>
        </div>
      </div>
      <div class="modal-footer">
        <span class="hint_preview" >You can print, download, delete gcode from remote.</span>
      </div>
    </div>
  </div>
  <RequestImp ref="req" />
</template>

<script>
import RequestImp from "./RequestImplement.vue";

export default{
  components:{
    RequestImp,
  },
  data(){
    return{
      isDisplay:false,
      preview_filename:"xxx",
      preview_head:200,
      preview_bed:60,
      preview_layercount:2,
      preview_time:"24:24:24",
    }
  },
  methods:{
    closeSpan(){
      this.isDisplay = false
    },
    show_preview(fileitem_name){
      this.isDisplay = true;
      this.preview_filename = fileitem_name;
    },
    goPrint(){
      this.closeSpan();
      this.$store.dispatch('update_now_tab', 1)
      this.$refs.req.start_print(this.preview_filename)
    },
    deleteFile(){
      this.$refs.req.delete_file(this.preview_filename)
    }
  },
  mounted(){

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
  padding: 2px 16px;
  width: auto;
  height: 80%;
  text-align: center;
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
}
.info_con{
  width: 60%;
  margin-left:20% ;
}
.preview_infolabel{
  float:left;
  width:50%;
}

/* .preview_op{
  margin-top: 2rem;
  width:100%;
} */

.preview_btn{
    max-width: 33.3%;
    margin-left: 1rem;
    margin-right: 1rem;
    padding-top: 1rem;
    padding-bottom: 0;
}

#preview_img{
  max-width: 80%;
  max-height: 80%;
  width: 50%;
  /* height: 45%; */
  display: inline-block;
  margin-left: 25%;
}

/* Phone */
@media screen and (max-width:600px){
  #preview_img{
  max-width: 90%;
  max-height: 50%;
  width: 90%;
  /* height: 45%; */
  display: inline-block;
  margin-left: 5%;
}

.info_con{
  width: 100%;
  margin-left:0;
}
.preview_infolabel{
  float:left;
  width:50%;
}


}

</style>