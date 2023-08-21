<template>
  <div>
    <img src="../assets/logo.png" alt="">
    <p align="center">SUPER-3D</p>
    <div  class="typing-indicator">
      <div  class="typing-circle"></div>
      <div  class="typing-circle"></div>
      <div  class="typing-circle"></div>
      <div  class="typing-shadow"></div>
      <div  class="typing-shadow"></div>
      <div  class="typing-shadow"></div>
    </div>
    <status-tab></status-tab>
  </div>
</template>

<script>
import StatusTab from './StatusTab.vue';
  export default {
    components:{
      StatusTab,
    },
    methods:{

    },
    data(){
      return{

      };
    },
  };
</script>

<style>

p{
  float: left;
  display: inline-block;
  font-size: 3.5rem;
  font-weight: bolder;
  vertical-align: middle;
}

img{
  float: left;
  width: 8rem;
  vertical-align: middle;
}

/* title area loader style */
.typing-indicator {
  float: left;
  display: inline-block;
  width: 6rem;
  height: 3rem;
  margin-top: 1rem;
  position: relative;
  align-items: center;
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


</style>