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
  width: 100%;
  height: 35px;
  color: green;
  margin-bottom: 15px;
  border:none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
#file_list>button:hover {
  transform: translateY(-2px);
  border: 2px solid #ccc;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
}

#file_list>button:active {
  transform: translateY(1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}


</style>