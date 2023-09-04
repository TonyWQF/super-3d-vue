<template>
  <div class="temp-card">
    <div class="show-card">
      <img class="tempicon" src="../assets/bed_in_state.png" alt="">
      <p class="cur-temp-style">{{BedTemp}}</p>
      <p class="tar-temp-style">/{{BedTargetTemp}}℃</p>
      <!-- <p class="label-hint-style">Bed</p> -->
    </div>
    <div class="show-card">
      <img class="tempicon" src="../assets/ext_in_state.png" alt="">
      <p class="cur-temp-style">{{NozzleTemp}}</p>
      <p class="tar-temp-style">/{{NozzleTargetTemp}}℃</p>
      <!-- <p class="label-hint-style">Head</p> -->
    </div>
  </div>
  <RequestImp ref="req" />
</template>

<script>
import { mapMutations, mapState } from 'vuex';
import RequestImp from "./RequestImplement.vue";

export default{
  components: {
    RequestImp,
  },
  created() {
    setInterval(this.get_status, 1000);
  },
  data() {
    return {
      NozzleTargetTemp:0,
      NozzleTemp: 0,
      BedTargetTemp:0,
      BedTemp: 0,
    }
  },
  methods: {
    ...mapMutations(["change_printer_status"]),
    ...mapMutations(["change_print_percent"]),
        
    get_status() {
      var retval = this.$refs.req.get_status()
      var result = retval[0]
      if(result == true) {

        var status_text = retval[1].slice(1,-1)
        // console.log(status_text)
        var status_item = status_text.split(',')
        this.NozzleTemp = status_item[1]
        this.NozzleTargetTemp = status_item[2]
        this.BedTemp = status_item[3]
        this.BedTargetTemp = status_item[4]

        // console.log("status_item[0]"+status_item[0]);
        // this.$store.commit('change_printer_status', status_item[0])
        // this.$store.commit('change_print_percent', status_item[10])
        // this.change_printer_status(status_item[0]);
        // this.change_print_percent(status_item[10]);

        var movement_operable = false
        if (this.$store.state.ui_state.printer_status== "PRINT_STATE_PRINTING") {
          console.log("NOW IS PRINTING");
          movement_operable = false
        }else if (this.$store.state.ui_state.printer_status== "PRINT_STATE_IDLE") {
          movement_operable = true 
        }

        console.log("inited");
        this.$store.dispatch('update_is_inited', true)
        this.$store.dispatch('update_movement_operable', movement_operable)
      }else{
        console.log("inited failed");
        this.$store.dispatch('update_is_inited', false)
      }
    },
  },
  computed:{
    ...mapState(['ui_state'])
  }
}
</script>

<style>
.temp-card{
  width:34rem;
  height:8rem;
  padding-top: 2rem;
  padding-right: 1.2rem;
  margin: 0;
  float: right;
  display:block;
  /* box-shadow: 0 8px 50px #23232333; */
  p{
    display: block;
  }
}
.show-card{
  float:right;
  width: 14rem;
  height: 10rem;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 1.5rem;
  grid-row-gap: 0px;
  margin-right: 1.5rem;
  padding-right: 2rem;
}
.cur-temp-style{
  font-size:28px;
  font-weight: bold;
  margin: 0;
  bottom: 0;
  left: 0;
  grid-area: 1 / 3 / 2 / 5;
  margin-left: -1.2rem;
  padding-top: 0.2rem;
  padding-right: 3rem;
}
.tar-temp-style{
  font-size: large;
  font-weight: normal;
  margin: 0;
  bottom: 0;
  right: 0;
  padding-top: 1.2rem;
  padding-right: 3rem;
  grid-area: 1 / 5 / 2 / 7;
}
.label-hint-style{
  font-size: larger;
  font-weight: bolder;
  margin: 0;
  bottom: 0;
  left: 0;
  text-align: bottom;
  grid-area: 1 / 3 / 2 / 5;
}
.tempicon {
  display: inline-block;
  width: 35px;
  height: 35px;
  top: 0;
  right: 0;
  grid-area: 1 / 1 / 2 / 3;
}


/* Phone */
@media screen and (max-width:600px){


.temp-card{
  width:100%;
  height:4rem;
  margin-top: -2rem;
  float: left;
  display:block;
  /* box-shadow: 0 8px 50px #23232333; */
  p{
    display: block;
  }
}
.show-card{
  float:right;
  width: 14rem;
  height: 10rem;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 1.5rem;
  grid-row-gap: 0px;
  margin-top: -2rem;
  padding-right: 2rem;
}

.cur-temp-style{
  font-size:28px;
  font-weight: bold;
  margin: 0;
  bottom: 0;
  left: 0;
  text-align: left;
  grid-area: 1 / 3 / 2 / 5;
  margin-left: -1.1rem;
  padding-top: 0.3rem;
  padding-right: 3rem;
}
.tar-temp-style{
  font-size: large;
  font-weight: normal;
  margin: 0;
  bottom: 0;
  right: 0;
  text-align: center;
  padding-top: 1.1rem;
  grid-area: 1 / 5 / 2 / 7;
  margin-left: -0.7rem;
}
.label-hint-style{
  font-size: larger;
  font-weight: bolder;
  margin: 0;
  bottom: 0;
  left: 0;
  text-align: bottom;
  grid-area: 1 / 3 / 2 / 5;
}
.tempicon {
  display: inline-block;
  width: 35px;
  height: 35px;
  top: 0;
  right: 0;
  grid-area: 1 / 1 / 2 / 3;
}

}


</style>