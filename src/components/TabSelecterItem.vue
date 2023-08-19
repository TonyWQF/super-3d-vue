<template>
  <div class="tab_style">
    <button :id="id" type="button" :checked="ischecked" class="button_style">
    <i :class="icon"></i>
    {{ label }}</button>
  </div>
</template>

<script>
import uniqueId from "lodash.uniqueid";

  export default{
    props:{
      label:{required:true, type: String},
      icon:{required:true, type: String},
      checked:{default: false, type: Boolean},
    },
    data(){
      return{
        ischecked: this.checked,
        id:uniqueId("tabselecteritem-"),
      };
    }
  }
</script>

<style>

.tab_style{
  width: 100%;
}

.button_style {
  display:block;
  background-color: inherit;
  color: black;
  padding: 22px 16px;
  width: 100%;
  height: 8rem;
  border: none;
  outline: none;
  text-align: left;
  cursor: pointer;
  transition: 0.3s;
  font-size: 24px;
}

/* Change background color of buttons on hover */
button:hover {
  background-color: #ddd;
}

/* Create an active/current "tab button" class */
button:active {
  background-color: #ccc;
  border:none;
}
button:focus {
  background-color: #ccc;
  border:none;
  outline: none;
}


</style>