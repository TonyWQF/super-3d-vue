<template>
  <div class="init_con">
    <span>Connecting to the remote printer, please wait a moment.</span>
    <circle-spinner-tab></circle-spinner-tab>
  </div>
</template>

<script>
import CircleSpinnerTab from "./CircleSpinnerTab.vue";

export default{
  components:{
    CircleSpinnerTab,
  },

}

</script>

<style>
.init_con{
  width:80%;
  position: absolute;
  top: 25%;
  left:10%;
  padding:25px;
  font-size: larger;
  box-shadow: 0 8px 50px #23232333;
}

</style>