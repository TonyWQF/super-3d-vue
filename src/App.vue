<template>
  <div id="app">
    <title-header></title-header>
    <whole-app></whole-app>
  </div>
</template>

<script>
import TitleHeader from "./components/TitleHeader.vue";
import WholeApp from "./components/WholeApp.vue"

export default {
  name: 'App',
  components:{
    TitleHeader,
    WholeApp,
  },
  data(){
    return{
      cur_main_tab:1,
    };
  },
  methods:{
    send_get(url){
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url, false);
      xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
          if(xhr.status == 200) {
            console.log("status == 200");
          }
          else {
            console.log(xhr.status)
          }
        }
        console.log(xhr.responseText)
      }
      xhr.send();
    },
    request_status() {
      var url_get_status = "api/status/machine";
      setInterval(this.send_get(url_get_status),1000);
    },
  },
  computed: {
  },
  mounted(){
    // this.request_status();
  }
}
</script>

<style>
  @media screen and (min-width: 550px) {
    .stack-small > * + * {
      margin-top: 1.4rem;
    }
    .stack-large > * + * {
      margin-top: 2.8rem;
    }
  }
  /* 全局样式结束 */
  #app {
    height: 98%;
    background: #fff;
    margin: 2rem 0 4rem 0;
    padding: 1rem;
    padding-top: 0;
    position: relative;
    box-shadow:
      0 2px 4px 0 rgba(0, 0, 0, 0.2),
      0 2.5rem 5rem 0 rgba(0, 0, 0, 0.1);
  }
  @media screen and (min-width: 550px) {
    #app {
      padding: 4rem;
    }
  }
  #app > * {
    max-width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
  #app > form {
    max-width: 100%;
    width: 100%;
  }
  #app h1 {
    display: block;
    min-width: 50%;
    width: 50%;
    text-align: left;
    float:left;
    margin: 0;
    margin-bottom: 1rem;
  }
</style>

