<template>
  <button :id="id" class="file_item" @delete_file="delete_item">{{ label }}</button>
</template>

<script>
export default{
  emits:["delete_item"],
  props:{
    label:{required:true, type: String},
    id:{required:true, type: String},
  },
  data(){
    return{
      
    }
  },
  methods:{
    delete_item(){
      this.$emit("delete_item")
    }
  }
}

</script>

<style>


/* file list area style */
/* #file_list{
  padding-left: 0;
  border-radius: 5px;
} */
#file_list>button {
  font-size: large;
  width: 98%;
  height: 40px;
  color: black;
  margin:5px;
  padding-top: 12px;
  /* margin-bottom: 15px; */
  border:none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-overflow: ellipsis;
  overflow: hidden;
  word-break: break-all;
  white-space: nowrap;
}

#file_list>button:hover {
  transform: translateY(-1px);
  border: 1px solid #ccc;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
}

#file_list>button:active {
  transform: translateY(1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}


</style>