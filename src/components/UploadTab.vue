<template>
  <div class="upload_tab">
    <label  class="custum-file-upload" for="file">
      <div class="upload_icon">
      <img src="" alt="">
      </div>
      <div class="upload_text">
        <span>Click to upload file</span>
        </div>
        <input type="file" id="file" accept=".gcode" ref="filedialog" @change="file_upload()">
    </label>
  </div>
  <RequestImp ref="req" />
</template>

<script>
import RequestImp from "./RequestImplement.vue";

export default{
  components: {
    RequestImp,
  },
  methods: {
    file_upload() {
      this.$refs.req.upload_file(this.$refs.filedialog.files[0])
    }
  }
}
</script>

<style>

.upload_tab{
  margin: 1%;
  width: 98%;
  height: 99%;
  box-shadow: 0 8px 50px #23232333;
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

/* Phone */
@media screen and (max-width:600px){
.upload_tab{
  margin: 1%;
  margin-left: -1.1rem;
  /* margin-top: 1.5rem; */
  width: 98%;
  height: 100%;
  box-shadow: 0 8px 50px #23232333;
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