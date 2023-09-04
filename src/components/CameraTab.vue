<template>
<div class="camera_process">
  <div class="panel_title">Camera</div>
  <img id="camera_show" src="../assets/Bulbasaur_0.jpg" alt="">
  <div class="camera_btn">
    <button id="camera_swtich" class="btn_style">On</button>
    <button id="camera_refresh" class="btn_style">Refresh</button>
  </div>

</div>
</template>


<script>
export default{

}

</script>


<style>

/* PC */
@media screen and (min-width:972px){

  #camera_show{
    width: 80%;
    margin-top: 2%;
    margin-bottom: 2%;
    margin-left: 10%;
    margin-right: 10%;
  }

  .camera_process{
    float:left;
    margin: 1%;
    width: 48%;
    height: 98%;
    box-shadow: 0 8px 50px #23232333;
    text-align: center;
  }


  .camera_btn{
    margin-top: 2rem;
    width:100%;
    height: 35%;
  }
}

/*平板*/
@media screen and (min-width:600px) and (max-width:972px){

  #camera_show{
    width: 80%;
    margin-top: 2%;
    margin-bottom: 2%;
    margin-left: 10%;
    margin-right: 10%;
  }

  .camera_process{
    float:left;
    margin: 1%;
    width: 48%;
    height: 98%;
    box-shadow: 0 8px 50px #23232333;
    text-align: center;
  }

  .camera_btn{
    margin-top: 2rem;
    width:100%;
    height: 35%;
  }
}

/* Phone */
@media screen and (max-width:600px){
#camera_show{
  width: 70%;
  height: 70%;
  margin-top: 1%;
  margin-bottom: 2%;
  margin-left: 15%;
}

.camera_process{
  float:left;
  margin: 1%;
  width: 100%;
  height: 40%;
  box-shadow: 0 8px 50px #23232333;
  text-align: center;
  margin-left: -1.5rem;
}

.camera_btn{
  margin-top: 2rem;
  width:100%;
  height: 35%;
}

}


</style>