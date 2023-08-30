<template>
  <div ref="sidenav" id="mySidenav" class="sidenav" v-show="visible">
    <div class="op_btn">Continue</div>
    <div class="op_btn">Stop</div>
  </div>
</template>

<script>
export default{
  data(){
    return{
      visible:false,
    }
  },
  methods:{
    openOption(){
      this.visible = true;
      this.$refs.sidenav.style.width = "95%";
    },
    closeOption(){
      this.visible = false;
      this.$refs.sidenav.style.width = "0px";
    }
  }
}
</script>



<style>

/* The side navigation menu */
.sidenav {
  float: right;
  height: 100%; /* 100% Full-height */
  width: 0; /* 0 width - change this with JavaScript */
  position: relative; /* Stay in place */
  z-index: 5; /* Stay on top */
  top: 0; /* Stay at the top */
  right: 0;
  background-color: #23232323; /* Black*/
  border: 1px solid #818181;
  overflow-x: hidden; /* Disable horizontal scroll */
  overflow-y: hidden; /* Disable horizontal scroll */
  padding: 0px; /* Place content 60px from the top */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
}

/* The navigation menu links */
.op_btn {
  float:left;
  width: 50%;
  height: 100%;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;
  text-align: center;
}

/* When you mouse over the navigation links, change their color */
.op_btn:hover {
  color: #f1f1f1;
}

/* Position and style the close button (top right corner) */
.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

</style>