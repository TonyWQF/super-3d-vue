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
        <div class="preview_op">
          <button id="go2print" class=" preview_btn">Print</button>
          <button id="downloadfile" class=" preview_btn">Download</button>
          <button id="deletefile" class=" preview_btn">Delete</button>
        </div>
      </div>
      <div class="modal-footer">
        <h5>You can print, download, delete gcode from remote.</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  data(){
    return{
      isDisplay:false,
      preview_filename:"xxx",
    }
  },
  methods:{
    closeSpan(){
      this.isDisplay = false
    },
    show_preview(fileitem_name){
      this.isDisplay = true;
      this.preview_filename = fileitem_name;
    }
  },
  mounted(){

  }
}
</script>


<style>
/* The Modal (background) */
.modal {
  /*display: none;  Hidden by default */
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
  animation-duration: 0.4s
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
  background-color: #5cb85c;
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
  background-color: #5cb85c;
  color: white;
}

#file_name{
  font-size: large;
  width: 70%;
}
.preview_op{
  width:100%;

}

.preview_btn{
    max-width: 33.3%;
    margin-left: 1rem;
    margin-right: 1rem;
    padding-top: 0;
    padding-bottom: 0;
}

#preview_img{
  max-width: 80%;
  max-height: 80%;
  width: 50rem;
  height: 45rem;

}

</style>