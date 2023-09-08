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
      var pack_index = 0;
      const pack_size = 256 * 1024;
      const totol_pack = Math.ceil(file.size / pack_size);
      var file_name = file.name;

      var file_reader = new FileReader();
      file_reader.onload = (e) => {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'api/files/upload', true);
        xhr.onload = () => {
          if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
              pack_index++;
              if(pack_index >= totol_pack) {
                console.log("Send complete")
                this.$emit('upload_update', file_name, "complete", 0);
              }
              else {
                var progress = Math.round(pack_index * pack_size / file.size * 100);
                this.$emit('upload_update', file_name, "progress", progress);
                var start = pack_index * pack_size;
                var end = file.size>=start+pack_size?start+pack_size:file.size;
                var blob = file.slice(start, end);
                file_reader.readAsArrayBuffer(blob);
              }
            }else{
              console.log(xhr.status)
              this.$emit('upload_update', file_name, "fail", 0);
            }
          }
        }
        xhr.onerror = () => {
          console.log("error")
          this.$emit('upload_update', file_name, "error", 0);
        }

        var form_data = new FormData();
        var bin_data = new Uint8Array(e.target.result);
        form_data.append('file_name', file_name);
        form_data.append('pack_size', pack_size);
        form_data.append('pack_index', pack_index);
        form_data.append('data', bin_data);

        xhr.send(form_data);
        
      }
      var first_pack_size = (file.size >= pack_size?pack_size:file.size);
      console.log("first_pack_size:" + first_pack_size)
      var blob = file.slice(0, first_pack_size);
      file_reader.readAsArrayBuffer(blob);
    },

    // {"estimated_time(s)", "nozzle_temperature(°C)", "build_plate_temperature(°C)", "layer_height", "matierial_weight:", "LAYER_COUNT:", "thumbnail:"}
    preview_file(filename) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/files/preview', false);
      var form_data = new FormData();
      form_data.append('file_name', filename);
      return this.post_method(xhr, form_data)
    },

    preview_last_file() {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", 'api/files/last_preview', false);
      return this.get_method(xhr)
    },

    start_print(filename) {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", 'api/files/print', false);
      var form_data = new FormData();
      form_data.append('file_name', filename);
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
      xhr.open("GET", 'api/files/list?page=' + file_list_page_index + '&page_per_count=10', false);
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

