<template>
  <div id="file_list">
    <file-list-item v-for="item in FileListItems" 
      :key="item.id"
      :id="item.id"
      :label="item.label" 
      @click="go_preview(item.label)"
    ></file-list-item>
    <preview-tab ref="PreviewTab"></preview-tab>
    <div class="filelist_op" >
      <button id="prev_filelist" class=" filelist_btn btn_style" align="center" @click="file_prev_page()">Prev.</button>
      <button id="refresh_filelist" class=" filelist_btn btn_style" align="center" @click="go_file_first_page()">Refresh</button>
      <button id="next_filelist" class=" filelist_btn btn_style" align="center" @click="file_next_page()">Next</button>
    </div> 
    <dialog-tab ref="preview_dialog" 
      :dialog_type="DialogType" 
      :title="Title"
      :hint="Hint" 
    ></dialog-tab>
  </div>
  <RequestImp ref='req' />
</template>


<script>
import { mapState } from "vuex";
import FileListItem from "./FileListItem.vue";
import PreviewTab from "./PreviewTab.vue";
import RequestImp from "./RequestImplement.vue" 

export default{
  components:{
    FileListItem,
    PreviewTab,
    RequestImp,
  },
  data(){
    return{
      DialogType:"Confirm",
      Title:"Printing",
      Hint:"Printer is printing, wait for finish...",

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
    go_preview(fileitem_name){
      if(this.$store.getters.get_now_printer_status == "PRINT_STATE_PRINTING"||
        this.$store.getters.get_now_printer_status == "PRINT_STATE_PAUSE"||
        this.$store.getters.get_now_printer_status == "PRINT_STATE_FAULT_PAUSE" ){
          this.$refs.preview_dialog.show();
        return;
      }

      if(fileitem_name != "") {
        console.log(fileitem_name);
        this.$refs.PreviewTab.show_preview(fileitem_name);
      }
    },
    file_list() {
      var result = this.$refs.req.file_list(this.file_list_page_index)
      if(result[0] == true) {
        var response_text = result[1]
        this.file_first_page = response_text.slice(1, response_text.indexOf(']'));
        this.file_names = response_text.slice(response_text.indexOf(']') + 1).split('//');

        // Clear item
        for(let item in this.FileListItems) {
          this.FileListItems[item].label = "";
        }

        if(this.file_names.length > 0) {
          for(let index in this.file_names) {
            this.FileListItems[index].label = this.file_names[index];
          }
        }
      }
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
  },
  computed:{
    ...mapState["ui_state"],
  }
}

</script>

<style>

#file_list{
    margin-top: 0.5rem;
    margin-left: 12%;
    width: 80%;
    height: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  #file_list>button {
    width: 98%;
    height: 38px;
    color: green;
    margin-top: 5px;
    margin-bottom: 5px;
    border:none;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  .filelist_btn{
    margin: auto;
    margin-top:1rem;
  }

  .filelist_op{
    margin-top: 2rem;
    width:100%
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


  
/* Phone */
@media screen and (max-width:600px){

  #file_list{
    margin-top: 1.6rem;
    width: 100%;
    height: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-left: -1.4rem;
  }

  .filelist_btn{
    margin: 1.1rem 1rem;
    width: 7rem;
    height: 35px;
  }
  .filelist_op{
    width:100%
  }

}
</style>