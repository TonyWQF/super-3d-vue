<template>
<div>
</div>
</template>


<script>
export default{
  emits: ['upload_update'],
  methods: {
    get_status () {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/status/machine', false);
      return this.get_method(xhr)
    },

    set_temp(target, temp) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/ctrl/heat', false);
      var form_data = new FormData();
      form_data.append('target', target);
      form_data.append('temp', temp);
      return this.post_method(xhr, form_data)
    },

    set_fan(target, speed) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/ctrl/fan', false);
      var form_data = new FormData();
      form_data.append('fan', target);
      form_data.append('speed', speed);
      return this.post_method(xhr, form_data)
    },

    move_axis(axis, distance) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/ctrl/move', false);
      var form_data = new FormData();
      form_data.append('axis', axis);
      form_data.append('distance', distance);
      return this.post_method(xhr, form_data)
    },

    home_axis(axis) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/ctrl/homeaxis', false);
      var form_data = new FormData();
      form_data.append('axis', axis);
      return this.post_method(xhr, form_data)
    },

    home_all() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/ctrl/homeall', false);
      return this.get_method(xhr)
    },

    extrude(distance) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/ctrl/extrude', false);
      var form_data = new FormData();
      form_data.append('distance', distance);
      return this.post_method(xhr, form_data)
    },

    retract(distance) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/ctrl/retract', false);
      var form_data = new FormData();
      form_data.append('distance', distance);
      return this.post_method(xhr, form_data)
    },

    quick_stop() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/ctrl/quick_stop', false);
      return this.get_method(xhr)
    },

    upload_file(file) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/files/upload', true);
      var form_data = new FormData();
      form_data.append('file', file);
      return this.post_method(xhr, form_data)
    },

    upload_file_with_progress(file) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/files/upload', true);
      var form_data = new FormData();
      form_data.append('file', file);
      var file_name = file.name
      // xhr.onload = (event) => {
      //   $emit('upload_update', "complete", 0)
      // }
      xhr.upload.onprogress = (event) => {
        if(event.lengthComputable == true) {
          var progress = Math.round(event.loaded / event.total * 100)
          this.$emit('upload_update', file_name, "progress", progress)
        }
      }
      xhr.onerror = () => {
        this.$emit('upload_update', file_name, "error", 0)
      }
      xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
              this.$emit('upload_update', file_name, "complete", 0)
            }else{
              this.$emit('upload_update', file_name, "fail", 0)
            }
        }
      };
      xhr.send(form_data)
    },

    delete_file(filename) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/files/delete', false);
      var form_data = new FormData();
      form_data.append('file_name', filename);
      console.log("delete_file:"+filename);
      return this.post_method(xhr, form_data)
    },

    // {"estimated_time(s)", "nozzle_temperature(°C)", "build_plate_temperature(°C)", "layer_height", "matierial_weight:", "LAYER_COUNT:", "thumbnail:"}
    preview_file(filename) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/files/preview', false);
      var form_data = new FormData();
      form_data.append('file_name', filename);
      return this.post_method(xhr, form_data)
    },

    start_print(filename) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/files/print', false);
      var form_data = new FormData();
      form_data.append('file_name', filename);
      console.log("start_print:"+filename);
      return this.post_method(xhr, form_data)
    },

    stop_print() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/files/stop', false);
      return this.get_method(xhr)
    },

    pause_print() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/files/pause', false);
      return this.get_method(xhr)
    },

    resume_print() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/files/resume', false);
      return this.get_method(xhr)
    },

    file_list(file_list_page_index) {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/files/list?page=' + file_list_page_index + '&page_per_count=9', false);
      return this.get_method(xhr)
    },

    post_method(Req, form_data) {
      var res;
      Req.onload = function() {
        if(Req.status == 200) {
          // console.log("Post success")
          var response_text = Req.responseText;
          res = [true, response_text]
        }
        else {
          console.log("Post fail")
          res = [false, ""]
        }
      }
      Req.send(form_data);
      return res
    },

    get_method(Req) {
      var res;
      Req.onload = function() {
        if(Req.status == 200) {
          // console.log("Get success")
          var response_text = Req.responseText;
          res = [true, response_text];
        }
        else {
          console.log("Get fail")
          res = [false, ""]
        }
      }
      Req.send();
      return res
    }
  },
}

</script>

