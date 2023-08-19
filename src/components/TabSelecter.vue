<template>
  <div class="tab">
    <tab-selecter-item  v-for="item in TabSelecterItems" :key="item.id"
      :label="item.label" 
      :ischecked="item.ischecked" 
      :icon="item.icon">
    </tab-selecter-item>
  </div>
</template>

<script>
import TabSelecterItem from './TabSelecterItem.vue';
import uniqueId from "lodash.uniqueid";

export default {
  components:{
    TabSelecterItem,
  },
  props:{
    // label:{required:true, type: String},
    // icon:{required:true, type: String},
    checked:{default:false, type: Boolean},
  },
  methods:{
      openCity(evt, tabName) {
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
          tabcontent[i].style.display = "none";
        }
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
          tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        document.getElementById(tabName).style.display = "block";
        evt.currentTarget.className += " active";
      }
    },
    data(){
      return{
        TabSelecterItems:[
          {id:uniqueId("tabselecteritem-"), icon:"iconfont icon-dayinji", label:"Print", ischecked:true},
          {id:uniqueId("tabselecteritem-"), icon:"iconfont icon-shangchuan", label:"Upload", ischecked:false},
          {id:uniqueId("tabselecteritem-"), icon:"iconfont icon-daohang-yonghu", label:"Remote", ischecked:false},
          {id:uniqueId("tabselecteritem-"), icon:"iconfont icon-xitongkongzhi", label:"Control", ischecked:false},
        ]
      };
    },
  };


</script>

<style>

div{
  padding: 0%;
  margin: 0;
  border: none; 
  width: 100%; 
}

.tab {
  float: left;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
  width: 30%;
  height: 60rem;
  font-size: larger;
}

</style>