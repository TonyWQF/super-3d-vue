<template>
  <div class="temp-card">
    <div class="show-card">
      <img class="icon" src="../assets/ext_in_state.png" alt="">
      <div class="div-temp-style">
        <p class="cur-temp-style">26º</p>
        <p class="tar-temp-style">/26º</p>
      </div>
      <!-- <p class="label-hint-style">Head</p> -->
    </div>
    <div class="show-card">
      <img class="icon" src="../assets/bed_in_state.png" alt="">
      <div class="div-temp-style">
        <p class="cur-temp-style">26º</p><p class="tar-temp-style">/26º</p>
        <p class="tar-temp-style"></p>
      </div>
      <!-- <p class="label-hint-style">Bed</p> -->
    </div>
  </div>
</template>

<script>
export default{

}
</script>

<style>
.temp-card{
  /* width: 12rem;
  height: 10rem; */
  float: right;
  display: inline-block;
  /* box-shadow: 0 8px 50px #23232333; */
  
}
.show-card{
  float: left;
  width: 12rem;
  height: 8rem;
  vertical-align: middle;
  margin: 1rem;
  padding: 1rem;
  /* box-shadow: 0 8px 50px #23232333; */
}
.div-temp-style{
  width: 12rem;
  height: 4rem;
  float: left;
  margin: 0;
}

.cur-temp-style{
  font-size: larger;
  font-weight: normal;
  width: 4rem;
  height: 4rem;
  float: left;
  margin: 0;
  bottom: 0;
}
.tar-temp-style{
  font-size: larger;
  font-weight: normal;
  width: 4rem;
  height: 4rem;
  /* float: right; */
  margin: 0;
  bottom: 0;
}
.label-hint-style{
  font-size: larger;
  font-weight: normal;
  width: 8rem;
  height: 2rem;
  float: left;
  margin: 0;
}

.icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  float: right;
}



</style>