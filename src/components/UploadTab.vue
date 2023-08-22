<template>
  <div>
    <label  class="custum-file-upload" for="file">
          <div class="upload_icon">
          <img src="" alt="">
          </div>
          <div class="upload_text">
              <span>Click to upload file</span>
              </div>
              <input type="file" id="file" onchange="file_upload()">
        </label>
  </div>
</template>

<script>
export default{
  data(){
    
  },
  methods:{

  }
}
</script>

<style>

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
  margin-left: -1.5rem;
}

}


</style>