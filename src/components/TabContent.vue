<template>
    <div :id="idString" class="tabcontent">
      <h3>{{ title }}</h3>
      <p>London is the capital city of England.</p>
    </div>
</template>

<script>
export default{
  props:{
    idString:{required:true, type:String},
    title:{required:true, type:String},
  },
  methods:{
    
  }
}
</script>