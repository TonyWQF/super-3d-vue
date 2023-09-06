<template>
  <div>
    <!--    台账导入框-->
    <el-dialog :title="upload.title" :visible.sync="upload.open" width="400px" center append-to-body
      @close='handleCancle'>
      <!--      文件导入位置-->
      <el-upload ref="uploada" drag action="" :http-request="voidOne" :on-change="handlFileChange"
        :file-list="upload.fileList" :auto-upload="false">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击导入</em></div>
      </el-upload>

      <el-input v-model="filePath" clearable placeholder="请输入路径" />

      <div slot="footer">
        <el-button @click="handleCancle">取 消</el-button>
        <el-button type="primary" @click="submitFileUpload">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>


export default {
  props: ["ftpUploadFlag"],
  data() {
    return {
      // 上传参数
      upload: {
        // 标题
        title: '文件上传',
        // 台账导入框
        open: this.ftpUploadFlag,
        // 是否禁用上传
        isUploading: false,
        // 上传的文件列表
        fileList: []
      },
      // 存储路径
      filePath: "",
    }
  },

  methods: {

    // 关闭弹窗
    handleCancle() {
      this.$emit('handleFtpUpload', false);
    },

    // 不使用elementui自带的上传设置
    voidOne() {
      return
    },
    // 所选文件改变时触发
    handlFileChange(file, fileList) {
      this.upload.fileList = fileList
    },
    // 上传文件
    submitFileUpload() {
      this.upload.isUploading = true
      // 上传前校验
      // 校验是否上传文件
      if (this.upload.fileList.length <= 0) {
        this.$message.error('请先选择上传文件')
        this.upload.isUploading = false
        return
      }
      // 校验文件格式
      let whiteList = ['jpg', 'png', 'doc', 'docx', 'txt']
      this.upload.fileList.forEach(item => {
        let fileSuffix = item.raw.name.substring(item.raw.name.lastIndexOf('.') + 1)
        if (whiteList.indexOf(fileSuffix) === -1) {
          whiteList = ''
          return
        }
      })
      if (whiteList === '') {
        this.$message.error('上传文件只能是 jpg, png, doc, docx, txt 格式')
        return
      }
      // 校验是否选择了参数
      if (this.filePath === '') {
        this.$message.error('存储路径不能为空')
        return
      }
      // 定义请求参数
      let formData = new FormData()
      this.upload.fileList.forEach(item => {
        formData.append('file', item.raw)
      })
      
      var filePath = this.filePath;
      // 设置首字符是 反斜杠 /
      if (filePath.substr(0, 1) !== '/') {
        filePath = '/' + filePath;
      }

      // 把所有的 反斜杠转义一下
      var path = filePath.replace('///g', '\/');

      formData.append('filePath', path)

      uploadFtp(formData).then((res) => {

        if (res.code == 200) {
          this.$message.success('上传成功')
        }

        // this.$refs.uploada.clearFiles()
        this.upload.fileList = ''
        this.upload.isUploading = false
        // 重置参数
        this.filePath = ''
      })

      this.handleCancle();
    }
  },

  mounted() {
    console.log();
  },
}
</script>