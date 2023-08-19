<template>
  <div id="file_list" class="content_box">
    <file-list-item v-for="item in FileListItems" 
      :key="item.id"
      :label="item.label" 
    ></file-list-item>
    <div>
      <button id="prev_filelist" class="button_style" align="center" @click="file_prev_page()">Prev.</button>
      <button id="refresh_filelist" class="button_style" align="center" @click="go_file_first_page()">Refresh</button>
      <button id="next_filelist" class="button_style" align="center" @click="file_next_page()">Next</button>
    </div> 
  </div>
</template>

<script>
import FileListItem from "./FileListItem.vue"

export default{
  components:{
    FileListItem,
  },
  data(){
    return{
      FileListItems:[
        {id:"fileitem-", label:"1.gcode"},
        {id:"fileitem-", label:"2.gcode"},
        {id:"fileitem-", label:"3.gcode"},
        {id:"fileitem-", label:"4.gcode"},
        {id:"fileitem-", label:"5.gcode"},
        {id:"fileitem-", label:"6.gcode"},
        {id:"fileitem-", label:"7.gcode"},
        {id:"fileitem-", label:"8.gcode"},
        {id:"fileitem-", label:"9.gcode"},
        {id:"fileitem-", label:"10.gcode"},
      ],
      file_list_page_index:0,
      file_first_page:0,
      file_names:[],

    }
  },
  methods: {
    file_list() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/files/list?page=' + this.file_list_page_index + '&page_per_count=10', true);
      xhr.onload = function() {
        if(xhr.status == 200) {
          console.log("Upload succes");
          var response_text = xhr.responseText;
          this.file_first_page = response_text.slice(1, response_text.indexOf(']'));
          this.file_names = response_text.slice(response_text.indexOf(']') + 1).split('//');

          console.log(this.file_list_page_index)
          console.log(this.file_names)

          // Clear item
          for(let item in this.FileListItems) {
            item.label = "";
          }

          if(this.file_names.length > 0) {
            for(let index in this.file_names) {
              // document.getElementById("file" + index).innerHTML = file_names[index];
              console.log(index);
              this.FileListItems[index].label = this.file_names[index];
            }
          }
          // else {

          // }
        }
      }
      xhr.send();
    },
    go_file_first_page() {
      this.file_list_page_index = 0;
      this.file_list();
    },
    file_next_page() {
      this.file_list_page_index++;
      this.file_list();
    },
    file_prev_page() {
      if(this.file_list_page_index > 0) {
        this.file_list_page_index--;
        this.file_list();
      }
    },

    // 这个函数 需要放在 上传的那个组件里
    file_upload() {
      var xhr = new XMLHttpRequest()
      xhr.open("POST", "api/files/upload", true)
      var form_data = new FormData();
      form_data.append('file',  document.getElementById('file').files[0])
      xhr.onload = function() {
        if(xhr.status == 200) {
          console.log("Upload success");
        }
      }
      xhr.send(form_data);
    },
  }
}

</script>