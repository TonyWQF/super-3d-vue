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