<template>
  <div class="upload_tab">
    <label  class="custum-file-upload" for="file">
      <div class="upload_icon">
      <img src="" alt="">
      </div>
      <div class="upload_text">
        <span>Click to upload file</span>
        </div>
        <input type="file" id="file" accept=".gcode" ref="filedialog" @change="file_upload" multiple="multiple">
    </label>
    <ul class="upload_list">
      <li v-for="item in this.$store.state.uploadList" :key="item.id">
        <upload-item :id="item.id" 
          :upload_filename="item.filename"
          :upload_percentage="item.upload_percentage"
          @confirm_delete="delete_task"
          ></upload-item>
      </li>
    </ul>
  </div>
  <RequestImp ref="req" @upload_update="uploadUpdate"/>
</template>

<script>
import UploadItem from "./UploadItem.vue";
import RequestImp from "./RequestImplement.vue";
import uniqueId from "lodash.uniqueid";
import { mapState } from "vuex";

export default{
  components: {
    UploadItem,
    RequestImp,
  },
  data(){
    return{
      // uploadList:[
      //   // {id: uniqueId("upload-item-"), filename:"xxx.gcode", upload_percentage:30},
      //   // {id: uniqueId("upload-item-"), filename:"111.gcode", upload_percentage:45},
      //   // {id: uniqueId("upload-item-"), filename:"222.gcode", upload_percentage:75},
      //   // {id: uniqueId("upload-item-"), filename:"333.gcode", upload_percentage:66},
      //   // {id: uniqueId("upload-item-"), filename:"444.gcode", upload_percentage:100},
      //   // {id: uniqueId("upload-item-"), filename:"555.gcode", upload_percentage:45},
      //   // {id: uniqueId("upload-item-"), filename:"666.gcode", upload_percentage:45},
      // ],
    }
  },
  methods: {
    uploadUpdate(file_name, state, progress){
      for (let index = 0; index < this.$store.state.uploadList.length; index++) {
        const element = this.$store.state.uploadList[index];
        console.log(element);
        if(element.filename == file_name){
          if(state=="progress"){
            element.upload_percentage = progress;
          }else if(state=="complete"){
            element.upload_percentage = "100";
            const temp = element;
            this.$store.state.uploadList.splice(index,1);
            this.$store.state.uploadList.push(temp);
          }else{
            element.upload_percentage = "error";
          }
        }
      }
      this.$store.dispatch('update_uploadList', this.$store.state.uploadList);
    },
    delete_task(file_name){
      for (let index = 0; index < this.$store.state.uploadList.length; index++) {
        const element = this.$store.state.uploadList[index];
        if(element.filename == file_name){
          this.$store.state.uploadList.splice(index,1);
        }
      }
      this.$store.dispatch('update_$store.state.uploadList', this.$store.state.uploadList);
    },
    file_upload() {
      
      for (var i=0;i<this.$refs.filedialog.files.length;i++) {

        this.$refs.req.upload_file_with_progress(this.$refs.filedialog.files[i])

        var get_id = uniqueId("upload-item-");
        var get_filename = this.$refs.filedialog.files[i].name
        var get_percent = 0

        const uploadItem = {id:get_id, filename:get_filename, upload_percentage:get_percent};
        this.$store.state.uploadList.unshift(uploadItem)

      }
      console.log(this.$store.state.uploadList)
      this.$store.dispatch('update_uploadList', this.$store.state.uploadList);
    }
  },
  computed:{
    ...mapState["uploadList"],
  }
}
</script>

<style>

.upload_tab{
  margin: 1%;
  width: 98%;
  height: 99%;
  box-shadow: 0 8px 50px #23232333;
  overflow: hidden; /*超出部分隐藏*/
  overflow-x: hidden;
  overflow-y:scroll;
}


/* upload area style */
.custum-file-upload {
  padding-left: 1%;
  height: 150px;
  /* width: 280px; */
  display: flex;
  flex-direction: column;
  align-items: space-between;
  gap: 20px;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  border: 2px dashed #cacaca;
  background-color: rgba(255, 255, 255, 1);
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0px 48px 35px -48px rgba(0,0,0,0.1);
}

.custum-file-upload .upload_icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.custum-file-upload .upload_icon svg {
  height: 80px;
  fill: rgba(75, 85, 99, 1);
}

.custum-file-upload .upload_text {
  display: flex;
  align-items: center;
  justify-content: center;
}

.custum-file-upload .upload_text span {
  font-weight: 400;
  color: rgba(75, 85, 99, 1);
}

.custum-file-upload input {
  display: none;
}


.upload_list{
  margin-top: 0;
  overflow: hidden;
  overflow-x: hidden;

}

/* Phone */
@media screen and (max-width:600px){
.upload_tab{
  margin: 1%;
  margin-left: -2.5rem;
  /* margin-top: 1.5rem; */
  width: 98%;
  height: 100%;
  box-shadow: 0 8px 50px #23232333;
  overflow: hidden; /*超出部分隐藏*/
  overflow-y:scroll;
}

.custum-file-upload {
  height: 150px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: space-between;
  gap: 20px;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  border: 2px dashed #cacaca;
  background-color: rgba(255, 255, 255, 1);
  border-radius: 10px;
  box-shadow: 0px 48px 35px -48px rgba(0,0,0,0.1);
  /* margin-left: -1.5rem; */
}

}


</style>